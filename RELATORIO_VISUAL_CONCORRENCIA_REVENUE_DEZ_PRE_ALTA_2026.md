# RELATÓRIO VISUAL — RADAR DE CONCORRÊNCIA REVENUE — POUSADA ARÁGUA (DEZEMBRO PRÉ-ALTA 2026)

**Formato enxuto** — amostra representativa (não coleta semana a semana), conforme orientação de Renildo: pelo histórico da região, os preços não costumam variar muito dentro do bloco 01–17/12/2026.
**Rodadas cobertas:** Rodada 6A (dias de semana, 07–11/12/2026) e Rodada 6B (fim de semana, 11–13/12/2026)
**Produto Villa de referência:** Pousada Arágua — unidade base (Organic/Fuego/Metallo) · perfil casal (2 adultos, 0 crianças, 1 acomodação)
**Fontes:** `COLETAS_CONCORRENCIA_REVENUE.csv`, `CESTA_COMPETITIVA_REVENUE_VILLA_ARAGUA.md`, `ALERTAS_CONCORRENCIA_REVENUE.md`, `REGRAS_CONVERSAO_OTA_MOTOR_REVENUE.md`, `INVENTARIO_TARIFAS_PUBLICADAS_AGO2026_ABR2027.csv`
**Coleta:** 2026-07-28, via Booking (Claude in Chrome), preços públicos visíveis, sem login, sem clicar em reservar.
**Diagnóstico:** gerado via agente `villa-precificacao-calendario`, com consulta às skills `villa-aragua-pricing-revenue` e `villa-aragua-growth-marketer` — agente acionado de fato.
**Status deste relatório:** `RELATORIO_ANALITICO_SEM_ALTERACAO_TARIFARIA`

**Villa Arágua no bloco:** motor **R$ 629,00** (bucket único "Dezembro/2026 1-18" do inventário, sem distinção dia de semana/fim de semana dentro do bloco) · Booking estimado **R$ 786,25**

---

## 1. Tabela aberta — Rodada 6A (dias de semana, 07–11/12/2026, 4 noites)

| Grupo | Concorrente | Acomodação âncora | Status | Preço total Booking | Diária Booking | Motor equivalente | Dif. R$ vs Villa motor | Dif. % vs Villa motor | Observação |
|---|---|---|---|---|---|---|---|---|---|
| NUCLEO | Vila Maciel | Apartamento Standard | COLETADO_COM_SUCESSO | R$ 924,00 (30% off; original R$ 1.320,00) | R$ 231,00 | R$ 184,80 | −R$ 444,20 | −70,6% | Nota Booking 3/5 |
| NUCLEO | Pousada dos Ingleses | Quarto Duplo Clássico | COLETADO_COM_SUCESSO | R$ 1.559,00 (R$1.439+R$120 taxas) | R$ 389,75 | R$ 311,80 | −R$ 317,20 | −50,4% | Taxa separada, já somada |
| NUCLEO | Pousada Dom Capudi | Quarto Duplo | COLETADO_COM_SUCESSO | R$ 1.805,00 | R$ 451,25 | R$ 361,00 | −R$ 268,00 | −42,6% | — |
| NUCLEO | Pousada Kaloa Eco Village | Suíte Standard | COLETADO_COM_SUCESSO | R$ 2.227,00 | R$ 556,75 | R$ 445,40 | −R$ 183,60 | −29,2% | — |
| NUCLEO | Pousada Riviera Bombinhas | Suíte Loft Riviera | COLETADO_COM_SUCESSO | R$ 2.300,00 | R$ 575,00 | R$ 460,00 | −R$ 169,00 | −26,9% | — |
| NUCLEO | Vila Boa Vida | Quarto Duplo Standard | COLETADO_COM_SUCESSO | R$ 2.640,00 | R$ 660,00 | R$ 528,00 | −R$ 101,00 | −16,1% | — |
| NUCLEO | Pousada Kia Ora Bombinhas | Quarto Duplo Deluxe c/ Vista Lateral do Mar | COLETADO_COM_SUCESSO | R$ 3.317,00 | R$ 829,25 | R$ 663,40 | +R$ 34,40 | +5,5% | Único núcleo acima da Villa nesta rodada |
| AMPLIADA | UP Hotel Boutique | Quarto Duplo Deluxe com Banheira | COLETADO_COM_SUCESSO | R$ 2.762,00 (7% off; original R$ 2.970,00) | R$ 690,50 | R$ 552,40 | −R$ 76,60 | −12,2% | Amostra fraca (n=1 de 2) |
| AMPLIADA | Morada do Guaruça | Apartamento de 1 Quarto | PRECISA_VALIDACAO_MANUAL | INDISPONIVEL | — | — | — | — | Esgotada, todas as categorias |
| TETO_MERCADO | Hotel/Pousada Atalaia do Mariscal | Suíte Superior | COLETADO_COM_SUCESSO | R$ 6.800,00 | R$ 1.700,00 | R$ 1.360,00 | +R$ 731,00 | +116,2% | Booking alertava "6 hotéis 4 estrelas já indisponíveis" na região |

