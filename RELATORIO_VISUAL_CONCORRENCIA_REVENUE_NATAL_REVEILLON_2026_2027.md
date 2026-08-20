# RELATÓRIO VISUAL — RADAR DE CONCORRÊNCIA REVENUE — POUSADA ARÁGUA (NATAL E RÉVEILLON 2026/2027)

**Diferença estrutural desta rodada:** o hóspede compra o período como **pacote** (com mínimo de noites), e a tarifa motor da Villa **varia dia a dia** dentro do pacote — não existe uma diária única. Toda comparação abaixo é **pacote total contra pacote total** e **diária média contra diária média**, nunca uma diária isolada contra o pacote inteiro.

**Rodadas cobertas:**
- Rodada 7A — Natal, janela 18–24/12/2026 (6 noites, antes da virada principal)
- Rodada 7B — Natal, pacote principal, 20–25/12/2026 (5 noites, mín. 5 diárias, inclui a noite de 24/12)
- Rodada 8A — Réveillon, pacote principal, 27/12/2026–03/01/2027 (7 noites, mín. 7 diárias)
- Rodada 8B — janela completa, 25/12/2026–03/01/2027 (9 noites)

**Produto Villa de referência:** Pousada Arágua — unidade base (Organic/Fuego/Metallo) · perfil casal (2 adultos, 0 crianças, 1 acomodação)
**Fontes:** `COLETAS_CONCORRENCIA_REVENUE.csv`, `CESTA_COMPETITIVA_REVENUE_VILLA_ARAGUA.md`, `ALERTAS_CONCORRENCIA_REVENUE.md`, `REGRAS_CONVERSAO_OTA_MOTOR_REVENUE.md`, `INVENTARIO_TARIFAS_PUBLICADAS_AGO2026_ABR2027.csv`
**Coleta:** 2026-07-29, via Booking (Claude in Chrome), preços públicos visíveis, sem login, sem clicar em reservar.
**Diagnóstico:** gerado via agente `villa-precificacao-calendario`, com consulta às skills `villa-aragua-pricing-revenue` e `villa-aragua-growth-marketer` — agente acionado de fato, cálculo do pacote Villa verificado de forma independente pelo agente (bateu com o cálculo preliminar).
**Status deste relatório:** `RELATORIO_ANALITICO_SEM_ALTERACAO_TARIFARIA` — todos os diagnósticos abaixo são **preliminares**. Renildo decide.

**Buckets do inventário usados no cálculo do pacote Villa (motor):** "Dezembro/2026 1-18" = R$ 629,00 · "Natal/2026 19-25 dez" = R$ 889,00 (mín. 5, proteger) · "Réveillon/2026 26-31 dez" = R$ 1.337,00 (mín. 7, proteger) · "Janeiro/2027 1-3" = R$ 1.337,00 (mesmo valor do Réveillon). Conversão Booking = motor × 1,25 (`REGRAS_CONVERSAO_OTA_MOTOR_REVENUE.md`).

**Ambiguidade sinalizada e verificada pelo agente:** a noite de 18/12 (fronteira entre os buckets "1-18" e "19-25") foi tratada como pertencente ao bucket "Dezembro 1-18" (R$ 629), por o próprio nome do bucket incluir o dia 18. O agente confirmou essa leitura ao reconferir o inventário, sem encontrar erro a corrigir — mas o ponto fica registrado como incerteza de fronteira, não como fato 100% resolvido no inventário.

---

## RODADA 7A — Natal, janela 18–24/12/2026 (6 noites)

### 1. Tabela aberta — concorrentes

