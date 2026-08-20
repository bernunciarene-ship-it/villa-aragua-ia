# RELATÓRIO VISUAL — RADAR DE CONCORRÊNCIA REVENUE — POUSADA ARÁGUA (JANEIRO 2027)

**Objetivo:** separar o posicionamento da Pousada Arágua em três blocos de janeiro/2027 — (1) primeira quinzena, historicamente de mais procura e alta ocupação; (2) semana intermediária; (3) última semana, historicamente de procura potencialmente mais baixa.

**Rodadas cobertas:**
- Rodada 9A — Janeiro alta/início, 03–10/01/2027 (7 noites)
- Rodada 9B — Janeiro alta/primeira quinzena, 10–17/01/2027 (7 noites)
- Rodada 9C — Janeiro intermediário, 17–24/01/2027 (7 noites)
- Rodada 9D — Última semana de janeiro, 24–31/01/2027 (7 noites)

**Produto Villa de referência:** Pousada Arágua — unidade base (Organic/Fuego/Metallo) · perfil casal (2 adultos, 0 crianças, 1 acomodação)
**Fontes:** `COLETAS_CONCORRENCIA_REVENUE.csv`, `CESTA_COMPETITIVA_REVENUE_VILLA_ARAGUA.md`, `ALERTAS_CONCORRENCIA_REVENUE.md`, `REGRAS_CONVERSAO_OTA_MOTOR_REVENUE.md`, `INVENTARIO_TARIFAS_PUBLICADAS_AGO2026_ABR2027.csv`
**Coleta:** 2026-07-26, via Booking (Claude in Chrome), preços públicos visíveis, sem login, sem clicar em reservar.
**Diagnóstico:** gerado via agente `villa-precificacao-calendario`, com consulta às skills `villa-aragua-pricing-revenue` e `villa-aragua-growth-marketer` — agente acionado de fato, cálculo do período Villa verificado de forma independente pelo agente (bateu com o cálculo preliminar).
**Status deste relatório:** `RELATORIO_ANALITICO_SEM_ALTERACAO_TARIFARIA` — todos os diagnósticos abaixo são **preliminares**. Renildo decide.

**Buckets do inventário usados no cálculo do período Villa (motor):** "Janeiro/2027 1-3" = R$ 1.337,00 (mín. 7/4, "mínimos variam no print; confirmar no sistema") · "Janeiro/2027 4-31" = R$ 1.070,00 (mín. 4, manter). Conversão Booking = motor × 1,25 (`REGRAS_CONVERSAO_OTA_MOTOR_REVENUE.md`).

**Achado estrutural confirmado pelo agente:** o inventário publicado não fragmenta o bucket "Janeiro 4-31" por semana — por isso a tarifa motor da Villa é **rigorosamente idêntica** nas rodadas 9B, 9C e 9D (R$ 1.070,00/diária). Qualquer diferença de posicionamento entre "primeira quinzena", "semana intermediária" e "última semana" vem inteiramente do comportamento da concorrência, não de variação própria da Villa.

---

## RODADA 9A — Janeiro alta/início, 03–10/01/2027 (7 noites)

### 1. Tabela aberta — concorrentes

