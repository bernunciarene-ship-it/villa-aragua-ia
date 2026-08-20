# Radar de Concorrência Revenue — Abril 2027 (Pousada Arágua)

**Formato enxuto — duas amostras representativas.** Canal: Booking. Perfil: casal, 2 adultos, 0 crianças, 1 acomodação. Produto de referência: base Organic/Fuego/Metallo.

**Status do relatório:** `RELATORIO_ANALITICO_SEM_ALTERACAO_TARIFARIA`. Diagnóstico apenas preliminar. Nenhuma tarifa foi alterada. Nenhuma decisão foi criada automaticamente. Nada foi movido para `DECISOES_REVENUE_PENDENTES_VILLA_ARAGUA.md`.

## Confirmação de governança

- Agente `villa-precificacao-calendario` acionado: **SIM** (invocação real nesta sessão).
- Skill `villa-aragua-pricing-revenue` consultada pelo agente: **SIM**.
- Skill `villa-aragua-growth-marketer` consultada: não foi necessária (diagnóstico é de precificação, não de marketing).
- Arquivos consultados: `CESTA_COMPETITIVA_REVENUE_VILLA_ARAGUA.md`, `COLETAS_CONCORRENCIA_REVENUE.csv`, `ALERTAS_CONCORRENCIA_REVENUE.md`, `REGRAS_CONVERSAO_OTA_MOTOR_REVENUE.md`, `INVENTARIO_TARIFAS_PUBLICADAS_AGO2026_ABR2027.csv` (bucket "Abril/2027"), `DECISOES_REVENUE_PENDENTES_VILLA_ARAGUA.md`, relatórios visuais anteriores como referência de formato.
- Regras aplicadas: conversão Booking→motor (÷1,25), separação NÚCLEO/AMPLIADA/TETO_MERCADO/PENDENTE, preços públicos apenas, comparação período-total vs. período-total, classificação de indisponibilidade em 6 categorias.

---

## Rodada 14A — Dias de semana, 19/04/2027 a 23/04/2027 (4 noites, inclui Tiradentes 21/04, quarta-feira)

### 1. Tabela aberta — Concorrentes

| Grupo | Concorrente | Acomodação âncora | Status | Classificação da indisponibilidade | Preço total Booking | Diária média Booking | Motor equivalente médio | Dif. R$ vs Villa motor* | Dif. % vs Villa motor* | Observação |
|---|---|---|---|---|---|---|---|---|---|---|
| NÚCLEO | Vila Boa Vida | Quarto Duplo Standard | Indisponível | `DATAS_PODEM_NAO_ESTAR_ABERTAS` | — | — | — | — | — | Sem datas alternativas nem aviso regional. |
| NÚCLEO | Vila Maciel | Apartamento Standard | Coletado | `COLETADO_COM_SUCESSO` | R$ 988,00 | R$ 247,00 | R$ 197,60 | −R$ 301,40 | −60,4% | "Temos só mais 2." |
| NÚCLEO | Pousada Kaloa Eco Village | Suíte Standard | Coletado | `COLETADO_COM_SUCESSO` | R$ 1.978,00 | R$ 494,50 | R$ 395,60 | −R$ 103,40 | −20,7% | Sem aviso de escassez. |
| NÚCLEO | Pousada Riviera Bombinhas | Suíte Loft Riviera | Coletado | `COLETADO_COM_SUCESSO` | R$ 1.697,00 | R$ 424,25 | R$ 339,40 | −R$ 159,60 | −32,0% | "Temos só mais 6." |
| NÚCLEO | Pousada dos Ingleses | Quarto Duplo Clássico | Coletado | `COLETADO_COM_SUCESSO` | R$ 1.515,00 (R$1.395+R$120 taxas) | R$ 378,75 | R$ 303,00 | −R$ 196,00 | −39,3% | "Temos só mais 1." |
| NÚCLEO | Pousada Dom Capudi | Quarto Duplo | Indisponível | `INDISPONIVEL_NAO_CONCLUSIVO` | — | — | — | — | — | Sem datas alternativas nem aviso regional. |
| NÚCLEO | Pousada Kia Ora Bombinhas | Quarto Duplo Deluxe c/ Vista Lateral do Mar | Coletado | `COLETADO_COM_SUCESSO` | R$ 2.151,00 | R$ 537,75 | R$ 430,20 | −R$ 68,80 | −13,8% | "Temos só mais 1." |
| AMPLIADA | Morada do Guaruça | Apartamento de 1 Quarto | Coletado | `COLETADO_COM_SUCESSO` | R$ 2.130,00 | R$ 532,50 | R$ 426,00 | −R$ 73,00 | −14,6% | "Temos só mais 6." |
| AMPLIADA | UP Hotel Boutique | Quarto Duplo Deluxe c/ Banheira | Indisponível (real) | `ESGOTADO_CONFIRMADO` | — | — | — | — | — | Aviso explícito: "6 cama e café já indisponíveis". |
| TETO_MERCADO | Atalaia do Mariscal | Suíte Superior | Indisponível | `INDISPONIVEL_NAO_CONCLUSIVO` | — | — | — | — | — | Referência apenas, não entra em média. |
| PENDENTE | Vila dos Açores | — | Não coletado | — | — | — | — | — | — | Mantido pendente. |

