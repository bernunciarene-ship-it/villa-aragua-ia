# Clusters de tópicos (topic clusters)

Estrutura de topic cluster — uma página pilar central + conteúdos satélites que aprofundam subtemas e linkam de volta para o pilar — acionada pelo modo `/content:cluster`. Este arquivo organiza os 10 clusters no formato de cluster completo; os dados de origem (praias, restaurantes, diferenciais de produto, dúvidas) continuam vindo de `clusters-bombinhas-mariscal.md`, `conteudo-pousada-casa.md`, `duvidas-objeções-como-conteudo.md` e `temas-sazonais-feriados.md` — este arquivo não duplica esses dados, apenas os organiza em formato de cluster (pilar + satélites + links internos).

## Por que topic cluster, e não só lista de temas

Um cluster ajuda tanto o hóspede quanto a busca/IA a entender que vários conteúdos menores fazem parte de um mesmo assunto maior — a página pilar responde à pergunta ampla, as satélites aprofundam pontos específicos e sempre linkam de volta. Isso evita conteúdo solto sem hierarquia, e fortalece a página pilar como referência central do tema (ver `villa-aragua-ai-seo-geo/references/estrutura-conteudo-citavel.md` para o padrão de estrutura de cada página).

## Modelo de ficha de cluster

```
CLUSTER: [nome do pilar]
Página pilar: [título/tema central]
Conteúdos satélites: [lista de subtemas]
Perguntas respondidas: [lista, ver consultas-alvo-ai-search.md da skill villa-aragua-ai-seo-geo]
Intenção de busca: [descoberta / hospedagem / comparação / dúvida / reserva]
Público: [casal / família / grupo / geral]
CTA: [ação esperada]
Links internos sugeridos: [para quais outras páginas/pilares esta página deveria linkar]
```

## Os 10 clusters

### Cluster — Praia de Mariscal
- Página pilar: "Praia de Mariscal: o que esperar e por que ela é boa para família"
- Satélites: distância até a Pousada (~130m) e até a Casa (~250m); outras praias próximas (Canto Grande, Tainha, Quatro Ilhas, Sepultura); roteiro de um dia na praia.
- Perguntas respondidas: "Praia de Mariscal é boa para família?", "Onde se hospedar perto da Praia de Mariscal?".
- Intenção: descoberta do destino.
- Público: geral, ênfase família.
- CTA: conhecer a Pousada/Casa como opção de hospedagem na região.
- Links internos: página da Pousada, página da Casa, guia de Bombinhas.

### Cluster — Bombinhas
- Página pilar: "Guia de Bombinhas: onde ficar, o que fazer, quando ir"
- Satélites: dias de chuva, roteiro de casal, roteiro com crianças, baixa temporada, restaurantes/passeios/trilhas (ver `clusters-bombinhas-mariscal.md`).
- Perguntas respondidas: "Onde ficar em Bombinhas para descansar?", "Qual melhor praia de Bombinhas para família?".
- Intenção: descoberta do destino.
- Público: geral.
- CTA: conhecer Mariscal e a Villa Arágua.
- Links internos: cluster Praia de Mariscal, cluster Pousada Arágua, cluster Casa Arágua.

### Cluster — Pousada Arágua
- Página pilar: "Pousada Arágua: pousada com café da manhã na acomodação em Mariscal"
- Satélites: as 8 acomodações, piscina comum, área de lazer, estacionamento por acomodação, FAQ da Pousada.
- Perguntas respondidas: "Pousada em Mariscal com café da manhã?", "Pousada com café servido na acomodação em Bombinhas existe?".
- Intenção: hospedagem.
- Público: casais, famílias pequenas.
- CTA: falar no WhatsApp, ver disponibilidade.
- Links internos: cluster Casa Arágua (comparativo), cluster reserva direta, FAQ.

### Cluster — Casa Arágua
- Página pilar: "Casa Arágua: casa completa com piscina privativa em Mariscal"
- Satélites: piscina privativa, churrasqueira, cozinha completa, estacionamento exclusivo em área aberta (nunca "garagem"), taxa de limpeza, FAQ da Casa (incluindo por que não há café da manhã).
- Perguntas respondidas: "Casa em Bombinhas com piscina privativa para até 6 pessoas?", "Casa com churrasqueira em Bombinhas vale a pena?".
- Intenção: hospedagem.
- Público: famílias grandes, grupos.
- CTA: falar no WhatsApp.
- Links internos: cluster Pousada Arágua (comparativo), cluster reserva direta, FAQ.

