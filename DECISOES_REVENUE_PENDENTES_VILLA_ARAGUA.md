# DECISÕES DE REVENUE MANAGEMENT — VILLA ARÁGUA

**Status do arquivo:** persistido — registro vivo de decisões humanas sobre as recomendações de `DIAGNOSTICO_PRELIMINAR_REVENUE_VILLA_ARAGUA.md`.
**Regra de uso:** cada card mantém a recomendação original (histórico) e a decisão aplicada, lado a lado. Nenhum card é editado por cima — quando uma decisão muda, adiciona-se uma nova entrada de histórico, nunca se apaga a anterior.
**Governança:** todo valor aqui foi decidido e aplicado manualmente por Renildo, fora desta conversa. **A IA não alterou nenhuma tarifa em nenhum sistema real** (Stays, Booking, Decolar, Airbnb) — este arquivo só registra o que já foi feito, para manter o cérebro Villa Arágua IA sincronizado com a realidade.

## Vocabulário de status

- `PENDENTE` — recomendação apresentada, sem decisão de Renildo ainda.
- `EM_ANALISE` — Renildo está avaliando, sem decisão fechada.
- `DECIDIDO_APLICADO` — decisão tomada e já aplicada manualmente no motor/canal real.
- `DECIDIDO_NAO_APLICADO` — decisão tomada, mas ainda não aplicada no sistema (usar com data-limite quando existir).

---

## Contexto da rodada de decisão — 2026-07-25

Renildo confirmou disponibilidade antes de decidir: **somente a Casa Arágua está reservada, de 28/12/2026 a 06/01/2027** (cobre o Réveillon 2026 e a virada de ano). Todas as demais datas e unidades analisadas neste pacote estavam livres no momento da decisão. Isso resolve, para a Casa Arágua, a dúvida que o inventário original deixava como "confirmar se há reserva" para Réveillon 2026 e janeiro 2027 (dias 1-3).

---

## Card 1 — Páscoa 2027, Pousada Arágua

**Status:** `DECIDIDO_APLICADO`
**Decidido e aplicado por:** Renildo, manualmente, em 2026-07-25.

### Recomendação original (histórico)
`DIAGNOSTICO_PRELIMINAR_REVENUE_VILLA_ARAGUA.md`, alerta 1: tarifa de Páscoa aparecia **abaixo** da tarifa base de março em toda a régua da Pousada (Organic/Fuego/Metallo R$ 595, Terra/Wood R$ 684, Acqua R$ 744, Luna R$ 785, Duplex Soleil R$ 970) — classificado `CORRIGIR_AGORA`, "provável erro de régua". Casa Arágua já estava coerente (R$ 1.549 contra R$ 1.385 do mês base) e não precisava de correção.

### Decisão aplicada

| Acomodação | Valor decidido | Mínimo de noites |
|---|---|---|
| Organic / Fuego / Metallo | R$ 717 | 3 |
| Terra / Wood | R$ 825 | 3 |
| Acqua | R$ 896 | 3 |
| Luna | R$ 946 | 3 |
| Duplex Soleil | R$ 1.169 | 3 |
| Casa Arágua | R$ 1.549 (mantido) | — |

**Observação:** os valores decididos equivalem ao patamar já publicado para "Novembro/2026 feriado forte 19-21" na mesma régua — a decisão reaproveitou um patamar já existente em vez de criar tarifa nova. Mínimo de noites (3) não mudou em relação ao publicado antes da correção.

---

## Card 2 — Carnaval 2027, Pousada + Casa Arágua

**Status:** `DECIDIDO_APLICADO`
**Decidido e aplicado por:** Renildo, manualmente, em 2026-07-25.

### Recomendação original (histórico)
`DIAGNOSTICO_PRELIMINAR_REVENUE_VILLA_ARAGUA.md`, alerta 2: Pousada classificada `SUBIR_COM_CAUTELA` (Carnaval parecia abaixo do potencial e abaixo de janeiro base). Casa Arágua classificada `SUBIR_COM_PRIORIDADE` — R$ 1.649 ficava apenas R$ 29 acima do Duplex Soleil (R$ 1.620), enfraquecendo o posicionamento premium; faixa de estudo sugerida R$ 1.850–1.950.

### Decisão aplicada

