# Funil Growth WhatsApp

Visão completa do funil de crescimento, do primeiro alcance ao retorno do hóspede — mais amplo que o funil comercial já detalhado em `villa-aragua-campaign-analytics/references/funil-whatsapp-reserva.md`, que esta skill usa como motor de cálculo. Aqui o objetivo é enxergar o funil inteiro de uma vez, para identificar em qual elo o esforço de growth deve se concentrar agora.

## As onze etapas

1. **Alcance** — quantas pessoas foram expostas à marca (Meta Ads, Instagram, Google, indicação).
2. **Clique** — quantas dessas pessoas tomaram uma ação (clicar no anúncio, no link da bio, no botão do WhatsApp).
3. **Conversa** — quantas de fato abriram uma conversa no WhatsApp.
4. **Lead qualificado** — quantas forneceram os dados mínimos de diagnóstico (período, pessoas, perfil).
5. **Orçamento** — quantas receberam valor/condição.
6. **Follow-up** — quantas entraram na cadência de reengajamento após não fechar de imediato.
7. **Reserva** — quantas confirmaram (pagamento/condição validada).
8. **Pagamento** — o fechamento financeiro da reserva (entrada, saldo).
9. **Pós-estadia** — o que acontece depois que o hóspede já viveu a experiência.
10. **Avaliação** — se o hóspede deixou prova social (Google, Booking, TripAdvisor).
11. **Retorno do hóspede** — se essa pessoa volta a reservar (direto, idealmente) numa próxima ocasião.

**Nota importante**: as etapas 1-8 já têm cálculo e critério detalhado em `villa-aragua-campaign-analytics/references/funil-whatsapp-reserva.md` e `metricas-meta-ads.md` — esta skill nunca recalcula essas fórmulas, apenas usa o resultado para decidir prioridade. As etapas 9-11 são o território específico desta skill de growth, porque tratam de retenção/relacionamento, não de aquisição.

## Por que o funil não termina na reserva

Um erro comum de olhar só até a etapa 7 (reserva): isso ignora que o hóspede satisfeito e bem tratado no pós-estadia é o insumo mais barato de crescimento futuro (avaliação, indicação, retorno). Growth sustentável de uma pousada pequena depende tanto de "trazer gente nova" quanto de "fazer quem já veio voltar e trazer mais gente".

## Onde identificar gargalo, e o que fazer

| Etapa com maior queda | Hipótese provável | Ação de growth |
|---|---|---|
| Alcance → clique | Criativo/copy fraco, público errado | Acionar `villa-aragua-creative-design-ads` e `villa-aragua-copywriting-conversion`; revisar `canais-aquisicao-villa.md` |
| Clique → conversa | Desalinhamento entre anúncio e expectativa ao clicar | Revisar promessa do anúncio vs. primeira mensagem (`villa-aragua-sales-receptionist`) |
| Conversa → qualificado | Abordagem inicial fraca ou lead fora do perfil | Revisar `villa-aragua-sales-receptionist` e segmentação de público |
| Qualificado → orçamento | Demora no processo interno | Ajuste operacional, não de growth/campanha |
| Orçamento → reserva | Objeção de preço, concorrência OTA, follow-up fraco | Acionar `villa-aragua-pricing-revenue` (margem/oferta) e `villa-aragua-sales-receptionist` (follow-up) |
| Reserva → pós-estadia com boa experiência | Falha operacional durante a estadia | Fora do escopo desta skill — questão operacional direta |
| Pós-estadia → avaliação | Pedido de avaliação fraco ou ausente | Revisar cadência de follow-up pós-estadia (`villa-aragua-sales-receptionist/references/follow-up.md`) |
| Avaliação/estadia → retorno | Falta de reconexão no tempo certo | Ver `reativacao-hospedes-antigos.md` |

## Como este funil orienta a prioridade de growth

- Se o gargalo está nas etapas 1-3 (alcance/clique/conversa): prioridade em canal de aquisição e criativo/copy (`canais-aquisicao-villa.md`, `experimentos-crescimento.md`).
- Se o gargalo está nas etapas 4-7 (qualificação até reserva): prioridade em atendimento e oferta (`villa-aragua-sales-receptionist`, `villa-aragua-pricing-revenue`) — mais campanha nova não resolve gargalo de conversão.
- Se o gargalo está nas etapas 9-11 (pós-estadia até retorno): prioridade em reativação e relacionamento (`reativacao-hospedes-antigos.md`), não em mais aquisição — é mais barato reconquistar quem já veio do que atrair gente nova.

## Conexão obrigatória com `villa-aragua-campaign-analytics`

Toda vez que esta skill precisar de um número (CPL, custo por conversa, taxa de conversão, ROAS), a fonte de cálculo é sempre `villa-aragua-campaign-analytics` — esta skill decide o que priorizar a partir do resultado, nunca calcula a métrica por conta própria. Isso evita duas skills com lógicas de cálculo divergentes.

## Como usar este arquivo na prática

1. Pedir ou revisar o relatório de funil mais recente (via `villa-aragua-campaign-analytics/references/relatorio-semanal-mensal.md`).
2. Identificar visualmente em qual das onze etapas está a maior queda proporcional.
3. Cruzar com a tabela acima para decidir a ação de growth prioritária do ciclo.
4. Sempre verificar se o gargalo é de aquisição (etapas 1-3), conversão (4-7) ou retenção (9-11) antes de recomendar qualquer canal/experimento novo.