### Cluster — Viagem com crianças
- Página pilar: "Onde ficar em Mariscal com crianças"
- Satélites: estrutura da Pousada (playground, área de lazer), capacidade da Casa Arágua para família grande, roteiro de praia com crianças (ver `clusters-bombinhas-mariscal.md`).
- Perguntas respondidas: "Onde ficar em Mariscal com crianças?".
- Intenção: família.
- Público: família.
- CTA: falar no WhatsApp para indicar a melhor opção conforme o grupo.
- Links internos: cluster Pousada Arágua, cluster Casa Arágua, cluster Praia de Mariscal.

### Cluster — Viagem em casal
- Página pilar: "Bombinhas e Mariscal para casais: onde ficar e o que fazer"
- Satélites: suítes indicadas para casal na Pousada, roteiro romântico (pôr do sol, jantar — ver concierge), Dia dos Namorados (ver `temas-sazonais-feriados.md`).
- Perguntas respondidas: variações de "onde ficar em Bombinhas para um casal" (hipótese de busca, ver `villa-aragua-ai-seo-geo/references/consultas-alvo-ai-search.md`).
- Intenção: casal.
- Público: casal.
- CTA: falar no WhatsApp.
- Links internos: cluster Pousada Arágua, cluster Bombinhas.

### Cluster — Grupos/famílias
- Página pilar: "Casa Arágua para grupos e famílias grandes em Bombinhas"
- Satélites: capacidade até 6 pessoas, privacidade, Duplex Soleil como alternativa dentro da Pousada (até 5 pessoas), comparativo de capacidade.
- Perguntas respondidas: "Casa em Bombinhas com piscina privativa para até 6 pessoas?".
- Intenção: grupo.
- Público: grupo, família grande.
- CTA: falar no WhatsApp.
- Links internos: cluster Casa Arágua, cluster Pousada Arágua.

### Cluster — Reserva direta
- Página pilar: "Vale reservar direto ou pelo Booking/Airbnb?"
- Satélites: vantagens da reserva direta, como funciona o processo, diferença de política de cada canal.
- Perguntas respondidas: "Vale reservar direto ou pelo Booking/Airbnb?".
- Intenção: reserva direta.
- Público: geral.
- CTA: chamar no WhatsApp oficial.
- Links internos: cluster Pousada Arágua, cluster Casa Arágua, FAQ.

### Cluster — Feriados e temporadas
- Página pilar: variável por data (ver `temas-sazonais-feriados.md` para status oficial de cada uma).
- Satélites: conteúdo de utilidade sobre a data na região, conteúdo comercial quando houver oferta confirmada.
- Perguntas respondidas: variam por feriado/temporada.
- Intenção: comercial/sazonal.
- Público: geral.
- CTA: reserva antecipada, sem urgência falsa.
- Links internos: cluster Pousada Arágua ou Casa Arágua (conforme o produto da oferta), nunca ambos misturados na mesma oferta.

### Cluster — Dúvidas frequentes
- Página pilar: "Perguntas frequentes: Pousada Arágua e Casa Arágua"
- Satélites: cada dúvida de `duvidas-objeções-como-conteudo.md` (café, pet, criança, estacionamento, check-in, desconto, distância).
- Perguntas respondidas: todas as consultas de dúvida/objeção já mapeadas.
- Intenção: dúvida.
- Público: geral.
- CTA: falar no WhatsApp para o que não estiver coberto.
- Links internos: todos os outros clusters relevantes por tema.

## Regra de ouro em qualquer cluster

Sempre que um cluster cobrir Pousada e Casa Arágua ao mesmo tempo (ex.: "Viagem com crianças", "Grupos/famílias", "Reserva direta"), cada satélite precisa deixar explícito a qual produto pertence cada comodidade/regra citada — nunca generalizar como se as duas fossem uma coisa só. O estacionamento da Casa é sempre "estacionamento exclusivo em área aberta para até 3 carros", nunca "garagem" ou "garagem coberta".

## Como este arquivo se relaciona com `villa-aragua-ai-seo-geo`

Esta skill organiza os clusters (o quê, para quem, por quê); `villa-aragua-ai-seo-geo` estrutura cada página do cluster no formato citável (resposta direta, FAQ, subtópicos — ver `estrutura-conteudo-citavel.md` daquela skill) e sugere dados estruturados quando fizer sentido. As duas trabalham sobre a mesma lista de clusters, nunca clusters diferentes — esta skill não altera nada de `villa-aragua-ai-seo-geo`, apenas entrega o tema já organizado para ela estruturar.

## Como usar este arquivo na prática (`/content:cluster`)

1. Escolher o cluster relevante para o ciclo de conteúdo atual.
2. Confirmar que a página pilar existe (ou está no plano) antes de criar conteúdo satélite solto.
3. Gerar o briefing de cada satélite com `brief-conteudo.md`.
4. Garantir que todo satélite linka de volta para a página pilar, e a pilar linka para os satélites relevantes.
5. Encaminhar para `villa-aragua-ai-seo-geo` estruturar e depois para a skill de execução escrever.
