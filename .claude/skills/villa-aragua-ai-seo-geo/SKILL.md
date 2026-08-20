# Villa Arágua — AI SEO / GEO

Esta skill ensina a **estruturar conteúdo da Villa Arágua para ser mais claro, útil, buscável e citável** — em busca orgânica tradicional (Google) e em respostas geradas por IA (ChatGPT, Perplexity, Gemini, Copilot, Google AI Overviews). É uma skill de estrutura e otimização de conteúdo já decidido, não de produção de texto final nem de execução técnica automática.

**Regra mais importante da skill, acima de qualquer outra**: esta skill **nunca promete que a Villa Arágua vai aparecer** no ChatGPT, Google, Perplexity, Gemini ou AI Overviews. Ranking, posição e citação por uma IA não são controláveis nem garantíveis por ninguém — o que esta skill faz é aumentar a **clareza, a indexabilidade, a utilidade e a chance de citabilidade** do conteúdo. Toda vez que a tentação for prometer resultado de busca/IA, a resposta correta é reformular em termos de qualidade estrutural do conteúdo, não de posição garantida.

## Fontes da verdade (não alterar, só consultar)

- `DADOS_OFICIAIS_ATENDIMENTO_VILLA_ARAGUA.md` — todo dado real que pode virar FAQ ou bloco de resposta direta (distâncias, comodidades, regras, horários).
- `GUIA_DIGITAL_HOSPEDE_VILLA_ARAGUA.md` — conteúdo já estruturado da jornada do hóspede, candidato natural a virar página HTML citável (hoje é documento, não página web).
- `HISTORIA_E_POSICIONAMENTO_VILLA_ARAGUA.md` — posicionamento e história desde 2007, base de autoridade/confiança da marca.
- `ROTEIRO_RECEPCIONISTA_IA.md` e `PROMPT_RECEPCIONISTA_IA_WHATSAPP.md` — as dúvidas reais que os hóspedes trazem, matéria-prima direta de consulta de busca.
- `AGENTE_IA_MARKETING_VENDAS_META_ADS_VILLA_ARAGUA.md` — funil comercial e objetivo de reserva direta, para onde toda otimização de conteúdo aponta no fim.
- `BOMBINHAS/VILLA ARAGUA IA 📄 CONCIERGE BOMBINHAS.docx` — banco real de praias, restaurantes, trilhas, passeios — única fonte válida de dado turístico de terceiros.
- `ACOMODACOES/` e `ACOMODACOES/CASA ARAGUA/VILLA ARAGUA 📁 CASA ARÁGUA.docx` — diferenciais reais por produto.
- `AVALIACOES/` — prova social real, nunca nota/depoimento inventado.
- `.claude/skills/villa-aragua-content-strategy/` (todas as referências) — **decide o tema e a prioridade**; esta skill nunca escolhe o que criar por conta própria, sempre parte do que aquela já priorizou.
- `.claude/skills/villa-aragua-copywriting-conversion/`, `villa-aragua-humanizer-pt-br/`, `villa-aragua-sales-receptionist/`, `villa-aragua-pricing-revenue/` — fontes de texto, tom, conversa comercial e preço/oferta que qualquer página citável precisa respeitar.

**Pendência conhecida**: não existe hoje site com conteúdo publicado, blog ativo, Google Search Console configurado, nem qualquer schema/dado estruturado implementado neste projeto. Esta skill planeja e recomenda para esse destino futuro — nunca presume que a infraestrutura técnica já existe.

## Como usar esta skill

1. **Para saber que perguntas mapear** → `consultas-alvo-ai-search.md`.
2. **Para decidir estrutura de cada página do site/guia/blog** → `paginas-citaveis-villa.md`.
3. **Para escrever FAQ curta e citável** → `faq-pousada-casa-bombinhas.md`.
4. **Para o padrão de qualquer página/artigo** → `estrutura-conteudo-citavel.md`.
5. **Para pensar dado estruturado (schema) com segurança** → `schema-e-dados-estruturados.md`.
6. **Para checklist técnico de indexação/monitoramento** → `robots-crawlers-monitoramento.md`.
7. **Para conteúdo de região citável** → `guia-bombinhas-mariscal.md`.
8. **Para revisar qualquer peça antes de publicar** → `checklist-ai-seo.md`.

## O que "citável" significa aqui

Um conteúdo é citável quando uma pessoa (ou uma IA resumindo para uma pessoa) consegue extrair a resposta certa **mesmo fora do contexto da página inteira** — frase clara, dado específico, sem depender de tom, adjetivo ou parágrafo anterior para fazer sentido. Isso não é escrever "para robô" — é escrever com uma clareza que também ajuda a pessoa real, que geralmente está com pressa, no celular, decidindo rápido se aquela pousada resolve a dúvida dela.

## O que esta skill nunca faz

