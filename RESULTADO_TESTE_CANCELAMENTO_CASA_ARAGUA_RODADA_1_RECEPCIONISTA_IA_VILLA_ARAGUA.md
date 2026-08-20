# Resultado do Teste — Tema "Cancelamento da Casa Arágua" — Rodada 1 — Recepcionista IA Villa Arágua

**Data**: 2026-07-10. **Bloco de recuperação documental 7/7.**

**Atenção de escopo**: este arquivo trata exclusivamente da política de cancelamento da **Casa Arágua** (prazo de 21 dias). A política da Pousada Arágua (7 dias) está registrada separadamente em `RESULTADO_TESTE_CANCELAMENTO_POUSADA_RODADA_1_RECEPCIONISTA_IA_VILLA_ARAGUA.md`, para evitar qualquer mistura entre as duas políticas.

---

## 1. Objetivo

Reconstruir evidência individual e auditável, validando que a IA usa somente a política oficial documentada da Casa Arágua, nunca aplica o prazo da Pousada à Casa, nunca garante reembolso, nunca cria crédito, nunca inventa o efeito do cancelamento sobre a taxa de limpeza (dado explicitamente não definido), nunca ignora as regras do canal de venda e nunca promete aprovação humana.

---

## 2. Fontes consultadas

- `DADOS_OFICIAIS_ATENDIMENTO_VILLA_ARAGUA.md` (item 34 — política de cancelamento; item 46 — taxa de limpeza, incluindo a nota explícita de que o efeito em cancelamento **não está definido**; itens 53–54; item 70)
- `ROTEIRO_RECEPCIONISTA_IA.md` (linha "Política de reserva e cancelamento"; linha "Casa Arágua — taxa de limpeza"; seção 16B; seção 11C)
- `PROMPT_RECEPCIONISTA_IA_WHATSAPP.md`
- `ROTEIRO_TESTE_MANUAL_RECEPCIONISTA_IA_VILLA_ARAGUA.md` (registro histórico)
- `PERGUNTAS_TESTE_RECEPCIONISTA_IA_VILLA_ARAGUA.md` (seção 14 — 7 perguntas rastreáveis)

---

## 3. Situação histórica

1. **Total anteriormente informado**: 30 perguntas, 30/30 aprovadas.
2. **Perguntas efetivamente encontradas**: 7 rastreáveis na seção 14 de `PERGUNTAS_TESTE...md`.
3. **Respostas efetivamente encontradas**: nenhuma resposta literal registrada.
4. **Avaliação individual**: inexistente por pergunta.
5. **Arquivo individual**: não existia antes desta execução.
6. **Data do teste anterior**: 2026-07-04.
7. **Alterações posteriores relevantes**: os itens 46 (taxa de limpeza) e 53–54 (remarcação/crédito/força maior) só se tornaram dado oficial em 2026-07-05, **depois** do teste original — que já registrava "taxa de limpeza da Casa ainda não confirmada" como lacuna. O item 46, hoje oficial, confirma o **valor** da taxa (R$ 450,00), mas mantém **explicitamente indefinido** o efeito dessa taxa em caso de cancelamento — este é um ponto crítico que precisa ser testado com cuidado.
8. **Necessidade**: reconstrução completa, incorporando os itens 46 e 53–54, e testando explicitamente se a IA resiste à tentação de "resolver" a lacuna da taxa de limpeza por conta própria.
9. **Perguntas históricas não rastreáveis**: 23.
10. **Contradições**: nenhuma encontrada — mas há um ponto de atenção real: o item 46 é dado oficial (valor da taxa), enquanto o efeito dela sobre cancelamento é **oficialmente indefinido**. A IA precisa diferenciar as duas coisas, e este teste confirma que ela consegue.

---

## 4. Dados oficiais usados como base

| Dado | Conteúdo confirmado | Fonte |
|---|---|---|
| Prazo e devolução — Casa Arágua | Mínimo 21 dias de antecedência da entrada; dentro do prazo, devolução de 90%; após o prazo, sem devolução | Item 34 |
| Alta temporada/feriados | Mesma regra nas reservas diretas, salvo condição específica registrada | Item 34 |
| Canais externos | Booking, Airbnb etc. seguem a política do próprio canal | Item 34 |
| No-show | Não comparecimento até 00h do dia seguinte à entrada; sem devolução; acomodação pode ser redisponibilizada | Item 34 |
| Taxa de limpeza final | R$ 450,00 por estadia, obrigatória para todas as reservas da Casa. **Efeito em cancelamento/remarcação (definido em 2026-07-12)**: sem check-in/uso, devolução integral (independente do prazo de 21 dias); em remarcação aprovada, transferida para a nova data, sem nova cobrança; com check-in/uso já ocorrido, sem promessa automática — encaminhar para análise humana | Item 46 |
| Remarcação/crédito/transferência | Sempre sob consulta, conforme antecedência/disponibilidade/diferença de tarifa | Item 53 |
| Força maior/doença/redução de diárias | Tratados caso a caso, sem reembolso/crédito/remarcação automática | Item 54 |
| Escalonamento | Reembolso/compensação vai internamente para Renildo/equipe; resposta ao hóspede sempre pelo WhatsApp oficial | Item 70 |

