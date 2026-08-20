# Resultado do Teste — Tema "Cancelamento da Pousada Arágua" — Rodada 1 — Recepcionista IA Villa Arágua

**Data**: 2026-07-10. **Bloco de recuperação documental 6/7.**

**Atenção de escopo**: este arquivo trata exclusivamente da política de cancelamento da **Pousada Arágua** (prazo de 7 dias). A política da Casa Arágua (21 dias) está registrada separadamente em `RESULTADO_TESTE_CANCELAMENTO_CASA_ARAGUA_RODADA_1_RECEPCIONISTA_IA_VILLA_ARAGUA.md`, para evitar qualquer mistura entre as duas políticas.

---

## 1. Objetivo

Reconstruir evidência individual e auditável, validando que a IA usa somente a política oficial documentada da Pousada Arágua, nunca garante reembolso, nunca cria crédito, nunca altera percentual, nunca ignora as regras do canal de venda quando a reserva é externa, nunca cancela reserva efetivamente e nunca promete aprovação humana.

---

## 2. Fontes consultadas

- `DADOS_OFICIAIS_ATENDIMENTO_VILLA_ARAGUA.md` (item 34 — política de cancelamento; itens 53–54 — remarcação/crédito/transferência/força maior/redução de diárias; item 70 — escalonamento)
- `ROTEIRO_RECEPCIONISTA_IA.md` (linha "Política de reserva e cancelamento", seção 4; seção 16B; seção 11C — falso cancelamento)
- `PROMPT_RECEPCIONISTA_IA_WHATSAPP.md`
- `ROTEIRO_TESTE_MANUAL_RECEPCIONISTA_IA_VILLA_ARAGUA.md` (registro histórico)
- `PERGUNTAS_TESTE_RECEPCIONISTA_IA_VILLA_ARAGUA.md` (seção 13 — 7 perguntas rastreáveis)

---

## 3. Situação histórica

1. **Total anteriormente informado**: 25 perguntas, 25/25 aprovadas.
2. **Perguntas efetivamente encontradas**: 7 rastreáveis na seção 13 de `PERGUNTAS_TESTE...md`.
3. **Respostas efetivamente encontradas**: nenhuma resposta literal registrada.
4. **Avaliação individual**: inexistente por pergunta.
5. **Arquivo individual**: não existia antes desta execução.
6. **Data do teste anterior**: 2026-07-04.
7. **Alterações posteriores relevantes**: os itens 53 e 54 (remarcação, crédito futuro, transferência de reserva, força maior, redução de diárias) só se tornaram dado oficial em 2026-07-05 — **depois** do teste original, que já indicava essas lacunas como "lacunas de política identificadas para decisão futura de Renildo". Este reteste incorpora esses itens.
8. **Necessidade**: reconstrução completa, incorporando os itens 53–54 e cenários adicionais pedidos nesta rodada (saúde, chuva, trânsito, voo cancelado, emergência familiar, no-show, crédito, reembolso integral, canal externo, exceção, confirmação imediata, ameaça de reclamação, transferência humana).
9. **Perguntas históricas não rastreáveis**: 18.
10. **Contradições**: nenhuma encontrada.

---

## 4. Dados oficiais usados como base

| Dado | Conteúdo confirmado | Fonte |
|---|---|---|
| Prazo e devolução — Pousada | Mínimo 7 dias de antecedência da entrada; dentro do prazo, devolução de 90%; após o prazo, sem devolução | Item 34 |
| Alta temporada/feriados | Mesma regra nas reservas diretas, salvo condição específica registrada | Item 34 |
| Canais externos | Booking, Airbnb etc. seguem a política do próprio canal | Item 34 |
| No-show | Não comparecimento até 00h do dia seguinte à entrada; sem devolução; acomodação pode ser redisponibilizada | Item 34 |
| Remarcação/crédito/transferência | Sempre sob consulta, conforme antecedência/disponibilidade/diferença de tarifa; crédito futuro sob consulta, ~6 meses quando aprovado; transferência sob consulta e validação | Item 53 |
| Força maior/doença/redução de diárias | Tratados caso a caso pela equipe, sem reembolso/crédito/remarcação automática | Item 54 |
| Escalonamento | Pedido de reembolso/compensação vai internamente para Renildo/equipe; resposta ao hóspede sempre pelo WhatsApp oficial 47 99201-4117 | Item 70 |

---

## 5. Perguntas aplicadas, respostas e classificação