| Grupo | Concorrente | Acomodação âncora | Status | Preço total Booking | Diária média Booking | Motor equivalente médio | Dif. R$ vs. diária média Villa motor | Dif. % vs. Villa motor | Observação |
|---|---|---|---|---|---|---|---|---|---|
| NUCLEO | Vila Maciel | Apartamento Standard | COLETADO_COM_SUCESSO | R$ 2.508,00 (15% off; original R$ 2.950,00) | R$ 418,00 | R$ 334,40 | −R$ 511,27 | −60,5% | Desconto promocional ativo |
| NUCLEO | Pousada Kaloa Eco Village | Suíte Standard | COLETADO_COM_SUCESSO | R$ 3.828,00 | R$ 638,00 | R$ 510,40 | −R$ 335,27 | −39,6% | — |
| NUCLEO | Vila Boa Vida | Quarto Duplo Standard | COLETADO_COM_SUCESSO | R$ 3.960,00 | R$ 660,00 | R$ 528,00 | −R$ 317,67 | −37,6% | — |
| NUCLEO | Pousada Riviera Bombinhas | Suíte Loft Riviera | COLETADO_COM_SUCESSO | R$ 6.384,00 | R$ 1.064,00 | R$ 851,20 | +R$ 5,53 | +0,7% | Praticamente empatada com a Villa |
| NUCLEO | Pousada Kia Ora Bombinhas | Quarto Duplo Deluxe c/ Vista Lateral do Mar | PRECISA_VALIDACAO_MANUAL | INDISPONIVEL | — | — | — | — | Esgotada, todas as categorias |
| NUCLEO | Pousada dos Ingleses | Quarto Duplo Clássico | PRECISA_VALIDACAO_MANUAL | INDISPONIVEL (âncora) | — | — | — | — | Âncora esgotada; só Suíte seguia à venda, não usada |
| NUCLEO | Pousada Dom Capudi | Quarto Duplo | PRECISA_VALIDACAO_MANUAL | INDISPONIVEL (âncora) | — | — | — | — | Âncora esgotada; categorias mais caras seguiam à venda, não usadas |
| AMPLIADA | UP Hotel Boutique | Quarto Duplo Deluxe com Banheira | COLETADO_COM_SUCESSO | R$ 5.700,00 (10% off; original R$ 6.334,00) | R$ 950,00 | R$ 760,00 | −R$ 85,67 | −10,1% | — |
| AMPLIADA | Morada do Guaruça | Apartamento de 1 Quarto | PRECISA_VALIDACAO_MANUAL | INDISPONIVEL | — | — | — | — | Esgotada, todas as categorias |
| TETO_MERCADO | Hotel/Pousada Atalaia do Mariscal | Suíte Superior | COLETADO_COM_SUCESSO | R$ 13.800,00 | R$ 2.300,00 | R$ 1.840,00 | +R$ 994,33 | +117,6% | Referência, não entra em nenhuma média. Booking alertava "6 hotéis 4 estrelas já indisponíveis" |

### 2. Tabela da Villa — pacote

| Acomodação | Total motor pacote | Diária média motor | Total Booking estimado | Diária média Booking estimada | Mín. noites aplicado | Observação |
|---|---|---|---|---|---|---|
| Organic / Fuego / Metallo (base) | R$ 5.074,00 | R$ 845,67 | R$ 6.342,50 | R$ 1.057,08 | Variável (1-18 mín. 1-2; Natal mín. 5) | Noite 18/12 tratada como bucket "1-18" (R$ 629) — fronteira sinalizada. Noites 19-23 (5 noites) no bucket Natal (R$ 889 cada) |

### 3. Resumo executivo — Rodada 7A

| Indicador | Valor |
|---|---|
| Núcleo disponível | 4 de 7 (57,1%) |
| Média núcleo Booking (diária) | R$ 695,00 |
| Mediana núcleo Booking | R$ 649,00 |
| Média motor equivalente núcleo | R$ 556,00 |
| Média ampliada Booking (n=1/2) | R$ 950,00 |
| Referência de teto | R$ 2.300,00 |
| Índice de disponibilidade total tentado | 60% (6/10) |
| **Sinal de demanda** | **ALTO** — 3 concorrentes núcleo indisponíveis + ampliada parcialmente esgotada + alerta explícito de escassez do Booking no teto |

### 4. Veredito de posicionamento — Rodada 7A

**`PROXIMA_DA_AMPLIADA`** — Villa +52,1% acima do núcleo (amostra moderada, 4/7), mas apenas +11,3% acima da única referência ampliada disponível.

### 5. Diagnóstico preliminar — Rodada 7A