| Acomodação | Valor decidido | Mínimo de noites |
|---|---|---|
| Organic / Fuego / Metallo | R$ 1.070 | 5 |
| Terra / Wood | R$ 1.231 | 5 |
| Acqua | R$ 1.338 | 5 |
| Luna | R$ 1.412 | 5 |
| Duplex Soleil | R$ 1.744 | 5 |
| Casa Arágua | R$ 1.890 | 5 |

**Observação:** os valores da Pousada passam a equivaler ao patamar já publicado para "Janeiro/2027 4-31" na mesma régua. Casa Arágua ficou dentro da faixa sugerida (R$ 1.850–1.950) e R$ 146 acima do Duplex Soleil — a Regra Casa Arágua x Duplex Soleil (Casa > Duplex em data forte) foi **validada por decisão humana concreta** nesta data. Mínimo de noites (5) não mudou.

---

## Card 3 — Casa Arágua, janeiro 2027 (período não reservado)

**Status:** `DECIDIDO_APLICADO`
**Decidido e aplicado por:** Renildo, manualmente, em 2026-07-25.

### Recomendação original (histórico)
`DIAGNOSTICO_PRELIMINAR_REVENUE_VILLA_ARAGUA.md`, alerta 3: Casa Arágua em janeiro/2027 (bloco 4-31) aparecia em R$ 1.624, abaixo do Duplex Soleil (R$ 1.744) — classificado `SUBIR_COM_CAUTELA`, faixa de estudo sugerida R$ 1.790–1.890. O bloco 1-3 estava marcado `NAO_MEXER_RESERVADO`, com observação "confirmar se há reserva".

### Confirmação de disponibilidade
Renildo confirmou: a Casa Arágua está reservada de **28/12/2026 a 06/01/2027** — esse período não foi e não deve ser alterado.

### Decisão aplicada

| Período | Valor decidido | Mínimo de noites |
|---|---|---|
| 28/12/2026 a 06/01/2027 | *(reservado — não alterado)* | — |
| A partir de 07/01/2027 | R$ 1.890 | 5 |

**Observação:** R$ 1.890 é o topo da faixa sugerida no diagnóstico original e o mesmo valor decidido para a Casa Arágua no Carnaval (Card 2) — a Casa Arágua passa a ter um patamar único de "alta temporada forte" (R$ 1.890 / mínimo 5 noites) cobrindo Carnaval e janeiro pós-reserva.

---

## Card 4 — Casa Arágua, setembro e outubro de 2026 (base)

**Status:** `DECIDIDO_APLICADO`
**Decidido e aplicado por:** Renildo, manualmente, em 2026-07-25.

### Recomendação original (histórico)
`DIAGNOSTICO_PRELIMINAR_REVENUE_VILLA_ARAGUA.md`, alerta 4: Casa Arágua abaixo do Duplex Soleil em ambos os períodos base (setembro R$ 684 vs Duplex R$ 732; outubro R$ 743 vs Duplex R$ 813) — classificado `SUBIR_COM_CAUTELA`, sem faixa numérica sugerida; o diagnóstico pedia apenas que fosse decisão consciente, não consequência automática da régua.

### Decisão aplicada

| Período | Valor decidido | Mínimo de noites |
|---|---|---|
| Setembro/2026 base | R$ 790 | 2 |
| Outubro/2026 base | R$ 890 | 2 |

**Observação:** R$ 790 fica acima do Duplex Soleil de setembro base (R$ 732) e R$ 890 fica acima do Duplex Soleil de outubro base (R$ 813) — a Casa Arágua passa a ficar consistentemente acima do topo da régua da Pousada nesses dois períodos. Mínimo de noites (2) não mudou.

---

## Regra de canais (decisão global)

**Status:** `DECIDIDO_APLICADO`
**Decidido e aplicado por:** Renildo, manualmente, em 2026-07-25, nos respectivos canais.

| Canal | Regra sobre o motor (Stays) |
|---|---|
| Booking | motor **+25%** |
| Decolar | motor **+17,6%** |
| Airbnb | motor **+17,6%** |

Esta é a primeira regra de markup por canal registrada no cérebro Villa Arágua IA — antes desta decisão, `concorrentes-otas.md` (skill `villa-aragua-pricing-revenue`) não tinha essa informação. Qualquer comparação de preço entre canais ou OTA deve usar esta regra a partir de agora.

---

## Card 5 — Tarifa tática dias comuns novembro 2026 — Pousada Arágua

**Status:** `DECIDIDO_APLICADO`
**Decidido e aplicado por:** Renildo, manualmente, em 2026-07-27.
**Classificação:** `TARIFA_TATICA_DIAS_DE_SEMANA_APLICADA_RENILDO`

