# Funil de Qualificação de Leads WhatsApp — Villa Arágua

**Natureza deste arquivo:** processo comercial para o atendimento no WhatsApp da Villa Arágua, transformando a classificação QL1–QL4/NQ (já registrada em `ADENDO_QUALIFICACAO_MANUAL_LEADS_7_SETEMBRO_2026_POUSADA_ARAGUA.md`) em um funil prático, com textos padrão, prioridade e cadência de follow-up. Este arquivo não cria automação, não altera WhatsApp, não altera Meta Ads, não instala ManyChat, não cria integração, não envia mensagem automaticamente e não substitui Rene/Nubia.

**Gerado em:** 2026-07-18
**Base:** `ADENDO_QUALIFICACAO_MANUAL_LEADS_7_SETEMBRO_2026_POUSADA_ARAGUA.md`, `BIBLIOTECA_COMERCIAL_RECEPCIONISTA_IA_VILLA_ARAGUA.md`

**Atualizado em 05/08/2026 — Ajuste Operacional Pré-Piloto:** Produto incluído como etapa formal de qualificação; regra explícita de não repetir dado já informado; critérios QL2/QL3/QL4 objetivados; tabela de registro paralela (antiga seção 12) substituída por referência ao Registro Comercial oficial (`CRM_LEADS_VILLA_ARAGUA.md`); pontes adicionadas para Arquitetura, Matriz, Guia, Biblioteca e Protocolo. Nenhuma definição de C, Estágio, ativo ou cadência foi duplicada ou redefinida. Ver seção 19 (Changelog).

**Nota sobre produto:** este processo é geral para a Villa Arágua (Pousada e Casa). As perguntas de qualificação (seção 5) ajudam a identificar qual produto o lead busca — a partir daí, cada resposta deve usar **somente** as informações do produto certo (Pousada ou Casa), nunca misturando amenities dos dois na mesma mensagem, conforme já estabelecido na arquitetura do Marketing & Meta Ads IA.

---

## 1. Status

- Processo comercial manual/assistido.
- Sem automação ativa.
- Sem ManyChat configurado.
- Sem CAPI instalada.
- Sem envio automático.
- Uso inicial por Rene/Nubia/Renildo como apoio de atendimento.

---

## 2. Objetivo do funil

- Diferenciar curioso de lead qualificado.
- Reduzir tempo perdido no WhatsApp com conversas sem intenção real.
- Aumentar a qualidade dos orçamentos enviados.
- Melhorar a leitura de desempenho da campanha (o que converte de verdade, não só o que gera clique).
- Criar base de aprendizado real para uma futura automação segura, se e quando aprovada.

---

## 3. Classificação dos leads — critérios objetivos

**Três dados essenciais** passam a organizar a fronteira entre níveis: **Datas, Número de pessoas e Produto**.

**Campo Produto (novo, formal a partir de 05/08/2026):**
- Pousada Arágua
- Casa Arágua Mariscal
- Indefinido

- **QL4** — Produto + Datas + Número de pessoas confirmados, com pedido explícito de orçamento ou intenção clara de avançar. Orçamento final só depois da conferência humana.
- **QL3** — Falta apenas um dos três dados essenciais (tipicamente Produto), ou existe uma dúvida objetiva pontual. Datas + Número de pessoas conhecidos, mas Produto indefinido, também entram em QL3 — com a próxima ação obrigatória de identificar o Produto (ver seção 5).
- **QL2** — Faltam dois ou mais dos três dados essenciais; demonstra pesquisa ativa (pergunta preço, estrutura, fotos ou produto). Pergunta normal de preço sem nenhum dado informado entra em QL2, não em QL1.
- **QL1** — Nenhum dos três dados essenciais informado; intenção vaga ou interação muito inicial (ex.: só "Oi").
- **NQ** — Fora do perfil, spam, ou incompatibilidade real confirmada — nunca presumida. Silêncio, isoladamente, não é critério de NQ (ver seção 11).

**Regras de transição que não mudam QL:**
- Silêncio não reduz QL automaticamente — silêncio muda o Estágio para "Aguardando retorno" no Registro Comercial, nunca o QL por si só.
- Pedido de desconto não muda QL — muda C para C3, conforme `ARQUITETURA_DO_SISTEMA_COMERCIAL_VILLA_ARAGUA.md`, seção 5. Este Funil não decide isso, apenas aponta (ver seção 13).
- Reclamação grave interrompe o fluxo normal de qualificação por C4 (mesma fonte), sem apagar o último Estágio conhecido do lead.

**Não usar C1–C4 dentro deste Funil** — essa classificação de risco pertence a `ARQUITETURA_DO_SISTEMA_COMERCIAL_VILLA_ARAGUA.md` (seção 5), aplicada em conjunto com a Biblioteca Comercial da Recepcionista IA. QL1–QL4/NQ é uma camada diferente: qualificação de intenção/maturidade, não classificação de risco da mensagem. QL e C são independentes — um lead QL4 pode gerar uma mensagem C1; um lead QL1 pode gerar uma mensagem C4.

---

## 4. Critérios por nível (objetivos)

Dados essenciais contados objetivamente: **Datas, Número de pessoas, Produto** (3 no total).

| Nível | Critério objetivo | Dados essenciais confirmados | Prioridade | Ação |
|---|---|---|---|---|
| QL4 | Produto + Datas + Pessoas confirmados, e pedido explícito de orçamento ou intenção clara de avançar | 3 de 3 | Alta | Encaminhar para conferência humana (Rene/Nubia) com resumo pronto |
| QL3 | Falta apenas 1 dos 3 dados essenciais (tipicamente Produto), ou existe 1 dúvida objetiva pontual | 2 de 3 | Média-alta | Identificar o dado faltante (ação obrigatória) antes de orçamento |
| QL2 | Faltam 2 ou mais dos 3 dados essenciais; demonstra pesquisa ativa (pergunta preço/estrutura/fotos/produto) | 0-1 de 3 | Média | Qualificar com informação, sem pressionar |
| QL1 | Nenhum dos 3 dados essenciais informado; intenção vaga ou só abertura | 0 de 3 | Baixa | Resposta leve, sem consumir tempo comercial |
| NQ | Fora do perfil, spam, ou incompatibilidade real confirmada (não presumida) | Não se aplica | Nenhuma | Resposta educada e encerramento |

**Nota:** pergunta normal de preço sem nenhum dado informado conta como QL2 (demonstra pesquisa ativa), não QL1 — mesmo com 0 de 3 dados essenciais confirmados, a intenção de pesquisa de preço já é sinal de QL2. Esta nota resolve, dentro deste Funil, a ambiguidade identificada na auditoria operacional de 05/08/2026 entre este arquivo e `MATRIZ_FOLLOWUP_QL_WHATSAPP_VILLA_ARAGUA.md`.

---

## 5. Lógica de qualificação (não é script rígido)

**Regra de não repetição (obrigatória, sempre válida):**

> Nunca repetir pergunta sobre informação que o lead já forneceu. Antes de responder, identificar o que já está conhecido e perguntar apenas o próximo dado realmente necessário.

Exemplos: já informou datas → não perguntar datas · já informou pessoas → não perguntar pessoas · já citou a Casa → não perguntar Pousada ou Casa · já informou criança → não perguntar se haverá criança · já pediu orçamento com dados completos → não reiniciar qualificação.

**Sequência operacional (lógica, não roteiro fixo):**

1. Ler o que o lead já informou.
2. Identificar o primeiro dado realmente faltante entre os três dados essenciais: Datas, Número de pessoas, Produto.
3. Confirmar o dado faltante — uma pergunta principal por mensagem em QL1 e início de QL2:
   - Datas: "Oi! Que bom te ver por aqui 😊 Pra eu te ajudar certinho, me conta: quais datas vocês estão pensando?"
   - Número de pessoas: "Quantas pessoas seriam?"
   - Produto, quando Datas e Número de pessoas já estão confirmados: **"Vocês estão considerando a Pousada Arágua ou a Casa Arágua Mariscal?"**
   - Lead indeciso entre os dois produtos: **"A Pousada tem suítes e uma proposta mais acolhedora, com café da manhã servido na acomodação. A Casa é completa e privativa, com piscina para o grupo. Qual dessas opções combina mais com a viagem de vocês?"**
4. Perguntar criança ou pet **somente quando relevante** — nunca como pergunta fixa da sequência (ex.: quando o grupo sugerir família, ou quando a indicação de acomodação depender disso).
5. Motivo da viagem (descanso a dois, família, comemoração) é **opcional e nunca bloqueia o avanço para orçamento** — só perguntar se ajudar a indicar produto/acomodação ou se o ritmo da conversa permitir.
6. Com os três dados essenciais completos (Datas + Número de pessoas + Produto), avançar diretamente para conferência/orçamento humano, **sem pedir permissão para isso**: "Com essas informações, a equipe consegue verificar disponibilidade e montar o orçamento conforme as regras."

**Em QL3/QL4:** Datas e Número de pessoas podem ser solicitados juntos, na mesma mensagem, somente quando ambos ainda faltarem e o lead já tiver sinalizado pressa ou pedido orçamento diretamente — nunca como abertura padrão de QL1/QL2.

**Nunca transformar a qualificação em interrogatório** — cada mensagem avança exatamente um dado por vez (exceto a exceção de QL3/QL4 acima), sempre lendo o que já foi escrito antes de perguntar de novo.

---

## 6. Texto padrão QL4

**Objetivo:** levar para orçamento/reserva.

**Nota de precedência:** a cadência e os textos de follow-up oficiais para QL4 (e demais níveis) estão em `MATRIZ_FOLLOWUP_QL_WHATSAPP_VILLA_ARAGUA.md`, que prevalece sobre este arquivo em caso de divergência de prazo, cadência ou texto de follow-up.

- **Resposta imediata:** "Que ótimo! 😊 Já anotei tudo aqui. Vou deixar suas informações organizadas para a equipe verificar e preparar seu orçamento certinho."
- **SLA interno da equipe (não é mensagem ao lead):** se a equipe ainda não deu retorno dentro do prazo interno, isso é um alerta interno para Rene/Nubia/Renildo agirem — não é follow-up comercial e não gera mensagem automática ao hóspede.
- **Follow-up comercial ao lead (só depois do orçamento efetivamente enviado):** ver textos e prazos em `MATRIZ_FOLLOWUP_QL_WHATSAPP_VILLA_ARAGUA.md`, seção 4.
- **Encerramento educado, se lead não responder após contato da equipe:** "Oi! Ficamos à disposição se quiser retomar — é só chamar por aqui quando fizer sentido pra você 😊"

---

## 7. Texto padrão QL3

**Objetivo:** completar dados e transformar em QL4.

- **Resposta imediata:** "Oi! Que bom que você chegou até a gente 😊 Só preciso de mais um detalhe pra te ajudar certinho."
- **Pergunta de ajuste (adaptar à lacuna real — nunca perguntar dado já informado):** "Vocês já têm uma data mais certa em mente, ou ainda estão decidindo o período?" / "Pra eu indicar a melhor opção, quantas pessoas seriam ao todo?" / se a lacuna for Produto: "Vocês estão considerando a Pousada Arágua ou a Casa Arágua Mariscal?"
- **Follow-up 48h:** "Oi! Ficou alguma dúvida sobre datas ou número de pessoas? Assim que tiver esses detalhes, já te ajudo com o orçamento 😊"
- **Nutrição leve (se não responder):** enviar uma foto real ou informação sobre Mariscal/a pousada/a casa (conforme o produto já identificado), sem cobrar resposta.

---

## 8. Texto padrão QL2

**Objetivo:** nutrir sem pressionar.

- **Resposta informativa:** "Oi! Que bom que você está conhecendo a Villa Arágua 😊 Me conta um pouco mais do que você está buscando, que te ajudo a decidir com calma."
- **Pergunta direta de valor, sem nenhum dado informado (classificação QL2 — ver seção 4):** redirecionar para os dados essenciais antes de qualquer valor — nunca citar preço, faixa ou "a partir de" (ver `BIBLIOTECA_COMERCIAL_RECEPCIONISTA_IA_VILLA_ARAGUA.md`, regra-mãe 1).
- **Envio de contexto sobre Mariscal/Pousada (ou Casa, conforme identificado):** compartilhar informação real — café da manhã na suíte e piscina de área comum (Pousada) ou privacidade e piscina privativa (Casa) — nunca misturando os dois produtos na mesma mensagem.
- **Follow-up 3 dias:** "Oi! Ainda pensando em Mariscal? Fico à disposição se quiser saber mais 😊"
- **Follow-up 7 dias:** "Oi! Passando pra lembrar que estamos por aqui, se em algum momento fizer sentido planejar sua próxima viagem 🌿"

---

## 9. Texto padrão QL1

**Objetivo:** manter relacionamento sem consumir muito tempo comercial.

- **Resposta curta e acolhedora:** "Oi! Que bom te ver por aqui 😊 Qualquer dúvida, é só chamar."
- **Follow-up leve opcional (só se fizer sentido, sem prazo fixo):** "Oi! Se um dia quiser conhecer mais sobre a Villa Arágua, estamos por aqui 🌿"
- **Sem insistência comercial** — não repetir as perguntas de qualificação nem cobrar resposta.

---

## 10. Texto padrão NQ

**Objetivo:** encerrar sem atrito.

- **Resposta educada:** "Oi! Agradecemos seu contato 😊 No momento, esse não é bem o perfil que atendemos, mas desejamos uma ótima viagem!"
- **Encerramento:** não insistir, não reabrir a conversa depois disso.
- **Alternativa genérica, sem indicar concorrente específico**, salvo decisão explícita de Renildo: "Se quiser, posso te indicar onde buscar mais opções na região de Bombinhas." — só usar se o lead pedir ajuda para achar outra opção, e sempre de forma genérica, nunca citando um concorrente pelo nome.

---

## 11. Cadência de follow-up

**A fonte oficial de prazo, cadência e texto de follow-up é sempre `MATRIZ_FOLLOWUP_QL_WHATSAPP_VILLA_ARAGUA.md`. Quando houver dúvida de prazo, consultar a Matriz — este Funil não infere prazo nem cria cadência por analogia.** A tabela abaixo é só um resumo de leitura rápida.

| Nível | Follow-up 1 | Follow-up 2 | Encerramento |
|---|---|---|---|
| QL4 | 24h após orçamento enviado | 48h | Após tentativa comercial sem resposta |
| QL3 | 48h (pergunta de ajuste sem resposta) | Nutrição leve, sem prazo fixo | Se não completar dados após 2 tentativas |
| QL2 | 3 dias | 7 dias | Sem encerramento formal — deixa em aberto |
| QL1 | Follow-up leve opcional, sem prazo fixo | — | Não se aplica — sem pressão |
| NQ | Não se aplica | Não se aplica | Imediato, na primeira resposta |

**Silêncio muda Estágio, não reduz QL automaticamente:** quando o lead não responde, o Registro Comercial move o Estágio para "Aguardando retorno" — o nível QL permanece o mesmo até que uma nova informação real justifique reclassificação.

**SLA interno não é follow-up:** o tempo que a equipe leva para responder ou preparar um orçamento internamente é um alerta interno (Rene/Nubia/Renildo) — nunca uma mensagem comercial ao lead. Follow-up é sempre recontato ao lead, seguindo os prazos da Matriz.

---

## 12. Registro oficial

O único Registro Comercial oficial da Villa Arágua é `CRM_LEADS_VILLA_ARAGUA.md` (20 campos — ver lista completa no próprio arquivo, seção "Campos do lead"). Este Funil **não mantém tabela própria de registro** — orienta o que observar e quando registrar; o lançamento acontece sempre no CRM oficial. Rene/Nubia não devem duplicar informação dentro deste Funil.

QL, C, Estágio, Produto e Próxima ação são registrados exclusivamente no CRM oficial, seguindo o vocabulário já definido lá (QL1-QL4/NQ; C1-C4 conforme a Arquitetura; os 8 estágios oficiais; Pousada Arágua/Casa Arágua Mariscal).

**Registro mínimo na entrada do lead:**
- ID
- Data de entrada
- Nome/identificação
- Canal de origem
- Campanha/anúncio, quando houver
- Estágio = Novo

**Registro após a primeira resposta:**
- Produto
- Datas
- Número de pessoas
- QL
- C
- Estágio
- Último contato
- Próxima ação

**Registro após orçamento:**
- Orçamento enviado?
- Próximo follow-up
- Responsável
- Precisa de Renildo?
- Status final, Motivo de perda e Observações curtas — quando o ciclo se fechar

**Orientação obrigatória (preservada):** o registro é de uso interno da equipe (Rene, Nubia, Renildo). Não expor nome completo, telefone ou qualquer dado pessoal em relatórios, prints, análises ou qualquer material que saia do uso operacional direto — inclusive em conversas futuras com IA, usar apenas dados agregados (quantidade por QL, taxas), nunca linha a linha com identificação pessoal.

---

## 13. Pontes para as fontes oficiais

Este Funil não copia nem redefine nenhuma das fontes abaixo — só aponta para onde consultar cada assunto:

| Assunto | Consultar |
|---|---|
| C1–C4 (risco comercial da mensagem) | `ARQUITETURA_DO_SISTEMA_COMERCIAL_VILLA_ARAGUA.md`, seção 5 |
| Estágio e campos do Registro Comercial | `CRM_LEADS_VILLA_ARAGUA.md` |
| Ativos e fotos | `GUIA_ATIVOS_COMERCIAIS_WHATSAPP_VILLA_ARAGUA.md` |
| Cadência de follow-up | `MATRIZ_FOLLOWUP_QL_WHATSAPP_VILLA_ARAGUA.md` |
| Textos comerciais dentro da conversa | `BIBLIOTECA_COMERCIAL_RECEPCIONISTA_IA_VILLA_ARAGUA.md` |
| Operação diária e escalonamento para Renildo | `PROTOCOLO_USO_DIARIO_RASCUNHO_ASSISTIDO_VILLA_ARAGUA.md` |

---

## 14. Fotos e ativos

Este Funil não mantém catálogo próprio de fotos — usa apenas as seguintes regras de ponte para `GUIA_ATIVOS_COMERCIAIS_WHATSAPP_VILLA_ARAGUA.md`:

- Primeiro contato normalmente sem foto.
- Produto identificado permite considerar 1 ativo, mas não obriga.
- Usar apenas código oficial do Guia (`AT-POU-XX` / `AT-CAS-XX`).
- Nunca foto em C3/C4.
- Nunca ativo do produto errado.
- **`AT-POU-SUITE-01` está bloqueado para qualquer uso no fluxo deste Funil, até reclassificação ou substituição oficial no Guia** — decisão operacional desta rodada; o status do próprio ativo no Guia não foi alterado (o Guia não foi editado nesta rodada).
- `AT-CAS-CHURRASQUEIRA-01` permanece bloqueado.
- `AT-POU-FACHADA-01` não orienta chegada.

---

## 15. Métricas comerciais

- conversas totais;
- QL4;
- QL3;
- QL2;
- QL1;
- NQ;
- custo por QL4;
- custo por QL3 + QL4;
- orçamentos enviados;
- reservas fechadas;
- taxa conversa → QL3/QL4;
- taxa orçamento → reserva.

---

## 16. Futuro com IA

### Fase 1 — Manual
Rene/Nubia classificam o lead e enviam as mensagens diretamente, usando este processo como guia.

### Fase 2 — IA assistida
Claude sugere a classificação QL e o texto de resposta, mas o humano sempre revisa e envia manualmente — mesmo modelo do Modo Rascunho Assistido já usado pela Recepcionista IA.

### Fase 3 — Semi-automação
ManyChat ou ferramenta equivalente aplica tags e organiza os follow-ups automaticamente, mas o envio de qualquer mensagem comercial relevante continua exigindo aprovação humana.

### Fase 4 — Automação controlada
Envio automático permitido apenas para mensagens simples e seguras (ex.: confirmação de recebimento), depois de validação de tom, consentimento, LGPD e eficácia comprovada nas fases anteriores.

**Nenhuma dessas fases está autorizada além da Fase 1 nesta etapa.**

---

## 17. Regras de segurança comercial

- Disponibilidade sempre conferida por humano.
- Orçamento sempre conferido por humano.
- Desconto sempre escalado para Renildo.
- Pet sob consulta — nunca autorizado automaticamente.
- Exceções operacionais sob consulta.
- Nunca pressionar o lead.
- Nunca inventar benefício, amenity ou promessa não documentada.
- Nunca parecer robô frio — tom sempre humano, leve e acolhedor, conforme a filosofia de atendimento da Villa Arágua.
- Nunca prometer vista para o mar ou piscina aquecida.
- Nunca usar "últimas vagas" ou qualquer urgência falsa.
- Nunca citar preço fixo sem aprovação.
- Nunca misturar Pousada e Casa na mesma mensagem.

---

## 18. Conclusão

O funil QL cria uma ponte entre campanha, WhatsApp, atendimento e aprendizado comercial. A primeira versão deve ser manual/assistida (Fase 1) antes de qualquer automação real — as Fases 2 a 4 permanecem como visão futura, não como próximo passo imediato.

Nesta atualização (05/08/2026), o Funil passou a tratar Produto como dado essencial formal, adotou lógica de qualificação sem repetição em vez de script fixo, objetivou as fronteiras QL2/QL3/QL4, e passou a apontar para o CRM oficial como único destino de registro — sem redefinir QL, C, Estágio, ativo ou cadência em nenhum momento.

---

*Este arquivo não altera `ADENDO_QUALIFICACAO_MANUAL_LEADS_7_SETEMBRO_2026_POUSADA_ARAGUA.md`, `BIBLIOTECA_COMERCIAL_RECEPCIONISTA_IA_VILLA_ARAGUA.md`, nem nenhum outro arquivo-base do projeto, `DADOS_OFICIAIS_ATENDIMENTO_VILLA_ARAGUA.md` ou `.claude/skills/`. Nenhuma automação, integração, ManyChat ou envio automático foi criado. O WhatsApp e o Meta Ads não foram alterados. Este processo não substitui Rene ou Nubia — é um guia de apoio ao atendimento humano.*

---

## 19. Changelog

- **05/08/2026 — Claude (a pedido de Renildo):** Ajuste operacional pré-piloto do Funil QL, a partir da auditoria operacional realizada nesta mesma data. Resumo:
  - **Produto incluído como etapa formal** de qualificação (Pousada Arágua / Casa Arágua Mariscal / Indefinido), integrado às seções 3, 4 e 5.
  - **Regra de não repetir dado já informado** adicionada explicitamente na seção 5, com exemplos.
  - **Critérios QL2/QL3/QL4 objetivados**, usando contagem dos três dados essenciais (Datas, Número de pessoas, Produto) em vez de expressões subjetivas como "maioria das perguntas" (seções 3 e 4). Ambiguidade QL1/QL2 para pergunta de preço sem dados resolvida (QL2).
  - **Tabela paralela de registro (antiga seção 12) substituída** por referência direta ao Registro Comercial oficial (`CRM_LEADS_VILLA_ARAGUA.md`, 20 campos, conferidos diretamente nesta rodada), com três listas de preenchimento por momento (entrada, primeira resposta, orçamento).
  - **Pontes adicionadas** (nova seção 13) para Arquitetura, CRM, Guia, Matriz, Biblioteca e Protocolo, e (nova seção 14) para o Guia de Ativos — sem copiar ou redefinir nenhuma dessas fontes.
  - Seção 11 (cadência) ajustada para remover redação residual que misturava SLA interno com follow-up ("24h (se equipe não respondeu)" → "24h após orçamento enviado"), com notas explícitas de que silêncio muda Estágio (não QL) e que SLA interno não é follow-up.
  - Linguagem de permissão redundante removida ("Quer que eu já prepare um orçamento certinho com base nisso?"); nova frase segura adotada quando os dados mínimos estão completos: "Com essas informações, a equipe consegue verificar disponibilidade e montar o orçamento conforme as regras."
  - **Nenhuma definição de C, Estágio, ativo ou cadência foi duplicada ou redefinida** — todas continuam vivendo exclusivamente em suas fontes oficiais.
  - Seções renumeradas de 16 para 19 (inserção das novas seções 13 e 14; Changelog como nova seção 19).
  - Backup criado em `BACKUP_ANTES_AJUSTE_OPERACIONAL_FUNIL_QL_2026-08-05/` antes da edição.
  - **Nenhum outro arquivo do projeto foi alterado nesta rodada** (Arquitetura, Biblioteca Comercial, Matriz, Guia de Ativos, CRM, Jornada Inicial, Templates Operacionais, agentes, skills, Mapas e CLAUDE.md permanecem como estavam).
