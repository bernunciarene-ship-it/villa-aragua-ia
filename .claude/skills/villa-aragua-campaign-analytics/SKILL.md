# Villa Arágua — Campaign Analytics

Esta skill ensina a **analisar performance de campanhas comerciais da Villa Arágua** — Meta Ads, funil WhatsApp, reservas e retorno financeiro — e transformar essa análise em decisão prática: manter, pausar, ajustar, escalar ou refazer campanha, criativo, público, copy ou oferta. É uma skill de análise e decisão, não de execução: para criar/reescrever peças, ver as skills de integração na seção abaixo.

**Regra mais importante da skill, acima de qualquer outra**: esta skill **nunca inventa métrica, receita, reserva, ROAS, CPA, CPL ou ROI**. Toda análise trabalha só com o que foi informado ou está documentado; quando faltar dado, a resposta correta é pedir o dado ou sinalizar a lacuna — nunca estimar um número e apresentá-lo como se fosse real. Ver `checklist-dados-campanha.md` para o que pedir antes de analisar qualquer coisa.

## Fontes da verdade (não alterar, só consultar)

- `AGENTE_IA_MARKETING_VENDAS_META_ADS_VILLA_ARAGUA.md` — estrutura de campanha (TOF/MOF/BOF), funil anúncio→WhatsApp→reserva, métricas que o agente de marketing já se compromete a acompanhar (seção 15), rotina diária/semanal/mensal (seção 16) e lista de pendências comerciais (seção 18) — a base mais completa para esta skill.
- `SETUP_INICIAL_META_ADS_7_SETEMBRO_VILLA_ARAGUA_2026.md` — estrutura real já validada: 3 campanhas (Pousada, Casa Arágua, Remarketing), orçamento total **R$ 45,00/dia** (Pousada R$ 25, Casa R$ 15, Remarketing R$ 5), critério de avaliação ("anúncio com lead mais qualificado, não necessariamente o de menor custo por mensagem").
- `COPYS_FINAIS_META_ADS_7_SETEMBRO_VILLA_ARAGUA_2026.md` e `COPYS_7_ANUNCIOS_INICIAIS_7_SETEMBRO_2026.md` — banco de copy já aprovada, referência para análise de criativos/copies.
- `CHECKLIST_DECISOES_CAMPANHA_REABERTURA_VILLA_ARAGUA_2026.md` — decisões já tomadas por Renildo (data de reabertura 01/08/2026, orçamento, oferta de reabertura) que servem de baseline para qualquer análise futura da campanha de reabertura.
- `DADOS_OFICIAIS_ATENDIMENTO_VILLA_ARAGUA.md` — diária média (Pousada R$ 500,00 / Casa R$ 990,00, mínimo 4 diárias), taxa de limpeza da Casa (R$ 450,00), parcelamento (+7%) — dados necessários para qualquer cálculo de receita/ROI. (Café da manhã não é mais receita da Casa — ela não oferece café em nenhuma condição, regra atualizada 2026-08-07.)
- `MARKETING E VENDAS/CAMPANHAS META ADS/HISTORICO CAMPANHAS META ADS/HISTORICO CAMPANHAS META ADS.xlsx` e a pasta `METRICAS/` (prints de campanhas antigas) — fonte primária de métricas históricas, **ainda não consolidada/lida por nenhum agente do projeto** (pendência confirmada em `AGENTE_IA_MARKETING_VENDAS_META_ADS_VILLA_ARAGUA.md`, seção 18).
- `MARKETING E VENDAS/CAMPANHAS META ADS/HISTORICO DE RESERVAS diretas e OTAs/PLANILHA PRE RESERVAS E BOOKING.xlsx` — planilha de reservas diretas x OTA, também ainda não consolidada.
- `MARKETING E VENDAS/CAMPANHAS META ADS/PUBLICOS META ADS/` (salvos, semelhantes, personalizados) e `CRIATIVOS CAMPANHAS META ADS/` — estrutura real de públicos e criativos já usada pela operação.
- `FINANCEIRO/` — ledgers simples de custo e receita da pousada, **sem categorização por caixa** (não é possível hoje separar automaticamente "custo de Meta Ads do mês" sem classificar manualmente cada lançamento — ver `villa-aragua-pricing-revenue/references/ponto-equilibrio-abertura.md`).
- `ESTATISTICAS E RESERVAS/` (ticket médio 2024–2026, estatística de reserva/ocupação) — histórico de ocupação e ticket médio, quando precisar contextualizar uma campanha dentro da sazonalidade.
- `CONCORRENTES/VILLA ARAGUA IA CONCORRENTES.docx` — hoje apenas lista de links do Booking, sem análise de preço/posicionamento (ver `villa-aragua-pricing-revenue/references/concorrentes-otas.md`) — nunca comparar CPA/ROAS com concorrente nomeado.
- As referências das outras seis skills do projeto (ver seção de integração abaixo).