### Recomendação original (histórico)

Rodada 5B do Radar de Concorrência Revenue (`RELATORIO_VISUAL_CONCORRENCIA_REVENUE_NOV_NORMAL_2026.md`, 09/11–12/11/2026): sinal de demanda `BAIXO`, 100% dos concorrentes disponíveis (núcleo 7/7, ampliada 2/2, teto 1/1), Villa +47,8% vs. núcleo e +27,1% vs. ampliada, veredito `ACIMA_DO_MERCADO_COM_RISCO`, diagnóstico preliminar `MANTER` com ponto de atenção explícito. A simulação tática subsequente recomendou `REDUZIR_10` **especificamente para 09/11–12/11** (única janela com dado real completo) e `AGUARDAR_DADOS` para 03/11–05/11, por falta de coleta própria do Radar nessa janela. A janela 16/11–18/11 havia sido sinalizada apenas como candidata a rodada futura de coleta, sem simulação nem recomendação.

### Decisão aplicada

| Acomodação | Valor decidido |
|---|---|
| Organic / Fuego / Metallo | R$ 475 |
| Terra / Wood | R$ 546 |
| Acqua | R$ 594 |
| Luna | R$ 627 |
| Duplex Soleil | R$ 774 |

**Datas de aplicação:**
- 02/11/2026 a 05/11/2026
- 09/11/2026 a 12/11/2026
- 16/11/2026 a 18/11/2026
- 22/11/2026 a 26/11/2026

### Observação

Apenas a janela **09/11–12/11** tem dado real completo do Radar sustentando a decisão (Rodada 5B) e está alinhada à recomendação `REDUZIR_10` da simulação (motor R$ 475 ≈ −9,7% sobre R$ 526). As demais três janelas (**02/11–05/11**, **16/11–18/11**, **22/11–26/11**) foram decisão gerencial de Renildo, baseada em histórico de menor ocupação em dias comuns de novembro e lógica tática de meio de semana — **sem coleta própria do Radar** para essas janelas especificamente. A janela 02/11–05/11 inclui um dia (02/11) a mais do que a faixa avaliada na simulação (03/11–05/11). A janela 22/11–26/11 começa em 22/11, um domingo — a primeira noite desse intervalo é tecnicamente uma noite de fim de semana dentro de um período tratado como "dias comuns"; registrado como observação factual de calendário, sem correção. Confirmado que a tarifa **não** foi aplicada em Finados (30/10–02/11), finais de semana em geral, feriado de Consciência Negra (19/11–22/11), outras datas especiais, nem em dezembro/janeiro/fevereiro — esses períodos permanecem com o tarifário anterior, protegido.

---

## Card 6 — Tarifa tática última semana de janeiro 2027 — Pousada Arágua

**Status:** `DECIDIDO_APLICADO`
**Decidido e aplicado por:** Renildo, manualmente, em 2026-07-28.
**Classificação:** `TARIFA_TATICA_ULTIMA_SEMANA_JANEIRO_2027_APLICADA_RENILDO`

### Recomendação original (histórico)

Rodada 9D do Radar de Concorrência Revenue (`RELATORIO_VISUAL_CONCORRENCIA_REVENUE_JANEIRO_2027.md`, 24/01–31/01/2027): sinal de demanda `MÉDIO` com tendência de queda, núcleo 100% disponível (7/7), sem aviso de escassez do Booking, veredito `ACIMA_DO_NUCLEO_MAS_DEFENSAVEL`, diagnóstico preliminar `MANTER` com ponto de atenção. O relatório **não** recomendou redução — o sinal era `MÉDIO`, não `BAIXO` confirmado (diferente do precedente de novembro/2026, Card 5). Na visualização solicitada em seguida, Vila Maciel e Pousada dos Ingleses mostraram queda nominal de preço consistente ao longo das 4 sub-rodadas de janeiro, com o menor valor do conjunto batendo justamente em 24–31/01.

### Decisão aplicada

| Acomodação | Valor decidido (motor) |
|---|---|
| Organic / Fuego / Metallo | R$ 985 |
| Terra / Wood | R$ 1.133 |
| Acqua | R$ 1.231 |
| Luna | R$ 1.300 |
| Duplex Soleil | R$ 1.606 |

**Datas de aplicação:** 24/01/2027 a 31/01/2027 (noites de 24 a 30/01, check-out em 31/01).

