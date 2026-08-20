# RELATÓRIO VISUAL — RADAR DE CONCORRÊNCIA REVENUE — POUSADA ARÁGUA (FEVEREIRO 2027 FORA DO CARNAVAL)

**Objetivo:** analisar o posicionamento da Pousada Arágua no restante de fevereiro/2027, separando pré-Carnaval, pós-Carnaval imediato, segunda metade e final do mês. O Carnaval 2027 já foi analisado separadamente (Rodada 10, diagnóstico `PROTEGER`, ver `RELATORIO_VISUAL_CONCORRENCIA_REVENUE_CARNAVAL_2027.md`).

**Rodadas cobertas:**
- Rodada 11A — Pré-Carnaval, 01–05/02/2027 (4 noites)
- Rodada 11B — Pós-Carnaval imediato, 10–17/02/2027 (7 noites)
- Rodada 11C — Segunda metade de fevereiro, 17–24/02/2027 (7 noites)
- Rodada 11D — Final de fevereiro, 24–28/02/2027 (4 noites)

**Produto Villa de referência:** Pousada Arágua — unidade base (Organic/Fuego/Metallo) · perfil casal (2 adultos, 0 crianças, 1 acomodação)
**Fontes:** `COLETAS_CONCORRENCIA_REVENUE.csv`, `CESTA_COMPETITIVA_REVENUE_VILLA_ARAGUA.md`, `ALERTAS_CONCORRENCIA_REVENUE.md`, `REGRAS_CONVERSAO_OTA_MOTOR_REVENUE.md`, `INVENTARIO_TARIFAS_PUBLICADAS_AGO2026_ABR2027.csv`, `RELATORIO_VISUAL_CONCORRENCIA_REVENUE_CARNAVAL_2027.md`
**Coleta:** 2026-07-28, via Booking (Claude in Chrome), preços públicos visíveis, sem login, sem clicar em reservar.
**Diagnóstico:** gerado via agente `villa-precificacao-calendario`, com consulta às skills `villa-aragua-pricing-revenue` e `villa-aragua-growth-marketer` — agente acionado de fato.
**Status deste relatório:** `RELATORIO_ANALITICO_SEM_ALTERACAO_TARIFARIA` — todos os diagnósticos abaixo são **preliminares**. Renildo decide.

**Villa Arágua no bloco:** motor R$ 822,00/diária (bucket único "Fevereiro/2027 base" do inventário, mín. 3, tipo "Alta/pós-alta", diagnóstico "manter") · Booking estimado R$ 1.027,50/diária. Tarifa **rigorosamente idêntica** nas 4 sub-rodadas — o inventário não fragmenta o bucket por semana.

---

## RODADA 11A — Pré-Carnaval, 01–05/02/2027 (4 noites)

### 1. Tabela aberta — concorrentes

| Grupo | Concorrente | Acomodação âncora | Status | Preço total Booking | Diária média Booking | Motor equivalente médio | Dif. R$ vs. Villa motor | Dif. % vs. Villa motor | Observação |
|---|---|---|---|---|---|---|---|---|---|
| NUCLEO | Vila Maciel | Apartamento Standard | COLETADO_COM_SUCESSO | R$ 2.470,00 | R$ 617,50 | R$ 494,00 | −R$ 328,00 | −39,9% | Sem desconto ativo nesta rodada |
| NUCLEO | Pousada Kaloa Eco Village | Suíte Standard | COLETADO_COM_SUCESSO | R$ 2.990,00 | R$ 747,50 | R$ 598,00 | −R$ 224,00 | −27,3% | — |
| NUCLEO | Pousada Dom Capudi | Quarto Duplo | COLETADO_COM_SUCESSO | R$ 3.325,00 | R$ 831,25 | R$ 665,00 | −R$ 157,00 | −19,1% | — |
| NUCLEO | Pousada Kia Ora Bombinhas | Quarto Duplo Deluxe c/ Vista Lateral do Mar | COLETADO_COM_SUCESSO | R$ 4.222,00 | R$ 1.055,50 | R$ 844,40 | +R$ 22,40 | +2,7% | Praticamente empatada com a Villa |
| NUCLEO | Vila Boa Vida | — | PRECISA_VALIDACAO_MANUAL | INDISPONIVEL | — | — | — | — | Esgotada |
| NUCLEO | Pousada Riviera Bombinhas | — | PRECISA_VALIDACAO_MANUAL | INDISPONIVEL | — | — | — | — | Esgotada |
| NUCLEO | Pousada dos Ingleses | — | PRECISA_VALIDACAO_MANUAL | INDISPONIVEL (âncora) | — | — | — | — | Âncora esgotada |
| AMPLIADA | UP Hotel Boutique | Quarto Duplo Deluxe com Banheira | COLETADO_COM_SUCESSO | R$ 4.725,00 | R$ 1.181,25 | R$ 945,00 | −R$ 123,00 | −13,0% | Único disponível do grupo |
| AMPLIADA | Morada do Guaruça | — | PRECISA_VALIDACAO_MANUAL | INDISPONIVEL | — | — | — | — | Esgotada |
| TETO_MERCADO | Hotel/Pousada Atalaia do Mariscal | Suíte Superior | PRECISA_VALIDACAO_MANUAL | DADO_NAO_ENCONTRADO | — | — | — | — | Âncora indisponível; só restava plano de ocupação single (1 pessoa), não comparável ao perfil casal |