**`PROTEGER`** — o inventário já classifica o bucket Natal como "proteger" ("evitar desconto cedo"), reforçado pelo sinal de demanda ALTO. Nada sustenta baixa.

---

## RODADA 7B — Natal, pacote principal, 20–25/12/2026 (5 noites, mín. 5, inclui 24/12)

### 1. Tabela aberta — concorrentes

| Grupo | Concorrente | Acomodação âncora | Status | Preço total Booking | Diária média Booking | Motor equivalente médio | Dif. R$ vs. diária média Villa motor | Dif. % vs. Villa motor | Observação |
|---|---|---|---|---|---|---|---|---|---|
| NUCLEO | Vila Maciel | Apartamento Standard | COLETADO_COM_SUCESSO | R$ 2.253,00 (15% off; original R$ 2.650,00) | R$ 450,60 | R$ 360,48 | −R$ 528,52 | −59,4% | Desconto promocional ativo |
| NUCLEO | Pousada Kaloa Eco Village | Suíte Standard | COLETADO_COM_SUCESSO | R$ 3.190,00 | R$ 638,00 | R$ 510,40 | −R$ 378,60 | −42,6% | — |
| NUCLEO | Vila Boa Vida | Quarto Duplo Standard | COLETADO_COM_SUCESSO | R$ 3.300,00 | R$ 660,00 | R$ 528,00 | −R$ 361,00 | −40,6% | — |
| NUCLEO | Pousada Riviera Bombinhas | Suíte Loft Riviera | PRECISA_VALIDACAO_MANUAL | INDISPONIVEL | — | — | — | — | Esgotada, todas as categorias |
| NUCLEO | Pousada Kia Ora Bombinhas | Quarto Duplo Deluxe c/ Vista Lateral do Mar | PRECISA_VALIDACAO_MANUAL | INDISPONIVEL | — | — | — | — | Esgotada, todas as categorias |
| NUCLEO | Pousada dos Ingleses | Quarto Duplo Clássico | PRECISA_VALIDACAO_MANUAL | INDISPONIVEL (âncora) | — | — | — | — | Âncora esgotada; só Suíte seguia à venda, não usada |
| NUCLEO | Pousada Dom Capudi | Quarto Duplo | PRECISA_VALIDACAO_MANUAL | INDISPONIVEL (âncora) | — | — | — | — | Âncora esgotada; categorias mais caras seguiam à venda, não usadas |
| AMPLIADA | UP Hotel Boutique | Quarto Duplo Deluxe com Banheira | COLETADO_COM_SUCESSO | R$ 5.322,00 (5% off; original R$ 5.602,00) | R$ 1.064,40 | R$ 851,52 | −R$ 46,85 | −4,2% | — |
| AMPLIADA | Morada do Guaruça | Apartamento de 1 Quarto | PRECISA_VALIDACAO_MANUAL | INDISPONIVEL | — | — | — | — | Esgotada, todas as categorias |
| TETO_MERCADO | Hotel/Pousada Atalaia do Mariscal | Suíte Superior | COLETADO_COM_SUCESSO | R$ 11.500,00 | R$ 2.300,00 | R$ 1.840,00 | +R$ 1.188,75 | +133,7% | Referência, não entra em nenhuma média |

**Alerta de qualidade da amostra:** os 4 ausentes do núcleo incluem justamente Riviera e Kia Ora — historicamente os dois mais caros do grupo. A ausência deles empurra a média núcleo bruta para baixo, inflando artificialmente o gap % da Villa vs. núcleo. A comparação vs. ampliada é a leitura mais confiável desta rodada.

### 2. Tabela da Villa — pacote

| Acomodação | Total motor pacote | Diária média motor | Total Booking estimado | Diária média Booking estimada | Mín. noites aplicado | Observação |
|---|---|---|---|---|---|---|
| Organic / Fuego / Metallo (base) | R$ 4.445,00 | R$ 889,00 | R$ 5.556,25 | R$ 1.111,25 | 5 | Única sub-rodada com diária motor 100% uniforme — todo o pacote está no bucket Natal. Inclui a noite de 24/12 sem prêmio adicional sobre as demais noites do bucket |

### 3. Resumo executivo — Rodada 7B

