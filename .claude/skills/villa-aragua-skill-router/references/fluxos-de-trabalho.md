# Fluxos de trabalho

Sequências prontas de skills para os cenários mais comuns — usar como ponto de partida sempre que o pedido encaixar num destes fluxos, ajustando etapas conforme o caso real (nem todo fluxo precisa das 100% das etapas).

## Fluxo A — Campanha Meta Ads completa

1. `villa-aragua-pricing-revenue` — validar/definir preço, pacote, oferta.
2. `villa-aragua-copywriting-conversion` — escrever a copy do anúncio.
3. `villa-aragua-creative-design-ads` — definir direção visual do criativo.
4. `villa-aragua-humanizer-pt-br` — humanizar o texto final.
5. `villa-aragua-sales-receptionist` — garantir que a primeira mensagem de WhatsApp confirma exatamente o que o anúncio promete.
6. `villa-aragua-campaign-analytics` — medir resultado depois de publicado.

## Fluxo B — Lead no WhatsApp

1. `villa-aragua-sales-receptionist` — conduzir a conversa/objeção.
2. `villa-aragua-pricing-revenue` — se houver preço, desconto ou condição especial envolvida.
3. `villa-aragua-humanizer-pt-br` — revisar tom antes de enviar.

## Fluxo C — Conteúdo de site/blog/guia digital

1. `villa-aragua-content-strategy` — decidir o tema e o briefing.
2. `villa-aragua-ai-seo-geo` — estruturar para busca e citabilidade.
3. `villa-aragua-copywriting-conversion` — escrever o texto final.
4. `villa-aragua-humanizer-pt-br` — humanizar.

## Fluxo D — Instagram orgânico

1. `villa-aragua-social-media-manager` — decidir pilar, formato e calendário.
2. `villa-aragua-copywriting-conversion` — escrever legenda/CTA.
3. `villa-aragua-creative-design-ads` — direção visual.
4. `villa-aragua-humanizer-pt-br` — humanizar.

## Fluxo E — Análise de campanha

1. `villa-aragua-campaign-analytics` — ler métricas e funil.
2. `villa-aragua-pricing-revenue` — avaliar retorno/margem, se aplicável.
3. `villa-aragua-sales-receptionist` — investigar gargalo de conversão no WhatsApp, se for o caso.
4. `villa-aragua-copywriting-conversion` — revisar copy, se o gargalo for de mensagem.
5. `villa-aragua-creative-design-ads` — revisar criativo, se o gargalo for visual.

## Fluxo F — Página citável para Google/IA

1. `villa-aragua-content-strategy` — tema e prioridade.
2. `villa-aragua-ai-seo-geo` — estrutura citável (resposta direta, FAQ, subtópicos).
3. `villa-aragua-copywriting-conversion` — texto final.
4. `villa-aragua-humanizer-pt-br` — humanizar.

## Fluxo G — Plano de crescimento / growth (30/60/90 dias, canais, reativação)

1. `villa-aragua-growth-marketer` — diagnóstico, canais prioritários, experimentos.
2. `villa-aragua-pricing-revenue` — validar qualquer oferta/margem envolvida.
3. A skill de execução conforme o canal escolhido pelo plano (`villa-aragua-copywriting-conversion`, `villa-aragua-social-media-manager` ou `villa-aragua-sales-receptionist`, conforme o caso).
4. `villa-aragua-campaign-analytics` — medir o resultado do experimento/plano.

## Fluxo H — Entender comportamento do lead antes de agir

1. `villa-aragua-marketing-psychology` — diagnosticar por que o lead hesita, compara preço ou some.
2. `villa-aragua-sales-receptionist` — aplicar o diagnóstico na conversa real.
3. `villa-aragua-humanizer-pt-br` — revisar tom da aplicação prática.

## Fluxo I — Auditoria e reorganização de conteúdo já existente

1. `villa-aragua-content-strategy` (modo `/content:audit`) — classificar o que já existe (manter/atualizar/unir/reaproveitar/arquivar/apagar).
2. `villa-aragua-ai-seo-geo` — reestruturar o que for classificado como "atualizar" e precisar de melhoria de citabilidade.
3. `villa-aragua-copywriting-conversion` — reescrever o texto onde necessário.
4. `villa-aragua-humanizer-pt-br` — humanizar o resultado final.

## Como adaptar um fluxo pronto a um caso real

- Pular etapas que não se aplicam (ex.: se não há oferta/preço envolvido, pular `villa-aragua-pricing-revenue` no Fluxo A).
- Nunca pular `villa-aragua-humanizer-pt-br` quando o resultado final for um texto voltado ao hóspede/lead — é sempre a última passada de qualquer fluxo que produz texto público.
- Se o pedido for mais simples que o fluxo completo (ex.: só "escreve a legenda", sem precisar de calendário), usar apenas a fatia relevante do fluxo (`villa-aragua-copywriting-conversion` + `villa-aragua-humanizer-pt-br`), não o fluxo inteiro.

## Como usar este arquivo na prática

1. Identificar se o pedido encaixa em um dos nove fluxos.
2. Anunciar o fluxo escolhido de forma breve ("Fluxo recomendado: 1) ..., 2) ..., 3) ...").
3. Executar as etapas em ordem, pulando as que não se aplicam ao caso real.
4. Se o pedido não encaixar em nenhum fluxo pronto, montar a sequência com base na `matriz-intencoes-skills.md` e nas `regras-de-prioridade.md`.
