# Decisões Pendentes — Fechamento da Rodada 1 — Recepcionista IA Villa Arágua

## BACKLOG OPERACIONAL PÓS-RODADA 1

**Data**: 2026-07-12 (criação e decisão das 3 CRÍTICAS) → 2026-07-13 (Rodada 1 encerrada formalmente; as 22 decisões restantes passam a compor o backlog operacional pós-Rodada 1).

**O que isso significa**: a Rodada 1 foi encerrada em `FECHAMENTO_RODADA_1_RECEPCIONISTA_IA_VILLA_ARAGUA.md` com as 3 decisões CRÍTICAS resolvidas. As **22 decisões restantes (6 ALTA, 7 MÉDIA, 9 BAIXA) não foram resolvidas nem descartadas** — elas passam a compor o backlog operacional da Villa Arágua, disponíveis para decisão de Renildo a qualquer momento, sem bloquear a operação da Recepcionista IA nem o início da Rodada 2. Nenhum conteúdo, prioridade ou classificação de risco destas 22 decisões foi alterado nesta atualização — apenas a moldura de acompanhamento (elas deixam de ser "pendência de fechamento da Rodada 1" e passam a ser "item de backlog operacional contínuo"). Nenhum campo `DECISÃO: [PENDENTE]` foi preenchido.

**Destaque separado — PENDÊNCIA PRIORITÁRIA DE OPERAÇÃO / COMPLIANCE**: a regularização e implantação da **FNRH Digital** (ligada à Decisão 3, já com regra de segurança definida) não é uma decisão comercial como as demais 22 — é uma pendência de compliance que precisa de ação operacional própria da Villa Arágua, fora do escopo de teste da Recepcionista IA. Ela permanece destacada como prioritária e **não deve ser confundida com "implantada"** em nenhuma comunicação futura.

**Natureza deste arquivo**: consolidação final de todas as pendências humanas da Rodada 1, extraídas de `PENDENCIAS_RENILDO_RODADA_1_VILLA_ARAGUA_IA.md`, `CONSOLIDACAO_PENDENCIAS_RODADA_1_5_VILLA_ARAGUA_IA.md`, `FECHAMENTO_RODADA_1_RECEPCIONISTA_IA_VILLA_ARAGUA.md` e dos 15 arquivos individuais `RESULTADO_TESTE_*`. Nenhum teste foi refeito, nenhuma regra foi alterada e nenhuma decisão foi tomada aqui — este arquivo apenas organiza o que já existe para que Renildo decida.

**Nota metodológica sobre o número "18"**: o relatório anterior citava 18 pendências, mas esse número somava bullets sem verificar duplicidade entre seções. A consolidação real encontrou **36 menções de pendência** espalhadas pelos documentos (algumas repetidas em mais de um arquivo, algumas sendo sub-perguntas da mesma decisão de fundo). Depois de agrupar o que é, de fato, a mesma decisão, restam **25 decisões reais e distintas** — ver seção "Resumo executivo" abaixo para o detalhamento.

Também foram encontradas **2 pendências reais que não estavam listadas em `PENDENCIAS_RENILDO...md`**, mas apareciam em outros registros da Rodada 1: (1) CNPJ, Instagram e e-mail oficiais ainda não propagados para a base operacional da IA (citado em `ROTEIRO_TESTE_MANUAL_RECEPCIONISTA_IA_VILLA_ARAGUA.md`, seção 7, "Pendências de fundo", e reafirmado no teste de Golpe/Pagamento); (2) localização exata da churrasqueira da Pousada em relação à piscina (citada no teste original de Churrasqueira e reafirmada no reteste de 2026-07-12). Ambas foram incorporadas às decisões abaixo.

---

## Resumo executivo

| # | Decisão | Prioridade | Risco atual | Temas/testes afetados | Status da decisão |
|---|---|---|---|---|---|
| 1 | Efeito da taxa de limpeza da Casa (R$ 450) sobre cancelamento e remarcação | CRÍTICA | Alto | Pedido de desconto, Cancelamento da Casa Arágua (original + reteste) — 3 | **DEFINIDA — 2026-07-12** |
| 2 | Acesso físico não instalado — contingência de energia e canal alternativo | CRÍTICA | Alto | Problema de acesso e lock box, Check-in/check-out/early/late — 2 | **DEFINIDA (canal de voz) — 2026-07-12; tecnologia física PENDENTE DE IMPLANTAÇÃO** |
| 3 | Procedimento de identificação no check-in / pessoa não cadastrada | CRÍTICA | Médio-alto | Problema de acesso e lock box, Check-in/check-out/early/late — 2 | **REGRA DE SEGURANÇA DEFINIDA — 2026-07-12; PROCEDIMENTO FNRH PENDENTE DE IMPLANTAÇÃO** |
| 4 | Responsável pela limpeza da churrasqueira da Casa Arágua | ALTA | Médio | Churrasqueira (original + reteste), Regras da Casa Arágua — 3 | PENDENTE — RENILDO |
| 5 | Procedimento de cancelamento partindo da própria Villa Arágua (não do hóspede) | ALTA | Médio | Cancelamento da Pousada, Cancelamento da Casa Arágua — 2 | PENDENTE — RENILDO |
| 6 | Política para cão de apoio emocional / animal de serviço | ALTA | Médio-alto | Pet — 1 | PENDENTE — RENILDO |
| 7 | CNPJ, Instagram e e-mail oficiais não propagados para a base da IA | ALTA | Médio | Hóspede desconfiado de golpe/pagamento, credibilidade institucional — 1 (+ contexto geral) | PENDENTE — RENILDO |
| 8 | Acessibilidade da Casa Arágua para cadeira de rodas | ALTA | Médio | Dúvida fora da base — 1 | PENDENTE — RENILDO |
| 9 | Cancelamento parcial de reserva com múltiplas acomodações (Pousada) | ALTA | Médio | Cancelamento da Pousada — 1 | PENDENTE — RENILDO |
| 10 | Caução para danos maiores na Casa Arágua (fora do contexto de eventos) | MÉDIA | Médio | Visitantes/festas/silêncio, Regras da Casa Arágua — 2 | PENDENTE — RENILDO |
| 11 | Limite de frequência de visitas ao longo da estadia | MÉDIA | Baixo-médio | Visitantes/festas/silêncio, Regras da Casa Arágua — 2 | PENDENTE — RENILDO |
| 12 | Café opcional da Casa (R$ 80/pessoa): periodicidade, dias isolados, cardápio | MÉDIA | Baixo-médio | Café da manhã (original + reteste) — 2 | PENDENTE — RENILDO |
| 13 | Tarifa de criança acima de 6 anos | MÉDIA | Baixo-médio | Crianças/capacidade/cama extra (original + reteste) — 2 | PENDENTE — RENILDO |
| 14 | Existe modelo de contrato/termo formal para enviar ao hóspede? | MÉDIA | Baixo | Golpe/pagamento/cobrança — 1 | PENDENTE — RENILDO |
| 15 | Processo formal para reincidência de reclamação do mesmo hóspede | MÉDIA | Baixo | Hóspede irritado — 1 | PENDENTE — RENILDO |
| 16 | Porções por bandeja e preferências simples de café além das 3 confirmadas | MÉDIA | Baixo | Café da manhã (original + reteste) — 2 | PENDENTE — RENILDO |
| 17 | Distribuição de pessoas por quarto na Casa Arágua | BAIXA | Baixo | Crianças/capacidade/cama extra — 1 | PENDENTE — RENILDO |
| 18 | Quantidade máxima de aparelhos conectados ao Wi-Fi | BAIXA | Baixo | Wi-Fi da Casa Arágua — 1 | PENDENTE — RENILDO |
| 19 | Exigência de carteira de vacinação do pet | BAIXA | Baixo | Pet — 1 | PENDENTE — RENILDO |
| 20 | Condição especial para hóspedes recorrentes/fidelidade | BAIXA | Baixo | Pedido de desconto — 1 | PENDENTE — RENILDO |
| 21 | Política de permuta (hospedagem por divulgação/influenciador) | BAIXA | Baixo | Pedido de desconto — 1 | PENDENTE — RENILDO |
| 22 | Política de troca de hóspede no meio da estadia | BAIXA | Baixo | Dúvida fora da base — 1 | PENDENTE — RENILDO |
| 23 | Utensílios detalhados da churrasqueira (Pousada e Casa) + localização vs. piscina | BAIXA | Baixo | Churrasqueira (original + reteste), Regras da Casa Arágua — 3 | PENDENTE — RENILDO |
| 24 | Itens de infraestrutura e conveniência não confirmados (7 itens agrupados) | BAIXA | Baixo | Dúvida fora da base (original + reteste), Pedido de desconto — 3 | PENDENTE — RENILDO |
| 25 | Auditoria do `PLAYBOOK_ATENDIMENTO_WHATSAPP.md` como documento geral | BAIXA | Baixo | Hóspede irritado, Wi-Fi da Casa Arágua — 2 | PENDENTE — RENILDO |