*Diferença calculada contra a régua motor da Villa (R$ 499,00/diária). Índice de disponibilidade núcleo: 5/7 = **71,4%**.

### 2. Tabela — Villa Arágua

| Acomodação | Total motor do período | Diária média motor | Total Booking estimado | Diária Booking estimada | Mínimo de noites aplicado |
|---|---|---|---|---|---|
| Organic/Fuego/Metallo | R$ 1.996,00 | R$ 499,00 | R$ 2.495,00 | R$ 623,75 | 2 (compatível — pacote de 4 noites) |

### 3. Resumo executivo — 14A

- Média núcleo Booking (5 coletados): R$ 1.665,80/pacote. Mediana: R$ 1.697,00 (Riviera).
- Média motor equivalente núcleo: R$ 333,16/diária.
- Média ampliada Booking: R$ 2.130,00/pacote (Morada, único preço coletado — UP esgotado).
- Referência de teto: não calculável (Atalaia indisponível).
- Índice de disponibilidade núcleo: 71,4% (5/7). Índice de disponibilidade total: 6/10 = 60,0%.
- **Sinal de demanda: MÉDIO.** Avisos de escassez pontuais ("só mais 1/2/6") em quase todos os coletados, mas 71,4% de disponibilidade núcleo ainda é folgado para uma leitura de demanda alta.
- **Grau de confiança: MÉDIO.** Boa amostra núcleo (5/7), mas é rodada única, sem histórico comparável de abril ainda.

### 4. Veredito de posicionamento — 14A

**`ACIMA_DO_NUCLEO_MAS_DEFENSAVEL`**. A Villa fica +49,8% acima da média motor núcleo, mas apenas +13,8% acima do concorrente mais caro coletado (Kia Ora) e ainda abaixo da referência ampliada (Morada do Guaruça, R$426,00/diária motor). Prêmio relevante, mas não descolado do topo do mercado coletado.

### 5. Diagnóstico preliminar — 14A

**`MANTER`**. Amostra boa (5/7 núcleo), sem erro de régua aparente, sem urgência de correção. Rodada diagnóstica, não corretiva.

---

## Rodada 14B — Final de semana, 23/04/2027 a 25/04/2027 (2 noites, sexta a domingo)

### 1. Tabela aberta — Concorrentes

