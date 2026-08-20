# RELATÓRIO VISUAL — RADAR DE CONCORRÊNCIA REVENUE — POUSADA ARÁGUA (FINAL DE OUTUBRO / NOVEMBRO 2026)

**Rodadas cobertas:** Rodada 3 (Finados, 30/10–02/11/2026) e Rodada 4 (feriado forte de Consciência Negra, 19–22/11/2026)
**Produto Villa de referência:** Pousada Arágua — unidade base (Organic/Fuego/Metallo) · perfil casal (2 adultos, 0 crianças, 1 acomodação)
**Fontes:** `COLETAS_CONCORRENCIA_REVENUE.csv`, `CESTA_COMPETITIVA_REVENUE_VILLA_ARAGUA.md`, `ALERTAS_CONCORRENCIA_REVENUE.md` (seções 6 e 7), `REGRAS_CONVERSAO_OTA_MOTOR_REVENUE.md`, `INVENTARIO_TARIFAS_PUBLICADAS_AGO2026_ABR2027.csv`
**Coleta:** 2026-07-26, via Booking (Claude in Chrome), preços públicos visíveis, sem login, sem clicar em reservar.
**Diagnóstico:** gerado via agente `villa-precificacao-calendario`, com consulta às skills `villa-aragua-pricing-revenue` e `villa-aragua-growth-marketer` — agente acionado de fato, não simulado pela memória da conversa.
**Status deste relatório:** `RELATORIO_ANALITICO_SEM_ALTERACAO_TARIFARIA`

---

## 1. Resumo executivo

- **Rodada 3 (Finados, 30/10–02/11):** Villa motor R$ 529,00 · Booking estimado R$ 661,25. Núcleo com 6 de 7 concorrentes disponíveis (Kia Ora esgotado). Villa +59,3% acima da média núcleo, −3,8% abaixo da média ampliada. Sinal de demanda `MÉDIO`. **Diagnóstico preliminar: `MANTER`.**
- **Rodada 4 (Consciência Negra, feriado forte 19–22/11):** Villa motor R$ 717,00 · Booking estimado R$ 896,25. Núcleo com apenas 5 de 7 disponíveis (Ingleses e Dom Capudi com a acomodação-âncora esgotada). Villa +54,9% acima da média núcleo, +31,2% acima da média ampliada. Sinal de demanda `ALTO`, reforçado por aviso do próprio Booking de escassez regional ("6 hotéis 4 estrelas já indisponíveis"). **Diagnóstico preliminar: `PROTEGER`.**
- Nenhuma tarifa foi alterada, nenhuma decisão foi registrada em `DECISOES_REVENUE_PENDENTES_VILLA_ARAGUA.md`. Os dois diagnósticos são **preliminares**, para leitura humana.
- O gap grande da Rodada 3 frente ao núcleo (+59,3%) é parcialmente artefato de amostra — Kia Ora, o núcleo historicamente mais caro, estava esgotado nessa rodada e reaparece na Rodada 4.

---

## 2. Tabela visual — Rodada 3 (Finados, 30/10–02/11/2026, 3 noites)

Villa Arágua: motor **R$ 529,00** · Booking estimado **R$ 661,25**

### A. Núcleo (peso alto)

| Concorrente | Acomodação âncora | Status | Preço total Booking | Diária Booking | Motor equivalente | Dif. R$ vs Villa motor | Dif. % vs Villa motor | Observação |
|---|---|---|---|---|---|---|---|---|
| Pousada dos Ingleses | Quarto Duplo Clássico | COLETADO_COM_SUCESSO | R$ 829,00 (R$ 709 + R$ 120 taxas) | R$ 276,33 | R$ 221,07 | −R$ 307,93 | −58,2% | Site exibe taxa separada do preço-base |
| Vila Maciel | Apartamento Standard | COLETADO_COM_SUCESSO | R$ 840,00 (20% off; original R$ 1.050,00) | R$ 280,00 | R$ 224,00 | −R$ 305,00 | −57,7% | Preço com desconto promocional ativo; nota de qualidade Booking 3/5 |
| Pousada Dom Capudi | Quarto Duplo | COLETADO_COM_SUCESSO | R$ 1.354,00 | R$ 451,33 | R$ 361,07 | −R$ 167,93 | −31,7% | — |
| Vila Boa Vida | Quarto Duplo Standard | COLETADO_COM_SUCESSO | R$ 1.373,00 | R$ 457,67 | R$ 366,13 | −R$ 162,87 | −30,8% | — |
| Pousada Kaloa Eco Village | Suíte Standard | COLETADO_COM_SUCESSO | R$ 1.510,00 | R$ 503,33 | R$ 402,67 | −R$ 126,33 | −23,9% | — |
| Pousada Riviera Bombinhas | Suíte Loft Riviera | COLETADO_COM_SUCESSO | R$ 1.568,00 | R$ 522,67 | R$ 418,13 | −R$ 110,87 | −21,0% | — |

