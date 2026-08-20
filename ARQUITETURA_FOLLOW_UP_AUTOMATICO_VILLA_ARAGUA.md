# ARQUITETURA FUTURA DE FOLLOW-UP AUTOMÁTICO — VILLA ARÁGUA

*Manual estratégico e conceitual. Não é automação real — nenhuma conexão com WhatsApp Business/API, Make, Zapier, n8n, Airtable, Google Sheets ou qualquer CRM foi feita ao escrever este arquivo. Nenhum arquivo original da Villa Arágua foi alterado; este documento apenas se apoia nas skills já existentes em `.claude/skills/`.*

## 1. Objetivo

O follow-up automático, quando construído, servirá para **recuperar leads que esfriaram**, **manter a conversa ativa** sem parecer insistência, **melhorar a conversão para reserva direta** e **reduzir a dependência de acompanhamento manual constante** — sempre com tom humano e sem pressão falsa. O objetivo não é "mandar mais mensagem", é não deixar um lead real se perder por falta de acompanhamento no momento certo, com a mesma qualidade de condução que a Recepcionista IA já usa numa conversa ao vivo.

## 2. Princípios

- Follow-up deve **parecer atendimento humano**, nunca robô.
- **Não usar urgência falsa.**
- **Não inventar disponibilidade.**
- **Não inventar desconto.**
- **Não insistir demais.**
- **Respeitar o silêncio do lead** — silêncio não é convite a mandar mais mensagens, é sinal para espaçar ainda mais.
- **Permitir opt-out** — todo lead pode pedir para parar, e isso precisa ser respeitado de imediato e permanentemente.
- **Diferenciar sempre Pousada Arágua e Casa Arágua** — nenhuma mensagem mistura os dois produtos ou aplica oferta de um ao outro.
- **Registrar o estágio do lead** a cada interação — sem isso, não há como saber qual o próximo passo certo.
- **Toda condição comercial precisa de fonte oficial** — preço, desconto, pacote, pet, early check-in, late check-out: nada disso é decidido pelo follow-up, tudo depende de regra já validada ou autorização humana.

## 3. Estágios do lead

- Lead novo
- Pediu preço
- Informou datas
- Não informou datas
- Orçamento enviado
- Perguntou e sumiu
- Comparando opções
- Objeção de preço
- Família com crianças
- Casal
- Pet
- Interessado na Casa Arágua
- Interessado na Pousada Arágua
- Reserva quase fechada
- Reserva perdida
- Pós-estadia
- Reativação futura

Cada lead deve ter **um estágio ativo por vez** (embora possa acumular características, como "família com crianças" + "interessado na Casa Arágua" + "objeção de preço" simultaneamente) — o estágio ativo é o que determina a próxima ação, as demais características são contexto para calibrar o tom da mensagem.

## 4. Gatilhos de follow-up

- Lead sem resposta após a primeira mensagem.
- Orçamento enviado e sem retorno.
- Lead perguntou preço e não informou datas.
- Lead demonstrou objeção (preço, disponibilidade, comparação).
- Lead pediu fotos (e não recebeu resposta de fechamento depois).
- Lead pediu desconto (e a resposta ainda não foi validada/enviada).
- Lead comparou com Booking/Airbnb ou outro concorrente.
- Lead de período de feriado (maior urgência real de checar disponibilidade, nunca urgência forçada).
- Lead de alta temporada.
- Lead da Casa Arágua sem retorno.
- Lead da Pousada Arágua sem retorno.
- Lead antigo, candidato a remarketing/reativação.

Cada gatilho aciona um tipo de mensagem (seção 6), nunca uma mensagem genérica única — o gatilho certo evita que o follow-up pareça disparo automático de massa.

## 5. Cadência sugerida

Esta seção descreve a cadência em **níveis de intenção da mensagem**, não em horas fixas — a cadência final (quando/quantas horas) é uma decisão a validar na prática, não uma regra oficial definida por este documento.

1. **Primeiro follow-up — leve**: reengajamento suave, sem cobrança, dando espaço para o lead responder no tempo dele.
2. **Segundo follow-up — ajuda prática**: reforça um benefício ou tira uma dúvida provável, indo além de só "perguntar se viu a mensagem".
3. **Terceiro follow-up — encerramento elegante**: deixa a porta aberta sem insistir mais, sinalizando que a Villa Arágua fica à disposição quando o lead quiser retomar.
4. **Reativação futura**: só entra depois, e apenas quando fizer sentido (feriado novo, hóspede antigo, temporada relevante) — não é parte da cadência imediata, é um contato pontual futuro.