### 2. Tabela da Villa

| Acomodação | Total motor | Diária média motor | Total Booking estimado | Diária média Booking estimada | Mínimo de noites | Observação |
|---|---|---|---|---|---|---|
| Organic / Fuego / Metallo | R$ 3.288,00 | R$ 822,00 | R$ 4.110,00 | R$ 1.027,50 | Inventário: mín. 3; busca real: 4 | Tarifa idêntica em todas as 4 sub-rodadas de fevereiro |

### 3. Resumo executivo — Rodada 11A

| Indicador | Valor |
|---|---|
| Núcleo disponível | 4 de 7 (57,1%) |
| Média núcleo Booking (diária) | R$ 812,94 |
| Mediana núcleo Booking | R$ 789,38 |
| Média motor equivalente núcleo | R$ 650,35 |
| Média ampliada Booking (n=1) | R$ 1.181,25 |
| Referência de teto | DADO_NAO_ENCONTRADO |
| Índice de disponibilidade total | 50,0% (5/10) |
| **Sinal de demanda** | **ALTO** — 3 de 7 do núcleo esgotados (43%, mesma magnitude do próprio Carnaval), e a categoria comparável do teto ficou inacessível ao perfil casal |

### 4. Veredito de posicionamento — Rodada 11A

**`ACIMA_DO_NUCLEO_MAS_DEFENSAVEL`** — Villa +26,4% acima da média motor núcleo, mas praticamente empatada com Kia Ora (+2,7%) e abaixo da ampliada/UP (−13,0%).

### 5. Diagnóstico preliminar — Rodada 11A

**`PROTEGER`** — datas coladas imediatamente antes do Carnaval (já `PROTEGER`), com esgotamento de núcleo no mesmo patamar do próprio feriado e teto inacessível ao perfil padrão.

---

## RODADA 11B — Pós-Carnaval imediato, 10–17/02/2027 (7 noites)

### 1. Tabela aberta — concorrentes