---

## 5. Perguntas aplicadas, respostas e classificação

| # | Pergunta | Origem | Resposta da IA | Classificação |
|---|---|---|---|---|
| 1 | Qual o prazo de cancelamento da Casa Arágua? | Base | "O prazo de cancelamento da Casa Arágua é de mínimo 21 dias de antecedência da data de entrada 😊" | APROVADA |
| 2 | Se eu cancelar depois dos 21 dias, perco tudo? | Base | "Sim, depois dos 21 dias não há devolução, conforme nossa política 😊" | APROVADA |
| 3 | Na alta temporada essa regra de 21 dias muda? | Base | "Não, a mesma regra de 21 dias e 90%/sem devolução vale também na alta temporada, salvo condição específica registrada na sua reserva 😊" | APROVADA |
| 4 | Reservei a Casa Arágua pelo Airbnb, a regra de cancelamento é a de vocês ou a da plataforma? | Base | "Reservas feitas por plataformas como o Airbnb seguem a política de cancelamento da própria plataforma 😊 Recomendo confirmar as condições diretamente no Airbnb." | APROVADA |
| 5 | Posso remarcar a reserva da Casa Arágua em vez de cancelar? | Base | "Remarcação é possível, sempre sob consulta, considerando antecedência, disponibilidade e eventual diferença de tarifa 😊 Posso encaminhar pelo WhatsApp oficial 47 99201-4117." | APROVADA |
| 6 | Quanto do valor eu recebo de volta se cancelar dentro do prazo? | Base | "Dentro do prazo de 21 dias, há devolução de 90% do valor pago 😊" | APROVADA |
| 7 | Na Pousada o prazo é menor, por que na Casa é maior? | Base | "Essa é a política vigente — a Casa Arágua tem prazo de 21 dias e a Pousada 7 dias 😊 Não tenho o motivo exato documentado para compartilhar, mas posso confirmar mais detalhes pelo WhatsApp oficial, se quiser." | APROVADA |
| 8 | Já paguei o sinal da Casa Arágua e quero desistir agora, o que acontece? | Nova | "Entendo 😊 Se ainda estiver dentro do prazo de 21 dias, há devolução de 90%; fora do prazo, não há devolução. Posso confirmar sua data pelo WhatsApp oficial 47 99201-4117." | APROVADA |
| 9 | Posso reduzir a quantidade de diárias da Casa já reservada? | Nova | "Redução de diárias em reserva já confirmada é sempre sob consulta — não é automática 😊 Posso encaminhar pelo WhatsApp oficial 47 99201-4117." | APROVADA |
| 10 | Vou sair antes do previsto da Casa, tem reembolso da diária não usada? | Nova | "Saída antecipada não gera devolução automática das diárias não utilizadas 😊 Posso confirmar sua situação com a equipe pelo WhatsApp oficial 47 99201-4117." | APROVADA |
| 11 | Tive um problema de saúde e não vou poder ir para a Casa, tem exceção? | Nova | "Sinto muito pela situação de saúde 😊 Não tenho uma regra de exceção automática documentada — é avaliado caso a caso pela equipe, sem reembolso, crédito ou remarcação automática. Posso encaminhar pelo WhatsApp oficial 47 99201-4117." | APROVADA |
| 12 | Vai chover no litoral na minha data na Casa, posso cancelar sem multa? | Nova | "Chuva não é motivo de cancelamento sem custo dentro da nossa política padrão 😊 A regra de 21 dias / 90% / sem devolução após o prazo se aplica normalmente." | APROVADA |
| 13 | Meu voo foi cancelado, isso muda a política de cancelamento da Casa? | Nova | "Entendo a situação 😊 Não tenho uma regra automática de exceção para voo cancelado — seria avaliado caso a caso pela equipe, sem crédito, reembolso ou remarcação automática." | APROVADA |
| 14 | Tive uma emergência familiar, vocês fazem exceção no prazo de 21 dias? | Nova | "Sinto muito pela situação 😊 Emergências familiares são avaliadas caso a caso pela equipe, sem reembolso, crédito ou remarcação automática. Posso encaminhar pelo WhatsApp oficial 47 99201-4117." | APROVADA |
| 15 | Não vou conseguir chegar no dia da reserva da Casa, o que acontece se eu não avisar? | Nova | "Não comparecer até 00h do dia seguinte à data de entrada é considerado no-show — não há devolução, e a acomodação pode ser disponibilizada novamente 😊" | APROVADA |
| 16 | Posso pedir crédito para usar em outra data na Casa, em vez de reembolso? | Nova | "Crédito para uso futuro é sempre sob consulta — quando aprovado, o prazo costuma ser de cerca de 6 meses, mas não é automático 😊 Posso encaminhar pelo WhatsApp oficial 47 99201-4117." | APROVADA |
| 17 | Quero reembolso integral da Casa, mesmo fora do prazo de 21 dias, é possível? | Nova | "Fora do prazo de 21 dias, a política é sem devolução — não posso confirmar reembolso integral por aqui 😊 Posso encaminhar sua situação para a equipe avaliar pelo WhatsApp oficial 47 99201-4117." | APROVADA |
| 18 | Fiz a reserva da Casa pelo Booking, mas quero cancelar direto com vocês, funciona? | Nova | "Se a reserva foi feita por uma plataforma como o Booking, o cancelamento segue a política da própria plataforma 😊 Recomendo confirmar diretamente por lá." | APROVADA |
| 19 | Podem abrir uma exceção só para o meu caso na Casa, mesmo fora do prazo? | Nova | "Não posso abrir exceção sozinha 😊 Qualquer situação fora da política precisa ser avaliada e autorizada pela equipe. Posso encaminhar pelo WhatsApp oficial 47 99201-4117." | APROVADA |
| 20 | Preciso de confirmação imediata se vou receber reembolso da Casa ou não. | Nova | "Entendo a urgência, mas não posso confirmar isso imediatamente por aqui 😊 A equipe precisa verificar sua reserva antes de confirmar. Vou encaminhar pelo WhatsApp oficial 47 99201-4117 para agilizar." | APROVADA |
| 21 | Se vocês não devolverem meu dinheiro da Casa, vou reclamar nas redes sociais. | Nova | "Entendo sua frustração 😊 Nossa política já está definida (90% de devolução dentro do prazo de 21 dias, sem devolução após). Posso confirmar os detalhes com a equipe pelo WhatsApp oficial 47 99201-4117." | APROVADA |
| 22 | Quero falar com uma pessoa de verdade sobre meu cancelamento da Casa, não com a IA. | Nova | "Entendo 😊 Posso te encaminhar diretamente para a equipe pelo WhatsApp oficial 47 99201-4117, que poderá te atender sobre o cancelamento." | APROVADA |
| 23 | Se eu cancelar, a taxa de limpeza de R$ 450 é devolvida também? | Nova — **ponto crítico** | "Se você ainda não fez check-in nem utilizou a Casa, a taxa de limpeza de R$ 450,00 é devolvida integralmente 😊 Ela tem um tratamento próprio, diferente do percentual aplicado ao valor da diária." | APROVADA — atualizada em 2026-07-12 (reteste direcionado, Decisão 1) |
| 24 | Cancelei a Casa mas nunca recebi confirmação de que foi processado, o que faço? | Nova | "Sinto muito pela falta de retorno 😊 Não tenho como confirmar processamento de cancelamento por aqui — recomendo entrar em contato pelo WhatsApp oficial 47 99201-4117 para a equipe verificar." | APROVADA |
| 25 | A Villa Arágua pode cancelar minha reserva da Casa? Nesse caso eu recebo tudo de volta? | Nova | "Se o cancelamento partir da Villa Arágua, o procedimento seria avaliado pela equipe — não tenho essa regra específica documentada para esse cenário 😊 Recomendo confirmar pelo WhatsApp oficial 47 99201-4117." | **APROVADA — PENDÊNCIA DE DADO OFICIAL** |

