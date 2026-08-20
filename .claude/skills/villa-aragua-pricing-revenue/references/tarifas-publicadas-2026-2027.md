# Tarifas publicadas — agosto/2026 a abril/2027

**Adicionado em:** 2026-07-24, a partir do pacote de Revenue Management de Renildo.
**Proveniência:** valores transcritos visualmente de prints do Stays/Arágua — **não confirmados no sistema**. Trate como "preço publicado a confirmar", uma categoria abaixo de "preço aprovado" na tabela de `matriz-precos-pousada-casa.md`.
**Fonte completa:** `INVENTARIO_TARIFAS_PUBLICADAS_AGO2026_ABR2027.md` (legível, agrupado por régua) e `INVENTARIO_TARIFAS_PUBLICADAS_AGO2026_ABR2027.csv` (machine-readable, 162 linhas) na raiz do projeto. Diagnóstico completo em `DIAGNOSTICO_PRELIMINAR_REVENUE_VILLA_ARAGUA.md`.

Este arquivo resolve, **parcialmente e com ressalva**, a pendência registrada em `calendario-sazonalidade.md` e `SKILL.md` de que "não existe diária diferenciada por temporada" — ela existe, está publicada no Stays, só não foi confirmada linha a linha nesta rodada.

## Régua de preço da Pousada (do mais barato ao mais caro)

1. **Organic / Fuego / Metallo** — grupo base
2. **Terra / Wood** — premium intermediária (Wood sempre segue Terra)
3. **Acqua** — superior
4. **Luna** — superior, acima de Acqua
5. **Duplex Soleil** — topo da Pousada

A Casa Arágua **não entra nessa escada** — é produto próprio (ver abaixo).

## Como usar isto ao responder sobre preço

1. Identificar produto (Pousada ou Casa) e acomodação → localizar o grupo/régua correspondente.
2. Identificar o período no calendário do inventário (baixa, retomada, média, pré-temporada, feriado, feriado forte, Natal, Réveillon, alta temporada, Carnaval, pós-temporada, Páscoa).
3. Buscar o valor e o mínimo de noites publicados para esse produto+período no inventário.
4. Antes de comunicar esse valor a um hóspede: é **preço publicado a confirmar**, não preço aprovado — sinalizar isso internamente e, se for uma resposta comercial, seguir `regras-desconto.md` e `comunicacao-preco-whatsapp.md` normalmente (nunca afirmar um valor como fechado sem checagem da equipe).
5. Se o período cair em uma das linhas sinalizadas como `corrigir agora` ou `não mexer se reservado` abaixo, tratar com atenção redobrada antes de qualquer resposta.

## Regra Casa Arágua x Duplex Soleil (sugerida, não aprovada)

Em datas fortes (Réveillon, janeiro, Carnaval, Semana Santa/Páscoa, feriados prolongados, Natal, alta temporada), a Casa Arágua deveria valer mais que o Duplex Soleil — hoje isso nem sempre acontece no inventário publicado (ver `DIAGNOSTICO_PRELIMINAR_REVENUE_VILLA_ARAGUA.md`, alertas 2 e 3). Até Renildo validar esta regra:

- não citar a diária da Casa como se fosse necessariamente maior que a do Duplex;
- não tratar o valor publicado da Casa como piso definitivo — ele pode subir após revisão.

## Pontos já sinalizados como possível erro de régua (não afirmar valor sem checar)

- **Semana Santa/Páscoa 2027**, todas as acomodações da Pousada: tarifa aparece **abaixo** da tarifa base de março do mesmo produto — provável erro de régua, marcado `corrigir agora`.
- **Réveillon 2026** e **janeiro 2027 (dias 1-3)** da Casa Arágua: aparecem como já reservados no print — não usar esses valores como referência de venda para as mesmas datas de anos futuros sem confirmar; tratar como aprendizado, não como tarifa a repetir.

## Atualização de pendência em `SKILL.md`

A pendência "diária diferenciada por baixa/média/alta temporada e por feriado específico — ainda a definir" passa a ser: **publicada no Stays para o período ago/2026–abr/2027, pendente apenas de confirmação direta no sistema** antes de ser tratada como preço aprovado.