---

# PRIORIDADE CRÍTICA

## Decisão 1 — Taxa de limpeza da Casa Arágua e cancelamento/remarcação

### Situação atual
A taxa de limpeza final da Casa Arágua é dado oficial confirmado: **R$ 450,00 por estadia**, obrigatória, cobrada à parte da diária (item 46 de `DADOS_OFICIAIS_ATENDIMENTO_VILLA_ARAGUA.md`).

### O que falta definir
Se essa taxa é devolvida, retida ou tratada de forma diferente do restante do valor da reserva em caso de **cancelamento**; e se ela permanece válida (sem nova cobrança) em caso de **remarcação** para outra data.

### Onde a pendência apareceu
`PENDENCIAS_RENILDO_RODADA_1_VILLA_ARAGUA_IA.md` (seção 4, chamada de "a pendência mais crítica da Rodada 1" desde 2026-07-04) e seção 2B; testes "Pedido de desconto" (pergunta original sobre taxa da Casa), "Cancelamento da Casa Arágua" (teste original e reteste de 2026-07-10, pergunta 23 do `RESULTADO_TESTE_CANCELAMENTO_CASA_ARAGUA_RODADA_1...md`).

### Por que isso importa para a Recepcionista IA
É uma das perguntas mais prováveis de um hóspede da Casa Arágua que precisa cancelar ou remarcar — envolve dinheiro (R$ 450) e pode gerar atrito se a IA responder errado ou de forma inconsistente.

### Comportamento seguro atual da IA
A IA nunca afirma se a taxa é devolvida ou retida — sempre reconhece que o dado não está confirmado e encaminha ao WhatsApp oficial 47 99201-4117.

### Risco de manter indefinido
**Alto.** Envolve valor financeiro relativamente alto (R$ 450) em um cenário emocionalmente sensível (cancelamento). Toda pergunta sobre isso hoje vira escalonamento manual — em volume, isso gera trabalho repetitivo para quem responde o WhatsApp oficial.

### Sugestão operacional para decisão
Como a taxa cobre um serviço (limpeza pós-estadia) que só será executado se a reserva realmente acontecer, uma lógica simples e defensável seria: dentro do prazo de cancelamento (21 dias), a taxa segue a mesma regra dos 90% de devolução; fora do prazo, fica retida junto com o restante. Para remarcação, a taxa permaneceria válida para a nova data, já que o serviço ainda será prestado.

**SUGESTÃO — AGUARDA DECISÃO DO PROPRIETÁRIO.**

### Decisão do Renildo
DECISÃO: **DEFINIDA (2026-07-12).** Quando a hospedagem for cancelada e não tiver ocorrido check-in nem utilização da Casa Arágua, a taxa de limpeza de R$ 450,00 é devolvida integralmente — tratamento próprio, que não acompanha automaticamente o percentual de retenção aplicado ao valor da hospedagem (que segue a política já documentada no item 34, sem alteração). Em remarcação aprovada, a taxa já paga é transferida para a nova data, sem nova cobrança. Caso já tenha ocorrido check-in ou utilização da Casa, a IA não promete devolução — encaminha para análise humana. A IA não executa reembolso, cancelamento ou remarcação sozinha, apenas explica a regra e encaminha a execução.

### Após a decisão
✅ **Executado em 2026-07-12**: atualizado `DADOS_OFICIAIS_ATENDIMENTO_VILLA_ARAGUA.md` (item 46), `ROTEIRO_RECEPCIONISTA_IA.md`, `PROMPT_RECEPCIONISTA_IA_WHATSAPP.md`. Reteste direcionado concluído em `RESULTADO_TESTE_CANCELAMENTO_CASA_ARAGUA_RODADA_1...md` (pergunta 23 atualizada + 5 perguntas novas na seção 5B) — 5/5 aprovadas. Não foi necessário alterar `RESULTADO_TESTE_PEDIDO_DESCONTO_RODADA_1...md` (a lógica de remarcação já estava coberta corretamente pela resposta genérica existente, sem menção indevida à taxa).

---

## Decisão 2 — Acesso físico ainda não instalado: contingência de energia e canal alternativo

### Situação atual
Porteiro eletrônico e lock boxes (Pousada e Casa) **não estão fisicamente instalados** — o acesso hoje depende do apoio da equipe pelo WhatsApp oficial (confirmado em `PENDENCIAS_CRITICAS_OPERACAO_REAL_VILLA_ARAGUA.md` e `AUDITORIA_FINAL_CHECKIN_AUTONOMO_VILLA_ARAGUA_V1.md`).

### O que falta definir
(1) Se/como uma falta de energia afetará o funcionamento do portão eletrônico/lock box quando forem instalados, e se haverá algum backup; (2) se existe algum canal alternativo ao WhatsApp (ex.: ligação telefônica) para o hóspede em caso de falha de internet no momento do acesso.

### Onde a pendência apareceu
`PENDENCIAS_RENILDO_RODADA_1_VILLA_ARAGUA_IA.md` (seção 2B); `RESULTADO_TESTE_ACESSO_LOCK_BOX_RODADA_1...md` (perguntas 23 e 24).

### Por que isso importa para a Recepcionista IA
São exatamente os cenários em que o hóspede está **parado na porta, sem conseguir entrar** — o momento de maior estresse possível no atendimento. Sem uma resposta pronta, a IA só pode orientar "tente de novo" ou "peça ajuda a alguém", o que é seguro mas frustrante.

### Comportamento seguro atual da IA
Reconhece o limite, não inventa canal alternativo nem promete que a energia não afeta o sistema, orienta o WhatsApp oficial 47 99201-4117 como único canal confirmado.

### Risco de manter indefinido
**Alto.** Baixa frequência, mas alto impacto quando acontece — é literalmente o hóspede sem conseguir entrar na acomodação.

### Sugestão operacional para decisão
Como a Villa Arágua não tem equipe 24h, uma solução simples e barata seria manter um número de telefone (mesmo que o mesmo WhatsApp oficial, mas com opção de ligação de voz) divulgado como alternativa em caso de falha de internet — sem exigir infraestrutura nova. Para energia, recomenda-se que qualquer equipamento futuro tenha bateria interna básica (a maioria dos lock boxes eletrônicos do mercado já vem com isso).

**SUGESTÃO — AGUARDA DECISÃO DO PROPRIETÁRIO.**

### Decisão do Renildo
DECISÃO: **PARCIALMENTE DEFINIDA (2026-07-12).** O número oficial de atendimento da Villa Arágua (47 99201-4117) também passa a ser considerado canal de contato por **ligação de voz** em situação de contingência de acesso, quando o WhatsApp não for suficiente ou estiver indisponível — a IA não promete atendimento humano imediato, tempo de resposta específico ou chegada presencial. O futuro sistema de acesso (Pousada e Casa) deverá prever uma solução segura de contingência para falha de energia ou indisponibilidade do fluxo digital — **a tecnologia (bateria interna, nobreak, chave física, gerador, modelo de equipamento) não foi escolhida nesta etapa** e permanece como **PENDÊNCIA DE IMPLANTAÇÃO técnica futura**, não como pendência de regra da Recepcionista IA. Enquanto porteiro eletrônico e lock boxes não estiverem fisicamente instalados e validados, a IA continua informando que o acesso depende do apoio da equipe, e nunca afirma que o sistema autônomo já está implantado.

### Após a decisão
✅ **Executado em 2026-07-12**: atualizado `DADOS_OFICIAIS_ATENDIMENTO_VILLA_ARAGUA.md` (item 30), `ROTEIRO_RECEPCIONISTA_IA.md` (seção 11B), `PROMPT_RECEPCIONISTA_IA_WHATSAPP.md`. Reteste direcionado concluído em `RESULTADO_TESTE_ACESSO_LOCK_BOX_RODADA_1...md` (perguntas 23, 24 atualizadas + 27, 28, 29 novas) — 5/5 aprovadas.

