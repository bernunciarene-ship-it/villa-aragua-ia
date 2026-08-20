# Auditoria de conteúdo

Método para revisar o que já existe e decidir o que fazer com cada peça — acionado pelo modo `/content:audit`. A decisão final de cada item segue `politica-keep-update-merge-kill.md`; este arquivo cobre o **método de auditoria** (o que olhar, como classificar).

## O que auditar

- Páginas fixas do site (institucionais, de produto).
- Posts de blog.
- Seções do guia digital.
- FAQs (Pousada, Casa, região).
- Páginas da Pousada Arágua.
- Páginas da Casa Arágua.
- Posts antigos de Instagram/campanha com conteúdo ainda referenciável.
- Conteúdos de feriado (ex.: material de campanhas passadas de 7 de Setembro, Natal, Réveillon).
- Conteúdos de Bombinhas/Mariscal (guias de região, dicas).

**Pendência conhecida**: hoje não existe site/blog publicado neste projeto, então a auditoria de "páginas do site" e "posts de blog" é, por ora, prospectiva — o método se aplica assim que esse conteúdo existir. O que já pode ser auditado hoje: `GUIA_DIGITAL_HOSPEDE_VILLA_ARAGUA.md`, os materiais de campanha já produzidos (`MARKETING E VENDAS/CAMPANHAS META ADS/`), e os próprios arquivos de referência desta e de outras skills.

## Os nove critérios de auditoria

Para cada peça de conteúdo, responder:

1. **Gera tráfego?** — há algum sinal (mesmo qualitativo) de que essa peça é encontrada/acessada? (dado real, quando existir via `villa-aragua-campaign-analytics`; caso contrário, marcar como "não medido")
2. **Gera WhatsApp?** — essa peça já levou alguém a iniciar conversa? (mesma ressalva de dado acima)
3. **Ajuda o hóspede?** — responde a uma dúvida real, mesmo de quem não vai reservar agora?
4. **Está atualizado?** — o dado (preço de referência, regra, comodidade, oferta) ainda bate com `DADOS_OFICIAIS_ATENDIMENTO_VILLA_ARAGUA.md` hoje?
5. **Tem dado oficial?** — toda afirmação de fato é rastreável a uma fonte oficial, ou há trecho impreciso/desatualizado?
6. **Diferencia Pousada e Casa?** — quando aplicável, a peça deixa claro a qual produto cada informação pertence, sem misturar oferta?
7. **Tem CTA?** — existe um caminho claro de volta para o WhatsApp, mesmo que leve?
8. **Pode ser citado por Google/IA?** — a peça tem resposta direta, estrutura clara, informação extraível fora de contexto (ver `villa-aragua-ai-seo-geo/references/estrutura-conteudo-citavel.md`)?
9. **Está competindo com outro conteúdo parecido?** — existe mais de uma peça tratando do mesmo tema de forma quase idêntica (risco de canibalização, ver `seo-otimizacao-conteudo.md`)?

## Modelo de ficha de auditoria

```
AUDITORIA DE CONTEÚDO — [nome/URL da peça]
Tipo: [página de site / post de blog / seção de guia / FAQ / post antigo / conteúdo de feriado / conteúdo de região]
Produto: [ ] Pousada Arágua  [ ] Casa Arágua  [ ] Ambos  [ ] Região/marca (sem produto específico)

1. Gera tráfego? [sim/não/não medido — fonte do dado, se houver]
2. Gera WhatsApp? [sim/não/não medido]
3. Ajuda o hóspede? [sim/não/parcialmente]
4. Está atualizado? [sim/não — o que mudou]
5. Tem dado oficial? [sim/não — o que precisa corrigir]
6. Diferencia Pousada/Casa? [sim/não/não se aplica]
7. Tem CTA? [sim/não]
8. Citável por Google/IA? [sim/não/parcialmente]
9. Compete com outro conteúdo? [sim, com [nome] / não]

Classificação: [ ] Manter  [ ] Atualizar  [ ] Unir  [ ] Reaproveitar  [ ] Arquivar  [ ] Apagar (requer aprovação humana)
Justificativa: [1-2 frases]
Próxima ação: [o que fazer e qual skill aciona]
```

## Como classificar (visão geral — regra completa em `politica-keep-update-merge-kill.md`)

- **Manter**: passa bem nos nove critérios, sem necessidade de ação.
- **Atualizar**: tema/estrutura ainda bons, mas dado desatualizado ou estrutura fraca em citabilidade.
- **Unir**: compete com outra peça do mesmo tema — combinar em uma versão mais forte.
- **Reaproveitar**: conteúdo bom, mas em formato que não aproveita todo o potencial (ex.: só existe como Instagram, poderia virar página de FAQ também) — ver `reaproveitamento-conteudo.md`.
- **Arquivar**: obsoleto (ex.: campanha de feriado já passado), sem valor de manter indexado/visível, mas sem necessidade de excluir de vez.
- **Apagar**: só com aprovação humana explícita — esta skill nunca decide apagar sozinha.

## Como rodar uma auditoria completa

1. Listar todo o conteúdo existente por tipo (usar a lista do topo deste arquivo).
2. Preencher a ficha de auditoria para cada peça (ou para os grupos mais relevantes, se o volume for grande).
3. Classificar segundo `politica-keep-update-merge-kill.md`.
4. Consolidar os resultados num resumo: quantas peças em cada classificação, quais ações prioritárias.
5. Alimentar `calendario-30-60-90.md` e `calendario-conteudo-mensal.md` com as ações decorrentes (atualizar X, unir Y com Z, criar novo brief para lacuna encontrada).

## O que esta auditoria nunca faz

- Nunca decide "apagar" sem aprovação humana explícita.
- Nunca classifica com base em impressão isolada — sempre passa pelos nove critérios.
- Nunca inventa dado de tráfego/conversão quando ele não existe — marcar como "não medido" é uma resposta válida e honesta.
- Nunca mistura avaliação de Pousada com a de Casa quando o conteúdo é específico de um produto.

## Como usar este arquivo na prática (`/content:audit`)

1. Definir o escopo da auditoria (todo o conteúdo, ou um recorte: só FAQs, só conteúdo de feriado, só páginas de produto).
2. Rodar a ficha de auditoria para cada peça do escopo.
3. Classificar cada uma segundo `politica-keep-update-merge-kill.md`.
4. Gerar a lista de ações e encaminhar para `brief-conteudo.md` (conteúdo novo/atualização) ou `reaproveitamento-conteudo.md` (mudança de formato) conforme o caso.