### B. Ampliada (peso baixo)

| Concorrente | Acomodação âncora | Status | Preço total Booking | Diária Booking | Motor equivalente | Dif. R$ vs Villa motor | Dif. % vs Villa motor | Observação |
|---|---|---|---|---|---|---|---|---|
| Morada do Guaruça | Apartamento de 1 Quarto | COLETADO_COM_SUCESSO | R$ 1.835,00 | R$ 611,67 | R$ 489,33 | −R$ 39,67 | −7,5% | — |
| UP Hotel Boutique | Quarto Duplo Deluxe com Banheira | COLETADO_COM_SUCESSO | R$ 2.291,00 (7% off; original R$ 2.464,00) | R$ 763,67 | R$ 610,93 | +R$ 81,93 | +15,5% | — |

### C. Teto de mercado

| Concorrente | Acomodação âncora | Status | Preço total Booking | Diária Booking | Motor equivalente | Dif. R$ vs Villa motor | Dif. % vs Villa motor | Observação |
|---|---|---|---|---|---|---|---|---|
| Hotel/Pousada Atalaia do Mariscal | Suíte Superior | COLETADO_COM_SUCESSO | R$ 4.500,00 | R$ 1.500,00 | R$ 1.200,00 | +R$ 671,00 | +126,8% | Referência de teto — não entra em nenhuma média |

### D. Indisponíveis / não usados na média

| Concorrente | Grupo | Status | Motivo |
|---|---|---|---|
| Pousada Kia Ora Bombinhas | NUCLEO | PRECISA_VALIDACAO_MANUAL | Booking: "Não temos disponibilidade" para todas as categorias no período — esgotado |

---

## 3. Tabela visual — Rodada 4 (Consciência Negra, feriado forte 19–22/11/2026, 3 noites)

Villa Arágua: motor **R$ 717,00** · Booking estimado **R$ 896,25**

### A. Núcleo (peso alto)

| Concorrente | Acomodação âncora | Status | Preço total Booking | Diária Booking | Motor equivalente | Dif. R$ vs Villa motor | Dif. % vs Villa motor | Observação |
|---|---|---|---|---|---|---|---|---|
| Vila Maciel | Apartamento Standard | COLETADO_COM_SUCESSO | R$ 1.032,00 (20% off; original R$ 1.290,00) | R$ 344,00 | R$ 275,20 | −R$ 441,80 | −61,6% | Preço com desconto promocional ativo |
| Vila Boa Vida | Quarto Duplo Standard | COLETADO_COM_SUCESSO | R$ 1.575,00 | R$ 525,00 | R$ 420,00 | −R$ 297,00 | −41,4% | — |
| Pousada Kaloa Eco Village | Suíte Standard | COLETADO_COM_SUCESSO | R$ 1.608,00 | R$ 536,00 | R$ 428,80 | −R$ 288,20 | −40,2% | — |
| Pousada Kia Ora Bombinhas | Quarto Duplo Deluxe c/ Vista Lateral do Mar | COLETADO_COM_SUCESSO | R$ 2.195,00 | R$ 731,67 | R$ 585,33 | −R$ 131,67 | −18,4% | Volta a aparecer disponível (estava esgotado na Rodada 3) |
| Pousada Riviera Bombinhas | Suíte Loft Riviera | COLETADO_COM_SUCESSO | R$ 2.269,00 | R$ 756,33 | R$ 605,07 | −R$ 111,93 | −15,6% | Maior salto de preço do ciclo frente à Rodada 3 (+R$ 186,93 motor equiv.) |

### B. Ampliada (peso baixo)

| Concorrente | Acomodação âncora | Status | Preço total Booking | Diária Booking | Motor equivalente | Dif. R$ vs Villa motor | Dif. % vs Villa motor | Observação |
|---|---|---|---|---|---|---|---|---|
| UP Hotel Boutique | Quarto Duplo Deluxe com Banheira | COLETADO_COM_SUCESSO | R$ 1.977,00 (7% off; original R$ 2.126,00) | R$ 659,00 | R$ 527,20 | −R$ 189,80 | −26,5% | — |
| Morada do Guaruça | Apartamento de 1 Quarto | COLETADO_COM_SUCESSO | R$ 2.122,00 | R$ 707,33 | R$ 565,87 | −R$ 151,13 | −21,1% | — |

### C. Teto de mercado