**Nota de coerência com o que já existe**: a skill `villa-aragua-sales-receptionist` já tem, hoje, uma cadência horária validada e em uso (`references/follow-up.md`): 24h → 72h → 7 dias. Este documento não contradiz essa cadência real — ela pode (ou não) ser a mesma usada quando a automação for construída, mas essa decisão fica para a fase de validação (Fase 1, seção 12), não para este documento conceitual. Tratar qualquer horário específico, aqui ou na futura automação, como **sugestão a confirmar na prática**, nunca como regra já travada só porque está escrita.

## 6. Tipos de mensagens

- Ajuda para escolher acomodação.
- Reforço de benefício (o que já está confirmado como diferencial real).
- Envio de foto/vídeo (apenas material real já existente, nunca descrição do que a foto "deveria" mostrar).
- Lembrete gentil.
- Quebra de objeção (preço, comparação com OTA, disponibilidade).
- Comparação Pousada x Casa (sempre com os dois produtos claramente identificados).
- Retomada após silêncio.
- Encerramento elegante.
- Remarketing sazonal (feriado, temporada, reativação).

## 7. Biblioteca futura de mensagens

Exemplos genéricos, sem preço e sem disponibilidade inventada — servem de ponto de partida para teste manual (Fase 1), não são texto final aprovado para disparo automático.

**Lead sem resposta**:
> "Oi! Fico à disposição se quiser continuar por aqui 😊 Consigo te ajudar com mais alguma informação sobre a Villa Arágua?"

**Orçamento enviado**:
> "Olá 😊 Conseguiu dar uma olhada nas opções que te passei? Fico à disposição para qualquer dúvida."

**Pediu preço sem datas**:
> "Consigo te ajudar com certeza 😊 Pra eu confirmar o valor certinho, me conta as datas de entrada e saída e quantas pessoas seriam?"

**Família em dúvida**:
> "Para famílias, a gente costuma pensar em espaço e praticidade — me conta as idades das crianças que já te oriento na melhor opção entre a Pousada e a Casa 😊"

**Casal em dúvida**:
> "Para um casal, a Pousada Arágua costuma ser bem procurada — clima tranquilo e café da manhã servido na acomodação. Posso te contar mais?"

**Casa Arágua**:
> "A Casa Arágua é uma casa completa e privativa, com piscina própria e espaço para até 6 pessoas. Posso te passar mais detalhes — me confirma as datas que você tem em mente?"

**Pousada Arágua**:
> "A Pousada Arágua fica bem pertinho da praia, com café da manhã servido na própria acomodação. Quer que eu verifique a disponibilidade para as datas de vocês?"

**Objeção de preço**:
> "Entendo 😊 O valor considera a localização, a estrutura e o atendimento durante toda a estadia. Posso verificar se existe alguma opção ou período que fique mais adequado para vocês."

**Encerramento elegante**:
> "Sem problema 😊 Vou deixar nosso atendimento em aberto por aqui. Se quiser retomar em qualquer momento, é só me chamar que verifico a disponibilidade atualizada para vocês."

## 8. Dados necessários para automação futura

- Nome do lead.
- Canal de origem.
- Data da entrada (do lead no funil).
- Interesse: Pousada ou Casa.
- Datas desejadas.
- Número de pessoas.
- Crianças (quantidade e idade).
- Pet (sim/não/não informado).
- Orçamento enviado (sim/não).
- Valor enviado (quando houver — nunca preenchido com valor inventado).
- Status do lead (seção 3).
- Última mensagem enviada.
- Próxima ação sugerida.
- Responsável humano.
- Observações.

## 9. Regras de bloqueio

A automação **não deve enviar** follow-up quando:

- O lead pediu para parar.
- O lead já reservou.
- O lead recusou claramente.
- Houve reclamação sensível.
- O assunto exige humano (ver lista de "precisa humano" já usada nas skills comerciais: desconto, Casa Arágua com valor, pet, early check-in, late check-out, cancelamento, alteração de reserva, dúvida de pagamento).
- Preço/desconto não está autorizado.
- Disponibilidade não foi confirmada.
- A dúvida envolve regra comercial não cadastrada em nenhuma fonte oficial.

Estas regras de bloqueio são **permanentes** — não são uma limitação só da fase inicial, continuam valendo mesmo depois de qualquer automação avançada estar no ar.

## 10. Skills envolvidas no futuro

- **`villa-aragua-sales-receptionist`** — dona do texto e da condução comercial do follow-up: diagnóstico, tom, objeção.
- **`villa-aragua-pricing-revenue`** — dona da regra de preço, desconto e pacote que qualquer follow-up possa mencionar.
- **`villa-aragua-humanizer-pt-br`** — responsável pelo tom final de cada mensagem, garantindo que nada soa robótico.
- **`villa-aragua-campaign-analytics`** — analisa a origem e a qualidade do lead, e mede o resultado do follow-up ao longo do tempo.
- **`villa-aragua-copywriting-conversion`** — apoia mensagens de conversão mais elaboradas (ex.: remarketing sazonal, campanha de feriado).
- **`villa-aragua-skill-router`** — decide qual fluxo de skills usar em cada situação de follow-up, quando não for óbvio.

