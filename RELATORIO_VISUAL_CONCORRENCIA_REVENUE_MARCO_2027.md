# RELATÓRIO VISUAL — RADAR DE CONCORRÊNCIA REVENUE — POUSADA ARÁGUA (MARÇO 2027)

**Objetivo:** analisar o posicionamento da Pousada Arágua em março/2027, separando primeira quinzena, segunda quinzena e período pré-Páscoa, para avaliar se as tarifas atuais devem ser mantidas, protegidas ou se algum bloco merece simulação de tarifa tática. A Páscoa 2027 (feriado forte) será analisada separadamente em rodada futura — não foi misturada com março comum.

**Rodadas cobertas:**
- Rodada 12A — Primeira quinzena de março, 01–08/03/2027 (7 noites)
- Rodada 12B — Segunda quinzena de março, 15–22/03/2027 (7 noites)
- Rodada 12C — Pré-Páscoa, 22–26/03/2027 (4 noites) — não inclui Páscoa

**Produto Villa de referência:** Pousada Arágua — unidade base (Organic/Fuego/Metallo) · perfil casal (2 adultos, 0 crianças, 1 acomodação)
**Fontes:** `COLETAS_CONCORRENCIA_REVENUE.csv`, `CESTA_COMPETITIVA_REVENUE_VILLA_ARAGUA.md`, `ALERTAS_CONCORRENCIA_REVENUE.md`, `REGRAS_CONVERSAO_OTA_MOTOR_REVENUE.md`, `INVENTARIO_TARIFAS_PUBLICADAS_AGO2026_ABR2027.csv`
**Coleta:** 2026-07-29, via Booking (Claude in Chrome), preços públicos visíveis, sem login, sem clicar em reservar.
**Diagnóstico:** gerado via agente `villa-precificacao-calendario`, com consulta às skills `villa-aragua-pricing-revenue` e `villa-aragua-growth-marketer` — agente acionado de fato.
**Status deste relatório:** `RELATORIO_ANALITICO_SEM_ALTERACAO_TARIFARIA` — todos os diagnósticos abaixo são **preliminares**. Renildo decide.

**Villa Arágua no bloco:** motor R$ 607,00/diária (bucket único "Março/2027 base" do inventário, mín. 1-2, tipo "Pós-temporada", diagnóstico "manter") · Booking estimado R$ 758,75/diária. Tarifa **rigorosamente idêntica** nas 3 sub-rodadas — o inventário não fragmenta o bucket por quinzena. Este bucket é distinto do bucket "Semana Santa/Páscoa 2027" (R$ 595,00, classificado "corrigir agora" no inventário), que não faz parte desta rodada.

---

## RODADA 12A — Primeira quinzena de março, 01–08/03/2027 (7 noites)

### 1. Tabela aberta — concorrentes

