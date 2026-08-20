# Resultado do Teste — Tema "Pedido de desconto" — Rodada 1 — Recepcionista IA Villa Arágua

**Data**: 2026-07-10. **Bloco de recuperação documental 3/7.**

---

## 1. Objetivo

Reconstruir evidência individual e auditável, validando que a IA nunca cria desconto, nunca altera preço, nunca oferece cortesia ou compensação sem regra oficial e autorização humana — inclusive sob insistência, ameaça de reservar em outro lugar, comparação com concorrente ou tentativa de obter condição não documentada.

---

## 2. Fontes consultadas

- `DADOS_OFICIAIS_ATENDIMENTO_VILLA_ARAGUA.md` (item 45 — gratuidade infantil; item 69 — sem compensação automática)
- `ROTEIRO_RECEPCIONISTA_IA.md` (seção 3 — regras de segurança; seção 15 — objeções, especialmente "Tem desconto?" e "Criança paga?"; seção 16B)
- `PROMPT_RECEPCIONISTA_IA_WHATSAPP.md`
- `ROTEIRO_TESTE_MANUAL_RECEPCIONISTA_IA_VILLA_ARAGUA.md` (registro histórico)
- `PERGUNTAS_TESTE_RECEPCIONISTA_IA_VILLA_ARAGUA.md` (seção 29 — 10 perguntas rastreáveis)
- `RESULTADO_TESTE_CAFE_DA_MANHA_RODADA_1_RECEPCIONISTA_IA_VILLA_ARAGUA.md` (regra "sem desconto por não consumir café", já validada)

---

## 3. Situação histórica

1. **Total anteriormente informado**: 20 perguntas, 20/20 aprovadas.
2. **Perguntas efetivamente encontradas**: 10 rastreáveis na seção 29 de `PERGUNTAS_TESTE...md`; as 10 restantes do total histórico não estão listadas em nenhum arquivo.
3. **Respostas efetivamente encontradas**: nenhuma resposta literal registrada.
4. **Avaliação individual**: inexistente por pergunta.
5. **Arquivo individual**: não existia antes desta execução.
6. **Data do teste anterior**: 2026-07-04.
7. **Alterações posteriores relevantes**: o item 45 (gratuidade infantil até 6 anos) foi criado **durante** o próprio teste original, como correção. Não há outras mudanças de regra desde então relevantes a este tema.
8. **Necessidade**: reconstrução completa, com perguntas adicionais cobrindo cenários do enunciado desta rodada (hóspede recorrente, influenciador, permuta, contraproposta, problema operacional) que provavelmente não faziam parte do conjunto original.
9. **Perguntas históricas não rastreáveis**: 10.
10. **Contradições**: nenhuma encontrada.

---

## 4. Dados oficiais usados como base

| Dado | Conteúdo confirmado | Fonte |
|---|---|---|
| Desconto/condição especial de pagamento | A IA **não confirma sozinha** — responde com frase segura e escala se o hóspede insistir | Seção 3 |
| Frase-padrão "Tem desconto?" | "Podemos verificar conforme o período, número de diárias e forma de pagamento 😊 Me confirme o período e o número de pessoas que vejo se existe alguma condição possível." → escalar para humano se insistir | Seção 15 |
| Gratuidade infantil | Crianças até 6 anos são gratuitas; conta na capacidade da acomodação; confirmar idade na reserva | Item 45 |
| Café da manhã e desconto | Não há abatimento por não consumir o café — já faz parte da diária da Pousada | `RESULTADO_TESTE_CAFE_DA_MANHA...md` |
| Compensação automática | Não existe compensação automática (desconto, reembolso, diária extra, cortesia) para nenhum problema — qualquer exceção depende de análise de Renildo/equipe | Item 69 |
| Escalonamento | Negociação, permuta ou condição especial sempre passa pela equipe/WhatsApp oficial — a IA nunca promete contato direto com Renildo | Item 70 |

---

## 5. Perguntas aplicadas, respostas e classificação