## Como usar esta skill

1. **Antes de qualquer análise** → `checklist-dados-campanha.md` — confirmar que os dados mínimos existem; sem eles, a análise vira hipótese, não conclusão.
2. **Para ler métricas brutas do Meta Ads** → `metricas-meta-ads.md`.
3. **Para entender o que aconteceu depois do clique** → `funil-whatsapp-reserva.md`.
4. **Para calcular retorno financeiro** → `roas-cpa-cpl-roi.md`.
5. **Para saber de onde a reserva realmente veio** → `atribuicao-canais.md`.
6. **Para comparar criativos, copies e públicos** → `analise-criativos-publicos.md`.
7. **Para consolidar tudo em relatório** → `relatorio-semanal-mensal.md`.
8. **Para transformar a análise em ação** → `decisoes-otimizacao.md`.

## Princípio central — lead barato não é o objetivo, lead que avança é

A métrica mais importante não é o menor custo por lead ou por conversa — é o lead que avança no funil (responde, qualifica, pede orçamento, reserva). Uma campanha pode ter CPL baixo e ser ruim (leads curiosos, fora do perfil, que nunca respondem no WhatsApp) e outra pode ter CPL mais alto e ser ótima (leads que viram reserva). Toda análise desta skill prioriza qualidade de avanço no funil sobre custo isolado por lead.

## Separação obrigatória: dado real, estimativa e hipótese

Toda vez que esta skill apresentar um número, ele precisa vir etiquetado como um dos três:

- **Dado real**: valor que está de fato em um arquivo/planilha/print informado pelo usuário (ex.: "investimento de R$ 315,00 na semana, conforme print enviado").
- **Estimativa**: cálculo feito a partir de dados reais, mas com alguma simplificação assumida (ex.: "custo por conversa estimado dividindo investimento pelo número de conversas informado, sem contar conversas que chegaram por outro canal").
- **Hipótese**: leitura ou recomendação sem dado numérico suficiente por trás (ex.: "hipótese: o público frio pode estar gerando curiosos, mas isso precisa ser confirmado com a taxa de resposta real").

Nunca apresentar estimativa ou hipótese como se fosse dado real.

## Distinções obrigatórias (nunca simplificar)

- **Lead ≠ reserva** — lead é contato inicial; reserva é confirmação com pagamento validado.
- **Conversa ≠ venda** — conversa é engajamento no WhatsApp; venda é reserva confirmada.
- **Faturamento bruto ≠ lucro** — faturamento é receita total; lucro depende de custos (Meta Ads, operação, limpeza, café, comissão de OTA quando aplicável).
- **Reserva confirmada ≠ pré-reserva ≠ orçamento enviado ≠ lead sem resposta** — quatro estágios diferentes do funil, nunca contados juntos como "reserva" (ver `funil-whatsapp-reserva.md`).
- **Receita reservada ≠ receita recebida ≠ lucro estimado** — reservado é o valor combinado; recebido é o que já entrou no caixa; lucro estimado é receita recebida menos custos atribuíveis (ver `roas-cpa-cpl-roi.md`).
- **Pousada Arágua ≠ Casa Arágua** — nunca somar métricas ou resultados dos dois produtos como se fossem uma campanha só; cada produto tem sua própria campanha, seu próprio custo de operação e sua própria análise (ver `SETUP_INICIAL_META_ADS_7_SETEMBRO_VILLA_ARAGUA_2026.md`, onde já são campanhas separadas).

## O que esta skill nunca faz