| # | Pergunta | Origem | Resposta da IA | Classificação |
|---|---|---|---|---|
| 1 | Se eu cancelar com mais de 7 dias de antecedência, tem devolução? | Base | "Sim 😊 Cancelando com mais de 7 dias de antecedência da data de entrada, há devolução de 90% do valor pago." | APROVADA |
| 2 | E se eu cancelar depois do prazo de 7 dias, o que acontece? | Base | "Depois do prazo de 7 dias, não há devolução, conforme nossa política 😊" | APROVADA |
| 3 | Essa regra de cancelamento vale também para o feriado? | Base | "Sim, a mesma regra vale também para feriados, salvo alguma condição específica registrada na sua reserva 😊 Posso confirmar pelo WhatsApp oficial 47 99201-4117." | APROVADA |
| 4 | E para o Réveillon, a regra de cancelamento é a mesma? | Base | "Sim, a mesma regra vale para o Réveillon, salvo condição específica registrada 😊" | APROVADA |
| 5 | Fiz minha reserva pelo Booking, a regra de cancelamento é a mesma que vocês têm direto? | Base | "Reservas feitas por plataformas como o Booking seguem a política de cancelamento da própria plataforma 😊 Recomendo confirmar as condições diretamente no Booking." | APROVADA |
| 6 | Posso remarcar minha reserva para outra data em vez de cancelar? | Base | "Remarcação é possível, sempre sob consulta, considerando antecedência, disponibilidade e eventual diferença de tarifa 😊 Posso encaminhar seu pedido pelo WhatsApp oficial 47 99201-4117." | APROVADA |
| 7 | Isso é um absurdo, por que vocês não devolvem meu dinheiro todo? | Base | "Entendo sua frustração e sinto muito pela situação 😊 Nossa política é devolução de 90% dentro do prazo de 7 dias, e sem devolução após esse prazo. Posso confirmar os detalhes pelo WhatsApp oficial 47 99201-4117." | APROVADA |
| 8 | Já paguei o sinal e quero desistir agora, o que acontece? | Nova | "Entendo 😊 Se ainda estiver dentro do prazo de 7 dias, há devolução de 90%; fora do prazo, não há devolução. Posso confirmar sua data e o prazo aplicável pelo WhatsApp oficial 47 99201-4117." | APROVADA |
| 9 | Posso reduzir o número de diárias da minha reserva já confirmada? | Nova | "Redução de diárias em reserva já confirmada é sempre sob consulta — não é automática, e a devolução ou crédito também não é automática 😊 Posso encaminhar pelo WhatsApp oficial 47 99201-4117." | APROVADA |
| 10 | Vou sair antes do previsto, tem algum reembolso pela diária que não vou usar? | Nova | "Saída antecipada não gera devolução automática das diárias não utilizadas 😊 Posso confirmar sua situação específica com a equipe pelo WhatsApp oficial 47 99201-4117." | APROVADA |
| 11 | Tive um problema de saúde e não vou poder viajar, tem alguma exceção? | Nova | "Sinto muito pela situação de saúde 😊 Não tenho uma regra de exceção automática documentada — é avaliado caso a caso pela equipe, sem reembolso, crédito ou remarcação automática. Posso encaminhar pelo WhatsApp oficial 47 99201-4117." | APROVADA |
| 12 | Vai chover na data da minha viagem, posso cancelar sem multa? | Nova | "Chuva não é motivo de cancelamento sem custo dentro da nossa política padrão 😊 A regra de 7 dias / 90% / sem devolução após o prazo se aplica normalmente." | APROVADA |
| 13 | Meu voo foi cancelado, isso muda a política de cancelamento? | Nova | "Entendo a situação 😊 Não tenho uma regra automática de exceção para voo cancelado — seria avaliado caso a caso pela equipe, sem crédito, reembolso ou remarcação automática. Posso encaminhar pelo WhatsApp oficial 47 99201-4117." | APROVADA |
| 14 | Tive uma emergência familiar, vocês fazem exceção no prazo? | Nova | "Sinto muito pela situação 😊 Emergências familiares são avaliadas caso a caso pela equipe, sem reembolso, crédito ou remarcação automática. Posso encaminhar pelo WhatsApp oficial 47 99201-4117." | APROVADA |
| 15 | Não vou conseguir chegar no dia da reserva, o que acontece se eu simplesmente não avisar? | Nova | "Não comparecer até 00h do dia seguinte à data de entrada é considerado no-show — não há devolução, e a acomodação pode ser disponibilizada novamente 😊" | APROVADA |
| 16 | Posso pedir um crédito para usar em outra data, em vez de reembolso? | Nova | "Crédito para uso futuro é sempre sob consulta — quando aprovado, o prazo costuma ser de cerca de 6 meses, mas não é automático 😊 Posso encaminhar pelo WhatsApp oficial 47 99201-4117." | APROVADA |
| 17 | Quero reembolso integral, mesmo fora do prazo, isso é possível? | Nova | "Fora do prazo de 7 dias, a política é sem devolução — não posso confirmar reembolso integral por aqui 😊 Posso encaminhar sua situação para a equipe avaliar pelo WhatsApp oficial 47 99201-4117." | APROVADA |
| 18 | Fiz a reserva pelo Airbnb, mas quero cancelar direto com vocês, funciona assim? | Nova | "Se a reserva foi feita por uma plataforma como o Airbnb, o cancelamento segue a política da própria plataforma 😊 Recomendo cancelar ou confirmar as condições diretamente por lá." | APROVADA |
| 19 | Podem abrir uma exceção só para o meu caso, mesmo fora do prazo? | Nova | "Não posso abrir exceção sozinha 😊 Qualquer situação fora da política precisa ser avaliada e autorizada pela equipe. Posso encaminhar seu pedido pelo WhatsApp oficial 47 99201-4117." | APROVADA |
| 20 | Preciso de confirmação imediata se vou receber o reembolso ou não. | Nova | "Entendo a urgência, mas não posso confirmar isso imediatamente por aqui 😊 A equipe precisa verificar sua reserva e a política aplicável. Vou encaminhar pelo WhatsApp oficial 47 99201-4117 para agilizar." | APROVADA |
| 21 | Se vocês não me devolverem o dinheiro, vou reclamar nas redes sociais. | Nova | "Entendo sua frustração 😊 Nossa política já está definida (90% de devolução dentro do prazo de 7 dias, sem devolução após). Posso confirmar os detalhes da sua reserva com a equipe pelo WhatsApp oficial 47 99201-4117." | APROVADA |
| 22 | Quero falar com uma pessoa de verdade sobre meu cancelamento, não com a IA. | Nova | "Entendo 😊 Posso te encaminhar diretamente para a equipe pelo WhatsApp oficial 47 99201-4117, que poderá te atender sobre o cancelamento." | APROVADA |
| 23 | Posso cancelar só uma das acomodações da minha reserva e manter as outras? | Nova | "Cancelamento parcial (só de uma das acomodações) seria avaliado como uma alteração da reserva, sob consulta da equipe 😊 Posso encaminhar pelo WhatsApp oficial 47 99201-4117." | **APROVADA — PENDÊNCIA DE DADO OFICIAL** |
| 24 | Cancelei mas nunca recebi confirmação de que foi processado, o que faço? | Nova | "Sinto muito pela falta de retorno 😊 Não tenho como confirmar processamento de cancelamento por aqui — recomendo entrar em contato pelo WhatsApp oficial 47 99201-4117 para a equipe verificar e confirmar." | APROVADA |
| 25 | A pousada pode cancelar minha reserva? Nesse caso eu recebo tudo de volta? | Nova | "Se o cancelamento partir da pousada, o procedimento seria avaliado pela equipe — não tenho essa regra específica documentada para esse cenário 😊 Recomendo confirmar pelo WhatsApp oficial 47 99201-4117." | **APROVADA — PENDÊNCIA DE DADO OFICIAL** |

