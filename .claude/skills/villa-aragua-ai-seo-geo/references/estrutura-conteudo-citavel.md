# Estrutura de conteúdo citável

Padrão de estrutura para qualquer página ou artigo da Villa Arágua, pensado para ser lido bem por uma pessoa com pressa e resumido bem por uma IA. Esta skill define a estrutura; `villa-aragua-copywriting-conversion` escreve o texto dentro dela.

## O padrão (13 elementos)

1. **Título claro** — descreve exatamente o que a página responde, sem jogo de palavras (ex.: "Casa Arágua: casa com piscina privativa em Mariscal, Bombinhas" em vez de algo poético e vago).
2. **Resposta direta no primeiro parágrafo** — a pergunta principal (ver `paginas-citaveis-villa.md`) respondida em 1-3 frases, antes de qualquer contexto ou história.
3. **Resumo rápido** — opcional, mas útil em páginas longas: 3-5 bullets com os pontos centrais, logo após a resposta direta.
4. **Subtítulos em forma de pergunta** — cada seção responde a uma sub-pergunta real (ex.: "Quantas pessoas a Casa Arágua acomoda?"), facilitando tanto a leitura humana quanto a extração por IA.
5. **Listas curtas** — comodidades, diferenciais, horários — sempre que a informação for enumerável, usar lista em vez de parágrafo corrido.
6. **Comparativos claros** — quando a página compara (Pousada x Casa, direto x OTA), usar tabela ou lista lado a lado, nunca comparação diluída em texto corrido.
7. **Dados oficiais** — toda afirmação de fato (distância, capacidade, horário) precisa vir de `DADOS_OFICIAIS_ATENDIMENTO_VILLA_ARAGUA.md` ou do concierge oficial.
8. **Diferenciais reais** — o que torna aquele produto/lugar específico, não descrição genérica de hotelaria.
9. **Links internos sugeridos** — para a página do produto irmão (Pousada ↔ Casa), para o guia de região, para a página de reserva direta.
10. **FAQ no final** — 3-6 perguntas curtas (ver `faq-pousada-casa-bombinhas.md`), no formato pergunta-resposta direta.
11. **CTA leve para WhatsApp** — convite, não pressão; nunca urgência falsa.
12. **Atualização e revisão periódica** — marcar quando o conteúdo foi revisado pela última vez (mentalmente ou em nota interna), porque dado de preço/regra pode mudar.
13. **Separação entre Pousada e Casa** — sempre que a página cobrir os dois produtos, usar seções/blocos claramente identificados, nunca misturar frase a frase.

## Por que essa estrutura ajuda tanto humano quanto IA

Uma pessoa com pressa lê o título, a resposta direta e o resumo, e já decide se continua lendo. Uma IA generativa que resume ou cita a página tende a extrair exatamente esses mesmos elementos (resposta direta, listas, FAQ) porque são as partes mais fáceis de isolar sem perder sentido. Não existe truque separado para "escrever para IA" — a mesma clareza que ajuda a pessoa real ajuda a citabilidade.

## Exemplos de estrutura aplicada

### Página da Casa Arágua
1. Título: "Casa Arágua: casa completa com piscina privativa em Mariscal, Bombinhas"
2. Resposta direta: casa privativa para até 6 pessoas, piscina privativa, a ~250m da praia.
3. Resumo rápido: piscina privativa, churrasqueira, cozinha completa, estacionamento exclusivo (até 3 carros), arquitetura balinesa.
4. Subtítulos: "Quantas pessoas acomoda?", "Tem piscina privativa?", "Como funciona o estacionamento?", "Tem café da manhã incluso?".
5. Comparativo (se aplicável): bloco/link para a página comparativa Pousada x Casa.
6. FAQ: ver bloco Casa em `faq-pousada-casa-bombinhas.md`.
7. CTA: falar no WhatsApp para verificar disponibilidade.