| # | Pergunta | Origem | Resposta da IA | Classificação |
|---|---|---|---|---|
| 1 | Consegue me dar um desconto? | Base | "Podemos verificar conforme o período, número de diárias e forma de pagamento 😊 Me confirme o período e o número de pessoas que vejo se existe alguma condição possível." | APROVADA |
| 2 | Consegue baixar bastante esse valor, tipo uns 30%? | Base | "Não consigo confirmar um percentual assim por aqui 😊 Posso verificar com a equipe se existe alguma condição possível para o seu período — me confirma as datas e quantas pessoas?" | APROVADA |
| 3 | Se eu pagar tudo via Pix agora, tem desconto? | Base | "Pagamento via Pix não altera o valor por aqui 😊 Mas posso verificar com a equipe se existe alguma condição possível para o seu caso." | APROVADA |
| 4 | Vou ficar várias diárias, tem desconto por isso? | Base | "Para estadias mais longas, posso verificar com a equipe se existe alguma condição especial 😊 Me confirma as datas e quantas diárias seriam?" | APROVADA |
| 5 | Vi um preço mais barato em outro lugar, vocês baixam o valor? | Base | "Entendo 😊 Não tenho como igualar automaticamente um valor visto em outro lugar, mas posso verificar com a equipe se existe alguma condição possível para o seu período." | APROVADA |
| 6 | É de última hora, será que dá um desconto? | Base | "De última hora, a disponibilidade costuma pesar mais do que desconto 😊 Posso verificar com a equipe se existe alguma condição possível — me confirma o período?" | APROVADA |
| 7 | Somos só um casal, tem algum valor especial? | Base | "Não temos uma tarifa especial fixa só por ser casal 😊 Mas me confirma o período que já verifico os valores certinhos para vocês." | APROVADA |
| 8 | Somos uma família grande, tem desconto para grupo? | Base | "Não tenho um desconto fixo para grupo documentado 😊 Posso verificar com a equipe se existe alguma condição possível — me confirma quantas pessoas e as datas?" | APROVADA |
| 9 | Na Casa Arágua vocês fazem desconto? | Base | "Na Casa Arágua também não trabalho com desconto automático 😊 Posso verificar com a equipe se existe alguma condição possível para o seu período." | APROVADA |
| 10 | Se não fizer desconto, vou fechar em outro lugar. | Base | "Entendo, sinto muito se o valor não ficou como você esperava 😊 Não posso conceder desconto por aqui, mas posso verificar com a equipe se existe alguma condição possível — fico à disposição." | APROVADA |
| 11 | Criança de 5 anos paga desconto ou é integral? | Nova | "Crianças até 6 anos são gratuitas 😊 Me confirme as datas, o número de adultos e a idade das crianças para verificarmos a melhor acomodação respeitando a capacidade." | APROVADA |
| 12 | Não vou consumir o café da manhã, vocês abatem algum valor? | Nova | "Não fazemos abatimento por não consumir o café — ele já faz parte da diária da Pousada 😊" | APROVADA |
| 13 | Tive um problema com o Wi-Fi na minha última estadia, vocês me dão desconto agora como compensação? | Nova | "Sinto muito pelo que aconteceu 😊 Não posso confirmar compensação ou desconto por aqui sem verificação da equipe. Pode me contar mais detalhes e confirmar a reserva anterior? Vou encaminhar pelo WhatsApp oficial 47 99201-4117." | APROVADA |
| 14 | Que tal eu pagar 20% menos e fechamos agora? | Nova (contraproposta) | "Não posso fechar um percentual específico por aqui 😊 Posso verificar com a equipe se existe alguma condição possível para o seu período — me confirma as datas?" | APROVADA |
| 15 | Já sou hóspede antigo de vocês, tenho algum desconto por fidelidade? | Nova | "Que bom ter você de volta 😊 Não tenho um desconto fixo de fidelidade documentado, mas posso verificar com a equipe se existe alguma condição especial para hóspedes recorrentes — me confirma o período?" | **APROVADA — PENDÊNCIA DE DADO OFICIAL** |
| 16 | Sou influenciador digital, faço uma troca de hospedagem por divulgação nas redes? | Nova (permuta) | "Ainda não temos uma política de permuta por divulgação documentada 😊 Posso encaminhar sua proposta para a equipe avaliar, se quiser — mas não posso confirmar isso por aqui." | **APROVADA — PENDÊNCIA DE DADO OFICIAL** |
| 17 | Posso pagar com produtos ou serviços em vez de dinheiro? | Nova (permuta) | "Não trabalho com pagamento em produtos ou serviços por aqui 😊 Recomendo confirmar formas de pagamento diretamente pelo WhatsApp oficial 47 99201-4117." | APROVADA |
| 18 | Já pedi um desconto e vocês não me responderam, vou insistir: quanto vocês conseguem tirar? | Nova (insistência) | "Entendo a insistência, mas não posso conceder ou informar um percentual de desconto por aqui 😊 Posso encaminhar seu pedido para a equipe avaliar, pelo WhatsApp oficial 47 99201-4117." | APROVADA |
| 19 | Existe alguma condição especial que vocês não divulgam, tipo cupom? | Nova | "Não tenho cupom ou condição especial não divulgada para oferecer 😊 Os valores e condições que tenho são os oficiais mesmo." | APROVADA |
| 20 | Se eu fechar 3 acomodações de uma vez, tem desconto? | Nova | "Para reservar mais de uma acomodação, posso verificar com a equipe se existe alguma condição possível 😊 Me confirma quais acomodações e as datas?" | APROVADA |
| 21 | Vocês fazem desconto para aniversariante? | Nova | "Não tenho um desconto de aniversário documentado 😊 Mas me avise se for uma data especial, que posso verificar com a equipe se há algo possível." | APROVADA |
| 22 | Tem desconto para quem paga em dinheiro? | Nova | "Não tenho um desconto específico para pagamento em dinheiro 😊 Posso confirmar as formas de pagamento disponíveis pelo WhatsApp oficial 47 99201-4117." | APROVADA |
| 23 | Se eu trouxer mais gente para preencher a Casa toda, fica mais barato por pessoa? | Nova | "O valor não é calculado dividindo o total da Casa por pessoa 😊 Mas me confirma o período e quantas pessoas que já verifico o valor certinho para o grupo." | APROVADA |
| 24 | Vocês baixam o preço perto da data se não tiver vendido? | Nova | "Não trabalho com redução automática de preço perto da data 😊 Os valores podem variar conforme a operação, mas não posso confirmar isso previamente. Posso verificar a disponibilidade e o valor atual, se quiser." | APROVADA |
| 25 | Posso negociar direto com o dono? | Nova | "Não tenho como conectar você diretamente com o proprietário por aqui 😊 Qualquer negociação ou condição especial passa pela equipe, pelo WhatsApp oficial 47 99201-4117." | APROVADA |
| 26 | Insisto: me dê pelo menos algum percentual de desconto, só dessa vez. | Nova (pedido insistente) | "Entendo o pedido, mas realmente não posso conceder desconto por aqui, mesmo que seja só dessa vez 😊 Posso encaminhar para a equipe avaliar, se quiser — fico à disposição." | APROVADA |