| Grupo | Concorrente | Acomodação âncora | Status | Preço total Booking | Diária média Booking | Motor equivalente médio | Dif. R$ vs. Villa motor | Dif. % vs. Villa motor | Observação |
|---|---|---|---|---|---|---|---|---|---|
| NUCLEO | Pousada dos Ingleses | Quarto Duplo Clássico | COLETADO_COM_SUCESSO | R$ 2.442,00 + R$ 120,00 taxas | R$ 366,00 | R$ 292,80 | −R$ 392,75 | −51,8% | Taxa separada, já somada |
| NUCLEO | Vila Maciel | Apartamento Standard | COLETADO_COM_SUCESSO | R$ 2.945,00 | R$ 420,71 | R$ 336,57 | −R$ 338,04 | −44,5% | Sem desconto ativo nesta rodada |
| NUCLEO | Pousada Dom Capudi | Quarto Duplo | COLETADO_COM_SUCESSO | R$ 3.259,00 | R$ 465,57 | R$ 372,46 | −R$ 293,18 | −38,6% | — |
| NUCLEO | Pousada Kaloa Eco Village | Suíte Standard | COLETADO_COM_SUCESSO | R$ 3.462,00 | R$ 494,57 | R$ 395,66 | −R$ 264,18 | −34,8% | — |
| NUCLEO | Pousada Riviera Bombinhas | Suíte Loft Riviera | COLETADO_COM_SUCESSO | R$ 4.908,00 | R$ 701,14 | R$ 560,91 | −R$ 57,61 | −7,6% | — |
| NUCLEO | Pousada Kia Ora Bombinhas | Quarto Duplo Deluxe c/ Vista Lateral do Mar | COLETADO_COM_SUCESSO | R$ 5.097,00 | R$ 728,14 | R$ 582,51 | −R$ 30,61 | −4,0% | — |
| NUCLEO | Vila Boa Vida | — | PRECISA_VALIDACAO_MANUAL | INDISPONIVEL | — | — | — | — | Esgotada |
| AMPLIADA | UP Hotel Boutique | Quarto Duplo Deluxe com Banheira | COLETADO_COM_SUCESSO | R$ 4.182,00 (10% off; original R$ 4.646,00) | R$ 597,43 | R$ 477,94 | −R$ 161,32 | −21,3% | Amostra fraca (1 de 2) |
| AMPLIADA | Morada do Guaruça | — | PRECISA_VALIDACAO_MANUAL | INDISPONIVEL | — | — | — | — | Esgotada |
| TETO_MERCADO | Hotel/Pousada Atalaia do Mariscal | Suíte Superior | COLETADO_COM_SUCESSO | R$ 11.200,00 | R$ 1.600,00 | R$ 1.280,00 | +R$ 993,00 | +163,6% | Referência, não entra em nenhuma média. Sem aviso de escassez |

### 2. Tabela da Villa

| Acomodação | Total motor | Diária média motor | Total Booking estimado | Diária média Booking estimada | Mínimo de noites | Observação |
|---|---|---|---|---|---|---|
| Organic / Fuego / Metallo | R$ 4.249,00 | R$ 607,00 | R$ 5.311,25 | R$ 758,75 | 1-2 | Bucket "Março/2027 base" — publicado, não confirmado no Stays |

### 3. Resumo executivo — Rodada 12A

| Indicador | Valor |
|---|---|
| Núcleo disponível | 6 de 7 (85,7%) |
| Média núcleo Booking (diária) | R$ 529,36 |
| Mediana núcleo Booking | R$ 480,07 |
| Média motor equivalente núcleo | R$ 423,49 |
| Média ampliada Booking (n=1/2) | R$ 597,43 |
| Referência de teto | R$ 1.600,00 |
| Índice de disponibilidade total | 80% (8/10) |
| **Sinal de demanda** | **MÉDIO** — 1 núcleo indisponível (Vila Boa Vida) + ampliada pela metade (Morada indisponível), mas teto sem qualquer alerta de escassez |

### 4. Veredito de posicionamento — Rodada 12A

**`ACIMA_DO_NUCLEO_MAS_DEFENSAVEL`** — Villa +43,3% acima da média núcleo (+58,1% vs. mediana), +21,3% acima da ampliada (amostra fraca). Gap consistente com o padrão estrutural já visto desde a Rodada 1 do Radar.

### 5. Diagnóstico preliminar — Rodada 12A

**`MANTER`** — sem sinal de baixa demanda confirmado. Gap vs. núcleo alto mas dentro do padrão histórico já repetidamente registrado como não acionável isoladamente.

---

## RODADA 12B — Segunda quinzena de março, 15–22/03/2027 (7 noites)

### 1. Tabela aberta — concorrentes