| Grupo | Concorrente | Acomodação âncora | Status | Preço total Booking | Diária média Booking | Motor equivalente médio | Dif. R$ vs. diária média Villa motor | Dif. % vs. Villa motor | Observação |
|---|---|---|---|---|---|---|---|---|---|
| NUCLEO | Vila Maciel | Apartamento Standard | COLETADO_COM_SUCESSO | R$ 4.734,00 (10% off; original R$ 5.260,00) | R$ 676,29 | R$ 541,03 | −R$ 567,11 | −51,2% | Desconto promocional ativo |
| NUCLEO | Pousada Kaloa Eco Village | Suíte Standard | COLETADO_COM_SUCESSO | R$ 6.087,00 | R$ 869,57 | R$ 695,66 | −R$ 412,48 | −37,2% | — |
| NUCLEO | Pousada dos Ingleses | Quarto Duplo Clássico | COLETADO_COM_SUCESSO | R$ 6.464,00 + R$ 120,00 taxas | R$ 940,57 | R$ 752,46 | −R$ 355,68 | −32,1% | Taxa separada, já somada |
| NUCLEO | Vila Boa Vida | Quarto Duplo Standard | COLETADO_COM_SUCESSO | R$ 6.810,00 | R$ 973,00 | R$ 778,40 | −R$ 329,74 | −29,8% | — |
| NUCLEO | Pousada Kia Ora Bombinhas | Quarto Duplo Deluxe c/ Vista Lateral do Mar | COLETADO_COM_SUCESSO | R$ 8.412,00 | R$ 1.201,71 | R$ 961,37 | −R$ 146,77 | −13,2% | — |
| NUCLEO | Pousada Riviera Bombinhas | Suíte Loft Riviera | COLETADO_COM_SUCESSO | R$ 9.908,00 | R$ 1.415,43 | R$ 1.132,34 | +R$ 24,20 | +2,2% | Praticamente empatada com a Villa |
| NUCLEO | Pousada Dom Capudi | Quarto Duplo | PRECISA_VALIDACAO_MANUAL | INDISPONIVEL (âncora) | — | — | — | — | Âncora esgotada; categorias mais caras seguiam à venda, não usadas |
| AMPLIADA | UP Hotel Boutique | Quarto Duplo Deluxe com Banheira | COLETADO_COM_SUCESSO | R$ 9.462,00 | R$ 1.351,71 | R$ 1.081,37 | +R$ 27,73 | +2,5% | Plano de 2 adultos mais barato |
| AMPLIADA | Morada do Guaruça | Apartamento de 1 Quarto | PRECISA_VALIDACAO_MANUAL | INDISPONIVEL | — | — | — | — | Esgotada, todas as categorias |
| TETO_MERCADO | Hotel/Pousada Atalaia do Mariscal | Suíte Superior | COLETADO_COM_SUCESSO | R$ 23.800,00 | R$ 3.400,00 | R$ 2.720,00 | +R$ 2.291,86 | +206,8% | Referência, não entra em nenhuma média. Booking alertava "6 hotéis 4 estrelas já indisponíveis" |

### 2. Tabela da Villa

| Acomodação | Total motor | Diária média motor | Total Booking estimado | Diária média Booking estimada | Mínimo de noites | Observação |
|---|---|---|---|---|---|---|
| Organic / Fuego / Metallo | R$ 7.757,00 | R$ 1.108,14 | R$ 9.696,25 | R$ 1.385,18 | 7/4 (noite 03/01) + 4 (noites 04–09/01) — mínimos não uniformes no bucket 1-3 | Período cruza dois buckets do inventário (1 noite a R$ 1.337 + 6 noites a R$ 1.070). Preço publicado a confirmar, não aprovado |

### 3. Resumo executivo — Rodada 9A

| Indicador | Valor |
|---|---|
| Núcleo disponível | 6 de 7 (85,7%) |
| Média núcleo Booking (diária) | R$ 1.012,76 |
| Mediana núcleo Booking | R$ 956,79 |
| Média motor equivalente núcleo | R$ 810,21 |
| Média ampliada Booking (n=1/2) | R$ 1.351,71 |
| Referência de teto | R$ 3.400,00 |
| Índice de disponibilidade total | 80% (8/10) |
| **Sinal de demanda** | **ALTO** — Dom Capudi (núcleo) com âncora esgotada + Atalaia com aviso do Booking "6 hotéis 4 estrelas já indisponíveis" |

### 4. Veredito de posicionamento — Rodada 9A

**`PROXIMA_DA_AMPLIADA`** — Villa +36,8% acima da média núcleo, mas apenas +2,5% acima da referência ampliada (UP).

### 5. Diagnóstico preliminar — Rodada 9A

**`PROTEGER`** — sinal de demanda ALTO real (esgotamento + aviso de escassez do próprio Booking); consistente com o mesmo padrão visto em Natal/Réveillon.

---

## RODADA 9B — Janeiro alta/primeira quinzena, 10–17/01/2027 (7 noites)

### 1. Tabela aberta — concorrentes