---

## Decisão 3 — Procedimento de identificação no check-in / pessoa não cadastrada

### Situação atual
Não existe procedimento de identificação/documento documentado para o check-in. A regra de segurança geral já impede a IA de autorizar sozinha o acesso de qualquer pessoa que não conste na reserva.

### O que falta definir
Se a Villa Arágua pede algum tipo de identificação (documento, nome completo) no check-in, e como proceder quando alguém tenta fazer check-in no lugar do titular da reserva.

### Onde a pendência apareceu
`RESULTADO_TESTE_CHECKIN_CHECKOUT_EARLY_LATE_RODADA_1...md` (pergunta 32); `RESULTADO_TESTE_ACESSO_LOCK_BOX_RODADA_1...md` (pergunta 17, sobre visitante tentando entrar antes do titular).

### Por que isso importa para a Recepcionista IA
Toca diretamente em segurança: alguém tentando se apresentar como hóspede sem realmente estar na reserva. Hoje a IA já recusa corretamente e escala, mas sem um procedimento formal, cada caso depende 100% do julgamento humano no WhatsApp.

### Comportamento seguro atual da IA
Nunca autoriza check-in de pessoa não cadastrada sem confirmação da equipe; nunca inventa procedimento de identificação; sempre encaminha ao WhatsApp oficial.

### Risco de manter indefinido
**Médio-alto.** Não é um risco frequente, mas é o tipo de situação (pessoa se passando por hóspede) que, se mal resolvida uma única vez, pode gerar problema sério de segurança ou de confiança.

### Sugestão operacional para decisão
Um procedimento simples e de baixo custo: pedir que o nome de quem for fazer o check-in bata com o nome informado na reserva (sem exigir documento físico, já que a operação é enxuta); em caso de divergência, a equipe confirma por telefone/WhatsApp com o titular antes de liberar o acesso.

**SUGESTÃO — AGUARDA DECISÃO DO PROPRIETÁRIO.**

### Decisão do Renildo
DECISÃO: **DECISÃO DE SEGURANÇA: DEFINIDA (2026-07-12).** A Recepcionista IA nunca libera automaticamente acesso ou check-in de pessoa que não esteja corretamente vinculada à hospedagem, ou cuja relação com a reserva esteja divergente ou não confirmada. Quando uma pessoa diferente do titular ou responsável conhecido pela reserva tentar fazer check-in ou solicitar acesso, a IA encaminha para verificação humana antes de qualquer liberação — a afirmação verbal da pessoa não é confirmação suficiente. A IA não inventa procedimento de conferência de identidade, não cria exceção sozinha, e não exige por iniciativa própria fotografia de documento, selfie, dados bancários, senha, código de autenticação ou qualquer dado não previsto em procedimento oficial documentado.

**PROCEDIMENTO DEFINITIVO DE IDENTIFICAÇÃO/FNRH: PENDENTE DE IMPLANTAÇÃO.** A Villa Arágua ainda não implantou/cadastrou seu fluxo na FNRH Digital. A IA nunca afirma que a Villa já utiliza FNRH Digital. Pendência prioritária registrada separadamente: "Regularizar e implantar o fluxo da FNRH Digital na Villa Arágua e, após a implantação, documentar o procedimento oficial de pré-check-in, check-in, conferência de dados e tratamento de divergência de hóspede para integração segura com a Recepcionista IA." Essa pendência **não autoriza** a IA a inventar um fluxo provisório.

### Após a decisão
✅ **Executado em 2026-07-12**: criada a nova seção 11D em `ROTEIRO_RECEPCIONISTA_IA.md` e `PROMPT_RECEPCIONISTA_IA_WHATSAPP.md`; adicionado o item 71 em `DADOS_OFICIAIS_ATENDIMENTO_VILLA_ARAGUA.md`, diferenciando explicitamente a regra de segurança (definida) do procedimento FNRH (pendente de implantação). Reteste direcionado concluído em `RESULTADO_TESTE_CHECKIN_CHECKOUT_EARLY_LATE_RODADA_1...md` (perguntas 31, 32 atualizadas + 33–37 novas) — 5/5 aprovadas. A pergunta 17 de `RESULTADO_TESTE_ACESSO_LOCK_BOX_RODADA_1...md` foi revisada e permanece consistente com a nova regra 11D, sem necessidade de alteração de resposta.

---

# PRIORIDADE ALTA

## Decisão 4 — Responsável pela limpeza da churrasqueira da Casa Arágua

### Situação atual
A churrasqueira da Casa Arágua é confirmada como exclusiva da reserva, sem taxa, com carvão por conta do hóspede e utensílios básicos disponíveis (item 48 de `DADOS_OFICIAIS`).

### O que falta definir
Se a limpeza final da churrasqueira, depois do uso, fica a cargo do hóspede ou da equipe.

### Onde a pendência apareceu
Esta é a pendência **mais recorrente** de toda a Rodada 1 fora do tema financeiro: apareceu no teste original de "Churrasqueira", no teste de "Regras da Casa Arágua" (2026-07-10) e novamente no reteste dedicado de "Churrasqueira" (2026-07-12) — 3 aparições distintas, sempre com a mesma resposta segura da IA.

### Por que isso importa para a Recepcionista IA
É uma pergunta prática e comum ("preciso limpar depois de usar?"). Sem resposta, a IA sempre escala uma dúvida operacional simples, gerando trabalho manual repetido.

### Comportamento seguro atual da IA
Reconhece que o dado não está confirmado, não decide sozinha quem é responsável, encaminha ao WhatsApp oficial.

### Risco de manter indefinido
**Médio.** Não é um risco de segurança, mas gera atrito operacional recorrente e uma sensação de "pousada desorganizada" se hóspedes diferentes receberem respostas diferentes de pessoas diferentes da equipe.

### Sugestão operacional para decisão
Dado que a Pousada já tem uma regra clara (equipe faz a limpeza final, hóspede só retira o que levou), manter a mesma lógica na Casa Arágua reduziria a carga cognitiva da operação — um único padrão para os dois produtos, mais fácil de comunicar e de a equipe seguir.

**SUGESTÃO — AGUARDA DECISÃO DO PROPRIETÁRIO.**

### Decisão do Renildo
DECISÃO: [PENDENTE]

### Após a decisão
Atualizar `DADOS_OFICIAIS_ATENDIMENTO_VILLA_ARAGUA.md` (item 48), `ROTEIRO_RECEPCIONISTA_IA.md`, `PROMPT_RECEPCIONISTA_IA_WHATSAPP.md`. Reteste: **reteste direcionado** (a mesma pergunta aparece em 3 arquivos) — `RESULTADO_TESTE_CHURRASQUEIRA_RODADA_1...md` (pergunta 29), `RESULTADO_TESTE_REGRAS_DA_CASA_ARAGUA_RODADA_1...md` (pergunta 14).

---

## Decisão 5 — Cancelamento partindo da própria Villa Arágua

### Situação atual
As políticas de cancelamento documentadas (item 34) tratam apenas do cancelamento feito **pelo hóspede**. Não há regra para quando é a própria Villa Arágua/pousada que precisa cancelar uma reserva já confirmada.

### O que falta definir
Procedimento e devolução (reembolso total? crédito? realocação?) quando o cancelamento parte da Villa Arágua, tanto na Pousada quanto na Casa Arágua.

### Onde a pendência apareceu
`RESULTADO_TESTE_CANCELAMENTO_POUSADA_RODADA_1...md` (pergunta 25) e `RESULTADO_TESTE_CANCELAMENTO_CASA_ARAGUA_RODADA_1...md` (pergunta 25).

### Por que isso importa para a Recepcionista IA
Embora seja uma situação rara, é de altíssimo impacto quando acontece — o hóspede não fez nada errado e precisa de uma resposta clara e justa. Uma resposta mal dada aqui tem grande potencial de virar reclamação pública.

### Comportamento seguro atual da IA
Reconhece o limite, não promete reembolso total nem nenhuma condição específica, encaminha ao WhatsApp oficial.

### Risco de manter indefinido
**Médio** (baixa frequência, mas alto impacto reputacional se ocorrer sem uma resposta pronta).

