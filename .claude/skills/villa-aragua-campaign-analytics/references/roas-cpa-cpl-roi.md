# ROAS, CPA, CPL e ROI

Fórmulas simples para calcular retorno — sempre com os dados que o usuário fornecer, nunca com número estimado sem avisar que é estimativa.

## Fórmulas

- **CPL (custo por lead)** = investimento ÷ número de leads.
- **Custo por conversa** = investimento ÷ conversas iniciadas no WhatsApp (diferente de CPL quando nem todo lead vira conversa real — ver `metricas-meta-ads.md`).
- **CPA (custo por aquisição/reserva)** = investimento ÷ reservas confirmadas (nunca ÷ pré-reservas ou orçamentos enviados).
- **ROAS (retorno sobre investimento em mídia)** = receita atribuída à campanha ÷ investimento em mídia.
- **ROI (retorno sobre investimento total)** = lucro estimado ÷ investimento total (mídia + custos operacionais atribuíveis, quando disponíveis).

## Por que CPL, custo por conversa e CPA nunca são a mesma coisa

Nem todo lead vira conversa (alguém pode clicar e nunca escrever de fato); nem toda conversa vira reserva. Calcular os três separadamente é o que permite identificar em qual etapa o dinheiro está "vazando" (ver `funil-whatsapp-reserva.md`). Reportar só o CPA final e esconder o CPL/custo por conversa impede enxergar se o problema é atrair gente (CPL alto) ou converter quem já chegou (CPA alto com CPL/custo por conversa normal).

## As cinco camadas de retorno — nunca misturar

| Camada | O que é | Cuidado |
|---|---|---|
| **Receita reservada** | Valor total combinado nas reservas confirmadas no período (diária × diárias, taxas quando aplicável) | Não é dinheiro que já entrou no caixa — é o valor "fechado" |
| **Receita recebida** | Valor que já entrou de fato (entrada paga, saldo pago) | Pode ser bem menor que a receita reservada se a estadia ainda não aconteceu ou o saldo ainda não foi pago |
| **ROAS bruto** | Receita reservada (ou recebida, deixar explícito qual) ÷ investimento em mídia | Não desconta nenhum custo operacional — mede só o retorno de mídia sobre a receita gerada |
| **ROI com custos operacionais** | Lucro estimado ÷ investimento total | Precisa descontar custo variável da estadia (limpeza, café, lavanderia — ver `villa-aragua-pricing-revenue/references/ponto-equilibrio-abertura.md`) além do investimento em mídia |
| **Lucro estimado** | Receita recebida (ou reservada, com ressalva) menos custos atribuíveis (mídia + operação variável) | É sempre "estimado" enquanto os ledgers de `FINANCEIRO/` não estiverem categorizados por caixa — nunca chamar de "lucro real" sem essa categorização feita |

**Regra de ouro**: sempre declarar qual das cinco camadas está sendo mostrada. "ROAS de 5x" sem dizer se é sobre receita reservada ou recebida, bruto ou líquido, é uma afirmação incompleta e pode enganar a decisão.

## Exemplo de cálculo (com números fictícios só para ilustrar o método — nunca usar estes números como se fossem reais da Villa Arágua)

Suponha, apenas como exercício didático: investimento de R$ 315,00 numa semana, 20 leads, 14 conversas iniciadas, 3 reservas confirmadas somando R$ 3.500,00 de receita reservada, das quais R$ 1.200,00 já recebidos como entrada.

- CPL = 315 ÷ 20 = R$ 15,75 por lead.
- Custo por conversa = 315 ÷ 14 = R$ 22,50 por conversa.
- CPA = 315 ÷ 3 = R$ 105,00 por reserva.
- ROAS bruto (sobre receita reservada) = 3.500 ÷ 315 ≈ 11,1x.
- ROAS sobre receita recebida = 1.200 ÷ 315 ≈ 3,8x (número bem mais conservador — e o mais honesto enquanto o restante da receita não entrou).
- ROI: exigiria somar custo variável das 3 estadias (limpeza, café, lavanderia) ao investimento de R$ 315,00 antes de dividir o lucro estimado — sem esse dado, reportar "ROI ainda não calculável com os dados disponíveis", nunca estimar um custo operacional que não foi informado.

## Como não confundir margem com receita

Receita alta não significa margem alta — ver `villa-aragua-pricing-revenue` para custo variável por diária (café, limpeza, lavanderia) e ponto de equilíbrio. Um ROAS bruto de 10x pode virar um ROI baixo se o custo operacional da estadia for alto proporcionalmente à diária — por isso ROI sempre exige o dado de custo, que nem sempre está disponível (ver pendência de categorização de `FINANCEIRO/`).

## O que fazer quando faltar dado para uma das fórmulas

- Nunca completar a lacuna com um número "razoável" ou "de mercado" — isso deixa de ser análise da Villa Arágua e vira invenção.
- Reportar explicitamente qual fórmula não pôde ser calculada e por quê (ex.: "ROI não calculado — falta custo operacional por estadia, ainda não categorizado em `FINANCEIRO/`").
- Sugerir o dado mínimo que resolveria a lacuna (ver `checklist-dados-campanha.md`).

## Como usar este arquivo na prática

1. Confirmar quais dados de investimento, leads, conversas e reservas estão disponíveis (ver `checklist-dados-campanha.md`).
2. Calcular CPL, custo por conversa e CPA separadamente.
3. Calcular ROAS deixando claro se é sobre receita reservada ou recebida.
4. Só calcular ROI se houver dado de custo operacional atribuível — caso contrário, sinalizar a lacuna.
5. Nunca comparar ROAS/CPA entre Pousada e Casa Arágua sem lembrar que os produtos têm ticket médio e custo variável diferentes — a comparação precisa considerar isso, não só o número final.
