#!/usr/bin/env python3
"""Teste de regressão — distância da praia e handoff/WhatsApp redundante.

Motivo: em 2026-09-09, em teste real do chat, à pergunta "Qual a distância
do mar?" a IA respondeu "A distância exata do mar não está registrada no
nosso painel..." e ainda reenviou o WhatsApp (47) 99201-4117, mesmo o
hóspede já estando no atendimento. As duas coisas estão erradas.

REGRA OFICIAL:
- Villa Arágua / Pousada Arágua: ~130 m da Praia de Mariscal (itens 1 e 94
  de DADOS_OFICIAIS_ATENDIMENTO_VILLA_ARAGUA.md). A IA responde direto.
  Nunca dizer que "não está registrada". Nunca "frente ao mar", "pé na
  areia", "vista para o mar".
- Casa Arágua Mariscal: ~250 m (item 2). Usar só quando a pergunta for
  especificamente sobre a Casa; o antigo "~180 m" foi revogado.
- Pergunta genérica ("Villa Arágua", "Pousada Arágua", "distância do mar")
  usa a distância da Pousada (~130 m).
- Handoff (item 92): em canal oficial já iniciado, a IA não reenvia o
  WhatsApp ao encaminhar para a equipe — encaminha "por aqui".

Este script NÃO conecta o chat de produção e NÃO altera arquivos. Verifica
que os arquivos canônicos carregam a regra de forma explícita e documenta
o contrato de regressão comportamental para o chat de produção.
"""

from pathlib import Path
from typing import Callable, Optional
import sys

RAIZ = Path(__file__).parent

# --------------------------------------------------------------------------
# Contrato de regressão comportamental (para o chat de produção / /api/chat)
# --------------------------------------------------------------------------
CASO_DISTANCIA = {
    "entrada": "Qual a distância do mar?",
    "deve_conter_um_de": ["aproximadamente 130m", "aproximadamente 130 m", "cerca de 130m", "cerca de 130 m"],
    "deve_conter": ["Praia de Mariscal"],
    "proibido": [
        "distância exata não está registrada",
        "não está registrada no painel",
        "não está registrada no nosso painel",
        "não consta no painel",
        "fale pelo WhatsApp",
        "(47) 99201-4117",
        "47 99201-4117",
        "frente ao mar",
        "frente-mar",
        "pé na areia",
        "vista para o mar",
    ],
}

CASO_HANDOFF = {
    "entrada": "Quero falar com a equipe.",
    "proibido_em_canal_oficial": ["(47) 99201-4117", "47 99201-4117", "entre em contato pelo WhatsApp"],
    "esperado": (
        "Encaminhar para a equipe atender no próprio canal: "
        '"Claro 😊 Vou encaminhar sua conversa para nossa equipe te atender por aqui." '
        'ou "Nossa equipe pode te ajudar por aqui." — sem reenviar o número.'
    ),
}

# --------------------------------------------------------------------------
# Arquivos canônicos
# --------------------------------------------------------------------------
DADOS = "DADOS_OFICIAIS_ATENDIMENTO_VILLA_ARAGUA.md"
PROMPT = "PROMPT_RECEPCIONISTA_IA_WHATSAPP.md"
ROTEIRO = "ROTEIRO_RECEPCIONISTA_IA.md"
BIB_OFICIAL = "BIBLIOTECA_OFICIAL_RECEPCIONISTA_IA_VILLA_ARAGUA.md"
RESP_WPP = ".claude/skills/villa-aragua-sales-receptionist/references/respostas-whatsapp.md"


def ler(rel: str) -> str:
    return (RAIZ / rel).read_text(encoding="utf-8")


def contem_todos(rel: str, trechos: list[str]) -> Callable[[], Optional[str]]:
    def checagem() -> Optional[str]:
        try:
            baixo = ler(rel).lower()
        except FileNotFoundError:
            return f"arquivo não encontrado: {rel}"
        faltando = [t for t in trechos if t.lower() not in baixo]
        return f"{rel}: trechos ausentes -> {faltando}" if faltando else None

    return checagem


def distancia_e_dado_oficial() -> Optional[str]:
    """A regra tem de dizer, em texto, que a distância é dado oficial e que a
    IA NÃO deve responder 'não está registrada'."""
    baixo = (ler(DADOS) + "\n" + ler(PROMPT) + "\n" + ler(ROTEIRO) + "\n" + ler(BIB_OFICIAL)).lower()
    exigidos = [
        "aproximadamente 130 m da praia de mariscal",
        'nunca dizer que a distância "não está registrada"',
    ]
    # a segunda âncora aparece com aspas curvas em alguns arquivos; aceitar variação
    tem_registrada = (
        'nunca dizer que a distância "não está registrada"' in baixo
        or "não está registrada" in baixo
        and "dado oficial" in baixo
    )
    faltando = []
    if "aproximadamente 130 m da praia de mariscal" not in baixo:
        faltando.append("frase padrão dos 130 m")
    if not tem_registrada:
        faltando.append('proibição de "não está registrada"')
    return f"regra de distância incompleta: {faltando}" if faltando else None


def nunca_frente_mar() -> Optional[str]:
    baixo = (ler(DADOS) + "\n" + ler(PROMPT) + "\n" + ler(ROTEIRO)).lower()
    exigidos = ["frente ao mar", "pé na areia", "vista para o mar"]
    faltando = [e for e in exigidos if e not in baixo]
    return f"termos proibidos não listados como proibidos: {faltando}" if faltando else None


