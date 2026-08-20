# Matriz de intenções e skills

Tabela de referência primária do router: para cada intenção reconhecível no pedido do usuário, qual é a skill principal e quais são as skills de apoio (e em que condição o apoio entra).

## Tabela completa

| Intenção | Skill principal | Skills de apoio (condição) |
|---|---|---|
| Responder lead no WhatsApp | `villa-aragua-sales-receptionist` | `villa-aragua-pricing-revenue` se envolver preço/desconto; `villa-aragua-humanizer-pt-br` para polimento final |
| Criar resposta comercial com valor, desconto ou objeção | `villa-aragua-sales-receptionist` | `villa-aragua-pricing-revenue` + `villa-aragua-humanizer-pt-br` |
| Definir preço, pacote, diária, desconto ou ponto de equilíbrio | `villa-aragua-pricing-revenue` | `villa-aragua-sales-receptionist` para comunicar ao hóspede |
| Analisar campanha Meta Ads | `villa-aragua-campaign-analytics` | `villa-aragua-pricing-revenue` para retorno/margem; `villa-aragua-creative-design-ads` para avaliar criativos; `villa-aragua-copywriting-conversion` para revisar copy; `villa-aragua-sales-receptionist` se o gargalo estiver no WhatsApp |
| Criar anúncio Meta Ads | `villa-aragua-copywriting-conversion` | `villa-aragua-creative-design-ads` + `villa-aragua-pricing-revenue` (se houver oferta) + `villa-aragua-humanizer-pt-br` |
| Avaliar ou criar criativo visual | `villa-aragua-creative-design-ads` | `villa-aragua-copywriting-conversion` + `villa-aragua-humanizer-pt-br` |
| Criar calendário Instagram | `villa-aragua-social-media-manager` | `villa-aragua-copywriting-conversion` + `villa-aragua-creative-design-ads` + `villa-aragua-humanizer-pt-br` |
| Criar post, legenda, story ou carrossel | `villa-aragua-social-media-manager` | `villa-aragua-copywriting-conversion` + `villa-aragua-humanizer-pt-br` |
| Planejar conteúdo de site, blog ou guia digital | `villa-aragua-content-strategy` | `villa-aragua-ai-seo-geo` + `villa-aragua-copywriting-conversion` + `villa-aragua-humanizer-pt-br` |
| Criar página citável para Google/IA | `villa-aragua-ai-seo-geo` | `villa-aragua-content-strategy` (tema/prioridade) + `villa-aragua-copywriting-conversion` + `villa-aragua-humanizer-pt-br` |
| Melhorar texto com cara de IA | `villa-aragua-humanizer-pt-br` | a skill de origem do texto, se houver (ex.: `villa-aragua-copywriting-conversion` se for anúncio) |
| Criar copy de site, landing page, CTA ou anúncio | `villa-aragua-copywriting-conversion` | `villa-aragua-humanizer-pt-br` + `villa-aragua-pricing-revenue` se houver preço/oferta |
| Medir resultado, ROAS, CPA, CPL ou funil | `villa-aragua-campaign-analytics` | `villa-aragua-pricing-revenue` se envolver margem/receita |
| Decidir o que criar de conteúdo | `villa-aragua-content-strategy` | `villa-aragua-ai-seo-geo` se o destino for site/blog/guia |
| Responder avaliação do Google | `villa-aragua-humanizer-pt-br` | `villa-aragua-social-media-manager` se for parte de gestão de comunidade mais ampla |
| Criar fluxo de campanha completa | depende do ponto de entrada (ver abaixo) | o router monta a sequência |
| Entender por que o lead hesita/compara preço/some | `villa-aragua-marketing-psychology` | `villa-aragua-sales-receptionist` para aplicar na conversa real |
| Priorizar canal de aquisição, plano 30/60/90, reativar hóspede antigo, parceria local | `villa-aragua-growth-marketer` | `villa-aragua-campaign-analytics` (medir) + `villa-aragua-pricing-revenue` (validar oferta) + a skill de execução conforme o canal escolhido |
| Auditar conteúdo existente / decidir manter, atualizar, unir, arquivar, apagar | `villa-aragua-content-strategy` (modo `/content:audit`) | `villa-aragua-ai-seo-geo` se envolver estrutura de busca |

## Fluxo de campanha completa — ponto de entrada define a ordem

Quando o pedido for amplo ("monta uma campanha completa"), a skill principal depende de qual ponta o usuário está puxando:

- Se o ponto de entrada é **estratégia/oferta** → principal: `villa-aragua-pricing-revenue`.
- Se o ponto de entrada é **copy** → principal: `villa-aragua-copywriting-conversion`.
- Se o ponto de entrada é **criativo** → principal: `villa-aragua-creative-design-ads`.
- Se o ponto de entrada é **análise** → principal: `villa-aragua-campaign-analytics`.
- Se o ponto de entrada é **atendimento** → principal: `villa-aragua-sales-receptionist`.

Em qualquer caso, o router monta a sequência completa a partir desse ponto de entrada — ver `fluxos-de-trabalho.md`, Fluxo A, para a ordem padrão de uma campanha Meta Ads do zero.

## Como uma intenção pode envolver mais de uma linha da tabela

Pedidos compostos (ex.: "cria o anúncio da Casa Arágua e já monta um post de Instagram com a mesma ideia") acionam duas linhas da matriz em sequência, não simultaneamente — primeiro resolve a linha de "criar anúncio Meta Ads", depois usa o resultado como insumo para "criar post, legenda, story ou carrossel" (via `villa-aragua-content-strategy/references/reaproveitamento-conteudo.md`, quando aplicável). Nunca acionar as duas skills principais ao mesmo tempo sem uma ordem definida.

## Como usar esta matriz na prática

1. Identificar a intenção do pedido e localizar a linha correspondente (ou a combinação de linhas, se for pedido composto).
2. Confirmar a skill principal e checar, para cada apoio, se a condição listada realmente se aplica ao pedido (não incluir apoio "por via das dúvidas").
3. Cruzar com `regras-de-prioridade.md` para o limite de quantas skills usar.
4. Se a intenção não se encaixar em nenhuma linha, tratar como pedido novo — descrever a intenção, escolher a skill mais próxima por função, e sinalizar se parece faltar uma skill no ecossistema.