| Grupo | Concorrente | Acomodação âncora | Status | Preço total Booking | Diária média Booking | Motor equivalente médio | Dif. R$ vs. Villa motor | Dif. % vs. Villa motor | Observação |
|---|---|---|---|---|---|---|---|---|---|
| NUCLEO | Vila Maciel | Apartamento Standard | COLETADO_COM_SUCESSO | R$ 2.953,00 (26% off; original R$ 3.990,00) | R$ 421,86 | R$ 337,49 | −R$ 484,51 | −58,9% | Desconto ativo — sinal de dificuldade de venda própria |
| NUCLEO | Pousada Kaloa Eco Village | Suíte Standard | COLETADO_COM_SUCESSO | R$ 5.233,00 | R$ 747,57 | R$ 598,06 | −R$ 223,94 | −27,2% | — |
| NUCLEO | Pousada Dom Capudi | Quarto Duplo | COLETADO_COM_SUCESSO | R$ 5.444,00 | R$ 777,71 | R$ 622,17 | −R$ 199,83 | −24,3% | — |
| NUCLEO | Pousada Riviera Bombinhas | Suíte Loft Riviera | COLETADO_COM_SUCESSO | R$ 6.845,00 | R$ 978,00 | R$ 782,40 | −R$ 39,60 | −4,8% | Voltou a aparecer disponível (esgotada em 11A) |
| NUCLEO | Pousada Kia Ora Bombinhas | Quarto Duplo Deluxe c/ Vista Lateral do Mar | COLETADO_COM_SUCESSO | R$ 7.388,00 | R$ 1.055,43 | R$ 844,34 | +R$ 22,34 | +2,6% | Praticamente empatado com a Villa |
| NUCLEO | Vila Boa Vida | — | PRECISA_VALIDACAO_MANUAL | INDISPONIVEL | — | — | — | — | Esgotada |
| NUCLEO | Pousada dos Ingleses | — | PRECISA_VALIDACAO_MANUAL | INDISPONIVEL (âncora) | — | — | — | — | Âncora esgotada |
| AMPLIADA | UP Hotel Boutique | Quarto Duplo Deluxe com Banheira | COLETADO_COM_SUCESSO | R$ 5.749,00 | R$ 821,29 | R$ 657,03 | −R$ 164,97 | −20,1% | Único disponível do grupo |
| AMPLIADA | Morada do Guaruça | — | PRECISA_VALIDACAO_MANUAL | INDISPONIVEL | — | — | — | — | Esgotada |
| TETO_MERCADO | Hotel/Pousada Atalaia do Mariscal | Suíte Superior | COLETADO_COM_SUCESSO | R$ 18.200,00 | R$ 2.600,00 | R$ 2.080,00 | +R$ 1.258,00 | +153,0% | Referência, não entra em média. Sem aviso de escassez |

### 2. Tabela da Villa

| Acomodação | Total motor | Diária média motor | Total Booking estimado | Diária média Booking estimada | Mínimo de noites | Observação |
|---|---|---|---|---|---|---|
| Organic / Fuego / Metallo | R$ 5.754,00 | R$ 822,00 | R$ 7.192,50 | R$ 1.027,50 | Inventário: mín. 3; busca real: 7 | Idêntico a 11A/11C/11D |

### 3. Resumo executivo — Rodada 11B

| Indicador | Valor |
|---|---|
| Núcleo disponível | 5 de 7 (71,4%) |
| Média núcleo Booking (diária) | R$ 796,11 |
| Mediana núcleo Booking | R$ 777,71 |
| Média motor equivalente núcleo | R$ 636,89 |
| Média ampliada Booking (n=1) | R$ 821,29 |
| Referência de teto | R$ 2.600,00 |
| Índice de disponibilidade total | 70,0% (7/10) |
| **Sinal de demanda** | **MÉDIO** — disponibilidade núcleo sobe (57,1%→71,4%) e teto volta sem alerta de escassez, mas Kaloa e Kia Ora mantêm preço idêntico a 11A — sem queda generalizada |

### 4. Veredito de posicionamento — Rodada 11B

**`ACIMA_DO_NUCLEO_MAS_DEFENSAVEL`** — Villa +29,1% acima da média núcleo, quase empatada com Riviera (−4,8%) e Kia Ora (+2,6%). Agora acima da ampliada (+20,1%, diferente de 11A).

### 5. Diagnóstico preliminar — Rodada 11B

**`MANTER`** — sinal MÉDIO, sem confirmação de queda de demanda suficiente para qualquer ação. Não repete a lógica de novembro/2026 (que exigia sinal BAIXO confirmado, zero esgotamento em todos os grupos).

---

## RODADA 11C — Segunda metade de fevereiro, 17–24/02/2027 (7 noites)

### 1. Tabela aberta — concorrentes

