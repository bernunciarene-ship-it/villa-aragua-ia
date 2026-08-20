# RELATÓRIO VISUAL — RADAR DE CONCORRÊNCIA REVENUE — POUSADA ARÁGUA (CARNAVAL 2027)

**Objetivo:** analisar o posicionamento competitivo da Pousada Arágua no Carnaval 2027, considerando o pacote de 5 diárias mínimas, sobre uma tarifa **já decidida e aplicada** por Renildo (Card 2 de `DECISOES_REVENUE_PENDENTES_VILLA_ARAGUA.md`, 2026-07-25) — esta rodada verifica o posicionamento competitivo, não propõe alteração.

**Rodada coberta:** Rodada 10 — Carnaval 2027, 05/02/2027 a 10/02/2027 (5 noites vendidas: 05, 06, 07, 08 e 09/02, check-out 10/02)
**Produto Villa de referência:** Pousada Arágua — unidade base (Organic/Fuego/Metallo) · perfil casal (2 adultos, 0 crianças, 1 acomodação)
**Fontes:** `COLETAS_CONCORRENCIA_REVENUE.csv`, `CESTA_COMPETITIVA_REVENUE_VILLA_ARAGUA.md`, `ALERTAS_CONCORRENCIA_REVENUE.md`, `REGRAS_CONVERSAO_OTA_MOTOR_REVENUE.md`, `INVENTARIO_TARIFAS_PUBLICADAS_AGO2026_ABR2027.csv`, `DECISOES_REVENUE_PENDENTES_VILLA_ARAGUA.md`
**Coleta:** 2026-07-28, via Booking (Claude in Chrome), preços públicos visíveis, sem login, sem clicar em reservar.
**Diagnóstico:** gerado via agente `villa-precificacao-calendario`, com consulta às skills `villa-aragua-pricing-revenue` e `villa-aragua-growth-marketer` — agente acionado de fato. Todos os números conferidos linha a linha no CSV, sem divergência.
**Status deste relatório:** `RELATORIO_ANALITICO_SEM_ALTERACAO_TARIFARIA` — diagnóstico **preliminar**. Renildo decide. O Card 2 (já `DECIDIDO_APLICADO`) não foi tocado.

**Villa Arágua no Carnaval:** motor R$ 1.070,00/diária (base Organic/Fuego/Metallo, tarifa plana — sem variação dia a dia dentro do pacote) · Booking estimado R$ 1.337,50/diária · pacote total (5 diárias) motor R$ 5.350,00 / Booking estimado R$ 6.687,50.

---

## 1. Tabela aberta — concorrentes

| Grupo | Concorrente | Acomodação âncora | Status | Preço total Booking | Diária média Booking | Motor equivalente médio | Dif. R$ vs. diária média Villa motor | Dif. % vs. Villa motor | Observação |
|---|---|---|---|---|---|---|---|---|---|
| NUCLEO | Vila Maciel | Apartamento Standard | COLETADO_COM_SUCESSO | R$ 2.531,00 (26% off; original R$ 3.420,00) | R$ 506,20 | R$ 404,96 | −R$ 665,04 | −62,2% | Nota Booking 3/5. Desconto promocional ativo de 26% — sinal de dificuldade de venda própria, não referência saudável de mercado |
| NUCLEO | Pousada Kaloa Eco Village | Suíte Standard | COLETADO_COM_SUCESSO | R$ 3.738,00 | R$ 747,60 | R$ 598,08 | −R$ 471,92 | −44,1% | Sem desconto ativo |
| NUCLEO | Pousada Dom Capudi | Quarto Duplo | COLETADO_COM_SUCESSO | R$ 4.988,00 | R$ 997,60 | R$ 798,08 | −R$ 271,92 | −25,4% | Historicamente sinalizado como "geralmente esgotado" em rodadas anteriores |
| NUCLEO | Pousada Kia Ora Bombinhas | Quarto Duplo Deluxe c/ Vista Lateral do Mar | COLETADO_COM_SUCESSO | R$ 5.486,00 | R$ 1.097,20 | R$ 877,76 | −R$ 192,24 | −18,0% | Categoria já é upgrade dentro do próprio concorrente (vista do mar) |
| NUCLEO | Vila Boa Vida | — | PRECISA_VALIDACAO_MANUAL | INDISPONIVEL | — | — | — | — | "Não temos disponibilidade" — **primeira vez em toda a série histórica (Rodadas 1–9D) que este concorrente aparece esgotado** |
| NUCLEO | Pousada Riviera Bombinhas | — | PRECISA_VALIDACAO_MANUAL | INDISPONIVEL | — | — | — | — | Esgotada; já havia ocorrido em outras rodadas (5A, 6B, 7B, 8B) |
| NUCLEO | Pousada dos Ingleses | — | PRECISA_VALIDACAO_MANUAL | INDISPONIVEL (âncora) | — | — | — | — | Âncora (Quarto Duplo Clássico) esgotada; categorias mais caras seguiam à venda, não usadas |
| AMPLIADA | UP Hotel Boutique | Quarto Duplo Deluxe com Banheira | COLETADO_COM_SUCESSO | R$ 5.569,00 | R$ 1.113,80 | R$ 891,04 | −R$ 178,96 | −16,7% | Único disponível do grupo. Banheira de hidromassagem em todas as categorias |
| AMPLIADA | Morada do Guaruça | — | PRECISA_VALIDACAO_MANUAL | INDISPONIVEL | — | — | — | — | Esgotada, todas as categorias |
| TETO_MERCADO | Hotel/Pousada Atalaia do Mariscal | Suíte Superior | COLETADO_COM_SUCESSO | R$ 14.500,00 | R$ 2.900,00 | R$ 2.320,00 | +R$ 1.250,00 | +115,0% | Referência, não entra em nenhuma média. **Sem** aviso de escassez regional nesta rodada — diferente de várias rodadas anteriores |

