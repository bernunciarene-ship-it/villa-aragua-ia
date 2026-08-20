# MAPA DE CÉLULAS — ABA SET 26 7SET — PLANILHA META ADS — VILLA ARÁGUA 2026

Mapeamento real de destino para o Zap de carga única. Gerado a partir da leitura direta da planilha **META ADS** no Google Drive (arquivo Google Sheets, ID `1FK4a-58isJJEX2Xc6YuK1hvk--0-nD_7M3EvG1_gjFw`), aba **SET 26 7SET**.

**Método de leitura**: export CSV literal da aba (via Google Drive), que preserva a ordem de linhas 1:1 com a planilha real — diferente da representação em linguagem natural (ferramenta que a própria documentação avisa não ter formato garantido). As 43 linhas exportadas foram conferidas uma a uma contra os 5 blocos esperados; a estrutura confere exatamente com o que o proprietário já tinha montado manualmente (mesma ordem de blocos, mesmos cabeçalhos de coluna, mesmas 5 linhas de Variação por bloco, todas hoje vazias nas colunas de copy).

**Ressalva de confiabilidade**: o export CSV do Google Drive retorna a aba ativa/principal do arquivo. Como o arquivo hoje contém a aba SET 26 7SET com essa estrutura confirmada em duas leituras independentes (leitura em linguagem natural e export CSV, ambas batendo), a leitura é considerada confiável **no estado atual** da planilha. Se o proprietário adicionar, remover ou reordenar linhas/abas antes da execução do Zap, este mapa precisa ser re-lido antes de disparar a carga.

Nenhuma célula foi alterada para gerar este mapa — leitura estritamente de consulta.

---

## Estrutura de colunas (igual para os 5 blocos)

| Coluna (planilha) | Campo |
|---|---|
| A | (nome do bloco — apenas na linha de cabeçalho do bloco; não tocar) |
| B | Variação (número 1–5, já preenchido; não tocar) |
| C | Foto sugerida |
| D | Texto na imagem |
| E | TÍTULO |
| F | TEXTO PRINCIPAL |
| G | DESCRIÇÃO |

O Zap escreve exclusivamente nas colunas **C, D, E, F, G** de cada linha de variação. Colunas A e B, linhas de cabeçalho de bloco e linhas de cabeçalho de campanha (`CAMPANHAS | Tipo de campanha | Criativos Sugeridos | Verba diária`) não são tocadas.

---

## Mapa de destino — 25 linhas

