# MAPA DO CÉREBRO COMERCIAL VILLA ARÁGUA

**Natureza:** documento vivo de implementação e governança operacional do Sistema Comercial da Villa Arágua.
**Criado em:** 2026-08-05
**Última atualização:** 2026-08-05 (atualização de governança — inserção da Fase 3.5 no roadmap, ver seção 23)

---

## 1. Identidade do Mapa Comercial

- **Função:** responder onde cada conceito da Arquitetura está implementado hoje, qual arquivo manda em cada assunto, quais agentes/skills participam, e o que está pronto, parcial, divergente, ausente ou futuro.
- **Natureza de documento vivo:** este mapa muda conforme a implementação muda — mas só depois de mudança aprovada por Renildo, nunca por dedução automática.
- **Relação com o Manifesto:** o Manifesto (`MANIFESTO_DA_OPERACAO_COMERCIAL_VILLA_ARAGUA.md`) é a referência cultural e de princípios — este mapa não repete filosofia, aponta para ela.
- **Relação com a Arquitetura:** a Arquitetura (`ARQUITETURA_DO_SISTEMA_COMERCIAL_VILLA_ARAGUA.md`) é a fonte conceitual superior — em caso de conflito conceitual, a Arquitetura vence este mapa. Este mapa não redefine conceito nenhum aprovado na Arquitetura, apenas registra onde cada conceito vive hoje na implementação.
- **Relação com o Mapa do Cérebro IA:** o `MAPA_DO_CEREBRO_IA_VILLA_ARAGUA.md` cobre o ecossistema inteiro da Villa Arágua IA (atendimento, operação, marketing amplo, aprendizado). Este Mapa Comercial é um recorte específico do sistema comercial dentro daquele ecossistema — não o substitui, não o duplica, e não deve ser atualizado neste momento como consequência da criação deste mapa.
- **Limites do documento:** este mapa é inventário e diagnóstico — não cria template, não corrige cadência, não altera CRM, não conecta WhatsApp, não decide preço. Qualquer correção identificada aqui é proposta para fase futura, nunca execução imediata.

---

## 2. Estado atual do sistema comercial

**Classificação geral: parcial.**

| Camada | Classificação |
|---|---|
| Governança documental (Manifesto, Arquitetura, este Mapa) | Pronto |
| Critérios de qualificação QL (documental) | Pronto |
| Cadência e textos de follow-up (documental) | Pronto — textos QL4 e separação SLA interno/follow-up consolidados na Fase 2 (05/08/2026); divergência restante limitada à cadência própria da skill `sales-receptionist` |
| Templates de resposta comercial (Biblioteca Comercial) | Pronto |
| Registro Comercial (CRM) | Parcial — estrutura existe, campos QL/C ausentes, sem dados reais lançados |
| Integração QL → agentes/skills | Ausente |
| Integração C/N → Registro Comercial | Ausente |
| Estágios oficiais unificados | Parcial — 8 estágios definidos na Arquitetura, CRM usa vocabulário próprio de 6 status |
| Conexão real com WhatsApp | Ausente — em preparação |
| Automação | Ausente — não autorizada |

**Resumo executivo:** a Villa Arágua tem hoje uma base documental comercial madura (Manifesto, Arquitetura, Funil QL, Matriz de Follow-up, Biblioteca Comercial, Protocolo de Uso Diário) e um piloto de Modo Rascunho Assistido em andamento para atendimento (não comercial). Na Fase 2 (05/08/2026), os textos QL4 com linguagem de execução autônoma foram corrigidos no Funil e na Biblioteca de Textos QL, alinhados à Matriz de Follow-up QL, e a confusão entre SLA interno da equipe e follow-up comercial ao lead foi separada explicitamente nos três arquivos. O que falta não é mais esse conteúdo — é integração: os agentes não leem QL, o CRM não tem campos de QL/C, a skill `sales-receptionist` mantém cadência própria fora da Matriz, e existem pelo menos três vocabulários de estágio/cadência que não foram unificados. Nenhuma automação, integração de WhatsApp ou envio automático existe. O sistema está pronto para operar manualmente com qualidade, mas não está pronto para qualquer camada de automação — a classificação geral segue **parcial**, pois CRM, agentes e skills ainda não foram consolidados.

---

## 3. Arquitetura implementada hoje

```text
Origem → Produto → Qualificação QL → Classificação C/N → Agente → Skill → Template → Revisão humana → Envio manual → Registro Comercial → Follow-up → Resultado
```

| Etapa | Arquivo atual | Responsável | Status | Risco | Lacuna |
|---|---|---|---|---|---|
| Origem | Meta Ads (campanhas), WhatsApp, indicação — sem arquivo único de origem | Rene/Nubia | Parcial | Baixo | Origem não é registrada em campo padronizado desde o primeiro contato |
| Produto | `BIBLIOTECA_COMERCIAL_RECEPCIONISTA_IA_VILLA_ARAGUA.md`, regras-mãe 5 e 20 | IA sugere / Rene-Nubia confirmam | Pronto | Baixo | — |
| Qualificação QL | `FUNIL_QUALIFICACAO_LEADS_WHATSAPP_QL_VILLA_ARAGUA.md` (critérios) | Rene/Nubia (manual) | Pronto documentalmente | Médio | Nenhum agente/skill aplica QL formalmente |
| Classificação C/N | `.claude/agents/villa-orquestrador-triagem.md` | Agente orquestrador | Pronto documentalmente | Médio | Não há ponte formal entre C/N e QL — nenhum arquivo declara a relação prática |
| Agente | `villa-comercial-reservas`, `villa-orquestrador-triagem`, `villa-risco-escalacao` | IA | Pronto | Baixo | Nenhum agente cita QL, Matriz ou CRM no seu próprio arquivo |
| Skill | `villa-aragua-sales-receptionist` | IA | Parcial | Médio | Mantém cadência própria (24h/72h/7 dias), paralela à Matriz QL |
| Template | `BIBLIOTECA_COMERCIAL_RECEPCIONISTA_IA_VILLA_ARAGUA.md`, `MATRIZ_FOLLOWUP_QL_WHATSAPP_VILLA_ARAGUA.md` | Rene/Nubia | Pronto | Baixo | Duas bibliotecas de texto comercial (Biblioteca Comercial x Matriz/Biblioteca de Textos QL) sem ponte documental explícita entre si |
| Revisão humana | `PROTOCOLO_USO_DIARIO_RASCUNHO_ASSISTIDO_VILLA_ARAGUA.md` | Rene/Nubia/Renildo | Pronto | Baixo | — |
| Envio manual | Protocolo de Uso Diário, seção 3 | Rene/Nubia/Renildo | Pronto | Baixo | — |
| Registro Comercial | `CRM_LEADS_VILLA_ARAGUA.md` | Rene/Nubia | Parcial | Alto | Sem campos QL/C; auto-declarado vazio de dados reais |
| Follow-up | `MATRIZ_FOLLOWUP_QL_WHATSAPP_VILLA_ARAGUA.md` (fonte autoritativa, linha 9) | Rene/Nubia | Pronto — textos QL4 do Funil e da Biblioteca alinhados na Fase 2 (05/08/2026) | Baixo | Ver seção 9 |
| Resultado | `CRM_LEADS_VILLA_ARAGUA.md`, status "convertido"/"perdido" | Rene/Nubia/Renildo | Parcial | Baixo | Vocabulário de resultado do CRM (6 status) não corresponde 1:1 aos 8 estágios da Arquitetura |