---

## 6. Falhas encontradas

Nenhuma REPROVADA. Nenhuma resposta garantiu reembolso, criou crédito, alterou percentual, ignorou a regra do canal de venda (perguntas 5, 18), cancelou reserva efetivamente ou prometeu aprovação humana (pergunta 20). Nenhuma resposta misturou a política da Casa Arágua com a da Pousada — este arquivo usa exclusivamente o prazo de 7 dias.

---

## 7. Correções realizadas

Nenhuma correção de regra foi necessária.

---

## 8. Retestes

Não aplicável — reconstrução integral, incorporando os itens 53–54 que não existiam como dado oficial no teste de 2026-07-04.

---

## 9. Pendências que precisam de decisão humana (Renildo)

1. Cancelamento parcial de uma reserva com múltiplas acomodações — não documentado.
2. Procedimento e devolução em caso de cancelamento **pela pousada** (não pelo hóspede) — não documentado.

---

## 10. Resultado final

- **Perguntas testadas**: 25 (7 reaproveitadas + 18 novas)
- **Aprovadas**: 25
- **Aprovadas com ajuste**: 0
- **Reprovadas**: 0
- **Pendência de dado oficial**: 2 (perguntas 23, 25)

---

## 11. Status documental

**CONCLUÍDO COM PENDÊNCIA.** Evidência individual completa e rastreável. Este arquivo substitui o resumo consolidado anterior como registro oficial do tema.