| Grupo | Concorrente | Acomodação âncora | Status | Preço total Booking | Diária média Booking | Motor equivalente médio | Dif. R$ vs. Villa motor | Dif. % vs. Villa motor | Observação |
|---|---|---|---|---|---|---|---|---|---|
| NUCLEO | Vila Maciel | Apartamento Standard | COLETADO_COM_SUCESSO | R$ 2.636,00 (26% off; original R$ 3.563,00) | R$ 376,57 | R$ 301,26 | −R$ 520,74 | −63,3% | Preço nominal caindo (era R$ 421,86 em 11B) |
| NUCLEO | Pousada dos Ingleses | Quarto Duplo Clássico | COLETADO_COM_SUCESSO | R$ 2.823,00 + R$ 120,00 taxas | R$ 420,43 | R$ 336,34 | −R$ 485,66 | −59,1% | Voltou a aparecer disponível (esgotada em 11A/11B) |
| NUCLEO | Pousada Dom Capudi | Quarto Duplo | COLETADO_COM_SUCESSO | R$ 5.187,00 | R$ 741,00 | R$ 592,80 | −R$ 229,20 | −27,9% | Preço caindo levemente (era R$ 777,71 em 11B) |
| NUCLEO | Pousada Kaloa Eco Village | Suíte Standard | COLETADO_COM_SUCESSO | R$ 5.233,00 | R$ 747,57 | R$ 598,06 | −R$ 223,94 | −27,2% | Idêntico a 11B — sem queda |
| NUCLEO | Pousada Riviera Bombinhas | Suíte Loft Riviera | COLETADO_COM_SUCESSO | R$ 6.845,00 | R$ 978,00 | R$ 782,40 | −R$ 39,60 | −4,8% | Idêntico a 11B — sem queda |
| NUCLEO | Pousada Kia Ora Bombinhas | Quarto Duplo Deluxe c/ Vista Lateral do Mar | COLETADO_COM_SUCESSO | R$ 7.388,00 | R$ 1.055,43 | R$ 844,34 | +R$ 22,34 | +2,6% | Idêntico a 11B — sem queda |
| NUCLEO | Vila Boa Vida | — | PRECISA_VALIDACAO_MANUAL | INDISPONIVEL | — | — | — | — | Único núcleo ainda esgotado |
| AMPLIADA | UP Hotel Boutique | Quarto Duplo Deluxe com Banheira | COLETADO_COM_SUCESSO | R$ 5.749,00 | R$ 821,29 | R$ 657,03 | −R$ 164,97 | −20,1% | Idêntico a 11B |
| AMPLIADA | Morada do Guaruça | — | PRECISA_VALIDACAO_MANUAL | INDISPONIVEL | — | — | — | — | Esgotada nas 4 sub-rodadas |
| TETO_MERCADO | Hotel/Pousada Atalaia do Mariscal | Suíte Superior | COLETADO_COM_SUCESSO | R$ 18.200,00 | R$ 2.600,00 | R$ 2.080,00 | +R$ 1.258,00 | +153,0% | Idêntico a 11B, referência, não entra em média |

### 2. Tabela da Villa

| Acomodação | Total motor | Diária média motor | Total Booking estimado | Diária média Booking estimada | Mínimo de noites | Observação |
|---|---|---|---|---|---|---|
| Organic / Fuego / Metallo | R$ 5.754,00 | R$ 822,00 | R$ 7.192,50 | R$ 1.027,50 | Inventário: mín. 3; busca real: 7 | Idêntico a 11B |

### 3. Resumo executivo — Rodada 11C

| Indicador | Valor |
|---|---|
| Núcleo disponível | 6 de 7 (85,7%) |
| Média núcleo Booking (diária) | R$ 719,83 |
| Mediana núcleo Booking | R$ 744,29 |
| Média motor equivalente núcleo | R$ 575,87 |
| Média ampliada Booking (n=1) | R$ 821,29 |
| Referência de teto | R$ 2.600,00 |
| Índice de disponibilidade total | 80,0% (8/10) |
| **Sinal de demanda** | **MÉDIO, com tendência de amolecimento** — disponibilidade núcleo sobe para 85,7%; Vila Maciel e Dom Capudi seguem em queda nominal; mas Kaloa, Riviera, Kia Ora, UP e Atalaia seguem no mesmo patamar de 11B — sem queda generalizada de preço |

### 4. Veredito de posicionamento — Rodada 11C

**`ACIMA_DO_NUCLEO_MAS_DEFENSAVEL`** — Villa +42,7% acima da média núcleo (maior gap até aqui, puxado por Vila Maciel e Ingleses). Frente aos pares mais próximos (Kia Ora +2,6%, Riviera −4,8%), a defensibilidade se mantém.

### 5. Diagnóstico preliminar — Rodada 11C

