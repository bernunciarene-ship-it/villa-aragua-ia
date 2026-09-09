#!/usr/bin/env python3
"""Teste de regressão — regra de hóspede adicional (R$ 120 por pessoa/noite).

Motivo: em 2026-09-09 a IA cotou a CASA ARÁGUA somando "hóspede adicional:
R$ 1.320 (R$ 120 por pessoa/noite)" ao valor da casa, para o pedido
"Casa Arágua para 4 adultos de 01/12/2026 a 12/12/2026". Isso está errado.

REGRA OFICIAL (item 93 de DADOS_OFICIAIS_ATENDIMENTO_VILLA_ARAGUA.md):
- Pousada Arágua: o adicional de R$ 120,00 por pessoa/noite pode ser
  aplicado APENAS às acomodações da Pousada, dentro da capacidade máxima
  e sobre um valor-base confirmado.
- Casa Arágua Mariscal: valor por casa/período. NÃO aplicar adicional
  automático por pessoa/noite. Para 4 adultos não há cobrança de hóspede
  adicional (Casa = valor da casa + taxa de limpeza de R$ 450,00/estadia).
  Ocupação diferente / dúvida / condição especial -> validação humana.

Este script NÃO conecta WhatsApp, /api/chat, Zapier, Make, API ou backend
e NÃO altera nenhum arquivo. Ele verifica, direto do disco, que os
arquivos canônicos de atendimento e precificação carregam a regra de
forma explícita — a defesa documental que impede a IA de voltar a somar
"hóspede adicional" numa cotação da Casa. Também documenta o CONTRATO de
regressão comportamental (entradas e saídas proibidas/permitidas) para
quem for plugar o chat de produção.
"""

from pathlib import Path
from typing import Callable, Optional
import sys

RAIZ = Path(__file__).parent

# --------------------------------------------------------------------------
# Contrato de regressão comportamental (para o chat de produção / /api/chat)
# --------------------------------------------------------------------------
CASO_CASA = {
    "entrada": "Casa Arágua para 4 adultos de 01/12/2026 a 12/12/2026",
    "proibido_na_resposta": [
        "hóspede adicional",
        "hospede adicional",
        "R$ 120 por pessoa",
        "R$ 120,00 por pessoa",
        "120 por pessoa/noite",
        "pessoa adicional",
        "R$ 1.320",
    ],
    "esperado": (
        "Tratar a Casa como valor por casa/período. Se houver valor confirmado "
        "por tabela/fonte, somar apenas: valor da Casa no período + taxa de "
        "limpeza de R$ 450,00 por estadia. Sem valor confirmado, dizer que a "
        "equipe vai verificar. Nunca somar adicional por pessoa."
    ),
}

CASO_POUSADA = {
    "entrada": "Suíte Acqua para 3 pessoas",
    "permitido_na_resposta": (
        "PODE aplicar R$ 120,00 por pessoa/noite como hóspede adicional quando "
        "estiver dentro da capacidade da acomodação (Acqua = 4) e houver "
        "valor-base confirmado. Sem valor-base confirmado, encaminhar para a equipe."
    ),
}

# --------------------------------------------------------------------------
# Arquivos canônicos
# --------------------------------------------------------------------------
DADOS = "DADOS_OFICIAIS_ATENDIMENTO_VILLA_ARAGUA.md"
PROMPT = "PROMPT_RECEPCIONISTA_IA_WHATSAPP.md"
ROTEIRO = "ROTEIRO_RECEPCIONISTA_IA.md"
BIB_COM = "BIBLIOTECA_COMERCIAL_RECEPCIONISTA_IA_VILLA_ARAGUA.md"
MAPA = "MAPA_CONTROLE_ATUAL_RECEPCIONISTA_IA_VILLA_ARAGUA.md"
MATRIZ = ".claude/skills/villa-aragua-pricing-revenue/references/matriz-precos-pousada-casa.md"
PRODUTOS = ".claude/skills/villa-aragua-sales-receptionist/references/produtos-pousada-casa.md"


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


def contrato_casa() -> Optional[str]:
    """A regra documentada deve proibir explicitamente somar adicional por
    pessoa/noite na Casa (as três frases-âncora do item 93)."""
    baixo = (ler(DADOS) + "\n" + ler(PROMPT) + "\n" + ler(ROTEIRO)).lower()
    exigidos = [
        "não aplicar adicional automático de r$ 120,00 por pessoa/noite",
        "4 adultos não existe cobrança de hóspede adicional",
        "nunca calcular total final da casa usando r$ 120,00 por pessoa/noite",
    ]
    faltando = [e for e in exigidos if e not in baixo]
    return f"proibições explícitas ausentes na regra da Casa: {faltando}" if faltando else None


def contrato_pousada() -> Optional[str]:
    """Teste de controle: a regra deve permitir o adicional na Pousada,
    dentro da capacidade e com valor-base confirmado."""
    baixo = (ler(DADOS) + "\n" + ler(PROMPT) + "\n" + ler(MATRIZ)).lower()
    exigidos = ["dentro da capacidade", "valor-base confirmado", "pousada arágua"]
    faltando = [e for e in exigidos if e not in baixo]
    return f"a permissão da Pousada não está explícita: {faltando}" if faltando else None


