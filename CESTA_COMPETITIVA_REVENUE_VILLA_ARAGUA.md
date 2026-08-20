# CESTA COMPETITIVA — RADAR DE CONCORRÊNCIA REVENUE — VILLA ARÁGUA

**Status do módulo:** `EM_IMPLANTACAO_MANUAL_ASSISTIDA`
**Função:** registrar quem são os concorrentes acompanhados e o link direto de cada um, separado por produto Villa comparável. É o cadastro-base do Radar de Concorrência — sem isso, não há o que coletar em `COLETAS_CONCORRENCIA_REVENUE.csv`.
**Coleta:** manual/assistida. Nenhum link, preço ou dado de concorrente é coletado automaticamente.

---

## Perfil de busca obrigatório (`REGRA_APROVADA_RENILDO`, 2026-07-25)

| Produto | Perfil de busca | Unidade Villa de referência |
|---|---|---|
| Pousada Arágua | 2 adultos, casal, 1 acomodação | Sempre a categoria **base** (Organic/Fuego/Metallo) — não buscar concorrente separado por suíte neste primeiro momento. As demais categorias (Terra/Wood, Acqua, Luna, Duplex Soleil) vêm da régua interna aprovada, não de nova coleta. |
| Casa Arágua | Casa/apartamento inteiro, preferencialmente 4 a 6 hóspedes | Casa Arágua (unidade única) |

## Como preencher

| Campo | O que colocar |
|---|---|
| nome | Nome do concorrente |
| produto comparável | `Pousada Arágua` ou `Casa Arágua` |
| unidade Villa de referência | Para Pousada: sempre "base (Organic/Fuego/Metallo)". Para Casa: sempre "Casa Arágua". |
| link direto | URL da página de reserva do concorrente (Booking, Airbnb, Decolar ou site próprio) |
| canal | `Booking` / `Airbnb` / `Decolar` / `site próprio` / `outro` |
| tipo | `pousada` / `suíte` / `apartamento` / `casa` |
| capacidade | Número de hóspedes |
| café da manhã | `sim` / `não` / `desconhecido` |
| piscina | `sim` / `não` / `desconhecido` |
| distância aproximada da praia | Em metros ou "a X min a pé" |
| peso na média | `alto` (concorrente direto, mesmo padrão/região) / `médio` (comparável parcial) / `baixo` (referência distante, usar com cautela) |
| observações de posicionamento | Qualquer diferencial relevante (ex.: "mais caro, vende exclusividade"; "mais barato, sem café") |
| status | `PENDENTE` (nome conhecido, sem link) / `LINK_CADASTRADO` (link preenchido, sem coleta ainda) / `LINK_CADASTRADO_E_COLETADO_COM_SUCESSO` (já tem coleta registrada em `COLETAS_CONCORRENCIA_REVENUE.csv`) / `PRECISA_VALIDACAO_MANUAL` (tentativa de coleta falhou) |

**Regra:** nenhum campo deve ser preenchido com valor inventado. Se não souber, usar `[PREENCHER]` ou `desconhecido` — nunca estimar um dado factual como se fosse confirmado.

---

## Concorrentes já monitorados (fonte: `CONCORRENTES/VILLA ARAGUA IA CONCORRENTES.docx`) — histórico

Estes 7 nomes vieram originalmente do projeto como lista de links do Booking, sem análise (conforme `AGENTE_IA_MARKETING_VENDAS_META_ADS_VILLA_ARAGUA.md` e a skill `villa-aragua-pricing-revenue`, referência `concorrentes-otas.md`). Em 2026-07-25, Renildo autorizou e classificou todos os 7 como comparáveis da **Pousada Arágua**, com nome oficial e link confirmado — ver tabela "Concorrentes autorizados — Pousada Arágua" abaixo. Mapa de nome antigo → nome oficial, para não perder o rastro:

| Nome nesta lista original | Nome oficial autorizado |
|---|---|
| Kia Ora | Pousada Kia Ora Bombinhas |
| Up Hotel Boutique | UP Hotel Boutique |
| Vila Boa Vida | Vila Boa Vida (sem mudança) |
| Dom Capudi | Pousada Dom Capudi |
| Kaloa Eco Village | Pousada Kaloa Eco Village |
| Morada do Guarucá | Morada do Guaruça |
| Villa dos Açores | Vila dos Açores |

Nenhuma linha desses 7 nomes permanece duplicada nesta seção — todos os dados (link, canal, status) vivem só na tabela oficial abaixo, para não haver duas fontes divergentes do mesmo concorrente.

---

## Concorrentes autorizados — Pousada Arágua (`REGRA_APROVADA_RENILDO`, 2026-07-25)

Cesta competitiva oficial da Pousada Arágua, autorizada por Renildo antes de qualquer nova coleta de preço. Perfil padrão de busca: 2 adultos, 0 crianças, 1 acomodação, casal. Canal principal: Booking, exceto Vila dos Açores (site próprio/Omnibees). `capacidade`, `café da manhã`, `piscina`, `distância da praia`, `peso na média` e `observações` abaixo só estão preenchidos onde já há dado confirmado (Vila Boa Vida, já coletada) — os demais ficam `[PREENCHER]`/`desconhecido` até nova coleta autorizada. `tipo` foi preenchido apenas quando a própria palavra já está no nome oficial do concorrente (ex.: "Pousada X" → `pousada`), nunca por suposição.