### Sugestão operacional para decisão
Uma prática comum e de baixo custo para pousadas pequenas: em caso de cancelamento pela própria operação, devolver 100% do valor pago (sem retenção) e, se possível, oferecer ajuda para encontrar outra opção na região — sem que isso vire uma promessa formal automática da IA enquanto não for uma política decidida.

**SUGESTÃO — AGUARDA DECISÃO DO PROPRIETÁRIO.**

### Decisão do Renildo
DECISÃO: [PENDENTE]

### Após a decisão
Atualizar `DADOS_OFICIAIS_ATENDIMENTO_VILLA_ARAGUA.md` (item 34), `ROTEIRO_RECEPCIONISTA_IA.md`. Reteste: **reteste de 1–3 perguntas** em cada um dos dois arquivos de cancelamento (pergunta 25 em cada).

---

## Decisão 6 — Política para cão de apoio emocional / animal de serviço

### Situação atual
A política de pet documentada (itens 6, 41, 60, 61) trata de pets recreativos comuns (cães e gatos pequenos). Não há menção a cães de apoio emocional ou animais de serviço.

### O que falta definir
Se esses animais seguem a mesma regra dos pets comuns ou têm tratamento diferenciado (o que costuma ter implicação legal em muitos contextos, incluindo isenção de restrições de porte/quantidade em legislações de acessibilidade).

### Onde a pendência apareceu
`RESULTADO_TESTE_PET_RODADA_1_RECEPCIONISTA_IA_VILLA_ARAGUA.md` (pergunta 22).

### Por que isso importa para a Recepcionista IA
É um tema sensível: uma resposta errada pode gerar tanto um problema de acessibilidade/legal quanto um desconforto genuíno se tratado apenas como "mais um pet".

### Comportamento seguro atual da IA
Não confirma nem nega, não trata como pet comum automaticamente, encaminha ao WhatsApp oficial para avaliação da equipe.

### Risco de manter indefinido
**Médio-alto.** É um tema com potencial de sensibilidade legal/de acessibilidade — mesmo com baixa frequência, merece uma definição clara e cuidadosa, de preferência com orientação além da própria equipe (ex.: uma consulta rápida sobre a legislação aplicável).

### Sugestão operacional para decisão
Recomenda-se, no mínimo, tratar animais de apoio emocional/serviço com autorização automática (sem exigir avaliação de porte), já que é o padrão mais comum e mais seguro nesse tipo de situação — mas essa é uma área onde vale a pena confirmar com mais cuidado antes de formalizar, dada a sensibilidade do tema.

**SUGESTÃO — AGUARDA DECISÃO DO PROPRIETÁRIO.**

### Decisão do Renildo
DECISÃO: [PENDENTE]

### Após a decisão
Atualizar `DADOS_OFICIAIS_ATENDIMENTO_VILLA_ARAGUA.md`, `ROTEIRO_RECEPCIONISTA_IA.md`, `PROMPT_RECEPCIONISTA_IA_WHATSAPP.md`. Reteste: **reteste de 1–3 perguntas** em `RESULTADO_TESTE_PET_RODADA_1...md` (pergunta 22).

---

## Decisão 7 — CNPJ, Instagram e e-mail oficiais não propagados para a base da IA

### Situação atual
A Villa Arágua tem CNPJ, Instagram e e-mail oficiais — mas esses dados **não estão na base operacional da Recepcionista IA**. Essa lacuna já era conhecida desde o fechamento original da Rodada 1 (citada como "pendência de fundo" em `ROTEIRO_TESTE_MANUAL_RECEPCIONISTA_IA_VILLA_ARAGUA.md`, seção 7), mas não constava explicitamente em `PENDENCIAS_RENILDO...md` — foi recuperada nesta consolidação.

### O que falta definir
Reunir e formalizar CNPJ, link do Instagram e e-mail oficial como dado oficial, para a IA poder compartilhá-los quando um hóspede pedir para verificar a legitimidade da Villa Arágua.

### Onde a pendência apareceu
`ROTEIRO_TESTE_MANUAL_RECEPCIONISTA_IA_VILLA_ARAGUA.md` (seção 7, nota final); reafirmada em `RESULTADO_TESTE_GOLPE_PAGAMENTO_RODADA_1_RECEPCIONISTA_IA_VILLA_ARAGUA.md` (perguntas 2 e 3).

### Por que isso importa para a Recepcionista IA
É usada diretamente no combate a golpe/desconfiança — exatamente o tema mais sensível relacionado a segurança financeira do hóspede. Hoje a IA precisa dizer "não tenho esse link agora", o que enfraquece a resposta de segurança no momento em que ela mais precisa ser forte.

### Comportamento seguro atual da IA
Não inventa CNPJ nem link de Instagram — reconhece o limite e direciona ao WhatsApp oficial.

### Risco de manter indefinido
**Médio.** Não é um risco por si só (a IA não erra), mas é uma oportunidade perdida de reforçar credibilidade justamente nos momentos em que o hóspede está mais desconfiado.

### Sugestão operacional para decisão
É a decisão mais simples desta lista: reunir os 3 dados (já existentes, não precisam ser criados) e propagá-los para a base oficial.

**SUGESTÃO — AGUARDA DECISÃO DO PROPRIETÁRIO.**

### Decisão do Renildo
DECISÃO: [PENDENTE]

### Após a decisão
Atualizar `DADOS_OFICIAIS_ATENDIMENTO_VILLA_ARAGUA.md`, `ROTEIRO_RECEPCIONISTA_IA.md`, `PROMPT_RECEPCIONISTA_IA_WHATSAPP.md`. Reteste: **nenhum reteste amplo necessário** — reteste de 1–3 perguntas em `RESULTADO_TESTE_GOLPE_PAGAMENTO_RODADA_1...md` (perguntas 2, 3, 8).

---

## Decisão 8 — Acessibilidade da Casa Arágua para cadeira de rodas

### Situação atual
Não há informação documentada sobre acessibilidade física da Casa Arágua (rampas, degraus, largura de portas, banheiro adaptado).

### O que falta definir
Se a Casa Arágua é ou não acessível para cadeira de rodas ou mobilidade reduzida.

### Onde a pendência apareceu
`RESULTADO_TESTE_DUVIDA_FORA_BASE_RODADA_1_RECEPCIONISTA_IA_VILLA_ARAGUA.md` (pergunta 13).

### Por que isso importa para a Recepcionista IA
Um hóspede com mobilidade reduzida decide a reserva com base nessa resposta — um erro aqui pode gerar uma situação constrangedora e difícil de reverter na chegada.

### Comportamento seguro atual da IA
Não confirma nem nega, recomenda confirmação antes de fechar a reserva.

### Risco de manter indefinido
**Médio.** Baixa frequência de pergunta, mas consequência potencialmente séria (hóspede chegando e não conseguindo usar o espaço).

### Sugestão operacional para decisão
Recomenda-se um levantamento simples e único (uma visita com esse olhar específico) para documentar de forma definitiva a acessibilidade real da Casa — depois disso a resposta pode ser direta e seguraz para sempre, sem depender de confirmação caso a caso.

**SUGESTÃO — AGUARDA DECISÃO DO PROPRIETÁRIO.**

### Decisão do Renildo
DECISÃO: [PENDENTE]

### Após a decisão
Atualizar `DADOS_OFICIAIS_ATENDIMENTO_VILLA_ARAGUA.md`, `ROTEIRO_RECEPCIONISTA_IA.md`. Reteste: **reteste de 1–3 perguntas** em `RESULTADO_TESTE_DUVIDA_FORA_BASE_RODADA_1...md` (pergunta 13).

---

## Decisão 9 — Cancelamento parcial de reserva com múltiplas acomodações

### Situação atual
A política de cancelamento (item 34) trata de "a reserva", sem prever o caso de uma reserva com mais de uma acomodação da Pousada, em que o hóspede queira cancelar apenas uma.

### O que falta definir
Se é possível cancelar só uma acomodação de uma reserva múltipla, mantendo as demais, e como isso afeta o cálculo de devolução.

### Onde a pendência apareceu
`RESULTADO_TESTE_CANCELAMENTO_POUSADA_RODADA_1_RECEPCIONISTA_IA_VILLA_ARAGUA.md` (pergunta 23).

### Por que isso importa para a Recepcionista IA
Situação relativamente rara (grupos grandes que reservam mais de uma suíte), mas quando ocorre, envolve cálculo financeiro que a IA não pode inventar.

### Comportamento seguro atual da IA
Trata como uma alteração de reserva, sob consulta da equipe — não confirma nem recusa automaticamente.