| Concorrente | Acomodação âncora | Status | Preço total Booking | Diária Booking | Motor equivalente | Dif. R$ vs Villa motor | Dif. % vs Villa motor | Observação |
|---|---|---|---|---|---|---|---|---|
| Hotel/Pousada Atalaia do Mariscal | Suíte Superior | COLETADO_COM_SUCESSO | R$ 3.900,00 | R$ 1.300,00 | R$ 1.040,00 | +R$ 323,00 | +45,0% | Booking exibia aviso: "6 hotéis 4 estrelas como este já estão indisponíveis no nosso site" — sinal de escassez regional |

### D. Indisponíveis / não usados na média

| Concorrente | Grupo | Status | Motivo |
|---|---|---|---|
| Pousada dos Ingleses | NUCLEO | PRECISA_VALIDACAO_MANUAL | Âncora aprovada (Quarto Duplo Clássico) não aparecia entre as categorias disponíveis — provável esgotamento. Outras categorias mais caras seguiam à venda (Chalé Master, Suíte, Quarto Duplo Básico), não usadas por não serem a âncora aprovada |
| Pousada Dom Capudi | NUCLEO | PRECISA_VALIDACAO_MANUAL | Âncora aprovada (Quarto Duplo) não aparecia entre as categorias disponíveis — provável esgotamento. Outras categorias mais caras seguiam à venda (Suíte Premium, Suíte com Vista do Jardim, Quarto Triplo Standard), não usadas por não serem a âncora aprovada |

---

## 4. Ranking visual por rodada

### Rodada 3 — do menor para o maior (diária Booking)

**Núcleo:**
1. Pousada dos Ingleses — R$ 276,33
2. Vila Maciel — R$ 280,00
3. Pousada Dom Capudi — R$ 451,33
4. Vila Boa Vida — R$ 457,67
5. Pousada Kaloa Eco Village — R$ 503,33
6. Pousada Riviera Bombinhas — R$ 522,67
— Pousada Kia Ora Bombinhas: indisponível, fora do ranking

**Ampliada:**
1. Morada do Guaruça — R$ 611,67
2. UP Hotel Boutique — R$ 763,67

**Teto de mercado:**
1. Hotel/Pousada Atalaia do Mariscal — R$ 1.500,00

### Rodada 4 — do menor para o maior (diária Booking)

**Núcleo:**
1. Vila Maciel — R$ 344,00
2. Vila Boa Vida — R$ 525,00
3. Pousada Kaloa Eco Village — R$ 536,00
4. Pousada Kia Ora Bombinhas — R$ 731,67
5. Pousada Riviera Bombinhas — R$ 756,33
— Pousada dos Ingleses: âncora esgotada, fora do ranking
— Pousada Dom Capudi: âncora esgotada, fora do ranking

**Ampliada:**
1. UP Hotel Boutique — R$ 659,00
2. Morada do Guaruça — R$ 707,33

**Teto de mercado:**
1. Hotel/Pousada Atalaia do Mariscal — R$ 1.300,00

---

## 5. Comparativo com Villa Arágua

| Métrica | Rodada 3 (Finados, 30/10–02/11) | Rodada 4 (Consciência Negra, 19–22/11) |
|---|---|---|
| Período | 30/10–02/11/2026 (3 noites) | 19–22/11/2026 (3 noites, feriado forte) |
| Villa motor base | R$ 529,00 | R$ 717,00 |
| Villa Booking estimado | R$ 661,25 | R$ 896,25 |
| Média núcleo Booking | R$ 415,22 (n=6 de 7) | R$ 578,60 (n=5 de 7) |
| Mediana núcleo Booking | R$ 454,50 | R$ 536,00 |
| Média motor equivalente núcleo | R$ 332,18 | R$ 462,88 |
| Média ampliada Booking | R$ 687,67 (n=2 de 2) | R$ 683,17 (n=2 de 2) |
| Villa vs. núcleo | +59,3% | +54,9% |
| Villa vs. ampliada | −3,8% | +31,2% |
| indice_disponibilidade_nucleo | 85,7% (6 de 7) | 71,4% (5 de 7) |
| indice_disponibilidade_total_tentado | 90% (9 de 10) | 80% (8 de 10) |
| sinal_demanda | MÉDIO | ALTO |
| Diagnóstico preliminar | `MANTER` | `PROTEGER` |

**Comparativo com as rodadas anteriores (Set/Out):** o padrão "Villa bem acima do núcleo, mais próxima ou ligeiramente acima da ampliada" se repete agora em quatro rodadas (Rodada 1: +48,7%/+3,4%; Rodada 2: +48,3%/+10,9%; Rodada 3: +59,3%/−3,8%; Rodada 4: +54,9%/+31,2%). O gap vs. núcleo oscila mais entre 48% e 59%, mas nunca inverte — a Villa nunca fica abaixo da média núcleo em nenhuma das quatro rodadas registradas até agora.