---

## 4. Fontes oficiais atuais

| Assunto | Arquivo-fonte | Status | Precedência | Observações |
|---|---|---|---|---|
| Manifesto/princípios | `MANIFESTO_DA_OPERACAO_COMERCIAL_VILLA_ARAGUA.md` | Pronto | 1ª (cultural) | — |
| Arquitetura conceitual | `ARQUITETURA_DO_SISTEMA_COMERCIAL_VILLA_ARAGUA.md` | Pronto | 2ª (conceitual, vence este mapa) | — |
| Dados oficiais | `DADOS_OFICIAIS_ATENDIMENTO_VILLA_ARAGUA.md` | Pronto (não lido nesta rodada — citado por outras fontes) | Fonte factual | Citado por Biblioteca Comercial, Funil, Matriz |
| Critérios QL | `FUNIL_QUALIFICACAO_LEADS_WHATSAPP_QL_VILLA_ARAGUA.md` | Pronto | Fonte oficial dos critérios (seção 3-5 do arquivo) | Textos QL4 (seção 6 do arquivo) corrigidos e alinhados à Matriz na Fase 2 — 05/08/2026 (ver seção 9 deste mapa) |
| Cadência e textos de follow-up | `MATRIZ_FOLLOWUP_QL_WHATSAPP_VILLA_ARAGUA.md` | Pronto | Fonte oficial declarada (linha 9 do arquivo: "esta matriz prevalece" sobre o Funil e a Biblioteca de Textos para prazo, cadência e follow-up) | Textos QL4 corrigidos aqui; precedência reforçada na Fase 2 — 05/08/2026 |
| Biblioteca de Textos QL (base) | `BIBLIOTECA_TEXTOS_FOLLOWUP_QL_WHATSAPP_VILLA_ARAGUA.md` | Parcial | Superada pela Matriz para follow-up; ainda fonte para textos de primeira resposta | Textos QL4 (seção 5, itens 4 e 5) corrigidos e alinhados à Matriz na Fase 2 — 05/08/2026 (ver seção 9 deste mapa) |
| Templates comerciais (resposta em conversa) | `BIBLIOTECA_COMERCIAL_RECEPCIONISTA_IA_VILLA_ARAGUA.md` | Pronto | Fonte oficial de resposta dentro da conversa | Não contém templates de follow-up dedicados (ver seção 10) |
| Risco C/N | C1–C4: `ARQUITETURA_DO_SISTEMA_COMERCIAL_VILLA_ARAGUA.md`, seção 5 (canônica, propagada em 06/08/2026); N1–N4: `.claude/agents/villa-orquestrador-triagem.md` | Pronto | Fonte formal de C1-C4 é a Arquitetura; `villa-orquestrador-triagem.md` continua fonte formal de N1-N4 e consome a definição de C1-C4 da Arquitetura | — |
| Uso diário | `PROTOCOLO_USO_DIARIO_RASCUNHO_ASSISTIDO_VILLA_ARAGUA.md` | Pronto | Fonte de rotina operacional do piloto | Atualizado no Lote 11 (2026-08-05) |
| Registro comercial | `CRM_LEADS_VILLA_ARAGUA.md` | Parcial | Fonte de estado comercial | Vazio de dados reais (auto-declarado, linha 62) |
| Piloto da IA | `DIARIO_BORDO_PILOTO_RECEPCIONISTA_IA_VILLA_ARAGUA.md` | Pronto (estrutura), vazio de registros | Fonte de acompanhamento do piloto operacional | Separado do CRM por definição (seção 12 da Arquitetura) |

---

## 5. Sistema QL

- **QL1, QL2, QL3, QL4, NQ** — definidos em `FUNIL_QUALIFICACAO_LEADS_WHATSAPP_QL_VILLA_ARAGUA.md`, seção 3-4 (critérios) e seção 5 (5 perguntas de qualificação).
- **Arquivos envolvidos:** Funil QL (critérios), Matriz de Follow-up QL (cadência/textos, fonte autoritativa para follow-up), Biblioteca de Textos QL (base, parcialmente superada), `ADENDO_QUALIFICACAO_MANUAL_LEADS_7_SETEMBRO_2026_POUSADA_ARAGUA.md` (origem histórica, não lido integralmente nesta rodada).
- **Divergências existentes:**
  - **Resolvido na Fase 2 — 05/08/2026:** QL4, no Funil (seção 6) e na Biblioteca de Textos QL (seção 5, itens 4 e 5), continha frases com linguagem de execução autônoma ("já te retorno", "já te mando assim que estiver pronto", "assim que tivermos disponibilidade confirmada"). Os textos foram substituídos, alinhados à Matriz de Follow-up QL, e ambos os arquivos passaram a declarar nota de precedência apontando a Matriz como fonte oficial de cadência e follow-up (ver seção 9 deste mapa).
  - **Ativo:** cadência paralela da skill `sales-receptionist` (24h/72h/7 dias, sem diferenciar QL) — fora do escopo da Fase 2, ver seção 9 e 16.
- **Quem confirma:** hoje, na prática documentada, Rene/Nubia/Renildo usam o Funil como guia manual — não há confirmação formal registrada em campo de nenhum sistema.
- **Onde registra:** `FUNIL_QUALIFICACAO_LEADS_WHATSAPP_QL_VILLA_ARAGUA.md`, seção 12 (tabela de registro manual, com coluna "QL") e `BIBLIOTECA_TEXTOS_FOLLOWUP_QL_WHATSAPP_VILLA_ARAGUA.md`, seção 13 (tabela equivalente). **O CRM oficial (`CRM_LEADS_VILLA_ARAGUA.md`) não tem campo QL.**
- **Integração atual com agentes/skills: não encontrado na implementação atual.** Nenhum dos 7 agentes lidos (`villa-orquestrador-triagem`, `villa-comercial-reservas`, `villa-risco-escalacao`, `villa-experiencia-tom`, `villa-aprendizado-manual`, `villa-marketing-meta-ads`) menciona QL. A skill `villa-aragua-sales-receptionist` (SKILL.md) também não cita QL.

QL existe documentalmente, de forma madura e testada; agentes e skills ainda não o aplicam formalmente; qualquer integração futura depende de fase própria do roadmap (seção 21).

---

## 6. Sistema C/N

- **Fonte:** C1-C4 (comercial) — `ARQUITETURA_DO_SISTEMA_COMERCIAL_VILLA_ARAGUA.md`, seção 5, única definição canônica desde 05/08/2026, propagada em 06/08/2026 para `.claude/agents/villa-orquestrador-triagem.md` e `MATRIZ_ROTEAMENTO_AGENTES_VILLA_ARAGUA.md`. N1-N4 (operacional) — `.claude/agents/villa-orquestrador-triagem.md`, seção "Níveis de atendimento", continua única definição formal.
- **Agente responsável:** `villa-orquestrador-triagem` classifica e roteia; `villa-comercial-reservas` produz "Risco comercial:" na saída obrigatória (linha 103 do arquivo do agente), mas sem citar C1-C4 explicitamente pelo nome; `villa-risco-escalacao` atua em C4/N4.
- **Escalonamento:** `villa-risco-escalacao.md` — atua sobre "qualquer N4 ou C4" (linha 76); `PROTOCOLO_USO_DIARIO_RASCUNHO_ASSISTIDO_VILLA_ARAGUA.md`, seção 7, detalha os gatilhos obrigatórios para Renildo (desconto, reembolso, crédito, compensação, cobrança, dano, avaliação negativa etc.).
- **Relação com QL: não encontrado na implementação atual.** Nenhum arquivo (Funil, Matriz, Biblioteca, agente) declara formalmente como QL e C/N se relacionam na prática — essa relação existe hoje apenas na Arquitetura (seção 9, conceitual), ainda não implementada.
- **Uso atual:** C/N é usado no fluxo dos agentes (`villa-orquestrador-triagem` classifica toda demanda com C1-C4/N1-N4 na saída obrigatória); QL é usado apenas no processo manual descrito no Funil/Matriz, sem cruzamento com C/N em nenhum registro real.

