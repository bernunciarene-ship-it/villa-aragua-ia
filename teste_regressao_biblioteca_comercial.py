#!/usr/bin/env python3
"""Teste de regressão da Biblioteca Comercial Recepcionista IA Villa Arágua.

Lê BIBLIOTECA_COMERCIAL_RECEPCIONISTA_IA_VILLA_ARAGUA.md direto do disco e
verifica estruturalmente os pontos críticos validados no Tema 4.24 (Partes
1 a 3) e a reclassificação canônica de C1-C4 de 05/08/2026 (propagada em
06/08/2026, conforme ARQUITETURA_DO_SISTEMA_COMERCIAL_VILLA_ARAGUA.md,
seção 5): categorias C1-C4 (C1 = atendimento simples; C2 = atendimento
comercial normal, incluindo orçamento/disponibilidade normal; C3 =
desconto/exceção/negociação sensível; C4 = conflito ou risco grave),
presença dos 22 templates comerciais, regra de não citar valor (inclusive
o café da Casa, já confirmado oficialmente), tratamento de pet como
diagnóstico, desconto como encaminhamento, disponibilidade como checagem,
correção do PC-C2-03 (cozinha completa não atribuída a Metallo/Wood),
rótulo correto do PC-C3-04 (sem "N4") e bloqueio explícito de automação
real.

Não conecta WhatsApp, Zapier, Make, API ou backend. Não altera nenhum
arquivo. Apenas lê o .md e reporta divergências no terminal.
"""

from pathlib import Path
from typing import Optional
import re
import sys

ARQUIVO = Path(__file__).parent / "BIBLIOTECA_COMERCIAL_RECEPCIONISTA_IA_VILLA_ARAGUA.md"

# Uma linha conta como "texto entregável ao hóspede" quando é uma linha de
# citação (começa com "> ") e não é uma nota de cuidado/explicação (contém
# "Cuidados"). Abordagem linha a linha, não regex multi-linha guloso, para
# evitar o mesmo tipo de falso positivo já corrigido no script operacional.


def extrair_textos_entregues(texto: str) -> str:
    linhas = []
    for linha in texto.splitlines():
        stripped = linha.strip()
        if not stripped.startswith(">"):
            continue
        if "Cuidados" in stripped:
            continue
        linhas.append(stripped)
    return "\n".join(linhas)


CODIGOS_ESPERADOS = (
    [f"PC-C1-{i:02d}" for i in range(1, 6)]
    + ["PC-C2-01", "PC-C2-02", "PC-C2-03", "PC-C2-04", "PC-C2-04-B", "PC-C2-05"]
    + [f"PC-C2-{i:02d}" for i in range(6, 11)]
    + [f"PC-C3-{i:02d}" for i in range(1, 6)]
    + ["PC-C4-06"]
)


def checar_contem(frase: str):
    def checagem(texto: str) -> Optional[str]:
        if frase not in texto:
            return f"frase esperada não encontrada: {frase!r}"
        return None

    return checagem


def checar_nao_contem(frase: str):
    def checagem(texto: str) -> Optional[str]:
        if frase in texto:
            return f"frase/termo proibido encontrado: {frase!r}"
        return None

    return checagem


def checar_nao_entregue_regex(padrao: str, descricao: str):
    regex = re.compile(padrao)

    def checagem(texto: str) -> Optional[str]:
        entregue = extrair_textos_entregues(texto)
        if regex.search(entregue):
            return f"padrão proibido encontrado em texto entregável: {descricao}"
        return None

    return checagem


def checar_todos_codigos_presentes(texto: str) -> Optional[str]:
    ausentes = [c for c in CODIGOS_ESPERADOS if c not in texto]
    if ausentes:
        return f"códigos ausentes: {', '.join(ausentes)}"
    return None


def checar_total_22_templates(texto: str) -> Optional[str]:
    # Conta só cabeçalhos reais de template ("**PC-C1-01 — Título**"), não
    # menções em texto corrido ou na tabela de equivalência de códigos
    # (seção 14), que cita de propósito os códigos antigos (ex.: PC-C4-01)
    # como registro histórico da reclassificação de 05/08/2026.
    encontrados = set(re.findall(r"\*\*(PC-C[1-4]-\d{2}(?:-B)?)\b", texto))
    esperados = set(CODIGOS_ESPERADOS)
    if encontrados != esperados:
        partes = []
        faltando = esperados - encontrados
        extras = encontrados - esperados
        if faltando:
            partes.append(f"faltando: {', '.join(sorted(faltando))}")
        if extras:
            partes.append(f"inesperados: {', '.join(sorted(extras))}")
        return "; ".join(partes)
    if len(encontrados) != 22:
        return f"total de códigos únicos é {len(encontrados)}, esperado 22"
    return None