**Observação:** redução aproximada de ~8% sobre o motor base publicado do bucket "Janeiro/2027 4-31" (R$ 1.070 → R$ 985 na base Organic/Fuego/Metallo), com os demais valores seguindo a régua percentual já usada em decisões anteriores (Terra/Wood ≈115%, Acqua ≈125%, Luna ≈132%, Duplex Soleil ≈163%). Ajuste cirúrgico limitado a esta única janela de 7 noites — **não** aplicado à primeira quinzena de janeiro (03–16/01, diagnóstico `PROTEGER`) nem à semana intermediária (17–23/01, diagnóstico `MANTER`), e **não** altera Natal, Réveillon ou Carnaval. Não deve ser anunciado como promoção. Motivo declarado por Renildo: antecipar-se a um possível enfraquecimento de demanda ainda não confirmado por dado de ocupação real, evitando chegar perto da data com vagas — decisão gerencial, não recomendação automática da IA (o diagnóstico do Radar para esta janela foi `MANTER`, não `BAIXAR_COM_JUSTIFICATIVA`).

---

## Card 7 — Tarifa tática final de fevereiro 2027 — Pousada Arágua

**Status:** `DECIDIDO_APLICADO`
**Decidido e aplicado por:** Renildo, manualmente, em 2026-07-28.
**Classificação:** `TARIFA_TATICA_FINAL_FEVEREIRO_2027_APLICADA_RENILDO`

### Recomendação original (histórico)

Radar de Concorrência Revenue — Fevereiro 2027 fora do Carnaval (`RELATORIO_VISUAL_CONCORRENCIA_REVENUE_FEVEREIRO_2027_POS_CARNAVAL.md`). A análise mais crítica veio da Rodada 11D (24/02–28/02/2027): sinal de demanda `MISTO/CONTRADITÓRIO` (Vila Maciel, Pousada dos Ingleses e UP Hotel Boutique nos menores preços de toda a série, mas o teto de mercado Atalaia 100% esgotado — sinal inédito em toda a série do Radar), veredito `ACIMA_DO_MERCADO_COM_RISCO`, diagnóstico preliminar `MANTER com ponto de atenção forte`. O relatório **não** recomendou redução nem simulou cenário — o sinal era contraditório, não `BAIXO` confirmado (critério usado em novembro/2026).

### Decisão aplicada

| Acomodação | Valor decidido (motor) |
|---|---|
| Organic / Fuego / Metallo | R$ 756 |
| Terra / Wood | R$ 869 |
| Acqua | R$ 945 |
| Luna | R$ 998 |
| Duplex Soleil | R$ 1.232 |

**Datas de aplicação:** 21/02/2027 a 28/02/2027 (noites de 21 a 27/02, check-out em 28/02).

**Observação:** redução aproximada de ~8% sobre o motor base publicado do bucket "Fevereiro/2027 base" (R$ 822 → R$ 756 na base Organic/Fuego/Metallo), com os demais valores seguindo a régua percentual já usada em decisões anteriores (Terra/Wood ≈115%, Acqua ≈125%, Luna ≈132%, Duplex Soleil ≈163%). A análise mais crítica que motivou a decisão veio especificamente da Rodada 11D (24–28/02); Renildo aplicou a tarifa em um intervalo maior (21–28/02), que também alcança parte da Rodada 11C (17–24/02, diagnóstico `MANTER com ponto de atenção`, sinal `MÉDIO` amolecendo — mais brando que o sinal da 11D). Este registro não corrige nem bloqueia a decisão, apenas documenta essa diferença de janelas. Não aplicado ao Carnaval nem ao pré-Carnaval, não aplicado ao restante de fevereiro fora do intervalo, e não se estende automaticamente a março. Não deve ser anunciada como promoção. Decisão gerencial, não recomendação automática da IA (o diagnóstico do Radar para a 11D foi `MANTER`, não `BAIXAR_COM_JUSTIFICATIVA`).

---

## Card 8 — Correção tarifária Março + Páscoa 2027 — Pousada Arágua

**Status:** `DECIDIDO_APLICADO`
**Decidido e aplicado por:** Renildo, manualmente, no motor de reservas.
**Classificações:** `CORRECAO_TARIFARIA_MARCO_2027_APLICADA_RENILDO` (março comum) e `TARIFA_CORRIGIDA_PASCOA_2027_APLICADA_RENILDO` (Páscoa). Status geral: `CORRECAO_TARIFARIA_MARCO_E_PASCOA_2027_APLICADA_RENILDO`.