**`MANTER`, com ponto de atenção** — mesma leitura já usada em janeiro (Rodada 9D): concorrentes reduzem preço nominal e abrem disponibilidade, mas ainda não há sinal BAIXO confirmado (nenhum grupo com 100% de disponibilidade; teto sustenta preço pleno sem desconto).

---

## RODADA 11D — Final de fevereiro, 24–28/02/2027 (4 noites)

### 1. Tabela aberta — concorrentes

| Grupo | Concorrente | Acomodação âncora | Status | Preço total Booking | Diária média Booking | Motor equivalente médio | Dif. R$ vs. Villa motor | Dif. % vs. Villa motor | Observação |
|---|---|---|---|---|---|---|---|---|---|
| NUCLEO | Vila Maciel | Apartamento Standard | COLETADO_COM_SUCESSO | R$ 1.710,00 | R$ 427,50 | R$ 342,00 | −R$ 480,00 | −58,4% | Sem desconto ativo e ainda assim o preço nominal mais baixo do conjunto das 4 sub-rodadas |
| NUCLEO | Pousada dos Ingleses | Quarto Duplo Clássico | COLETADO_COM_SUCESSO | R$ 1.613,00 + R$ 120,00 taxas | R$ 433,25 | R$ 346,60 | −R$ 475,40 | −57,8% | Preço nominal mais baixo do conjunto das 4 sub-rodadas |
| NUCLEO | Pousada Dom Capudi | Quarto Duplo | COLETADO_COM_SUCESSO | R$ 2.964,00 | R$ 741,00 | R$ 592,80 | −R$ 229,20 | −27,9% | Idêntico a 11C |
| NUCLEO | Pousada Kaloa Eco Village | Suíte Standard | COLETADO_COM_SUCESSO | R$ 2.990,00 | R$ 747,50 | R$ 598,00 | −R$ 224,00 | −27,3% | Idêntico a 11A |
| NUCLEO | Pousada Kia Ora Bombinhas | Quarto Duplo Deluxe c/ Vista Lateral do Mar | COLETADO_COM_SUCESSO | R$ 4.222,00 | R$ 1.055,50 | R$ 844,40 | +R$ 22,40 | +2,7% | Único concorrente sempre acima/empatado com a Villa nas 4 sub-rodadas |
| NUCLEO | Vila Boa Vida | — | PRECISA_VALIDACAO_MANUAL | INDISPONIVEL | — | — | — | — | Esgotada |
| NUCLEO | Pousada Riviera Bombinhas | — | PRECISA_VALIDACAO_MANUAL | INDISPONIVEL | — | — | — | — | Esgotada |
| AMPLIADA | UP Hotel Boutique | Quarto Duplo Deluxe com Banheira | COLETADO_COM_SUCESSO | R$ 2.813,00 | R$ 703,25 | R$ 562,60 | −R$ 259,40 | −31,6% | Preço nominal bem mais baixo que 11A/11B/11C — maior queda de todo o conjunto |
| AMPLIADA | Morada do Guaruça | — | PRECISA_VALIDACAO_MANUAL | INDISPONIVEL | — | — | — | — | Esgotada nas 4 sub-rodadas |
| TETO_MERCADO | Hotel/Pousada Atalaia do Mariscal | Suíte Superior | PRECISA_VALIDACAO_MANUAL | **INDISPONIVEL — 100% esgotado** | — | — | — | — | **DADO_NAO_ENCONTRADO.** Primeira vez em toda a série histórica do Radar (Rodadas 1–11C) que o próprio teto de mercado aparece totalmente esgotado |

### 2. Tabela da Villa

| Acomodação | Total motor | Diária média motor | Total Booking estimado | Diária média Booking estimada | Mínimo de noites | Observação |
|---|---|---|---|---|---|---|
| Organic / Fuego / Metallo | R$ 3.288,00 | R$ 822,00 | R$ 4.110,00 | R$ 1.027,50 | Inventário: mín. 3; busca real: 4 | Idêntico a 11A |

### 3. Resumo executivo — Rodada 11D