---

## 7. Registro Comercial

**Termo conceitual usado neste mapa: Registro Comercial. Implementação atual: `CRM_LEADS_VILLA_ARAGUA.md`.**

- **Campos existentes** (19 campos, seção "Campos do lead"): Data, Nome do lead, Canal, Origem, Campanha, Produto, Período desejado, Número de adultos, Número de crianças, Perfil, Pedido principal, Orçamento enviado, Valor enviado, Objeção principal, Status, Reserva confirmada, Receita estimada, Motivo de perda, Próximo follow-up, Aprendizado.
- **Campos faltantes** (frente ao Modelo Mínimo de Informação da Arquitetura, seção 16): QL, C, Estágio (no vocabulário oficial da Arquitetura), Responsável, Canal atual de conversa, Canal de conversão/reserva.
- **Vocabulário atual de status** (6 valores): novo, respondido, em negociação, aguardando retorno, perdido, convertido.
- **Divergências com QL/C:** o CRM não tem coluna QL nem C — quem quiser cruzar QL com resultado comercial hoje precisa combinar manualmente a tabela do Funil/Matriz (que tem QL) com o CRM (que tem status/resultado), sem chave de ligação formal entre os dois.
- **Status do registro:** estrutura pronta, mas **auto-declarado vazio de leads reais** (linha 62: "o CRM ainda está vazio — nenhum lead foi inventado ou estimado para preencher esta seção"). Primeira meta prática de preenchimento era a partir de 29/07/2026 (linha 76).
- **Separação do Diário de Bordo:** confirmada — o CRM registra estado comercial do lead; o `DIARIO_BORDO_PILOTO_RECEPCIONISTA_IA_VILLA_ARAGUA.md` registra comportamento da IA no piloto de atendimento. Os dois nunca se sobrepõem hoje, conforme já estabelecido na Arquitetura (invariante da seção 12).

**Nenhuma alteração foi feita no CRM nesta rodada.**

---

## 8. Funil e estágios

Os 8 estágios aprovados na Arquitetura (seção 5):
1. Novo
2. Em qualificação
3. Orçamento
4. Aguardando retorno
5. Negociação/validação
6. Reservado
7. Perdido
8. Nutrição

- **Já existem no CRM, com outro nome:** "novo" (igual), "aguardando retorno" (igual), "em negociação" (aproxima-se de "Negociação/validação"), "perdido" (igual), "convertido" (aproxima-se de "Reservado", mas não é sinônimo exato — "convertido" no CRM exige reserva fechada confirmada, igual à regra do estágio "Reservado" da Arquitetura).
- **Não existem no CRM:** "Em qualificação", "Orçamento" e "Nutrição" como estágios distintos — hoje ficam implícitos dentro de "respondido" ou "em negociação".
- **Vocabulário paralelo:**
  - O CRM usa "respondido" como status, que não corresponde a nenhum dos 8 estágios da Arquitetura.
  - A skill `villa-aragua-campaign-analytics` (`references/funil-whatsapp-reserva.md`, linhas 17-22) usa seu **próprio** vocabulário de 4 estágios: "Lead sem resposta", "Orçamento enviado", "Pré-reserva", "Reserva confirmada" — distinto tanto do CRM quanto da Arquitetura.
  - O Funil QL e a Biblioteca de Textos QL usam apenas os níveis QL, sem estágio processual próprio — não conflitam diretamente, mas também não usam os 8 estágios da Arquitetura.
- **O que precisa ser consolidado (proposta para fase futura, não executada aqui):** unificar CRM, `campaign-analytics` e Arquitetura em um único vocabulário de estágio — hoje existem três vocabulários (CRM: 6 status; campaign-analytics: 4 estágios; Arquitetura: 8 estágios) sem ponte formal entre eles.

---

## 9. Cadência

Mapeamento dos arquivos com lógica de cadência:

| Fonte | Cadência declarada | Observação |
|---|---|---|
| `MATRIZ_FOLLOWUP_QL_WHATSAPP_VILLA_ARAGUA.md` (fonte oficial, seção 9) | QL4: 24h/48h/encerramento · QL3: 24-48h/3 dias/encerramento · QL2: 3 dias/7 dias · QL1: 7 dias (opcional) · NQ: imediato | Fonte autoritativa declarada (linha 9) |
| `FUNIL_QUALIFICACAO_LEADS_WHATSAPP_QL_VILLA_ARAGUA.md` (seção 11) | QL4: 24h/48h · QL3: 48h/nutrição leve · QL2: 3 dias/7 dias · QL1: sem prazo fixo · NQ: imediato | Compatível com a Matriz; textos QL4 (seção 6) alinhados à Matriz na Fase 2 — 05/08/2026 |
| `BIBLIOTECA_TEXTOS_FOLLOWUP_QL_WHATSAPP_VILLA_ARAGUA.md` (seção 11) | QL4: 24h/48h · QL3: 48h/3 dias · QL2: 3 dias/7 dias · QL1: 7 dias | Superada pela Matriz para follow-up (nota de precedência, linha 9 da Matriz); textos QL4 (seção 5, itens 4-5) alinhados à Matriz na Fase 2 — 05/08/2026 |
| `villa-aragua-sales-receptionist/references/follow-up.md` | 24h/72h/7 dias, genérico, sem diferenciar por QL | **Cadência paralela** — não usa QL, não referencia a Matriz |
| `villa-aragua-campaign-analytics/references/funil-whatsapp-reserva.md` (linha 11) | Cita "24h/72h/7 dias" como cadência de referência, citando o arquivo `follow-up.md` da sales-receptionist | Reforça a cadência paralela, não a Matriz QL |

