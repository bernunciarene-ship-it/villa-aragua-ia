# MAPA DE USO DAS SKILLS — VILLA ARÁGUA IA

*Documento de orquestração do ecossistema de skills da Villa Arágua. Gerado e mantido a partir da skill `villa-aragua-skill-router` (`.claude/skills/villa-aragua-skill-router/`) — para o detalhe operacional completo de roteamento (matriz, regras de prioridade, prompts prontos), ver as referências daquela skill. Nenhum arquivo de skill original foi alterado para criar ou atualizar este mapa; ele apenas lê e resume o que já existe em `.claude/skills/`.*

## 1. Objetivo do mapa

Este arquivo existe para orientar o Claude Code (ou qualquer IA operando no projeto Villa Arágua) a **escolher a skill certa conforme a tarefa**, sem depender de Renildo lembrar manualmente qual das 12 skills locais usar em cada situação. Ele funciona como a visão de cima: quem quiser o detalhe fino de roteamento (matriz completa, regras de prioridade, fluxos prontos, prompts) vai em `villa-aragua-skill-router/references/`; quem quiser a visão geral rápida — o que existe, para que serve, quando usar, o que não fazer — fica neste mapa.

## 2. Regra de ouro

Antes de escolher qualquer skill, diferenciar sempre estas dez dimensões — misturá-las é a causa mais comum de roteamento errado:

- **Pousada Arágua** — produto com café incluso, piscina comum, 8 acomodações.
- **Casa Arágua** — produto privativo, piscina própria, até 6 pessoas, estacionamento exclusivo em área aberta (nunca "garagem coberta").
- **Meta Ads** — tráfego pago (campanha, anúncio, criativo).
- **Social Media** — Instagram orgânico (calendário, post, comunidade).
- **Conteúdo orgânico** — o que criar para site/blog/guia digital, sem ser pago nem ser Instagram.
- **SEO/GEO** — estrutura de página para busca e IA generativa.
- **Pricing** — quanto cobrar, desconto, pacote, margem.
- **Atendimento WhatsApp** — a conversa comercial real com o lead/hóspede.
- **Análise de campanhas** — medir o que já rodou (não criar).
- **Humanização textual** — a forma final de qualquer texto, nunca o conteúdo em si.

Uma tarefa que mistura duas dessas dimensões sem perceber (ex.: tratar "criar conteúdo de Instagram" como se fosse "estratégia de conteúdo de blog") é o principal sintoma de que o roteamento precisa passar pela `villa-aragua-skill-router` antes de executar.

## 3. Tabela geral das skills

| Skill | Papel | Entrada ideal | Saída esperada | Riscos se usada errado |
|---|---|---|---|---|
| `villa-aragua-sales-receptionist` | Conduzir a conversa comercial no WhatsApp | Mensagem real de um lead/hóspede | Resposta pronta, com diagnóstico e próximo passo | Prometer preço/disponibilidade sem checar; misturar Pousada e Casa na mesma resposta |
| `villa-aragua-pricing-revenue` | Definir/validar preço, pacote, desconto, margem | Pergunta sobre valor, oferta ou viabilidade de abrir uma data | Valor aprovado/sugerido, ou sinalização de que depende de autorização | Confirmar desconto ou pacote sem base oficial; aplicar tarifa da Pousada à Casa |
| `villa-aragua-humanizer-pt-br` | Tirar "cara de IA" de um texto já pronto | Texto já escrito, de qualquer origem | Mesmo texto, tom mais humano — nunca conteúdo novo | Mudar o conteúdo/promessa do texto original, não só a forma |
| `villa-aragua-copywriting-conversion` | Escrever copy comercial (site, anúncio, CTA) | Briefing de peça comercial | Texto final da peça | Inventar diferencial ou oferta não confirmada; usar urgência falsa |
| `villa-aragua-creative-design-ads` | Orientar direção visual de criativos/anúncios | Peça a produzir ou avaliar (imagem/vídeo) | Diretriz visual ou avaliação do criativo | Sugerir imagem que implique preço/disponibilidade não confirmada |
| `villa-aragua-social-media-manager` | Planejar Instagram orgânico e comunidade | Pedido de calendário, post, resposta a comentário/DM | Calendário, ideia de post, resposta de comunidade | Transformar o perfil em panfleto de oferta; misturar Pousada/Casa no mesmo post sem identificar |
| `villa-aragua-campaign-analytics` | Analisar campanha/funil já rodando | Dados reais de investimento, leads, reservas | Diagnóstico + recomendação (manter/pausar/ajustar/escalar) | Inventar métrica, ROAS ou reserva não informada |
| `villa-aragua-content-strategy` | Decidir o que criar de conteúdo (site/blog/guia) | Necessidade de planejamento editorial | Tema, cluster, briefing, calendário | Confundir com execução (achar que ela escreve o texto final) |
| `villa-aragua-ai-seo-geo` | Estruturar página/FAQ para busca e IA generativa | Tema já definido, precisa virar página citável | Estrutura (pergunta, resposta direta, FAQ, subtópicos) | Prometer ranking/posição garantida em busca ou IA |
| `villa-aragua-growth-marketer` | Coordenar prioridade estratégica de crescimento | Dúvida de onde investir tempo/orçamento | Plano de canais/experimentos, nunca a execução em si | Tratar curtida/alcance como sucesso; recomendar escalar sem evidência |
| `villa-aragua-marketing-psychology` | Explicar o comportamento do lead | Dúvida de "por que ele hesitou/sumiu/comparou preço" | Diagnóstico comportamental, com ética | Usar para justificar manipulação, escassez falsa ou pressão |
| `villa-aragua-skill-router` | Orquestrar as demais | Pedido amplo, ambíguo ou composto | Skill principal + apoio + ordem de execução | Acionar todas as skills "por segurança"; substituir a execução de outra skill |