---

## 6. Leitura comercial (growth-marketer)

A leitura de que "a Villa Arágua não compete por ser mais barata que a OTA — compete por valor agregado" (skill `villa-aragua-growth-marketer`, referência `reserva-direta-reducao-otas.md`) se sustenta nas duas rodadas, com ênfase diferente:

- **Rodada 3 (sinal médio):** o gap grande vs. núcleo (+59,3%) é majoritariamente artefato de amostra — ausência do Kia Ora, historicamente o núcleo mais caro. Não há sinal de queda de demanda que justifique baixa; pelo contrário, há 1 esgotamento. A leitura comercial funciona aqui como argumento defensivo: não usar o gap de OTA como gatilho automático de redução.
- **Rodada 4 (sinal alto):** o argumento comercial é mais robusto — 2 esgotamentos no núcleo mais barato **e** um aviso de escassez regional do próprio Booking (não de um concorrente isolado) sustentam `PROTEGER` com mais confiança do que o `MANTER` mais cauteloso da Rodada 3. Aqui não é apenas "não há motivo para baixar" — há sinal ativo de que a região está com procura forte.
- Em nenhuma das duas rodadas a skill sustenta `BAIXAR_COM_JUSTIFICATIVA`: o preço de concorrente é referência de calibragem, "nunca ordem a seguir" (skill `villa-aragua-pricing-revenue`, referência `concorrentes-otas.md`).
- Nenhuma condição comercial, desconto ou texto de venda foi decidido neste relatório — eventual transformação em resposta de objeção de WhatsApp é handoff para o agente `villa-comercial-reservas`.

---

## 7. Diagnóstico preliminar (vocabulário oficial)

**Rodada 3 (Finados, 30/10–02/11/2026): `MANTER`**
Justificativa: gap vs. núcleo inflado por ausência do Kia Ora na amostra; gap vs. ampliada praticamente neutro (−3,8%); sinal de demanda `MÉDIO` não sustenta alta nem baixa. Leitura mais honesta com o dado disponível.

**Rodada 4 (Consciência Negra, feriado forte 19–22/11/2026): `PROTEGER`**
Justificativa: maior sinal de demanda das quatro rodadas registradas (2 concorrentes núcleo com âncora esgotada + aviso de escassez regional do próprio Booking); tarifa de feriado forte já publicada combinada a esse sinal aponta para proteger o preço, não reduzir.

Nenhum destes diagnósticos foi movido para `DECISOES_REVENUE_PENDENTES_VILLA_ARAGUA.md`. Ambos permanecem registrados como preliminares nas seções 6 e 7 de `ALERTAS_CONCORRENCIA_REVENUE.md`.

---

## 8. Pontos de atenção para Renildo

- **Kia Ora sumindo/reaparecendo entre rodadas:** esgotado na Rodada 3, disponível na Rodada 4 a R$ 731,67 diária — é o concorrente núcleo historicamente mais caro (R$ 468–585 motor equiv. nas rodadas em que aparece). Sua ausência pontual distorce a média núcleo para baixo; sempre checar se está na amostra antes de interpretar um "gap vs. núcleo" isolado.
- **Riviera com salto de preço na Rodada 4:** de R$ 418,13 para R$ 605,07 motor equivalente — o maior aumento entre rodadas de qualquer concorrente núcleo neste ciclo, ficando o mais caro do núcleo depois do Kia Ora. Vale monitorar em rodadas futuras se é um ajuste pontual de feriado forte ou uma mudança de posicionamento.
- **Escassez regional no teto de mercado (Rodada 4):** o aviso "6 hotéis 4 estrelas já indisponíveis" é dado do próprio Booking, não estimativa — sinal de mercado mais forte do que qualquer coleta pontual de concorrente isolado.
- **Ingleses e Dom Capudi com âncora esgotada (Rodada 4):** os dois concorrentes núcleo mais baratos ficaram sem a categoria de entrada, reduzindo a amostra núcleo para 5 de 7 — isso enfraquece um pouco a precisão da média núcleo desta rodada especificamente.
- **Gap entre Villa e inventário publicado (Finados):** o inventário não tem linha própria para Finados (30/10–02/11) — usa o mesmo valor de "Outubro/2026 feriado" (R$ 529,00) já aplicado à Rodada 2 (12 de outubro). Vale confirmar com Renildo se Finados, por ser feriado nacional, deveria ter régua distinta do feriado municipal de 12/10 — isso não foi presumido nem corrigido automaticamente aqui.
- **Amostra ainda pequena (4 rodadas):** o padrão "Villa bem acima do núcleo, mais próxima da ampliada" já se repete nas quatro rodadas — começa a parecer estrutural, mas ainda não é amostra suficiente para virar regra fixa de precificação.