**Identificação de divergências:**
- **Cadência oficial atual (para quem usa QL):** a Matriz de Follow-up QL é a fonte oficial declarada para prazo, cadência e texto de follow-up de todos os níveis QL, inclusive QL4 (nota de precedência, linha 9 da Matriz, reforçada na Fase 2 — 05/08/2026, incluindo referência explícita ao Funil, que antes não era citado na nota).
- **QL4 pós-orçamento:** significa recontato comercial ao lead depois que o orçamento foi efetivamente enviado pela equipe — é o que a Matriz descreve como "follow-up 24h após orçamento enviado" (seção 4 da Matriz). Essa definição está agora explícita no cabeçalho da própria Matriz ("Definições que valem para todo este arquivo").
- **SLA interno é alerta interno, não mensagem ao lead:** atraso da equipe em responder ou preparar o orçamento internamente gera alerta interno para Rene/Nubia/Renildo — nunca uma mensagem comercial automática ao hóspede. Essa distinção está agora explícita no Funil (seção 6), na Biblioteca de Textos QL (seção 5) e na Matriz (cabeçalho).
- **Resolvido na Fase 2 — 05/08/2026: confusão entre SLA interno e follow-up.** O Funil QL, seção 6 ("Texto padrão QL4"), usava "Follow-up 24h (se equipe ainda não respondeu)" — redação que misturava atraso interno da equipe com recontato comercial ao lead, o risco que a Arquitetura nomeia como invariante (seção 12, "SLA interno da equipe não é follow-up ao lead"). O Funil e a Biblioteca de Textos QL foram reescritos para separar as duas linhas explicitamente, na mesma direção já adotada pela Matriz.
- **Resolvido na Fase 2 — 05/08/2026: textos com linguagem de execução autônoma.** Os textos com "já te retorno", "já te mando assim que estiver pronto" e "assim que tivermos disponibilidade confirmada" foram substituídos no Funil (seção 6) e na Biblioteca de Textos QL (seção 5, itens 4-5), alinhados aos textos já corrigidos na Matriz (seção 4). Confirmado por busca textual nos três arquivos nesta rodada: nenhuma das expressões de execução autônoma remanesce.
- **Ativo: divergência QL1/QL3/QL4 de redação.** O Funil (QL3: "48h/nutrição leve") e a Biblioteca de Textos (QL3: "48h/3 dias") mantêm pequena diferença de redação na segunda etapa do QL3, sem impacto prático relevante — ambas cedem à Matriz, que declara "24h/48h (se não respondeu)/3 dias" para QL3 (seção 9 da Matriz). Não alterado nesta rodada (fora do escopo autorizado da Fase 2).
- **Ativo: cadência paralela da `sales-receptionist`.** A skill `villa-aragua-sales-receptionist` mantém 24h/72h/7 dias própria, sem diferenciar por QL — isso é exatamente o que a Arquitetura (decisão aprovada por Renildo, seção 19) determina que deve deixar de existir, mas **ainda não foi removida**; skills não fizeram parte do escopo autorizado da Fase 2.

**Nesta rodada:** nenhum novo arquivo QL foi editado — a correção de textos QL4 e a separação SLA interno/follow-up já haviam sido concluídas na Fase 2 (05/08/2026, ver seção 23); esta atualização apenas reflete, no Mapa, o estado já implementado nos três arquivos-fonte (Funil, Biblioteca, Matriz).

---

## 10. Templates

| Categoria | Fonte | Validade | Risco | Duplicação | Necessidade de ajuste |
|---|---|---|---|---|---|
| Resposta dentro da conversa | `BIBLIOTECA_COMERCIAL_RECEPCIONISTA_IA_VILLA_ARAGUA.md` (códigos `PC-EXT-01` a `PC-EXT-38`, `PC-C1` a `PC-C4`) | Válida | Baixo | Nenhuma identificada | Nenhuma |
| Follow-up | `MATRIZ_FOLLOWUP_QL_WHATSAPP_VILLA_ARAGUA.md` (fonte oficial) + `BIBLIOTECA_TEXTOS_FOLLOWUP_QL_WHATSAPP_VILLA_ARAGUA.md` (base, parcialmente superada) + `FUNIL_QUALIFICACAO_LEADS_WHATSAPP_QL_VILLA_ARAGUA.md` (critérios) | Válida — textos QL4 **corrigidos e alinhados à Matriz na Fase 2 (05/08/2026)** | Baixo | Sim, estrutural — dois/três arquivos com textos/menções de follow-up, resolvida por nota de precedência explícita nos três, não por unificação física | **Resolvido na Fase 2 — 05/08/2026:** Funil e Biblioteca-base atualizados com os textos QL4 já corrigidos na Matriz; linguagem de execução autônoma removida. Unificação física dos arquivos continua não planejada (não é objetivo desta fase) |
| Contenção | Conduzida por `villa-risco-escalacao.md`, sem template fixo próprio | Válida (por design — contenção é sempre caso a caso) | Baixo | Nenhuma | Nenhuma |
| Pós-venda | Textos genéricos dentro da Biblioteca Comercial (agradecimento/avaliação) | Válida | Baixo | Nenhuma identificada | Nenhuma |
| Reativação | `MATRIZ_FOLLOWUP_QL_WHATSAPP_VILLA_ARAGUA.md`, seção 11 ("Textos de reativação futura") — **biblioteca para consulta futura, não autoriza disparo agora** (linha 251) | Válida como referência futura | Baixo | Nenhuma | Nenhuma — já marcada corretamente como não autorizada |

---

## 11. Agentes

| Agente | Função | Entrada | Saída | Lê QL? | Lê C/N? | Consulta Registro Comercial? | Consulta Matriz? | Risco de sobreposição | Status |
|---|---|---|---|---|---|---|---|---|---|
| `villa-orquestrador-triagem` | Classifica demanda e direciona | Mensagem/dúvida | Classificação, nível, agente recomendado, C1-C4/N1-N4 | Não encontrado na implementação atual | Sim (define C/N) | Não encontrado na implementação atual | Não encontrado na implementação atual | Baixo | Pronto, sem integração QL |
| `villa-recepcionista-rascunho` | Rascunho assistido central (não lido integralmente nesta rodada) | Mensagem de hóspede/lead | Rascunho classificado | Não encontrado na implementação atual | Provável (não confirmado nesta leitura) | Não encontrado na implementação atual | Não encontrado na implementação atual | — | Não auditado nesta rodada |
| `villa-comercial-reservas` | Rascunhos comerciais seguros | Mensagem de lead | Diagnóstico, produto, dados faltantes, risco comercial, rascunho, observação para Renildo | Não encontrado na implementação atual | Cita "Risco comercial" na saída, sem nomear C1-C4 explicitamente | Não encontrado na implementação atual | Não encontrado na implementação atual | Baixo | Pronto, sem integração QL/CRM |
| `villa-risco-escalacao` | Contenção e escalação N4/C4 | Casos sensíveis | Tipo de risco, gravidade, resposta de contenção | Não encontrado na implementação atual | Sim (atua sobre C4/N4 nomeados) | Não encontrado na implementação atual | Não encontrado na implementação atual | Baixo | Pronto |
| `villa-experiencia-tom` | Revisão de tom | Mensagem já decidida | Versão revisada | Não | Não | Não | Não | Baixo | Pronto, escopo não inclui QL/C/N por design |
| `villa-aprendizado-manual` | Analisa piloto, propõe candidatos | Registros do piloto | Hipóteses de template/regra | Não encontrado na implementação atual | Não encontrado na implementação atual | Não encontrado na implementação atual | Não encontrado na implementação atual | Baixo | Pronto, sem integração QL/CRM |
| `villa-marketing-meta-ads` | Campanhas, criativos, funil Meta Ads → WhatsApp | Necessidade de campanha | Briefing, copy, público, funil de 7 etapas | Não | Não | Não | Não | Baixo | Pronto, escopo é campanha, não qualificação individual |

**Confirmação geral:** nenhum dos 7 agentes lidos cita QL, Matriz de Follow-up ou CRM/Registro Comercial em seu próprio arquivo-fonte. Todos compartilham o mesmo bloco de "Regras máximas da Villa Arágua", que já proíbe decisão de preço/desconto/reserva pela IA — essa base é consistente com os invariantes da Arquitetura.

---

## 12. Skills

