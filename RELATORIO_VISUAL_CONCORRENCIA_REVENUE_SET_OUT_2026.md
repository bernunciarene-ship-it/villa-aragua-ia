# RELATÓRIO VISUAL — RADAR DE CONCORRÊNCIA REVENUE — POUSADA ARÁGUA (SET/OUT 2026)

**Rodadas cobertas:** Rodada 1 (7 de Setembro) e Rodada 2 (12 de Outubro)
**Fontes:** `COLETAS_CONCORRENCIA_REVENUE.csv`, `CESTA_COMPETITIVA_REVENUE_VILLA_ARAGUA.md`, `ALERTAS_CONCORRENCIA_REVENUE.md`, `REGRAS_CONVERSAO_OTA_MOTOR_REVENUE.md`
**Regra de integridade:** todo valor abaixo veio de um destes arquivos. Nenhum valor foi recalculado a partir de suposição — onde não havia dado registrado, o campo aparece como `DADO_NAO_ENCONTRADO`, não como estimativa.
**Status deste relatório:** `RELATORIO_ANALITICO_SEM_ALTERACAO_TARIFARIA`

---

## 1. Como ler este relatório

- **Preço Booking** é o preço público que o hóspede vê na OTA — já inclui o acréscimo de +25% que a Villa Arágua aplica sobre o motor (`REGRAS_CONVERSAO_OTA_MOTOR_REVENUE.md`). O mesmo raciocínio vale para os concorrentes: o preço deles no Booking também é preço de vitrine, não necessariamente igual ao que eles cobram por fora.
- **Motor equivalente** = diária Booking ÷ 1,25. É a conversão obrigatória para colocar qualquer concorrente na mesma base do motor da Villa Arágua (Stays).
- **A Villa Arágua deve ser comparada de duas formas, sempre lado a lado:** pelo **motor** (o valor que Renildo realmente define) e pelo **Booking estimado** (motor × 1,25, para comparar "vitrine com vitrine" contra os concorrentes).
- **Núcleo, Ampliada e Teto de Mercado nunca são misturados numa única média.** Núcleo = peso alto, é a comparação principal. Ampliada = peso baixo, leitura de mercado secundária. Teto de mercado = só referência de topo, nunca entra em média nenhuma.
- **Diferença R$ e Diferença %** nas tabelas abaixo são sempre "concorrente − Villa motor equivalente". Valor **negativo** = concorrente mais barato que a Villa. Valor **positivo** = concorrente mais caro que a Villa.

---

## 2. Rodada 1 — 7 de Setembro

**Período:** 04/09/2026 a 08/09/2026 · 4 noites · perfil casal (2 adultos, 0 crianças, 1 acomodação)
**Villa Arágua motor base:** R$ 499,00
**Villa Arágua Booking estimado:** R$ 623,75

### A. Núcleo

| Concorrente | Acomodação âncora | Status | Preço total Booking | Diária Booking | Motor equivalente | Dif. R$ vs Villa motor | Dif. % vs Villa motor | Observação |
|---|---|---|---|---|---|---|---|---|
| Vila Boa Vida | Quarto Duplo Standard | COLETADO_COM_SUCESSO | R$ 1.695,00 | R$ 423,75 | R$ 339,00 | −R$ 160,00 | −32,1% | — |
| Vila Maciel | Apartamento Standard | COLETADO_COM_SUCESSO | R$ 938,00 (30% off; original R$ 1.340,00) | R$ 234,50 | R$ 187,60 | −R$ 311,40 | −62,4% | Preço com desconto promocional ativo no momento da coleta |
| Pousada Kaloa Eco Village | Suíte Standard | COLETADO_COM_SUCESSO | R$ 1.949,00 | R$ 487,25 | R$ 389,80 | −R$ 109,20 | −21,9% | — |
| Pousada Riviera Bombinhas | Suíte Loft Riviera | COLETADO_COM_SUCESSO | R$ 1.894,00 | R$ 473,50 | R$ 378,80 | −R$ 120,20 | −24,1% | — |
| Pousada dos Ingleses | Quarto Duplo Clássico | COLETADO_COM_SUCESSO | R$ 1.254,00 (R$ 1.134 + R$ 120 taxas à parte) | R$ 313,50 | R$ 250,80 | −R$ 248,20 | −49,7% | Site exibe taxa separada do preço-base |
| Pousada Kia Ora Bombinhas | Quarto Duplo Deluxe c/ Vista Lateral do Mar | COLETADO_COM_SUCESSO | R$ 2.341,00 | R$ 585,25 | R$ 468,20 | −R$ 30,80 | −6,2% | Concorrente núcleo mais próximo da Villa nesta rodada |