| Indicador | Valor |
|---|---|
| Núcleo disponível | 5 de 7 (71,4%) |
| Média núcleo Booking (diária) | R$ 680,95 |
| Mediana núcleo Booking | R$ 741,00 |
| Média motor equivalente núcleo | R$ 544,76 |
| Média ampliada Booking (n=1) | R$ 703,25 |
| Referência de teto | DADO_NAO_ENCONTRADO — esgotado, sem plano alternativo |
| Índice de disponibilidade total | 60,0% (6/10) |
| **Sinal de demanda** | **MISTO/CONTRADITÓRIO — não classificável como BAIXO nem ALTO com segurança.** Núcleo com preços nominais mais baixos de toda a série (Vila Maciel e Ingleses) e ampliada (UP) também caindo forte; ao mesmo tempo, o teto de mercado vende tudo — sinal inédito em toda a série |

### 4. Veredito de posicionamento — Rodada 11D

**`ACIMA_DO_MERCADO_COM_RISCO`** — Villa +50,9% acima da média núcleo e +46,1% acima da diária Booking da ampliada, o maior gap das 4 sub-rodadas em ambas as comparações. Único concorrente ainda próximo é Kia Ora (+2,7%); todos os demais, inclusive a ampliada, agora estão bem abaixo da Villa. Sem referência de teto disponível para calibrar headroom acima.

### 5. Diagnóstico preliminar — Rodada 11D

**`MANTER`, com ponto de atenção forte** — não classificado como `BAIXAR_COM_JUSTIFICATIVA` e sem simulação de redução, porque o sinal não é um BAIXO confirmado no padrão do precedente de novembro/2026 (que exigia zero esgotamento em núcleo/ampliada/teto simultaneamente). Aqui o teto está 100% esgotado — o oposto do padrão de novembro. Há dois movimentos de mercado diferentes acontecendo ao mesmo tempo, não resolvidos por este relatório.

**Por que não simular redução aqui:** o critério definido para esta rodada era "sinal de demanda BAIXO confirmado". O sinal aqui é contraditório, não baixo — a queda nominal em Vila Maciel/Ingleses/UP pode refletir esforço desses concorrentes específicos para vender antes do fim do mês, enquanto o esgotamento total do Atalaia sugere demanda forte concentrada nesse período (possivelmente evento pontual não identificado). Simular redução sobre um sinal ambíguo, sem confirmação, contrariaria o próprio critério estabelecido para acionar simulação.

---

## Leitura específica de fevereiro

**O pré-Carnaval (11A) deve ser protegido por estar colado no feriado?**
Sim. Esgotamento de núcleo (43%) no mesmo patamar do próprio Carnaval e teto inacessível ao perfil casal padrão são sinais concretos de demanda alta por spillover de reservas antecipadas de Carnaval.

**O pós-Carnaval imediato (11B) mostra queda de demanda?**
Parcialmente. A disponibilidade do núcleo sobe (57,1%→71,4%) e o teto volta a vender sem alerta de escassez — sinal de esfriamento em relação a 11A. Mas Kaloa e Kia Ora mantêm exatamente o mesmo preço de 11A, sem desconto — não há queda de demanda generalizada, apenas parcial e concentrada em alguns concorrentes.

**A segunda metade de fevereiro (11C) ainda se comporta como alta temporada?**
De forma mista. A disponibilidade do núcleo já está em 85,7% e dois concorrentes (Vila Maciel, Dom Capudi) seguem caindo nominal. Mas os concorrentes de padrão mais próximo da Villa (Kaloa, Riviera, Kia Ora) e o teto (Atalaia) permanecem exatamente no mesmo preço de 11B, sem nenhum desconto — o "núcleo duro" do mercado ainda segura o patamar de alta temporada, mesmo com mais quartos abertos.

**O final de fevereiro (11D) mostra risco de diária zero?**
Não há esse risco na leitura da Villa (a tarifa é fixa pelo bucket, sem sinal de necessidade de zerar). Mas há um risco de **posicionamento**: a Villa está, nesta sub-rodada, no ponto mais distante de toda a concorrência comparável (núcleo e ampliada), com exceção de Kia Ora. Ao mesmo tempo, o teto vendeu 100% — o dado mais forte de demanda de toda a série. Este contraste não deve ser resolvido de forma forçada; é matéria para nova rodada de coleta mais próxima da data e para leitura de ocupação real da própria Villa.

**A Villa está acima do núcleo, próxima da ampliada ou acima do mercado com risco — em cada sub-rodada?**