| Bloco | Anúncio | Variação | Linha Google Sheets | Foto (col. C) | Texto imagem (col. D) | Título (col. E) | Texto principal (col. F) | Descrição (col. G) |
|---|---|---|---:|---|---|---|---|---|
| BLOCO 1 — POUSADA — PACOTE DIRETO | POUSADA_7SET_PACOTE_DIRETO_01 | 1 | 7 | C7 | D7 | E7 | F7 | G7 |
| BLOCO 1 — POUSADA — PACOTE DIRETO | POUSADA_7SET_PACOTE_DIRETO_01 | 2 | 8 | C8 | D8 | E8 | F8 | G8 |
| BLOCO 1 — POUSADA — PACOTE DIRETO | POUSADA_7SET_PACOTE_DIRETO_01 | 3 | 9 | C9 | D9 | E9 | F9 | G9 |
| BLOCO 1 — POUSADA — PACOTE DIRETO | POUSADA_7SET_PACOTE_DIRETO_01 | 4 | 10 | C10 | D10 | E10 | F10 | G10 |
| BLOCO 1 — POUSADA — PACOTE DIRETO | POUSADA_7SET_PACOTE_DIRETO_01 | 5 | 11 | C11 | D11 | E11 | F11 | G11 |
| BLOCO 2 — POUSADA — CAFÉ | POUSADA_7SET_CAFE_01 | 1 | 14 | C14 | D14 | E14 | F14 | G14 |
| BLOCO 2 — POUSADA — CAFÉ | POUSADA_7SET_CAFE_01 | 2 | 15 | C15 | D15 | E15 | F15 | G15 |
| BLOCO 2 — POUSADA — CAFÉ | POUSADA_7SET_CAFE_01 | 3 | 16 | C16 | D16 | E16 | F16 | G16 |
| BLOCO 2 — POUSADA — CAFÉ | POUSADA_7SET_CAFE_01 | 4 | 17 | C17 | D17 | E17 | F17 | G17 |
| BLOCO 2 — POUSADA — CAFÉ | POUSADA_7SET_CAFE_01 | 5 | 18 | C18 | D18 | E18 | F18 | G18 |
| BLOCO 3 — POUSADA — PISCINA | POUSADA_7SET_PISCINA_01 | 1 | 22 | C22 | D22 | E22 | F22 | G22 |
| BLOCO 3 — POUSADA — PISCINA | POUSADA_7SET_PISCINA_01 | 2 | 23 | C23 | D23 | E23 | F23 | G23 |
| BLOCO 3 — POUSADA — PISCINA | POUSADA_7SET_PISCINA_01 | 3 | 24 | C24 | D24 | E24 | F24 | G24 |
| BLOCO 3 — POUSADA — PISCINA | POUSADA_7SET_PISCINA_01 | 4 | 25 | C25 | D25 | E25 | F25 | G25 |
| BLOCO 3 — POUSADA — PISCINA | POUSADA_7SET_PISCINA_01 | 5 | 26 | C26 | D26 | E26 | F26 | G26 |
| BLOCO 4 — CASA — PISCINA PRIVATIVA | CASA_7SET_PISCINA_PRIVATIVA_01 | 1 | 32 | C32 | D32 | E32 | F32 | G32 |
| BLOCO 4 — CASA — PISCINA PRIVATIVA | CASA_7SET_PISCINA_PRIVATIVA_01 | 2 | 33 | C33 | D33 | E33 | F33 | G33 |
| BLOCO 4 — CASA — PISCINA PRIVATIVA | CASA_7SET_PISCINA_PRIVATIVA_01 | 3 | 34 | C34 | D34 | E34 | F34 | G34 |
| BLOCO 4 — CASA — PISCINA PRIVATIVA | CASA_7SET_PISCINA_PRIVATIVA_01 | 4 | 35 | C35 | D35 | E35 | F35 | G35 |
| BLOCO 4 — CASA — PISCINA PRIVATIVA | CASA_7SET_PISCINA_PRIVATIVA_01 | 5 | 36 | C36 | D36 | E36 | F36 | G36 |
| BLOCO 5 — CASA — ESPAÇO INTEGRADO / CHURRASQUEIRA | CASA_7SET_CHURRASQUEIRA_01 | 1 | 39 | C39 | D39 | E39 | F39 | G39 |
| BLOCO 5 — CASA — ESPAÇO INTEGRADO / CHURRASQUEIRA | CASA_7SET_CHURRASQUEIRA_01 | 2 | 40 | C40 | D40 | E40 | F40 | G40 |
| BLOCO 5 — CASA — ESPAÇO INTEGRADO / CHURRASQUEIRA | CASA_7SET_CHURRASQUEIRA_01 | 3 | 41 | C41 | D41 | E41 | F41 | G41 |
| BLOCO 5 — CASA — ESPAÇO INTEGRADO / CHURRASQUEIRA | CASA_7SET_CHURRASQUEIRA_01 | 4 | 42 | C42 | D42 | E42 | F42 | G42 |
| BLOCO 5 — CASA — ESPAÇO INTEGRADO / CHURRASQUEIRA | CASA_7SET_CHURRASQUEIRA_01 | 5 | 43 | C43 | D43 | E43 | F43 | G43 |

---

## Linhas que NÃO devem ser tocadas (referência, para conferência visual)

| Linha | Conteúdo |
|---|---|
| 1 | Título geral: "SETEMBRO 2026 \| 7 DE SETEMBRO" |
| 3–4 | Cabeçalho de campanha "POUSADA — 7 SETEMBRO" |
| 6 | Cabeçalho de colunas do Bloco 1 |
| 12–13 | Linha em branco + cabeçalho de colunas do Bloco 2 |
| 19–21 | Linhas em branco + cabeçalho de colunas do Bloco 3 |
| 27–29 | Linha em branco + cabeçalho de campanha "CASA — 7 SETEMBRO" |
| 31 | Cabeçalho de colunas do Bloco 4 |
| 37–38 | Linha em branco + cabeçalho de colunas do Bloco 5 |

---

## Status

Arquivo criado em 2026-07-13, a partir de leitura real (não presumida) da aba SET 26 7SET via export CSV do Google Drive. 25 linhas de mapeamento, cobrindo exatamente os 5 blocos do Lote 1. Nenhuma célula foi alterada.