### Risco de manter indefinido
**Médio** (financeiro, mas baixa frequência).

### Sugestão operacional para decisão
Tratar cada acomodação da reserva como uma "sub-reserva" independente para fins de cancelamento, aplicando a mesma regra de prazo/devolução a cada uma separadamente — mantém a lógica simples e consistente com a política já existente.

**SUGESTÃO — AGUARDA DECISÃO DO PROPRIETÁRIO.**

### Decisão do Renildo
DECISÃO: [PENDENTE]

### Após a decisão
Atualizar `DADOS_OFICIAIS_ATENDIMENTO_VILLA_ARAGUA.md` (item 34), `ROTEIRO_RECEPCIONISTA_IA.md`. Reteste: **reteste de 1–3 perguntas** em `RESULTADO_TESTE_CANCELAMENTO_POUSADA_RODADA_1...md` (pergunta 23).

---

# PRIORIDADE MÉDIA

## Decisão 10 — Caução para danos maiores na Casa Arágua (fora de eventos)

### Situação atual
Já está confirmado que **não há caução fixa oficial para eventos** (item 66). Para danos em geral (fora do contexto de evento), a IA trata como "avaliação caso a caso", o que é seguro, mas não há confirmação formal de que não existe caução alguma.

### O que falta definir
Se existe ou não algum tipo de caução/depósito de segurança para a Casa Arágua, fora do contexto específico de eventos.

### Onde a pendência apareceu
`RESULTADO_TESTE_VISITANTES_FESTAS_SILENCIO_RODADA_1...md` e `RESULTADO_TESTE_REGRAS_DA_CASA_ARAGUA_RODADA_1...md` (pergunta 22).

### Por que isso importa para a Recepcionista IA
Hóspedes de casas de temporada costumam perguntar sobre caução — uma resposta clara reduz atrito na hora de fechar a reserva.

### Comportamento seguro atual da IA
Não inventa caução, trata dano como avaliação caso a caso pela equipe.

### Risco de manter indefinido
**Médio.** Não é um risco de segurança, mas pode gerar surpresa desagradável se um dano maior acontecer e não houver clareza prévia sobre como isso é tratado financeiramente.

### Sugestão operacional para decisão
Para manter a operação simples, a alternativa mais fácil de administrar é não cobrar caução prévia (mantendo o modelo atual) e reforçar a política de "avaliação e cobrança por custo de reposição quando necessário" — evita burocracia de cobrar e devolver caução em uma operação enxuta.

**SUGESTÃO — AGUARDA DECISÃO DO PROPRIETÁRIO.**

### Decisão do Renildo
DECISÃO: [PENDENTE]

### Após a decisão
Atualizar `DADOS_OFICIAIS_ATENDIMENTO_VILLA_ARAGUA.md`, `ROTEIRO_RECEPCIONISTA_IA.md`. Reteste: **reteste de 1–3 perguntas** em `RESULTADO_TESTE_REGRAS_DA_CASA_ARAGUA_RODADA_1...md` (pergunta 22).

---

## Decisão 11 — Limite de frequência de visitas ao longo da estadia

### Situação atual
Visitantes já têm regra clara: sempre sob consulta e autorização prévia, sem taxa fixa (itens 43, 64). Não há, porém, um limite de frequência — por exemplo, se um hóspede pode receber visita todos os dias da estadia.

### O que falta definir
Se existe algum limite de frequência de visitas, ou se cada visita é avaliada isoladamente sem limite de repetição.

### Onde a pendência apareceu
`RESULTADO_TESTE_VISITANTES_FESTAS_SILENCIO_RODADA_1...md` (pergunta 26).

### Por que isso importa para a Recepcionista IA
Evita que a regra de "autorização prévia" vire, na prática, uma autorização automática recorrente sem controle.

### Comportamento seguro atual da IA
Trata cada visita como um pedido novo, sob consulta — não promete frequência ilimitada nem cria um limite que não existe.

### Risco de manter indefinido
**Baixo-médio.** Não é um risco imediato, mas pode gerar uso indevido da regra de visitantes se não houver algum limite de bom senso.

### Sugestão operacional para decisão
Manter o modelo atual (cada visita avaliada individualmente pela equipe) já funciona como controle natural — não é necessário criar um número fixo, apenas reforçar internamente que visitas muito frequentes merecem atenção redobrada da equipe.

**SUGESTÃO — AGUARDA DECISÃO DO PROPRIETÁRIO.**

### Decisão do Renildo
DECISÃO: [PENDENTE]

### Após a decisão
Atualizar `DADOS_OFICIAIS_ATENDIMENTO_VILLA_ARAGUA.md`, `ROTEIRO_RECEPCIONISTA_IA.md`, se uma regra for criada. Reteste: **nenhum**, se a decisão for manter o modelo atual; **reteste de 1–3 perguntas**, se uma regra nova for criada.

---

## Decisão 12 — Café opcional da Casa Arágua (R$ 80/pessoa): periodicidade, dias isolados e cardápio

### Situação atual
O valor está confirmado: **R$ 80,00 por pessoa**, sob consulta, com solicitação antecipada (item 47).

### O que falta definir
(1) Se o valor é cobrado por dia de estadia, por período contratado, ou como valor único; (2) se é possível contratar o café da Casa em apenas um dos dias da estadia; (3) se o cardápio do pacote da Casa é o mesmo cardápio habitual da Pousada (item 57).

### Onde a pendência apareceu
`RESULTADO_TESTE_CAFE_DA_MANHA_RODADA_1_RECEPCIONISTA_IA_VILLA_ARAGUA.md` (perguntas 20, 21, 25).

### Por que isso importa para a Recepcionista IA
É uma pergunta comercial direta — hóspedes da Casa que consideram contratar o café precisam saber exatamente quanto vão pagar antes de decidir.

### Comportamento seguro atual da IA
Confirma o valor por pessoa (R$ 80), mas não confirma a unidade de tempo nem o cardápio exato — encaminha para confirmação.

### Risco de manter indefinido
**Baixo-médio.** Afeta a clareza comercial, mas não gera risco de segurança ou reclamação grave — só perde uma oportunidade de fechar a venda do café de forma mais fluida.

### Sugestão operacional para decisão
Cobrar por dia de café efetivamente entregue (não um valor único fixo para toda a estadia) tende a ser mais simples de comunicar e mais justo para quem quer o café só em alguns dias — e usar o mesmo cardápio habitual da Pousada evita ter que administrar dois cardápios diferentes.

**SUGESTÃO — AGUARDA DECISÃO DO PROPRIETÁRIO.**

### Decisão do Renildo
DECISÃO: [PENDENTE]

### Após a decisão
Atualizar `DADOS_OFICIAIS_ATENDIMENTO_VILLA_ARAGUA.md` (item 47), `ROTEIRO_RECEPCIONISTA_IA.md`, `PROMPT_RECEPCIONISTA_IA_WHATSAPP.md`, `GUIA_DIGITAL_HOSPEDE_VILLA_ARAGUA.md`. Reteste: **reteste de 1–3 perguntas** em `RESULTADO_TESTE_CAFE_DA_MANHA_RODADA_1...md` (perguntas 20, 21, 25).

---

## Decisão 13 — Tarifa de criança acima de 6 anos

### Situação atual
Está confirmado que crianças **até 6 anos são gratuitas** e que criança acima de 6 anos **não** é gratuita (item 45). O que não está explícito é se ela sempre paga a tarifa normal de adulto, ou se há alguma avaliação caso a caso conforme a composição do grupo.

### O que falta definir
Formalizar se a tarifa acima de 6 anos é sempre "tarifa normal" ou se pode variar conforme o caso.

### Onde a pendência apareceu
`PENDENCIAS_RENILDO_RODADA_1_VILLA_ARAGUA_IA.md` (subseção "Crianças, berço, cama extra e itens de bebê"); reafirmada em `RESULTADO_TESTE_CRIANCAS_CAPACIDADE_CAMA_EXTRA_RODADA_1...md`.

### Por que isso importa para a Recepcionista IA
Afeta diretamente o cálculo de valor de famílias com filhos entre 7 e 17 anos — um grupo comum no perfil de hóspede da Villa Arágua.

### Comportamento seguro atual da IA
Informa corretamente que não há gratuidade acima de 6 anos, sem afirmar se o valor é sempre igual ao de adulto.

