# RELATÓRIO VISUAL — RADAR DE CONCORRÊNCIA REVENUE — POUSADA ARÁGUA (NOVEMBRO NORMAL 2026)

**Objetivo:** checar o posicionamento da Pousada Arágua em novembro/2026 **fora** das datas especiais (Finados e Consciência Negra já cobertas em rodadas anteriores), para entender se a tarifa comum do mês está competitiva, alta, baixa ou defensável.
**Rodadas cobertas:** Rodada 5A (fim de semana comum, 06–08/11/2026) e Rodada 5B (meio de semana comum, 09–12/11/2026)
**Produto Villa de referência:** Pousada Arágua — unidade base (Organic/Fuego/Metallo) · perfil casal (2 adultos, 0 crianças, 1 acomodação)
**Fontes:** `COLETAS_CONCORRENCIA_REVENUE.csv`, `CESTA_COMPETITIVA_REVENUE_VILLA_ARAGUA.md`, `ALERTAS_CONCORRENCIA_REVENUE.md`, `REGRAS_CONVERSAO_OTA_MOTOR_REVENUE.md`, `INVENTARIO_TARIFAS_PUBLICADAS_AGO2026_ABR2027.csv`
**Coleta:** 2026-07-27, via Booking (Claude in Chrome), preços públicos visíveis, sem login, sem clicar em reservar.
**Diagnóstico:** gerado via agente `villa-precificacao-calendario`, com consulta às skills `villa-aragua-pricing-revenue` e `villa-aragua-growth-marketer` — agente acionado de fato, não simulado pela memória da conversa.
**Status deste relatório:** `RELATORIO_ANALITICO_SEM_ALTERACAO_TARIFARIA`

---

## Nota de fonte sobre a tarifa da Villa

O inventário publicado tem duas linhas para novembro: **"Novembro/2026 base"** = R$ 526,00 (mín. 1–2 diárias, "Pré-temporada") e **"Novembro/2026 início/feriado"** = R$ 579,00 (mín. 3 diárias, tipo explicitamente "Feriado"). Como nenhuma das duas janelas coletadas (06–08/11 e 09–12/11) toca um feriado nacional — Finados já passou, Consciência Negra ainda não chegou, e 15/11 cai num domingo em 2026 sem gerar feriado prolongado — foi usada a linha **"Novembro/2026 base" (R$ 526,00)** para as duas sub-rodadas, inclusive a 5B (3 noites), tratando o número de noites como não determinante nesta decisão. **Isto é uma leitura, não um fato confirmado** — o inventário não detalha as datas exatas do bucket "início/feriado". Fica registrado como dado a confirmar com Renildo no Stays, tratado como "preço publicado a confirmar", nunca como "preço aprovado".

---

## 1. Tabela aberta — Rodada 5A (fim de semana comum, 06–08/11/2026, 2 noites)

Villa Arágua: motor **R$ 526,00** · Booking estimado **R$ 657,50**

| Grupo | Concorrente | Acomodação âncora | Status | Preço total Booking | Diária Booking | Motor equivalente | Dif. R$ vs Villa motor | Dif. % vs Villa motor | Observação |
|---|---|---|---|---|---|---|---|---|---|
| NUCLEO | Vila Maciel | Apartamento Standard | COLETADO_COM_SUCESSO | R$ 608,00 (20% off; original R$ 760,00) | R$ 304,00 | R$ 243,20 | −R$ 282,80 | −53,8% | Nota Booking 3/5; desconto ativo |
| NUCLEO | Pousada dos Ingleses | Quarto Duplo Clássico | COLETADO_COM_SUCESSO | R$ 839,00 (R$719 + R$120 taxas) | R$ 419,50 | R$ 335,60 | −R$ 190,40 | −36,2% | Taxa separada no site, já somada |
| NUCLEO | Pousada Dom Capudi | Quarto Duplo | COLETADO_COM_SUCESSO | R$ 903,00 | R$ 451,50 | R$ 361,20 | −R$ 164,80 | −31,3% | — |
| NUCLEO | Pousada Kia Ora Bombinhas | Quarto Duplo Deluxe c/ Vista Lateral do Mar | COLETADO_COM_SUCESSO | R$ 1.024,00 | R$ 512,00 | R$ 409,60 | −R$ 116,40 | −22,1% | — |
| NUCLEO | Vila Boa Vida | Quarto Duplo Standard | COLETADO_COM_SUCESSO | R$ 1.050,00 | R$ 525,00 | R$ 420,00 | −R$ 106,00 | −20,2% | — |
| NUCLEO | Pousada Kaloa Eco Village | Suíte Standard | COLETADO_COM_SUCESSO | R$ 1.072,00 | R$ 536,00 | R$ 428,80 | −R$ 97,20 | −18,5% | — |
| NUCLEO | Pousada Riviera Bombinhas | Suíte Loft Riviera | PRECISA_VALIDACAO_MANUAL | INDISPONIVEL | — | — | — | — | Todas as categorias esgotadas |
| AMPLIADA | UP Hotel Boutique | Quarto Duplo Deluxe com Banheira | COLETADO_COM_SUCESSO | R$ 1.252,00 (5% off; original R$1.318) | R$ 626,00 | R$ 500,80 | −R$ 25,20 | −4,8% | — |
| AMPLIADA | Morada do Guaruça | Apartamento de 1 Quarto | PRECISA_VALIDACAO_MANUAL | INDISPONIVEL (âncora) | — | — | — | — | Âncora esgotada; outras categorias mais caras à venda, não usadas por regra |
| TETO_MERCADO | Hotel/Pousada Atalaia do Mariscal | Suíte Superior | PRECISA_VALIDACAO_MANUAL | INDISPONIVEL | — | — | — | — | Todas as categorias esgotadas |