| Indicador | Valor |
|---|---|
| Núcleo disponível | 3 de 7 (42,9% — a menor disponibilidade núcleo de todo o Radar) |
| Média núcleo Booking (diária) | R$ 582,87 |
| Mediana núcleo Booking | R$ 638,00 |
| Média motor equivalente núcleo | R$ 466,29 |
| Média ampliada Booking (n=1/2) | R$ 1.064,40 |
| Referência de teto | R$ 2.300,00 |
| Índice de disponibilidade total tentado | 50% (5/10) |
| **Sinal de demanda** | **ALTO** — a maior escassez núcleo já registrada em todo o Radar (4 concorrentes indisponíveis + ampliada parcialmente esgotada) |

### 4. Veredito de posicionamento — Rodada 7B

**`PROXIMA_DA_AMPLIADA`** — vs. núcleo bruto, Villa fica +90,7% acima (amostra 3/7, enviesada para os concorrentes mais baratos, leitura pouco confiável). Vs. ampliada, apenas +4,4% acima — leitura mais honesta do posicionamento real.

### 5. Diagnóstico preliminar — Rodada 7B

**`PROTEGER`** — pacote inclui a noite de 24/12 (o ativo mais valioso do calendário de Natal), sinal de demanda ALTO, inventário já classifica este bucket como "proteger". A comparação núcleo bruta não deve motivar baixa — está distorcida pela ausência dos concorrentes mais caros.

---

## RODADA 8A — Réveillon, pacote principal, 27/12/2026–03/01/2027 (7 noites, mín. 7)

### 1. Tabela aberta — concorrentes

| Grupo | Concorrente | Acomodação âncora | Status | Preço total Booking | Diária média Booking | Motor equivalente médio | Dif. R$ vs. diária média Villa motor | Dif. % vs. Villa motor | Observação |
|---|---|---|---|---|---|---|---|---|---|
| NUCLEO | Vila Maciel | Apartamento Standard | COLETADO_COM_SUCESSO | R$ 6.280,00 (20% off; original R$ 7.850,00) | R$ 897,14 | R$ 717,71 | −R$ 619,29 | −46,3% | Desconto promocional ativo |
| NUCLEO | Pousada Dom Capudi | Quarto Duplo | COLETADO_COM_SUCESSO | R$ 6.983,00 | R$ 997,57 | R$ 798,06 | −R$ 538,89 | −40,3% | Voltou a aparecer disponível (esgotada na 7A/7B) |
| NUCLEO | Vila Boa Vida | Quarto Duplo Standard | COLETADO_COM_SUCESSO | R$ 7.245,00 | R$ 1.035,00 | R$ 828,00 | −R$ 501,43 | −38,1% | — |
| NUCLEO | Pousada Kaloa Eco Village | Suíte Standard | COLETADO_COM_SUCESSO | R$ 7.656,00 | R$ 1.093,71 | R$ 874,97 | −R$ 462,72 | −34,6% | — |
| NUCLEO | Pousada Kia Ora Bombinhas | Quarto Duplo Deluxe c/ Vista Lateral do Mar | COLETADO_COM_SUCESSO | R$ 9.635,00 | R$ 1.376,43 | R$ 1.101,14 | −R$ 179,00 | −13,4% | Voltou a aparecer disponível (esgotada na 7A/7B) |
| NUCLEO | Pousada Riviera Bombinhas | Suíte Loft Riviera | COLETADO_COM_SUCESSO | R$ 11.322,00 | R$ 1.617,43 | R$ 1.293,94 | +R$ 62,00 | +4,6% | Praticamente empatada com a Villa |
| NUCLEO | Pousada dos Ingleses | Quarto Duplo Clássico | PRECISA_VALIDACAO_MANUAL | INDISPONIVEL (âncora) | — | — | — | — | Âncora esgotada; só Suíte seguia à venda, não usada |
| AMPLIADA | UP Hotel Boutique | Quarto Duplo Deluxe com Banheira | COLETADO_COM_SUCESSO | R$ 13.031,00 (10% off; original R$ 14.479,00) | R$ 1.861,57 | R$ 1.489,26 | +R$ 306,32 | +22,9% | — |
| AMPLIADA | Morada do Guaruça | Apartamento de 1 Quarto | PRECISA_VALIDACAO_MANUAL | INDISPONIVEL | — | — | — | — | Indisponível nas 4 sub-rodadas de Natal/Réveillon |
| TETO_MERCADO | Hotel/Pousada Atalaia do Mariscal | Suíte Superior | COLETADO_COM_SUCESSO | R$ 23.800,00 | R$ 3.400,00 | R$ 2.720,00 | +R$ 1.239,32 | +92,7% | Referência, não entra em nenhuma média. Booking alertava "6 hotéis 4 estrelas já indisponíveis" |