| nome | unidade Villa de referência | link direto | canal | tipo | capacidade | café da manhã | piscina | distância da praia | peso na média | observações | status |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Vila Boa Vida | base (Organic/Fuego/Metallo) | https://www.booking.com/hotel/br/vila-boa-vida.pt-br.html?checkin=2026-10-09&checkout=2026-10-12&group_adults=2&group_children=0&no_rooms=1 | Booking | pousada | não coletado (por tipo de quarto: máx. 2 pessoas em todos os tipos testados) | sim | sim | ≈650 m (a página do Booking também lista "Mariscal Beach 2 m" em outra seção — inconsistência da própria fonte, não resolvida) | médio | Nota 8,7/10 (136 avaliações), café da manhã destacado. 5 tipos de acomodação no mesmo período (casal, 3 diárias): Quarto Duplo Standard R$ 1.271 (usado como âncora), Suíte R$ 1.571, Suíte c/ hidromassagem R$ 1.946, Suíte Deluxe c/ hidromassagem R$ 2.246, Chalé R$ 2.321. Depósito caução de R$ 500 na chegada (reembolsável, não é tarifa). Rodada 1 (04–08/09/2026, feriado 7 de Setembro): R$ 1.695 total, diária R$ 423,75, motor equiv. R$ 339,00. Rodada 2 (09–12/10/2026, feriado 12 de Outubro): R$ 1.271 total, diária R$ 423,67, motor equiv. R$ 338,93. Rodada 3 (30/10–02/11/2026, feriado de Finados): R$ 1.373 total, diária R$ 457,67, motor equiv. R$ 366,13. Rodada 4 (19–22/11/2026, feriado forte de Consciência Negra): R$ 1.575 total, diária R$ 525,00, motor equiv. R$ 420,00. | LINK_CADASTRADO_E_COLETADO_COM_SUCESSO |
| Vila Maciel | base (Organic/Fuego/Metallo) | https://www.booking.com/hotel/br/villa-maciel-bombinhas.pt-br.html?checkin=2026-10-09&checkout=2026-10-12&group_adults=2&group_children=0&no_rooms=1 | Booking | [PREENCHER] | [PREENCHER] | desconhecido | desconhecido | [PREENCHER] | [PREENCHER] | Rodada 1 (04–08/09/2026): R$ 938 total (30% off, original R$ 1.340), diária R$ 234,50, motor equiv. R$ 187,60. Rodada 2 (09–12/10/2026): R$ 840 total (20% off, original R$ 1.050), diária R$ 280,00, motor equiv. R$ 224,00. Rodada 3 (30/10–02/11/2026): R$ 840 total (20% off, original R$ 1.050), diária R$ 280,00, motor equiv. R$ 224,00. Rodada 4 (19–22/11/2026): R$ 1.032 total (20% off, original R$ 1.290), diária R$ 344,00, motor equiv. R$ 275,20. Âncora: Apartamento Standard. | LINK_CADASTRADO_E_COLETADO_COM_SUCESSO |
| Morada do Guaruça | base (Organic/Fuego/Metallo) | https://www.booking.com/hotel/br/morada-do-guaruca.pt-br.html?checkin=2026-10-09&checkout=2026-10-12&group_adults=2&group_children=0&no_rooms=1 | Booking | [PREENCHER] | [PREENCHER] | desconhecido | desconhecido | [PREENCHER] | [PREENCHER] | Rodada 1 (04–08/09/2026): âncora aprovada (Apartamento de 1 Quarto) não disponível — provável esgotamento no feriado. Rodada 2 (09–12/10/2026): disponível, R$ 1.835 total, diária R$ 611,67, motor equiv. R$ 489,33. Rodada 3 (30/10–02/11/2026): disponível, R$ 1.835 total, diária R$ 611,67, motor equiv. R$ 489,33. Rodada 4 (19–22/11/2026): disponível, R$ 2.122 total, diária R$ 707,33, motor equiv. R$ 565,87. | LINK_CADASTRADO_E_COLETADO_COM_SUCESSO |
| Pousada Kaloa Eco Village | base (Organic/Fuego/Metallo) | https://www.booking.com/hotel/br/pousada-kaloa-eco-village.pt-br.html?checkin=2026-10-09&checkout=2026-10-12&group_adults=2&group_children=0&no_rooms=1 | Booking | pousada | [PREENCHER] | desconhecido | desconhecido | [PREENCHER] | [PREENCHER] | Rodada 1 (04–08/09/2026): R$ 1.949 total, diária R$ 487,25, motor equiv. R$ 389,80. Rodada 2 (09–12/10/2026): R$ 1.462 total, diária R$ 487,33, motor equiv. R$ 389,87. Rodada 3 (30/10–02/11/2026): R$ 1.510 total, diária R$ 503,33, motor equiv. R$ 402,67. Rodada 4 (19–22/11/2026): R$ 1.608 total, diária R$ 536,00, motor equiv. R$ 428,80. Âncora: Suíte Standard. | LINK_CADASTRADO_E_COLETADO_COM_SUCESSO |
| UP Hotel Boutique | base (Organic/Fuego/Metallo) | https://www.booking.com/hotel/br/up-boutique.pt-br.html?checkin=2026-10-09&checkout=2026-10-12&group_adults=2&group_children=0&no_rooms=1 | Booking | hotel | [PREENCHER] | desconhecido | desconhecido | [PREENCHER] | [PREENCHER] | Rodada 1 (04–08/09/2026): R$ 2.412 total, diária R$ 603,00, motor equiv. R$ 482,40. Rodada 2 (09–12/10/2026): R$ 1.744 total, diária R$ 581,33, motor equiv. R$ 465,07. Rodada 3 (30/10–02/11/2026): R$ 2.291 total (7% off, original R$ 2.464), diária R$ 763,67, motor equiv. R$ 610,93. Rodada 4 (19–22/11/2026): R$ 1.977 total (7% off, original R$ 2.126), diária R$ 659,00, motor equiv. R$ 527,20. Âncora: Quarto Duplo Deluxe com Banheira. | LINK_CADASTRADO_E_COLETADO_COM_SUCESSO |
| Pousada Riviera Bombinhas | base (Organic/Fuego/Metallo) | https://www.booking.com/hotel/br/pousada-riviera-bombinhas.pt-br.html?checkin=2026-10-09&checkout=2026-10-12&group_adults=2&group_children=0&no_rooms=1 | Booking | pousada | [PREENCHER] | desconhecido | desconhecido | [PREENCHER] | [PREENCHER] | Rodada 1 (04–08/09/2026): R$ 1.894 total, diária R$ 473,50, motor equiv. R$ 378,80. Rodada 2 (09–12/10/2026): R$ 1.458 total, diária R$ 486,00, motor equiv. R$ 388,80. Rodada 3 (30/10–02/11/2026): R$ 1.568 total, diária R$ 522,67, motor equiv. R$ 418,13. Rodada 4 (19–22/11/2026): R$ 2.269 total, diária R$ 756,33, motor equiv. R$ 605,07. Âncora: Suíte Loft Riviera. | LINK_CADASTRADO_E_COLETADO_COM_SUCESSO |
| Pousada Kia Ora Bombinhas | base (Organic/Fuego/Metallo) | https://www.booking.com/hotel/br/kia-ora-bombinhas.pt-br.html?checkin=2026-10-09&checkout=2026-10-12&group_adults=2&group_children=0&no_rooms=1 | Booking | pousada | [PREENCHER] | desconhecido | desconhecido | [PREENCHER] | [PREENCHER] | Rodada 1 (04–08/09/2026): R$ 2.341 total, diária R$ 585,25, motor equiv. R$ 468,20. Rodada 2 (09–12/10/2026): R$ 2.006 total, diária R$ 668,67, motor equiv. R$ 534,93. Rodada 3 (30/10–02/11/2026): sem disponibilidade — esgotado (todas as categorias). Rodada 4 (19–22/11/2026): disponível, R$ 2.195 total, diária R$ 731,67, motor equiv. R$ 585,33. Âncora: Quarto Duplo Deluxe com Vista Lateral do Mar. | LINK_CADASTRADO_E_COLETADO_COM_SUCESSO |
| Pousada dos Ingleses | base (Organic/Fuego/Metallo) | https://www.booking.com/hotel/br/pousada-dos-ingleses.pt-br.html?checkin=2026-10-09&checkout=2026-10-12&group_adults=2&group_children=0&no_rooms=1 | Booking | pousada | [PREENCHER] | desconhecido | desconhecido | [PREENCHER] | [PREENCHER] | Rodada 1 (04–08/09/2026): R$ 1.134 + R$ 120 taxas = R$ 1.254 total, diária R$ 313,50, motor equiv. R$ 250,80. Rodada 2 (09–12/10/2026): R$ 850 + R$ 120 taxas = R$ 970 total, diária R$ 323,33, motor equiv. R$ 258,67. Rodada 3 (30/10–02/11/2026): R$ 709 + R$ 120 taxas = R$ 829 total, diária R$ 276,33, motor equiv. R$ 221,07. Rodada 4 (19–22/11/2026): âncora aprovada (Quarto Duplo Clássico) não disponível — provável esgotamento no feriado forte; outras categorias mais caras seguem à venda (Chalé Master, Suíte, Quarto Duplo Básico), não usadas por não serem a âncora aprovada. Âncora: Quarto Duplo Clássico. | LINK_CADASTRADO_E_COLETADO_COM_SUCESSO |
| Pousada Dom Capudi | base (Organic/Fuego/Metallo) | https://www.booking.com/hotel/br/pousada-dom-capudi.pt-br.html?checkin=2026-10-09&checkout=2026-10-12&group_adults=2&group_children=0&no_rooms=1 | Booking | pousada | [PREENCHER] | desconhecido | desconhecido | [PREENCHER] | [PREENCHER] | Rodada 1 (04–08/09/2026): sem disponibilidade — esgotado. Rodada 2 (09–12/10/2026): disponível, R$ 1.354 total, diária R$ 451,33, motor equiv. R$ 361,07. Rodada 3 (30/10–02/11/2026): disponível, R$ 1.354 total, diária R$ 451,33, motor equiv. R$ 361,07. Rodada 4 (19–22/11/2026): âncora aprovada (Quarto Duplo) não disponível — provável esgotamento no feriado forte; outras categorias mais caras seguem à venda (Suíte Premium, Suíte com Vista do Jardim, Quarto Triplo Standard), não usadas por não serem a âncora aprovada. Âncora: Quarto Duplo. | LINK_CADASTRADO_E_COLETADO_COM_SUCESSO |
| Vila dos Açores | base (Organic/Fuego/Metallo) | https://book.omnibees.com/hotelresults?q=9886 | site próprio / Omnibees | [PREENCHER] | [PREENCHER] | desconhecido | desconhecido | [PREENCHER] | [PREENCHER] | Site direto — **não aplicar automaticamente** a conversão Booking/1,25 usada para os demais. Hipótese de referência (não validada): site direto pode aparecer ~15% a 25% abaixo do Booking; tratar só como hipótese até coleta real confirmar. Não incluído nas Rodadas 1 e 2 (pendente/não usar). | LINK_CADASTRADO |
| Hotel / Pousada Atalaia do Mariscal | base (Organic/Fuego/Metallo) | https://www.booking.com/hotel/br/pousada-atalaia-do-mariscal.pt-br.html?checkin=2026-10-09&checkout=2026-10-12&group_adults=2&group_children=0&no_rooms=1 | Booking | [PREENCHER] | [PREENCHER] | desconhecido | desconhecido | [PREENCHER] | [PREENCHER] | Rodada 1 (04–08/09/2026): sem disponibilidade — esgotado. Rodada 2 (09–12/10/2026): disponível, R$ 4.800 total, diária R$ 1.600,00, motor equiv. R$ 1.280,00 (referência, não entra em média). Rodada 3 (30/10–02/11/2026): disponível, R$ 4.500 total, diária R$ 1.500,00, motor equiv. R$ 1.200,00. Rodada 4 (19–22/11/2026): disponível, R$ 3.900 total, diária R$ 1.300,00, motor equiv. R$ 1.040,00 — Booking exibia aviso "6 hotéis 4 estrelas já indisponíveis" para o período, forte sinal de demanda regional. Âncora: Suíte Superior. | LINK_CADASTRADO_E_COLETADO_COM_SUCESSO |