| Grupo | Concorrente | Acomodação âncora | Status | Preço total Booking | Diária média Booking | Motor equivalente médio | Dif. R$ vs. Villa motor | Dif. % vs. Villa motor | Observação |
|---|---|---|---|---|---|---|---|---|---|
| NUCLEO | Vila Maciel | Apartamento Standard | COLETADO_COM_SUCESSO | R$ 2.708,00 | R$ 386,86 | R$ 309,49 | −R$ 371,89 | −49,0% | Sem desconto ativo; caiu de R$ 420,71 (12A) |
| NUCLEO | Pousada Dom Capudi | Quarto Duplo | COLETADO_COM_SUCESSO | R$ 3.259,00 | R$ 465,57 | R$ 372,46 | −R$ 293,18 | −38,6% | Idêntico a 12A |
| NUCLEO | Pousada Kaloa Eco Village | Suíte Standard | COLETADO_COM_SUCESSO | R$ 3.462,00 | R$ 494,57 | R$ 395,66 | −R$ 264,18 | −34,8% | Idêntico a 12A |
| NUCLEO | Pousada Kia Ora Bombinhas | Quarto Duplo Deluxe c/ Vista Lateral do Mar | COLETADO_COM_SUCESSO | R$ 4.950,00 | R$ 707,14 | R$ 565,71 | −R$ 51,61 | −6,8% | Caiu de R$ 728,14 (12A) |
| NUCLEO | Vila Boa Vida | — | PRECISA_VALIDACAO_MANUAL | INDISPONIVEL | — | — | — | — | Esgotada |
| NUCLEO | Pousada Riviera Bombinhas | — | PRECISA_VALIDACAO_MANUAL | INDISPONIVEL | — | — | — | — | Esgotada |
| NUCLEO | Pousada dos Ingleses | — | PRECISA_VALIDACAO_MANUAL | INDISPONIVEL (âncora) | — | — | — | — | Âncora esgotada |
| AMPLIADA | UP Hotel Boutique | Quarto Duplo Deluxe com Banheira | COLETADO_COM_SUCESSO | R$ 4.182,00 (10% off; original R$ 4.646,00) | R$ 597,43 | R$ 477,94 | −R$ 161,32 | −21,3% | Idêntico a 12A |
| AMPLIADA | Morada do Guaruça | — | PRECISA_VALIDACAO_MANUAL | INDISPONIVEL | — | — | — | — | Esgotada nas 3 sub-rodadas |
| TETO_MERCADO | Hotel/Pousada Atalaia do Mariscal | Suíte Superior | COLETADO_COM_SUCESSO | R$ 11.400,00 | R$ 1.628,57 | R$ 1.302,86 | +R$ 1.021,57 | +168,3% | Referência, não entra em nenhuma média. Sem aviso de escassez |

### 2. Tabela da Villa

| Acomodação | Total motor | Diária média motor | Total Booking estimado | Diária média Booking estimada | Mínimo de noites | Observação |
|---|---|---|---|---|---|---|
| Organic / Fuego / Metallo | R$ 4.249,00 | R$ 607,00 | R$ 5.311,25 | R$ 758,75 | 1-2 | Idêntico a 12A — mesmo bucket uniforme do inventário |

### 3. Resumo executivo — Rodada 12B

| Indicador | Valor |
|---|---|
| Núcleo disponível | 4 de 7 (57,1% — o pior índice de toda a série de março) |
| Média núcleo Booking (diária) | R$ 513,54 |
| Mediana núcleo Booking | R$ 480,07 |
| Média motor equivalente núcleo | R$ 410,83 |
| Média ampliada Booking (n=1/2) | R$ 597,43 |
| Referência de teto | R$ 1.628,57 |
| Índice de disponibilidade total | 60% (6/10) |
| **Sinal de demanda** | **MÉDIO/CONTRADITÓRIO** — disponibilidade núcleo caindo (pior índice do bloco) aponta pressão, mas preço nominal caindo nos concorrentes disponíveis e teto sem alerta — padrão semelhante à Rodada 11D (fevereiro), sem o agravante do teto esgotado |