| Sub-rodada | Posição |
|---|---|
| 11A | Acima do núcleo, mas defensável (quase empatada com Kia Ora; abaixo da ampliada/UP) |
| 11B | Acima do núcleo, mas defensável (quase empatada com Riviera e Kia Ora; agora acima da ampliada) |
| 11C | Acima do núcleo, mas defensável (maior gap frente à média, ainda defensável frente a Kia Ora/Riviera) |
| 11D | Acima do mercado com risco (maior gap de toda a série frente a núcleo e ampliada; só Kia Ora segue próxima) |

**Faz sentido simular redução tática em algum bloco?**
Não, em nenhum dos 4 blocos. Nenhum atinge o critério de sinal `BAIXO` confirmado (zero esgotamento em núcleo/ampliada/teto simultaneamente, como em novembro/2026). 11A e 11B têm sinal ALTO/MÉDIO com esgotamento real em pelo menos um grupo. 11C tem sinal MÉDIO com amolecimento parcial, mas teto e núcleo de padrão mais próximo seguem sem desconto. 11D tem sinal contraditório (núcleo/ampliada caindo, mas teto 100% esgotado) — justamente o oposto do padrão que autorizaria simulação.

**Faz sentido proteger algum bloco?**
Sim — 11A, pela adjacência direta ao Carnaval e esgotamento no mesmo patamar do próprio feriado.

**O melhor caminho é manter, proteger, subir, baixar, esperar ou comparar melhor — para cada uma das 4 sub-rodadas?**

| Sub-rodada | Diagnóstico preliminar |
|---|---|
| 11A (pré-Carnaval) | `PROTEGER` |
| 11B (pós-Carnaval imediato) | `MANTER` |
| 11C (segunda metade) | `MANTER`, com ponto de atenção |
| 11D (final de fevereiro) | `MANTER`, com ponto de atenção forte |

---

## Riscos e observações (leitura comercial)

- Comparação sempre "visível vs. visível, mesmo canal" e "motor vs. motor equivalente", nunca cruzando as duas bases, conforme `REGRAS_CONVERSAO_OTA_MOTOR_REVENUE.md`.
- Nenhum dos 4 blocos recebeu `BAIXAR_COM_JUSTIFICATIVA`, então a leitura de `reserva-direta-reducao-otas.md` não é obrigatória para justificar decisão nesta rodada — mas fica registrado como pano de fundo: mesmo com Vila Maciel e Ingleses bem mais baratos no Booking em todas as sub-rodadas, a Villa compete por reserva direta, atendimento próximo e valor percebido, não por igualar tarifa de OTA de produto de padrão mais simples.
- Morada do Guaruça esteve esgotada nas 4 sub-rodadas — padrão consistente, não um evento pontual desta rodada.
- Vila Maciel usa desconto promocional em 11B e 11C (26% off) mas não em 11A e 11D — variação promocional própria do concorrente, não do mercado como um todo.

---

## Dados que faltam

- Ocupação real da Pousada Arágua para fevereiro/2027 — esta análise é 100% competitiva, sem dado de demanda própria da Villa.
- Confirmação no sistema Stays de que R$ 822,00/diária (bucket "Fevereiro/2027 base") está de fato aplicado linha a linha no motor — os valores do inventário são "preço publicado a confirmar", não "preço aprovado".
- Explicação para o esgotamento total do Atalaia em 11D (evento pontual, grupo fechado, ou demanda regional real) — não investigável a partir dos dados disponíveis.
- Vila dos Açores segue sem coleta/validação (`PENDENTE`).
- Nenhuma evidência de campanha Meta Ads específica para este período.

---

## Conclusão

Nenhuma decisão nova foi gerada por este relatório. Nenhuma tarifa foi alterada. Nenhum card foi criado ou movido em `DECISOES_REVENUE_PENDENTES_VILLA_ARAGUA.md`.

**Rodada 11A (pré-Carnaval, 01–05/02):** `PROTEGER`
**Rodada 11B (pós-Carnaval imediato, 10–17/02):** `MANTER`
**Rodada 11C (segunda metade, 17–24/02):** `MANTER`, com ponto de atenção
**Rodada 11D (final de fevereiro, 24–28/02):** `MANTER`, com ponto de atenção forte

**Status deste relatório:** `RELATORIO_ANALITICO_SEM_ALTERACAO_TARIFARIA`
