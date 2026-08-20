# Diário de Bordo — Piloto Recepcionista IA Villa Arágua

**Criado no:** Lote 11 da série "WhatsApp Rápido" (2026-08-05)
**Arquivo relacionado:** `PROTOCOLO_USO_DIARIO_RASCUNHO_ASSISTIDO_VILLA_ARAGUA.md`

---

## Objetivo

Registrar o uso diário da Recepcionista IA em Modo Rascunho Assistido durante o piloto.

Este diário serve para:

- acompanhar rascunhos usados;
- registrar ajustes;
- identificar erros;
- medir qualidade;
- decidir aprendizados futuros;
- evitar que mudanças sejam feitas de forma improvisada.

---

## Regras de uso

- Preencher apenas quando a IA for usada para gerar rascunho real.
- Não registrar dados sensíveis do hóspede.
- Não colar comprovantes, senhas, documentos ou dados pessoais completos.
- Registrar o tipo de caso, não expor informações privadas.
- Aprendizado só vira alteração de biblioteca/protocolo após aprovação de Renildo.

---

## Registro diário

| Data | Horário | Quem revisou | Tipo de mensagem | Nível de risco | Template/regra usado | Rascunho aprovado? | Ajuste feito? | Escalou para Renildo? | Motivo | Aprendizado | Precisa persistir? | Observação |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | | | |

*(Tabela de registro por mensagem — segue vazia; nenhum atendimento individual foi lançado linha a linha nesta rodada, para não expor dado de hóspede sem necessidade. O registro agregado do início do piloto real está na seção "Registro do dia — 06/08/2026" abaixo, conforme a Auditoria do Piloto Comercial Real de 06/08/2026 e as decisões de Renildo sobre essa auditoria.)*

---

## Registro do dia — 06/08/2026 (início do piloto real)

**Origem:** Auditoria do Piloto Comercial Real de 06/08/2026, aprovada por Renildo. Este registro separa fatos observados, aprendizados já confirmados (compatíveis com regra oficial já vigente) e hipóteses ainda em teste — nenhuma hipótese abaixo foi transformada em regra oficial.

### Fatos

- O piloto comercial real da Villa Arágua começou em 06/08/2026, com leads reais vindos principalmente de Meta Ads.
- Campanhas de Meta Ads geraram os primeiros leads reais atendidos dentro deste piloto.
- QL, C, Estágio e o Registro Comercial (CRM) foram usados na operação real de atendimento.
- A origem da campanha (Produto e Período já conhecidos pelo anúncio) permitiu evitar perguntas repetidas ao lead em casos reais observados hoje.
- Casos reais de orçamento, grupo grande e feriado (7 de Setembro) foram atendidos durante o piloto.
- Um caso real de redirecionamento (período pedido incompatível com a regra comercial vigente, com oferta de datas alternativas) também foi atendido.
- Os Templates Operacionais QL/C (`TEMPLATES_OPERACIONAIS_QL_C_VILLA_ARAGUA.md`) serviram de referência para a condução dos atendimentos de hoje.
- Valores e ofertas específicos do 7 de Setembro usados nos atendimentos de hoje são operacionais e temporários, vinculados a essa campanha — não foram registrados aqui como regra ou template estrutural permanente (ver `TEMPLATES_OPERACIONAIS_QL_C_VILLA_ARAGUA.md`, changelog de 06/08/2026).

### Aprendizados confirmados (já compatíveis com regra oficial vigente)

- Nunca repetir dado que o lead já informou.
- A origem da campanha deve ser usada como contexto comercial conhecido — Produto e Período já definidos pelo anúncio não devem ser perguntados de novo. Consolidado nesta mesma rodada em `FUNIL_QUALIFICACAO_LEADS_WHATSAPP_QL_VILLA_ARAGUA.md` (seção 5) e `TEMPLATES_OPERACIONAIS_QL_C_VILLA_ARAGUA.md` (`T-QL1-ORIGEM-POUSADA-01`/`T-QL1-ORIGEM-CASA-01`).
- Perguntas objetivas do hóspede devem ser respondidas antes de qualquer nova pergunta de qualificação.
- Silêncio não reduz QL nem C automaticamente (Arquitetura, seção 5; Funil, seção 11).
- Grupos grandes podem receber configuração consultiva (combinação de acomodações), já prevista na Biblioteca Comercial, Regra 22 e `PC-EXT-17`.