### 2. Tabela da Villa — pacote

| Acomodação | Total motor pacote | Diária média motor | Total Booking estimado | Diária média Booking estimada | Mín. noites aplicado | Observação |
|---|---|---|---|---|---|---|
| Organic / Fuego / Metallo (base) | R$ 9.359,00 | R$ 1.337,00 | R$ 11.698,75 | R$ 1.671,25 | 7 | Diária motor 100% uniforme — buckets Réveillon (26-31 dez) e Janeiro 1-3 têm o mesmo valor (R$ 1.337); a virada de ano não gera degrau de preço |

### 3. Resumo executivo — Rodada 8A

| Indicador | Valor |
|---|---|
| Núcleo disponível | 6 de 7 (85,7% — a melhor amostra de todo o conjunto Natal/Réveillon) |
| Média núcleo Booking (diária) | R$ 1.169,55 |
| Mediana núcleo Booking | R$ 1.064,36 |
| Média motor equivalente núcleo | R$ 935,64 |
| Média ampliada Booking (n=1/2) | R$ 1.861,57 |
| Referência de teto | R$ 3.400,00 |
| Índice de disponibilidade total tentado | 80% (8/10) |
| **Sinal de demanda** | **ALTO** — apenas Ingleses indisponível no núcleo, mas Morada indisponível na ampliada e alerta explícito de escassez do Booking no teto |

### 4. Veredito de posicionamento — Rodada 8A

**`ACIMA_DO_NUCLEO_MAS_DEFENSAVEL`** — melhor amostra núcleo do conjunto, Villa +42,9% acima do núcleo com premium justificável, e **abaixo** da ampliada (−10,2%) — não está no teto de risco.

### 5. Diagnóstico preliminar — Rodada 8A

**`PROTEGER`** — amostra forte, sinal de demanda ALTO, inventário já classifica o bucket como "proteger" ("avaliar junto com janeiro/2027"). Villa nem chega à referência ampliada — sem indício de estar cara demais.

---

## RODADA 8B — Janela completa, 25/12/2026–03/01/2027 (9 noites)

### 1. Tabela aberta — concorrentes