## 4. Quando usar cada skill

### `villa-aragua-sales-receptionist`
Usar sempre que houver uma mensagem real (ou a simular) de um lead/hóspede no WhatsApp — diagnóstico de perfil, indicação de Pousada ou Casa, tratamento de objeção, cadência de follow-up. Não usar para decidir um preço novo ou escrever um anúncio do zero.

### `villa-aragua-pricing-revenue`
Usar sempre que a pergunta for "quanto cobrar", "tem desconto", "vale abrir essa data", ou qualquer condição comercial (parcelamento, pacote de feriado, taxa da Casa). Não usar para comunicar o valor ao hóspede (isso é `sales-receptionist`) nem para decidir campanha (isso é `growth-marketer`/`campaign-analytics`).

### `villa-aragua-humanizer-pt-br`
Usar como última passada de qualquer texto que uma pessoa real vai ler — WhatsApp, anúncio, post, página, resposta de avaliação. Não usar para decidir o que o texto deve dizer — ela só ajusta a forma.

### `villa-aragua-copywriting-conversion`
Usar para escrever ou revisar texto comercial: página de site, CTA, headline, anúncio Meta Ads. Não usar para decidir tema de conteúdo de longo prazo (isso é `content-strategy`) nem para validar preço (isso é `pricing-revenue`).

### `villa-aragua-creative-design-ads`
Usar para orientar ou avaliar a parte visual de um criativo/anúncio — formato, proporção, direção de imagem/vídeo. Não usar para escrever o texto que acompanha a peça.

### `villa-aragua-social-media-manager`
Usar para calendário de Instagram, ideia de post/story/reels/carrossel, resposta de comunidade (DM/comentário). Não usar para Meta Ads pago nem para planejamento de conteúdo de site/blog.

### `villa-aragua-campaign-analytics`
Usar quando já existir campanha rodando e o pedido for entender/medir resultado — funil, CPL, CPA, ROAS, gargalo. Não usar para criar a campanha do zero (isso é o Fluxo A completo, ver seção 5).

### `villa-aragua-content-strategy`
Usar para decidir o que criar de conteúdo (site, blog, guia digital), organizar clusters, auditar conteúdo existente (`/content:audit`) ou montar calendário editorial. Não usar para escrever o texto final nem para estruturar citabilidade técnica (isso é `ai-seo-geo`).

### `villa-aragua-ai-seo-geo`
Usar quando o conteúdo precisar virar página/FAQ estruturada para aparecer bem em busca orgânica ou ser citável por IA generativa. Não usar para decidir o tema (isso é `content-strategy`) nem para prometer posição de busca.

### `villa-aragua-growth-marketer`
Usar para decisão estratégica de onde investir esforço — canais de aquisição, plano de 30/60/90 dias, reativação de hóspede antigo, parceria local. Não usar para executar a peça (ela aciona a skill de execução certa) nem para medir resultado (isso é `campaign-analytics`).

### `villa-aragua-marketing-psychology`
Usar quando a dúvida for sobre comportamento do lead — por que hesita, compara preço, some depois do orçamento. Não usar para decidir preço (isso é `pricing-revenue`) nem para escrever a mensagem em si.

### `villa-aragua-skill-router`
Usar sempre que não estiver claro qual das outras 11 skills usar, ou quando o pedido envolver mais de um domínio ao mesmo tempo. Ver seção 9.

## 5. Combinações recomendadas de skills

- **WhatsApp comercial**: `sales-receptionist` → `pricing-revenue` (se envolver preço/desconto) → `humanizer-pt-br`.
- **Campanha Meta Ads (criação)**: `pricing-revenue` → `copywriting-conversion` → `creative-design-ads` → `humanizer-pt-br` → `sales-receptionist` (coerência com o atendimento) → `campaign-analytics` (medir depois).
- **Conteúdo Instagram**: `content-strategy` (tema) → `social-media-manager` (formato/calendário) → `copywriting-conversion` (legenda) → `creative-design-ads` (visual) → `humanizer-pt-br`.
- **Página/FAQ/guia digital**: `ai-seo-geo` (estrutura) → `content-strategy` (tema/prioridade) → `copywriting-conversion` (texto final) → `humanizer-pt-br`.
- **Análise de campanha com venda**: `campaign-analytics` (diagnóstico) → `sales-receptionist` (se o gargalo for atendimento) → `pricing-revenue` (se o gargalo for oferta/margem).
- **Plano de crescimento**: `growth-marketer` → `pricing-revenue` (validação) → skill de execução do canal escolhido → `campaign-analytics` (medição).
- **Entender o lead antes de agir**: `marketing-psychology` → `sales-receptionist` → `humanizer-pt-br`.

## 6. Exemplos práticos de roteamento

| Pedido do usuário | Skill principal | Skill de apoio | Observação |
|---|---|---|---|
| "Crie uma resposta para lead no WhatsApp" | `sales-receptionist` | `pricing-revenue` (se envolver preço/desconto) + `humanizer-pt-br` | Diagnosticar perfil antes de indicar Pousada ou Casa |
| "Analise esta campanha Meta Ads" | `campaign-analytics` | `pricing-revenue` (se houver receita/margem) + `sales-receptionist` (se o gargalo for WhatsApp) | Nunca inventar métrica não informada |
| "Crie copy para anúncio" | `copywriting-conversion` | `creative-design-ads` + `pricing-revenue` (se houver oferta) + `humanizer-pt-br` | Especificar sempre Pousada ou Casa — nunca anúncio genérico misturando os dois |
| "Monte calendário de conteúdo para setembro" | `content-strategy` | `social-media-manager` (se for Instagram) + `ai-seo-geo` (se for site/blog) | Cruzar com calendário de sazonalidade (7 de Setembro tem pacote confirmado, exclusivo da Pousada) |
| "Humanize esta mensagem" | `humanizer-pt-br` | A skill de origem do texto, se precisar corrigir conteúdo (não só forma) | Humanizer nunca muda o que o texto promete, só como |
| "Qual preço cobrar no feriado?" | `pricing-revenue` | `sales-receptionist` (para comunicar depois) | Só usar dado oficial já aprovado; feriado sem pacote confirmado não tem valor fechado |
| "Crie FAQ para o site" | `ai-seo-geo` | `content-strategy` (prioridade do tema) + `copywriting-conversion` (texto final) | Resposta sempre curta, direta, com dado oficial |
| "Crie briefing de criativo para Instagram" | `creative-design-ads` | `social-media-manager` (formato/calendário) + `copywriting-conversion` (texto) | Definir se é Pousada, Casa ou peça comparativa identificada |
| "Monte follow-up para lead que sumiu" | `sales-receptionist` | `pricing-revenue` (se a objeção for preço) + `humanizer-pt-br` | Cadência já validada: 24h → 72h → 7 dias. `FASE_1_FOLLOW_UP_MANUAL_ASSISTIDO_VILLA_ARAGUA.md` deve ser usado para o processo manual em uso hoje; `ARQUITETURA_FOLLOW_UP_AUTOMATICO_VILLA_ARAGUA.md` é a visão futura de automação |
| "Compare Pousada e Casa para uma família" | `sales-receptionist` | `pricing-revenue` (se pedir valor) | Comparar por critério real (capacidade, café, piscina) — nunca vender um produto desvalorizando o outro |

## 7. Regras de proteção comercial

- Não inventar disponibilidade — qualquer resposta sobre data depende de checagem real.
- Não prometer desconto — desconto sempre depende de `villa-aragua-pricing-revenue` e, em última instância, de autorização de Renildo/equipe.
- Não misturar Pousada e Casa — cada produto tem regra, preço e diferenciais próprios; comparação só em peça explicitamente comparativa e identificada.
- Não usar urgência falsa — nenhuma menção a "últimas vagas" ou contagem regressiva sem data/disponibilidade real.
- Não alterar regra sem fonte oficial — todo dado (preço, comodidade, distância, política) vem de `DADOS_OFICIAIS_ATENDIMENTO_VILLA_ARAGUA.md` ou arquivo oficial equivalente.
- Não chamar o estacionamento da Casa Arágua de "garagem coberta" — é sempre "estacionamento exclusivo em área aberta para até 3 carros".
- Não aplicar pacote da Pousada à Casa — cada oferta é exclusiva do produto para o qual foi aprovada (ex.: pacote de 7 de Setembro é só da Pousada).

Estas regras valem para **todas** as skills do ecossistema, não apenas para as que lidam diretamente com preço ou atendimento — uma peça de Instagram ou uma página de SEO que viole qualquer uma delas está errada da mesma forma que uma resposta de WhatsApp estaria.

## 8. Hierarquia de decisão

Ordem de checagem ao decidir qual skill aciona primeiro:

1. **Se envolve preço** → `villa-aragua-pricing-revenue`.
2. **Se envolve WhatsApp/lead** → `villa-aragua-sales-receptionist`.
3. **Se envolve tom humano de um texto já escrito** → `villa-aragua-humanizer-pt-br`.
4. **Se envolve anúncio** → `villa-aragua-copywriting-conversion` (texto) e/ou `villa-aragua-creative-design-ads` (visual).
5. **Se envolve campanha/métrica** → `villa-aragua-campaign-analytics`.
6. **Se envolve Instagram orgânico** → `villa-aragua-social-media-manager`.
7. **Se envolve planejamento editorial** → `villa-aragua-content-strategy`.
8. **Se envolve Google, FAQ, site, guia digital ou busca por IA** → `villa-aragua-ai-seo-geo`.
9. **Se envolve prioridade estratégica de crescimento** → `villa-aragua-growth-marketer`.
10. **Se envolve entender o comportamento do lead** → `villa-aragua-marketing-psychology`.
11. **Se houver dúvida** → `villa-aragua-skill-router` decide e justifica.

Esta hierarquia resolve a maioria dos conflitos por ordem de prioridade — se um pedido acionar mais de uma linha (ex.: envolve preço **e** WhatsApp), normalmente a primeira linha que se aplica define a skill principal, e as demais entram como apoio.

## 9. Como usar a skill-router

A `villa-aragua-skill-router` **não substitui** nenhuma das outras 11 skills — ela não escreve copy, não calcula preço, não desenha criativo, não humaniza texto. O papel dela é só decidir: qual skill principal, quais skills de apoio, em qual ordem, e qual a saída esperada. Sempre que não estiver claro por onde começar — pedido amplo, composto, ou literalmente "qual skill eu uso" — é ela quem resolve a ambiguidade antes de qualquer execução começar. Ver `villa-aragua-skill-router/SKILL.md` para o comportamento completo e os formatos de saída (tarefa simples / complexa / dúvida).

## 10. Pendências futuras

- Integração com automação de follow-up (ver `ARQUITETURA_FOLLOW_UP_AUTOMATICO_VILLA_ARAGUA.md`, na raiz do projeto — hoje é manual/arquitetura, não automação real).
- Conexão com CRM de leads (ainda não existe nenhum CRM em uso no projeto).
- Conexão técnica com WhatsApp (Business API ou similar) — não configurada.
- Biblioteca de respostas aprovadas (hoje as respostas-modelo estão dentro das skills, ainda não consolidadas num banco único e versionado).
- Banco de preços oficiais consultável programaticamente (hoje o preço vive em `DADOS_OFICIAIS_ATENDIMENTO_VILLA_ARAGUA.md` e nas referências de `pricing-revenue`, sem um "banco" único).
- Banco de disponibilidade real (não existe hoje nenhuma fonte automatizada de disponibilidade — toda checagem de data é manual/humana).
- Logs de campanhas consolidados (os arquivos brutos existem em `MARKETING E VENDAS/CAMPANHAS META ADS/`, mas ainda não estão centralizados de forma consultável).
- Histórico de leads (não existe hoje uma base histórica de leads fora das conversas de WhatsApp já encerradas).

## Observação final

Este mapa é o documento de orquestração do ecossistema de skills da Villa Arágua — ele resume o que já está detalhado em cada skill individual e no roteador (`villa-aragua-skill-router`). Sempre que uma nova skill for criada ou uma existente for ampliada, este mapa deve ser atualizado para continuar refletindo a realidade do projeto — nunca deixá-lo desatualizado listando skill que não existe mais, ou omitindo uma nova.