### Hipóteses em teste (não formalizadas nesta rodada)

- Imagem institucional no primeiro contato, antes do produto definido.
- Imagem em follow-up.
- Imagem de despedida, para lead QL4 encerrado sem conversão.
- Sequência emocional de imagens ao longo da jornada do lead.
- Follow-up específico de redirecionamento de datas.
- Novos templates sazonais reaproveitáveis entre feriados, sem duplicar por data.

**Nota:** todas as hipóteses acima permanecem em observação. Nenhuma foi formalizada em template, regra, Biblioteca Visual ou cadência oficial nesta rodada — decisão explícita de Renildo, registrada na Auditoria do Piloto Comercial Real de 06/08/2026.

---

## Registro do dia — 08/08/2026 (correção crítica pós-auditoria)

**Origem:** Auditoria do Aprendizado Real de 08/08/2026 (21 casos + teste cego de 14 cenários) e rodada de correção crítica pós-auditoria aprovada por Renildo na mesma data. Este registro documenta correções factuais/documentais e reafirma o que segue como hipótese, sem formalizar nada além do explicitamente aprovado.

### Correções aplicadas

- **QL de campanha com Produto+Período conhecidos**: `TEMPLATES_OPERACIONAIS_QL_C_VILLA_ARAGUA.md` classificava o cenário "campanha COM período, só Pessoas faltando" como QL1 (fichas `T-QL1-ORIGEM-POUSADA-01` e `T-QL1-ORIGEM-CASA-01`, campos 5/20/23, e tabela-resumo). O Funil (`FUNIL_QUALIFICACAO_LEADS_WHATSAPP_QL_VILLA_ARAGUA.md`, fonte oficial de QL) já classifica esse cenário como **QL3** (2 de 3 dados essenciais conhecidos). Corrigido nesta data — decisão de Renildo, sem reabrir a definição conceitual de QL.
- **Faixa etária do mezanino Fuego/Metallo**: no atendimento real de hoje (Caso Andreia), foi informada a faixa "14 a 54 anos". A fonte oficial (`DADOS_OFICIAIS_ATENDIMENTO_VILLA_ARAGUA.md`, item 7) confirma **14 a 59 anos** — a regra oficial já estava correta e não foi alterada. Busca em todo o projeto (fora de pastas de backup) por "14-54"/"54 anos" não encontrou nenhuma referência viva divergente — o erro de hoje não chegou a se propagar para nenhum arquivo, ficou restrito à mensagem enviada à hóspede. Registrado aqui como erro do piloto, para acompanhamento.
- **Classificação do caso Elizete (Pousada/Soleil, exceção C3)**: nenhum arquivo do projeto (CRM, Diário ou outro) continha afirmação de que Elizete "fechou", "converteu" ou "reservou" — busca por "Elizete" no projeto não encontrou nenhuma ocorrência prévia. Fica registrado aqui, pela primeira vez, o estado factual correto: Elizete escolheu a Suíte Soleil (Pousada Arágua), a exceção comercial C3 de 3 diárias foi aprovada por Renildo, o valor R$ 3.096 foi apresentado — **mas ainda não há confirmação humana de pagamento/reserva**. Classificação: **QL4, C3, Estágio = Negociação/validação**, Status final = **não preenchido** até confirmação real.

### Fato operacional — VALIDADO/FORMALIZADO em 11/08/2026