| Grupo | Concorrente | Acomodação âncora | Status | Classificação da indisponibilidade | Preço total Booking | Diária média Booking | Motor equivalente médio | Dif. R$ vs Villa motor* | Dif. % vs Villa motor* | Observação |
|---|---|---|---|---|---|---|---|---|---|---|
| NÚCLEO | Vila Boa Vida | Quarto Duplo Standard | Indisponível | `DATAS_PODEM_NAO_ESTAR_ABERTAS` | — | — | — | — | — | Sem datas alternativas nem aviso regional. |
| NÚCLEO | Vila Maciel | Apartamento Standard | Coletado | `COLETADO_COM_SUCESSO` | R$ 551,00 | R$ 275,50 | R$ 220,40 | −R$ 278,60 | −55,8% | "Temos só mais 2." |
| NÚCLEO | Pousada Kaloa Eco Village | Suíte Standard | Coletado | `COLETADO_COM_SUCESSO` | R$ 989,00 | R$ 494,50 | R$ 395,60 | −R$ 103,40 | −20,7% | Sem aviso de escassez. |
| NÚCLEO | Pousada Riviera Bombinhas | Suíte Loft Riviera | Indisponível | `INDISPONIVEL_NAO_CONCLUSIVO` | — | — | — | — | — | Disponível em 14A; indisponível aqui, sem aviso regional. |
| NÚCLEO | Pousada dos Ingleses | Quarto Duplo Clássico | Coletado | `COLETADO_COM_SUCESSO` | R$ 818,00 (R$698+R$120 taxas) | R$ 409,00 | R$ 327,20 | −R$ 171,80 | −34,4% | "Temos só mais 1." |
| NÚCLEO | Pousada Dom Capudi | Quarto Duplo | Indisponível | `INDISPONIVEL_NAO_CONCLUSIVO` | — | — | — | — | — | Mesmo padrão de 14A. |
| NÚCLEO | Pousada Kia Ora Bombinhas | Quarto Duplo Deluxe c/ Vista Lateral do Mar | Indisponível | `INDISPONIVEL_NAO_CONCLUSIVO` | — | — | — | — | — | Disponível em 14A; indisponível aqui, sem aviso regional. |
| AMPLIADA | Morada do Guaruça | Apartamento de 1 Quarto | Coletado | `COLETADO_COM_SUCESSO` | R$ 1.118,00 | R$ 559,00 | R$ 447,20 | +R$ 51,80 (Villa abaixo) | — | "Temos só mais 6." |
| AMPLIADA | UP Hotel Boutique | Quarto Duplo Deluxe c/ Banheira | Indisponível (real) | `ESGOTADO_CONFIRMADO` | — | — | — | — | — | Mesmo aviso explícito de esgotamento regional. |
| TETO_MERCADO | Atalaia do Mariscal | Suíte Superior | Indisponível | `INDISPONIVEL_NAO_CONCLUSIVO` | — | — | — | — | — | Referência apenas. |
| PENDENTE | Vila dos Açores | — | Não coletado | — | — | — | — | — | — | Mantido pendente. |

*Diferença calculada contra a régua motor da Villa (R$ 499,00/diária). Índice de disponibilidade núcleo: 3/7 = **42,9%**.

### 2. Tabela — Villa Arágua

| Acomodação | Total motor do período | Diária média motor | Total Booking estimado | Diária Booking estimada | Mínimo de noites aplicado |
|---|---|---|---|---|---|
| Organic/Fuego/Metallo | R$ 998,00 | R$ 499,00 | R$ 1.247,50 | R$ 623,75 | 2 (compatível — pacote de 2 noites) |

### 3. Resumo executivo — 14B

- Média núcleo Booking (3 coletados): R$ 786,00/pacote. Mediana: R$ 818,00 (Ingleses).
- Média motor equivalente núcleo: R$ 314,40/diária.
- Média ampliada Booking: R$ 1.118,00/pacote (Morada, único coletado — UP esgotado).
- Referência de teto: não calculável (Atalaia indisponível).
- Índice de disponibilidade núcleo: 42,9% (3/7) — bem mais baixo que 14A. Índice de disponibilidade total: 4/10 = 40,0%.
- **Sinal de demanda: MÉDIO.** A queda de disponibilidade é real, mas a maioria das indisponibilidades desta rodada é `INDISPONIVEL_NAO_CONCLUSIVO` — que por regra não conta como sinal forte.
- **Grau de confiança: BAIXO.** Amostra núcleo de apenas 3 concorrentes é pequena demais para uma leitura firme.

**⚠️ Nota metodológica importante (identificada pelo agente):** a queda da diária motor núcleo de R$333,16 (14A) para R$314,40 (14B) é um **artefato de composição amostral**, não um sinal de preço mais baixo no fim de semana. Kia Ora (o mais caro do núcleo, R$430,20/diária) e Riviera (R$339,40/diária) desaparecem da amostra 14B por indisponibilidade — sobra só o trio mais barato (Vila Maciel, Kaloa, Ingleses). Os valores de R$/diária de 14A e 14B **não são diretamente comparáveis** como "preço de semana vs. preço de fim de semana". O dado confiável desta comparação é o **índice de disponibilidade** (71,4% → 42,9%), não a média de preço.

### 4. Veredito de posicionamento — 14B

**`POSICIONAMENTO_INDEFINIDO_AGUARDAR_DADOS`**. A Villa aparece +58,7% acima da média núcleo, mas essa média vem de apenas 3/7 concorrentes — amostra pequena e enviesada para baixo pela ausência dos dois competidores mais caros (Kia Ora, Riviera). Isso compromete qualquer leitura fina de posicionamento para este bloco específico.

### 5. Diagnóstico preliminar — 14B

