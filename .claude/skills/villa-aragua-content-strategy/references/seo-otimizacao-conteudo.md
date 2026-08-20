# SEO — otimização de conteúdo

Checklist editorial de otimização, acionado pelo modo `/content:seo`. Este é o nível **editorial** de revisão (estrutura do texto, clareza, organização) — a estrutura técnica avançada de citabilidade por IA generativa e sugestão de dados estruturados é sempre `villa-aragua-ai-seo-geo` (ver `checklist-ai-seo.md` e `schema-e-dados-estruturados.md` daquela skill). As duas checklists se complementam; esta não substitui aquela.

## O checklist (14 itens)

- [ ] **H1 claro** — o título principal descreve exatamente o que a página responde, sem jogo de palavras vago.
- [ ] **H2 em formato de pergunta** — cada subtítulo é uma sub-pergunta real que o hóspede faria (ex.: "A Casa Arágua tem café incluso?"), não um rótulo genérico ("Comodidades").
- [ ] **Resposta direta no início** — a pergunta principal da página é respondida já no primeiro parágrafo, antes de qualquer contexto ou história.
- [ ] **FAQ presente** — a página tem uma seção de perguntas frequentes ao final (ver `villa-aragua-ai-seo-geo/references/faq-pousada-casa-bombinhas.md`).
- [ ] **Links internos** — a página linka para o produto irmão (Pousada ↔ Casa), para o cluster de região, e para a página de reserva direta, quando aplicável.
- [ ] **Title** — o título de aba/busca é único, claro, e reflete o conteúdo real da página (nunca clickbait).
- [ ] **Meta description** — resume a página de forma honesta em 1-2 frases, sem prometer o que a página não entrega.
- [ ] **Alt text** — toda imagem tem texto alternativo descritivo real (ex.: "piscina privativa da Casa Arágua ao entardecer"), nunca genérico ("imagem1.jpg") nem inventado além do que a foto mostra.
- [ ] **Dados oficiais** — toda afirmação de fato é rastreável a `DADOS_OFICIAIS_ATENDIMENTO_VILLA_ARAGUA.md`, ao concierge oficial, ou a uma avaliação real.
- [ ] **CTA presente** — a página tem um convite claro e leve para o WhatsApp, nunca ausente e nunca com urgência falsa.
- [ ] **Separação Pousada x Casa** — quando a página cobre os dois produtos, cada bloco de informação está claramente identificado a qual produto pertence.
- [ ] **Útil para hóspede real** — a página ajudaria de fato alguém a decidir ou resolver uma dúvida, não só "preencher" um tema.
- [ ] **Evita conteúdo genérico** — a página tem diferencial real da Villa Arágua/região, não frases que serviriam para qualquer pousada de qualquer lugar.
- [ ] **Evita canibalização** — não existe outra página/artigo tratando do mesmo tema de forma quase idêntica, competindo pela mesma pergunta (ver seção abaixo).

## Canibalização de temas — o que é e como evitar

Canibalização acontece quando duas ou mais páginas tentam responder à mesma pergunta principal, competindo entre si em vez de se complementarem. Sinais de canibalização:
- Duas páginas com título muito parecido (ex.: "Café da manhã na Pousada Arágua" e "Como funciona o café da manhã na Pousada").
- Duas páginas com a mesma resposta direta, apenas reescrita.
- Um cluster (`clusters-topicos.md`) com satélites que se sobrepõem em vez de aprofundar ângulos diferentes.

**Como resolver**: unir as páginas em uma versão mais forte (ver `politica-keep-update-merge-kill.md`, critério "unir"), ou diferenciar claramente o ângulo de cada uma (ex.: uma página responde "o que tem no café da manhã", outra responde "como funciona o horário do café").

## Relação entre H1/H2 em pergunta e resposta direta

Um H2 em formato de pergunta ("A Casa Arágua tem estacionamento?") só funciona bem se a resposta vier logo abaixo, direta, sem rodeio ("Sim, estacionamento exclusivo em área aberta para até 3 carros."). H2 de pergunta sem resposta direta imediatamente abaixo frustra tanto o leitor quanto a extração por IA.

## Como este checklist se diferencia do `checklist-ai-seo.md` de `villa-aragua-ai-seo-geo`

- Este arquivo (`seo-otimizacao-conteudo.md`) é a revisão **editorial**: estrutura do texto, clareza, organização básica de SEO on-page.
- `villa-aragua-ai-seo-geo/references/checklist-ai-seo.md` é a revisão de **citabilidade por IA**: se o conteúdo pode ser entendido fora de contexto, se é citável sem distorção, se schema seria aplicável.
- Na prática, um conteúdo passa primeiro por este checklist (organização editorial) e depois pelo checklist daquela skill (citabilidade avançada) antes de publicar.

## Como usar este arquivo na prática (`/content:seo`)

1. Rodar os 14 itens em qualquer página/artigo antes de considerá-lo pronto.
2. Corrigir qualquer item de estrutura (H1, H2, resposta direta, FAQ, links) diretamente no texto.
3. Verificar canibalização contra o inventário de conteúdo já existente (via `/content:audit`).
4. Encaminhar para `villa-aragua-ai-seo-geo` rodar o checklist de citabilidade avançada como última etapa antes de publicar.