| Grupo | Concorrente | Acomodação âncora | Status | Preço total Booking | Diária média Booking | Motor equivalente médio | Dif. R$ vs. diária média Villa motor | Dif. % vs. Villa motor | Observação |
|---|---|---|---|---|---|---|---|---|---|
| NUCLEO | Vila Maciel | Apartamento Standard | COLETADO_COM_SUCESSO | R$ 7.272,00 (20% off; original R$ 9.090,00) | R$ 808,00 | R$ 646,40 | −R$ 640,80 | −49,8% | Desconto promocional ativo |
| NUCLEO | Vila Boa Vida | Quarto Duplo Standard | COLETADO_COM_SUCESSO | R$ 8.940,00 | R$ 993,33 | R$ 794,67 | −R$ 492,36 | −38,3% | — |
| NUCLEO | Pousada Kaloa Eco Village | Suíte Standard | COLETADO_COM_SUCESSO | R$ 9.388,00 | R$ 1.043,11 | R$ 834,49 | −R$ 452,58 | −35,2% | — |
| NUCLEO | Pousada Riviera Bombinhas | Suíte Loft Riviera | PRECISA_VALIDACAO_MANUAL | INDISPONIVEL | — | — | — | — | Esgotada, todas as categorias |
| NUCLEO | Pousada Kia Ora Bombinhas | Quarto Duplo Deluxe c/ Vista Lateral do Mar | PRECISA_VALIDACAO_MANUAL | INDISPONIVEL | — | — | — | — | Esgotada, todas as categorias |
| NUCLEO | Pousada dos Ingleses | Quarto Duplo Clássico | PRECISA_VALIDACAO_MANUAL | INDISPONIVEL (âncora) | — | — | — | — | Âncora esgotada; só Suíte seguia à venda, não usada |
| NUCLEO | Pousada Dom Capudi | Quarto Duplo | PRECISA_VALIDACAO_MANUAL | INDISPONIVEL (âncora) | — | — | — | — | Voltou a ficar indisponível — havia aparecido disponível na janela mais curta (8A) |
| AMPLIADA | UP Hotel Boutique | Quarto Duplo Deluxe com Banheira | COLETADO_COM_SUCESSO | R$ 14.023,00 (10% off; original R$ 15.581,00) | R$ 1.558,11 | R$ 1.246,49 | −R$ 40,72 | −3,2% | — |
| AMPLIADA | Morada do Guaruça | Apartamento de 1 Quarto | PRECISA_VALIDACAO_MANUAL | INDISPONIVEL | — | — | — | — | Indisponível nas 4 sub-rodadas de Natal/Réveillon |
| TETO_MERCADO | Hotel/Pousada Atalaia do Mariscal | Suíte Superior | COLETADO_COM_SUCESSO | R$ 30.600,00 | R$ 3.400,00 | R$ 2.720,00 | +R$ 1.412,77 | +122,1% | Referência, não entra em nenhuma média. Booking alertava "6 hotéis 4 estrelas já indisponíveis" |

**Alerta de qualidade da amostra:** mesma distorção da 7B — os 4 ausentes do núcleo incluem Riviera e Kia Ora (os mais caros), inflando o gap % vs. núcleo bruto.

### 2. Tabela da Villa — pacote

| Acomodação | Total motor pacote | Diária média motor | Total Booking estimado | Diária média Booking estimada | Mín. noites aplicado | Observação |
|---|---|---|---|---|---|---|
| Organic / Fuego / Metallo (base) | R$ 11.585,00 | R$ 1.287,22 | R$ 14.481,25 | R$ 1.609,03 | Variável (Natal mín. 5 / Réveillon mín. 7) | Noite 25/12 no bucket Natal (R$ 889), noites 26/12–02/01 (8 noites) no valor uniforme R$ 1.337 (Réveillon e Jan 1-3 coincidem) |

### 3. Resumo executivo — Rodada 8B

| Indicador | Valor |
|---|---|
| Núcleo disponível | 3 de 7 (42,9% — empatado com a 7B como o pior do conjunto) |
| Média núcleo Booking (diária) | R$ 948,15 |
| Mediana núcleo Booking | R$ 993,33 |
| Média motor equivalente núcleo | R$ 758,52 |
| Média ampliada Booking (n=1/2) | R$ 1.558,11 |
| Referência de teto | R$ 3.400,00 |
| Índice de disponibilidade total tentado | 50% (5/10) |
| **Sinal de demanda** | **ALTO** — 4 concorrentes núcleo indisponíveis, ampliada parcialmente esgotada, alerta explícito de escassez do Booking no teto |

### 4. Veredito de posicionamento — Rodada 8B

**`PROXIMA_DA_AMPLIADA`** — vs. núcleo bruto, Villa fica +69,7% acima (amostra fraca/enviesada, 3/7). Vs. ampliada, apenas +3,3% acima — leitura mais confiável desta rodada.

### 5. Diagnóstico preliminar — Rodada 8B

**`PROTEGER`** — janela mais longa e mais cara do conjunto, sinal de demanda ALTO, comparação núcleo pouco confiável por composição de amostra, proximidade forte com a ampliada não sustenta nenhuma baixa.

---

## Leitura específica — conjunto Natal + Réveillon

**A Pousada Arágua está bem posicionada para Natal (7A/7B)?**
Sim, de forma defensável. Nas duas sub-rodadas a Villa fica muito acima do núcleo bruto (+52,1% na 7A, +90,7% na 7B), mas o núcleo tem amostra fraca e enviesada — especialmente na 7B, onde faltam justamente os dois concorrentes mais caros (Riviera e Kia Ora). Frente à referência ampliada — leitura mais próxima do padrão real da Villa — o gap cai para +11,3% (7A) e +4,4% (7B), ambos defensáveis.