- **Suíte Wood — área externa cercada/portõezinhos para pet**: característica informada diretamente por Renildo durante o piloto de 08/08/2026 (não é invenção da IA nem do atendimento). Classificação original: **"fato operacional informado por Renildo, ainda não formalizado em fonte oficial"** — nesse status, a Recepcionista IA foi orientada a não usar a característica autonomamente. **Status atualizado em 11/08/2026**: achado confirmado durante auditoria pontual disparada pelo atendimento real de Victorio Roda (CRM ID50) — Renildo confirmou por escrito que a informação segue verdadeira, com as ressalvas de que a Wood não é exclusividade pet, a regra geral de aceitação permanece válida, e não deve ser prometida segurança absoluta/contenção garantida/pet sozinho no local. **Formalizado em `DADOS_OFICIAIS_ATENDIMENTO_VILLA_ARAGUA.md`, item 6**, nesta mesma data. A partir de agora, a característica **pode** ser usada pela Recepcionista IA como diferencial de conveniência (nunca como exclusividade), citando a fonte oficial. Backup do estado anterior em `BACKUP_ANTES_FORMALIZACAO_WOOD_PET_2026-08-11/`. Histórico original preservado acima (nada apagado, só marcado como resolvido).

### Hipóteses em teste (reafirmado — não formalizadas nesta rodada)

- Foto de desejo na abertura pós-composição.
- Downsell antes de desconto (refinamento sobre não insistir diante de discrepância histórica de preço).
- Mensagem apagada ≠ perda/NQ automática.
- Estratégia de inventário diferenciada por produto (Pousada x Casa) no mesmo período.
- Parar de vender após escolha confirmada (transição para fechamento).
- "Caro" como sinal de produto superdimensionado vs. fora de orçamento.

**Nota:** nenhuma das hipóteses acima foi formalizada em template, regra, campo de CRM ou governança visual nesta rodada — decisão explícita de Renildo. A discussão de precedência entre códigos de ativo visual (`AT-*`/`POU-*`/`CAS-*`/`TUR-*`) e a criação de campo de CRM para hóspede recorrente/cadastrado seguem como pendências separadas, fora do escopo desta correção.

---

## APRENDIZADO OPERACIONAL DE 10/08/2026 — FECHADO

**Registrado em:** fechamento operacional de 10/08/2026, a pedido de Renildo, com três gates (integridade do CRM, aprendizado auditado, preparação da rotina de 11/08).

**GATE 1 — bloqueio material encontrado e resolvido nesta rodada:**
- Premissa inicial de Renildo ("já cadastrei os leads de hoje") não se confirmou: `CRM_LEADS_VILLA_ARAGUA.md` estava sem nenhuma linha de lead real (só o template, desde 29/07); nenhum dos 16 leads citados no fechamento aparecia em nenhuma fonte do projeto nem em CRM externo (Airtable checado, sem base relacionada).
- Achado independente: `FUNIL_QUALIFICACAO_LEADS_WHATSAPP_QL_VILLA_ARAGUA.md` (fonte oficial de QL) estava corrompido — sobrescrito hoje às 15:34 com o conteúdo "11111111" (8 bytes), no lugar de ~22KB de critérios reais.
- **Ação tomada:** Funil restaurado a partir de `BACKUP_ANTES_PROPAGACAO_C1C4_PRIMEIRA_MENSAGEM_2026-08-06/` (318 linhas recuperadas), com backup do estado corrompido salvo em `BACKUP_ANTES_RESTAURACAO_FUNIL_2026-08-10/`. 16 leads registrados em `CRM_LEADS_VILLA_ARAGUA.md` (seção "Leads de 10/08/2026") a partir dos fatos consolidados por Renildo, com QL/C marcados como sugestão da IA pendente de confirmação por Rene/Nubia, e todo campo sem base factual marcado como "não informado — confirmar" em vez de estimado.