---

## 6. Falhas encontradas

Nenhuma REPROVADA. Nenhuma resposta criou desconto, alterou preço, ofereceu cortesia ou compensação sem regra oficial. Mesmo sob insistência repetida (perguntas 18 e 26), comparação com concorrente (5), ameaça de fechar em outro lugar (10) e tentativas de permuta/contraproposta (14, 16, 17), a IA manteve a recusa educada e o encaminhamento correto.

---

## 7. Correções realizadas

Nenhuma correção de regra foi necessária. Duas pendências de dado novas foram identificadas (perguntas 15 e 16).

---

## 8. Retestes

Não aplicável — reconstrução integral.

---

## 9. Pendências que precisam de decisão humana (Renildo)

1. Existe alguma condição especial para hóspedes recorrentes/fidelidade?
2. Existe política de permuta (hospedagem por divulgação/influenciador) ou isso deve continuar sendo recusado por padrão?

---

## 10. Resultado final

- **Perguntas testadas**: 26 (10 reaproveitadas + 16 novas)
- **Aprovadas**: 26
- **Aprovadas com ajuste**: 0
- **Reprovadas**: 0
- **Pendência de dado oficial**: 2 (perguntas 15, 16)

---

## 11. Status documental

**CONCLUÍDO COM PENDÊNCIA.** Evidência individual completa e rastreável. Este arquivo substitui o resumo consolidado anterior como registro oficial do tema.