## 11. Possível arquitetura técnica futura

Em nível conceitual, sem escolha nem configuração feita agora:

- **WhatsApp** como canal de envio (formato ainda a definir: número normal com envio manual apoiado por IA, ou WhatsApp Business/API).
- **CRM ou planilha** para registrar os dados da seção 8.
- **Make, Zapier ou n8n** como possível camada de automação/orquestração entre o CRM e o WhatsApp.
- **Banco de regras oficiais** — fonte única de preço, disponibilidade, política de pet/criança/check-in, para a automação nunca inventar.
- **Biblioteca de mensagens aprovadas** — versão validada e testada dos modelos da seção 7.
- **Logs** — registro de todo envio automático, para auditoria e correção de erro.
- **Aprovação humana em casos sensíveis** — ponto de controle obrigatório antes de qualquer mensagem que toque preço, disponibilidade ou exceção operacional.

## 12. Fases de implantação

- **Fase 1 — Manual assistido**: a IA sugere a mensagem, uma pessoa revisa e envia manualmente. Objetivo: aprender o que funciona.
- **Fase 2 — Templates semi-automáticos**: mensagens padronizadas e pré-aprovadas, prontas para uso rápido, mas ainda enviadas por uma pessoa.
- **Fase 3 — Automação com aprovação humana**: o sistema prepara e agenda, mas cada envio passa por aprovação antes de sair.
- **Fase 4 — Automação parcial com regras**: mensagens de baixo risco (lembrete leve, confirmação de dado) podem sair sem aprovação individual; tudo que toca as regras de bloqueio (seção 9) continua exigindo humano.
- **Fase 5 — Integração completa com CRM/WhatsApp**: arquitetura técnica da seção 11 madura e validada, operando de ponta a ponta — ainda assim, com os pontos de aprovação humana da Fase 4 preservados para os casos sensíveis.

Nenhuma fase deve ser pulada — cada uma existe para validar a anterior antes de aumentar o nível de automação.

## 13. Checklist antes de automatizar

- [ ] Banco de preços oficial existe e está acessível.
- [ ] Banco de disponibilidade existe e está confiável.
- [ ] Política de desconto está definida e documentada.
- [ ] Política de pet está definida e documentada.
- [ ] Política de criança está definida e documentada.
- [ ] Regras de check-in/check-out (incluindo early/late) estão definidas e documentadas.
- [ ] Mensagens estão aprovadas (não só rascunhadas).
- [ ] Opt-out funciona de verdade e é respeitado sem exceção.
- [ ] Existe responsável humano definido para revisar/aprovar casos sensíveis.
- [ ] O sistema foi testado com leads reais antes de qualquer disparo em escala.
- [ ] Existem logs de erro e um processo para corrigir falha rapidamente.

Se qualquer item estiver sem resposta clara, a automação não deve avançar de fase.

---

## Confirmações finais

- **Caminho do arquivo**: `/Users/luisrenegomesreis/Desktop/VILLA ARAGUA IA/ARQUITETURA_FOLLOW_UP_AUTOMATICO_VILLA_ARAGUA.md` (raiz do projeto).
- **Nenhum arquivo original da Villa Arágua foi alterado** — este documento se apoia em `villa-aragua-sales-receptionist`, `villa-aragua-pricing-revenue`, `villa-aragua-humanizer-pt-br`, `villa-aragua-campaign-analytics` e `villa-aragua-skill-router`, todos preservados sem modificação.
- **Nenhuma automação real foi criada** — nenhum WhatsApp Business/API, Make, Zapier, n8n, Airtable, Google Sheets ou CRM foi acessado ou configurado.

### Pendências encontradas

- Não existe hoje nenhum CRM ou planilha de leads em uso — a seção 8 é uma proposta de campos mínimos, não uma ferramenta já implementada.
- A cadência da seção 5 é conceitual (leve/prático/elegante); a cadência horária real (24h/72h/7 dias) já existe validada em `villa-aragua-sales-receptionist/references/follow-up.md` — a decisão de reaproveitar esses horários na automação futura ainda não foi tomada.
- Nenhuma ferramenta técnica da seção 11 foi escolhida.
- Não existe banco de preços/disponibilidade consultável programaticamente — hoje é tudo baseado em arquivo oficial lido manualmente/pela IA sob demanda.
- Não existe histórico de desempenho de follow-up (taxa de resposta, reservas recuperadas) para calibrar a cadência com dado real.
