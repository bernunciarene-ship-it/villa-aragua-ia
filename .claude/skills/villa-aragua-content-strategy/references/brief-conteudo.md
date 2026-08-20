# Brief de conteúdo

Modelo de briefing completo para qualquer conteúdo novo — acionado pelo modo `/content:brief`. Complementa `briefings-para-outras-skills.md` (que foca no formato de entrega específico por skill de execução): este arquivo é o briefing "de origem", mais completo, preenchido antes de decidir para qual skill ele vai.

## Modelo de brief

```
BRIEF DE CONTEÚDO — VILLA ARÁGUA

Título provisório: [título de trabalho, pode mudar na escrita final]
Objetivo: [atrair / educar / comparar / converter / ajudar o hóspede / apoiar reserva direta — pode ser mais de um, mas sempre com um objetivo primário claro]
Público: [casal / família / grupo / hóspede antigo / geral]
Etapa da jornada: [uma das 9 etapas de jornada-conteudo-hospede.md]
Intenção de busca: [descoberta / hospedagem / comparação / dúvida / reserva — ver consultas-alvo-ai-search.md da skill villa-aragua-ai-seo-geo]
Pergunta principal: [a consulta-alvo central que este conteúdo responde]
Resposta direta: [1-3 frases que respondem a pergunta principal, com dado oficial]
Produto relacionado: [ ] Pousada Arágua  [ ] Casa Arágua  [ ] Ambos (comparativo, em blocos identificados)  [ ] Destino/região (sem produto específico)
Dados oficiais necessários: [lista literal dos fatos a usar, com fonte — ex.: "distância 130m, fonte DADOS_OFICIAIS_ATENDIMENTO_VILLA_ARAGUA.md"]
Objeção que o conteúdo responde: [se houver, ver duvidas-objeções-como-conteudo.md]
CTA: [ação esperada, sempre leve, nunca urgência falsa]
Links internos: [para quais outras páginas/clusters este conteúdo deveria linkar]
Prova social: [se houver avaliação real aplicável — nunca inventar; se não houver, escrever "nenhuma disponível"]
Skill indicada para execução: [copywriting-conversion, na maioria dos casos; social-media-manager se o destino for só Instagram]
Pendências: [o que falta confirmar antes de publicar, se houver]
```

## Por que cada campo existe

- **Título provisório**: evita começar a escrever sem saber exatamente o que a peça promete responder.
- **Objetivo**: obriga a nomear a função do conteúdo antes de escrevê-lo — um conteúdo sem objetivo claro tende a não servir bem a nenhum propósito (ver princípio central do `SKILL.md`).
- **Etapa da jornada + intenção de busca**: garante que o conteúdo é calibrado para o momento certo do hóspede, não genérico.
- **Resposta direta**: já adianta o núcleo do que `villa-aragua-ai-seo-geo` vai estruturar como bloco citável — evita retrabalho entre as duas skills.
- **Produto relacionado**: obriga a decisão explícita de Pousada/Casa/ambos/região antes de escrever, evitando mistura de oferta no meio do texto.
- **Dados oficiais necessários**: força listar a fonte de cada fato antes de escrever, reduzindo risco de inventar dado durante a redação.
- **Objeção respondida**: conecta o conteúdo ao funil comercial real, não só à curiosidade.
- **Prova social**: obriga a checar se existe avaliação real aplicável, em vez de inventar depoimento por "completar" a peça.
- **Pendências**: qualquer lacuna de dado fica registrada, não escondida.

## Regras obrigatórias ao preencher

- Nunca inventar preço, disponibilidade, regra, comodidade, distância, estabelecimento ou depoimento — todo dado vem de `DADOS_OFICIAIS_ATENDIMENTO_VILLA_ARAGUA.md`, do concierge oficial (`BOMBINHAS/VILLA ARAGUA IA 📄 CONCIERGE BOMBINHAS.docx`) ou de `AVALIACOES/`.
- Se o brief cobrir Pousada e Casa Arágua ao mesmo tempo, marcar "Ambos (comparativo)" e garantir que cada dado no corpo do brief está etiquetado com o produto correspondente.
- Nunca chamar o estacionamento da Casa Arágua de "garagem" ou "garagem coberta" — sempre "estacionamento exclusivo em área aberta para até 3 carros".
- Se o conteúdo envolver qualquer valor/oferta, o brief precisa registrar explicitamente que isso ainda depende de validação em `villa-aragua-pricing-revenue` antes de publicar.

## Como este brief se conecta com outras skills

- Depois de preenchido, se o destino for página/artigo com potencial de busca, encaminhar também para `villa-aragua-ai-seo-geo` estruturar (pergunta principal e resposta direta já dão a base).
- A skill de execução final (`villa-aragua-copywriting-conversion` na maioria dos casos) recebe este brief como insumo principal.
- `villa-aragua-humanizer-pt-br` entra depois do texto escrito, não na etapa de brief.

## Como usar este arquivo na prática (`/content:brief`)

1. Preencher todos os campos do modelo antes de acionar qualquer skill de execução.
2. Verificar se o brief nasceu de uma lacuna identificada em `/content:audit` ou de um satélite de `/content:cluster` — sempre que possível, não brifar um tema isolado sem relação com o plano geral.
3. Validar preço/oferta em `villa-aragua-pricing-revenue`, se aplicável, antes de considerar o brief "pronto para execução".
4. Entregar o brief preenchido à skill indicada, junto com o formato específico de `briefings-para-outras-skills.md` quando o destino for uma skill diferente de `villa-aragua-copywriting-conversion`.