- Nunca promete ranking, posição de busca, aparição no ChatGPT/Google/Perplexity/Gemini/AI Overviews — fala sempre em clareza, indexabilidade, utilidade e chance de citabilidade.
- Nunca inventa preço, disponibilidade, promoção, desconto, regra, comodidade, distância, avaliação, nota, depoimento, estabelecimento, praia, restaurante ou passeio — todo dado turístico de terceiros vem do concierge oficial; todo dado da Villa Arágua vem de `DADOS_OFICIAIS_ATENDIMENTO_VILLA_ARAGUA.md`.
- Nunca mistura oferta da Pousada com a da Casa Arágua no mesmo bloco de conteúdo, nem aplica pacote de um produto ao outro automaticamente.
- Nunca chama o estacionamento da Casa Arágua de "garagem" ou "garagem coberta".
- Nunca usa urgência falsa em título, resposta direta ou CTA.
- Nunca recomenda alteração técnica (robots.txt, sitemap, schema, Search Console, código) como se já tivesse sido aplicada — toda recomendação técnica é sugestão explícita a validar antes de publicar, nunca uma ação executada por esta skill.
- Nunca cria FAQPage (ou qualquer schema) com resposta que não está visível na própria página.
- Nunca decide o tema/prioridade do conteúdo por conta própria — isso é papel de `villa-aragua-content-strategy`; esta skill estrutura o que já foi decidido.

## Separação obrigatória: dado oficial, hipótese, sugestão editorial e pendência

Toda afirmação desta skill se classifica em um dos quatro:

- **Dado oficial**: confirmado em arquivo da Villa Arágua (ex.: "Pousada Arágua fica a ~130 metros da praia, fonte `DADOS_OFICIAIS_ATENDIMENTO_VILLA_ARAGUA.md`").
- **Hipótese**: leitura razoável sobre comportamento de busca/IA, sem garantia (ex.: "hipótese: uma pergunta como 'onde ficar em Mariscal com crianças' provavelmente tem volume de busca, mas isso não foi medido").
- **Sugestão editorial**: recomendação de estrutura/formato para melhorar clareza e citabilidade (ex.: "sugestão: transformar a seção 8 do Guia Digital em página própria de FAQ").
- **Pendência**: o que falta confirmar, medir ou implementar antes de qualquer conclusão (ex.: "pendência: não existe Google Search Console configurado para medir indexação real").

## Integração com as outras skills do projeto

Esta é a décima skill do ecossistema Villa Arágua, e opera numa cadeia clara de responsabilidades:

- **`villa-aragua-content-strategy`** decide o tema e a prioridade de conteúdo — esta skill recebe esse tema e estrutura para busca, IA e citabilidade.
- **`villa-aragua-ai-seo-geo`** (esta skill) estrutura: pergunta principal, resposta direta, subtópicos, FAQ, dados estruturados sugeridos.
- **`villa-aragua-copywriting-conversion`** escreve a página, o artigo ou o bloco comercial final a partir da estrutura definida aqui.
- **`villa-aragua-humanizer-pt-br`** humaniza a linguagem do texto escrito, garantindo que a clareza técnica não vire tom robótico.
- **`villa-aragua-social-media-manager`** adapta o conteúdo estruturado para Instagram (formato bem diferente de página/FAQ).
- **`villa-aragua-creative-design-ads`** orienta imagem/vídeo de apoio quando a peça precisar.
- **`villa-aragua-sales-receptionist`** usa as FAQs e blocos de resposta direta desta skill como base para respostas no WhatsApp — consistência entre o que a página promete e o que a Recepcionista IA confirma.
- **`villa-aragua-pricing-revenue`** valida qualquer preço, oferta ou condição comercial antes de ela aparecer em página, FAQ ou schema.
- **`villa-aragua-campaign-analytics`** mede o resultado real (tráfego, leads, reservas) quando esse dado existir — esta skill nunca mede sozinha, nunca estima número de tráfego ou posição de busca.

Fluxo prático sugerido: `villa-aragua-content-strategy` decide o tema → `consultas-alvo-ai-search.md` mapeia as perguntas reais por trás dele → `paginas-citaveis-villa.md` e `estrutura-conteudo-citavel.md` definem a estrutura → `faq-pousada-casa-bombinhas.md` e `guia-bombinhas-mariscal.md` fornecem os blocos de resposta direta → `villa-aragua-copywriting-conversion` escreve → `villa-aragua-humanizer-pt-br` humaniza → `schema-e-dados-estruturados.md` sugere marcação técnica (a validar) → `checklist-ai-seo.md` revisa antes de publicar → `robots-crawlers-monitoramento.md` acompanha indexação e presença em respostas de IA depois de publicado → `villa-aragua-campaign-analytics` mede o resultado quando houver dado.

## Pendências conhecidas (sinalizar, não inventar)

- Não existe site com conteúdo publicado, blog ativo, Google Search Console ou Google Perfil da Empresa configurado documentado neste projeto — todas as recomendações técnicas desta skill são para quando essa infraestrutura existir.
- Não existe nenhum schema/dado estruturado implementado hoje.
- Não existe monitoramento histórico de como a Villa Arágua aparece (ou não) em ChatGPT, Perplexity, Gemini ou Google AI Overviews — `robots-crawlers-monitoramento.md` propõe como começar esse monitoramento manualmente, sem presumir resultado.
- Não existe análise de como concorrentes aparecem em busca/IA — `CONCORRENTES/VILLA ARAGUA IA CONCORRENTES.docx` é só lista de links do Booking, sem essa análise.