### Resumo executivo — Rodada 6A

| Indicador | Valor |
|---|---|
| Média núcleo Booking (n=7/7) | R$ 527,57 |
| Mediana núcleo Booking | R$ 556,75 |
| Média motor equivalente núcleo | R$ 422,06 |
| Média ampliada Booking (n=1/2, amostra fraca) | R$ 690,50 |
| Referência de teto | R$ 1.700,00 |
| Índice de disponibilidade núcleo | 100% (7/7) |
| Índice de disponibilidade total tentado | 90% (9/10) |
| **Sinal de demanda** | **MÉDIO** — núcleo 100% disponível, mas Booking emitiu alerta de escassez regional no teto mesmo assim |

### Veredito de posicionamento — Rodada 6A

**`ACIMA_DO_NUCLEO_MAS_DEFENSAVEL`** — Villa +49,0% vs. núcleo (padrão estrutural já visto em todas as rodadas), +13,9% vs. ampliada (amostra fraca).

### Diagnóstico preliminar — Rodada 6A

**`MANTER`** — gap vs. núcleo é estrutural, não específico da data; núcleo 100% disponível não sustenta alta; leitura comercial (growth-marketer) afasta baixa automática motivada só pelo gap de OTA.

---

## 2. Tabela aberta — Rodada 6B (fim de semana, 11–13/12/2026, 2 noites)