**Coleta:** nenhum destes 10 concorrentes recém-cadastrados (`LINK_CADASTRADO`) deve ser coletado ainda — só o link e a classificação foram registrados nesta rodada. Nova coleta de preço só acontece mediante autorização explícita de Renildo, um concorrente/link por vez, como já ocorreu com Vila Boa Vida.

---

## Rodada 0 — Mapeamento de Âncoras Comparáveis (`REGRA_APROVADA_RENILDO`, 2026-07-25)

**Objetivo:** antes de qualquer nova coleta de preço (Rodada 1), definir qual acomodação de cada concorrente serve de âncora de comparação com a base da Pousada Arágua (Organic/Fuego/Metallo). **Nenhum preço foi coletado ou registrado em `COLETAS_CONCORRENCIA_REVENUE.csv` nesta rodada** — os valores abaixo aparecem só para justificar a escolha da âncora, não como dado coletado.

**Critérios mínimos de equivalência:** 2 adultos · acomodação privativa · banheiro privativo · cama de casal ou configuração equivalente · padrão visual minimamente compatível · conforto compatível com pousada. Excluído por regra: hostel, quarto compartilhado, beliche, quarto econômico muito inferior, quarto sem janela ou categoria claramente abaixo da proposta da Pousada Arágua. **Regra explícita seguida:** a acomodação âncora é a *menor comparável*, nunca automaticamente a mais barata do concorrente — nos casos abaixo em que a mais barata foi rejeitada, o motivo está registrado.