### Recomendação original (histórico)

- **Páscoa 2027:** Card 1 acima (`DECIDIDO_APLICADO`, 2026-07-25) havia fixado a base em R$ 717 — correção de um erro de régua identificado internamente (a tarifa de Páscoa aparecia abaixo do mês base de março), não uma decisão ancorada em benchmarking de concorrência. A Rodada 13 (`RELATORIO_VISUAL_CONCORRENCIA_REVENUE_PASCOA_2027.md`) foi o primeiro benchmarking real feito contra esse valor e revelou a Villa ≈62,6% acima da Kia Ora, o concorrente núcleo mais caro coletado (motor equivalente médio R$ 441,07/diária). Veredito: `ACIMA_DO_MERCADO_COM_RISCO`. Diagnóstico preliminar: `ESPERAR` (não `BAIXAR_COM_JUSTIFICATIVA`). O relatório apresentou uma mesa de cenários de simulação (manter, −5% a −20%) apenas como referência, a pedido de Renildo, sem recomendar qual aplicar.
- **Março comum:** Rodada 12 (`RELATORIO_VISUAL_CONCORRENCIA_REVENUE_MARCO_2027.md`), base R$ 607, diagnósticos `MANTER` (12A, 12B) e `PROTEGER` (12C) — nenhum sinal de demanda `BAIXO` confirmado em nenhum dos três blocos.

### Decisão aplicada

| Acomodação | Valor decidido (motor) |
|---|---|
| Organic / Fuego / Metallo | R$ 529 |
| Terra / Wood | R$ 608 |
| Acqua | R$ 661 |
| Luna | R$ 698 |
| Duplex Soleil | R$ 862 |

**Períodos de aplicação:**
- Março comum: 01/03/2027 a 26/03/2027 (noites de 01 a 25/03, check-out em 26/03).
- Páscoa 2027: 26/03/2027 a 29/03/2027 (noites de 26, 27 e 28/03, check-out em 29/03). Mínimo de 3 diárias mantido.

**Motivo — Páscoa:** aproximar a Villa da Kia Ora (concorrente núcleo mais caro coletado na Rodada 13), reduzindo o gap de ≈62,6% para ≈20% (R$ 529 ÷ R$ 441,07 ≈ 1,199×), diminuindo o risco de ficar descolada do mercado e perder conversão, mantendo posicionamento premium.

**Motivo — março comum:** corrigir a coerência tarifária do mês — ao reduzir a Páscoa para R$ 529 (abaixo da base anterior de março, R$ 607), a Páscoa ficaria mais barata que um mês comum, o que não faz sentido para um feriado forte. Março não teve sinal de demanda `BAIXO` confirmado (Rodada 12 mostrou `MANTER`/`PROTEGER`), então este ajuste **não** é promoção ou liquidação — é correção de coerência e posicionamento, mantendo a Villa acima do núcleo mais barato coletado.

### Observações de rastreabilidade

- Este Card **corrige/substitui, para fins de tarifa vigente, o valor decidido no Card 1** para o período de Páscoa — o Card 1 permanece registrado acima como histórico, sem alteração, para preservar a rastreabilidade da decisão original de 2026-07-25.
- Não aplicado automaticamente a abril — qualquer extensão exige nova decisão explícita.
- Não altera janeiro (Cards 5, 6), fevereiro (Card 7), Carnaval (Card 2), Natal ou Réveillon.
- Não deve ser anunciada como promoção pública.
- Mínimo de noites não alterado em nenhum dos dois períodos, exceto manutenção do mínimo de 3 diárias já vigente na Páscoa.
- Decisão gerencial de Renildo, não recomendação automática da IA — o diagnóstico do Radar para a Páscoa foi `ESPERAR` e para março foi `MANTER`/`PROTEGER`, nenhum dos dois `BAIXAR_COM_JUSTIFICATIVA`.

---

## O que este registro não faz

- Não altera nada em Stays, Booking, Decolar ou Airbnb — Renildo já aplicou manualmente antes deste registro.
- Não aprova automaticamente nenhuma decisão futura semelhante — cada card novo segue precisando de decisão humana explícita.
- Não apaga a recomendação original de `DIAGNOSTICO_PRELIMINAR_REVENUE_VILLA_ARAGUA.md` — o histórico fica preservado nos dois arquivos.