| Skill | Função | Lógica própria | Sobreposição | Necessidade futura de ajuste | Status |
|---|---|---|---|---|---|
| `villa-aragua-sales-receptionist` | Atendimento/vendas WhatsApp, diagnóstico, objeção, follow-up | **Sim** — cadência própria 24h/72h/7 dias em `references/follow-up.md`, sem diferenciar QL | Sobrepõe-se à Matriz de Follow-up QL | Remover cadência própria, apontar para a Matriz (decisão já aprovada na Fase 0) | Parcial — funcional, mas com cadência paralela |
| `villa-aragua-marketing-psychology` | Psicologia de decisão do lead | Não — aplica-se a outras skills | Nenhuma | Nenhuma | Pronto |
| `villa-aragua-humanizer-pt-br` | Humanização de texto final | Não | Nenhuma | Nenhuma | Pronto |
| `villa-aragua-skill-router` | Orquestra qual skill usar | Lista fixa de skills no próprio arquivo | **Desatualizada** — lista 11 skills (SKILL.md, linha 9-21), mas o diretório `.claude/skills/` contém 16 (faltam `campaign-learning-register`, `campaign-preflight-checklist`, `meta-business-security-audit`, `villa-financial-five-boxes-classifier`, e a própria `villa-aragua-skill-router` não se autolista) | Risco de roteamento incompleto | Atualizar a lista de 11 para o total real (fase futura) | Parcial |
| `villa-aragua-campaign-analytics` | Análise de campanha, funil, ROAS/CPA/CPL | **Sim** — vocabulário próprio de 4 estágios em `references/funil-whatsapp-reserva.md` (linhas 17-22): "Lead sem resposta", "Orçamento enviado", "Pré-reserva", "Reserva confirmada" | Sobrepõe-se aos 8 estágios da Arquitetura e aos 6 status do CRM | Passar a usar o vocabulário oficial do CRM/Arquitetura (decisão já aprovada na Fase 0) | Parcial — funcional, mas com vocabulário paralelo |
| `villa-aragua-growth-marketer` | Coordenação estratégica de crescimento, reativação | Não teria cadência própria identificada nesta rodada (não lida integralmente) | Não auditado nesta rodada | — | Não auditado integralmente nesta rodada |

---

## 13. Humanos

| Pessoa | Permissões | Limites | Responsabilidades | Escalonamento |
|---|---|---|---|---|
| **Rene** | Revisa e envia N1/N2/comercial simples dentro dos templates; confirma/corrige QL (conceitual, Arquitetura seção 14) | Não decide preço, desconto, exceção, cobrança, dano, avaliação | Primeira linha, registra no CRM/Diário de Bordo | Escala para Renildo em casos sensíveis (Protocolo, seção 7) |
| **Nubia** | Mesmas permissões de Rene | Mesmos limites de Rene | Substituta integral de Rene | Mesma regra de Rene |
| **Renildo** | Decide tudo, incluindo exceções; aprova mudanças estruturais | — | Governança, decisão financeira/reputacional, decisão C3/C4 sensível | É o destino final da escalada — não escala para ninguém |

Fonte: `PROTOCOLO_USO_DIARIO_RASCUNHO_ASSISTIDO_VILLA_ARAGUA.md`, seção 4; `MANIFESTO_DA_OPERACAO_COMERCIAL_VILLA_ARAGUA.md`, seção 8; `ARQUITETURA_DO_SISTEMA_COMERCIAL_VILLA_ARAGUA.md`, seção 14.

---

## 14. Meta Ads e entrada de leads

- **Origem Meta Ads:** campanhas planejadas via agente `villa-marketing-meta-ads` e skill `villa-aragua-campaign-analytics`; nenhuma campanha real foi lida/auditada nesta rodada.
- **Campanha/anúncio:** vocabulário de status definido em `villa-marketing-meta-ads.md` ("rascunho", "publicada", "em análise", "ativa", "pausada", "encerrada", "histórica/obsoleta").
- **Canal de entrada:** WhatsApp é o canal principal de conversa comercial hoje, segundo todas as fontes lidas (Funil QL, Matriz, Biblioteca Comercial).
- **Conexão atual com WhatsApp: manual.** Não encontrado na implementação atual nenhuma integração técnica ativa (API, Zapier, Make, ManyChat) — todos os arquivos (Funil, Matriz, Biblioteca) declaram explicitamente "sem automação ativa", "sem ManyChat", "sem CAPI".
- **Estado manual atual:** confirmado pelo Manifesto (seção 9) e pelo contexto operacional já fornecido por Renildo — campanhas entrando, atendimento manual, conexão em preparação (5 a 10 dias, sem data rígida registrada em arquivo).
- **Preparação futura:** Fase 3/4 descritas no Funil QL (seção 14) e na Matriz (seção 13) — semi-automação (ManyChat) e automação controlada, **nenhuma autorizada além da Fase 1/2 (manual/assistida) hoje**.

**Não assumido que a conexão já está pronta** — todas as fontes confirmam que ainda não está.

---

## 15. WhatsApp

- **Situação atual: manual**, confirmada em todas as fontes lidas (Manifesto, Protocolo de Uso Diário, Funil QL, Matriz).
- **Integração em preparação:** confirmado pelo contexto operacional fornecido por Renildo nesta fase (negociação técnica em andamento) — nenhum arquivo do projeto ainda documenta essa integração como concluída ou com data fixa.
- **Modo Rascunho Assistido:** confirmado como modo vigente em todos os arquivos centrais (`PROTOCOLO_USO_DIARIO_RASCUNHO_ASSISTIDO_VILLA_ARAGUA.md`, seção 3: "A IA só ajuda a escrever. A IA não decide. A IA não envia.").
- **Nenhum envio automático:** confirmado — regra explícita em todas as fontes.
- **Nenhuma confirmação automática:** confirmado — regra explícita em todas as fontes.
- **Requisitos mínimos antes da conexão** (inferência a partir do roadmap já existente no Funil/Matriz, seção "Futuro com IA"/"Preparação para IA assistida futura"): consolidar cadência única (resolver divergência da seção 9 deste mapa), validar tom/consentimento/LGPD, e só então avançar para Fase 3 (semi-automação) — nenhuma dessas condições está marcada como cumprida hoje.

---

## 16. Divergências conhecidas

1. **Cadência paralela na skill `sales-receptionist`** — **Ativo.** `references/follow-up.md` usa 24h/72h/7 dias fixo, sem diferenciar QL, ignorando a Matriz. Fora do escopo autorizado da Fase 2 (skills não alteradas).
2. **QL sem integração** — **Ativo.** Nenhum agente ou skill lê ou aplica QL formalmente (seção 5 e 11 deste mapa). **Futuro — depende de aprovação de Renildo** (Fase 4 do roadmap, seção 21).
3. **CRM sem QL/C** — **Ativo.** `CRM_LEADS_VILLA_ARAGUA.md` não tem essas colunas (seção 7 deste mapa). **Futuro — depende de aprovação de Renildo** (Fase 3 do roadmap, seção 21).
4. **`campaign-analytics` com estágios próprios** — **Ativo.** Vocabulário de 4 estágios, distinto do CRM (6 status) e da Arquitetura (8 estágios) (seção 8 e 12 deste mapa). **Futuro — depende de aprovação de Renildo** (Fase 5 do roadmap, seção 21).
5. **`skill-router` desatualizado** — **Ativo.** Lista 11 skills, existem 16 no diretório (seção 12 deste mapa). **Futuro — depende de aprovação de Renildo** (Fase 5 do roadmap, seção 21).
6. **Textos QL4 antigos** — **Resolvido na Fase 2 — 05/08/2026.** Linguagem de execução autônoma removida do Funil QL (seção 6) e da Biblioteca de Textos QL (seção 5, itens 4-5), alinhados aos textos já corrigidos na Matriz (seção 9 deste mapa). Confirmado por busca textual nos três arquivos: nenhuma expressão de execução autônoma remanesce.
7. **Vocabulários paralelos de estágio/status** — **Ativo.** CRM (6 status), `campaign-analytics` (4 estágios), Arquitetura (8 estágios) — três vocabulários não unificados (seção 8 deste mapa). **Futuro — depende de aprovação de Renildo** (Fase 5 do roadmap, seção 21).
8. **Confusão parcial entre SLA interno e follow-up** — **Resolvido na Fase 2 — 05/08/2026.** A redação do Funil QL (seção 6) que misturava "Follow-up 24h (se equipe ainda não respondeu)" foi separada em duas linhas explícitas — SLA interno da equipe (alerta interno) e follow-up comercial ao lead (só após orçamento enviado) — na mesma direção já adotada pela Matriz (seção 9 deste mapa).