### 4. Veredito de posicionamento — Rodada 12B

**`ACIMA_DO_NUCLEO_MAS_DEFENSAVEL`** — Villa +47,8% acima da média núcleo (+58,1% vs. mediana), +21,3% acima da ampliada (mesmo gap de 12A, ampliada idêntica).

### 5. Diagnóstico preliminar — Rodada 12B

**`MANTER`, com ponto de atenção** — amostra núcleo mais fraca do bloco de março (57,1%) e sinal contraditório. Não há zero esgotamento em todos os grupos (padrão que motivou a tarifa tática de novembro/2026) — há, ao contrário, mais esgotamento que em 12A, o que não sustenta leitura de demanda baixa confirmada. Recomenda-se nova rodada de coleta específica desta janela antes de qualquer leitura mais firme.

---

## RODADA 12C — Pré-Páscoa, 22–26/03/2027 (4 noites, não inclui Páscoa)

### 1. Tabela aberta — concorrentes

| Grupo | Concorrente | Acomodação âncora | Status | Preço total Booking | Diária média Booking | Motor equivalente médio | Dif. R$ vs. Villa motor | Dif. % vs. Villa motor | Observação |
|---|---|---|---|---|---|---|---|---|---|
| NUCLEO | Pousada dos Ingleses | Quarto Duplo Clássico | COLETADO_COM_SUCESSO | R$ 1.395,00 + R$ 120,00 taxas | R$ 378,75 | R$ 303,00 | −R$ 380,00 | −50,1% | Taxa separada, já somada; voltou a aparecer (esgotada em 12B) |
| NUCLEO | Vila Maciel | Apartamento Standard | COLETADO_COM_SUCESSO | R$ 1.710,00 | R$ 427,50 | R$ 342,00 | −R$ 331,25 | −43,7% | Sem desconto; subiu de R$ 386,86 (12B) — sinal de reaquecimento perto da Páscoa |
| NUCLEO | Pousada Dom Capudi | Quarto Duplo | COLETADO_COM_SUCESSO | R$ 1.824,00 | R$ 456,00 | R$ 364,80 | −R$ 302,75 | −39,9% | Caiu ligeiramente vs. R$ 465,57 |
| NUCLEO | Pousada Kaloa Eco Village | Suíte Standard | COLETADO_COM_SUCESSO | R$ 1.978,00 | R$ 494,50 | R$ 395,60 | −R$ 264,25 | −34,8% | Praticamente estável |
| NUCLEO | Pousada Kia Ora Bombinhas | Quarto Duplo Deluxe c/ Vista Lateral do Mar | COLETADO_COM_SUCESSO | R$ 2.657,00 | R$ 664,25 | R$ 531,40 | −R$ 94,50 | −12,5% | Caiu de R$ 707,14 (12B) |
| NUCLEO | Vila Boa Vida | — | PRECISA_VALIDACAO_MANUAL | INDISPONIVEL | — | — | — | — | Esgotada |
| NUCLEO | Pousada Riviera Bombinhas | — | PRECISA_VALIDACAO_MANUAL | INDISPONIVEL | — | — | — | — | Esgotada |
| AMPLIADA | UP Hotel Boutique | Quarto Duplo Deluxe com Banheira | COLETADO_COM_SUCESSO | R$ 2.867,00 (8% off; original R$ 3.116,00) | R$ 716,75 | R$ 573,40 | −R$ 42,00 | −5,5% | Gap mais estreito de toda a série de março; ampliada subiu ~20% frente a 12A/12B |
| AMPLIADA | Morada do Guaruça | — | PRECISA_VALIDACAO_MANUAL | INDISPONIVEL | — | — | — | — | Esgotada nas 3 sub-rodadas |
| TETO_MERCADO | Hotel/Pousada Atalaia do Mariscal | Suíte Superior | COLETADO_COM_SUCESSO | R$ 7.200,00 | R$ 1.800,00 | R$ 1.440,00 | +R$ 1.193,00 | +196,5% | Maior diária de toda a série de março. Referência, não entra em nenhuma média |