### Risco de manter indefinido
**Baixo-médio.** Não é um risco de segurança, apenas uma zona cinzenta comercial que a IA já trata com segurança (não inventa desconto).

### Sugestão operacional para decisão
A forma mais simples de administrar, sem exigir cálculo especial: tarifa normal de adulto para qualquer pessoa acima de 6 anos, sem exceção — mantém a regra fácil de comunicar e de aplicar.

**SUGESTÃO — AGUARDA DECISÃO DO PROPRIETÁRIO.**

### Decisão do Renildo
DECISÃO: [PENDENTE]

### Após a decisão
Atualizar `DADOS_OFICIAIS_ATENDIMENTO_VILLA_ARAGUA.md` (item 45), `ROTEIRO_RECEPCIONISTA_IA.md`. Reteste: **nenhum** (a resposta atual já é segura e não muda de comportamento, apenas ganha mais precisão).

---

## Decisão 14 — Modelo de contrato/termo formal para o hóspede

### Situação atual
Não existe um contrato/termo padrão documentado para ser enviado a um hóspede que solicitar.

### O que falta definir
Se existe (ou deve existir) um documento formal desse tipo.

### Onde a pendência apareceu
`RESULTADO_TESTE_GOLPE_PAGAMENTO_RODADA_1...md` (pergunta 8).

### Por que isso importa para a Recepcionista IA
Reforça credibilidade em momentos de desconfiança, mas não é essencial para a operação básica — hoje a Villa Arágua funciona sem esse documento.

### Comportamento seguro atual da IA
Reconhece que não tem esse documento para enviar, encaminha para a equipe.

### Risco de manter indefinido
**Baixo.**

### Sugestão operacional para decisão
Não é uma prioridade para uma operação enxuta — pode ficar como "não temos contrato formal, apenas confirmação de reserva" enquanto isso não gerar reclamação real de hóspedes.

**SUGESTÃO — AGUARDA DECISÃO DO PROPRIETÁRIO.**

### Decisão do Renildo
DECISÃO: [PENDENTE]

### Após a decisão
Atualizar `DADOS_OFICIAIS_ATENDIMENTO_VILLA_ARAGUA.md`, `ROTEIRO_RECEPCIONISTA_IA.md`, se um documento for criado. Reteste: **nenhum**, exceto se um documento novo for criado (então reteste de 1–3 perguntas).

---

## Decisão 15 — Processo formal para reincidência de reclamação

### Situação atual
A regra 16B trata qualquer reclamação (primeira vez ou repetida) da mesma forma segura: acolhe, não promete solução imediata, escala.

### O que falta definir
Se deve existir algum processo diferenciado quando o mesmo hóspede relata o mesmo problema mais de uma vez.

### Onde a pendência apareceu
`RESULTADO_TESTE_HOSPEDE_IRRITADO_RODADA_1...md` (pergunta 13).

### Por que isso importa para a Recepcionista IA
Reincidência costuma ser um sinal de que algo realmente não foi resolvido — merece atenção redobrada da equipe, mesmo que a IA não deva prometer prioridade.

### Comportamento seguro atual da IA
Reconhece a repetição, encaminha normalmente, sem prometer prioridade (que não pode ser prometida sem regra).

### Risco de manter indefinido
**Baixo.** A IA já se comporta com segurança; a ausência de processo formal só significa que a triagem de reincidência depende do cuidado manual da equipe.

### Sugestão operacional para decisão
Recomenda-se apenas uma orientação interna simples: quando a equipe perceber reincidência pelo histórico de mensagens, tratar como prioridade operacional — sem precisar formalizar isso como promessa da IA ao hóspede.

**SUGESTÃO — AGUARDA DECISÃO DO PROPRIETÁRIO.**

### Decisão do Renildo
DECISÃO: [PENDENTE]

### Após a decisão
Nenhuma alteração de dado oficial necessária, apenas orientação interna da equipe (fora do escopo da base da IA). Reteste: **nenhum**.

---

## Decisão 16 — Porções por bandeja e preferências simples de café além das 3 confirmadas

### Situação atual
Já é dado oficial: preferências simples de "sem leite", "sem queijo" e "mais frutas" são atendidas sob aviso prévio (item 58). Cardápio habitual também está confirmado (item 57).

### O que falta definir
(1) Se a quantidade de porções por bandeja segue "conforme número de hóspedes da reserva" ou outra regra; (2) se a equipe atende preferências simples **além** das três já confirmadas.

### Onde a pendência apareceu
`PENDENCIAS_RENILDO_RODADA_1_VILLA_ARAGUA_IA.md` (subseção "Café da manhã..."); `RESULTADO_TESTE_CAFE_DA_MANHA_RODADA_1...md`.

### Por que isso importa para a Recepcionista IA
Afeta principalmente famílias grandes (quantidade de porções) e hóspedes com preferências alimentares um pouco fora do já confirmado.

### Comportamento seguro atual da IA
Cita apenas as 3 preferências confirmadas, não promete porção extra automaticamente.

### Risco de manter indefinido
**Baixo.**

### Sugestão operacional para decisão
Formalizar "porções conforme número de hóspedes confirmados na reserva" é a lógica mais simples e já é, na prática, o que provavelmente já acontece operacionalmente.

**SUGESTÃO — AGUARDA DECISÃO DO PROPRIETÁRIO.**

### Decisão do Renildo
DECISÃO: [PENDENTE]

### Após a decisão
Atualizar `DADOS_OFICIAIS_ATENDIMENTO_VILLA_ARAGUA.md` (itens 57-58), `ROTEIRO_RECEPCIONISTA_IA.md`. Reteste: **nenhum**.

---

# PRIORIDADE BAIXA

## Decisão 17 — Distribuição de pessoas por quarto na Casa Arágua

### Situação atual
A capacidade total da Casa Arágua (6 pessoas) está confirmada (item 8). A distribuição interna por quarto não está.

### O que falta definir
Quantos quartos a Casa tem e quantas pessoas cabem em cada um.

### Onde a pendência apareceu
`RESULTADO_TESTE_CRIANCAS_CAPACIDADE_CAMA_EXTRA_RODADA_1...md` (pergunta 25).

### Por que isso importa para a Recepcionista IA
Ajuda famílias grandes a se organizarem antes da viagem, mas não afeta a segurança nem a política comercial.

### Comportamento seguro atual da IA
Não inventa distribuição, encaminha para confirmação.

### Risco de manter indefinido
**Baixo.**

### Sugestão operacional para decisão
Um levantamento simples (contagem de quartos e camas da Casa) resolve isso de forma definitiva.

**SUGESTÃO — AGUARDA DECISÃO DO PROPRIETÁRIO.**

### Decisão do Renildo
DECISÃO: [PENDENTE]

### Após a decisão
Atualizar `DADOS_OFICIAIS_ATENDIMENTO_VILLA_ARAGUA.md`, `ROTEIRO_RECEPCIONISTA_IA.md`. Reteste: **nenhum**.

---

## Decisão 18 — Quantidade máxima de aparelhos no Wi-Fi

### Situação atual
Velocidade confirmada (700 mega). Número de aparelhos simultâneos recomendado não está documentado.

### Onde a pendência apareceu
`RESULTADO_TESTE_WIFI_CASA_ARAGUA_RODADA_1...md` (perguntas 12, 24).

### O que falta definir
Um número aproximado recomendado, se Renildo tiver essa informação do provedor.

### Por que isso importa para a Recepcionista IA
Relevante só para grupos grandes com múltiplos dispositivos e uso intenso (ex.: home office de vários hóspedes ao mesmo tempo).

### Comportamento seguro atual da IA
Não inventa número, apenas reforça que a estrutura é forte (700 mega).

### Risco de manter indefinido
**Baixo.**

### Sugestão operacional para decisão
Não é crítico formalizar um número exato — manter a resposta atual ("estrutura forte de 700 mega") já cobre a grande maioria dos casos sem necessidade de dado adicional.

**SUGESTÃO — AGUARDA DECISÃO DO PROPRIETÁRIO.**

### Decisão do Renildo
DECISÃO: [PENDENTE]

### Após a decisão
Atualizar `DADOS_OFICIAIS_ATENDIMENTO_VILLA_ARAGUA.md` (item 32), se um número for confirmado. Reteste: **nenhum**.

---

## Decisão 19 — Exigência de carteira de vacinação do pet

### Situação atual
Pet pequeno é aceito sem taxa, mediante aviso prévio (itens 6, 41, 60).

### O que falta definir
Se é exigida carteira de vacinação do pet no check-in.

### Onde a pendência apareceu
`RESULTADO_TESTE_PET_RODADA_1...md` (pergunta 23).

### Por que isso importa para a Recepcionista IA
Detalhe prático que hóspedes com pet podem perguntar antes de viajar.

### Comportamento seguro atual da IA
Não inventa exigência, recomenda confirmar com a equipe.

### Risco de manter indefinido
**Baixo.**

### Sugestão operacional para decisão
Não exigir formalmente reduz burocracia para a operação enxuta atual — mas recomenda-se ao menos orientar verbalmente que o pet esteja com a saúde em dia.

**SUGESTÃO — AGUARDA DECISÃO DO PROPRIETÁRIO.**

### Decisão do Renildo
DECISÃO: [PENDENTE]

### Após a decisão
Atualizar `DADOS_OFICIAIS_ATENDIMENTO_VILLA_ARAGUA.md`, `ROTEIRO_RECEPCIONISTA_IA.md`, se uma exigência for criada. Reteste: **nenhum**.

---

## Decisão 20 — Condição especial para hóspedes recorrentes/fidelidade

### Situação atual
Não existe programa de fidelidade documentado.

### Onde a pendência apareceu
`RESULTADO_TESTE_PEDIDO_DESCONTO_RODADA_1...md` (pergunta 15).

### O que falta definir
Se Renildo quer criar alguma condição especial para quem já se hospedou antes.

### Por que isso importa para a Recepcionista IA
Pode ser uma alavanca comercial futura (fidelização), mas não é uma necessidade operacional imediata.

### Comportamento seguro atual da IA
Não promete condição de fidelidade, encaminha para a equipe.

### Risco de manter indefinido
**Baixo.**

### Sugestão operacional para decisão
Pode ficar em aberto por ora — é uma decisão mais de marketing/growth do que de segurança operacional, sem urgência para a Rodada 1.

**SUGESTÃO — AGUARDA DECISÃO DO PROPRIETÁRIO.**

### Decisão do Renildo
DECISÃO: [PENDENTE]

### Após a decisão
Atualizar `DADOS_OFICIAIS_ATENDIMENTO_VILLA_ARAGUA.md`, `ROTEIRO_RECEPCIONISTA_IA.md`, se uma política for criada. Reteste: **nenhum**.

---

## Decisão 21 — Política de permuta (hospedagem por divulgação/influenciador)

### Situação atual
Não existe política de permuta documentada; a IA recusa por padrão.

### Onde a pendência apareceu
`RESULTADO_TESTE_PEDIDO_DESCONTO_RODADA_1...md` (perguntas 16, 17).

### O que falta definir
Se a Villa Arágua quer trabalhar com parcerias de divulgação em troca de hospedagem.

### Por que isso importa para a Recepcionista IA
Tema comercial/marketing, não operacional — cada caso hoje já é corretamente escalado.

### Comportamento seguro atual da IA
Recusa automática, sem confirmar nem inventar política, encaminha proposta para avaliação.

### Risco de manter indefinido
**Baixo.**

### Sugestão operacional para decisão
Fora do escopo de segurança operacional — decisão estratégica de marketing que pode ser avaliada com calma, sem pressa desta rodada.

**SUGESTÃO — AGUARDA DECISÃO DO PROPRIETÁRIO.**

### Decisão do Renildo
DECISÃO: [PENDENTE]

### Após a decisão
Atualizar `DADOS_OFICIAIS_ATENDIMENTO_VILLA_ARAGUA.md`, `ROTEIRO_RECEPCIONISTA_IA.md`, se uma política for criada. Reteste: **nenhum**.

---

## Decisão 22 — Política de troca de hóspede no meio da estadia

### Situação atual
Não documentada.

### Onde a pendência apareceu
`RESULTADO_TESTE_DUVIDA_FORA_BASE_RODADA_1...md` (pergunta 19).

### O que falta definir
Se é permitido que uma pessoa da reserva seja substituída por outra durante a estadia.

### Por que isso importa para a Recepcionista IA
Situação rara, mas relevante para controle de quem está de fato hospedado (segurança leve, não crítica).

### Comportamento seguro atual da IA
Reconhece o limite, encaminha ao WhatsApp oficial.

### Risco de manter indefinido
**Baixo.**

### Sugestão operacional para decisão
Tratar como qualquer alteração de reserva — sob consulta e confirmação da equipe, sem regra fixa nova necessária.

**SUGESTÃO — AGUARDA DECISÃO DO PROPRIETÁRIO.**

### Decisão do Renildo
DECISÃO: [PENDENTE]

### Após a decisão
Atualizar `DADOS_OFICIAIS_ATENDIMENTO_VILLA_ARAGUA.md`, se necessário. Reteste: **nenhum**.

---

## Decisão 23 — Utensílios detalhados da churrasqueira e localização vs. piscina

### Situação atual
Confirmado: carvão por conta do hóspede, utensílios básicos disponíveis (Pousada e Casa), sem taxa (itens 33, 48).

### O que falta definir
(1) Lista exata de utensílios (grelha, espetos, pegador, faca, tábua, acendedor); (2) localização exata da churrasqueira da Pousada em relação à piscina.

### Onde a pendência apareceu
`PENDENCIAS_RENILDO_RODADA_1_VILLA_ARAGUA_IA.md`; `RESULTADO_TESTE_CHURRASQUEIRA_RODADA_1...md` (pergunta 8); citado desde o teste original de Churrasqueira (2026-07-04) e reafirmado no reteste (2026-07-12).

### Por que isso importa para a Recepcionista IA
Detalhe prático de conveniência — não afeta segurança nem valor.

### Comportamento seguro atual da IA
Fala apenas "utensílios básicos", sem listar itens específicos; não afirma proximidade exata da piscina.

### Risco de manter indefinido
**Baixo.**

### Sugestão operacional para decisão
Um levantamento único e simples (fotografar/listar o que já existe fisicamente) resolve os dois pontos de uma vez.

**SUGESTÃO — AGUARDA DECISÃO DO PROPRIETÁRIO.**

### Decisão do Renildo
DECISÃO: [PENDENTE]

### Após a decisão
Atualizar `DADOS_OFICIAIS_ATENDIMENTO_VILLA_ARAGUA.md` (itens 33, 48), `ROTEIRO_RECEPCIONISTA_IA.md`. Reteste: **nenhum**.

---

## Decisão 24 — Itens de infraestrutura e conveniência não confirmados

### Situação atual
Sete itens de baixo impacto, todos com o mesmo padrão de resposta segura da IA (reconhece o limite, não inventa, encaminha ao WhatsApp oficial): carregador para carro elétrico; transfer do aeroporto; convênio oficial com passeio de barco; confirmação explícita de que não há restaurante próprio; confirmação explícita de que a Pousada não serve almoço/jantar; desconto para morador de Bombinhas; existência de cofre em todas as acomodações; supermercado maior próximo (nome/distância).

### O que falta definir
Confirmação factual simples de cada item — nenhum deles exige uma política nova, apenas uma resposta de sim/não.

### Onde a pendência apareceu
`PENDENCIAS_RENILDO_RODADA_1_VILLA_ARAGUA_IA.md` (seção 2); reafirmados em `RESULTADO_TESTE_DUVIDA_FORA_BASE_RODADA_1...md` e `RESULTADO_TESTE_PEDIDO_DESCONTO_RODADA_1...md`.

### Por que isso importa para a Recepcionista IA
São perguntas ocasionais de conveniência — nenhuma delas é crítica, mas juntas representam uma parte considerável dos escalonamentos "de baixo valor" para o WhatsApp oficial.

### Comportamento seguro atual da IA
Nunca inventa nenhum desses 7 itens; trata a ausência de estrutura (restaurante, almoço/jantar) como inferência seguramente comunicada, não como afirmação oficial.

### Risco de manter indefinido
**Baixo**, individualmente. Em conjunto, apenas reduzem a autonomia da IA em perguntas simples de turismo/conveniência.

### Sugestão operacional para decisão
Como são 7 confirmações factuais rápidas, recomenda-se resolver todas de uma vez em uma única sessão de perguntas e respostas com Renildo — o esforço de decisão é pequeno e o ganho de autonomia da IA é imediato.