| Grupo | Concorrente | Acomodação âncora | Status | Preço total Booking | Diária média Booking | Motor equivalente médio | Dif. R$ vs. diária média Villa motor | Dif. % vs. Villa motor | Observação |
|---|---|---|---|---|---|---|---|---|---|
| NUCLEO | Vila Maciel | Apartamento Standard | COLETADO_COM_SUCESSO | R$ 4.092,00 (26% off; original R$ 5.530,00) | R$ 584,57 | R$ 467,66 | −R$ 602,34 | −56,3% | Desconto promocional ativo |
| NUCLEO | Pousada Kaloa Eco Village | Suíte Standard | COLETADO_COM_SUCESSO | R$ 5.460,00 | R$ 780,00 | R$ 624,00 | −R$ 446,00 | −41,7% | — |
| NUCLEO | Pousada dos Ingleses | Quarto Duplo Clássico | COLETADO_COM_SUCESSO | R$ 4.840,00 + R$ 120,00 taxas | R$ 708,57 | R$ 566,86 | −R$ 503,14 | −47,0% | Taxa separada, já somada |
| NUCLEO | Vila Boa Vida | Quarto Duplo Standard | COLETADO_COM_SUCESSO | R$ 6.230,00 | R$ 890,00 | R$ 712,00 | −R$ 358,00 | −33,5% | — |
| NUCLEO | Pousada Kia Ora Bombinhas | Quarto Duplo Deluxe c/ Vista Lateral do Mar | COLETADO_COM_SUCESSO | R$ 8.412,00 | R$ 1.201,71 | R$ 961,37 | −R$ 108,63 | −10,2% | — |
| NUCLEO | Pousada Riviera Bombinhas | Suíte Loft Riviera | COLETADO_COM_SUCESSO | R$ 9.084,00 | R$ 1.297,71 | R$ 1.038,17 | −R$ 31,83 | −3,0% | — |
| NUCLEO | Pousada Dom Capudi | Quarto Duplo | PRECISA_VALIDACAO_MANUAL | INDISPONIVEL (âncora) | — | — | — | — | Âncora esgotada novamente |
| AMPLIADA | UP Hotel Boutique | Quarto Duplo Deluxe com Banheira | COLETADO_COM_SUCESSO | R$ 8.712,00 | R$ 1.244,57 | R$ 995,66 | +R$ 25,66 | +2,6% | Plano de 2 adultos mais barato |
| AMPLIADA | Morada do Guaruça | Apartamento de 1 Quarto | PRECISA_VALIDACAO_MANUAL | INDISPONIVEL | — | — | — | — | Esgotada |
| TETO_MERCADO | Hotel/Pousada Atalaia do Mariscal | Suíte Superior | COLETADO_COM_SUCESSO | R$ 20.300,00 | R$ 2.900,00 | R$ 2.320,00 | +R$ 1.350,00 | +223,8% | Referência, não entra em nenhuma média. Booking alertava "6 hotéis 4 estrelas já indisponíveis" |

### 2. Tabela da Villa

| Acomodação | Total motor | Diária média motor | Total Booking estimado | Diária média Booking estimada | Mínimo de noites | Observação |
|---|---|---|---|---|---|---|
| Organic / Fuego / Metallo | R$ 7.490,00 | R$ 1.070,00 | R$ 9.362,50 | R$ 1.337,50 | 4 (bucket "4-31", inteiro) | Idêntico em valor a 9C e 9D — inventário não distingue semana dentro do bloco "4-31" |

### 3. Resumo executivo — Rodada 9B

| Indicador | Valor |
|---|---|
| Núcleo disponível | 6 de 7 (85,7%) |
| Média núcleo Booking (diária) | R$ 910,43 |
| Mediana núcleo Booking | R$ 835,00 |
| Média motor equivalente núcleo | R$ 728,34 |
| Média ampliada Booking (n=1/2) | R$ 1.244,57 |
| Referência de teto | R$ 2.900,00 |
| Índice de disponibilidade total | 80% (8/10) |
| **Sinal de demanda** | **ALTO** — mesmo padrão de 9A: Dom Capudi esgotado + aviso "6 hotéis 4 estrelas indisponíveis" |

### 4. Veredito de posicionamento — Rodada 9B

**`PROXIMA_DA_AMPLIADA`** — Villa +46,9% acima da média núcleo, +7,5% acima da ampliada. Gap vs. ampliada cresce frente a 9A (2,5%→7,5%), mas ainda dentro da faixa "próxima".

### 5. Diagnóstico preliminar — Rodada 9B

**`PROTEGER`** — mesma leitura de demanda alta de 9A. Tarifa igual à de 9C/9D, mas aqui sustentada por sinal de demanda mais forte.

---