**Pendente/não usar:** Vila dos Açores — não coletado nesta rodada, sem dado para este período.

---

## 2. Tabela da Villa

| Acomodação | Valor motor/diária | Total motor pacote (5 diárias) | Diária média motor | Total Booking estimado | Diária média Booking estimada | Mínimo de noites | Observação |
|---|---|---|---|---|---|---|---|
| Organic / Fuego / Metallo (base) | R$ 1.070,00 | R$ 5.350,00 | R$ 1.070,00 | R$ 6.687,50 | R$ 1.337,50 | 5 | Unidade de referência desta rodada |
| Terra / Wood | R$ 1.231,00 | R$ 6.155,00 | R$ 1.231,00 | R$ 7.693,75 | R$ 1.538,75 | 5 | ≈115% sobre a base — régua respeitada |
| Acqua | R$ 1.338,00 | R$ 6.690,00 | R$ 1.338,00 | R$ 8.362,50 | R$ 1.672,50 | 5 | ≈125% sobre a base — régua respeitada |
| Luna | R$ 1.412,00 | R$ 7.060,00 | R$ 1.412,00 | R$ 8.825,00 | R$ 1.765,00 | 5 | ≈132% sobre a base — régua respeitada |
| Duplex Soleil | R$ 1.744,00 | R$ 8.720,00 | R$ 1.744,00 | R$ 10.900,00 | R$ 2.180,00 | 5 | ≈163% sobre a base (temporada forte) — régua respeitada |

**Nenhum erro de régua encontrado** — os valores decididos em 2026-07-25 (Card 2) conferem exatamente com a régua percentual aprovada aplicada sobre a base de R$ 1.070,00.

---

## 3. Resumo executivo

| Indicador | Valor |
|---|---|
| Núcleo disponível | 4 de 7 (57,1%) |
| Média núcleo Booking (diária) | R$ 837,15 |
| Mediana núcleo Booking (diária) | R$ 872,60 |
| Média motor equivalente núcleo | R$ 669,72 |
| Média ampliada Booking (n=1/2, só UP) | R$ 1.113,80 |
| Referência de teto (Atalaia) | R$ 2.900,00 Booking / R$ 2.320,00 motor |
| Índice de disponibilidade total (6 de 10) | 60,0% |
| **Sinal de demanda** | **ALTO** — Vila Boa Vida esgotada pela primeira vez em toda a série histórica de coletas (Rodadas 1 a 9D); 3 de 7 do núcleo indisponíveis (43%) no maior pacote de feriado fora de Natal/Réveillon |

---

## 4. Veredito de posicionamento

**`ACIMA_DO_NUCLEO_MAS_DEFENSAVEL`** — Villa +59,8% acima da média motor equivalente do núcleo (puxada para baixo por Vila Maciel, produto simples com desconto ativo de 26%). Frente aos concorrentes de padrão mais próximo (Kia Ora −18,0%, Dom Capudi −25,4%) e frente à ampliada (UP −16,7%), a diferença é bem mais modesta e defensável. Villa segue muito abaixo do teto de mercado (+115,0% de headroom acima da Villa) — há espaço de mercado acima, não risco de isolamento no topo.

---

## 5. Diagnóstico preliminar

**`PROTEGER`** — tarifa de data forte já decidida e aplicada por Renildo (Card 2, `DECIDIDO_APLICADO`, respeitando a régua interna). O sinal de demanda ALTO (esgotamento recorde do núcleo, incluindo um concorrente que nunca havia esgotado antes) reforça que não há motivo para abrir espaço para desconto — é hora de proteger o patamar já decidido. Esta rodada **não gera decisão nova** nem move nada em `DECISOES_REVENUE_PENDENTES_VILLA_ARAGUA.md` — apenas confirma que o Card 2 segue bem sustentado pelos dados.