### B. Ampliada

| Concorrente | Acomodação âncora | Status | Preço total Booking | Diária Booking | Motor equivalente | Dif. R$ vs Villa motor | Dif. % vs Villa motor | Observação |
|---|---|---|---|---|---|---|---|---|
| UP Hotel Boutique | Quarto Duplo Deluxe com Banheira | COLETADO_COM_SUCESSO | R$ 2.412,00 | R$ 603,00 | R$ 482,40 | −R$ 16,60 | −3,3% | Único dado da ampliada nesta rodada — Morada do Guaruça indisponível |

### C. Teto de mercado

| Concorrente | Acomodação âncora | Status | Preço total Booking | Diária Booking | Motor equivalente | Dif. R$ vs Villa motor | Dif. % vs Villa motor | Observação |
|---|---|---|---|---|---|---|---|---|
| Hotel/Pousada Atalaia do Mariscal | Suíte Superior | PRECISA_VALIDACAO_MANUAL | DADO_NAO_ENCONTRADO | DADO_NAO_ENCONTRADO | DADO_NAO_ENCONTRADO | DADO_NAO_ENCONTRADO | DADO_NAO_ENCONTRADO | Sem disponibilidade no Booking para o período — esgotado. Site ofereceu datas alternativas (11–13/09 e 4–7/09), não usadas por não coincidirem com o período pedido |

### D. Indisponíveis / não usados na média

| Concorrente | Grupo | Status | Motivo |
|---|---|---|---|
| Pousada Dom Capudi | NUCLEO | PRECISA_VALIDACAO_MANUAL | Booking: "Não temos disponibilidade aqui de sex., 4 de set. de 2026 a ter., 8 de set. de 2026." Todas as categorias indisponíveis |
| Morada do Guaruça | AMPLIADA | PRECISA_VALIDACAO_MANUAL | Âncora aprovada (Apartamento de 1 Quarto) não aparecia entre as categorias disponíveis — provável esgotamento. Outras categorias mais caras seguiam à venda, mas não foram usadas por não serem a âncora aprovada |
| Hotel/Pousada Atalaia do Mariscal | TETO_MERCADO | PRECISA_VALIDACAO_MANUAL | Sem disponibilidade no Booking para o período |

---

## 3. Rodada 2 — 12 de Outubro

**Período:** 09/10/2026 a 12/10/2026 · 3 noites · perfil casal (2 adultos, 0 crianças, 1 acomodação)
**Villa Arágua motor base:** R$ 529,00
**Villa Arágua Booking estimado:** R$ 661,25

### A. Núcleo

| Concorrente | Acomodação âncora | Status | Preço total Booking | Diária Booking | Motor equivalente | Dif. R$ vs Villa motor | Dif. % vs Villa motor | Observação |
|---|---|---|---|---|---|---|---|---|
| Vila Boa Vida | Quarto Duplo Standard | COLETADO_COM_SUCESSO | R$ 1.271,00 | R$ 423,67 | R$ 338,93 | −R$ 190,07 | −35,9% | — |
| Vila Maciel | Apartamento Standard | COLETADO_COM_SUCESSO | R$ 840,00 (20% off; original R$ 1.050,00) | R$ 280,00 | R$ 224,00 | −R$ 305,00 | −57,7% | Preço com desconto promocional ativo no momento da coleta |
| Pousada Kaloa Eco Village | Suíte Standard | COLETADO_COM_SUCESSO | R$ 1.462,00 | R$ 487,33 | R$ 389,87 | −R$ 139,13 | −26,3% | — |
| Pousada Riviera Bombinhas | Suíte Loft Riviera | COLETADO_COM_SUCESSO | R$ 1.458,00 | R$ 486,00 | R$ 388,80 | −R$ 140,20 | −26,5% | — |
| Pousada dos Ingleses | Quarto Duplo Clássico | COLETADO_COM_SUCESSO | R$ 970,00 (R$ 850 + R$ 120 taxas à parte) | R$ 323,33 | R$ 258,67 | −R$ 270,33 | −51,1% | Site exibe taxa separada do preço-base |
| Pousada Dom Capudi | Quarto Duplo | COLETADO_COM_SUCESSO | R$ 1.354,00 | R$ 451,33 | R$ 361,07 | −R$ 167,93 | −31,7% | Estava esgotado na Rodada 1; disponível nesta rodada |
| Pousada Kia Ora Bombinhas | Quarto Duplo Deluxe c/ Vista Lateral do Mar | COLETADO_COM_SUCESSO | R$ 2.006,00 | R$ 668,67 | R$ 534,93 | +R$ 5,93 | +1,1% | Único concorrente núcleo **acima** da Villa nesta rodada |