**Classificação de uso na média (`REGRA_APROVADA_RENILDO`, 2026-07-25):**

- `NUCLEO` — concorrentes núcleo da primeira rodada, peso `alto`: Vila Boa Vida, Vila Maciel, Pousada Kaloa Eco Village, Pousada Riviera Bombinhas, Pousada dos Ingleses, Pousada Dom Capudi, Pousada Kia Ora Bombinhas.
- `AMPLIADA` — entram na leitura de mercado mas com peso reduzido na média núcleo da base: UP Hotel Boutique, Morada do Guaruça (peso `baixo`).
- `TETO_MERCADO` — referência de teto/premium, não usada na média núcleo da base: Hotel/Pousada Atalaia do Mariscal (peso `não usar`).
- `PENDENTE` — sem uso na média até validação: Vila dos Açores (peso `não usar`).

| Concorrente | Acomodação âncora escolhida | Mais barata rejeitada? | Motivo da rejeição | Critério de equivalência | Status da âncora | Uso na média | Peso na média base | Observação |
|---|---|---|---|---|---|---|---|---|
| Vila Boa Vida | Quarto Duplo Standard (R$ 1.271/3 diárias) | Não — já era a mais barata e cumpria todos os critérios | — | 2 adultos ok · privativo ok · banheiro privativo ok · 1 cama de casal ok | `ANCORA_APROVADA` | `NUCLEO` | alto | Mesma âncora já usada na coleta original (2026-07-25); consistente. |
| Vila Maciel | Apartamento Standard (R$ 840 com desconto / R$ 1.050 original, 3 diárias) | Não — só existem 2 categorias, ambas equivalentes em padrão | — | 2 adultos ok · apartamento inteiro privativo ok · banheiro privativo ok · 1 cama de casal (+ sofá-cama) ok | `ANCORA_APROVADA` | `NUCLEO` | alto | Nota de qualidade Booking: 3/5. Site mostra tarifa com 20% de desconto ativo — registrar os dois valores (original e com desconto) se/quando coletar de fato. |
| Morada do Guaruça | Apartamento de 1 Quarto (R$ 1.835/3 diárias) | Não — era a mais barata das 5 categorias | — | 2 adultos ok · apartamento inteiro privativo ok · banheiro no quarto ok · 1 cama de casal grande (+ sofá-cama) ok | `ANCORA_PROVISORIA` (mantida, decisão de Renildo) | `AMPLIADA` | baixo | Aprovado por Renildo (2026-07-25): apartamento de 1 quarto, 50 m² com cozinha — produto mais completo que suíte base, entra na leitura de mercado com peso reduzido, não no núcleo. |
| Pousada Kaloa Eco Village | Suíte Standard (R$ 1.462/3 diárias) | Não — era a mais barata das 2 categorias | — | 2 adultos ok · suíte privativa ok · banheiro no quarto ok · 1 cama de casal ok | `ANCORA_APROVADA` | `NUCLEO` | alto | Nome da categoria já é literalmente "Suíte Standard" — boa equivalência de nomenclatura com a régua da Villa. |
| UP Hotel Boutique | Quarto Duplo Deluxe com Banheira (R$ 1.744 com desconto / R$ 1.875 original, 3 diárias) | **Sim** — havia tarifa de R$ 1.617, mas era plano "Máx. pessoas: 1" (ocupação single) | Não atende ao critério de 2 adultos — corretamente descartada, não é uma suíte inferior, é outro plano de ocupação | 2 adultos ok · quarto privativo ok · banheiro privativo ok · 1 cama de casal grande ok | `ANCORA_APROVADA` | `AMPLIADA` | baixo | Decisão explícita de Renildo (2026-07-25): serve como referência ampliada de mercado e percepção de valor, mas não deve puxar a média núcleo da base Organic/Fuego/Metallo. Propriedade "boutique" com banheira de hidromassagem em todas as categorias — padrão acima da média; nota de qualidade Booking 3/5. |
| Pousada Riviera Bombinhas | Suíte Loft Riviera (R$ 1.458/3 diárias) | Não — era a mais barata das 3 categorias | — | 2 adultos ok · suíte privativa ok · banheiro no quarto ok · 1 cama de casal ok | `ANCORA_APROVADA` | `NUCLEO` | alto | — |
| Pousada Kia Ora Bombinhas | Quarto Duplo Deluxe com Vista Lateral do Mar (R$ 2.006/3 diárias) | Não — era a mais barata entre as categorias listadas | — | 2 adultos ok · quarto privativo ok · banheiro privativo ok · 1 cama de casal grande ok | `ANCORA_APROVADA` | `NUCLEO` | alto | Preço bem acima da régua atual da Villa para o mesmo período (Organic/Fuego/Metallo Out. base = R$ 499) — relevante para leitura de mercado, não é motivo de rejeição da âncora. |
| Pousada dos Ingleses | Quarto Duplo Clássico (R$ 850 + R$ 120 de impostos/taxas = R$ 970 total, 3 diárias) | Não — era a mais barata das 4 categorias | — | 2 adultos ok · quarto privativo ok · banheiro privativo ok · 1 cama de casal ok | `ANCORA_APROVADA` | `NUCLEO` | alto | **Atenção para coleta futura:** este site mostra o preço-base separado dos impostos/taxas (não "impostos e taxas incluídos" como os demais) — somar R$ 120 sempre que coletar aqui. |
| Pousada Dom Capudi | Quarto Duplo (R$ 1.354/3 diárias) | Não — era a mais barata das 7 categorias | — | 2 adultos ok · quarto privativo ok · banheiro no quarto ok · 1 cama de casal ok | `ANCORA_APROVADA` | `NUCLEO` | alto | Página exibia aviso "Geralmente esgotado" — sinal de alta demanda, não afeta a escolha da âncora. |
| Vila dos Açores | Não identificada | — | — | Não avaliável — ver observação | `PRECISA_VALIDACAO_MANUAL` (mantida, decisão de Renildo) | `PENDENTE` | não usar | O motor próprio (Omnibees) não exibiu nenhuma categoria de quarto nem para 09–12/10/2026 (todas as datas de outubro aparecem bloqueadas no calendário) nem para uma data de teste próxima (25–26/07/2026, sem restrição no calendário, mas sem retorno de quartos após a busca). Não usar em média até haver preço e disponibilidade confirmados. |
| Hotel / Pousada Atalaia do Mariscal | Suíte Superior (R$ 4.800/3 diárias) | Não havia opção mais barata — é a mais barata das 7 categorias listadas | — | 2 adultos ok · suíte privativa ok · banheiro privativo ok · 1 cama de casal (+ solteiro/sofá-cama conforme categoria) ok | `ANCORA_APROVADA` (para uso como teto de mercado — Renildo resolveu a pendência anterior) | `TETO_MERCADO` | não usar | Decisão de Renildo (2026-07-25): não entra na média núcleo da base Organic/Fuego/Metallo. Serve como referência de produto premium — possível ponto de comparação para Duplex Soleil ou limite superior de mercado, não para a base. |

