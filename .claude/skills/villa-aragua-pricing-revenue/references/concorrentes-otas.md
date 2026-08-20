# OTAs e concorrentes

## Radar de Concorrência Revenue (módulo ativo desde 2026-07-25, status `EM_IMPLANTACAO_MANUAL_ASSISTIDA`)

Existe agora uma metodologia estruturada para esta análise, nos seguintes arquivos na raiz do projeto:

- `CESTA_COMPETITIVA_REVENUE_VILLA_ARAGUA.md` — cadastro de concorrentes e links (7 nomes trazidos de `CONCORRENTES/VILLA ARAGUA IA CONCORRENTES.docx`, ainda sem dados complementares preenchidos).
- `COLETAS_CONCORRENCIA_REVENUE.csv` — log de coleta manual/assistida (ainda vazio, só cabeçalho).
- `REGRAS_CONVERSAO_OTA_MOTOR_REVENUE.md` — fórmulas obrigatórias para nunca confundir preço visível de OTA com preço de motor.
- `ALERTAS_CONCORRENCIA_REVENUE.md` — modelo de saída e a rotina inicial de coleta (16 datas prioritárias, todas `PENDENTE_COLETA`).

**Isto não substitui a limitação abaixo — só dá a ela um formato.** Enquanto a cesta e as coletas não forem preenchidas por Renildo, a limitação de dados continua valendo integralmente: nenhuma comparação numérica real existe ainda, só a estrutura pronta para recebê-la. Nenhuma automação de scraping foi criada — toda coleta é manual.

## Objetivo estratégico

Reduzir dependência de OTAs (Booking/Airbnb) e aumentar reserva direta via WhatsApp — objetivo explícito registrado em `AGENTE_IA_MARKETING_VENDAS_META_ADS_VILLA_ARAGUA.md`: "menor dependência de OTAs (Booking/Airbnb)".

## Limitação atual dos dados — não inventar o que ainda não existe

- `CONCORRENTES/VILLA ARAGUA IA CONCORRENTES.docx` hoje é **apenas uma lista de links do Booking**, sem análise de preço ou posicionamento (confirmado literalmente em `AGENTE_IA_MARKETING_VENDAS_META_ADS_VILLA_ARAGUA.md`: "hoje apenas links, sem análise de preço/posicionamento").
- `MARKETING E VENDAS/CAMPANHAS META ADS/HISTORICO DE RESERVAS diretas e OTAs/PLANILHA PRE RESERVAS E BOOKING.xlsx` existe, mas **ainda não foi consolidada/analisada**.
- Isso significa: **nunca afirmar "a Villa Arágua é mais barata/cara que o concorrente X" com número específico** — não existe essa comparação validada hoje. Qualquer leitura de preço de concorrente exige checar manualmente no Booking/Airbnb, na data, e tratar como referência pontual, não como dado permanente.

## Concorrentes monitorados (fonte: `CONCORRENTES/VILLA ARAGUA IA CONCORRENTES.docx` e `CLAUDE.md`)

Pousadas/casas em Bombinhas, principalmente Mariscal e Canto Grande:

- Kia Ora
- Up Hotel Boutique
- Vila Boa Vida
- Dom Capudi
- Kaloa Eco Village
- Morada do Guarucá
- Villa dos Açores

## Como comparar com concorrentes (quando houver checagem pontual)

Ao avaliar um concorrente para calibrar posicionamento, observar:

- Capacidade (número de pessoas/quartos).
- Distância da praia.
- Piscina (comum ou privativa).
- Café da manhã (incluso ou não).
- Privacidade (pousada compartilhada vs casa exclusiva).
- Nota/avaliações no Booking.
- Preço da diária no mesmo período e mesma janela de antecedência (comparar "maçã com maçã" — datas e número de pessoas equivalentes).

**Usar o preço do concorrente como referência de calibragem, nunca como ordem a seguir.** O objetivo do Revenue Manager é "aumentar receita sem perder posicionamento" (fonte: `CLAUDE.md`) — isso pode significar manter um preço mais alto que um concorrente específico, se a Villa Arágua entrega mais estrutura (café, piscina, área comum, atendimento).

## Comparando Booking/Airbnb x reserva direta

- **Taxas de plataforma**: Booking e Airbnb cobram comissão do anfitrião — isso é conhecimento geral do setor, mas a Villa Arágua não tem, nos arquivos oficiais, o percentual exato negociado com cada plataforma; não inventar um número específico de comissão.
- **Argumento de venda para reserva direta** (já validado, fonte: `objecoes-vendas.md` da skill `villa-aragua-sales-receptionist`): "Reservando direto com a gente, o atendimento é próximo do início ao fim da estadia, e qualquer dúvida durante a estadia é resolvida direto pelo nosso WhatsApp oficial."
- **Evitar guerra de preço**: não é estratégia da Villa Arágua tentar vencer o Booking/Airbnb baixando preço até igualar ou ficar abaixo — a estratégia é defender reserva direta pelo valor agregado (atendimento, relação, previsibilidade), não pela menor tarifa.
- Se o hóspede disser "vi mais barato no Booking/Airbnb", a resposta reforça valor, nunca inventa comparação de número (ver `regras-desconto.md` e `comunicacao-preco-whatsapp.md`).

## O que fica pendente (sinalizar, não inventar)

- Análise textual/comparativa de preço dos 7 concorrentes monitorados — ainda não existe.
- Consolidação da planilha de reservas diretas x OTAs — ainda não existe.
- Percentual real de dependência de OTA vs reserva direta na receita da Villa Arágua — não confirmado nos arquivos atuais.

Quando o usuário pedir uma "análise de concorrência" completa, a resposta correta é apoiar a estruturação dessa análise (que dados coletar, como organizar), não fabricar números que não existem na base oficial.