| Grupo | Concorrente | Acomodação âncora | Status | Preço total Booking | Diária Booking | Motor equivalente | Dif. R$ vs Villa motor | Dif. % vs Villa motor | Observação |
|---|---|---|---|---|---|---|---|---|---|
| NUCLEO | Vila Maciel | Apartamento Standard | COLETADO_COM_SUCESSO | R$ 704,00 (20% off; original R$ 880,00) | R$ 352,00 | R$ 281,60 | −R$ 347,40 | −55,2% | — |
| NUCLEO | Pousada Dom Capudi | Quarto Duplo | COLETADO_COM_SUCESSO | R$ 903,00 | R$ 451,50 | R$ 361,20 | −R$ 267,80 | −42,6% | — |
| NUCLEO | Pousada dos Ingleses | Quarto Duplo Clássico | COLETADO_COM_SUCESSO | R$ 927,00 (R$807+R$120 taxas) | R$ 463,50 | R$ 370,80 | −R$ 258,20 | −41,1% | Taxa separada, já somada |
| NUCLEO | Pousada Kaloa Eco Village | Suíte Standard | COLETADO_COM_SUCESSO | R$ 1.114,00 | R$ 557,00 | R$ 445,60 | −R$ 183,40 | −29,2% | — |
| NUCLEO | Vila Boa Vida | Quarto Duplo Standard | COLETADO_COM_SUCESSO | R$ 1.320,00 | R$ 660,00 | R$ 528,00 | −R$ 101,00 | −16,1% | — |
| NUCLEO | Pousada Riviera Bombinhas | Suíte Loft Riviera | PRECISA_VALIDACAO_MANUAL | INDISPONIVEL | — | — | — | — | Esgotada, todas as categorias |
| NUCLEO | Pousada Kia Ora Bombinhas | Quarto Duplo Deluxe c/ Vista Lateral do Mar | PRECISA_VALIDACAO_MANUAL | INDISPONIVEL | — | — | — | — | Esgotada, todas as categorias |
| AMPLIADA | Morada do Guaruça | Apartamento de 1 Quarto | PRECISA_VALIDACAO_MANUAL | INDISPONIVEL | — | — | — | — | Esgotada, todas as categorias |
| AMPLIADA | UP Hotel Boutique | Quarto Duplo Deluxe com Banheira | PRECISA_VALIDACAO_MANUAL | DADO_NAO_ENCONTRADO | — | — | — | — | Restrição de estadia mínima de 3 diárias — não é esgotamento, é regra de mínimo de noites, incompatível com a busca de 2 noites |
| TETO_MERCADO | Hotel/Pousada Atalaia do Mariscal | Suíte Superior | PRECISA_VALIDACAO_MANUAL | INDISPONIVEL | — | — | — | — | Esgotada. Booking alertava "7 hotéis 4 estrelas já indisponíveis" — subiu de 6 (Rodada 6A) para 7 em poucos dias |

### Resumo executivo — Rodada 6B

| Indicador | Valor |
|---|---|
| Média núcleo Booking (n=5/7) | R$ 496,80 |
| Mediana núcleo Booking | R$ 463,50 |
| Média motor equivalente núcleo | R$ 397,44 |
| Média ampliada Booking | DADO_NAO_ENCONTRADO (0 de 2 utilizáveis) |
| Referência de teto | DADO_NAO_ENCONTRADO (esgotado) |
| Índice de disponibilidade núcleo | 71,4% (5/7) |
| Índice de disponibilidade total tentado | 50% (5/10) |
| **Sinal de demanda** | **ALTO** — maior sinal de esgotamento já registrado em todo o Radar: núcleo reduzido, ampliada zerada, teto esgotado, alerta do Booking escalando de 6 para 7 hotéis indisponíveis em poucos dias |

### Veredito de posicionamento — Rodada 6B

**`POSICIONAMENTO_FORTE_PROTEGER`** — o gap de +58,3% vs. núcleo não reflete "Villa cara demais": a amostra núcleo está reduzida e enviesada para os concorrentes mais baratos (os equivalentes já venderam). Sem dado de ampliada/teto para comparar, e com o sinal de demanda mais forte do Radar.

### Diagnóstico preliminar — Rodada 6B

**`PROTEGER`** — mesmo raciocínio da Rodada 4 (Consciência Negra), aqui reforçado por um sinal ainda mais forte. Não é hora de descontar; não há base confiável para calibrar alta agora.

---

## 3. Leitura específica

**Os dias de semana de dezembro pré-alta estão competitivos?**
Sim, dentro do padrão já validado. O gap de +49,0% vs. núcleo é o mesmo comportamento estrutural visto em todas as rodadas anteriores (feriado ou não). Núcleo 100% disponível, mas o próprio Booking sinaliza aquecimento regional mesmo assim.

**O final de semana está defensável?**
Sim, fortemente — é o maior sinal de esgotamento já visto no Radar.

**Existe risco de diária zero nos dias de semana?**
Nenhuma evidência disso nos dados coletados. Diferente da tarifa tática de novembro/2026 (aplicada com sinal_demanda BAIXO e 100% de disponibilidade **sem alerta de escassez**), aqui o núcleo também está 100% disponível, mas **com** alerta explícito de escassez regional do Booking — sinal oposto ao de novembro. Não há visibilidade do ritmo real de reservas da Villa (dado que falta).

**A Villa está acima do núcleo, próxima da ampliada ou acima do mercado com risco?**
6A: acima do núcleo (+49,0%), relativamente próxima da ampliada (+13,9%, amostra fraca) — sem indício de risco. 6B: acima do núcleo em base enfraquecida (+58,3%), sem comparação válida de ampliada — leitura de posicionamento protegido pela demanda, não de risco.

**Faz sentido simular redução tática para dias de semana?**
**Não.** Não foi identificado risco real na Rodada 6A (núcleo com disponibilidade plena, sinal de demanda MÉDIO — não BAIXO —, e alerta de escassez regional do próprio Booking). Por isso nenhum cenário de redução foi simulado — simular aqui repetiria, sem justificativa nos dados, a lógica aplicada em novembro/2026, onde o sinal era genuinamente BAIXO e sem nenhum alerta de escassez.

**Os finais de semana devem ser preservados?**
Sim, sem ambiguidade — `PROTEGER` é o diagnóstico mais defensável dado o maior sinal de esgotamento já registrado no Radar.

---

## 4. Comparação com o padrão das rodadas anteriores

| Rodada | Período | Tipo | Gap vs. núcleo | Sinal de demanda | Diagnóstico |
|---|---|---|---|---|---|
| 1 | 04–08/09 | Feriado (7 Set) | +48,7% | MÉDIO/ALTO | MANTER/ESPERAR → PROTEGER/ESPERAR (1R) |
| 2 | 09–12/10 | Feriado (12 Out) | +48,3% | BAIXO | MANTER |
| 3 | 30/10–02/11 | Feriado (Finados) | +59,3%* | MÉDIO | MANTER |
| 4 | 19–22/11 | Feriado forte (Consc. Negra) | +54,9% | ALTO | PROTEGER |
| 5A | 06–08/11 | Comum (fim de semana) | +43,6% | MÉDIO | MANTER |
| 5B | 09–12/11 | Comum (meio de semana) | +47,8% | BAIXO | MANTER, ponto de atenção |
| **6A** | **07–11/12** | **Pré-alta (dias de semana)** | **+49,0%** | **MÉDIO** | **MANTER** |
| **6B** | **11–13/12** | **Pré-alta (fim de semana)** | **+58,3%** | **ALTO** | **PROTEGER** |

*gap parcialmente artefato de ausência do Kia Ora na amostra (ver Rodada 3).

O gap estrutural (~44–59%) se repete em oito rodadas seguidas, independente de feriado ou data comum — reforça a leitura já registrada de que é um padrão de composição da cesta, não efeito de data isolada. A diferença real entre as rodadas está sempre no sinal de demanda, não no gap de preço em si.

---

## 5. Dados que faltam

- Ritmo real de reservas/ocupação da Villa Arágua para o bloco 01–17/12/2026 (Stays) — o Radar mede só preço/disponibilidade de concorrente, não a demanda real pela Villa.
- Confirmação com Renildo de que R$ 629,00 (bucket único "Dezembro/2026 1-18") é a tarifa correta e ativa no motor hoje — tratar como "preço publicado a confirmar", não "aprovado".
- Ampliada e teto da Rodada 6B seguem sem dado válido por indisponibilidade real na data — não é possível completar essa camada nesta rodada; nova tentativa fica para rodada futura ou data adjacente.

---

## Conclusão

Nenhuma decisão nova foi gerada por este relatório. Nenhuma tarifa foi alterada. Nenhum cenário de redução foi simulado — não havia risco identificado que justificasse simular.

**Rodada 6A (dias de semana, 07–11/12):** `MANTER`
**Rodada 6B (fim de semana, 11–13/12):** `PROTEGER`

**Status deste relatório:** `RELATORIO_ANALITICO_SEM_ALTERACAO_TARIFARIA`