def checar_pc_c2_03_sem_cozinha_completa(texto: str) -> Optional[str]:
    m = re.search(r"\*\*PC-C2-03.*?(?=\n\*\*PC-C2-04|\Z)", texto, re.DOTALL)
    if not m:
        return "bloco do PC-C2-03 não encontrado"
    bloco = m.group(0)
    entregue = extrair_textos_entregues(bloco)
    if "cozinha completa" in entregue:
        return "texto entregável do PC-C2-03 atribui 'cozinha completa' a Metallo/Wood"
    if "Metallo" not in bloco or "Wood" not in bloco:
        return "PC-C2-03 não menciona Metallo e Wood como esperado"
    return None


def checar_bloqueio_automacao(texto: str) -> Optional[str]:
    linha = next(
        (
            l
            for l in texto.splitlines()
            if "WhatsApp real" in l and "Zapier" in l and "Make" in l and "API" in l and "backend" in l
        ),
        None,
    )
    if linha is None:
        return "linha de bloqueio explícito de WhatsApp real/Zapier/Make/API/backend não encontrada"
    return None


CHECAGENS = [
    ("categoria C1 presente (atendimento simples)", checar_contem("### Bloco C1 — Informação de produto")),
    ("categoria C2 presente (diagnóstico e direcionamento)", checar_contem("### Bloco C2 — Diagnóstico e direcionamento")),
    (
        "categoria C2 (continuação) presente — orçamento e disponibilidade normal, não C3",
        checar_contem("### Bloco C2 (continuação) — Orçamento e disponibilidade normal"),
    ),
    (
        "categoria C3 presente (negociação ou exceção sensível, não orçamento normal)",
        checar_contem("### Bloco C3 — Negociação ou exceção sensível"),
    ),
    (
        "categoria C4 presente (conflito ou risco grave, não desconto/exceção comum)",
        checar_contem("### Bloco C4 — Conflito ou risco grave"),
    ),
    ("prefixo de templates PC-C1 presente", checar_contem("PC-C1")),
    ("prefixo de templates PC-C2 presente", checar_contem("PC-C2")),
    ("prefixo de templates PC-C3 presente", checar_contem("PC-C3")),
    ("prefixo de templates PC-C4 presente", checar_contem("PC-C4")),
    ("22 códigos de template esperados presentes", checar_todos_codigos_presentes),
    ("total de templates comerciais é exatamente 22", checar_total_22_templates),
    (
        "regra-mãe de não citar valor comercial presente",
        checar_contem("a IA não cita diária, não cita pacote, não cita taxa adicional"),
    ),
    (
        "nenhum valor em R$ (ex.: R$ 80) em texto entregável",
        checar_nao_entregue_regex(r"R\$\s?\d", "valor monetário (R$...)"),
    ),
    (
        "pet tratado como diagnóstico/checagem humana",
        checar_contem("para a equipe confirmar certinho se a acomodação escolhida atende a essa situação"),
    ),
    (
        "desconto (C3) tratado como encaminhamento, não concessão",
        checar_contem("Essa parte de valores fica com a equipe para avaliar"),
    ),
    (
        "orçamento/disponibilidade normal (C2) tratado como checagem com a equipe, não confirmação pela IA",
        checar_contem("A equipe verifica a disponibilidade certinha pra essas datas e retorna com a resposta."),
    ),
    ("PC-C2-03 revisado sem 'cozinha completa' para Metallo/Wood", checar_pc_c2_03_sem_cozinha_completa),
    (
        "PC-C3-04 usa rótulo 'C3 sensível — encaminhamento imediato para Renildo' (não mais C4)",
        checar_contem("C3 sensível — encaminhamento imediato para Renildo"),
    ),
    ("Nenhum template comercial usa rótulo 'N4' (evita confundir com emergência operacional)", checar_nao_contem("N4")),
    (
        "bloqueio explícito de WhatsApp real, Zapier, Make, API e backend",
        checar_bloqueio_automacao,
    ),
]


def main() -> int:
    if not ARQUIVO.exists():
        print(f"ERRO: arquivo não encontrado: {ARQUIVO}")
        return 1

    texto = ARQUIVO.read_text(encoding="utf-8")

    falhas = []
    print(f"Lendo: {ARQUIVO}\n")
    for nome, checagem in CHECAGENS:
        erro = checagem(texto)
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