### Página da Pousada Arágua
1. Título: "Pousada Arágua: pousada com café da manhã na acomodação em Mariscal, Bombinhas"
2. Resposta direta: pousada boutique de 8 acomodações, café sempre incluso e entregue na suíte, a ~130m da praia.
3. Resumo rápido: café incluso, piscina comum, área de lazer, estacionamento por acomodação.
4. Subtítulos: "O café da manhã está incluso?", "A piscina é privativa?", "Quantas acomodações existem?".
5. FAQ: ver bloco Pousada em `faq-pousada-casa-bombinhas.md`.
6. CTA: falar no WhatsApp.

### Página Pousada x Casa
1. Título: "Pousada Arágua ou Casa Arágua: qual escolher em Bombinhas"
2. Resposta direta: resumo de 1-2 frases do critério central (praticidade com café incluso x privacidade de casa completa).
3. Comparativo: tabela lado a lado (ver `villa-aragua-content-strategy/references/conteudo-pousada-casa.md`).
4. Subtítulos: "Qual escolher para uma família pequena?", "Qual escolher para um grupo de amigos?".
5. FAQ: perguntas de decisão (ver `faq-pousada-casa-bombinhas.md`).
6. CTA: falar no WhatsApp para ajudar a decidir.

### Guia de Mariscal
1. Título: "Guia de Mariscal, Bombinhas: praias, restaurantes e passeios"
2. Resposta direta: Mariscal é uma região tranquila de Bombinhas, indicada para família e caminhada, onde fica a Villa Arágua.
3. Subtítulos: "Qual a praia de Mariscal?", "Onde comer perto de Mariscal?", "O que fazer em dias de chuva?".
4. Listas: praias próximas, restaurantes, passeios, trilhas (ver `guia-bombinhas-mariscal.md`).
5. FAQ: "A Praia de Mariscal é boa para família?", "Como chegar em Mariscal?".
6. CTA: conhecer a Villa Arágua como hospedagem na região.

### Artigo "O que fazer em Bombinhas com chuva"
1. Título: "O que fazer em Bombinhas em dia de chuva"
2. Resposta direta: lista curta logo no início (cafés, sorveterias, aquário, pizzarias, compras em Porto Belo, cinema em Balneário Camboriú).
3. Subtítulos: um por categoria de atividade.
4. FAQ: "Bombinhas tem cinema?", "O que fazer perto de Mariscal quando chove?".
5. CTA leve: convite para conhecer a Villa Arágua (indireto, o artigo é de utilidade, não de venda direta).

### Artigo "Onde ficar em Mariscal com crianças"
1. Título: "Onde ficar em Mariscal, Bombinhas, com crianças"
2. Resposta direta: Mariscal é indicada para família; a Villa Arágua oferece Pousada Arágua (área de lazer, playground) e Casa Arágua (espaço privativo para grupo).
3. Subtítulos: "A Pousada tem estrutura para criança?", "A Casa Arágua é uma boa opção para família grande?".
4. FAQ: perguntas de família (ver `faq-pousada-casa-bombinhas.md`).
5. CTA: falar no WhatsApp.

## O que este padrão nunca faz

- Nunca sacrifica clareza por criatividade — título e resposta direta sempre priorizam ser entendidos rápido.
- Nunca omite a diferenciação Pousada/Casa numa página que cobre os dois.
- Nunca usa CTA com urgência falsa ("últimas vagas", contagem regressiva sem data real).
- Nunca insere dado que não veio de fonte oficial só para "completar" uma seção.

## Como usar este arquivo na prática

1. Aplicar os 13 elementos a qualquer página nova ou revisão de página existente.
2. Usar os exemplos como modelo direto para as páginas mais prioritárias (Pousada, Casa, comparativa, guia de região).
3. Encaminhar a estrutura preenchida para `villa-aragua-copywriting-conversion` escrever o texto final.
4. Rodar `checklist-ai-seo.md` como última verificação antes de publicar.