**Achado geral:** nenhum dos 11 concorrentes exigiu status `NAO_COMPARAVEL` — não foram encontrados hostels, quartos compartilhados, beliches como única opção, nem quartos sem janela em nenhuma das buscas. As duas exceções que precisam de decisão humana (Vila dos Açores e Atalaia do Mariscal) são por motivos diferentes: falta de dado disponível vs. possível descompasso de categoria/preço.

---

## Template — Concorrentes da Casa Arágua

Buscar sempre com perfil de casa/apartamento inteiro, preferencialmente 4 a 6 hóspedes.

| nome | unidade Villa de referência | link direto | canal | tipo | capacidade | café da manhã | piscina | distância da praia | peso na média | observações | status |
|---|---|---|---|---|---|---|---|---|---|---|---|
| [PREENCHER] | Casa Arágua | | | | | | | | | | PENDENTE |
| [PREENCHER] | Casa Arágua | | | | | | | | | | PENDENTE |
| [PREENCHER] | Casa Arágua | | | | | | | | | | PENDENTE |
| [PREENCHER] | Casa Arágua | | | | | | | | | | PENDENTE |
| [PREENCHER] | Casa Arágua | | | | | | | | | | PENDENTE |

---

## Próximo passo

Depois de preenchida esta cesta, cada linha vira ponto de coleta em `COLETAS_CONCORRENCIA_REVENUE.csv` nas datas prioritárias listadas em `ALERTAS_CONCORRENCIA_REVENUE.md`, seção "Rotina inicial de coleta".

**Regra explícita (2026-07-25):** uma coleta isolada (como a primeira, Vila Boa Vida/Booking/09–12 out. 2026) nunca vira recomendação de alteração de preço sozinha — é só um ponto da cesta competitiva. Recomendação tarifária em `ALERTAS_CONCORRENCIA_REVENUE.md` só deve ser gerada depois de coleta de mais concorrentes ou autorização explícita de Renildo.