def casa_nunca_180() -> Optional[str]:
    baixo = (ler(DADOS) + "\n" + ler(ROTEIRO)).lower()
    if "250" not in baixo:
        return "distância da Casa (~250 m) ausente"
    if "180" not in baixo:
        return 'guarda contra o antigo "~180 m" da Casa ausente'
    return None


def handoff_sem_whatsapp_em_canal_oficial() -> Optional[str]:
    baixo = (ler(PROMPT) + "\n" + ler(ROTEIRO) + "\n" + ler(DADOS)).lower()
    exigidos = [
        "vou encaminhar sua conversa para nossa equipe te atender por aqui",
        "não repete o número",
    ]
    faltando = [e for e in exigidos if e not in baixo]
    # reforço específico deste caso: fallback + WhatsApp
    if "respostas de fallback" not in baixo:
        faltando.append("reforço sobre respostas de fallback e WhatsApp")
    return f"regra de handoff incompleta: {faltando}" if faltando else None


CHECAGENS: list[tuple[str, Callable[[], Optional[str]]]] = [
    (
        "DADOS_OFICIAIS: item 94 (regra de resposta sobre distância) presente",
        contem_todos(DADOS, ["| 94 |", "distância da praia / do mar", "não está registrada"]),
    ),
    (
        "DADOS_OFICIAIS: distâncias oficiais mantidas (Pousada ~130 m / Casa ~250 m)",
        contem_todos(DADOS, ["Aproximadamente 130 metros", "Aproximadamente 250 metros"]),
    ),
    (
        "PROMPT: regra de resposta sobre distância presente na seção de dados oficiais",
        contem_todos(PROMPT, ["Regra de resposta sobre distância da praia / do mar", "item 94", 'não está registrada"']),
    ),
    (
        "PROMPT: reforço de fallback sem reenviar WhatsApp em canal oficial",
        contem_todos(PROMPT, ["Respostas de fallback", "não** devem ser seguidas do número do WhatsApp"]),
    ),
    (
        "ROTEIRO: resposta pronta para 'Qual a distância do mar?' presente",
        contem_todos(ROTEIRO, ["Qual a distância do mar?", "aproximadamente 130 m da Praia de Mariscal"]),
    ),
    (
        "ROTEIRO: linhas da tabela de regras reforçadas (dado oficial, não misturar produtos)",
        contem_todos(ROTEIRO, ["Dado oficial (itens 1 e 94)", "Dado oficial (itens 2 e 94)"]),
    ),
    (
        "ROTEIRO: seção 16C com reforço de fallback dentro de canal oficial",
        contem_todos(ROTEIRO, ["Respostas de fallback dentro de canal oficial"]),
    ),
    (
        "BIBLIOTECA_OFICIAL: PC-N1-10 cobre 'qual a distância do mar' e proíbe 'não está registrada'",
        contem_todos(BIB_OFICIAL, ["qual a distância do mar", '"não está registrada"', "Resposta rápida"]),
    ),
    (
        "respostas-whatsapp (skill): linha de distância do mar/da praia com a regra",
        contem_todos(RESP_WPP, ["Distância do mar / da praia", "nunca** dizer que \"não está registrada\""]),
    ),
    ("Contrato: distância é dado oficial e a IA responde direto", distancia_e_dado_oficial),
    ("Contrato: termos proibidos (frente ao mar / pé na areia / vista para o mar) listados", nunca_frente_mar),
    ("Contrato: Casa = ~250 m e nunca ~180 m", casa_nunca_180),
    ("Contrato: handoff em canal oficial não reenvia o WhatsApp (inclui fallback)", handoff_sem_whatsapp_em_canal_oficial),
    # regras que NÃO podem ter sido tocadas
    ("Intacto: taxa de limpeza Casa R$ 450,00/estadia", contem_todos(DADOS, ["R$ 450,00 por estadia"])),
    ("Intacto: hóspede adicional R$ 120 só na Pousada (item 93)", contem_todos(DADOS, ["| 93 |", "apenas às acomodações da Pousada Arágua"])),
    ("Intacto: pagamento 50% Pix + saldo no check-in (item 91)", contem_todos(DADOS, ["50% do valor total via Pix no momento da confirmação da reserva"])),
    ("Intacto: cancelamento Pousada 7 dias / Casa 21 dias", contem_todos(ROTEIRO, ["mínimo 7 dias de antecedência", "mínimo 21 dias"])),
]


def main() -> int:
    print("Teste de regressão — distância da praia / do mar e handoff\n")
    print(f"Contrato DISTÂNCIA -> entrada: {CASO_DISTANCIA['entrada']!r}")
    print(f"   deve conter um de: {CASO_DISTANCIA['deve_conter_um_de']} + {CASO_DISTANCIA['deve_conter']}")
    print(f"   proibido: {CASO_DISTANCIA['proibido']}")
    print(f"Contrato HANDOFF   -> entrada: {CASO_HANDOFF['entrada']!r}")
    print(f"   proibido em canal oficial: {CASO_HANDOFF['proibido_em_canal_oficial']}\n")

    falhas = []
    for nome, checagem in CHECAGENS:
        try:
            erro = checagem()
        except FileNotFoundError as e:
            erro = f"arquivo não encontrado: {e}"
        status = "FALHOU" if erro else "OK"
        print(f"[{status}] {nome}")
        if erro:
            print(f"         -> {erro}")
            falhas.append(nome)

    print()
    if falhas:
        print(f"RESULTADO: {len(falhas)}/{len(CHECAGENS)} checagens falharam.")
        return 1
    print(f"RESULTADO: {len(CHECAGENS)}/{len(CHECAGENS)} checagens aprovadas. Nenhuma falha encontrada.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