## RODADA 9C — Janeiro intermediário, 17–24/01/2027 (7 noites)

### 1. Tabela aberta — concorrentes

| Grupo | Concorrente | Acomodação âncora | Status | Preço total Booking | Diária média Booking | Motor equivalente médio | Dif. R$ vs. diária média Villa motor | Dif. % vs. Villa motor | Observação |
|---|---|---|---|---|---|---|---|---|---|
| NUCLEO | Vila Maciel | Apartamento Standard | COLETADO_COM_SUCESSO | R$ 3.885,00 (26% off; original R$ 5.250,00) | R$ 555,00 | R$ 444,00 | −R$ 626,00 | −58,5% | Desconto promocional ativo |
| NUCLEO | Pousada dos Ingleses | Quarto Duplo Clássico | COLETADO_COM_SUCESSO | R$ 4.840,00 + R$ 120,00 taxas | R$ 708,57 | R$ 566,86 | −R$ 503,14 | −47,0% | Taxa separada, já somada |
| NUCLEO | Pousada Kaloa Eco Village | Suíte Standard | COLETADO_COM_SUCESSO | R$ 5.460,00 | R$ 780,00 | R$ 624,00 | −R$ 446,00 | −41,7% | — |
| NUCLEO | Pousada Dom Capudi | Quarto Duplo | COLETADO_COM_SUCESSO | R$ 5.819,00 | R$ 831,29 | R$ 665,03 | −R$ 404,97 | −37,8% | Voltou a aparecer disponível (esgotada em 9A/9B) |
| NUCLEO | Vila Boa Vida | Quarto Duplo Standard | COLETADO_COM_SUCESSO | R$ 6.230,00 | R$ 890,00 | R$ 712,00 | −R$ 358,00 | −33,5% | — |
| NUCLEO | Pousada Kia Ora Bombinhas | Quarto Duplo Deluxe c/ Vista Lateral do Mar | COLETADO_COM_SUCESSO | R$ 8.412,00 | R$ 1.201,71 | R$ 961,37 | −R$ 108,63 | −10,2% | — |
| NUCLEO | Pousada Riviera Bombinhas | Suíte Loft Riviera | COLETADO_COM_SUCESSO | R$ 9.084,00 | R$ 1.297,71 | R$ 1.038,17 | −R$ 31,83 | −3,0% | — |
| AMPLIADA | UP Hotel Boutique | Quarto Duplo Deluxe com Banheira | COLETADO_COM_SUCESSO | R$ 8.663,00 | R$ 1.237,57 | R$ 990,06 | +R$ 18,66 | +1,9% | Plano de 2 adultos mais barato |
| AMPLIADA | Morada do Guaruça | Apartamento de 1 Quarto | PRECISA_VALIDACAO_MANUAL | INDISPONIVEL | — | — | — | — | Esgotada |
| TETO_MERCADO | Hotel/Pousada Atalaia do Mariscal | Suíte Superior | COLETADO_COM_SUCESSO | R$ 20.300,00 | R$ 2.900,00 | R$ 2.320,00 | +R$ 1.350,00 | +223,8% | Referência, não entra em nenhuma média. **Sem** aviso de escassez nesta rodada — diferente das demais |

### 2. Tabela da Villa

| Acomodação | Total motor | Diária média motor | Total Booking estimado | Diária média Booking estimada | Mínimo de noites | Observação |
|---|---|---|---|---|---|---|
| Organic / Fuego / Metallo | R$ 7.490,00 | R$ 1.070,00 | R$ 9.362,50 | R$ 1.337,50 | 4 (bucket "4-31") | Valor idêntico a 9B e 9D — a Villa não tem tarifa própria distinta para esta semana no inventário atual |

### 3. Resumo executivo — Rodada 9C

| Indicador | Valor |
|---|---|
| Núcleo disponível | 7 de 7 — amostra completa |
| Média núcleo Booking (diária) | R$ 894,90 |
| Mediana núcleo Booking | R$ 831,29 |
| Média motor equivalente núcleo | R$ 715,92 |
| Média ampliada Booking (n=1/2) | R$ 1.237,57 |
| Referência de teto | R$ 2.900,00 — sem aviso de escassez |
| Índice de disponibilidade total | 90% (9/10) |
| **Sinal de demanda** | **MÉDIO** — núcleo 100% disponível e sem aviso de escassez do Booking (sinal mais fraco que 9A/9B), mas sem evidência de demanda baixa |