---

## 17. Riscos atuais

| Risco | Categoria | Severidade |
|---|---|---|
| Cadência paralela da skill `sales-receptionist` (fora do sistema QL) pode gerar mensagem inconsistente se dois atendentes usarem fontes diferentes | Comercial | Médio (reduzido de Alto — divergência dentro do sistema QL já resolvida na Fase 2, 05/08/2026; risco residual limitado à skill fora do escopo desta fase) |
| CRM sem QL/C impede leitura cruzada de maturidade x resultado | Documental/Registro | Alto |
| **Resolvido na Fase 2 — 05/08/2026:** textos QL4 antigos (execução autônoma) existiam no Funil e na Biblioteca de Textos QL — substituídos e alinhados à Matriz; confusão entre SLA interno e follow-up também separada nos mesmos arquivos | Comercial | Resolvido |
| `skill-router` desatualizado pode rotear incorretamente para skill inexistente na lista | Técnico/Documental | Médio |
| `campaign-analytics` com vocabulário próprio de estágio dificulta relatório único de funil | Documental | Médio |
| CRM vazio de dados reais compromete qualquer análise de funil até que passe a ser alimentado | Operacional | Alto |
| Nenhuma automação existe — risco de automação prematura é hoje baixo, mas deve ser vigiado conforme a integração WhatsApp avança | Automação | Baixo |
| Processo QL/C/N/CRM ainda é conceitualmente rico demais para uso 100% manual sem confusão — risco de complexidade para Rene/Nubia se tudo for exigido de uma vez | Complexidade para Rene/Nubia | Médio |

---

## 18. O que já está pronto

- Manifesto da Operação Comercial.
- Arquitetura do Sistema Comercial.
- Este Mapa Comercial (inventário).
- Biblioteca Comercial da Recepcionista IA (`PC-EXT-01` a `38`, `PC-C1` a `C4`).
- Biblioteca Oficial da Recepcionista IA (operacional, 90 templates + regras transversais).
- Protocolo de Uso Diário do Rascunho Assistido (atualizado no Lote 11).
- Diário de Bordo do Piloto (estrutura criada, aguardando uso real).
- Sete agentes especialistas (`villa-orquestrador-triagem`, `villa-recepcionista-rascunho`, `villa-comercial-reservas`, `villa-risco-escalacao`, `villa-experiencia-tom`, `villa-aprendizado-manual`, `villa-marketing-meta-ads`).
- Dezesseis skills no ecossistema (`.claude/skills/`).
- Funil QL documental (critérios e perguntas de qualificação).
- Matriz de Follow-up QL (cadência e textos, já revisada por 7 skills formais).
- Modo Rascunho Assistido, com teste cego aprovado (Lote 10, 30/30 casos).
- Textos QL4 alinhados no Funil e na Biblioteca de Textos QL, sem linguagem de execução autônoma — Fase 2, 05/08/2026.
- Precedência da Matriz formalizada explicitamente no cabeçalho dos três arquivos QL (Funil, Biblioteca, Matriz) — Fase 2, 05/08/2026.
- SLA interno da equipe separado do follow-up comercial ao lead, com definição explícita nos três arquivos QL — Fase 2, 05/08/2026.
- Linguagem de execução autônoma ("já te retorno", "já te mando", "assim que tivermos disponibilidade confirmada" e equivalentes) removida dos arquivos QL revisados — Fase 2, 05/08/2026.

---

## 19. O que está parcial

- Integração QL ↔ agentes (documentado, não aplicado por nenhum agente).
- Registro Comercial/CRM (estrutura pronta, campos QL/C ausentes, sem dados reais lançados).
- Cadência unificada — textos QL4 do Funil e da Biblioteca de Textos QL já alinhados à Matriz (Fase 2, 05/08/2026); ainda pendente: a skill `sales-receptionist` mantém cadência própria (24h/72h/7 dias), fora do escopo desta fase.
- Estágios oficiais (definidos na Arquitetura, mas três vocabulários distintos coexistem: CRM, `campaign-analytics`, Arquitetura).
- Conexão WhatsApp (em negociação, sem data documentada em arquivo).
- Métricas (conceitualmente definidas na Arquitetura, seção 17; sem fórmula de cálculo nem dado real ainda, por depender do CRM alimentado).

---

## 20. O que ainda não existe

- Integração real com WhatsApp (API, Zapier, Make, ManyChat) — **não encontrado na implementação atual**.
- Qualquer automação de envio — **não encontrado na implementação atual**; explicitamente proibida em todas as fontes lidas.
- Banco de disponibilidade integrado (Stays ou equivalente conectado ao fluxo comercial) — **não encontrado na implementação atual**.
- CRM integrado com QL/C — **não encontrado na implementação atual**.
- Agentes lendo QL — **não encontrado na implementação atual**.
- Skills usando o vocabulário oficial de estágio (CRM/Arquitetura) — **não encontrado na implementação atual**; `campaign-analytics` usa vocabulário próprio.

---

## 21. Roadmap de consolidação

**Princípios do roadmap:**
- **Nenhum agente, skill ou automação poderá assumir oficialmente o Registro Comercial antes da conclusão da Fase 3.5.**

