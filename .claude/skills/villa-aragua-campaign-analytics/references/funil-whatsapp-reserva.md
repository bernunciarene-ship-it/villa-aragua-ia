# Funil WhatsApp → Reserva

Estrutura para analisar o que acontece entre o clique no anúncio (ou o contato orgânico) e a reserva confirmada. É aqui que se descobre se uma campanha "boa no Meta Ads" é de fato boa para o negócio.

## As etapas do funil (nunca contar juntas)

1. **Leads recebidos** — todo contato que chegou no WhatsApp, de qualquer origem.
2. **Leads respondidos** — quantos desses contatos tiveram resposta da Recepcionista IA/equipe (idealmente todos, ver tempo médio de resposta abaixo).
3. **Leads qualificados** — quantos forneceram os dados mínimos de diagnóstico (período, número de pessoas, perfil — ver `villa-aragua-sales-receptionist/references/diagnostico-lead.md`).
4. **Orçamentos enviados** — quantos leads qualificados receberam valor/condição.
5. **Follow-ups feitos** — quantos leads que não fecharam de imediato entraram na cadência de follow-up (24h/72h/7 dias, ver `villa-aragua-sales-receptionist/references/follow-up.md`).
6. **Reservas confirmadas** — pagamento/condição de entrada validada, reserva de fato fechada.
7. **Reservas perdidas** — leads qualificados que não fecharam, com motivo registrado (ver seção abaixo).

**Regra central**: cada etapa é um número diferente. Nunca reportar "50 leads" como "50 reservas em potencial", nem "20 conversas" como "20 vendas". Um relatório correto sempre lista as sete etapas separadamente, mesmo quando o número cai muito de uma etapa para outra — a queda é justamente o dado mais importante (ver gargalos abaixo).

## Diferenciando os estágios de negociação

- **Lead sem resposta**: contato recebido, sem retorno da Villa Arágua ainda ou sem retorno do lead após primeira mensagem.
- **Orçamento enviado**: valor e condição foram passados, sem confirmação do lead ainda.
- **Pré-reserva**: lead sinalizou intenção clara ("quero reservar", "pode seguir") mas o pagamento/condição de entrada ainda não foi validado.
- **Reserva confirmada**: pagamento ou condição de entrada validada — só neste ponto conta como reserva de verdade.

Nunca tratar pré-reserva como reserva confirmada em nenhum relatório ou cálculo de CPA/ROAS.

## Taxa de conversão por etapa

Calcular sempre etapa a etapa, não do início direto ao fim:

- Taxa de resposta = leads respondidos ÷ leads recebidos.
- Taxa de qualificação = leads qualificados ÷ leads respondidos.
- Taxa de orçamento = orçamentos enviados ÷ leads qualificados.
- Taxa de fechamento = reservas confirmadas ÷ orçamentos enviados.
- Taxa de conversão geral = reservas confirmadas ÷ leads recebidos (útil para CPA, mas esconde onde está o gargalo — sempre olhar também as taxas por etapa).

## Tempo médio de resposta

Métrica crítica e muitas vezes subestimada: quanto mais rápido a Recepcionista IA/equipe responde, maior a chance de avanço no funil (cadência oficial recomenda resposta em até 5 minutos para lead novo, fonte: `CLAUDE.md`/`villa-aragua-sales-receptionist`). Se o tempo médio de resposta estiver alto, isso é um gargalo de atendimento, não de campanha — a solução não é trocar criativo, é revisar o fluxo com `villa-aragua-sales-receptionist`.

## Motivos de perda (registrar sempre que possível)

Categorias úteis para consolidar reservas perdidas:

- Preço/orçamento acima do esperado pelo lead.
- Disponibilidade não coincidiu com a data desejada.
- Lead escolheu concorrente/OTA.
- Lead sumiu sem responder ao follow-up.
- Lead não era o perfil certo (ex.: pediu evento/festa, grupo maior que a capacidade).
- Lead ainda "vai pensar" — em aberto, não necessariamente perdido.

Sem essa categorização (mesmo que qualitativa, vinda de observação da equipe), não é possível saber se o problema é preço, produto, atendimento ou campanha — apenas dizer "não fechou" não é análise, é constatação.

## Objeções mais frequentes

Cruzar com o banco já validado em `villa-aragua-sales-receptionist/references/objecoes-vendas.md` ("achei caro", "vi mais barato", "vou pensar", "tem desconto", "posso parcelar" etc.). Se uma objeção específica aparecer com frequência incomum num período, isso é sinal de que a campanha está atraindo um perfil de lead diferente do esperado, ou que a copy/criativo está gerando expectativa que a proposta de valor não sustenta sozinha — ver `analise-criativos-publicos.md`.

## Identificando gargalos no funil

| Onde a queda é maior | Hipótese mais provável | Onde investigar/agir |
|---|---|---|
| Leads recebidos → respondidos | Atendimento lento ou fora de horário | `villa-aragua-sales-receptionist` — tempo de resposta e rotina de plantão |
| Respondidos → qualificados | Lead não engaja com as perguntas de diagnóstico, ou é curioso/fora do perfil | Público do anúncio (`analise-criativos-publicos.md`) e abordagem inicial (`villa-aragua-sales-receptionist`) |
| Qualificados → orçamento enviado | Demora em calcular/enviar valor, ou falta de disponibilidade real | Processo interno de orçamento, não a campanha |
| Orçamento enviado → reserva | Objeção de preço, concorrência com OTA, falta de follow-up | `villa-aragua-pricing-revenue` (margem/oferta) e `follow-up.md` (cadência) |
| Reserva perdida por "sumiu" | Follow-up fraco ou tardio | `villa-aragua-sales-receptionist/references/follow-up.md` |

## Como usar este arquivo na prática

1. Pedir ou reunir os números de cada etapa (ver `checklist-dados-campanha.md`) — nunca estimar uma etapa que não foi informada.
2. Calcular as taxas de conversão etapa a etapa, identificando onde a queda é mais acentuada.
3. Classificar reservas perdidas por motivo, mesmo que de forma simples/qualitativa.
4. Cruzar o gargalo identificado com a skill certa para agir (ver tabela acima) antes de mexer na campanha de Meta Ads em si — nem todo problema de conversão é problema de anúncio.
