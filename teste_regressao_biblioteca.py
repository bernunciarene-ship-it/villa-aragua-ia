#!/usr/bin/env python3
"""Teste de regressão da Biblioteca Oficial Recepcionista IA Villa Arágua.

Lê BIBLIOTECA_OFICIAL_RECEPCIONISTA_IA_VILLA_ARAGUA.md direto do disco e
verifica estruturalmente os pontos críticos já validados na Rodada 4
(Temas 4.6 a 4.21): presença dos 25 templates, dados oficiais corretos
(distâncias, política de cancelamento, cama extra, emergência), remoção
do vídeo de chegada e ausência das observações obsoletas sobre
"importação de textos antigos".

Não conecta WhatsApp, Zapier, Make, API ou backend. Apenas lê o arquivo
e reporta divergências.
"""

from pathlib import Path
from typing import Optional
import re
import sys

ARQUIVO = Path(__file__).parent / "BIBLIOTECA_OFICIAL_RECEPCIONISTA_IA_VILLA_ARAGUA.md"

# Marcadores que introduzem um bloco de texto realmente entregável ao hóspede
# (em oposição a linhas de regra/cuidado que apenas mencionam uma frase para
# explicar o que evitar). As checagens de "frase proibida no texto entregue"
# rodam só dentro desses blocos, não no documento inteiro.
MARCADORES_TEXTO_ENTREGUE = r"\*\*(?:Texto completo|Texto|Versão curta|Resposta[^:]*):\*\*"


def extrair_textos_entregues(texto: str) -> str:
    # Para no próximo marcador em negrito (outro campo, ex.: **Cuidados:**),
    # numa linha em branco, ou no fim do arquivo — o que vier primeiro. No
    # documento, campos consecutivos (Texto / Versão curta / Cuidados) não têm
    # linha em branco entre si, então não dá pra usar só "\n\n" como limite.
    blocos = re.findall(
        MARCADORES_TEXTO_ENTREGUE + r"\n(.*?)(?=\n\*\*|\n\n|\Z)", texto, re.DOTALL
    )
    return "\n".join(blocos)

CODIGOS_ESPERADOS = (
    [f"PC-N1-{i:02d}" for i in range(1, 11)]
    + [f"PC-N2-{i:02d}" for i in range(1, 4)]
    + [f"PC-N3-{i:02d}" for i in range(1, 10)]
    + [f"PC-N4-{i:02d}" for i in range(1, 4)]
)


def checar_todos_codigos_presentes(texto: str) -> Optional[str]:
    ausentes = [c for c in CODIGOS_ESPERADOS if c not in texto]
    if ausentes:
        return f"códigos ausentes: {', '.join(ausentes)}"
    return None


def checar_contem(frase: str):
    def checagem(texto: str) -> Optional[str]:
        if frase not in texto:
            return f"frase esperada não encontrada: {frase!r}"
        return None

    return checagem


def checar_nao_contem(frase: str):
    """Frase não pode aparecer em lugar nenhum do documento (ex.: observação obsoleta)."""

    def checagem(texto: str) -> Optional[str]:
        if frase in texto:
            return f"frase obsoleta/proibida encontrada: {frase!r}"
        return None

    return checagem


def checar_nao_entregue(frase: str):
    """Frase não pode aparecer dentro de um bloco de texto realmente entregável
    ao hóspede (Texto completo / Texto / Versão curta / Resposta) — pode, porém,
    ser citada em linhas de regra/cuidado explicando o que evitar."""

    def checagem(texto: str) -> Optional[str]:
        if frase in extrair_textos_entregues(texto):
            return f"frase proibida encontrada dentro de um texto entregável: {frase!r}"
        return None

    return checagem


def checar_whatsapp_bloqueado(texto: str) -> Optional[str]:
    linha = next((l for l in texto.splitlines() if "WhatsApp real" in l and "|" in l), None)
    if linha is None:
        return "linha de status do WhatsApp real não encontrada na tabela"
    if "Bloqueado" not in linha and "Não autorizado" not in linha:
        return f"status do WhatsApp real não está como bloqueado: {linha!r}"
    return None


CHECAGENS = [
    ("25 códigos de template presentes", checar_todos_codigos_presentes),
    ("distância oficial da Pousada (~130m)", checar_contem("aproximadamente 130 metros")),
    ("distância oficial da Casa (~250m)", checar_contem("aproximadamente 250 metros")),
    ("PC-N1-09 usa 'cozinha e sala integradas'", checar_contem("cozinha e sala integradas")),
    ("'cozinha equipada' não é usada em nenhum texto entregável (ajuste PC-N1-09)", checar_nao_entregue("cozinha equipada")),
    (
        "frase oficial de cama extra presente",
        checar_contem("não são itens que oferecemos como serviço padrão"),
    ),
    ("SAMU 192 presente", checar_contem("SAMU no 192")),
    ("Polícia 190 presente", checar_contem("Polícia 190")),
    ("política de cancelamento Pousada (7 dias)", checar_contem("7 dias de antecedência")),
    ("política de cancelamento Casa (21 dias)", checar_contem("21 dias de antecedência")),
    ("devolução de 90% presente", checar_contem("devolução de 90%")),
    ("vídeo de chegada não é referenciado em nenhum texto entregável (removido no Tema 4.8)", checar_nao_entregue("link_video_chegada")),
    (
        "observação obsoleta de 'importação de textos antigos' ausente",
        checar_nao_contem("Importação e conferência dos textos completos dos 21"),
    ),
    (
        "observação obsoleta de 'material carregado neste chat' ausente",
        checar_nao_contem("nem todos os textos completos aparecem no material carregado"),
    ),
    ("WhatsApp real segue bloqueado no status oficial", checar_whatsapp_bloqueado),
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