---

## 6. Leitura específica de Carnaval

**A Pousada Arágua está bem posicionada para Carnaval?**
Sim, de forma geral. Acima da média núcleo, mas dentro de faixa defensável frente aos concorrentes de padrão mais comparável (Kia Ora, Dom Capudi), e a régua interna está coerente com o patamar já testado em janeiro/2027.

**O pacote de 5 diárias está competitivo?**
Em estrutura, sim — mínimo de 5 noites é padrão para o período entre os concorrentes que também venderam pacotes fechados. Em preço, a Villa está acima da média, o que é esperado num cenário de núcleo com esgotamentos.

**O valor total do pacote está defensável?**
Sim, com ressalva: o total Booking estimado da Villa (R$ 6.687,50) fica acima até dos concorrentes mais caros do núcleo (Kia Ora R$ 5.486,00, Dom Capudi R$ 4.988,00) — a defesa não vem de estar "dentro" do núcleo, vem de diferenciais reais (café da manhã na suíte, charme, piscina, churrasqueira) e do sinal de demanda alto.

**Existe risco de estar barato demais?**
Não. A Villa está acima da média em todas as leituras (mercado e motor equivalente).

**Existe risco de estar caro demais?**
Risco moderado, mas mitigado: a diferença é grande só frente aos dois concorrentes de padrão mais simples/promocional (Vila Maciel, Kaloa); frente a concorrentes de padrão mais próximo (Kia Ora, Dom Capudi) e frente à ampliada (UP), a diferença cai para 16,7–25,4%. Villa segue bem abaixo do teto de mercado.

**Existe sinal de demanda suficiente para proteger?**
Sim — esgotamento inédito de Vila Boa Vida e 43% do núcleo indisponível são sinais concretos de forte procura nesse período.

**Manter, proteger, subir, baixar, esperar ou comparar melhor?**
`PROTEGER` — não abrir espaço para desconto na tarifa já decidida.

**Algum concorrente está validando preço mais alto?**
Sim — Kia Ora (R$ 877,76 motor), Dom Capudi (R$ 798,08) e UP Hotel Boutique (R$ 891,04, ampliada) sustentam um patamar mais próximo da Villa; Atalaia (teto, R$ 2.320,00 motor) mostra que há espaço de mercado bem acima do preço atual da Villa.

**Algum concorrente está puxando a média para baixo de forma pouco comparável?**
Sim — Vila Maciel (motor equiv. R$ 404,96) é o principal responsável: produto de padrão mais simples (nota Booking 3/5), com desconto promocional ativo de 26% no momento da coleta, sinal de dificuldade de venda própria, não referência saudável de mercado.

---

## 7. Riscos e observações (leitura comercial)

- Comparação sempre "visível vs. visível, mesmo canal" (Booking) e "motor equivalente vs. motor", nunca cruzando as duas bases, conforme `REGRAS_CONVERSAO_OTA_MOTOR_REVENUE.md`.
- Como o diagnóstico é `PROTEGER` (não `BAIXAR_COM_JUSTIFICATIVA`), a leitura de `reserva-direta-reducao-otas.md` não é obrigatória para justificar a decisão, mas reforça o racional: mesmo com Vila Maciel e Kaloa mais baratos no Booking, a Villa compete por reserva direta, atendimento próximo e valor percebido — o gap frente a esses dois concorrentes de padrão inferior não deve, sozinho, pressionar redução na tarifa de Carnaval já decidida.
- Nenhum dado de Meta Ads específico para Carnaval 2027 foi verificado nesta rodada.

---

## Dados que faltam

- Ocupação real da Pousada Arágua para Carnaval 2027 — esta análise é 100% competitiva, sem dado de demanda própria da Villa.
- Confirmação no sistema Stays de que R$ 1.070,00/diária (Card 2) está de fato aplicado linha a linha no motor.
- `CESTA_COMPETITIVA_REVENUE_VILLA_ARAGUA.md` ainda não foi atualizada com observações específicas da Rodada 10 (só consta até a Rodada 4 na coluna de observações) — os dados desta rodada já existem no CSV.
- Vila dos Açores segue sem coleta/validação (`PENDENTE`).
- Nenhuma evidência disponível sobre campanha Meta Ads ativa especificamente para Carnaval 2027.

---

## Conclusão

Nenhuma decisão nova foi gerada por este relatório. Nenhuma tarifa foi alterada. Nenhum card foi movido ou modificado em `DECISOES_REVENUE_PENDENTES_VILLA_ARAGUA.md` — o Card 2 (Carnaval 2027, `DECIDIDO_APLICADO`) permanece exatamente como estava.

**Rodada 10 (Carnaval 2027, 05–10/02):** `PROTEGER`

**Status deste relatório:** `RELATORIO_ANALITICO_SEM_ALTERACAO_TARIFARIA`