CHECAGENS: list[tuple[str, Callable[[], Optional[str]]]] = [
    (
        "DADOS_OFICIAIS: item 93 (regra de hóspede adicional) presente",
        contem_todos(DADOS, ["| 93 |", "R$ 120,00 por pessoa/noite"]),
    ),
    (
        "DADOS_OFICIAIS: R$ 120/pessoa/noite é exclusivo da Pousada Arágua",
        contem_todos(DADOS, ["apenas às acomodações da Pousada Arágua", "não se aplica à Casa Arágua Mariscal"]),
    ),
    (
        "DADOS_OFICIAIS: Casa = valor por casa/período, sem adicional por pessoa",
        contem_todos(
            DADOS,
            [
                "valor da casa/período",
                "Não aplicar adicional automático de R$ 120,00 por pessoa/noite",
                "4 adultos não existe cobrança de hóspede adicional",
            ],
        ),
    ),
    (
        "DADOS_OFICIAIS: regra de segurança (não misturar; não confirmar sem humano)",
        contem_todos(
            DADOS,
            [
                "nunca misturar regra de preço da Pousada com regra de preço da Casa",
                "nunca calcular total final da Casa usando R$ 120,00 por pessoa/noite",
                "encaminhar para validação humana",
            ],
        ),
    ),
    (
        "PROMPT: regra de hóspede adicional (só Pousada) presente",
        contem_todos(
            PROMPT,
            ["R$ 120,00 por pessoa/noite é exclusiva das acomodações da Pousada Arágua", "não se aplica à Casa Arágua"],
        ),
    ),
    (
        "PROMPT: Casa = valor por período/casa, sem adicional automático por pessoa",
        contem_todos(PROMPT, ["valor próprio por período/casa", "não deve receber cálculo automático de adicional por pessoa"]),
    ),
    (
        "ROTEIRO: linha da tabela de regras sobre hóspede adicional presente",
        contem_todos(
            ROTEIRO,
            ["Hóspede adicional — R$ 120,00 por pessoa/noite", "exclusivo das acomodações da Pousada Arágua", "Não se aplica à Casa Arágua Mariscal"],
        ),
    ),
    (
        "ROTEIRO: resposta pronta para 'Casa Arágua para 4 adultos' sem adicional por pessoa",
        contem_todos(ROTEIRO, ["Quanto fica a Casa Arágua para 4 (ou mais) adultos?", "valor por casa/período"]),
    ),
    (
        "BIBLIOTECA_COMERCIAL: PC-C2-08 tem cuidado sobre não aplicar adicional à Casa",
        contem_todos(BIB_COM, ["exclusiva das acomodações da Pousada Arágua", "nunca aplicar à Casa Arágua Mariscal"]),
    ),
    (
        "MAPA_CONTROLE: nota de que adicional por pessoa não vale para a Casa",
        contem_todos(MAPA, ["item 93", "nunca aplicar à Casa Arágua"]),
    ),
    (
        "matriz-precos: Pousada tem regra de adicional; Casa NÃO recebe adicional por pessoa",
        contem_todos(MATRIZ, ["somente às acomodações da Pousada Arágua", "NÃO se aplica à Casa", "valor da casa/período"]),
    ),
    (
        "produtos-pousada-casa: regra de ouro inclui adicional só-Pousada",
        contem_todos(PRODUTOS, ["Adicional de hóspede (R$ 120,00 por pessoa/noite) é só da Pousada"]),
    ),
    (
        "Taxa de limpeza intacta: Casa R$ 450,00/estadia",
        contem_todos(DADOS, ["R$ 450,00 por estadia"]),
    ),
    (
        "Taxa de limpeza intacta: Pousada sem taxa separada (item 82)",
        contem_todos(DADOS, ["Não há cobrança de taxa de limpeza na Pousada Arágua"]),
    ),
    (
        "Pagamento intacto: 50% via Pix + saldo no check-in (item 91)",
        contem_todos(DADOS, ["50% do valor total via Pix no momento da confirmação da reserva"]),
    ),
    (
        "Cancelamento intacto: Pousada 7 dias / Casa 21 dias",
        contem_todos(ROTEIRO, ["mínimo 7 dias de antecedência", "mínimo 21 dias"]),
    ),
    (
        "Contrato CASA: a regra proíbe explicitamente somar adicional por pessoa na Casa",
        contrato_casa,
    ),
    (
        "Contrato POUSADA: a regra permite o adicional na Pousada dentro da capacidade e com valor-base confirmado",
        contrato_pousada,
    ),
]


def main() -> int:
    print("Teste de regressão — hóspede adicional (Casa Arágua x Pousada Arágua)\n")
    print(f"Contrato CASA    -> entrada: {CASO_CASA['entrada']!r}")
    print(f"                    resposta NÃO pode conter: {CASO_CASA['proibido_na_resposta']}")
    print(f"Contrato POUSADA -> entrada: {CASO_POUSADA['entrada']!r}")
    print("                    resposta PODE aplicar R$ 120/pessoa/noite dentro da capacidade + valor-base\n")

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