- Nunca inventa métrica, receita, número de reservas, ROAS, CPA, CPL ou ROI que não tenha sido informado ou documentado.
- Nunca trata lead como reserva, nem conversa como venda, nem faturamento bruto como lucro.
- Nunca mistura campanha da Pousada com campanha da Casa Arágua na mesma análise, salvo quando o objetivo explícito é comparar as duas lado a lado (e mesmo assim, com números separados por produto).
- Nunca recomenda escalar orçamento sem evidência mínima (mais de um período de dados, taxa de avanço no funil consistente) — ver critério em `decisoes-otimizacao.md`.
- Nunca recomenda pausar uma campanha só por ansiedade de curto prazo (ex.: 1-2 dias sem lead) — campanhas novas precisam de tempo mínimo de aprendizado do algoritmo antes de qualquer decisão.
- Nunca decide sozinha preço, desconto, oferta ou orçamento final — sempre recomenda, e a decisão de aplicar é de Renildo/equipe (mesma régua de `AGENTE_IA_MARKETING_VENDAS_META_ADS_VILLA_ARAGUA.md`).
- Nunca compara CPA/CPL/ROAS com concorrente nomeado — não existe esse dado validado (ver `atribuicao-canais.md` e `analise-criativos-publicos.md`).

## Integração com as outras skills do projeto

Esta é a sétima skill do ecossistema Villa Arágua. Ela **analisa e recomenda**; a execução da recomendação acontece nas outras skills:

- **`villa-aragua-pricing-revenue`** avalia margem, preço e retorno real de qualquer oferta que a análise aponte como candidata a ajuste — nenhuma recomendação de preço/desconto sai desta skill sem passar por ali.
- **`villa-aragua-sales-receptionist`** é acionada quando a análise do funil aponta gargalo no atendimento (tempo de resposta alto, baixa taxa de qualificação, objeção recorrente sem resposta boa) — ela ajusta como a conversa é conduzida.
- **`villa-aragua-copywriting-conversion`** reescreve anúncios, páginas e CTAs quando a análise de criativos/copies aponta uma copy fraca ou desalinhada com o público.
- **`villa-aragua-creative-design-ads`** revisa direção visual e formato quando a análise aponta um criativo (imagem/vídeo) com desempenho abaixo do esperado.
- **`villa-aragua-humanizer-pt-br`** melhora a forma de qualquer mensagem (anúncio, follow-up, resposta) apontada como fria, robotizada ou fora do tom da marca.
- **`villa-aragua-social-media-manager`** ajuda a diferenciar o que é resultado de tráfego pago (Meta Ads) do que é resultado de conteúdo orgânico (Instagram), evitando atribuir a uma campanha paga um lead que na verdade veio do perfil.

Fluxo prático sugerido para uma rodada de análise: `checklist-dados-campanha.md` (o que falta) → `metricas-meta-ads.md` + `funil-whatsapp-reserva.md` (o que aconteceu) → `roas-cpa-cpl-roi.md` + `atribuicao-canais.md` (o retorno, com os limites de atribuição) → `analise-criativos-publicos.md` (o que funcionou e o que não funcionou) → `relatorio-semanal-mensal.md` (consolidar) → `decisoes-otimizacao.md` (transformar em decisão) → acionar a skill de execução correspondente (pricing, receptionist, copywriting, creative ou humanizer).

## Pendências conhecidas (sinalizar, não inventar)

- Métricas históricas de Meta Ads existem em arquivo bruto (`HISTORICO CAMPANHAS META ADS.xlsx`, prints em `METRICAS/`), mas **ainda não foram lidas/consolidadas** por nenhum agente do projeto — qualquer análise histórica depende de abrir esses arquivos primeiro.
- Planilha de reservas diretas x OTA (`PLANILHA PRE RESERVAS E BOOKING.xlsx`) existe, mas **ainda não foi consolidada**.
- `FINANCEIRO/` são ledgers simples sem categorização por caixa — não dá para extrair automaticamente "custo de Meta Ads do mês" ou "lucro da operação" sem classificar manualmente cada lançamento primeiro.
- Não existe percentual real de dependência de OTA vs. reserva direta na receita da Villa Arágua.
- Não existe comissão exata negociada com Booking/Airbnb/Decolar documentada — não inventar percentual.
- Não existe análise de preço/posicionamento dos concorrentes monitorados (`CONCORRENTES/`).
- Não existe, até o momento, relatório consolidado de nenhuma campanha rodando (a operação está em fase de reabertura, com o primeiro setup real ainda em `SETUP_INICIAL_META_ADS_7_SETEMBRO_VILLA_ARAGUA_2026.md`) — os exemplos desta skill usam a estrutura validada (3 campanhas, R$ 45,00/dia) como referência, nunca como resultado já obtido.