### B. Ampliada

| Concorrente | Acomodação âncora | Status | Preço total Booking | Diária Booking | Motor equivalente | Dif. R$ vs Villa motor | Dif. % vs Villa motor | Observação |
|---|---|---|---|---|---|---|---|---|
| Morada do Guaruça | Apartamento de 1 Quarto | COLETADO_COM_SUCESSO | R$ 1.835,00 | R$ 611,67 | R$ 489,33 | −R$ 39,67 | −7,5% | Estava esgotada na Rodada 1; disponível nesta rodada |
| UP Hotel Boutique | Quarto Duplo Deluxe com Banheira | COLETADO_COM_SUCESSO | R$ 1.744,00 | R$ 581,33 | R$ 465,07 | −R$ 63,93 | −12,1% | — |

### C. Teto de mercado

| Concorrente | Acomodação âncora | Status | Preço total Booking | Diária Booking | Motor equivalente | Dif. R$ vs Villa motor | Dif. % vs Villa motor | Observação |
|---|---|---|---|---|---|---|---|---|
| Hotel/Pousada Atalaia do Mariscal | Suíte Superior | COLETADO_COM_SUCESSO | R$ 4.800,00 | R$ 1.600,00 | R$ 1.280,00 | +R$ 751,00 | +142,0% | Referência de teto — não entra em nenhuma média. Estava esgotado na Rodada 1 |

### D. Indisponíveis / não usados na média

Nenhum. Todos os 10 concorrentes tentados (Vila dos Açores segue fora, por estar `PENDENTE`) foram coletados com sucesso nesta rodada.

---

## 4. Ranking visual por rodada

### Rodada 1 — do menor para o maior (diária Booking)

**Núcleo:**
1. Vila Maciel — R$ 234,50
2. Pousada dos Ingleses — R$ 313,50
3. Vila Boa Vida — R$ 423,75
4. Pousada Riviera Bombinhas — R$ 473,50
5. Pousada Kaloa Eco Village — R$ 487,25
6. Pousada Kia Ora Bombinhas — R$ 585,25
— Pousada Dom Capudi: indisponível, fora do ranking

**Ampliada:**
1. UP Hotel Boutique — R$ 603,00
— Morada do Guaruça: indisponível, fora do ranking

**Teto de mercado:**
— Hotel/Pousada Atalaia do Mariscal: indisponível, fora do ranking

### Rodada 2 — do menor para o maior (diária Booking)

**Núcleo:**
1. Vila Maciel — R$ 280,00
2. Pousada dos Ingleses — R$ 323,33
3. Vila Boa Vida — R$ 423,67
4. Pousada Dom Capudi — R$ 451,33
5. Pousada Riviera Bombinhas — R$ 486,00
6. Pousada Kaloa Eco Village — R$ 487,33
7. Pousada Kia Ora Bombinhas — R$ 668,67

**Ampliada:**
1. UP Hotel Boutique — R$ 581,33
2. Morada do Guaruça — R$ 611,67

**Teto de mercado:**
1. Hotel/Pousada Atalaia do Mariscal — R$ 1.600,00

---

## 5. Resumo comparativo

| Métrica | Rodada 1 (7 de Setembro) | Rodada 2 (12 de Outubro) |
|---|---|---|
| Período | 04–08/09/2026 (4 noites) | 09–12/10/2026 (3 noites) |
| Média núcleo Booking | R$ 419,63 | R$ 445,76 |
| Mediana núcleo Booking | R$ 448,63 | R$ 451,33 |
| Média motor equivalente núcleo | R$ 335,70 | R$ 356,61 |
| Média ampliada Booking | R$ 603,00 (n=1 de 2) | R$ 596,50 (n=2 de 2) |
| Villa motor base | R$ 499,00 | R$ 529,00 |
| Villa Booking estimado | R$ 623,75 | R$ 661,25 |
| Villa vs. núcleo | +48,7% | +48,3% |
| Villa vs. ampliada | +3,4% | +10,9% |
| indice_disponibilidade_nucleo | 85,7% (6 de 7) | 100% (7 de 7) |
| indice_disponibilidade_total_tentado | 70% (7 de 10) | 100% (10 de 10) |
| sinal_demanda | MÉDIO/ALTO | BAIXO |
| Diagnóstico registrado | `MANTER` / `ESPERAR` (+ adendo `PROTEGER` / `ESPERAR` na Rodada 1R) | `MANTER` |

