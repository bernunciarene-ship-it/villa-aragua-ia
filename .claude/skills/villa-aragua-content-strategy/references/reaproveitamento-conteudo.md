# Reaproveitamento de conteúdo

Lógica para transformar um conteúdo principal já validado em várias peças, por canal — acionada pelo modo `/content:repurpose`. Evita recriar do zero em cada canal e garante consistência entre o que o site diz, o que o Instagram mostra e o que o WhatsApp confirma.

## Princípio central

Um bom conteúdo de origem (uma página, um artigo, um brief bem feito) carrega informação suficiente para alimentar formatos bem diferentes — mas cada formato exige adaptação real, não cópia mecânica. Reaproveitar não é publicar o mesmo texto em lugares diferentes; é extrair o núcleo (pergunta, resposta, dado oficial) e reconstruir na linguagem certa de cada canal.

## Os onze destinos possíveis de reaproveitamento

1. **Página do site** — versão completa, com todos os subtópicos e FAQ (ver `villa-aragua-ai-seo-geo/references/estrutura-conteudo-citavel.md`).
2. **Artigo de blog** — versão de profundidade média, focada numa única pergunta central.
3. **FAQ** — a resposta direta extraída e reduzida a 1-3 frases (ver `faq-pousada-casa-bombinhas.md` da skill `villa-aragua-ai-seo-geo`).
4. **Post de Instagram** — versão curta com uma imagem/gancho visual, legenda reduzida (ver `villa-aragua-social-media-manager`).
5. **Carrossel** — quando o conteúdo tem vários subtópicos/comparações, cada um vira um cartão.
6. **Reels** — quando o conteúdo tem elemento visual/de movimento (tour, bastidor, dica em vídeo).
7. **Stories** — versão ainda mais reduzida, espontânea, ou usada para enquete/caixa de perguntas sobre o mesmo tema.
8. **Mensagem de WhatsApp** — versão de resposta rápida, no tom da Recepcionista IA, para quando o tema surgir numa conversa real.
9. **Resposta da Recepcionista IA** — incorporação do dado/resposta ao roteiro de atendimento (`villa-aragua-sales-receptionist`), garantindo que a IA responde de forma consistente com o que está publicado.
10. **Copy de anúncio** — versão comercial direta, com CTA mais forte, sempre validando qualquer preço/oferta em `villa-aragua-pricing-revenue` antes de usar em Meta Ads.
11. **E-mail ou mensagem para hóspede antigo** — versão de reconexão, tom mais pessoal (ver `villa-aragua-growth-marketer/references/reativacao-hospedes-antigos.md`).

## Exemplo aplicado: "Onde ficar em Mariscal com crianças"

Partindo de um conteúdo de origem (página ou brief já validado), o mesmo tema pode virar:

- **Página SEO**: "Onde ficar em Mariscal com crianças" — página completa com resposta direta, comparação Pousada x Casa para famílias, FAQ.
- **Carrossel Instagram**: cartão 1 = pergunta/gancho ("Viajando com crianças para Mariscal?"), cartões seguintes = Pousada (playground, área de lazer) e Casa (espaço privativo), último cartão = CTA.
- **FAQ**: "A Pousada Arágua tem estrutura para criança?" com resposta direta de 1-2 frases.
- **Mensagem de WhatsApp**: versão que a Recepcionista IA usa quando um lead menciona viajar com filhos — puxando diagnóstico (idade das crianças, número de pessoas) antes de indicar produto.
- **Anúncio Meta Ads**: copy focada no público família, com CTA para o WhatsApp, ângulo validado com `villa-aragua-copywriting-conversion` e `villa-aragua-pricing-revenue`.
- **Story com enquete**: "Vocês preferem playground (Pousada) ou espaço só para a família (Casa)?" — engajamento leve, reforçando os dois produtos sem empurrar um sobre o outro.
- **Bloco do guia digital**: nota prática para quem já reservou e quer saber o que esperar da estrutura para crianças durante a estadia.

## Regras de reaproveitamento

- Nunca reaproveitar um conteúdo que ainda não foi validado quanto a dado oficial — o núcleo precisa estar correto antes de virar sete formatos diferentes com o mesmo erro.
- Sempre adaptar o tom ao canal (ver `villa-aragua-humanizer-pt-br` para a diferença de tom entre site institucional, Instagram e WhatsApp).
- Nunca reaproveitar oferta/pacote de um produto para o outro — se o conteúdo de origem é da Pousada, os reaproveitamentos continuam sendo da Pousada, a menos que o conteúdo de origem já fosse comparativo.
- Sempre que o reaproveitamento envolver preço/oferta (ex.: copy de anúncio), validar em `villa-aragua-pricing-revenue` antes de publicar, mesmo que o conteúdo de origem já tenha sido validado — condições podem mudar entre o conteúdo original e o reaproveitamento.
- Reaproveitar não é obrigatório em todos os onze formatos para todo conteúdo — escolher os destinos que fazem sentido para aquele tema específico e para o momento do calendário (`calendario-30-60-90.md` / `calendario-conteudo-mensal.md`).

## Como decidir quais destinos priorizar

1. O conteúdo de origem já está validado (dado oficial, estrutura, CTA)?
2. Qual etapa da jornada ele serve mais fortemente (ver `jornada-conteudo-hospede.md`) — isso indica se o reaproveitamento prioritário é de topo (Instagram, blog) ou de fundo de funil (WhatsApp, FAQ, anúncio)?
3. Existe capacidade real de produção para todos os formatos, ou é melhor escolher 2-3 destinos de maior impacto agora e deixar os demais para depois?

## Como usar este arquivo na prática (`/content:repurpose`)

1. Escolher o conteúdo de origem já validado (de `/content:brief` ou de uma página/artigo já publicado).
2. Selecionar os destinos de reaproveitamento relevantes para o momento.
3. Para cada destino, adaptar tom e formato (nunca copiar o texto integral sem ajuste).
4. Encaminhar cada peça para a skill de execução correta (`villa-aragua-social-media-manager` para Instagram, `villa-aragua-sales-receptionist` para WhatsApp/Recepcionista, `villa-aragua-copywriting-conversion` para anúncio/site, `villa-aragua-humanizer-pt-br` para revisão de tom final).