**A Pousada Arágua está bem posicionada para Réveillon (8A/8B)?**
Sim. A 8A tem a melhor amostra núcleo de todo o conjunto (85,7%) e mostra a Villa com premium de +42,9% sobre o núcleo, mas **abaixo** da ampliada (−10,2%) — posição confortável, não arriscada. A 8B (janela mais longa) repete o padrão de amostra núcleo fraca e enviesada, mas fica a apenas +3,3% da ampliada.

**O valor total do pacote está competitivo?**
Sim, no sentido de "competitivo dentro do padrão que a Villa disputa" (boutique/ampliada) — não no sentido de "mais barato que o núcleo". A Villa nunca aparece abaixo do núcleo ou da ampliada em nenhuma das 4 sub-rodadas.

**A diária média está defensável?**
Sim. Em todas as 4 sub-rodadas a diária média Booking da Villa fica entre −10,2% e +11,4% da referência ampliada — a comparação mais confiável, já que o núcleo bruto está distorcido pela ausência recorrente de Riviera e Kia Ora justamente nas janelas mais longas/de virada.

**Existe risco de estar barato demais?**
Não identificado em nenhuma das 4 sub-rodadas — a Villa está sempre acima do núcleo e próxima ou abaixo da ampliada, nunca abaixo dela.

**Existe risco de estar caro demais?**
Baixo. A única sub-rodada em que a Villa supera a ampliada é a 8A (+11,4% na leitura do agente sobre a diária, ainda assim bem abaixo do teto, que fica a mais de 2× o preço da Villa). Nas demais (7A, 7B, 8B) a Villa fica abaixo ou muito perto da ampliada. Combinado ao sinal de demanda ALTO consistente nas 4 sub-rodadas, o risco de perder reserva por preço é baixo.

**Alguma noite específica parece puxar o pacote de forma exagerada?**
Não, pela estrutura atual do motor. A tarifa é **plana dentro de cada bucket** — a noite de 24/12 recebe o mesmo valor das demais noites do bucket Natal (R$ 889), e a virada de 31/12 para 1/1 não tem prêmio, pois o bucket Réveillon (26-31 dez) e o bucket Janeiro 1-3 têm exatamente o mesmo valor (R$ 1.337). Nenhuma noite individual "puxa" o pacote para cima de forma desproporcional — mas isso também significa que a Villa não está capturando um possível prêmio adicional nas duas noites mais valiosas do calendário (24/12 e 31/12) frente ao resto do próprio bucket. Registrado como **ponto de atenção estrutural** para Renildo avaliar no futuro, não como recomendação de mudança agora. A única ambiguidade real de leitura de dado é a noite 18/12 na 7A (fronteira de bucket), já sinalizada.

**Faz sentido manter, proteger, subir, baixar ou apenas monitorar — Natal e Réveillon separadamente?**
- **Natal (7A/7B): `PROTEGER`.** Sinal de demanda ALTO nas duas sub-rodadas, inventário já classifica o bucket como "proteger", e a comparação mais confiável (vs. ampliada) mostra folga pequena e saudável (+4,4% a +11,3%).
- **Réveillon (8A/8B): `PROTEGER`.** Mesmo padrão — sinal de demanda ALTO, inventário já classifica como "proteger" ("avaliar junto com janeiro/2027"), e a Villa nunca ultrapassa a ampliada de forma preocupante.
- **Nota para rodadas futuras (não é recomendação de ação agora):** a escassez recorrente do núcleo nas janelas mais longas (7B e 8B, com apenas 3/7 disponíveis — a pior amostra de todo o Radar) é um sinal que, se repetido em rodadas futuras equivalentes, pode sustentar uma leitura de `SUBIR_COM_CAUTELA` — mas ainda não é dado suficiente para virar diagnóstico nesta rodada.

---

## Comparação com o padrão das rodadas anteriores

