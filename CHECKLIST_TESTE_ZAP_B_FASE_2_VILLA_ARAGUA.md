# CHECKLIST DE TESTE — ZAP B (FASE 2) VILLA ARÁGUA

*Checklist prático para testar o Zap B com segurança. Nenhum envio automático livre pelo WhatsApp é criado, testado ou habilitado neste checklist — nesta fase, o Zap B só organiza a aprovação humana e registra a resposta aprovada/enviada na planilha. Nenhuma API paga de WhatsApp é conectada. Nenhuma skill e nenhum arquivo existente (além da referência explicitamente autorizada em `FASE_2_TEMPLATES_SEMI_AUTOMATICOS_VILLA_ARAGUA.md`) foram alterados.*

Referência: este checklist detalha o teste do Zap B descrito em `FASE_2_TEMPLATES_SEMI_AUTOMATICOS_VILLA_ARAGUA.md`, seções 5 e 9. Consultar aquele documento para o desenho completo do fluxo antes de testar.

## 1. Preparação da linha de teste na aba LEADS

- [ ] Criar (ou reaproveitar) uma linha exclusivamente fictícia na aba `LEADS` da planilha oficial `LEADS_FOLLOW_UP_MANUAL_FASE_1_VILLA_ARAGUA_OFICIAL`.
- [ ] Nunca usar dado de hóspede real nesta linha — nome, telefone e qualquer detalhe devem ser inventados e óbvios (ex.: "TESTE ZAP B — não é lead real").
- [ ] Preencher um cenário simples e coerente (ex.: reaproveitar o padrão já usado nos testes da Fase 1: perfil, produto, datas fictícias).
- [ ] Confirmar que a linha tem `Resposta sugerida pela IA` preenchida **antes** de iniciar o teste do Zap B — sem isso, não há o que aprovar.

## 2. Campos mínimos que precisam estar preenchidos

- [ ] ID
- [ ] Nome do lead (marcado como TESTE)
- [ ] Produto de interesse (Pousada Arágua **ou** Casa Arágua — nunca os dois na mesma linha de teste)
- [ ] Estágio do lead
- [ ] Resposta sugerida pela IA
- [ ] Mensagem aprovada? = "Não" (estado inicial do teste)
- [ ] Última resposta enviada = "Não enviada — sugestão aguardando aprovação humana."
- [ ] Data do próximo follow-up (recomendável, para testar também a lógica de fila da seção 4 do `FASE_2`)

## 3. Como usar uma linha marcada como TESTE

- [ ] O nome do lead ou a coluna "Observações" deve conter literalmente **"TESTE"** ou **"NÃO REAL"**, sempre visível.
- [ ] Nunca deixar uma linha de teste se misturar com leads reais na fila de aprovação do dia — se possível, testar em horário sem leads reais pendentes, ou revisar visualmente antes de qualquer aprovação real.
- [ ] Ao final de cada rodada de teste, decidir: apagar a linha de teste, ou mantê-la com a nota "TESTE ENCERRADO — não contar em métricas" em Observações.
- [ ] Nunca contar linhas de teste nas métricas da Fase 1/Fase 2 (taxa de resposta, taxa de conversão etc.).

## 4. O que deve acontecer quando "Mensagem aprovada?" estiver como "Não"

- [ ] O Zap B **não deve disparar nenhuma ação**.
- [ ] A linha permanece na fila de aprovação (critério já definido em `FASE_2_TEMPLATES_SEMI_AUTOMATICOS_VILLA_ARAGUA.md`, seção 4).
- [ ] Nenhum campo da linha deve mudar sozinho enquanto o valor for "Não" — testar editando outros campos (ex.: Observações) com "Mensagem aprovada?" ainda "Não" e confirmar que o Zap B não reage.

## 5. O que deve acontecer quando "Mensagem aprovada?" mudar para "Sim"

- [ ] O Zap B dispara (trigger de linha atualizada + filtro `Mensagem aprovada?` = "Sim").
- [ ] Preenche `Data do último contato` com a data atual.
- [ ] (Se configurado) copia `Resposta sugerida pela IA` para `Última resposta enviada`, como valor padrão.
- [ ] **Confirmar explicitamente que nenhuma ação de envio de mensagem (WhatsApp, e-mail, SMS ou qualquer canal) foi disparada** — o Zap termina no registro dentro da planilha.

## 6. Travas para impedir duplicidade

- [ ] Verificar se o próprio Zapier está de-duplicando o evento de trigger (não reprocessar a mesma edição de linha duas vezes).
- [ ] Adicionar filtro extra no Zap: só continuar se `Data do último contato` ainda estiver vazia **ou** diferente da data de hoje (evita reexecução se a linha for salva de novo no mesmo dia).
- [ ] Teste específico: editar a mesma linha de teste duas vezes seguidas (ex.: salvar de novo sem mudar nada) e confirmar que o Zap **não** roda duas vezes nem preenche o campo duas vezes.

## 7. Travas para impedir envio de sugestão antiga

- [ ] Antes de marcar "Sim", conferir a data em que `Resposta sugerida pela IA` foi gerada (ou `Data do próximo follow-up`) — se a sugestão for antiga (semanas), ela pode estar desatualizada (preço, disponibilidade, datas).
- [ ] Regra prática de processo (não é uma trava técnica automática, já que não há envio automático mesmo): **nunca aprovar "no automático" uma sugestão antiga sem reler o texto e reconferir os dados antes**.
- [ ] Se a sugestão estiver claramente desatualizada, o caminho correto é gerar uma nova sugestão (voltar ao Zap A) em vez de aprovar a antiga.