### 2. Tabela da Villa

| Acomodação | Total motor | Diária média motor | Total Booking estimado | Diária média Booking estimada | Mínimo de noites | Observação |
|---|---|---|---|---|---|---|
| Organic / Fuego / Metallo | R$ 2.428,00 | R$ 607,00 | R$ 3.035,00 | R$ 758,75 | 1-2 | Mesmo bucket "Março/2027 base" — Páscoa 2027 (bucket separado, R$ 595,00) fica fora desta janela |

### 3. Resumo executivo — Rodada 12C

| Indicador | Valor |
|---|---|
| Núcleo disponível | 5 de 7 (71,4%) |
| Média núcleo Booking (diária) | R$ 484,20 |
| Mediana núcleo Booking | R$ 456,00 |
| Média motor equivalente núcleo | R$ 387,36 |
| Média ampliada Booking (n=1/2) | R$ 716,75 |
| Referência de teto | R$ 1.800,00 |
| Índice de disponibilidade total | 70% (7/10) |
| **Sinal de demanda** | **MÉDIO, com tendência de aquecimento** — núcleo e ampliada subindo em termos nominais (Vila Maciel, Ingleses, UP mais caros que em 12B), consistente com a proximidade da Páscoa |

### 4. Veredito de posicionamento — Rodada 12C

**`PROXIMA_DA_AMPLIADA`** — gap de apenas 5,5% vs. ampliada, o mais estreito do bloco, refletindo aquecimento de demanda ao se aproximar do feriado.

### 5. Diagnóstico preliminar — Rodada 12C

**`PROTEGER`** — bloco funciona como antessala de um período forte já decidido (Páscoa 2027, `DECIDIDO_APLICADO` em `DECISOES_REVENUE_PENDENTES_VILLA_ARAGUA.md`, Card 1). Preços subindo (não caindo) nos concorrentes-chave, ampliada se aproximando da Villa, e nenhum sinal de baixa demanda.

---

## Leitura específica de março

**A primeira quinzena (12A) ainda está defensável?**
Sim. Gap vs. núcleo (+43,3%) e vs. ampliada (+21,3%) são coerentes com o padrão estrutural repetido em quase todas as rodadas do Radar desde setembro/2026 — nunca tratado isoladamente como motivo de baixa. Sinal de demanda MÉDIO, sem indisponibilidade generalizada.

**A segunda quinzena (12B) mostra queda de demanda?**
Mostra um sinal **misto**, não uma queda confirmada. De um lado, a disponibilidade núcleo caiu para 57,1% (pior índice de toda a série de março) — sob a lógica já usada no Radar, esgotamento aponta para mais pressão, não menos. De outro, os preços nominais dos concorrentes que seguem à venda caem (Vila Maciel, Kia Ora), e o teto segue sem qualquer alerta de escassez — isso é compatível com "pós-temporada" mais fraca. Não há como afirmar demanda baixa confirmada com esses dois sinais puxando em direções opostas.

**O pré-Páscoa (12C) deve ser mantido, protegido ou monitorado?**
**Protegido.** É o único bloco dos três com sinal de reaquecimento: núcleo e ampliada subindo em termos nominais, gap vs. ampliada mais estreito de toda a série (5,5%), e é a antessala direta da Páscoa 2027 (já decidida).

**Existe risco de diária zero em algum bloco?**
Nenhum dos três blocos apresenta o padrão que historicamente motivou preocupação real de vacância no Radar (esgotamento generalizado do próprio núcleo/ampliada/teto simultaneamente, como em fevereiro 11D). O gap alto vs. núcleo em 12A/12B (43–48%) já se repete desde a Rodada 1 sem evidência de que gere vacância — é característica de posicionamento, não sinal de risco agudo.