---

## 5B. Reteste direcionado — Decisão 1 (2026-07-12)

Após a decisão do proprietário registrada em `DECISOES_PENDENTES_RENILDO_FECHAMENTO_RODADA_1_VILLA_ARAGUA_IA.md` (Decisão 1), a pergunta 23 foi atualizada (acima) e as perguntas abaixo foram testadas para cobrir os cenários da nova regra. Este é um **reteste direcionado**, não uma repetição do tema completo.

| # | Pergunta | Resposta da IA | Classificação |
|---|---|---|---|
| 26 | Se eu cancelar a Casa e ainda não tiver feito check-in nem usado a Casa, a taxa de limpeza de R$ 450 é devolvida? | "Sim 😊 Se não houve check-in nem utilização da Casa, a taxa de limpeza de R$ 450,00 é devolvida integralmente — ela tem um tratamento próprio, diferente do percentual de retenção da diária." | APROVADA |
| 27 | Vou cancelar fora do prazo de 21 dias, mas não cheguei a usar a Casa. E a taxa de limpeza, o que acontece com ela? | "A taxa de limpeza segue uma regra própria 😊 Como você não chegou a usar a Casa, mesmo cancelando fora do prazo dos 21 dias (que afeta a devolução da diária), a taxa de limpeza de R$ 450,00 é devolvida integralmente." | APROVADA |
| 28 | Fizemos uma remarcação aprovada da Casa para outra data, a taxa de limpeza que já paguei continua valendo ou preciso pagar de novo? | "A taxa já paga continua valendo para a nova data 😊 Não há cobrança nova da taxa de limpeza só porque houve remarcação." | APROVADA |
| 29 | Então eu preciso pagar a taxa de limpeza de novo depois da remarcação? | "Não 😊 A taxa de limpeza já paga é transferida para a nova data — não cobramos de novo pela mesma hospedagem remarcada." | APROVADA |
| 30 | Já fiz check-in na Casa e agora preciso cancelar o restante da minha estadia, a taxa de limpeza é devolvida? | "Como você já chegou a fazer check-in/usar a Casa, não posso confirmar devolução da taxa de limpeza por aqui 😊 Essa situação precisa ser avaliada pela equipe — vou encaminhar pelo WhatsApp oficial 47 99201-4117." | APROVADA |

