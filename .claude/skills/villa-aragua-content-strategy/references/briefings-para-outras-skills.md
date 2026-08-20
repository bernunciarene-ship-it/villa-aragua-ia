# Briefings para outras skills

Esta skill decide o quê criar e por quê; estes modelos são a entrega — o que passar para cada skill de execução transformar em peça final. Nenhum briefing deve incluir preço, oferta ou dado turístico não confirmado; se algo estiver pendente, o briefing sinaliza isso explicitamente em vez de presumir.

## Modelo geral de briefing (base para todos)

```
BRIEFING DE CONTEÚDO — VILLA ARÁGUA

Tema: [tema específico]
Pilar: [um dos 12 pilares de pilares-conteudo-villa.md]
Tipo de conteúdo: [informativo / inspiracional / comparativo / comercial]
Etapa da jornada: [uma das 9 etapas de jornada-conteudo-hospede.md]
Produto: [ ] Pousada Arágua  [ ] Casa Arágua  [ ] Marca/região (sem produto específico)  [ ] Comparativo (os dois, em blocos identificados)
Público-alvo: [casal / família / grupo / hóspede antigo / geral]
Canal de destino: [site / blog / guia digital / Instagram / Meta Ads / WhatsApp]
CTA esperado: [nenhum / ler mais / chamar no WhatsApp / seguir perfil]
Dados oficiais a usar: [lista literal dos fatos confirmados a incluir, com fonte]
O que NÃO incluir: [preço fechado, oferta não confirmada, depoimento inventado, comparação de concorrente nomeado — o que for aplicável]
Pendências sinalizadas: [o que falta confirmar antes de publicar, se houver]
```

## Briefing para `villa-aragua-copywriting-conversion`

Usar quando o destino final é texto de site, blog, página comparativa ou FAQ. Além do modelo geral, incluir:
- Estrutura esperada (página institucional, artigo de blog, FAQ com perguntas e respostas).
- Objeção principal que o texto precisa neutralizar, se houver (ver `duvidas-objeções-como-conteudo.md`).
- Se o texto vai citar preço: confirmar que já passou por `villa-aragua-pricing-revenue` antes de briefar.

## Briefing para `villa-aragua-social-media-manager`

Usar quando o destino é Instagram (feed, reels, stories, carrossel). Além do modelo geral, incluir:
- Em qual pilar do calendário editorial daquela skill o tema se encaixa (ela tem seus próprios 12 pilares específicos de Instagram).
- Se o tema já foi tratado recentemente em outro canal (para adaptar, não repetir igual).

## Briefing para `villa-aragua-creative-design-ads`

Usar sempre que o conteúdo precisar de direção visual (imagem, vídeo, carrossel) além de texto simples. Além do modelo geral, incluir:
- Referências visuais reais disponíveis (pasta de fotos/vídeos da acomodação, criativos já produzidos).
- Se é conteúdo pago (Meta Ads) ou orgânico — muda o tipo de peça e o formato esperado.

## Briefing para `villa-aragua-humanizer-pt-br`

Usar como última etapa, depois que o texto já foi escrito por `villa-aragua-copywriting-conversion` ou pela skill de execução correspondente. Incluir:
- O texto já escrito.
- Canal de destino (o tom varia um pouco entre site institucional e Instagram/WhatsApp, ver `villa-aragua-humanizer-pt-br/references/tom-de-voz-villa-aragua.md`).

## Briefing para `villa-aragua-sales-receptionist`

Usar quando o conteúdo precisa gerar uma mensagem inicial de WhatsApp coerente com o que foi publicado (ex.: uma campanha de feriado, um anúncio, um post de reserva direta). Incluir:
- A promessa exata feita no conteúdo publicado (para a Recepcionista IA confirmar a mesma coisa, sem desencontro).
- Objeções esperadas relacionadas ao tema (ver `duvidas-objeções-como-conteudo.md`).

## Briefing para `villa-aragua-ai-seo-geo` (quando existir)

Até essa skill ser criada, este briefing fica registrado como pendência de otimização técnica — não é executável ainda. Estrutura prevista:
- Tema e cluster de origem (`clusters-bombinhas-mariscal.md` ou outro).
- Intenção de busca provável (informacional, comparativa, transacional).
- Formato de resposta direta esperado (útil para IA generativa responder bem sobre a Villa Arágua).
- Palavras/expressões reais que hóspedes usam para essa dúvida (extraídas do WhatsApp, quando disponível).

## Como sequenciar múltiplos briefings para o mesmo tema

Muitos temas viram mais de uma peça (ex.: um artigo de blog + um post de Instagram + uma resposta padrão de WhatsApp, todos sobre "café da manhã na Pousada"). Nesse caso:
1. Gerar primeiro o briefing "de origem" (geralmente o mais completo, para `villa-aragua-copywriting-conversion` ou `villa-aragua-social-media-manager`).
2. Gerar os briefings derivados citando a peça de origem, para manter consistência entre canais.
3. Fechar com o briefing de humanização como última etapa de todos.

## Como usar este arquivo na prática

1. Depois de definir o tema no calendário (`calendario-conteudo-mensal.md`), escolher o(s) briefing(s) necessário(s) conforme o(s) canal(is) de destino.
2. Preencher cada campo com dado real — nunca deixar em branco silenciosamente; se faltar dado, escrever "pendente: [o que falta]".
3. Entregar o briefing para a skill de execução indicada — esta skill não escreve a partir daqui, apenas prepara o terreno.