**GATE 2 — aprendizados A–I classificados (não formalizados em nenhuma fonte oficial):**
- A (dado novo do lead substitui contexto presumido da campanha, campanha permanece origem) — **B, aprendizado confirmado** (caso Aleanne).
- B (campanha com Produto+Período conhecidos não repete pergunta de data) — **A, já oficial** em `TEMPLATES_OPERACIONAIS_QL_C_VILLA_ARAGUA.md` (correção de 08/08/2026, campo 12/30) — mas ver regressão abaixo: a regra é oficial para a primeira mensagem, não para o follow-up da Matriz.
- C (follow-up posterior não deve só repetir o anterior) — **A, já oficial** (Matriz seções 4-8 variam texto por tentativa; skill `follow-up.md` já tem a regra "nunca repetir a mesma frase").
- D (follow-up pode revelar barreira real: preço, produto superdimensionado, datas incompatíveis, necessidade de tempo) — **B, aprendizado confirmado** (casos Tabata Caffe, ME ATIVAMENTE, Crismael/Dorivan).
- E (produto inadequado ≠ objeção de preço, não gerar desconto automático) — **B, aprendizado confirmado** (caso Tabata Caffe) — não encontrada em nenhuma fonte escrita até agora.
- F (sem produto adequado, saber parar de vender) — **B, aprendizado confirmado** (caso Tabata Caffe) — idem, não encontrada em fonte escrita.
- G (interpretar "vou analisar"/"obrigada"/"infelizmente não conseguimos" por contexto, não por palavra isolada) — **B, aprendizado confirmado** (casos Paula, Dorivan, Crismael, Eliete, Aleanne, ME ATIVAMENTE).
- H (responder pergunta objetiva intermediária antes de retomar qualificação) — **B, aprendizado confirmado** (caso Elayne, localização).
- I (cadastrado ≠ hóspede; recorrente só com evidência real) — **B, aprendizado confirmado**, com evidência dupla: o próprio bloqueio do Gate 1 desta rodada, e o caso Everton (recorrência declarada pelo lead, ainda não cruzada com histórico interno).

**Regressão de execução (auditada, causa raiz identificada, correção NÃO aplicada ainda):**
- Leads afetados: Adry, Farias, Aldemir, Aleanne, Marcos (campanha reabertura 04–08/09) — QL3 classificado corretamente, mas o follow-up perguntou de novo "datas ou número de pessoas" apesar de Produto+Período já conhecidos pela campanha.
- **Causa raiz:** `MATRIZ_FOLLOWUP_QL_WHATSAPP_VILLA_ARAGUA.md`, seção 5 (QL3), textos de "resposta imediata" e "follow-up 24h/48h" (linhas 84-87) são fixos — perguntam sempre "datas ou número de pessoas", sem condicional para dado já conhecido. A correção de 08/08/2026 ajustou apenas os templates de **primeira mensagem** de campanha em `TEMPLATES_OPERACIONAIS_QL_C_VILLA_ARAGUA.md` (linha 76, `T-QL1-ORIGEM-POUSADA-01`/`CASA-01`, campo 12) — que já perguntam só o que falta — mas não tocou os textos de **follow-up** da Matriz, que continuam genéricos.
- Não é problema de skill/agente nem de precedência entre fontes — a skill `villa-aragua-sales-receptionist/references/follow-up.md` já declara corretamente a Matriz como fonte oficial. O problema é o conteúdo da própria Matriz seção 5.
- **Proposta de correção (não aplicada — fora do escopo estrito do Gate 3 desta rodada, aguardando decisão de Renildo):** tornar os textos de follow-up QL3 (seção 5) condicionais ao dado que falta, no mesmo espírito do campo 12 dos Templates — ex.: trocar "Ficou alguma dúvida sobre datas ou número de pessoas?" por uma variante que só cite o dado realmente pendente.

**GATE 3 — divergência de cadência Matriz vs. skill:** checada e **não encontrada como viva**. `follow-up.md` da skill já declara explicitamente a Matriz como fonte oficial e rotula a cadência genérica 24h/72h/7 dias como "apoio secundário, só quando o QL ainda não foi classificado, nunca prevalece sobre a Matriz". Nenhuma correção necessária aqui.

**Hipóteses visuais de 10/08 — registradas como hipótese, não regra** (casos Zoleide, Elayne, Crismael): foto de piscina/desejo após qualificação, ativo respondendo pergunta objetiva de localização, e foto do único produto adequado ainda durante qualificação. Sem padronização — decisão explícita de não formalizar nesta rodada.