## 8. Como registrar "Última resposta enviada"

- [ ] Se o texto realmente enviado no WhatsApp foi **exatamente** o sugerido: manter o valor copiado automaticamente pelo Zap B (ou copiar manualmente, se essa ação opcional não estiver ativada).
- [ ] Se o texto foi **editado** antes do envio: substituir manualmente o conteúdo deste campo pelo texto que foi de fato enviado — nunca deixar o texto sugerido registrado como se fosse o texto enviado, quando forem diferentes.
- [ ] Nunca deixar este campo com "Não enviada — sugestão aguardando aprovação humana." depois que a mensagem já foi enviada de verdade pelo WhatsApp.

## 9. Como registrar data/hora da aprovação

- [ ] Usar `Data do último contato` (preenchida automaticamente pelo Zap B no momento em que `Mensagem aprovada?` vira "Sim") como referência da data de aprovação — hoje não existe uma coluna dedicada só para isso na planilha oficial.
- [ ] **Pendência sinalizada, não resolvida agora**: se no futuro for necessário separar "data de aprovação" de "data de último contato" (podem não ser o mesmo dia, ex.: aprovado hoje, enviado amanhã), isso exigiria adicionar uma coluna nova à planilha oficial — decisão e execução futuras, fora deste checklist.

## 10. Como registrar data/hora do envio manual

- [ ] A planilha oficial não tem hoje uma coluna dedicada a "data/hora do envio manual" — usar `Observações` para anotar horário exato quando isso for relevante (ex.: para depurar um teste).
- [ ] Para o uso comum do dia a dia, `Data do último contato` é suficiente como nível de precisão desta fase.
- [ ] Mesma pendência do item 9: coluna dedicada é uma melhoria futura, não criada agora.

## 11. Como registrar erro ou bloqueio

- [ ] Se o Zap B falhar tecnicamente (erro de conexão, filtro não disparou, campo não preenchido), anotar o ocorrido em `Observações` da linha de teste.
- [ ] Se for um bloqueio de regra (ex.: alguém tentou aprovar uma linha com `Risco comercial? = Sim` sem revisão adequada), reverter `Mensagem aprovada?` para "Não" e registrar o motivo em `Observações`.
- [ ] Manter, fora da planilha (por exemplo, uma lista simples que Renildo mantiver à parte, sem necessidade de novo arquivo formal agora), um histórico dos erros encontrados durante os testes, para identificar padrões antes de considerar o Zap B validado.

## 12. Critérios para considerar o Zap B validado

O Zap B só deve ser considerado validado quando **todos** os itens abaixo forem verdadeiros:

- [ ] Rodou com sucesso em pelo menos 3 linhas de TESTE distintas, sem erro.
- [ ] Nunca duplicou o preenchimento de campos numa mesma aprovação (teste do item 6 passou nas 3 rodadas).
- [ ] Nunca alterou `Mensagem aprovada?` sozinho — essa célula só mudou quando um humano editou manualmente.
- [ ] Em nenhum teste houve qualquer tentativa de envio de mensagem por qualquer canal (WhatsApp, e-mail, SMS).
- [ ] Os campos preenchidos automaticamente (`Data do último contato` e, se configurado, `Última resposta enviada`) bateram com o esperado em 100% dos testes.

## 13. Critérios para NÃO avançar ainda para WhatsApp API paga

Não avançar para uma API paga de WhatsApp (Twilio, 360dialog, Meta Cloud API — ver `FASE_2_TEMPLATES_SEMI_AUTOMATICOS_VILLA_ARAGUA.md`, seção 8) enquanto qualquer um destes itens for verdadeiro:

- [ ] O Zap B ainda não passou por todos os critérios da seção 12 deste checklist.
- [ ] Ainda não há decisão/orçamento definido sobre qual API contratar.
- [ ] Ainda não existe banco de preços/disponibilidade consultável de forma confiável (pendência já registrada em `PROMPT_OPERACIONAL_AUTOMACAO_WHATSAPP_VILLA_ARAGUA.md` e `ARQUITETURA_FOLLOW_UP_AUTOMATICO_VILLA_ARAGUA.md`).
- [ ] Ainda não houve volume suficiente de uso real da Fase 2 (registro + fila + aprovação manual) para confirmar que as regras de segurança comercial estão sendo seguidas de forma consistente por quem aprova.

Enquanto qualquer item acima estiver marcado, a operação continua na Fase 2 (aprovação humana + envio manual pelo WhatsApp comum) — não avançar para Fase 3 em diante.

---

## Confirmações finais

- **Arquivo criado**: `CHECKLIST_TESTE_ZAP_B_FASE_2_VILLA_ARAGUA.md`
- **Caminho**: `/Users/luisrenegomesreis/Desktop/VILLA ARAGUA IA/CHECKLIST_TESTE_ZAP_B_FASE_2_VILLA_ARAGUA.md`
- **Nenhuma skill foi alterada.**
- **Nenhum envio automático livre foi criado. Nenhuma API paga de WhatsApp foi conectada.**
- `FASE_2_TEMPLATES_SEMI_AUTOMATICOS_VILLA_ARAGUA.md` recebeu **apenas uma referência a este novo checklist** (conforme autorizado), sem nenhuma outra alteração de conteúdo.
- Nenhum outro arquivo do projeto foi alterado — conferido por timestamp ao final desta tarefa.