---

## 6. O que Renildo deve observar olhando os preços

**Quem realmente pressiona o preço da Villa (núcleo, mais próximos):** Pousada Kia Ora Bombinhas é o concorrente núcleo mais caro nas duas rodadas — na Rodada 2 já ultrapassou a Villa (+1,1%). É o concorrente que mais vale acompanhar de perto, porque está na mesma faixa de preço da Villa, não muito abaixo.

**Quem é barato demais para comparar diretamente:** Vila Maciel (R$ 234,50 a R$ 280,00/diária) está muito abaixo em ambas as rodadas — mais de 55% a 62% abaixo da Villa. É um apartamento simples de 22 m², nota de qualidade 3/5 no Booking; entra no núcleo por cumprir os critérios mínimos de equivalência, mas não é o mesmo padrão de produto. Pousada dos Ingleses também fica bem abaixo (−49,7% e −51,1%).

**Quem parece premium (teto de mercado):** Hotel/Pousada Atalaia do Mariscal, com diária de R$ 1.600,00 na Rodada 2 — mais que o triplo da Villa. Não é referência de preço para o dia a dia, é referência de "quanto o mercado aceita pagar no topo" em Mariscal.

**Quem estava indisponível:** na Rodada 1, três concorrentes (Dom Capudi, Morada do Guaruça, Atalaia do Mariscal) estavam esgotados para o feriado de 7 de Setembro — inclusive o próprio teto de mercado. Na Rodada 2 (12 de Outubro), todos os dez tentados tinham disponibilidade.

**Onde a Villa está posicionada:** a Villa fica consistentemente ~48% acima da média núcleo nas duas rodadas — não é um efeito pontual de uma data, parece um padrão estável. Já contra a média ampliada (concorrentes de padrão mais próximo ao da Villa), a diferença é bem menor: +3,4% na Rodada 1 e +10,9% na Rodada 2. Ou seja, a Villa está longe da faixa "barata" do núcleo, mas perto da faixa "ampliada" — o grupo mais parecido com o posicionamento da Villa.

**Por que não baixar automaticamente só por estar acima da média núcleo:** a média núcleo inclui produtos de padrão bem diferente (de apartamento simples de 22 m² a suíte com vista de mar) — baixar para se igualar a essa média poderia significar competir com um produto que não é comparável. Além disso, na Rodada 1, o esgotamento de 3 concorrentes é sinal de demanda real, não motivo para vender mais barato: quando concorrente esgota, isso normalmente indica que o mercado está pagando, não que está sobrando vaga.

**Como Meta Ads e reserva direta mudam a leitura:** a campanha de reabertura (lançamento previsto 01/08) e a prioridade de venda direta via WhatsApp mudam o cálculo — a Villa não depende só de aparecer competitiva no Booking, porque parte da demanda deve vir de fora da OTA. Isso é exatamente o argumento já registrado na Rodada 1R: "a Villa Arágua não compete por ser mais barata que a OTA — compete por valor agregado." O gap de 48% vs. núcleo pesa menos quando uma fatia relevante da ocupação vem de reserva direta, não de quem está comparando preços de pousada no Booking.

---

## 7. Conclusão

Nenhuma decisão nova foi gerada por este relatório — ele apenas organiza visualmente o que já estava registrado.

**Rodada 1 (7 de Setembro):** `PROTEGER` + `ESPERAR`

**Rodada 2 (12 de Outubro):** `MANTER`, com ponto de atenção — o gap de ~48% vs. núcleo se repetiu sem o sinal de demanda (esgotamento) que sustentou a leitura da Rodada 1; registrado como algo a observar em rodadas futuras, não como motivo para agir agora.

**Status deste relatório:** `RELATORIO_ANALITICO_SEM_ALTERACAO_TARIFARIA`