| Fase | Objetivo | Arquivos afetados | Risco | Dependência | Critério de conclusão | Aprovação de Renildo |
|---|---|---|---|---|---|---|
| 1. Governança documental | Consolidar Manifesto, Arquitetura, este Mapa | Nenhum arquivo além dos 3 já criados | Baixo | Nenhuma | Os 3 documentos existirem e estarem alinhados | ✅ **Concluída** (05/08/2026) |
| 2. Consolidação de Cadência e Textos QL | Corrigir textos QL4 antigos, unificar cadência documental do sistema QL (Funil, Biblioteca, Matriz), remover cadência própria da `sales-receptionist` | Funil QL, Biblioteca de Textos QL, Matriz de Follow-up QL, `sales-receptionist/references/follow-up.md` | Médio | Fase 1 concluída | Textos e cadência únicos, sem divergência registrada | ✅ **Concluída em 05/08/2026 — escopo documental do sistema QL** (Funil, Biblioteca, Matriz: textos QL4 corrigidos, SLA interno separado de follow-up, precedência da Matriz formalizada). A remoção da cadência própria da skill `sales-receptionist` **não foi executada** — skills ficaram fora do escopo autorizado desta fase e permanecem como divergência ativa (seção 16, item 1) |
| 3. Registro Comercial mínimo | Adicionar campos QL/C/estágio oficial ao Registro Comercial | `CRM_LEADS_VILLA_ARAGUA.md` | Alto (mexe em fonte viva) | Fase 2 concluída | Registro Comercial com campos mínimos definidos na Arquitetura (seção 16) | ✅ **Concluída em 05/08/2026** — estrutura ajustada em `CRM_LEADS_VILLA_ARAGUA.md` (ID, QL, C, Estágio oficial, Último contato, Próxima ação, Responsável, Precisa de Renildo? e demais campos mínimos aprovados); ainda vazio de dados reais. *Nota: as seções 2, 7, 16, 19 e 20 deste mapa ainda não foram atualizadas para refletir esta conclusão — reconciliação completa do mapa fica para rodada futura dedicada (fora do escopo desta atualização de governança).* |
| 3.5. Piloto Operacional do Registro Comercial | Validar o Registro Comercial em operação real — pessoas e processo, **não** IA, automação, WhatsApp, agentes ou skills — antes de ensinar agentes/skills ou iniciar integrações. Ver detalhamento completo abaixo da tabela | `CRM_LEADS_VILLA_ARAGUA.md` (uso diário; estrutura não é alterada nesta fase) | Baixo | Fase 3 concluída | Rene preenche naturalmente; Nubia opera sem necessidade constante de ajuda; Renildo confirma que o Registro Comercial ajuda a tomada de decisão; sem necessidade de mudanças estruturais importantes | ⏳ **Inserida nesta rodada (05/08/2026) — em andamento, depende de confirmação de Renildo ao final do piloto (~1 semana ou 20-30 leads reais)** |
| 4. Aprendizado dos Agentes | Ensinar agentes a ler/sugerir QL — os agentes passam a **aprender uma arquitetura já consolidada**, não a definir regra nova | `villa-orquestrador-triagem`, `villa-comercial-reservas` | Médio | **Fase 3.5 concluída** | Agentes citam QL na saída obrigatória | **Futuro — depende de aprovação de Renildo; bloqueada até a Fase 3.5 concluir (ver Princípios do roadmap, acima)** |
| 5. Aprendizado das Skills | `campaign-analytics` passa a usar estágio oficial; `skill-router` atualizado — as skills passam a **aprender uma arquitetura já consolidada**, não a definir regra nova | `campaign-analytics/references/funil-whatsapp-reserva.md`, `skill-router/SKILL.md` | Baixo | **Fase 3.5 concluída** | Vocabulário único em uso | **Futuro — depende de aprovação de Renildo; bloqueada até a Fase 3.5 concluir (ver Princípios do roadmap, acima)** |
| 6. Integração WhatsApp (Modo Rascunho Assistido) | Conectar WhatsApp mantendo o Modo Rascunho Assistido — revisão humana sempre presente, nenhum envio automático | Fora do escopo documental — decisão técnica | Alto | Fases 4 e 5 concluídas | Decisão explícita de Renildo, sempre em Modo Rascunho Assistido | **Futuro — depende de aprovação de Renildo** |
| 7. Métricas e Indicadores | Ativar, com fórmula de cálculo, as métricas já conceituadas na Arquitetura (seção 17) a partir de dados reais do Registro Comercial | `CRM_LEADS_VILLA_ARAGUA.md` (leitura) | Baixo | Fase 6 concluída | Métricas calculadas a partir de dados reais, revisadas na rotina semanal | **Futuro — depende de aprovação de Renildo** |
| 8. Automações futuras | Qualquer automação de envio ou integração técnica adicional | Fora do escopo documental — decisão técnica | Alto | Fase 7 concluída | Somente após nova decisão de governança explícita de Renildo | **Futuro — depende de aprovação de Renildo; não autorizada nesta rodada nem em nenhuma anterior** |

**Nota sobre fases removidas do roadmap anterior:** as antigas Fases 6 ("Testes" — lote cego QL+C) e 7 ("Piloto comercial manual") do roadmap de 8 fases não aparecem mais como fases isoladas nesta atualização, a pedido explícito de Renildo. Conceitualmente, a validação de uso permanece coberta pela nova Fase 3.5 (piloto do Registro Comercial) e, futuramente, por qualquer teste que as Fases 4 e 5 (Aprendizado dos Agentes/Skills) exijam antes de sua própria conclusão — nada do conteúdo dessas fases antigas foi descartado como ideia, apenas reorganizado dentro da nova estrutura de 9 fases.

### Fase 3.5 — Piloto Operacional do Registro Comercial (detalhamento)

**Missão:** validar o Registro Comercial em operação real antes de ensinar agentes, skills ou iniciar integrações.

**Princípios:**
- Esta fase existe para validar **pessoas e processo**.
- Ela **não** existe para validar IA.
- Ela **não** existe para validar automação.
- Ela **não** existe para validar WhatsApp.
- Ela **não** existe para validar agentes.
- Ela **não** existe para validar skills.
- O objetivo é confirmar que Rene, Nubia e Renildo conseguem utilizar o Registro Comercial de forma simples, consistente e útil durante o atendimento real.

**Objetivos — validar:**
- tempo de preenchimento;
- clareza dos campos;
- facilidade de uso;
- entendimento dos 8 estágios;
- entendimento de QL;
- entendimento de C;
- facilidade do follow-up;
- qualidade das informações registradas;
- aderência à rotina diária.

**O que observar** (durante aproximadamente uma semana ou 20-30 leads reais), registrar:
- quais campos sempre são preenchidos;
- quais campos quase nunca são usados;
- quais campos confundem;
- quais campos fazem falta;
- quais campos podem virar sugestão automática da IA;
- quais campos devem permanecer exclusivamente humanos.

**Critério de aprovação:** a Fase 3.5 será considerada concluída quando:
- Rene conseguir preencher naturalmente;
- Nubia conseguir operar sem necessidade constante de ajuda;
- Renildo confirmar que o Registro Comercial ajuda a tomada de decisão;
- não houver necessidade de mudanças estruturais importantes.

**Enquanto isso não acontecer:**
- agentes **não** serão alterados;
- skills **não** serão alteradas;
- automações **não** serão iniciadas;
- integração do WhatsApp continuará em Modo Rascunho Assistido.

---

## 22. Regras de atualização do mapa

- Este é um **documento vivo** — reflete o estado real da implementação, não um plano.
- Atualização **somente após mudança aprovada** por Renildo — nunca por dedução automática da IA.
- **Changelog próprio** deste mapa (seção 23), independente do changelog da Arquitetura (que já declara ter changelog separado, seção 22 da Arquitetura).
- **Não altera a Arquitetura por consequência automática** — se uma implementação mudar, este mapa é atualizado; a Arquitetura só muda por decisão conceitual explícita de Renildo.
- **Não apaga histórico** — mudanças viram nova entrada de changelog, não substituição silenciosa de conteúdo anterior.
- **Não duplica fontes** — este mapa sempre aponta para o arquivo oficial (Funil, Matriz, Biblioteca, CRM, agentes, skills), nunca copia o conteúdo integral deles.
- **Marcação obrigatória de status:** todo item deste mapa deve ser classificado como pronto / parcial / divergente / ausente / futuro, conforme já aplicado nas seções acima.

---

## 23. Changelog