### Resumo executivo — Rodada 5A

| Indicador | Valor |
|---|---|
| Média núcleo Booking (n=6/7) | R$ 458,00 |
| Mediana núcleo Booking | R$ 481,75 |
| Média motor equivalente núcleo | R$ 366,40 |
| Média ampliada Booking (n=1/2, amostra fraca) | R$ 626,00 |
| Referência de teto | DADO_NAO_ENCONTRADO (Atalaia esgotada) |
| Índice de disponibilidade núcleo | 85,7% (6/7) |
| Índice de disponibilidade total tentado | 70% (7/10) |
| **Sinal de demanda** | **MÉDIO** — 3 de 10 concorrentes esgotados (Riviera núcleo, Morada âncora, Atalaia teto) num fim de semana "comum", sem feriado |

### Veredito de posicionamento — Rodada 5A

**`ACIMA_DO_NUCLEO_MAS_DEFENSAVEL`** — Villa +43,6% vs. núcleo (gap estrutural já visto em todas as rodadas); +5,0% vs. ampliada (quase alinhada, mas amostra fraca n=1). Sinal de demanda MÉDIO reforça a defensabilidade.

### Diagnóstico preliminar — Rodada 5A

**`MANTER`** — o gap estrutural vs. núcleo repete o padrão de todas as rodadas anteriores e não é, isoladamente, motivo de queda. A proximidade com a ampliada e o sinal de demanda MÉDIO (esgotamento real fora de feriado) reforçam manter a tarifa atual. **Preliminar — Renildo decide.**

---

## 2. Tabela aberta — Rodada 5B (meio de semana comum, 09–12/11/2026, 3 noites)

Villa Arágua: motor **R$ 526,00** · Booking estimado **R$ 657,50**

| Grupo | Concorrente | Acomodação âncora | Status | Preço total Booking | Diária Booking | Motor equivalente | Dif. R$ vs Villa motor | Dif. % vs Villa motor | Observação |
|---|---|---|---|---|---|---|---|---|---|
| NUCLEO | Vila Maciel | Apartamento Standard | COLETADO_COM_SUCESSO | R$ 744,00 (20% off; original R$930) | R$ 248,00 | R$ 198,40 | −R$ 327,60 | −62,3% | Desconto ativo |
| NUCLEO | Pousada dos Ingleses | Quarto Duplo Clássico | COLETADO_COM_SUCESSO | R$ 1.068,00 (R$948 + R$120 taxas) | R$ 356,00 | R$ 284,80 | −R$ 241,20 | −45,9% | Disponível — âncora esgotada na 5A |
| NUCLEO | Pousada Dom Capudi | Quarto Duplo | COLETADO_COM_SUCESSO | R$ 1.354,00 | R$ 451,33 | R$ 361,07 | −R$ 164,93 | −31,4% | — |
| NUCLEO | Pousada Riviera Bombinhas | Suíte Loft Riviera | COLETADO_COM_SUCESSO | R$ 1.458,00 | R$ 486,00 | R$ 388,80 | −R$ 137,20 | −26,1% | Disponível — esgotada na 5A |
| NUCLEO | Pousada Kia Ora Bombinhas | Quarto Duplo Deluxe c/ Vista Lateral do Mar | COLETADO_COM_SUCESSO | R$ 1.536,00 | R$ 512,00 | R$ 409,60 | −R$ 116,40 | −22,1% | — |
| NUCLEO | Vila Boa Vida | Quarto Duplo Standard | COLETADO_COM_SUCESSO | R$ 1.575,00 | R$ 525,00 | R$ 420,00 | −R$ 106,00 | −20,2% | — |
| NUCLEO | Pousada Kaloa Eco Village | Suíte Standard | COLETADO_COM_SUCESSO | R$ 1.608,00 | R$ 536,00 | R$ 428,80 | −R$ 97,20 | −18,5% | — |
| AMPLIADA | UP Hotel Boutique | Quarto Duplo Deluxe com Banheira | COLETADO_COM_SUCESSO | R$ 1.507,00 (7% off; original R$1.620) | R$ 502,33 | R$ 401,87 | −R$ 124,13 | −23,6% | — |
| AMPLIADA | Morada do Guaruça | Apartamento de 1 Quarto | COLETADO_COM_SUCESSO | R$ 1.597,00 | R$ 532,33 | R$ 425,87 | −R$ 100,13 | −19,0% | Disponível — âncora esgotada na 5A |
| TETO_MERCADO | Hotel/Pousada Atalaia do Mariscal | Suíte Superior | COLETADO_COM_SUCESSO | R$ 3.600,00 | R$ 1.200,00 | R$ 960,00 | +R$ 434,00 | +82,5% | Referência, não entra em média; disponível — esgotada na 5A |

### Resumo executivo — Rodada 5B

| Indicador | Valor |
|---|---|
| Média núcleo Booking (n=7/7, completa) | R$ 444,90 |
| Mediana núcleo Booking | R$ 486,00 |
| Média motor equivalente núcleo | R$ 355,92 |
| Média ampliada Booking (n=2/2, completa) | R$ 517,33 |
| Referência de teto (n=1/1) | R$ 1.200,00 |
| Índice de disponibilidade núcleo | 100% (7/7) |
| Índice de disponibilidade total tentado | 100% (10/10) |
| **Sinal de demanda** | **BAIXO** — zero esgotamentos, contraste direto com a 5A a poucos dias de distância |

### Veredito de posicionamento — Rodada 5B

**`ACIMA_DO_MERCADO_COM_RISCO`** — amostra completa (núcleo 7/7, ampliada 2/2), Villa +47,8% vs. núcleo e +27,1% vs. ampliada — o maior gap vs. ampliada já registrado no Radar com amostra completa. Combinado ao sinal de demanda BAIXO, é o cenário com risco mais concreto de todas as coletas até agora.

### Diagnóstico preliminar — Rodada 5B

**`MANTER`**, com **ponto de atenção explícito** — o vocabulário oficial exige justificativa registrada para `BAIXAR_COM_JUSTIFICATIVA`, e a leitura comercial não sustenta baixa automática só porque o núcleo de OTA está mais barato. O padrão (gap grande + sinal BAIXO) já apareceu na Rodada 2 e mesmo assim ficou `MANTER`. Diferença: o gap vs. ampliada aqui (+27,1%) é bem maior que na Rodada 2 (+10,9%) — fica registrado como sinal a monitorar em rodadas futuras de "novembro comum", não como decisão. **Preliminar — Renildo decide.**

---

## 3. Ranking visual por rodada

### Rodada 5A — do menor para o maior (diária Booking)

**Núcleo:**
1. Vila Maciel — R$ 304,00
2. Pousada dos Ingleses — R$ 419,50
3. Pousada Dom Capudi — R$ 451,50
4. Pousada Kia Ora Bombinhas — R$ 512,00
5. Vila Boa Vida — R$ 525,00
6. Pousada Kaloa Eco Village — R$ 536,00
— Pousada Riviera Bombinhas: indisponível, fora do ranking

**Ampliada:**
1. UP Hotel Boutique — R$ 626,00
— Morada do Guaruça: âncora indisponível, fora do ranking

**Teto de mercado:**
— Hotel/Pousada Atalaia do Mariscal: indisponível, fora do ranking

### Rodada 5B — do menor para o maior (diária Booking)

**Núcleo:**
1. Vila Maciel — R$ 248,00
2. Pousada dos Ingleses — R$ 356,00
3. Pousada Dom Capudi — R$ 451,33
4. Pousada Riviera Bombinhas — R$ 486,00
5. Pousada Kia Ora Bombinhas — R$ 512,00
6. Vila Boa Vida — R$ 525,00
7. Pousada Kaloa Eco Village — R$ 536,00

**Ampliada:**
1. UP Hotel Boutique — R$ 502,33
2. Morada do Guaruça — R$ 532,33

**Teto de mercado:**
1. Hotel/Pousada Atalaia do Mariscal — R$ 1.200,00

---

## 4. Comparação com o padrão das rodadas de feriado (1 a 4)

| Rodada | Período | Tipo | Gap vs. núcleo | Gap vs. ampliada | Sinal de demanda | Diagnóstico |
|---|---|---|---|---|---|---|
| 1 | 04–08/09 | Feriado (7 Set) | +48,7% | +3,4% (n=1, fraca) | MÉDIO/ALTO | MANTER/ESPERAR → PROTEGER/ESPERAR (1R) |
| 2 | 09–12/10 | Feriado (12 Out) | +48,3% | +10,9% (n=2, completa) | BAIXO | MANTER |
| 3 | 30/10–02/11 | Feriado (Finados) | +59,3%* | −3,8% (n=2, completa) | MÉDIO | MANTER |
| 4 | 19–22/11 | Feriado forte (Consc. Negra) | +54,9% | +31,2% (n=2, completa) | ALTO | PROTEGER |
| **5A** | **06–08/11** | **Comum (fim de semana)** | **+43,6%** | **+5,0% (n=1, fraca)** | **MÉDIO** | **MANTER** |
| **5B** | **09–12/11** | **Comum (meio de semana)** | **+47,8%** | **+27,1% (n=2, completa)** | **BAIXO** | **MANTER, com ponto de atenção** |

*gap parcialmente artefato de ausência do Kia Ora na amostra (ver Rodada 3).

**Leitura comparativa:** a tarifa de novembro comum está, de forma geral, tão ou mais defensável quanto a maioria das datas de feriado frente ao núcleo — o gap estrutural (~+44% a +48%) se repete em praticamente todas as rodadas, feriado ou não, reforçando que é um padrão de composição da cesta, não um efeito de data específica. A diferença real está na **5B frente à ampliada**: com +27,1% e amostra completa, o gap se aproxima do nível da Rodada 4 (+31,2%), mas sem o sinal de demanda que sustentou `PROTEGER` naquela rodada — aqui o sinal é o oposto (BAIXO). É o primeiro momento do Radar em que "gap grande + amostra completa + zero pressão de demanda" aparecem juntos.

---

## 5. Leitura comercial (growth-marketer)

A skill `villa-aragua-growth-marketer` (referência `reserva-direta-reducao-otas.md`) reforça que "a Villa Arágua não compete por ser mais barata que a OTA — compete por valor agregado (atendimento, relação, previsibilidade). Baixar preço para 'vencer' a OTA corrói margem sem necessidade." Esse princípio pesa contra qualquer baixa automática motivada só pela média núcleo, em ambas as sub-rodadas — mas o mesmo documento reconhece um limite: a OTA ainda é útil para "preencher ocupação em datas de baixa demanda", que é exatamente o perfil da 5B.

**Diferença relevante entre 5A e 5B:**
- **5A (fim de semana):** o sinal de demanda MÉDIO (esgotamento real em 3 de 10 tentativas) já reduz por si só a pressão para baixar — há evidência de mercado apoiando `MANTER`, sem depender só do argumento de marca.
- **5B (meio de semana):** o sinal de demanda BAIXO retira esse apoio — a sustentação do preço atual depende mais diretamente do argumento comercial (atendimento próximo, previsibilidade, reserva direta via WhatsApp) do que de qualquer evidência de escassez. É o cenário mais frágil para `MANTER` sem esforço comercial ativo — reserva direta, Meta Ads direcionando para conversa qualificada em vez de comparação de preço.

Nenhuma condição comercial, desconto ou texto de venda foi decidido neste relatório — eventual ação é handoff para o agente `villa-comercial-reservas`.

---

## Dados que faltam

- Confirmação no sistema (Stays) de que R$ 526,00 é de fato a tarifa aplicável tanto a 06–08/11 quanto a 09–12/11 — o inventário não detalha as datas exatas do bucket "Novembro/2026 início/feriado" (R$ 579,00).
- Nenhum feriado/evento identificado nas fontes que justifique esse bucket logo no início de novembro — vale confirmar com Renildo a que ele se refere.
- Ampliada da 5A com amostra fraca (1 de 2, Morada esgotada) — leitura indicativa, não conclusiva.
- Nenhum dado de ocupação real da Pousada Arágua para novembro/2026 (reservas confirmadas, ritmo de vendas) — a análise é só de posicionamento frente à concorrência visível no Booking.
- Proporção reserva direta vs. OTA para calibrar o peso do argumento comercial na 5B — pendência já registrada na skill de growth-marketer.

---

## Conclusão

Nenhuma decisão nova foi gerada por este relatório. Ambos os diagnósticos permanecem **preliminares** — não foram movidos para `DECISOES_REVENUE_PENDENTES_VILLA_ARAGUA.md`. Nenhuma tarifa foi alterada.

**Rodada 5A (fim de semana comum):** `MANTER`
**Rodada 5B (meio de semana comum):** `MANTER`, com ponto de atenção — maior gap vs. ampliada já registrado com amostra completa, sem sinal de demanda para sustentá-lo; monitorar em rodadas futuras.

**Status deste relatório:** `RELATORIO_ANALITICO_SEM_ALTERACAO_TARIFARIA`