**SUGESTÃO — AGUARDA DECISÃO DO PROPRIETÁRIO.**

### Decisão do Renildo
DECISÃO: [PENDENTE]

### Após a decisão
Atualizar `DADOS_OFICIAIS_ATENDIMENTO_VILLA_ARAGUA.md`, `ROTEIRO_RECEPCIONISTA_IA.md`, `PROMPT_RECEPCIONISTA_IA_WHATSAPP.md`, `GUIA_DIGITAL_HOSPEDE_VILLA_ARAGUA.md`. Reteste: **nenhum**.

---

## Decisão 25 — Auditoria do `PLAYBOOK_ATENDIMENTO_WHATSAPP.md`

### Situação atual
O Playbook tem uma referência cruzada quebrada (já corrigida em `ROTEIRO_RECEPCIONISTA_IA.md`/`PROMPT_RECEPCIONISTA_IA_WHATSAPP.md`) e conteúdo defasado (distância antiga da Casa, política antiga de pet). O fluxo técnico real (Wi-Fi, energia, ar-condicionado, piscina, churrasqueira) já foi resolvido pelos itens 68–70, então este documento **não bloqueia mais nada operacionalmente**.

### O que falta definir
Se o Playbook será atualizado, arquivado como histórico, ou substituído por outro documento.

### Onde a pendência apareceu
`PENDENCIAS_RENILDO_RODADA_1_VILLA_ARAGUA_IA.md` (seção 5); identificado no teste "Hóspede irritado" e auditado no teste "Wi-Fi da Casa Arágua".

### Por que isso importa para a Recepcionista IA
Não afeta o comportamento atual da IA (que já não depende mais desse documento), mas é uma pendência de organização documental que pode confundir quem administra o projeto no futuro.

### Comportamento seguro atual da IA
Já não referencia mais o Playbook para fluxo técnico — nenhum comportamento de risco associado.

### Risco de manter indefinido
**Baixo.**

### Sugestão operacional para decisão
Como o conteúdo relevante já foi absorvido pelos itens oficiais 68–70, a opção mais simples é arquivar o Playbook como histórico, evitando manter dois documentos com informação parcialmente sobreposta.

**SUGESTÃO — AGUARDA DECISÃO DO PROPRIETÁRIO.**

### Decisão do Renildo
DECISÃO: [PENDENTE]

### Após a decisão
Nenhum arquivo da Recepcionista IA precisa ser alterado — apenas o próprio `PLAYBOOK_ATENDIMENTO_WHATSAPP.md` (fora do escopo desta base de testes). Reteste: **nenhum**.

---

## Mapa de impacto final

| Decisão | Arquivos potencialmente afetados | Temas de teste afetados | Reteste necessário |
|---|---|---|---|
| 1. Taxa de limpeza — cancelamento/remarcação | `DADOS_OFICIAIS`, `ROTEIRO`, `PROMPT` | Cancelamento da Casa Arágua | ✅ Concluído (5/5 aprovadas) |
| 2. Acesso físico — energia/canal alternativo | `DADOS_OFICIAIS`, `ROTEIRO` (11B), `PROMPT` | Problema de acesso e lock box | ✅ Concluído (5/5 aprovadas) |
| 3. Identificação no check-in | `ROTEIRO` (11D, nova), `PROMPT` (11D, nova), `DADOS_OFICIAIS` (item 71, novo) | Check-in/check-out/early/late, Problema de acesso | ✅ Concluído (5/5 aprovadas) |
| 4. Limpeza da churrasqueira da Casa | `DADOS_OFICIAIS`, `ROTEIRO`, `PROMPT` | Churrasqueira, Regras da Casa Arágua | Reteste direcionado (2 arquivos) |
| 5. Cancelamento pela Villa | `DADOS_OFICIAIS`, `ROTEIRO` | Cancelamento da Pousada, Cancelamento da Casa | Reteste de 1–3 perguntas (2 arquivos) |
| 6. Cão de apoio emocional/serviço | `DADOS_OFICIAIS`, `ROTEIRO`, `PROMPT` | Pet | Reteste de 1–3 perguntas |
| 7. CNPJ/Instagram/e-mail | `DADOS_OFICIAIS`, `ROTEIRO`, `PROMPT` | Golpe/pagamento/cobrança | Nenhum reteste amplo — 1–3 perguntas |
| 8. Acessibilidade cadeira de rodas | `DADOS_OFICIAIS`, `ROTEIRO` | Dúvida fora da base | Reteste de 1–3 perguntas |
| 9. Cancelamento parcial multi-acomodação | `DADOS_OFICIAIS`, `ROTEIRO` | Cancelamento da Pousada | Reteste de 1–3 perguntas |
| 10. Caução danos maiores Casa | `DADOS_OFICIAIS`, `ROTEIRO` | Regras da Casa Arágua, Visitantes/festas/silêncio | Reteste de 1–3 perguntas |
| 11. Limite frequência de visitas | `DADOS_OFICIAIS`, `ROTEIRO` (se criar regra) | Visitantes/festas/silêncio | Nenhum, exceto se criar regra nova |
| 12. Café Casa — periodicidade/cardápio | `DADOS_OFICIAIS`, `ROTEIRO`, `PROMPT`, `GUIA_DIGITAL` | Café da manhã | Reteste de 1–3 perguntas |
| 13. Tarifa criança acima de 6 | `DADOS_OFICIAIS`, `ROTEIRO` | Crianças/capacidade/cama extra | Nenhum |
| 14. Contrato/termo formal | `DADOS_OFICIAIS`, `ROTEIRO` (se criar) | Golpe/pagamento/cobrança | Nenhum, exceto se criar documento |
| 15. Reincidência de reclamação | Nenhum (orientação interna) | Hóspede irritado | Nenhum |
| 16. Porções/preferências café | `DADOS_OFICIAIS`, `ROTEIRO` | Café da manhã | Nenhum |
| 17. Distribuição de quartos Casa | `DADOS_OFICIAIS`, `ROTEIRO` | Crianças/capacidade/cama extra | Nenhum |
| 18. Aparelhos Wi-Fi | `DADOS_OFICIAIS` | Wi-Fi da Casa Arágua | Nenhum |
| 19. Carteira de vacinação pet | `DADOS_OFICIAIS`, `ROTEIRO` (se criar) | Pet | Nenhum |
| 20. Hóspede recorrente/fidelidade | `DADOS_OFICIAIS`, `ROTEIRO` (se criar) | Pedido de desconto | Nenhum |
| 21. Permuta/influenciador | `DADOS_OFICIAIS`, `ROTEIRO` (se criar) | Pedido de desconto | Nenhum |
| 22. Troca de hóspede em estadia | `DADOS_OFICIAIS` (se necessário) | Dúvida fora da base | Nenhum |
| 23. Utensílios churrasqueira + localização | `DADOS_OFICIAIS`, `ROTEIRO` | Churrasqueira | Nenhum |
| 24. Infraestrutura e conveniência (7 itens) | `DADOS_OFICIAIS`, `ROTEIRO`, `PROMPT`, `GUIA_DIGITAL` | Dúvida fora da base, Pedido de desconto | Nenhum |
| 25. Auditoria do Playbook | `PLAYBOOK_ATENDIMENTO_WHATSAPP.md` (fora do escopo da IA) | Hóspede irritado, Wi-Fi da Casa Arágua | Nenhum |

**Nenhuma decisão desta lista, individualmente ou em conjunto, exige reteste ampliado dos 426 cenários já validados** — todas são alterações pontuais de dado oficial, sem mudança estrutural na forma como a Recepcionista IA se comporta.

---

## Status

Arquivo criado em 2026-07-12, como preparação para decisão do proprietário.

**Atualização (2026-07-12)**: as 3 decisões CRÍTICAS (1, 2 e 3) foram analisadas e definidas pelo proprietário nesta mesma data. Decisão 1 (taxa de limpeza) foi **totalmente resolvida**. Decisão 2 (contingência de acesso) foi **parcialmente resolvida** — o canal de voz está definido, mas a tecnologia física de contingência permanece pendência de implantação (não de regra da IA). Decisão 3 (identificação no check-in) teve a **regra de segurança definida**, mas o procedimento definitivo de identificação/registro permanece pendência de implantação da FNRH Digital (não de regra da IA). As 22 decisões restantes (ALTA, MÉDIA e BAIXA) continuam com `DECISÃO: [PENDENTE]`, sem alteração nesta execução.
