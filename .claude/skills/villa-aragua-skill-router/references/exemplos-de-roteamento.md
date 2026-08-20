# Exemplos de roteamento

Casos práticos de pedido → roteamento, para calibrar o comportamento do router em situações reais. Usar como modelo de formato de resposta (ver `SKILL.md`, seção "Formatos de saída").

## Exemplo 1

**Pedido**: "Preciso analisar minhas campanhas Meta Ads."

**Roteamento**:
- Principal: `villa-aragua-campaign-analytics`.
- Apoio: `villa-aragua-pricing-revenue` se a análise envolver receita/ROAS; `villa-aragua-creative-design-ads` se houver avaliação de criativo; `villa-aragua-copywriting-conversion` se houver revisão de copy.
- Formato de saída: tarefa simples a média — "Vou usar principalmente `villa-aragua-campaign-analytics`. Apoio: `villa-aragua-pricing-revenue`, se envolver receita/margem." seguido da análise.

## Exemplo 2

**Pedido**: "Responda esse cliente que pediu desconto."

**Roteamento**:
- Principal: `villa-aragua-sales-receptionist`.
- Apoio: `villa-aragua-pricing-revenue` (validar se há margem/condição) + `villa-aragua-humanizer-pt-br` (tom final).
- Formato de saída: tarefa simples — "Vou usar principalmente `villa-aragua-sales-receptionist`. Apoio: `villa-aragua-pricing-revenue` e `villa-aragua-humanizer-pt-br`." seguido da resposta pronta.

## Exemplo 3

**Pedido**: "Crie uma página sobre onde ficar em Mariscal com crianças."

**Roteamento**:
- Principal: `villa-aragua-content-strategy` (decide o tema/briefing).
- Apoio: `villa-aragua-ai-seo-geo` (estrutura citável) + `villa-aragua-copywriting-conversion` (texto final) + `villa-aragua-humanizer-pt-br` (humanização).
- Formato de saída: tarefa complexa (Fluxo C/F de `fluxos-de-trabalho.md`) — "Fluxo recomendado: 1) `villa-aragua-content-strategy`, 2) `villa-aragua-ai-seo-geo`, 3) `villa-aragua-copywriting-conversion`, 4) `villa-aragua-humanizer-pt-br`." seguido da execução ou do plano.

## Exemplo 4

**Pedido**: "Monte calendário de Instagram da semana."

**Roteamento**:
- Principal: `villa-aragua-social-media-manager`.
- Apoio: `villa-aragua-copywriting-conversion` (legendas) + `villa-aragua-creative-design-ads` (direção visual) + `villa-aragua-humanizer-pt-br` (revisão de tom).
- Formato de saída: tarefa complexa (Fluxo D) — "Fluxo recomendado: 1) `villa-aragua-social-media-manager`, 2) `villa-aragua-copywriting-conversion`, 3) `villa-aragua-creative-design-ads`, 4) `villa-aragua-humanizer-pt-br`." seguido do calendário.

## Exemplo 5

**Pedido**: "Quero melhorar esse anúncio da Casa Arágua."

**Roteamento**:
- Principal: `villa-aragua-copywriting-conversion`.
- Apoio: `villa-aragua-creative-design-ads` (se envolver a parte visual) + `villa-aragua-pricing-revenue` (se houver oferta citada no anúncio) + `villa-aragua-humanizer-pt-br` (tom final).
- Atenção: o anúncio é da Casa Arágua — qualquer revisão precisa manter os diferenciais corretos da Casa (piscina privativa, estacionamento exclusivo em área aberta — nunca "garagem") e não misturar com oferta da Pousada.
- Formato de saída: tarefa simples a média — "Vou usar principalmente `villa-aragua-copywriting-conversion`. Apoio: `villa-aragua-creative-design-ads` e `villa-aragua-humanizer-pt-br` (e `villa-aragua-pricing-revenue` se houver oferta no anúncio)." seguido da revisão.

## Exemplo 6

**Pedido**: "Qual skill uso para isso?"

**Roteamento**:
- Formato de saída (modelo de dúvida): "A skill principal é [X]. Use [Y] como apoio se tiver preço/desconto/dados/criativo." — sempre pedindo, se necessário, um detalhe a mais do pedido original para confirmar a intenção antes de responder com certeza.

## Exemplo 7

**Pedido**: "Por que esse lead sumiu depois do orçamento?"

**Roteamento**:
- Principal: `villa-aragua-marketing-psychology` (entender o comportamento).
- Apoio: `villa-aragua-sales-receptionist` (aplicar o diagnóstico num follow-up real).
- Formato de saída: tarefa simples — "Vou usar principalmente `villa-aragua-marketing-psychology`. Apoio: `villa-aragua-sales-receptionist` para aplicar na prática." seguido da análise.

## Exemplo 8

**Pedido**: "Monta um plano de crescimento para os próximos 90 dias."

**Roteamento**:
- Principal: `villa-aragua-growth-marketer`.
- Apoio: `villa-aragua-pricing-revenue` (validar ofertas do plano) + `villa-aragua-campaign-analytics` (medir resultado ao longo do plano).
- Formato de saída: tarefa complexa (Fluxo G) — "Fluxo recomendado: 1) `villa-aragua-growth-marketer`, 2) `villa-aragua-pricing-revenue`, 3) `villa-aragua-campaign-analytics` (para medir depois)." seguido do plano.

## Exemplo 9

**Pedido**: "Cria o anúncio da Casa e já analisa se valeria a pena escalar depois."

**Roteamento**:
- Este é um pedido composto — duas intenções em sequência, não simultâneas.
- Primeira parte ("cria o anúncio"): principal `villa-aragua-copywriting-conversion`, apoio `villa-aragua-creative-design-ads` + `villa-aragua-humanizer-pt-br`.
- Segunda parte ("analisa se valeria a pena escalar depois"): isso só pode ser respondido depois de existir dado real de desempenho — sinalizar que `villa-aragua-campaign-analytics` entra **depois** de o anúncio rodar, não antes; não simular ou inventar um resultado agora.
- Formato de saída: "Fluxo recomendado: 1) `villa-aragua-copywriting-conversion` + `villa-aragua-creative-design-ads` + `villa-aragua-humanizer-pt-br` (criar o anúncio agora); 2) `villa-aragua-campaign-analytics` (medir depois de rodar, quando houver dado real)."

## Exemplo 10 — quando falta uma skill

**Pedido**: "Configura o disparo automático de e-mail marketing para hóspedes antigos."

**Roteamento**:
- Não existe, hoje, nenhuma skill de e-mail marketing no ecossistema (`.claude/skills/` não tem essa skill).
- Resposta correta: sinalizar que essa função específica (disparo automatizado de e-mail) não tem skill dedicada ainda; a aproximação mais próxima é `villa-aragua-growth-marketer/references/reativacao-hospedes-antigos.md`, que cobre a estratégia de reativação (mensagem, cadência, tom), mas não a automação técnica de envio.
- Nunca inventar uma skill "villa-aragua-email-marketing" que não existe.

## Como usar este arquivo na prática

1. Localizar o exemplo mais parecido com o pedido real recebido.
2. Adaptar o roteamento ao caso específico (produto, canal, dado envolvido).
3. Usar o formato de saída correspondente (simples, complexo, ou dúvida) conforme `SKILL.md`.
4. Se o pedido não se parecer com nenhum exemplo, montar o roteamento do zero com `matriz-intencoes-skills.md` e `regras-de-prioridade.md`.