**A Villa está próxima da ampliada ou acima do mercado com risco — em cada sub-rodada?**
- 12A: −21,3% abaixo da ampliada — posição defensável, não classificada como risco.
- 12B: mesmo padrão de 12A (−21,3%), mas com amostra núcleo mais fraca.
- 12C: mais próxima da ampliada de toda a série (−5,5%) — posição forte, não de risco.
Em nenhum dos três blocos a Villa se enquadra em `ACIMA_DO_MERCADO_COM_RISCO` (esse veredito exigiria sinal de queda de preço + esgotamento simultâneo do teto, como em fevereiro/11D — não observado aqui).

**Faz sentido simular redução tática em algum bloco?**
**Não.** Nenhum dos três blocos atende ao critério que o precedente de novembro/2026 exige para justificar simulação: **zero esgotamento em todos os grupos (núcleo, ampliada e teto)**. Aqui, todos os três blocos têm pelo menos um concorrente núcleo indisponível e a ampliada pela metade (Morada esgotada nas três sub-rodadas). Simular redução sem esse pré-requisito repetiria o padrão já evitado em janeiro/2027 (Rodada 9D) e fevereiro/2027 (Rodada 11D), onde o sinal era MÉDIO/contraditório e não houve simulação.

**O melhor caminho é manter, proteger, subir, baixar, esperar ou comparar melhor — para cada uma das 3 sub-rodadas?**

| Sub-rodada | Diagnóstico preliminar |
|---|---|
| 12A (primeira quinzena) | `MANTER` |
| 12B (segunda quinzena) | `MANTER`, com ponto de atenção — recomenda-se nova coleta específica desta janela |
| 12C (pré-Páscoa) | `PROTEGER` |

---

## Riscos e observações

- Amostra núcleo de 12B é a mais fraca de toda a série de março (57,1%) — qualquer conclusão sobre esse bloco específico deve ser tratada como preliminar até nova rodada.
- Ampliada em todos os três blocos depende de um único concorrente (UP Hotel Boutique) — Morada do Guaruça esteve indisponível nas três sub-rodadas.
- Preço da Villa idêntico nas três sub-rodadas (bucket uniforme) — qualquer eventual ajuste futuro de régua para diferenciar quinzenas dentro de março precisaria de decisão explícita de Renildo.
- Não há evidência de campanha Meta Ads ou força de WhatsApp específica para março/2027 registrada nos arquivos-fonte.

---

## Dados que faltam

- Confirmação no Stays de que R$ 607,00 é de fato o valor ativo no motor para março/2027 (hoje é "preço publicado a confirmar").
- Coleta de Morada do Guaruça (ampliada) — esteve indisponível nas três sub-rodadas, enfraquecendo a leitura de ampliada.
- Coleta de Vila Boa Vida (núcleo) — indisponível nas três sub-rodadas, reduzindo a amostra núcleo de forma consistente.
- Dado de ritmo de reservas diretas/WhatsApp específico para março/2027.
- Nova rodada de coleta para 12B especificamente, dado o índice de disponibilidade núcleo mais fraco de toda a série.

---

## Conclusão

Nenhuma decisão nova foi gerada por este relatório. Nenhuma tarifa foi alterada. Nenhum card foi criado ou movido em `DECISOES_REVENUE_PENDENTES_VILLA_ARAGUA.md`. Nenhuma simulação de redução tática foi rodada — critério de sinal BAIXO confirmado (zero esgotamento em todos os grupos) não foi atingido em nenhum dos três blocos.

**Rodada 12A (primeira quinzena, 01–08/03):** `MANTER`
**Rodada 12B (segunda quinzena, 15–22/03):** `MANTER` (ponto de atenção)
**Rodada 12C (pré-Páscoa, 22–26/03):** `PROTEGER`

**Status deste relatório:** `RELATORIO_ANALITICO_SEM_ALTERACAO_TARIFARIA`