**`COMPARAR_MELHOR`**. Amostra núcleo insuficiente (42,9%) para recomendar qualquer ajuste com confiança. Recomenda-se nova coleta de fim de semana em abril, capturando especificamente Kia Ora e Riviera, antes de qualquer leitura mais firme sobre este bucket.

---

## 6. Leitura específica de abril

1. **Os dias de semana devem ter tarifa mais competitiva?** A régua atual (R$499) já não está descolada do núcleo em 14A (+13,8% sobre o mais caro coletado) — não há evidência de necessidade urgente de reduzir.
2. **O final de semana suporta tarifa mais alta?** O índice de disponibilidade caiu de 71,4% para 42,9%, o que é consistente com a hipótese de Renildo de mais demanda no fim de semana — mas a comparação de preço em si (14A vs. 14B) está distorcida pela composição amostral (ver nota acima), então não dá para quantificar "quanto mais" com este dado.
3. **Tiradentes mostrou algum sinal real de força ou pode ser tratado como dia comum?** Os dados coletados **não contradizem** a posição de Renildo de tratar Tiradentes como dia comum — não houve aviso de esgotamento amplo nem tarifa isolada de feriado visível. Mas a coleta foi feita para o bloco inteiro de 4 noites (19–23/04), sem isolar a diária de 21/04 — o desenho da coleta não tem poder de detectar um pico isolado de meio de semana, mesmo que exista. Ausência de evidência aqui não é prova de ausência; confiança sobre esta pergunta específica: **BAIXA**.
4. **Faz sentido criar dois buckets em abril: semana e final de semana?** A hipótese está **parcialmente sustentada, não confirmada**. O índice de disponibilidade aponta na direção certa (fim de semana mais apertado), mas a diferença de preço observada está confundida pela amostra. Recomenda-se tratar como hipótese em teste — não criar os dois buckets ainda com este único dado.
5. **Qual preço-base sugerido para dias de semana, se houver ajuste?** Nenhum ajuste sugerido — a base atual (R$499) já está `MANTER` em 14A.
6. **Qual preço-base sugerido para final de semana, se houver ajuste?** Nenhum ajuste sugerido nesta rodada — a amostra de 14B é insuficiente (`COMPARAR_MELHOR`) para qualquer sugestão numérica responsável.
7. **O que pode ser replicado para o restante de abril?** A metodologia de duas amostras (semana + fim de semana) é replicável, mas a rodada de fim de semana precisa de amostra maior — sugere-se repetir 14B em uma data futura, priorizando recoletar especificamente Kia Ora e Riviera (que sumiram desta amostra) antes de generalizar para o resto do mês.

Nenhum risco claro foi identificado nos dias de semana (14A = `MANTER`), portanto **nenhuma simulação de redução foi executada**. Nenhum sinal forte foi confirmado nos finais de semana (14B = `COMPARAR_MELHOR`, não `SUBIR_COM_PRIORIDADE` nem `POSICIONAMENTO_FORTE_PROTEGER`), portanto **nenhuma simulação de aumento foi executada** — simular um aumento sobre uma leitura classificada como "aguardar dados" criaria uma falsa aparência de precisão que os dados não sustentam.

---

## Comparativo com rodadas anteriores

| Rodada | Período | Veredito | Diagnóstico | Sinal de demanda |
|---|---|---|---|---|
| 12 (Março) | 12A-12C | — | MANTER (12A/B), PROTEGER (12C) | MÉDIO aquecendo (12C) |
| 13 (Páscoa) | 26-29/03 | ACIMA_DO_MERCADO_COM_RISCO | ESPERAR | MÉDIO (confiança BAIXA) |
| **14A (Abril, semana)** | **19-23/04** | **ACIMA_DO_NUCLEO_MAS_DEFENSAVEL** | **MANTER** | **MÉDIO (confiança MÉDIA)** |
| **14B (Abril, fim de semana)** | **23-25/04** | **POSICIONAMENTO_INDEFINIDO_AGUARDAR_DADOS** | **COMPARAR_MELHOR** | **MÉDIO (confiança BAIXA)** |

Abril retoma um padrão mais próximo do núcleo do que a Páscoa (que mostrou gap de quase 2×) — reforçando que o gap da Páscoa era específico daquele feriado, não uma mudança estrutural na régua da Villa.

---

**Importante:** nenhuma tarifa foi alterada nesta rodada. Nenhuma decisão foi criada automaticamente. Nada foi movido para `DECISOES_REVENUE_PENDENTES_VILLA_ARAGUA.md`. Este diagnóstico é preliminar — a decisão final é de Renildo.
