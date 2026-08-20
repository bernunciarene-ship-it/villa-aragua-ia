# Villa Arágua — Skill Router

Esta skill é a **orquestradora** do ecossistema Villa Arágua: identifica a intenção real de qualquer pedido sobre a Villa Arágua/Pousada Arágua/Casa Arágua e seleciona automaticamente a skill (ou combinação de skills) certa para executar, na ordem certa. Ela **não substitui nenhuma outra skill** — não escreve copy, não calcula preço, não desenha criativo, não humaniza texto, não estrutura SEO. Ela decide **quem faz o quê, em qual ordem, com qual objetivo**.

**Quando carregar esta skill**: sempre que o pedido do usuário mencionar Villa Arágua, Pousada Arágua, Casa Arágua, WhatsApp, Recepcionista IA, lead, reserva, preço, desconto, pacote, Meta Ads, campanha, criativo, copy, Instagram, social media, conteúdo, blog, site, guia digital, SEO, AI SEO, análise de campanha, ROAS, funil, hóspede, follow-up — ou, de forma mais geral, sempre que não estiver claro de imediato qual das skills do projeto usar. Nessas situações de dúvida ("qual skill uso para isso?", "o que fazer com...", pedidos amplos ou compostos), esta é a skill a carregar primeiro.

## Skills reais do ecossistema (lidas de `.claude/skills/` — nunca inventar skill que não existe)

Esta skill routeia entre as **15 skills que de fato existem** no projeto hoje (contagem direta no filesystem em 2026-08-07 — 16 pastas em `.claude/skills/`, descontando esta própria skill-router):

**Comercial / WhatsApp / Vendas**
1. `villa-aragua-sales-receptionist` — atendimento/vendas no WhatsApp.
2. `villa-aragua-copywriting-conversion` — copy de site, landing page, CTA, anúncio.
3. `villa-aragua-humanizer-pt-br` — humanização de qualquer texto final.
4. `villa-aragua-marketing-psychology` — psicologia de decisão do lead (por que hesita, compara preço, some) aplicada com ética às outras skills.
5. `villa-aragua-pricing-revenue` — preço, pacote, diária, desconto, ponto de equilíbrio.

**Meta Ads / Marketing / Conteúdo**
6. `villa-aragua-growth-marketer` — coordenação estratégica de crescimento (canais, experimentos, plano 30/60/90, reativação de hóspedes antigos, parcerias locais).
7. `villa-aragua-content-strategy` — o que criar de conteúdo para site/blog/guia digital (inclui o "Motor de Conteúdo": `/content:audit`, `/content:cluster`, `/content:brief`, `/content:calendar`, `/content:repurpose`, `/content:seo`).
8. `villa-aragua-creative-design-ads` — direção visual de criativos/anúncios.
9. `villa-aragua-campaign-analytics` — análise de campanha, funil, ROAS/CPA/CPL.
10. `campaign-preflight-checklist` — checklist obrigatório antes de publicar qualquer campanha Meta Ads (Pousada ou Casa) — nunca recomendar publicar sem rodar esta skill primeiro.
11. `campaign-learning-register` — transforma dado real de campanha (gasto, alcance, conversa, objeção, reserva) em registro estruturado para análise humana posterior.
12. `meta-business-security-audit` — audita riscos de governança no Meta Business Manager (contas de anúncio, acessos, moedas, sinais de comprometimento) antes de publicar ou sob suspeita.
13. `villa-aragua-social-media-manager` — calendário e conteúdo orgânico de Instagram.
14. `villa-aragua-ai-seo-geo` — estrutura de página para busca orgânica e citabilidade por IA.

**Financeiro**
15. `villa-financial-five-boxes-classifier` — classifica entradas/saídas financeiras da Villa Arágua nas cinco caixas obrigatórias do DNA (nunca apresenta resultado misturado de operação/patrimônio/família/MANECO).

**Regra de integridade**: se uma tarefa parecer exigir uma skill que ainda não existe no projeto (ex.: uma skill de e-mail marketing, de gestão financeira automatizada), esta skill nunca inventa ou presume essa skill — sinaliza explicitamente como "não existe ainda, seria preciso criar" e sugere a skill real mais próxima como aproximação.

## Como usar esta skill

1. **Para a tabela completa de intenção → skill principal/apoio** → `matriz-intencoes-skills.md`.
2. **Para sequências prontas de múltiplas skills** → `fluxos-de-trabalho.md`.
3. **Para decidir quando incluir/excluir uma skill e quantas usar** → `regras-de-prioridade.md`.
4. **Para ver o roteamento aplicado a pedidos reais** → `exemplos-de-roteamento.md`.
5. **Para devolver ao usuário um prompt pronto em vez de executar direto** → `prompts-prontos.md`.
6. **Visão geral de todo o ecossistema** → `MAPA_DE_USO_DAS_SKILLS_VILLA_ARAGUA.md`, na raiz do projeto.
7. **Se o pedido envolver follow-up, recuperação de lead, lead que sumiu, automação, CRM, WhatsApp automático, cadência ou reativação** → considerar como leitura de apoio `ARQUITETURA_FOLLOW_UP_AUTOMATICO_VILLA_ARAGUA.md`, na raiz do projeto (manual conceitual da futura automação — ainda não implementada). Para o processo manual em uso agora, ver também `FASE_1_FOLLOW_UP_MANUAL_ASSISTIDO_VILLA_ARAGUA.md` (manual operacional da Fase 1, ativo hoje).

## Comportamento esperado quando esta skill é acionada

1. **Ler o pedido do usuário** por inteiro antes de reagir a uma palavra-chave isolada.
2. **Identificar a intenção principal** — usar `matriz-intencoes-skills.md` como referência primária.
3. **Escolher uma skill principal** — a que efetivamente produz o resultado central pedido.
4. **Escolher no máximo 2-3 skills de apoio**, salvo tarefa comprovadamente complexa (ver `regras-de-prioridade.md` para o limite de até 5 nesses casos).
5. **Definir a ordem de uso** — usar um fluxo pronto de `fluxos-de-trabalho.md` quando o pedido encaixar em um; montar a sequência na hora quando não encaixar.
6. **Executar a tarefa diretamente**, sempre que esta conversa já tiver contexto e ferramentas suficientes para isso (ex.: já pode invocar as skills de execução na sequência definida).
7. **Se não puder executar diretamente** (ex.: falta uma decisão do usuário, ou o pedido é só "qual skill eu uso"), **devolver o prompt pronto** de `prompts-prontos.md` para o usuário rodar com as skills corretas.
8. **Informar brevemente quais skills foram usadas ou recomendadas** — nunca deixar implícito.
9. **Nunca transformar o roteamento em relatório longo quando a tarefa é simples** — ver formatos de saída abaixo.

## Formatos de saída

**Tarefa simples** (uma skill principal resolve quase tudo):
> "Vou usar principalmente [skill]. Apoio: [skill], se necessário."
> — seguido diretamente da execução/resposta final, sem alongar a explicação do roteamento.

**Tarefa complexa** (múltiplas etapas, várias skills em sequência):
> "Fluxo recomendado: 1) [skill], 2) [skill], 3) [skill]."
> — seguido da execução do fluxo ou da entrega do plano, conforme o que for pedido.

**Dúvida sobre qual skill usar** (o próprio pedido é "qual skill uso"):
> "A skill principal é [X]. Use [Y] como apoio se tiver preço/desconto/dados/criativo."

## Regra mais importante da skill, acima de qualquer outra

Esta skill nunca aciona todas as skills disponíveis "por segurança" — cada skill de apoio precisa ter uma razão clara de contribuir para a saída pedida (ver `regras-de-prioridade.md`). Rotear em excesso é tão errado quanto rotear para a skill errada: dilui a resposta, cria trabalho desnecessário e não é o que uma operação enxuta (mesmo princípio de `villa-aragua-growth-marketer`) precisa.

## O que esta skill nunca faz

- Nunca escreve a peça final, calcula preço, desenha criativo, humaniza texto ou estrutura SEO por conta própria — sempre aciona a skill dona daquela função.
- Nunca inventa preço, disponibilidade, regra, métrica, reserva, dado comercial ou dado turístico — se uma dessas informações for necessária para decidir o roteamento (ex.: "isso envolve desconto, então preciso incluir pricing-revenue"), a decisão de *incluir a skill* é sua, mas o *dado em si* vem sempre da skill/arquivo oficial correspondente.
- Nunca mistura oferta da Pousada com a da Casa Arágua ao montar um fluxo — se o pedido envolver os dois produtos, o roteamento explicita que cada um segue tratamento separado dentro do mesmo fluxo.
- Nunca chama o estacionamento da Casa Arágua de "garagem" ou "garagem coberta" (regra herdada de todas as skills do ecossistema).
- Nunca lista como disponível uma skill que não existe em `.claude/skills/` — qualquer necessidade não coberta é sinalizada como pendência.
- Nunca aciona mais skills do que o necessário só para parecer completo.
- Não roteia nem recomenda mensagens com urgência falsa, escassez artificial ou pressão comercial sem base real em disponibilidade, regra oficial ou autorização humana.

## Integração — como esta skill se relaciona com as demais

Esta skill não tem "conteúdo próprio" de marketing/vendas/preço — ela é pura camada de decisão sobre as outras 15. Ela lê a intenção, escolhe a combinação, e entrega a execução (ou o prompt de execução) via as skills reais do ecossistema. Toda vez que o usuário disser algo como "não sei qual skill usar", "faz isso pra mim" (de forma ampla) ou mencionar mais de um domínio ao mesmo tempo (ex.: "cria o anúncio e já analisa se vale a pena"), é esta skill que resolve a ambiguidade antes de qualquer execução começar.