- **2026-08-05 — Claude (a pedido de Renildo):** criação do Mapa do Cérebro Comercial, como inventário vivo da implementação atual do Sistema Comercial da Villa Arágua, após leitura integral de `MANIFESTO_DA_OPERACAO_COMERCIAL_VILLA_ARAGUA.md`, `ARQUITETURA_DO_SISTEMA_COMERCIAL_VILLA_ARAGUA.md`, `MAPA_DO_CEREBRO_IA_VILLA_ARAGUA.md` (referenciado, não citado linha a linha nesta rodada), `FUNIL_QUALIFICACAO_LEADS_WHATSAPP_QL_VILLA_ARAGUA.md`, `MATRIZ_FOLLOWUP_QL_WHATSAPP_VILLA_ARAGUA.md`, `BIBLIOTECA_TEXTOS_FOLLOWUP_QL_WHATSAPP_VILLA_ARAGUA.md`, `BIBLIOTECA_COMERCIAL_RECEPCIONISTA_IA_VILLA_ARAGUA.md`, `CRM_LEADS_VILLA_ARAGUA.md`, `PROTOCOLO_USO_DIARIO_RASCUNHO_ASSISTIDO_VILLA_ARAGUA.md`, `DIARIO_BORDO_PILOTO_RECEPCIONISTA_IA_VILLA_ARAGUA.md`, agentes relevantes em `.claude/agents/` e skills relevantes em `.claude/skills/`. Nenhum desses arquivos foi alterado nesta rodada.
- **2026-08-05 — Claude (a pedido de Renildo):** atualização deste Mapa pós-Fase 2 (Consolidação de Cadência e Textos QL). Resumo: (1) textos QL4 com linguagem de execução autônoma foram corrigidos no Funil (seção 6) e na Biblioteca de Textos QL (seção 5, itens 4-5); (2) Funil e Biblioteca de Textos QL foram alinhados aos textos já corrigidos na Matriz de Follow-up QL; (3) SLA interno da equipe separado explicitamente de follow-up comercial ao lead nos três arquivos QL; (4) precedência da Matriz reforçada no cabeçalho dos três arquivos, incluindo definição explícita de QL4 pós-orçamento (recontato só após orçamento efetivamente enviado); (5) seções 2, 3, 4, 5, 9, 10, 16, 17, 18, 19 e 21 deste mapa atualizadas para refletir o novo estado, com itens resolvidos marcados como tal sem apagar histórico. Divergências fora do escopo desta fase (cadência própria da `sales-receptionist`, QL sem integração com agentes, CRM sem QL/C, `campaign-analytics` com estágios próprios, `skill-router` desatualizado, vocabulários paralelos de estágio) permanecem ativas. Fase 3 não foi iniciada. Arquivos-fonte envolvidos (já alterados na Fase 2, nesta rodada apenas confirmados por leitura): `FUNIL_QUALIFICACAO_LEADS_WHATSAPP_QL_VILLA_ARAGUA.md`, `BIBLIOTECA_TEXTOS_FOLLOWUP_QL_WHATSAPP_VILLA_ARAGUA.md`, `MATRIZ_FOLLOWUP_QL_WHATSAPP_VILLA_ARAGUA.md`. Backup deste mapa criado em `BACKUP_ANTES_ATUALIZACAO_MAPA_POS_FASE2_2026-08-05/` antes da edição. Nenhum outro arquivo do projeto foi alterado nesta rodada. Aprovação: Renildo.
- **2026-08-05 — Claude (a pedido de Renildo):** atualização de governança do roadmap (seção 21). Resumo: (1) inserida oficialmente a nova **Fase 3.5 — Piloto Operacional do Registro Comercial**, entre a Fase 3 e a Fase 4, com missão, princípios (o que ela não valida: IA, automação, WhatsApp, agentes, skills), objetivos de validação, itens a observar (~1 semana ou 20-30 leads reais) e critério de aprovação explícitos; (2) roadmap reorganizado de 8 para 9 fases — Fases 1, 2 e 3 marcadas ✅ concluídas; as antigas Fases 6 ("Testes") e 7 ("Piloto comercial manual") deixaram de existir como fases isoladas, com nota explicando a reorganização sem descartar o conteúdo conceitual; novas Fases 6 (Integração WhatsApp), 7 (Métricas e Indicadores) e 8 (Automações futuras) definidas; (3) ajuste de filosofia: "Agentes"/"Atualizar agentes" renomeado para **"Aprendizado dos Agentes"**, e "Skills"/"Atualizar Skills" para **"Aprendizado das Skills"**, com nota de que os agentes/skills passam a aprender uma arquitetura já consolidada, não a definir regra nova; (4) nova regra de princípio adicionada à seção 21: "Nenhum agente, skill ou automação poderá assumir oficialmente o Registro Comercial antes da conclusão da Fase 3.5" — as Fases 4 e 5 agora dependem explicitamente da Fase 3.5 concluída, não mais da Fase 3. **Escopo desta rodada:** somente a seção 21 (Roadmap) e este changelog foram alterados — as seções 2, 7, 16, 19 e 20 deste mapa ainda refletem o estado pré-conclusão da Fase 3 e não foram reconciliadas nesta rodada (fora do escopo desta atualização de governança, sinalizado como próximo passo). Nenhum outro arquivo do projeto foi lido ou alterado nesta rodada — apenas este Mapa. Backup criado em `BACKUP_ANTES_FASE3.5_GOVERNANCA_MAPA_2026-08-05/` antes da edição. Aprovação: Renildo.
- **2026-08-06 — Claude (a pedido de Renildo):** propagação da definição canônica de C1–C4 (Auditoria do Piloto Comercial Real de 06/08/2026, frente A). Resumo: (1) seção 4 ("Fontes oficiais atuais"), linha "Risco C/N" — corrigida para apontar `ARQUITETURA_DO_SISTEMA_COMERCIAL_VILLA_ARAGUA.md`, seção 5, como fonte formal de C1-C4 (antes apontava só o Orquestrador), preservando `villa-orquestrador-triagem.md` como fonte formal de N1-N4; (2) seção 6 ("Sistema C/N"), linha "Fonte" — mesma correção, com nota de que a propagação ocorreu em 06/08/2026 para `villa-orquestrador-triagem.md` e `MATRIZ_ROTEAMENTO_AGENTES_VILLA_ARAGUA.md`. Nenhuma outra seção deste mapa foi alterada nesta rodada — a reconciliação completa das seções 2, 7, 16, 19 e 20 (já sinalizada como pendente desde 05/08/2026) continua fora do escopo aprovado. Arquivos-fonte efetivamente editados nesta rodada (fora deste mapa): `MATRIZ_ROTEAMENTO_AGENTES_VILLA_ARAGUA.md`, `.claude/agents/villa-orquestrador-triagem.md`, `.claude/agents/villa-recepcionista-rascunho.md`, `teste_regressao_biblioteca_comercial.py`, `MAPA_DO_CEREBRO_IA_VILLA_ARAGUA.md` (seção 23), `TEMPLATES_OPERACIONAIS_QL_C_VILLA_ARAGUA.md`, `DIARIO_BORDO_PILOTO_RECEPCIONISTA_IA_VILLA_ARAGUA.md`. Backup de todos criado em `BACKUP_ANTES_PROPAGACAO_C1C4_PRIMEIRA_MENSAGEM_2026-08-06/` antes da edição. Aprovação: Renildo.