**Direção arquitetural e oportunidade Bombinhas/GEO:** registradas apenas como direção em estudo e oportunidade futura, respectivamente — nenhuma ferramenta escolhida, nenhum conteúdo novo criado.

**Os três pendentes foram resolvidos nesta mesma rodada, com autorização explícita de Renildo:**
1. Correção aplicada em `MATRIZ_FOLLOWUP_QL_WHATSAPP_VILLA_ARAGUA.md`, seção 5 (backup em `BACKUP_ANTES_CORRECAO_FOLLOWUP_QL3_CONTEXTUAL_2026-08-10/`).
2. Sub-rotina "INICIAR DIA OPERACIONAL" adicionada em `.claude/agents/villa-rotina-gestao-operacional.md` (backup em `BACKUP_ANTES_SUBROTINA_INICIAR_DIA_OPERACIONAL_2026-08-10/`).
3. Teste "INICIAR DIA OPERACIONAL — 11/08/2026" executado via subagente, lendo CRM/Matriz/Funil diretamente (sem leads colados manualmente), primeira saída preservada — **resultado: PASSOU COM RESSALVA**. Ressalva: a fila A/B/C/D funcionou corretamente (sem inventar dado, sem mudar QL/C sozinha, respeitando pausa consciente, separando C3 em fila D, sem enviar nada), mas a rotina diária ainda não tem fonte de dados para reservas/check-in/check-out do dia nem para casos de risco abertos — ambos ficaram como lacuna explícita, não como falha do mecanismo testado. Registrado como candidato de melhoria futura (campo de "próximo follow-up" estruturado por data, em vez de texto livre).

---

## APRENDIZADO OPERACIONAL DE 08/08/2026 — FECHADO

**Registrado em:** rodada de propagação final Fase 2 (08/08/2026), após duas rodadas de propagação da revogação do café pago da Casa Arágua (Fase 1: 8 arquivos vivos; Fase 2: 13 arquivos vivos adicionais, incluindo reescrita conceitual da regra-mãe 17 da `BIBLIOTECA_COMERCIAL_RECEPCIONISTA_IA_VILLA_ARAGUA.md`, de "valor não citado" para "serviço inexistente").

- **Café da Casa Arágua**: corrigido em todas as fontes vivas identificadas (21 arquivos ao total, nas duas fases) — a Casa Arágua não oferece café da manhã em nenhuma condição (não incluso, não sob consulta, não como adicional pago). 8 testes de regressão (A–H, cobrindo Recepcionista IA, WhatsApp, Meta Ads, SEO/FAQ e pricing/pacotes) rodados com primeira saída preservada — todos **PASSARAM**.
- **Histórico preservado**: registros de Rodada 1, 1.5 e 2 (testes, questionários de decisão, fechamentos) mantidos intactos, sem edição — não são fonte viva.
- **Duas exceções registradas, não bloqueantes**: (1) `AGENTE_MARKETING_CAMPANHAS_META_ADS_VILLA_ARAGUA.md` permanece com dúvida de classificação VIVO/HISTÓRICO — não editado, fica como pendência para decisão de Renildo; (2) uso residual do termo "garagem" (em vez de "estacionamento exclusivo em área aberta") identificado incidentalmente em 2 arquivos durante os testes — fora do escopo desta correção (só café), não corrigido, reportado para rodada futura.
- **Hipóteses do piloto continuam não formalizadas** — nenhuma regra nova criada nesta rodada além da correção factual do café.

---

## Categorias de erro

- Promessa indevida
- Risco mal classificado
- Escalonamento errado
- Dado oficial inventado
- Tom inadequado
- Excesso de resposta
- Pergunta de dado desnecessário
- Idioma ruim
- Frase que parece execução autônoma
- Template insuficiente
- Outro

---

## Fechamento semanal

| Semana | Total de rascunhos usados | Aprovados sem ajuste | Aprovados com ajuste | Rejeitados | Escalados para Renildo | Principais temas | Principais erros | Pendências recorrentes | Casos de risco evitados | Tempo economizado estimado | Decisões de Renildo | Aprendizados aprovados | Aprendizados não aprovados | Próxima ação |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | | | | | |
