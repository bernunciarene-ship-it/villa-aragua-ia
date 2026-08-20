# Robots, crawlers e monitoramento

Checklist para **revisar e recomendar**, nunca para alterar automaticamente. Toda ação técnica descrita aqui (editar robots.txt, sitemap, canonical, Search Console) precisa ser executada por uma pessoa com acesso técnico ao site — esta skill só orienta o que olhar e o que sugerir.

**Pendência conhecida**: não existe hoje, neste projeto, site publicado, sitemap, robots.txt, Google Search Console ou Google Perfil da Empresa configurado e documentado. Este checklist é o roteiro para quando essa infraestrutura existir — nenhum item abaixo deve ser tratado como já verificado ou já aplicado.

## Checklist técnico (revisar, não alterar)

- [ ] **sitemap.xml** — existe, está atualizado, inclui todas as páginas relevantes (Pousada, Casa, guia de região, FAQs)?
- [ ] **robots.txt** — não está bloqueando por engano páginas que deveriam ser indexadas?
- [ ] **Canonical** — cada página aponta corretamente para si mesma (evitando conteúdo duplicado)?
- [ ] **Páginas bloqueadas** — existe alguma página importante marcada como `noindex` sem necessidade?
- [ ] **Páginas órfãs** — existe conteúdo (ex.: uma página de campanha antiga) sem nenhum link interno apontando para ela?
- [ ] **Titles e meta descriptions** — cada página tem título e descrição únicos, claros, sem duplicação entre páginas?
- [ ] **Headings H1/H2** — cada página tem só um H1 (o título principal) e subtítulos organizados em H2/H3 correspondendo aos subtópicos (ver `estrutura-conteudo-citavel.md`)?
- [ ] **Links internos** — a página da Pousada linka para a Casa (e vice-versa), para o guia de região, para a página de reserva direta?
- [ ] **Performance mobile** — a página carrega bem e é legível em celular (a maior parte do tráfego de turismo é mobile)?
- [ ] **Google Search Console** (se disponível) — há erro de indexação, cobertura, ou queda de desempenho relatada?
- [ ] **Indexação** — as páginas novas foram de fato indexadas (verificável só com Search Console ou busca direta `site:dominio.com`)?
- [ ] **Páginas duplicadas** — existe mais de uma página tratando do mesmo tema de forma quase idêntica (ex.: duas páginas de FAQ da Pousada)?
- [ ] **Páginas de campanha antigas** — páginas de uma campanha encerrada (ex.: feriado já passado) ainda estão indexadas com informação desatualizada? Precisam de atualização, redirecionamento ou remoção, conforme o caso.
- [ ] **Imagens sem alt text** — fotos de acomodação, região, prova social têm texto alternativo descritivo (não genérico)?
- [ ] **PDFs ou guias que deveriam virar página HTML** — o `GUIA_DIGITAL_HOSPEDE_VILLA_ARAGUA.md`, por exemplo, é hoje um documento; quando publicado, ganha muito mais indexabilidade como página HTML do que como PDF.
- [ ] **Possíveis crawlers de IA** — verificar (com cautela, porque as regras de cada empresa mudam com frequência) se o robots.txt está bloqueando ou permitindo crawlers de IA (ex.: agentes de busca de assistentes de IA) de forma intencional, não por acidente. Não presumir uma lista fixa de user-agents como definitiva — checar a documentação vigente de cada ferramenta no momento da revisão.

## Monitoramento manual de presença em respostas de IA

Como não existe ferramenta automatizada confiável para medir isso, o monitoramento é manual e qualitativo:

1. **Fazer as perguntas-alvo** (ver `consultas-alvo-ai-search.md`) diretamente no ChatGPT, Perplexity, Gemini e Google, periodicamente (ex.: a cada mês).
2. **Registrar se a Villa Arágua aparece** na resposta, e como (citada, linkada, mencionada de passagem).
3. **Registrar quais concorrentes ou fontes aparecem** no lugar (sem inventar comparação de preço/posicionamento com eles, ver `villa-aragua-pricing-revenue/references/concorrentes-otas.md`) — apenas observar quem está sendo citado.
4. **Registrar qual página da Villa Arágua deveria existir** para responder melhor àquela pergunta, caso a marca não tenha aparecido ou tenha aparecido de forma fraca.
5. **Transformar lacunas em pauta** para `villa-aragua-content-strategy` decidir se aquele tema entra no próximo ciclo de conteúdo.

## Modelo de registro do monitoramento manual

```
MONITORAMENTO AI SEARCH — VILLA ARÁGUA
Data da checagem: [data]
Pergunta testada: [uma das consultas-alvo]
Ferramenta: [ChatGPT / Perplexity / Gemini / Google]
A Villa Arágua apareceu? [sim / não / parcialmente]
Como apareceu (se sim): [citada / linkada / mencionada sem detalhe]
Quem apareceu no lugar (se não): [observação, sem comparação de preço]
Página que deveria existir/melhorar: [ex.: "faltou uma página clara sobre X"]
Encaminhado para content-strategy: [ ] sim  [ ] não ainda
```

## Por que isso nunca vira promessa de resultado

Esse monitoramento é observação, não garantia — uma IA pode citar a Villa Arágua num mês e não citar no seguinte, por motivos fora de controle (mudança de modelo, mudança de fonte usada pela ferramenta). O valor do monitoramento é identificar lacunas de conteúdo reais, não acompanhar "ranking" como se fosse um placar a vencer.

## Como usar este arquivo na prática

1. Rodar o checklist técnico sempre que houver mudança grande no site (nova página, nova estrutura) ou periodicamente (ex.: trimestral).
2. Apresentar qualquer achado técnico como recomendação a validar com quem tem acesso técnico ao site — nunca como alteração já feita.
3. Rodar o monitoramento manual de IA periodicamente, registrando cada checagem no modelo acima.
4. Encaminhar lacunas identificadas para `villa-aragua-content-strategy`, que decide a prioridade de criar/ajustar conteúdo.
