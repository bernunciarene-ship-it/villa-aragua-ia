# CONFIGURAÇÃO DO ZAP — CARGA ÚNICA — SET 26 7SET — META ADS — VILLA ARÁGUA

Documentação operacional para montagem manual do Zap. Nenhum Zap foi criado, editado ou executado a partir deste documento — é o roteiro para montagem controlada.

---

## NOME DO ZAP

**ZAP CARGA META ADS — SET 26 7SET — VILLA ARAGUA**

---

## ETAPA 1 — TRIGGER

**App**: Webhooks by Zapier
**Evento**: Catch Hook
**Objetivo**: receber o payload validado de 25 registros (`PAYLOAD_ZAPIER_SET_26_7SET_META_ADS_VILLA_ARAGUA.json`), enviado manualmente (ou via ferramenta de teste do Webhooks by Zapier) — não a partir de nenhuma automação existente.

---

## ETAPA 2 — LOOP

**App**: Looping by Zapier
**Objetivo**: criar uma iteração para cada um dos 25 objetos do array `registros`.

Campos disponíveis em cada iteração do loop:
- `bloco`
- `anuncio`
- `variacao`
- `linha_destino`
- `foto_sugerida`
- `texto_imagem`
- `titulo`
- `texto_principal`
- `descricao`

---

## ETAPA 3 — GOOGLE SHEETS

**Ação**: Atualizar linha existente (Update Row) — **não** "Create Spreadsheet Row" / **não** "Add Row".
**Planilha**: META ADS (ID `1FK4a-58isJJEX2Xc6YuK1hvk--0-nD_7M3EvG1_gjFw`)
**Aba**: SET 26 7SET
**Linha a atualizar**: campo `linha_destino` de cada iteração do loop.

**Mapeamento exclusivo de colunas** (ver `MAPA_CELULAS_SET_26_7SET_META_ADS_VILLA_ARAGUA.md` para os endereços completos):

| Coluna da aba | Origem no payload |
|---|---|
| C — Foto sugerida | `foto_sugerida` |
| D — Texto na imagem | `texto_imagem` |
| E — TÍTULO | `titulo` |
| F — TEXTO PRINCIPAL | `texto_principal` |
| G — DESCRIÇÃO | `descricao` |

**Não mapear**: coluna A (nome do bloco), coluna B (número da variação — já preenchido na planilha), nem qualquer célula de cabeçalho de bloco/campanha.

**Não usar a aba SET 26 7SET como trigger deste Zap** — o trigger é exclusivamente o Webhook (Etapa 1).

---

## TRAVAS DE SEGURANÇA (obrigatórias, documentadas antes de qualquer teste real)

1. **Somente aba SET 26 7SET** — a ação do Google Sheets deve apontar exclusivamente para essa aba, dentro da planilha META ADS.
2. **Exatamente 25 registros** — o payload de carga completa (`PAYLOAD_ZAPIER_SET_26_7SET_META_ADS_VILLA_ARAGUA.json`) tem 25 objetos, validado nesta execução; o Zap não deve processar mais nem menos que isso.
3. **Somente os 5 anúncios do Lote 1** — POUSADA_7SET_PACOTE_DIRETO_01, POUSADA_7SET_CAFE_01, POUSADA_7SET_PISCINA_01, CASA_7SET_PISCINA_PRIVATIVA_01, CASA_7SET_CHURRASQUEIRA_01. Nenhum anúncio do Lote 2 ou pausado entra neste Zap.
4. **`linha_destino` precisa existir no mapa aprovado** (`MAPA_CELULAS_SET_26_7SET_META_ADS_VILLA_ARAGUA.md`) — linhas 7–11, 14–18, 22–26, 32–36, 39–43. Qualquer valor fora dessa lista deve travar a execução, não seguir em frente.
5. **Não alterar título de bloco ou cabeçalho** — a ação do Google Sheets escreve apenas nas colunas C a G das linhas de variação; nunca nas colunas A/B nem nas linhas de cabeçalho de bloco/campanha.
6. **Não inserir nem excluir linha** — a ação é sempre "atualizar linha existente" por número de linha, nunca "adicionar linha".
7. **Não executar automaticamente mais de uma vez** — este é um Zap de carga única; após a execução controlada da carga completa, o Zap deve ser desativado ou movido para Draft novamente, não deixado ligado com o Webhook ativo.
8. **Zap deve permanecer em Draft até o teste real controlado** (ver Etapa 7 do processo, arquivo `PAYLOAD_TESTE_1_LINHA_ZAP_META_ADS_SET_26_7SET.json`).
9. **Primeiro teste deve atualizar apenas UMA linha** — Bloco 1, Variação 1, linha 7 — nunca a carga completa de primeira.
10. **Somente após validação visual da linha 7 no Google Sheets** (conferir se caiu exatamente nas colunas C–G, sem tocar cabeçalho, sem duplicar linha) é que a carga das 25 variações pode ser autorizada.

---

## Pré-requisitos antes de montar o Zap de verdade

- Conta Zapier com acesso ao Google Sheets já conectado à planilha META ADS.
- `PAYLOAD_ZAPIER_SET_26_7SET_META_ADS_VILLA_ARAGUA.json` revisado por Renildo (ou quem for autorizar).
- `PAYLOAD_TESTE_1_LINHA_ZAP_META_ADS_SET_26_7SET.json` disparado e validado visualmente antes de qualquer carga completa.

---

## Status

Arquivo criado em 2026-07-13. Documentação operacional apenas — nenhum Zap foi criado ou executado a partir deste arquivo.