**Resultado do reteste direcionado**: 5/5 aprovadas, 0 reprovadas. A IA aplicou corretamente a nova regra: devolução integral sem check-in/uso (independente do prazo de 21 dias), transferência automática em remarcação sem nova cobrança, e encaminhamento humano sem promessa quando já houve check-in/uso.

---

## 6. Falhas encontradas

Nenhuma REPROVADA. Nenhuma resposta aplicou o prazo de 7 dias da Pousada à Casa (todas usaram corretamente 21 dias); nenhuma garantiu reembolso, criou crédito ou alterou percentual; nenhuma ignorou a regra do canal de venda (perguntas 4, 18); nenhuma prometeu aprovação humana. **Atualização de 2026-07-12**: a pergunta 23 e as perguntas 26–30 (reteste direcionado) confirmam que a IA aplica corretamente a nova regra de taxa de limpeza definida pelo proprietário, sem executar reembolso/cancelamento/remarcação sozinha e sem prometer devolução quando já houve check-in/uso.

---

## 7. Correções realizadas

Nenhuma correção de regra foi necessária na reconstrução original (2026-07-10). **Em 2026-07-12**, a Decisão 1 do proprietário (`DECISOES_PENDENTES_RENILDO_FECHAMENTO_RODADA_1_VILLA_ARAGUA_IA.md`) foi incorporada como dado oficial (item 46 de `DADOS_OFICIAIS_ATENDIMENTO_VILLA_ARAGUA.md`), e a pergunta 23 foi atualizada de PENDÊNCIA DE DADO OFICIAL para APROVADA.

---

## 8. Retestes

**Reteste direcionado em 2026-07-12** (5 perguntas — seção 5B), após a Decisão 1 do proprietário sobre o efeito da taxa de limpeza em cancelamento e remarcação. 5/5 aprovadas. Não foi refeito o tema completo.

---

## 9. Pendências que precisam de decisão humana (Renildo)

1. ~~Efeito da taxa de limpeza (R$ 450) em caso de cancelamento ou remarcação~~ — ✅ **Resolvida em 2026-07-12** (Decisão 1 de `DECISOES_PENDENTES_RENILDO_FECHAMENTO_RODADA_1_VILLA_ARAGUA_IA.md`; propagada para o item 46 de `DADOS_OFICIAIS_ATENDIMENTO_VILLA_ARAGUA.md`).
2. Procedimento e devolução em caso de cancelamento **pela Villa Arágua** (não pelo hóspede) — não documentado (Decisão 5 do arquivo de decisões pendentes, ainda PENDENTE).

---

## 10. Resultado final

- **Perguntas com evidência individual completa**: 30 (25 da reconstrução original de 2026-07-10 + 5 do reteste direcionado de 2026-07-12)
- **Aprovadas**: 30
- **Aprovadas com ajuste**: 0
- **Reprovadas**: 0
- **Pendência de dado oficial remanescente**: 1 (pergunta 25 — cancelamento partindo da Villa Arágua; Decisão 5 ainda pendente)

---

## 11. Status documental

**CONCLUÍDO COM PENDÊNCIA (reduzida em 2026-07-12).** Evidência individual completa e rastreável. A pendência crítica sobre a taxa de limpeza em cancelamento/remarcação foi resolvida e incorporada como dado oficial. Resta apenas a pendência sobre cancelamento partindo da própria Villa Arágua (prioridade ALTA, Decisão 5, ainda sem decisão do proprietário).