### 4. Veredito de posicionamento — Rodada 9C

**`ACIMA_DO_NUCLEO_MAS_DEFENSAVEL`** — Villa +49,5% acima da média núcleo, +8,1% acima da ampliada (subindo de 7,5% em 9B). Sem o reforço de esgotamento/escassez que sustentava 9A/9B.

### 5. Diagnóstico preliminar — Rodada 9C

**`MANTER`** — sem sinal de esgotamento/escassez, mas também sem evidência de fraqueza de demanda real; sem dado de ritmo de reservas próprio que justifique subir, baixar ou proteger de forma mais assertiva.

---

## RODADA 9D — Última semana de janeiro, 24–31/01/2027 (7 noites)

### 1. Tabela aberta — concorrentes

| Grupo | Concorrente | Acomodação âncora | Status | Preço total Booking | Diária média Booking | Motor equivalente médio | Dif. R$ vs. diária média Villa motor | Dif. % vs. Villa motor | Observação |
|---|---|---|---|---|---|---|---|---|---|
| NUCLEO | Pousada dos Ingleses | Quarto Duplo Clássico | COLETADO_COM_SUCESSO | R$ 3.695,00 + R$ 120,00 taxas | R$ 545,00 | R$ 436,00 | −R$ 634,00 | −59,3% | Taxa separada, já somada. Preço mais baixo do conjunto das 4 rodadas para este concorrente |
| NUCLEO | Vila Maciel | Apartamento Standard | COLETADO_COM_SUCESSO | R$ 3.367,00 (26% off; original R$ 4.550,00) | R$ 481,00 | R$ 384,80 | −R$ 685,20 | −64,0% | Desconto promocional ativo |
| NUCLEO | Pousada Kaloa Eco Village | Suíte Standard | COLETADO_COM_SUCESSO | R$ 5.460,00 | R$ 780,00 | R$ 624,00 | −R$ 446,00 | −41,7% | — |
| NUCLEO | Pousada Dom Capudi | Quarto Duplo | COLETADO_COM_SUCESSO | R$ 5.819,00 | R$ 831,29 | R$ 665,03 | −R$ 404,97 | −37,8% | — |
| NUCLEO | Vila Boa Vida | Quarto Duplo Standard | COLETADO_COM_SUCESSO | R$ 6.230,00 | R$ 890,00 | R$ 712,00 | −R$ 358,00 | −33,5% | — |
| NUCLEO | Pousada Kia Ora Bombinhas | Quarto Duplo Deluxe c/ Vista Lateral do Mar | COLETADO_COM_SUCESSO | R$ 8.412,00 | R$ 1.201,71 | R$ 961,37 | −R$ 108,63 | −10,2% | — |
| NUCLEO | Pousada Riviera Bombinhas | Suíte Loft Riviera | COLETADO_COM_SUCESSO | R$ 9.084,00 | R$ 1.297,71 | R$ 1.038,17 | −R$ 31,83 | −3,0% | — |
| AMPLIADA | UP Hotel Boutique | Quarto Duplo Deluxe com Banheira | COLETADO_COM_SUCESSO | R$ 8.494,00 | R$ 1.213,43 | R$ 970,74 | −R$ 4,48 | −0,4% | Plano de 2 adultos mais barato |
| AMPLIADA | Morada do Guaruça | Apartamento de 1 Quarto | PRECISA_VALIDACAO_MANUAL | INDISPONIVEL | — | — | — | — | Indisponível nas 4 rodadas de janeiro/2027 |
| TETO_MERCADO | Hotel/Pousada Atalaia do Mariscal | Suíte Superior | COLETADO_COM_SUCESSO | R$ 20.300,00 | R$ 2.900,00 | R$ 2.320,00 | +R$ 1.350,00 | +223,8% | Referência, não entra em nenhuma média. Sem aviso de escassez |

**Achado transversal (tendência ao longo do mês):** Vila Maciel caiu de R$ 676,29 (9A) → R$ 584,57 (9B) → R$ 555,00 (9C) → R$ 481,00 (9D); Pousada dos Ingleses caiu de R$ 940,57 (9A) → R$ 708,57 (9B) → R$ 708,57 (9C) → R$ 545,00 (9D). É o sinal quantitativo mais forte da análise — mas é preço listado 6 meses fora da data, não confirmação de ocupação real.