| Rodada | Período | Tipo | Gap vs. núcleo | Sinal de demanda | Diagnóstico |
|---|---|---|---|---|---|
| 1 | 04–08/09 | Feriado (7 Set) | +48,7% | MÉDIO/ALTO | MANTER/ESPERAR → PROTEGER/ESPERAR (1R) |
| 2 | 09–12/10 | Feriado (12 Out) | +48,3% | BAIXO | MANTER |
| 3 | 30/10–02/11 | Feriado (Finados) | +59,3%* | MÉDIO | MANTER |
| 4 | 19–22/11 | Feriado forte (Consc. Negra) | +54,9% | ALTO | PROTEGER |
| 5A | 06–08/11 | Comum (fim de semana) | +43,6% | MÉDIO | MANTER |
| 5B | 09–12/11 | Comum (meio de semana) | +47,8% | BAIXO | MANTER, ponto de atenção |
| 6A | 07–11/12 | Pré-alta (dias de semana) | +49,0% | MÉDIO | MANTER |
| 6B | 11–13/12 | Pré-alta (fim de semana) | +58,3% | ALTO | PROTEGER |
| **7A** | **18–24/12** | **Natal (janela)** | **+52,1%** | **ALTO** | **PROTEGER** |
| **7B** | **20–25/12** | **Natal (pacote principal)** | **+90,7%†** | **ALTO** | **PROTEGER** |
| **8A** | **27/12–03/01** | **Réveillon (pacote principal)** | **+42,9%** | **ALTO** | **PROTEGER** |
| **8B** | **25/12–03/01** | **Réveillon (janela completa)** | **+69,7%†** | **ALTO** | **PROTEGER** |

*gap parcialmente artefato de ausência do Kia Ora na amostra (ver Rodada 3).
†gap inflado por amostra núcleo enviesada (ausência de Riviera e Kia Ora, os concorrentes núcleo mais caros) — vs. ampliada, o gap real fica entre +3,3% e +4,4%.

O gap estrutural vs. núcleo se mantém elevado em todas as 12 rodadas, mas Natal/Réveillon é o primeiro bloco em que **todas as 4 sub-rodadas** registram sinal de demanda ALTO simultaneamente — nenhuma rodada anterior teve essa consistência.

---

## Dados que faltam

- Ritmo real de reservas/ocupação da Villa Arágua para dezembro/2026–janeiro/2027 (Stays) — o Radar mede só preço/disponibilidade de concorrente, não a demanda real pela Villa.
- Confirmação com Renildo de que os valores dos buckets "Natal/2026 19-25 dez" (R$ 889), "Réveillon/2026 26-31 dez" (R$ 1.337) e "Janeiro/2027 1-3" (R$ 1.337) são as tarifas corretas e ativas no motor hoje — tratar como "preço publicado a confirmar", não "aprovado".
- Fronteira da noite 18/12 (bucket "1-18" vs. bucket Natal) — tratada como "1-18" nesta rodada; vale confirmação futura com Renildo se o sistema realmente aplica dessa forma.
- Núcleo e ampliada da 7B e 8B seguem com amostra reduzida por indisponibilidade real na data — não é possível completar essas camadas nesta rodada; nova tentativa fica para rodada futura ou data adjacente.
- Morada do Guaruça ficou indisponível nas 4 sub-rodadas — sem dado de ampliada alternativo neste bloco além do UP Hotel Boutique.

---

## Conclusão

Nenhuma decisão nova foi gerada por este relatório. Nenhuma tarifa foi alterada. Nenhum card foi movido para `DECISOES_REVENUE_PENDENTES_VILLA_ARAGUA.md`. Todos os diagnósticos abaixo são preliminares — Renildo decide.

**Rodada 7A (Natal, janela 18–24/12):** `PROTEGER`
**Rodada 7B (Natal, pacote principal 20–25/12):** `PROTEGER`
**Rodada 8A (Réveillon, pacote principal 27/12–03/01):** `PROTEGER`
**Rodada 8B (janela completa 25/12–03/01):** `PROTEGER`

**Status deste relatório:** `RELATORIO_ANALITICO_SEM_ALTERACAO_TARIFARIA`