### 2. Tabela da Villa

| Acomodação | Total motor | Diária média motor | Total Booking estimado | Diária média Booking estimada | Mínimo de noites | Observação |
|---|---|---|---|---|---|---|
| Organic / Fuego / Metallo | R$ 7.490,00 | R$ 1.070,00 | R$ 9.362,50 | R$ 1.337,50 | 4 (bucket "4-31") | Valor idêntico a 9B e 9C — mesma limitação de granularidade do inventário |

### 3. Resumo executivo — Rodada 9D

| Indicador | Valor |
|---|---|
| Núcleo disponível | 7 de 7 — amostra completa |
| Média núcleo Booking (diária) | R$ 861,10 |
| Mediana núcleo Booking | R$ 831,29 |
| Média motor equivalente núcleo | R$ 688,77 |
| Média ampliada Booking (n=1/2) | R$ 1.213,43 |
| Referência de teto | R$ 2.900,00 — sem aviso de escassez |
| Índice de disponibilidade total | 90% (9/10) |
| **Sinal de demanda** | **MÉDIO**, com viés de enfraquecimento — núcleo 100% disponível, sem aviso de escassez, e queda nominal progressiva de dois concorrentes núcleo ao longo do mês |

### 4. Veredito de posicionamento — Rodada 9D

**`ACIMA_DO_NUCLEO_MAS_DEFENSAVEL`** — Villa +55,3% acima da média núcleo (maior gap das 4 sub-rodadas), +10,2% acima da ampliada (ultrapassando 10% pela primeira vez no bloco). Não escalado para `ACIMA_DO_MERCADO_COM_RISCO` por falta de dado de ocupação/ritmo de reservas próprio.

### 5. Diagnóstico preliminar — Rodada 9D

**`MANTER`**, com ponto de atenção — a queda nominal da concorrência é um sinal a monitorar, não uma justificativa automática de baixa. Por `reserva-direta-reducao-otas.md`: a Villa não compete por igualar preço de OTA, compete por valor, atendimento e reserva direta.

---

## Leitura específica de janeiro

**A primeira quinzena (9A/9B) está bem posicionada?**
Sim. Villa fica muito acima do núcleo (37–47%), padrão estrutural repetido em todo o Radar desde setembro, mas frente à referência mais comparável (ampliada/UP) a diferença é pequena (2,5% a 7,5%), com sinal de demanda ALTO real (concorrente núcleo esgotado + aviso de escassez do próprio Booking) sustentando a tarifa.

**A semana de 17 a 23/01 (9C) deve ser mantida ou protegida?**
Mantida (`MANTER`), não protegida. O sinal de demanda cai de ALTO para MÉDIO — não porque a Villa mudou de preço (ela não mudou), mas porque a concorrência núcleo deixou de mostrar esgotamento e o Booking parou de exibir aviso de escassez regional.

**A última semana de janeiro (9D) mostra queda real de demanda?**
Não é conclusivo, mas há um sinal real a favor da hipótese: dois concorrentes núcleo (Vila Maciel e Pousada dos Ingleses) reduziram preço nominal de forma consistente ao longo das 4 sub-rodadas, com o menor valor do conjunto batendo justamente na 9D. Ainda assim é dado de OTA a 6 meses da data, não confirmação de ocupação real.

**Existe risco de a Villa estar barata demais?**
Não. Em nenhuma das 4 sub-rodadas a Villa aparece abaixo do núcleo ou perto da mediana núcleo — está sempre 37% a 55% acima.

**Existe risco de estar cara demais?**
Existe um risco crescente a monitorar, mais concentrado em 9D: o gap vs. ampliada passa de 2,5% (9A) para 10,2% (9D), coincidindo com a concorrência núcleo baixando preço nominal na última semana. Não chega a `ACIMA_DO_MERCADO_COM_RISCO` com o dado atual (falta dado de ocupação/ritmo de reservas próprio), mas é o ponto mais forte de atenção da rodada.

**Faz sentido simular redução tática na última semana?**
Com o dado disponível hoje, não há justificativa suficiente — diferente do precedente de novembro/2026 (tarifa tática aplicada por Renildo), baseado em sinal de demanda `BAIXO` confirmado (zero esgotamento em núcleo/ampliada/teto). Em 9D o sinal é `MÉDIO` com tendência de queda, não `BAIXO` confirmado. Pode fazer sentido revisitar essa simulação mais perto da data, quando houver dado de ritmo de reservas real da Villa.

**Faz sentido proteger ou subir algum bloco?**
Proteger faz sentido para 9A e 9B (sinal de demanda ALTO com evidência direta do Booking). Não há base para subir em nenhum bloco — a Villa já está bem acima do núcleo em todos eles.

**Caminho por bloco:**

| Bloco | Diagnóstico |
|---|---|
| Primeira quinzena forte (03–16/01, 9A+9B) | `PROTEGER` |
| Semana intermediária (17–23/01, 9C) | `MANTER` |
| Última semana (24–31/01, 9D) | `MANTER`, com ponto de atenção registrado para releitura em rodada futura mais próxima da data |

---

## Comparativo final

| Bloco | Noites | Total motor Villa | Diária média motor | Total Booking estimado | Diária média Booking estimada | Média núcleo Booking (diária) | % Villa vs. núcleo | % Villa vs. ampliada | Sinal de demanda | Diagnóstico |
|---|---|---|---|---|---|---|---|---|---|---|
| 03–16/01 (9A+9B) | 14 | R$ 15.247,00 | R$ 1.089,07 | R$ 19.058,75 | R$ 1.361,34 | R$ 961,60 (média das 2 rodadas) | +41,6% | +2,5% a +7,5% (por sub-rodada) | ALTO | `PROTEGER` |
| 17–23/01 (9C) | 7 | R$ 7.490,00 | R$ 1.070,00 | R$ 9.362,50 | R$ 1.337,50 | R$ 894,90 | +49,5% | +8,1% | MÉDIO | `MANTER` |
| 24–31/01 (9D) | 7 | R$ 7.490,00 | R$ 1.070,00 | R$ 9.362,50 | R$ 1.337,50 | R$ 861,10 | +55,3% | +10,2% | MÉDIO (tendência de queda) | `MANTER` (ponto de atenção) |

**Achado central do bloco de janeiro:** a tarifa da Villa é rigorosamente idêntica nas 3 semanas de 10/01 a 31/01 (motor R$ 1.070,00, sem exceção) porque o inventário publicado não fragmenta o bucket "Janeiro/2027 4-31". O que muda ao longo do mês é exclusivamente o comportamento da concorrência: sinal de demanda caindo de ALTO (9A/9B) para MÉDIO (9C/9D), e dois concorrentes núcleo baixando preço nominal de forma consistente rumo ao fim do mês. Isso não gera, com os dados de hoje, nenhuma recomendação de baixa ou alta — mas é um sinal estrutural relevante para Renildo avaliar se vale, no futuro, segmentar o inventário publicado por semana dentro do bloco "4-31" em vez de mantê-lo uniforme.

---

## Dados que faltam

- Ritmo de reservas/ocupação real da própria Pousada Arágua para janeiro/2027 (período muito distante — 6 meses da data de coleta).
- Confirmação no sistema (Stays) de que os valores R$ 1.337,00 e R$ 1.070,00 do inventário publicado são os efetivamente aplicados — hoje são "preço publicado a confirmar", não "preço aprovado".
- Confirmação do mínimo de noites real do bucket "Janeiro/2027 1-3" (o próprio inventário registra "mínimos variam no print").
- Coleta de Vila dos Açores (status `PENDENTE`, não incluída em nenhuma média).
- Nova rodada de coleta mais próxima da data real (ex.: 60–90 dias antes) para confirmar se a tendência de queda nominal da concorrência em 9D se mantém ou reverte.

---

## Conclusão

Nenhuma decisão nova foi gerada por este relatório. Nenhuma tarifa foi alterada. Nenhum card foi movido para `DECISOES_REVENUE_PENDENTES_VILLA_ARAGUA.md`. Todos os diagnósticos acima são preliminares — Renildo decide.

**Rodada 9A (03–10/01):** `PROTEGER`
**Rodada 9B (10–17/01):** `PROTEGER`
**Rodada 9C (17–24/01):** `MANTER`
**Rodada 9D (24–31/01):** `MANTER` (ponto de atenção)

**Status deste relatório:** `RELATORIO_ANALITICO_SEM_ALTERACAO_TARIFARIA`
