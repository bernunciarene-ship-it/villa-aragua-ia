# ALERTAS DE CONCORRÊNCIA — RADAR DE CONCORRÊNCIA REVENUE — VILLA ARÁGUA

**Status do módulo:** `EM_IMPLANTACAO_MANUAL_ASSISTIDA`
**Função:** modelo de saída que o agente `villa-precificacao-calendario` (com apoio da skill `villa-aragua-pricing-revenue`) deve produzir sempre que houver coleta suficiente em `COLETAS_CONCORRENCIA_REVENUE.csv` para um período. Cada alerta é uma recomendação — nunca uma alteração.
**Pré-requisito de qualquer alerta real:** `CESTA_COMPETITIVA_REVENUE_VILLA_ARAGUA.md` preenchida para o produto analisado + linhas correspondentes em `COLETAS_CONCORRENCIA_REVENUE.csv`. Sem coleta, não existe alerta — só o card vazio de rotina (seção 3).
**Padrão de saída em duas camadas (`REGRA_APROVADA_RENILDO`, 2026-07-25):** a partir de agora, toda rodada do Radar passa a exigir resumo executivo **e** relatório visual de preços (tabela aberta por concorrente). Regra completa registrada em `.claude/agents/villa-precificacao-calendario.md`. Modelo de referência já aplicado: `RELATORIO_VISUAL_CONCORRENCIA_REVENUE_SET_OUT_2026.md`.

---

## 1. Modelo de card (usar exatamente esta estrutura)

```
### Período: [período analisado]

- Produto Villa: [Pousada Arágua / Casa Arágua]
- Unidade Villa: [acomodação de referência]
- Canal de comparação: [Booking / Airbnb / Decolar / site próprio]
- Preço atual motor Villa: [R$ valor]
- Preço visível Villa no canal: [R$ valor — motor × markup do canal, ver REGRAS_CONVERSAO_OTA_MOTOR_REVENUE.md]
- Média concorrência visível no canal: [R$ valor]
- Menor concorrente: [nome — R$ valor]
- Maior concorrente: [nome — R$ valor]
- Posição da Villa vs. média: [acima / na média / abaixo, com %]
- Diagnóstico: [MANTER / PROTEGER / CORRIGIR_AGORA / SUBIR_COM_CAUTELA / SUBIR_COM_PRIORIDADE / BAIXAR_COM_JUSTIFICATIVA / ESPERAR / COMPARAR_MELHOR / AGUARDAR_DADOS / NAO_MEXER_RESERVADO]
- Preço visível recomendado no canal: [R$ valor]
- Preço recomendado para motor de reserva: [R$ valor — aplicar fórmula de conversão]
- Justificativa: [1–3 frases, baseadas só no que foi coletado]
- Status: PENDENTE_DECISAO_RENILDO
```

### Regra de preenchimento por produto

- **Pousada Arágua:** `Unidade Villa` do card acima é sempre a categoria base (Organic/Fuego/Metallo), coletada com perfil casal/2 adultos/1 unidade. Depois de preencher o card para a base, acrescentar a projeção pela régua interna (Terra/Wood ×1,15 · Acqua ×1,25 · Luna ×1,32 · Duplex Soleil ×1,63 ou ×1,50 em baixa pura) como uma tabela extra no mesmo card, em vez de abrir um card novo por suíte — ver `REGRAS_CONVERSAO_OTA_MOTOR_REVENUE.md`, seção 4.1, para o formato dessa tabela.
- **Casa Arágua:** `Unidade Villa` é sempre "Casa Arágua", coletada com perfil de casa inteira, 4 a 6 hóspedes. Não há régua a projetar — a Casa é produto único.

### Vocabulário de diagnóstico deste módulo (`REGRA_APROVADA_RENILDO`, 2026-07-25 — unificado com o agente `villa-precificacao-calendario`)

Separar sempre três coisas: (1) status da coleta (`COLETADO_COM_SUCESSO`/`PRECISA_VALIDACAO_MANUAL`/`INDISPONIVEL`/`LINK_COM_PROBLEMA`/`LINK_CADASTRADO`), (2) classificação do concorrente (`NUCLEO`/`AMPLIADA`/`TETO_MERCADO`/`PENDENTE`), e (3) o diagnóstico de preço abaixo — só o terceiro vai no campo `Diagnóstico` do card.

- `MANTER` — Villa bem posicionada frente à concorrência coletada.
- `PROTEGER` — tarifa de data forte já decidida; não abrir espaço para desconto ou redução.
- `CORRIGIR_AGORA` — erro evidente de régua ou tarifa; corrigir sem esperar próxima rodada.
- `SUBIR_COM_CAUTELA` — Villa parece abaixo da média núcleo, mas com poucos dados ou concorrência fraca na amostra.
- `SUBIR_COM_PRIORIDADE` — Villa claramente abaixo da média núcleo com boa amostra e alta procura esperada no período.
- `BAIXAR_COM_JUSTIFICATIVA` — Villa destoando muito acima da concorrência comparável, com risco real de perda de reserva; baixar só com justificativa registrada, nunca automático.
- `ESPERAR` — período ainda distante ou baixa prioridade comercial agora, mesmo com dado suficiente.
- `COMPARAR_MELHOR` — amostra de concorrentes fraca/desatualizada ou com excesso de `AMPLIADA`/`PENDENTE`; pedir nova coleta antes de recomendar.
- `AGUARDAR_DADOS` — coleta insuficiente ou amostra do núcleo incompleta para qualquer leitura confiável.
- `NAO_MEXER_RESERVADO` — período já com reserva confirmada; vira aprendizado para datas futuras, nunca alteração retroativa.

**Regras de tradução dos termos antigos:** `BAIXAR` (sem qualificador) → `BAIXAR_COM_JUSTIFICATIVA`; `COMPARAR_CONCORRENCIA` → `COMPARAR_MELHOR`. `PRECISA_VALIDACAO_MANUAL`, `COLETADO_COM_SUCESSO` e `INDISPONIVEL` não são diagnóstico de preço — são status de coleta, tratados à parte.

Todo card nasce com `status: PENDENTE_DECISAO_RENILDO`. Quando Renildo decidir, o card correspondente deve ser referenciado em `DECISOES_REVENUE_PENDENTES_VILLA_ARAGUA.md` como um novo registro — este arquivo não muda o próprio status para `DECIDIDO_APLICADO`; quem registra decisão aplicada é sempre o arquivo de decisões.

---

## 2. Exemplo ilustrativo (não é dado real — só demonstra o formato)

```
### Período: ILUSTRATIVO — não usar como referência real

- Produto Villa: Casa Arágua
- Unidade Villa: Casa Arágua
- Canal de comparação: Booking
- Preço atual motor Villa: R$ 1.890,00
- Preço visível Villa no canal: R$ 2.362,50
- Média concorrência visível no canal: R$ 2.100,00 (exemplo)
- Menor concorrente: Concorrente Exemplo A — R$ 1.900,00 (exemplo)
- Maior concorrente: Concorrente Exemplo B — R$ 2.400,00 (exemplo)
- Posição da Villa vs. média: acima, +12,5% (exemplo)
- Diagnóstico: COMPARAR_MELHOR
- Preço visível recomendado no canal: [depende de coleta real]
- Preço recomendado para motor de reserva: [depende de coleta real]
- Justificativa: exemplo criado só para mostrar como o card deve ser preenchido depois que houver coleta real em COLETAS_CONCORRENCIA_REVENUE.csv.
- Status: PENDENTE_DECISAO_RENILDO
```

---

## 3. Rotina inicial de coleta — datas prioritárias

Nenhuma destas datas tem coleta ainda. Esta é a fila de trabalho — cada linha vira um card do modelo acima assim que houver dados suficientes em `COLETAS_CONCORRENCIA_REVENUE.csv`.

| Data/período | Produto(s) a coletar | Status |
|---|---|---|
| Setembro 2026 | Pousada Arágua + Casa Arágua | PENDENTE_COLETA |
| 7 de Setembro 2026 | Pousada Arágua: **coletada (Rodada 1, 04–08/09/2026)** — ver seção 4. Casa Arágua ainda pendente. | Pousada: `COLETADO`; Casa: `PENDENTE_COLETA` |
| Outubro 2026 | Pousada Arágua + Casa Arágua | PENDENTE_COLETA |
| 12 de Outubro 2026 | Pousada Arágua: **coletada (Rodada 2, 09–12/10/2026)** — ver seção 5. Casa Arágua ainda pendente. | Pousada: `COLETADO`; Casa: `PENDENTE_COLETA` |
| Novembro 2026 | Pousada Arágua + Casa Arágua | PENDENTE_COLETA |
| 2 de Novembro 2026 | Pousada Arágua + Casa Arágua | PENDENTE_COLETA |
| 20 de Novembro 2026 | Pousada Arágua + Casa Arágua | PENDENTE_COLETA |
| Dezembro/2026 até dia 17 | Pousada Arágua + Casa Arágua | PENDENTE_COLETA |
| Natal 2026 | Pousada Arágua + Casa Arágua | PENDENTE_COLETA |
| Réveillon 2026/2027 | Pousada Arágua *(Casa Arágua reservada — não coletar para decisão de preço, só para aprendizado)* | PENDENTE_COLETA |
| Janeiro 2027 | Pousada Arágua + Casa Arágua *(a partir de 07/01 para a Casa — ver `DECISOES_REVENUE_PENDENTES_VILLA_ARAGUA.md`)* | PENDENTE_COLETA |
| Fevereiro 2027 | Pousada Arágua + Casa Arágua | PENDENTE_COLETA |
| Carnaval 2027 | Pousada Arágua + Casa Arágua | PENDENTE_COLETA |
| Março 2027 | Pousada Arágua + Casa Arágua | PENDENTE_COLETA |
| Páscoa 2027 | Pousada Arágua + Casa Arágua | PENDENTE_COLETA |
| Abril 2027 | Pousada Arágua + Casa Arágua | PENDENTE_COLETA |

**Correção de 2026-07-25 — perfil de coleta da Pousada (`REGRA_APROVADA_RENILDO`):** a coleta da Pousada usa sempre o perfil casal (2 adultos, 1 unidade) e tem como unidade Villa de referência a **categoria base (Organic/Fuego/Metallo)** — não o Duplex Soleil, e não uma suíte específica. Não pesquisar concorrente separado por suíte neste primeiro momento: o preço coletado vira âncora da base, e as demais categorias (Terra/Wood, Acqua, Luna, Duplex Soleil) são obtidas por projeção da régua interna, não por nova coleta. Metodologia e exemplo completo em `REGRAS_CONVERSAO_OTA_MOTOR_REVENUE.md`, seção 4.1.
**Unidade de referência da Casa:** Casa Arágua (unidade única), perfil de casa/apartamento inteiro, preferencialmente 4 a 6 hóspedes — pesquisa própria, nunca usa o perfil casal nem a régua da Pousada.

### Ordem sugerida de execução

1. Preencher `CESTA_COMPETITIVA_REVENUE_VILLA_ARAGUA.md` (pré-requisito de tudo).
2. Coletar as datas de maior prioridade comercial primeiro: 7 de Setembro 2026, Réveillon 2026/2027, Carnaval 2027, Páscoa 2027 e Natal 2026 (feriados fortes já com preço decidido em `DECISOES_REVENUE_PENDENTES_VILLA_ARAGUA.md` — a coleta aqui serve para validar/ajustar, não para decidir do zero).
3. Seguir para as datas base restantes na ordem cronológica da tabela acima.

---

## 4. Rodada 1 — Resultado (Pousada Arágua, 04–08/09/2026, feriado 7 de Setembro + Curitiba 08/09)

**Coletado em:** 2026-07-25, via Booking (Claude in Chrome), perfil casal/2 adultos/0 crianças/1 acomodação, âncoras aprovadas na Rodada 0. Dados completos em `COLETAS_CONCORRENCIA_REVENUE.csv`. **Este é diagnóstico preliminar — nenhuma recomendação de alteração tarifária foi gerada.**

### Concorrentes coletados com sucesso (7 de 10 tentados)
Vila Boa Vida, Vila Maciel, Pousada Kaloa Eco Village, Pousada Riviera Bombinhas, Pousada dos Ingleses, Pousada Kia Ora Bombinhas (núcleo, 6 de 7) + UP Hotel Boutique (ampliada, 1 de 2).

### Concorrentes com falha/indisponíveis (3 de 10)
- **Pousada Dom Capudi** (núcleo) — `PRECISA_VALIDACAO_MANUAL`: sem disponibilidade no Booking para 04–08/09/2026 (esgotado).
- **Morada do Guaruça** (ampliada) — `PRECISA_VALIDACAO_MANUAL`: âncora aprovada (Apartamento de 1 Quarto) não disponível para o período; outras categorias mais caras seguiam à venda, mas não foram usadas por não serem a âncora aprovada.
- **Hotel/Pousada Atalaia do Mariscal** (teto de mercado) — `PRECISA_VALIDACAO_MANUAL`: sem disponibilidade no Booking para 04–08/09/2026 (esgotado); site ofereceu datas alternativas não coincidentes com o período pedido.

**Vila dos Açores** não foi tentada nesta rodada (pendente/não usar, por decisão já registrada).

### 1. Média núcleo (n=6 de 7 — Pousada Dom Capudi indisponível, excluído do cálculo)

| Métrica | Valor |
|---|---|
| Menor diária Booking | R$ 234,50 (Vila Maciel) |
| Maior diária Booking | R$ 585,25 (Pousada Kia Ora Bombinhas) |
| Média diária Booking | R$ 419,63 |
| Mediana diária Booking | R$ 448,63 |
| Média motor equivalente (÷1,25) | R$ 335,70 |

### 2. Média ampliada (n=1 de 2 — Morada do Guaruça indisponível, excluído)

| Métrica | Valor |
|---|---|
| Média diária Booking (só UP Hotel Boutique) | R$ 603,00 |
| Média motor equivalente | R$ 482,40 |

**Nota:** com apenas 1 de 2 concorrentes coletados, esta média ampliada é uma referência fraca nesta rodada — não tratar como conclusiva.

### 3. Teto de mercado

Sem dado nesta rodada — Hotel/Pousada Atalaia do Mariscal (único concorrente desta categoria) estava indisponível no Booking para 04–08/09/2026.

### Villa Arágua no período

| Referência | Valor |
|---|---|
| Base no motor (Organic/Fuego/Metallo, Setembro/2026 feriado, já publicado) | R$ 499,00 |
| Estimada no Booking (motor × 1,25) | R$ 623,75 |

### Posição preliminar da Villa

- **Vs. média núcleo:** R$ 623,75 (Booking) e R$ 499,00 (motor) ficam **acima** da média núcleo em ambas as bases — aproximadamente **+48,7%** acima da média núcleo (Booking: 623,75 vs 419,63; motor: 499,00 vs 335,70 — mesma proporção, como esperado pela conversão constante).
- **Vs. média ampliada (n=1):** R$ 623,75 fica **levemente acima** de R$ 603,00 (UP Hotel Boutique) — cerca de **+3,4%**, uma diferença pequena, mas a base de comparação é fraca (um único concorrente).

### Diagnóstico preliminar (sem recomendação automática)

**Classificação preliminar oficial: `MANTER` / `ESPERAR`**

**Motivo:** a Villa Arágua está bem acima da média núcleo, mas praticamente alinhada à referência ampliada. Além disso, houve concorrentes indisponíveis/esgotados no período, o que indica pressão de demanda e reduz a força da média núcleo como argumento para baixar preço. Portanto, não há recomendação de baixar preço neste momento. Também não há recomendação de subir sem nova evidência.

**Observação:** a média núcleo pode subestimar o mercado real quando concorrentes relevantes já estão esgotados. Esgotamento deve ser tratado como sinal de demanda, não como preço zero.

**Nenhuma ação, ajuste ou recomendação de preço é derivada deste diagnóstico.** Este diagnóstico permanece preliminar em `ALERTAS_CONCORRENCIA_REVENUE.md` e não foi movido para `DECISOES_REVENUE_PENDENTES_VILLA_ARAGUA.md`.

### Novos indicadores (a partir desta rodada)

- **`indice_disponibilidade_nucleo`** — proporção do núcleo efetivamente coletada: 6 de 7 = **85,7%**.
- **`indice_disponibilidade_total_tentado`** — proporção de todos os concorrentes tentados (núcleo + ampliada + teto, excluindo Vila dos Açores por estar `PENDENTE`) efetivamente coletada: 7 de 10 = **70%**.
- **`sinal_demanda`: `BAIXO` / `MÉDIO` / `ALTO`** — nesta rodada: **`MÉDIO/ALTO`**.

---

## 4R. Rodada 1R — Reprocessamento Estratégico com Revenue + Growth (Pousada Arágua, 04–08/09/2026)

**O que é isto:** leitura complementar/adendo sobre a Rodada 1, cruzando os mesmos dados já coletados com o contexto estratégico da reabertura da Pousada Arágua (04–08/09/2026), a campanha Meta Ads prevista para 01/08/2026, e o peso esperado da venda direta frente às OTAs. **Não substitui, não apaga e não altera o diagnóstico original da Rodada 1 (`MANTER`/`ESPERAR`, seção 4 acima)** — este é um segundo olhar, registrado ao lado do primeiro.

**Executado em:** 2026-07-25, por meio de acionamento real do agente `villa-precificacao-calendario` (via subagente), não por execução direta na memória desta conversa.

### Confirmação de execução

- Agente acionado: **SIM**
- Skill `villa-aragua-pricing-revenue` consultada: **SIM**
- Skill `villa-aragua-growth-marketer` consultada: **SIM**
- Arquivos/referências consultados: `villa-aragua-growth-marketer/references/reserva-direta-reducao-otas.md`; `villa-aragua-pricing-revenue/references/concorrentes-otas.md`; `SKILL.md` das duas skills; dados já coletados da Rodada 1 (fornecidos no pedido, sem nova coleta).
- Regras aplicadas: vocabulário oficial de 10 estados de diagnóstico (`REGRA_APROVADA_RENILDO`); conversão Booking = motor × 1,25; classificação núcleo/ampliada/teto (`uso_na_media`); regra "Leitura comercial antes de recomendar baixa de preço"; regra "Evitar guerra de preço com Booking/Airbnb"; princípio "reserva direta > preço mais baixo".

### Leitura de Revenue

A Villa está em R$ 499,00 no motor para 04–08/09/2026, equivalente a R$ 623,75 no Booking (499 × 1,25). Contra a média núcleo (R$ 419,63 Booking / R$ 335,70 motor equivalente), a diferença é **+48,7%** — leitura correta é motor vs. motor equivalente do núcleo, não motor vs. Booking bruto do concorrente. Contra a média ampliada (R$ 603,00, amostra fraca, só 1 de 2 concorrentes), a diferença cai para **+3,4%** — quase empatada, mas essa média pesa pouco (`uso_na_media: AMPLIADA`, amostra incompleta). O índice de disponibilidade do núcleo (85,7%, com Dom Capudi esgotado) e o índice total (70%, com Morada do Guaruça e Atalaia do Mariscal também esgotados), somados ao feriado prolongado (7 de Setembro + feriado de Curitiba), sustentam sinal de demanda `MÉDIO/ALTO` — não um cenário de necessidade de baixa.

### Leitura comercial (growth-marketer)

`reserva-direta-reducao-otas.md`: "a Villa Arágua não compete por ser mais barata que a OTA — compete por valor agregado (atendimento, relação, previsibilidade). Baixar preço para 'vencer' a OTA corrói margem sem necessidade e não é a estratégia da marca." O mesmo arquivo reconhece papel legítimo da OTA em baixa demanda/descoberta — que não é o caso aqui, com sinal de demanda médio/alto e a data coincidindo com reabertura + campanha Meta Ads programada. `concorrentes-otas.md` reforça: preço de concorrente é referência de calibragem, nunca ordem a seguir — "pode significar manter um preço mais alto que um concorrente específico, se a Villa Arágua entrega mais estrutura." Como a média núcleo Booking é preço de OTA, não de motor, essa leitura sustenta não usar o gap de 48,7% como gatilho automático de baixa.

### Respostas às 7 perguntas

1. **O diagnóstico `MANTER`/`ESPERAR` original continua adequado?** Sim — os fatores novos (reabertura, Meta Ads, venda direta) reforçam a mesma leitura, não a contradizem.
2. **A campanha Meta Ads e a venda direta sustentam manter o preço mesmo acima da média núcleo?** Sim. A campanha programada para 01/08/2026 e a força esperada do WhatsApp dão à Villa um canal de conversão que não depende de igualar preço de OTA.
3. **O preço deve ser `PROTEGER`, `MANTER` ou `ESPERAR`/monitorar?** `PROTEGER` o motor atual (feriado forte, reabertura, sem sinal de necessidade de caixa urgente) combinado com `ESPERAR`/monitorar quanto a qualquer ajuste — não mexer agora, acompanhar ritmo de reservas após o lançamento da campanha.
4. **Risco de baixar agora?** Corrói margem sem necessidade comprovada, ancora a percepção de valor da reabertura num preço mais baixo logo no primeiro feriado forte pós-reabertura, e cria precedente difícil de reverter em datas futuras equivalentes.
5. **Risco de manter?** Ficar com quartos vazios se a campanha Meta Ads não gerar volume de leads a tempo, ou perder para um concorrente núcleo mais barato sem o hóspede perceber o diferencial de atendimento/estrutura — risco mitigável, não motivo para baixa preventiva.
6. **Orientação comercial para vender esse preço?** Reforçar no WhatsApp e na campanha o argumento de atendimento próximo do início ao fim da estadia, previsibilidade e estrutura (café na suíte, piscina, churrasqueira) — nunca comparar número de OTA; se o lead citar preço do Booking, reforçar valor, sem inventar comparação numérica.
7. **Deve haver handoff para `villa-comercial-reservas`?** Sim — para produzir a resposta padrão de WhatsApp a objeções de preço citando Booking/concorrente nesse período, e para alinhar a copy da campanha Meta Ads de reabertura em torno de valor (não desconto) para 04–08/09/2026.

### Diagnóstico final complementar

**`PROTEGER` + `ESPERAR`.** A tarifa do motor (R$ 499,00) para 04–08/09/2026 deve ser protegida de qualquer redução automática motivada só pela média núcleo Booking, dado o sinal de demanda médio/alto, a reabertura da pousada e a campanha Meta Ads programada; ao mesmo tempo, o período segue em modo de espera/monitoramento — não há dado de ritmo de reservas pós-campanha para justificar subir ou baixar preço agora.

### Riscos

- **Risco de baixar agora:** perda de margem na reabertura, ancoragem de preço baixo para o público vindo via Meta Ads, sinal de fragilidade no relançamento da marca — sem necessidade comprovada.
- **Risco de manter:** possível vacância se a campanha atrasar ou performar abaixo do esperado; mitigável monitorando ritmo de reservas diretas e reforçando valor (não desconto) se a ocupação não evoluir perto da data.

### Orientação comercial

Sustentar o preço via comunicação de valor: atendimento direto do início ao fim da estadia, estrutura completa (café na suíte, piscina, churrasqueira) e a narrativa de reabertura como motivo de desejo, não de desconto. A campanha Meta Ads deve direcionar para WhatsApp, priorizando conversa qualificada sobre esse período; qualquer objeção de preço citando Booking deve ser respondida reforçando diferencial, nunca com redução automática de tarifa.

### Status

`DIAGNOSTICO_COMPLEMENTAR_SEM_ALTERACAO_TARIFARIA`

---

## 5. Rodada 2 — Resultado (Pousada Arágua, 09–12/10/2026, feriado 12 de Outubro)

**Coletado em:** 2026-07-25, via Booking (Claude in Chrome), perfil casal/2 adultos/0 crianças/1 acomodação, âncoras aprovadas na Rodada 0. Dados completos em `COLETAS_CONCORRENCIA_REVENUE.csv`. **Este é diagnóstico preliminar — nenhuma recomendação de alteração tarifária foi gerada.**

### Concorrentes coletados com sucesso (10 de 10 tentados)
Vila Boa Vida, Vila Maciel, Pousada Kaloa Eco Village, Pousada Riviera Bombinhas, Pousada dos Ingleses, Pousada Dom Capudi, Pousada Kia Ora Bombinhas (núcleo, 7 de 7) + Morada do Guaruça, UP Hotel Boutique (ampliada, 2 de 2) + Hotel/Pousada Atalaia do Mariscal (teto de mercado, 1 de 1).

### Concorrentes com falha
Nenhum.

### Concorrentes indisponíveis
Nenhum — diferença notável em relação à Rodada 1, onde 3 concorrentes (Dom Capudi, Morada do Guaruça e Atalaia do Mariscal) estavam esgotados. Todos os três apareceram disponíveis nesta rodada, com os mesmos valores já vistos na Rodada 0 (09–12/10 é a mesma janela testada naquela rodada).

**Vila dos Açores** não foi tentada nesta rodada (pendente/não usar, por decisão já registrada).

### 1. Média núcleo (n=7 de 7 — amostra completa)

| Métrica | Valor |
|---|---|
| Menor diária Booking | R$ 280,00 (Vila Maciel) |
| Maior diária Booking | R$ 668,67 (Pousada Kia Ora Bombinhas) |
| Média diária Booking | R$ 445,76 |
| Mediana diária Booking | R$ 451,33 (Pousada Dom Capudi) |
| Média motor equivalente (÷1,25) | R$ 356,61 |

### 2. Média ampliada (n=2 de 2 — amostra completa)

| Métrica | Valor |
|---|---|
| Média diária Booking (Morada do Guaruça R$ 611,67 + UP Hotel Boutique R$ 581,33) | R$ 596,50 |
| Média motor equivalente | R$ 477,20 |

### 3. Teto de mercado (n=1 de 1)

| Métrica | Valor |
|---|---|
| Hotel/Pousada Atalaia do Mariscal — diária Booking | R$ 1.600,00 |
| Motor equivalente (referência, não entra em média) | R$ 1.280,00 |

### Villa Arágua no período

| Referência | Valor |
|---|---|
| Base no motor (Organic/Fuego/Metallo, Outubro/2026 feriado, já publicado) | R$ 529,00 |
| Estimada no Booking (motor × 1,25) | R$ 661,25 |

### Posição preliminar da Villa

- **Vs. média núcleo:** R$ 661,25 (Booking) e R$ 529,00 (motor) ficam **acima** da média núcleo em ambas as bases — aproximadamente **+48,3%** (mesma proporção nas duas bases, como esperado pela conversão constante).
- **Vs. média ampliada (n=2, amostra completa):** R$ 661,25 fica **acima** de R$ 596,50 — cerca de **+10,9%**. Diferença maior que a vista na Rodada 1 (+3,4%), mas agora com amostra ampliada completa (2 de 2), não mais 1 de 2.

### Novos indicadores desta rodada

- **`indice_disponibilidade_nucleo`** — 7 de 7 = **100%**.
- **`indice_disponibilidade_total_tentado`** — 10 de 10 (excluindo Vila dos Açores) = **100%**.
- **`sinal_demanda`: `BAIXO`** — nenhum concorrente esgotado em nenhuma categoria (núcleo, ampliada ou teto), o oposto do padrão da Rodada 1 (3 esgotados, sinal `MÉDIO/ALTO`). Sem critério fixo aprovado ainda para converter índice em rótulo — esta leitura é qualitativa, baseada só em "zero esgotamento" vs. "esgotamento observado" entre as duas rodadas.

### Diagnóstico preliminar (sem recomendação automática)

**Classificação preliminar oficial: `MANTER`**

**Motivo:** a diferença da Villa frente à média núcleo (+48,3%) é quase idêntica à da Rodada 1 (+48,7%) — não é um efeito pontual de uma data específica, parece um padrão estrutural entre a base da Villa e o núcleo de concorrentes coletado. Já a diferença frente à média ampliada (a referência de padrão mais próximo do posicionamento da Villa) subiu de +3,4% para +10,9%, agora com amostra completa. Ao mesmo tempo, o sinal de demanda mudou de `MÉDIO/ALTO` (Rodada 1, com esgotamento) para `BAIXO` (Rodada 2, sem nenhum esgotamento) — ou seja, o argumento que sustentava `ESPERAR`/`MANTER` na Rodada 1 (pressão de demanda visível) não está presente desta vez. Isso não é, por si só, motivo para `BAIXAR_COM_JUSTIFICATIVA` — duas rodadas ainda são uma amostra pequena de datas, e o núcleo inclui concorrentes de porte variado (de R$ 280 a R$ 668 de diária). Fica registrado como ponto de atenção para rodadas futuras, não como recomendação.

**Nenhuma ação, ajuste ou recomendação de preço é derivada deste diagnóstico.** Este diagnóstico permanece preliminar em `ALERTAS_CONCORRENCIA_REVENUE.md` e não foi movido para `DECISOES_REVENUE_PENDENTES_VILLA_ARAGUA.md`.

---

## 6. Rodada 3 — Resultado (Pousada Arágua, 30/10–02/11/2026, feriado de Finados)

**Coletado em:** 2026-07-26, via Booking (Claude in Chrome), perfil casal/2 adultos/0 crianças/1 acomodação, âncoras aprovadas na Rodada 0. Dados completos em `COLETAS_CONCORRENCIA_REVENUE.csv`. Diagnóstico gerado via agente `villa-precificacao-calendario`, com consulta às skills `villa-aragua-pricing-revenue` e `villa-aragua-growth-marketer`. **Este é diagnóstico preliminar — nenhuma recomendação de alteração tarifária foi gerada.**

### Concorrentes coletados com sucesso (9 de 10 tentados)
Vila Boa Vida, Vila Maciel, Pousada Kaloa Eco Village, Pousada Riviera Bombinhas, Pousada dos Ingleses, Pousada Dom Capudi (núcleo, 6 de 7) + Morada do Guaruça, UP Hotel Boutique (ampliada, 2 de 2) + Hotel/Pousada Atalaia do Mariscal (teto de mercado, 1 de 1).

### Concorrentes com falha
Nenhum.

### Concorrentes indisponíveis
Pousada Kia Ora Bombinhas (núcleo) — Booking exibiu "Não temos disponibilidade" para todas as categorias no período. É o concorrente núcleo historicamente mais caro (R$ 468–585 motor equiv. nas demais rodadas); sua ausência reduz mecanicamente a média núcleo desta rodada.

**Vila dos Açores** não foi tentada (pendente/não usar, por decisão já registrada).

### 1. Média núcleo (n=6 de 7 — Kia Ora indisponível)

| Métrica | Valor |
|---|---|
| Menor diária Booking | R$ 276,33 (Pousada dos Ingleses) |
| Maior diária Booking | R$ 522,67 (Pousada Riviera Bombinhas) |
| Média diária Booking | R$ 415,22 |
| Mediana diária Booking | R$ 454,50 |
| Média motor equivalente (÷1,25) | R$ 332,18 |

### 2. Média ampliada (n=2 de 2 — amostra completa)

| Métrica | Valor |
|---|---|
| Média diária Booking (Morada do Guaruça R$ 611,67 + UP Hotel Boutique R$ 763,67) | R$ 687,67 |
| Média motor equivalente | R$ 550,13 |

### 3. Teto de mercado (n=1 de 1)

| Métrica | Valor |
|---|---|
| Hotel/Pousada Atalaia do Mariscal — diária Booking | R$ 1.500,00 |
| Motor equivalente (referência, não entra em média) | R$ 1.200,00 |

### Villa Arágua no período

| Referência | Valor |
|---|---|
| Base no motor (Organic/Fuego/Metallo, Outubro/2026 feriado, já publicado) | R$ 529,00 |
| Estimada no Booking (motor × 1,25) | R$ 661,25 |

**Nota de fonte:** o inventário não tem linha própria para "Finados" — usa o mesmo bucket "Outubro/2026 feriado" da Rodada 2 (12 de outubro). Gap a confirmar com Renildo: se Finados (feriado nacional) deveria ter régua distinta do feriado municipal de 12/10, não presumir automaticamente que são o mesmo caso.

### Posição preliminar da Villa

- **Vs. média núcleo:** R$ 661,25 (Booking) fica **acima** da média núcleo — aproximadamente **+59,3%**. Maior gap das rodadas até agora, mas em parte efeito de composição de amostra (ausência do Kia Ora, o núcleo mais caro).
- **Vs. média ampliada (n=2, amostra completa):** R$ 661,25 fica **abaixo** de R$ 687,67 — cerca de **−3,8%**.

### Novos indicadores desta rodada

- **`indice_disponibilidade_nucleo`** — 6 de 7 = **85,7%**.
- **`indice_disponibilidade_total_tentado`** — 9 de 10 (excluindo Vila dos Açores) = **90%**.
- **`sinal_demanda`: `MÉDIO`** — 1 concorrente núcleo esgotado (Kia Ora). Sinal de pressão, mas mais fraco que o da Rodada 4 (ver seção 7).

### Diagnóstico preliminar (sem recomendação automática)

**Classificação preliminar oficial: `MANTER`**

**Motivo:** o gap frente ao núcleo (+59,3%) é o maior das rodadas até agora, mas não é uma leitura confiável de "a Villa se distanciou ainda mais do mercado" — é parcialmente artefato da ausência do Kia Ora (historicamente o núcleo mais caro) na amostra. Frente à ampliada — referência de padrão mais próximo do posicionamento da Villa — a Villa fica levemente abaixo (−3,8%), padrão consistente com rodadas anteriores. O sinal de demanda `MÉDIO` (1 esgotamento) não sustenta `SUBIR_COM_PRIORIDADE`, e a leitura comercial da skill `villa-aragua-growth-marketer` (gap vs. OTA núcleo não é, isoladamente, justificativa de baixa) afasta `BAIXAR_COM_JUSTIFICATIVA`. `MANTER` é a leitura mais honesta com o dado disponível nesta rodada.

**Nenhuma ação, ajuste ou recomendação de preço é derivada deste diagnóstico.** Permanece preliminar nesta seção e não foi movido para `DECISOES_REVENUE_PENDENTES_VILLA_ARAGUA.md`.

---

## 7. Rodada 4 — Resultado (Pousada Arágua, 19–22/11/2026, feriado forte de Consciência Negra)

**Coletado em:** 2026-07-26, via Booking (Claude in Chrome), perfil casal/2 adultos/0 crianças/1 acomodação, âncoras aprovadas na Rodada 0. Dados completos em `COLETAS_CONCORRENCIA_REVENUE.csv`. Diagnóstico gerado via agente `villa-precificacao-calendario`, com consulta às skills `villa-aragua-pricing-revenue` e `villa-aragua-growth-marketer`. **Este é diagnóstico preliminar — nenhuma recomendação de alteração tarifária foi gerada.**

### Concorrentes coletados com sucesso (8 de 10 tentados)
Vila Boa Vida, Vila Maciel, Pousada Kaloa Eco Village, Pousada Riviera Bombinhas, Pousada Kia Ora Bombinhas (núcleo, 5 de 7) + Morada do Guaruça, UP Hotel Boutique (ampliada, 2 de 2) + Hotel/Pousada Atalaia do Mariscal (teto de mercado, 1 de 1).

### Concorrentes com falha
Nenhum.

### Concorrentes indisponíveis (na acomodação-âncora)
Pousada dos Ingleses e Pousada Dom Capudi (núcleo) — em ambos, a acomodação-âncora aprovada não aparecia entre as categorias disponíveis; outras categorias mais caras seguiam à venda, mas não foram usadas por não serem a âncora aprovada. São, historicamente, dois dos concorrentes núcleo mais baratos — sua ausência reduz a amostra núcleo justamente na ponta mais econômica.

**Vila dos Açores** não foi tentada (pendente/não usar, por decisão já registrada).

### 1. Média núcleo (n=5 de 7 — Ingleses e Dom Capudi com âncora esgotada)

| Métrica | Valor |
|---|---|
| Menor diária Booking | R$ 344,00 (Vila Maciel) |
| Maior diária Booking | R$ 756,33 (Pousada Riviera Bombinhas) |
| Média diária Booking | R$ 578,60 |
| Mediana diária Booking | R$ 536,00 |
| Média motor equivalente (÷1,25) | R$ 462,88 |

### 2. Média ampliada (n=2 de 2 — amostra completa)

| Métrica | Valor |
|---|---|
| Média diária Booking (Morada do Guaruça R$ 707,33 + UP Hotel Boutique R$ 659,00) | R$ 683,17 |
| Média motor equivalente | R$ 546,53 |

### 3. Teto de mercado (n=1 de 1)

| Métrica | Valor |
|---|---|
| Hotel/Pousada Atalaia do Mariscal — diária Booking | R$ 1.300,00 |
| Motor equivalente (referência, não entra em média) | R$ 1.040,00 |

Observação: Booking exibia aviso explícito **"6 hotéis 4 estrelas como este já estão indisponíveis no nosso site"** para o período — sinal de escassez regional no segmento de padrão superior, não apenas da Atalaia isoladamente. Dado do próprio Booking, não estimativa.

### Villa Arágua no período

| Referência | Valor |
|---|---|
| Base no motor (Organic/Fuego/Metallo, Novembro/2026 feriado forte 19–21, já publicado) | R$ 717,00 |
| Estimada no Booking (motor × 1,25) | R$ 896,25 |

### Posição preliminar da Villa

- **Vs. média núcleo:** R$ 896,25 (Booking) fica **acima** da média núcleo — aproximadamente **+54,9%**.
- **Vs. média ampliada (n=2, amostra completa):** R$ 896,25 fica **acima** de R$ 683,17 — cerca de **+31,2%**. Diferença bem maior que nas rodadas anteriores frente à ampliada.

### Novos indicadores desta rodada

- **`indice_disponibilidade_nucleo`** — 5 de 7 = **71,4%**.
- **`indice_disponibilidade_total_tentado`** — 8 de 10 (excluindo Vila dos Açores) = **80%**.
- **`sinal_demanda`: `ALTO`** — 2 concorrentes núcleo com âncora esgotada (justamente os mais baratos) + aviso explícito de escassez regional do próprio Booking no segmento de padrão superior. É o sinal de demanda mais forte das quatro rodadas registradas até agora.

### Diagnóstico preliminar (sem recomendação automática)

**Classificação preliminar oficial: `PROTEGER`**

**Motivo:** esta é a rodada com maior sinal de demanda registrado até agora — 2 concorrentes núcleo (os mais baratos) com a âncora esgotada, somado a um aviso de escassez regional do próprio Booking no teto de mercado (dado da plataforma, não estimativa). A tarifa de feriado forte já publicada no inventário (R$ 717,00) combinada com este sinal de demanda alto aponta para proteger o preço, não para reduzir. A Villa fica +54,9% acima do núcleo e +31,2% acima da ampliada — gaps que, isoladamente via OTA, poderiam sugerir baixa, mas a leitura comercial da skill `villa-aragua-growth-marketer` não sustenta isso como justificativa automática, e o sinal de demanda alto reforça o oposto. Registrado à parte, sem virar decisão: o salto de preço da Pousada Riviera Bombinhas nesta rodada (de R$ 418 para R$ 605 motor equiv. frente à Rodada 3) é ponto de atenção para rodadas futuras.

**Nenhuma ação, ajuste ou recomendação de preço é derivada deste diagnóstico.** Permanece preliminar nesta seção e não foi movido para `DECISOES_REVENUE_PENDENTES_VILLA_ARAGUA.md`.

### Pontos de atenção transversais (Rodadas 3 e 4)

- **Kia Ora sumindo/reaparecendo entre rodadas:** esgotado na Rodada 3, disponível na Rodada 4 a R$ 731,67 diária — é o concorrente núcleo historicamente mais caro; sua presença/ausência distorce a média núcleo de forma relevante. Checar sempre se está na amostra antes de interpretar um "gap vs. núcleo" isolado.
- **Riviera com salto de preço na Rodada 4:** de R$ 418,13 para R$ 605,07 motor equiv. — o maior aumento entre rodadas de qualquer concorrente núcleo neste ciclo.
- **Gap Villa vs. inventário publicado (Finados):** ver nota de fonte na Rodada 3 — o inventário usa o mesmo valor de "Outubro/2026 feriado" para Finados; confirmar com Renildo se Finados deveria ter régua própria.
- **Amostra ainda pequena (4 rodadas):** o padrão "Villa bem acima do núcleo, mais próxima da ampliada" se repete nas quatro rodadas — começa a parecer estrutural, mas ainda não é amostra suficiente para virar regra fixa.

---

## 8. Decisão de Renildo — Rodadas 3 e 4 (registro gerencial)

**Renildo visualizou o resumo executivo e o relatório visual das Rodadas 3 e 4 (`RELATORIO_VISUAL_CONCORRENCIA_REVENUE_OUT_NOV_2026.md`) e decidiu manter as tarifas atuais para:**

- **Rodada 3 — Finados (30/10/2026 a 02/11/2026):** tarifa mantida sem alteração.
- **Rodada 4 — Consciência Negra (19/11/2026 a 22/11/2026):** tarifa mantida sem alteração.

**Status: `TARIFARIO_MANTIDO_RENILDO_SEM_ALTERACAO`**

Esta é uma decisão gerencial de Renildo, registrada aqui em `ALERTAS_CONCORRENCIA_REVENUE.md` — **não foi movida para `DECISOES_REVENUE_PENDENTES_VILLA_ARAGUA.md`** (esse arquivo permanece intocado) e **nenhuma tarifa foi alterada** no Stays, Booking, Airbnb ou Decolar. Os diagnósticos preliminares `MANTER` (Rodada 3) e `PROTEGER` (Rodada 4) das seções 6 e 7 permanecem como estavam, agora acompanhados desta confirmação de decisão humana.

---

## 9. Decisão de Renildo — Tarifa Tática Dias Comuns Novembro 2026 (registro gerencial)

**Origem:** após a Rodada 5B (seção do relatório `RELATORIO_VISUAL_CONCORRENCIA_REVENUE_NOV_NORMAL_2026.md`) e a simulação tática de dias de semana (não registrada em arquivo, feita sob demanda de Renildo), **Renildo decidiu e aplicou manualmente no motor** uma tarifa tática reduzida para determinados dias comuns de novembro/2026, Pousada Arágua, unidade base (Organic/Fuego/Metallo) e régua derivada.

**Classificação:** `TARIFA_TATICA_DIAS_DE_SEMANA_APLICADA_RENILDO`

### Valores aplicados no motor

| Acomodação | Valor aplicado |
|---|---|
| Organic / Fuego / Metallo | R$ 475 |
| Terra / Wood | R$ 546 |
| Acqua | R$ 594 |
| Luna | R$ 627 |
| Duplex Soleil | R$ 774 |

### Datas em que Renildo aplicou a tarifa

- 02/11/2026 a 05/11/2026
- 09/11/2026 a 12/11/2026
- 16/11/2026 a 18/11/2026
- 22/11/2026 a 26/11/2026

### Motivo registrado por Renildo

- Rodada 5B mostrou sinal de demanda `BAIXO`;
- 100% dos concorrentes disponíveis nessa rodada (núcleo 7/7, ampliada 2/2, teto 1/1);
- Villa estava +47,8% vs. núcleo e +27,1% vs. ampliada;
- risco real de diária zero em dias comuns de novembro;
- redução aproximada de 10% reduz o gap sem transformar a Villa em opção barata;
- objetivo: melhorar competitividade sem guerra de preço, aproximar da ampliada em baixa demanda, manter a Pousada acima do núcleo, preservar feriados e finais de semana com tarifário protegido.

### Observações de rastreabilidade (diferença entre dado real e decisão gerencial)

- **09/11 a 12/11/2026** — única janela com **dado real completo** do Radar (Rodada 5B: núcleo 7/7, ampliada 2/2, sinal de demanda BAIXO, veredito `ACIMA_DO_MERCADO_COM_RISCO`, diagnóstico preliminar `MANTER` com ponto de atenção). A simulação tática prévia recomendava `REDUZIR_10` especificamente para esta janela — a decisão aplicada por Renildo (motor R$ 475, ≈ −9,7% sobre R$ 526) está alinhada a essa recomendação.
- **02/11 a 05/11/2026** — a simulação prévia havia recomendado `AGUARDAR_DADOS` para a janela equivalente (03/11–05/11), por não haver coleta própria do Radar. Renildo aplicou mesmo assim, com um dia a mais (02/11) do que o simulado, **por decisão gerencial baseada em histórico de menor ocupação em dias comuns de novembro** — não há coleta do Radar sustentando esse período especificamente.
- **16/11 a 18/11/2026** — esta janela havia sido sinalizada na simulação anterior apenas como **candidata a rodada futura de coleta** (pré-véspera do feriado forte de Consciência Negra), sem ter sido simulada nem recomendada. Renildo aplicou por decisão gerencial própria, sem dado do Radar para esse período.
- **22/11 a 26/11/2026** — janela não simulada nem coletada. Início do intervalo é **22/11/2026, um domingo** (dia imediatamente seguinte ao checkout da Rodada 4 / feriado forte de Consciência Negra, 19–22/11) — ou seja, a noite de 22/11 é tecnicamente uma noite de fim de semana dentro de um intervalo tratado como "dias comuns". Registrado aqui apenas como observação factual de calendário, sem correção ou bloqueio — a aplicação foi mantida exatamente como decidida por Renildo.
- **Não aplicado** (confirmado por Renildo): Finados (30/10 a 02/11), finais de semana em geral, feriado de Consciência Negra (19/11 a 22/11), outras datas especiais, dezembro/janeiro/fevereiro. Esses períodos permanecem com o tarifário anterior, protegido.

**Status: `TARIFA_TATICA_DIAS_COMUNS_NOVEMBRO_2026_APLICADA_RENILDO`**

Esta é uma decisão gerencial de Renildo, já aplicada manualmente no motor antes deste registro. Registrada aqui em `ALERTAS_CONCORRENCIA_REVENUE.md` e também como card `DECIDIDO_APLICADO` em `DECISOES_REVENUE_PENDENTES_VILLA_ARAGUA.md`. **A IA não alterou nenhuma tarifa em nenhum sistema real** — este registro apenas documenta o que Renildo já fez, para manter o cérebro Villa Arágua IA sincronizado com a realidade.

---

## 10. Rodada 6 — Resultado (Dezembro Pré-Alta 2026)

**Coletado em:** 2026-07-28, via Booking (Claude in Chrome), perfil casal/2 adultos/0 crianças/1 acomodação, âncoras aprovadas na Rodada 0. Dados completos em `COLETAS_CONCORRENCIA_REVENUE.csv`. Diagnóstico gerado via agente `villa-precificacao-calendario`, com consulta às skills `villa-aragua-pricing-revenue` e `villa-aragua-growth-marketer` — agente acionado de fato. Relatório visual completo em `RELATORIO_VISUAL_CONCORRENCIA_REVENUE_DEZ_PRE_ALTA_2026.md`. **Este é diagnóstico preliminar — nenhuma recomendação de alteração tarifária foi gerada.**

Objetivo: checar o posicionamento da Pousada Arágua no bloco 01–17/12/2026 (pré-alta), com amostra representativa de dias de semana e de fim de semana — não coleta semana a semana, por orientação de Renildo (histórico da região não mostra grande variação dentro desse bloco).

**Villa Arágua no bloco:** motor R$ 629,00 (bucket único "Dezembro/2026 1-18" do inventário) | Booking estimado R$ 786,25.

### Rodada 6A — Dias de semana pré-alta (07/12/2026 a 11/12/2026)

- Núcleo 100% disponível (7 de 7).
- Booking alertou escassez regional ("6 hotéis 4 estrelas já indisponíveis"), mesmo com o núcleo plenamente disponível.
- Villa +49,0% vs. média núcleo.
- Sinal de demanda: `MÉDIO`.
- Veredito de posicionamento: `ACIMA_DO_NUCLEO_MAS_DEFENSAVEL`.
- **Diagnóstico preliminar: `MANTER`.**

**Leitura:** não repetir automaticamente a lógica da tarifa tática de novembro/2026. Apesar de a Villa estar acima do núcleo, aqui há sinal de escassez regional ativo (alerta do próprio Booking) — diferente de novembro, onde o sinal de demanda era `BAIXO` e sem nenhum alerta de escassez. Não há evidência suficiente para redução tática nos dias de semana desta janela.

### Rodada 6B — Final de semana pré-alta (11/12/2026 a 13/12/2026)

- Maior sinal de esgotamento de todo o Radar até agora.
- Núcleo com disponibilidade de 71,4% (5 de 7 — Riviera e Kia Ora esgotados).
- Ampliada zerada (Morada esgotada; UP com restrição de estadia mínima de 3 diárias, incompatível com a busca de 2 noites).
- Teto de mercado esgotado (Atalaia).
- Alerta do Booking escalando: de "6 hotéis 4 estrelas indisponíveis" (Rodada 6A) para "7 hotéis 4 estrelas indisponíveis" em poucos dias.
- Veredito de posicionamento: `POSICIONAMENTO_FORTE_PROTEGER`.
- **Diagnóstico preliminar: `PROTEGER`.**

### Decisão gerencial de Renildo — Rodada 6

**Renildo visualizou o diagnóstico preliminar das Rodadas 6A e 6B e decidiu:**

- Manter as tarifas atuais da pré-alta de dezembro neste momento.
- Não aplicar tarifa tática nos dias de semana de dezembro (diferente da decisão tomada para novembro/2026 — ver seção 9).
- Proteger os finais de semana da pré-alta de dezembro.

**Status: `DIAGNOSTICO_PRELIMINAR_SEM_ALTERACAO_TARIFARIA`**

Esta é uma decisão gerencial de Renildo, registrada aqui em `ALERTAS_CONCORRENCIA_REVENUE.md` — **não foi movida para `DECISOES_REVENUE_PENDENTES_VILLA_ARAGUA.md`** (esse arquivo permanece intocado nesta rodada) e **nenhuma tarifa foi alterada** no Stays, Booking, Airbnb ou Decolar. Os diagnósticos preliminares `MANTER` (Rodada 6A) e `PROTEGER` (Rodada 6B) permanecem registrados acima, agora acompanhados desta confirmação de decisão humana.

---

## 11. Rodada 7/8 — Resultado (Natal e Réveillon 2026/2027)

**Coletado em:** 2026-07-29, via Booking (Claude in Chrome), perfil casal/2 adultos/0 crianças/1 acomodação, âncoras aprovadas na Rodada 0. Dados completos em `COLETAS_CONCORRENCIA_REVENUE.csv`. Diagnóstico gerado via agente `villa-precificacao-calendario`, com consulta às skills `villa-aragua-pricing-revenue` e `villa-aragua-growth-marketer` — agente acionado de fato. Relatório visual completo em `RELATORIO_VISUAL_CONCORRENCIA_REVENUE_NATAL_REVEILLON_2026_2027.md`. **Este é diagnóstico preliminar — nenhuma recomendação de alteração tarifária foi gerada.**

Objetivo: checar o posicionamento da Pousada Arágua para Natal e Réveillon 2026/2027, tratando o período como **pacote** (mínimo de noites, tarifa motor variando dia a dia dentro do pacote) — comparação sempre pacote total contra pacote total e diária média contra diária média, nunca diária isolada contra pacote completo.

### Rodada 7A — Natal, janela 18/12/2026 a 24/12/2026 (6 noites)

- Diária média Villa Booking estimada: R$ 1.057,08.
- Sinal de demanda: `ALTO`.
- Veredito de posicionamento: `PROXIMA_DA_AMPLIADA`.
- **Diagnóstico preliminar: `PROTEGER`.**

### Rodada 7B — Natal, pacote principal 20/12/2026 a 25/12/2026 (5 noites, inclui 24/12)

- Diária média Villa Booking estimada: R$ 1.111,25.
- Sinal de demanda: `ALTO`.
- Veredito de posicionamento: `PROXIMA_DA_AMPLIADA`.
- **Diagnóstico preliminar: `PROTEGER`.**

### Rodada 8A — Réveillon, pacote principal 27/12/2026 a 03/01/2027 (7 noites)

- Diária média Villa Booking estimada: R$ 1.671,25.
- Sinal de demanda: `ALTO`.
- Veredito de posicionamento: `ACIMA_DO_NUCLEO_MAS_DEFENSAVEL`.
- **Diagnóstico preliminar: `PROTEGER`.**

### Rodada 8B — Réveillon, janela completa 25/12/2026 a 03/01/2027 (9 noites)

- Diária média Villa Booking estimada: R$ 1.609,03.
- Sinal de demanda: `ALTO`.
- Veredito de posicionamento: `PROXIMA_DA_AMPLIADA`.
- **Diagnóstico preliminar: `PROTEGER`.**

**Leitura:** as quatro sub-rodadas fecharam com sinal de demanda `ALTO` — o primeiro bloco do Radar em que isso se repete de forma consistente em todas as sub-rodadas. Não aplicar desconto. Não criar tarifa tática. Não repetir a lógica de novembro/2026 (aplicada sobre sinal de demanda `BAIXO` e sem alerta de escassez — cenário oposto ao observado aqui). A análise deve ser lida sempre por pacote total e diária média, nunca por diária isolada.

**Observação estrutural:** a tarifa da Villa está plana dentro dos buckets de Natal e Réveillon — 24/12 e 31/12 não carregam prêmio extra específico sobre as demais noites do respectivo bucket. Registrado como observação para avaliação futura de Renildo, não como recomendação automática de alteração.

### Decisão gerencial de Renildo — Rodada 7/8

**Renildo visualizou o diagnóstico preliminar das Rodadas 7A, 7B, 8A e 8B e decidiu:**

- Manter os valores atuais de Natal e Réveillon neste momento.
- Não aplicar desconto nem tarifa tática nessas datas.
- Monitorar procura direta, WhatsApp, Booking e disponibilidade da concorrência.

**Status: `DIAGNOSTICO_PRELIMINAR_PROTEGER_SEM_ALTERACAO_TARIFARIA`**

Esta é uma decisão gerencial de Renildo, registrada aqui em `ALERTAS_CONCORRENCIA_REVENUE.md` — **não foi movida para `DECISOES_REVENUE_PENDENTES_VILLA_ARAGUA.md`** (esse arquivo permanece intocado nesta rodada) e **nenhuma tarifa foi alterada** no Stays, Booking, Airbnb ou Decolar. Os diagnósticos preliminares `PROTEGER` (Rodadas 7A, 7B, 8A e 8B) permanecem registrados acima, agora acompanhados desta confirmação de decisão humana.

---

## 12. Rodada 9 — Resultado (Janeiro 2027)

**Coletado em:** 2026-07-26, via Booking (Claude in Chrome), perfil casal/2 adultos/0 crianças/1 acomodação, âncoras aprovadas na Rodada 0. Dados completos em `COLETAS_CONCORRENCIA_REVENUE.csv`. Diagnóstico gerado via agente `villa-precificacao-calendario`, com consulta às skills `villa-aragua-pricing-revenue` e `villa-aragua-growth-marketer` — agente acionado de fato. Relatório visual completo em `RELATORIO_VISUAL_CONCORRENCIA_REVENUE_JANEIRO_2027.md`. **Este é diagnóstico preliminar — nenhuma recomendação de alteração tarifária foi gerada.**

Objetivo: separar o posicionamento da Pousada Arágua em janeiro/2027 em três blocos — primeira quinzena (alta procura histórica), semana intermediária e última semana (procura potencialmente mais baixa).

### Bloco 1 — Primeira quinzena, 03/01/2027 a 16/01/2027 (Rodadas 9A e 9B)

- Diária média Villa Booking estimada: R$ 1.361,00.
- Sinal de demanda: `ALTO`.
- **Diagnóstico preliminar: `PROTEGER`.**

**Leitura:** bloco de alta procura e alta ocupação histórica — proteger margem.

### Bloco 2 — Semana intermediária, 17/01/2027 a 23/01/2027 (Rodada 9C)

- Diária média Villa Booking estimada: R$ 1.337,50.
- Sinal de demanda: `MÉDIO`.
- **Diagnóstico preliminar: `MANTER`.**

**Leitura:** manter tarifa atual e monitorar procura.

### Bloco 3 — Última semana, 24/01/2027 a 31/01/2027 (Rodada 9D)

- Diária média Villa Booking estimada: R$ 1.337,50.
- Sinal de demanda: `MÉDIO`, com tendência de queda.
- **Diagnóstico preliminar: `MANTER`, com ponto de atenção.**

**Leitura:** concorrentes reduzem preço nominal ao longo do mês, mas ainda não há sinal `BAIXO` confirmado para justificar tarifa tática.

**Achado central:** o inventário publicado da Villa não fragmenta o bucket "Janeiro/2027 4-31" por semana — a tarifa da Villa permanece igual de 10/01 a 31/01, e toda a diferença de posicionamento entre os três blocos vem do comportamento da concorrência, não de variação própria da Villa.

### Decisão gerencial de Renildo — Rodada 9

**Renildo visualizou o diagnóstico preliminar das Rodadas 9A, 9B, 9C e 9D e decidiu:**

- Manter os valores atuais de janeiro/2027 neste momento.
- Não aplicar a lógica de novembro/2026 (tarifa tática dias comuns) automaticamente em janeiro.
- Não criar tarifa tática agora.
- Reavaliar especialmente a última semana (24–31/01) se houver baixa procura direta, baixa ocupação ou alta disponibilidade dos concorrentes em nova rodada de coleta.

**Status: `DIAGNOSTICO_PRELIMINAR_SEM_ALTERACAO_TARIFARIA`**

Esta é uma decisão gerencial de Renildo, registrada aqui em `ALERTAS_CONCORRENCIA_REVENUE.md` — **não foi movida para `DECISOES_REVENUE_PENDENTES_VILLA_ARAGUA.md`** (esse arquivo permanece intocado nesta rodada) e **nenhuma tarifa foi alterada** no Stays, Booking, Airbnb ou Decolar. Os diagnósticos preliminares `PROTEGER` (Bloco 1) e `MANTER` (Blocos 2 e 3) permanecem registrados acima, agora acompanhados desta confirmação de decisão humana.

---

## 13. Decisão de Renildo — Tarifa Tática Última Semana de Janeiro 2027

**Status:** `TARIFA_TATICA_ULTIMA_SEMANA_JANEIRO_2027_APLICADA_RENILDO`
**Decidido e aplicado por:** Renildo, manualmente, em 2026-07-28.

### Recomendação original (histórico)

Rodada 9D do Radar de Concorrência Revenue (`RELATORIO_VISUAL_CONCORRENCIA_REVENUE_JANEIRO_2027.md`, 24/01–31/01/2027): sinal de demanda `MÉDIO` com tendência de queda, núcleo 100% disponível (7/7), sem aviso de escassez do Booking, veredito `ACIMA_DO_NUCLEO_MAS_DEFENSAVEL`, diagnóstico preliminar `MANTER` com ponto de atenção — o relatório não recomendou redução, por o sinal ser `MÉDIO` e não `BAIXO` confirmado (diferente do precedente de novembro/2026, seção 9). Na leitura visual solicitada em seguida, dois concorrentes núcleo (Vila Maciel e Pousada dos Ingleses) mostraram queda nominal de preço consistente ao longo das 4 sub-rodadas de janeiro, batendo no menor valor do conjunto justamente em 24–31/01. Após visualizar esses dados, Renildo decidiu aplicar uma redução tática por conta própria, antecipando-se a um possível enfraquecimento de demanda ainda não confirmado por dado de ocupação real.

### Decisão aplicada

| Acomodação | Valor decidido (motor) |
|---|---|
| Organic / Fuego / Metallo | R$ 985 |
| Terra / Wood | R$ 1.133 |
| Acqua | R$ 1.231 |
| Luna | R$ 1.300 |
| Duplex Soleil | R$ 1.606 |

**Datas de aplicação:** 24/01/2027 a 31/01/2027 — noites de 24, 25, 26, 27, 28, 29 e 30/01, com check-out em 31/01.

**Redução aproximada:** ~8% sobre o motor base publicado do bucket "Janeiro/2027 4-31" (R$ 1.070 → R$ 985 na base Organic/Fuego/Metallo). Os demais valores seguem a régua percentual já usada em outras decisões (Terra/Wood ≈115%, Acqua ≈125%, Luna ≈132%, Duplex Soleil ≈163% sobre a base).

### Observação

Ajuste cirúrgico e limitado a uma única janela de 7 noites — **não** aplicado à primeira quinzena de janeiro (03–16/01, Rodadas 9A/9B, diagnóstico `PROTEGER`), **não** aplicado à semana intermediária (17–23/01, Rodada 9C, diagnóstico `MANTER`), e **não** altera Natal, Réveillon ou Carnaval. Não deve ser anunciado como promoção — é ajuste tático de motor, não campanha comercial. Esta decisão é gerencial de Renildo, baseada em leitura de tendência de preço da concorrência (Vila Maciel e Pousada dos Ingleses em queda constante) e no objetivo de sair na frente antes de eventual enfraquecimento de demanda, e **não** é uma recomendação automática da IA — o diagnóstico preliminar do Radar para esta janela foi `MANTER`, não `BAIXAR_COM_JUSTIFICATIVA`.

**Status: `TARIFA_TATICA_ULTIMA_SEMANA_JANEIRO_2027_APLICADA_RENILDO`**

Esta é uma decisão gerencial de Renildo, já aplicada manualmente no motor antes deste registro. Registrada aqui em `ALERTAS_CONCORRENCIA_REVENUE.md` e também como card `DECIDIDO_APLICADO` em `DECISOES_REVENUE_PENDENTES_VILLA_ARAGUA.md`. **A IA não alterou nenhuma tarifa em nenhum sistema real** — este registro apenas documenta o que Renildo já fez, para manter o cérebro Villa Arágua IA sincronizado com a realidade.

---

## 14. Decisão de Renildo — Tarifa Tática Final de Fevereiro 2027

**Status:** `TARIFA_TATICA_FINAL_FEVEREIRO_2027_APLICADA_RENILDO`
**Decidido e aplicado por:** Renildo, manualmente, em 2026-07-28.

### Recomendação original (histórico)

Radar de Concorrência Revenue — Fevereiro 2027 fora do Carnaval (`RELATORIO_VISUAL_CONCORRENCIA_REVENUE_FEVEREIRO_2027_POS_CARNAVAL.md`). A análise mais crítica veio da **Rodada 11D (24/02–28/02/2027)**: sinal de demanda `MISTO/CONTRADITÓRIO` (Vila Maciel, Pousada dos Ingleses e UP Hotel Boutique caíram para os menores preços de toda a série, mas o teto de mercado Atalaia ficou 100% esgotado — sinal inédito em toda a série do Radar), veredito `ACIMA_DO_MERCADO_COM_RISCO`, diagnóstico preliminar `MANTER com ponto de atenção forte`. O relatório **não** recomendou redução nem simulou cenário — o critério para simulação exigia sinal `BAIXO` confirmado (como em novembro/2026), e o sinal aqui era contraditório, não baixo. Após visualizar esse diagnóstico, Renildo decidiu agir com antecedência.

### Decisão aplicada

| Acomodação | Valor decidido (motor) |
|---|---|
| Organic / Fuego / Metallo | R$ 756 |
| Terra / Wood | R$ 869 |
| Acqua | R$ 945 |
| Luna | R$ 998 |
| Duplex Soleil | R$ 1.232 |

**Datas de aplicação:** 21/02/2027 a 28/02/2027 — noites de 21, 22, 23, 24, 25, 26 e 27/02, com check-out em 28/02.

**Redução aproximada:** ~8% sobre o motor base publicado do bucket "Fevereiro/2027 base" (R$ 822 → R$ 756 na base Organic/Fuego/Metallo). Os demais valores seguem a régua percentual já usada em outras decisões (Terra/Wood ≈115%, Acqua ≈125%, Luna ≈132%, Duplex Soleil ≈163% sobre a base).

### Observação de rastreabilidade

A análise mais crítica que motivou esta decisão veio especificamente da **Rodada 11D (24/02 a 28/02)**. Por decisão gerencial, Renildo aplicou a tarifa tática em um intervalo maior — **21/02 a 28/02** — que também alcança parte da **Rodada 11C (17/02 a 24/02)**, cujo diagnóstico preliminar era `MANTER com ponto de atenção`, sinal `MÉDIO` amolecendo (não o mesmo sinal contraditório da 11D). Este registro não bloqueia nem corrige a decisão de Renildo — apenas documenta o fato de que parte do intervalo aplicado (21–23/02) corresponde a uma janela com diagnóstico mais brando do que a que motivou a decisão.

Confirmado que esta redução **não** foi aplicada ao Carnaval (Rodada 10, Card 2, `PROTEGER`), **não** ao pré-Carnaval (Rodada 11A, `PROTEGER`), **não** ao restante de fevereiro fora do intervalo 21–28/02, e **não** se estende automaticamente a março. Não deve ser anunciada como promoção — é ajuste tático de motor, cirúrgico e limitado a esta janela, aplicado manualmente por Renildo, não recomendação automática da IA (o diagnóstico do Radar para a 11D foi `MANTER`, não `BAIXAR_COM_JUSTIFICATIVA`).

**Status: `TARIFA_TATICA_FINAL_FEVEREIRO_2027_APLICADA_RENILDO`**

Esta é uma decisão gerencial de Renildo, já aplicada manualmente no motor antes deste registro. Registrada aqui em `ALERTAS_CONCORRENCIA_REVENUE.md` e também como card `DECIDIDO_APLICADO` em `DECISOES_REVENUE_PENDENTES_VILLA_ARAGUA.md`. **A IA não alterou nenhuma tarifa em nenhum sistema real** — este registro apenas documenta o que Renildo já fez, para manter o cérebro Villa Arágua IA sincronizado com a realidade.

---

## 15. Rodada 12 — Resultado (Março 2027)

**Coletado em:** 2026-07-29, via Booking (Claude in Chrome), perfil casal/2 adultos/0 crianças/1 acomodação, âncoras aprovadas na Rodada 0. Dados completos em `COLETAS_CONCORRENCIA_REVENUE.csv`. Diagnóstico gerado via agente `villa-precificacao-calendario`, com consulta às skills `villa-aragua-pricing-revenue` e `villa-aragua-growth-marketer` — agente acionado de fato. Relatório visual completo em `RELATORIO_VISUAL_CONCORRENCIA_REVENUE_MARCO_2027.md`. **Este é diagnóstico preliminar — nenhuma recomendação de alteração tarifária foi gerada.**

Objetivo: separar o posicionamento da Pousada Arágua em março/2027 em três blocos — primeira quinzena, segunda quinzena e pré-Páscoa (sem misturar com a Páscoa 2027, que será analisada em rodada separada).

### Rodada 12A — Primeira quinzena, 01/03/2027 a 08/03/2027

- Núcleo disponível: 6/7.
- Sinal de demanda: `MÉDIO`.
- Veredito de posicionamento: `ACIMA_DO_NUCLEO_MAS_DEFENSAVEL`.
- **Diagnóstico preliminar: `MANTER`.**

### Rodada 12B — Segunda quinzena, 15/03/2027 a 22/03/2027

- Núcleo disponível: 4/7 — pior disponibilidade de toda a série de março.
- Sinal de demanda: `MÉDIO/contraditório`.
- Veredito de posicionamento: `ACIMA_DO_NUCLEO_MAS_DEFENSAVEL`.
- **Diagnóstico preliminar: `MANTER`, com atenção.**

**Observação:** a disponibilidade núcleo caiu, mas os preços nominais dos concorrentes também caíram na mesma janela — sinal contraditório, não uma queda de demanda confirmada. Recomenda-se nova coleta específica de 15/03 a 22/03 em atualização futura antes de qualquer ajuste tarifário.

### Rodada 12C — Pré-Páscoa, 22/03/2027 a 26/03/2027

- Núcleo disponível: 5/7.
- Sinal de demanda: `MÉDIO`, com tendência de aquecimento.
- Veredito de posicionamento: `PROXIMA_DA_AMPLIADA`.
- **Diagnóstico preliminar: `PROTEGER`.**

**Observação:** Vila Maciel, Pousada dos Ingleses e UP Hotel Boutique subiram de preço frente à Rodada 12B, e o gap da Villa contra a referência ampliada caiu para apenas 5,5% — o mais estreito de toda a série de março. Isso justifica a proteção, por ser antessala direta da Páscoa 2027 (já decidida, Card 1 em `DECISOES_REVENUE_PENDENTES_VILLA_ARAGUA.md`).

### Decisão gerencial de Renildo — Rodada 12

**Renildo visualizou o diagnóstico preliminar das Rodadas 12A, 12B e 12C e decidiu:**

- Manter as tarifas atuais de março/2027 neste momento.
- Não aplicar tarifa tática em março agora.
- Não repetir automaticamente a lógica aplicada em novembro/2026, janeiro/2027 ou fevereiro/2027.
- Recoletar especificamente a janela de 15/03 a 22/03 em atualização futura.
- Proteger o bloco de 22/03 a 26/03, por ser antessala da Páscoa.

**Status: `MARCO_2027_MANTIDO_COM_ATENCAO_12B_E_PROTECAO_PRE_PASCOA`**

Esta é uma decisão gerencial de Renildo, registrada aqui em `ALERTAS_CONCORRENCIA_REVENUE.md` — **não foi movida para `DECISOES_REVENUE_PENDENTES_VILLA_ARAGUA.md`** (esse arquivo permanece intocado nesta rodada) e **nenhuma tarifa foi alterada** no Stays, Booking, Airbnb ou Decolar. Os diagnósticos preliminares `MANTER` (Blocos 12A e 12B) e `PROTEGER` (Bloco 12C) permanecem registrados acima, agora acompanhados desta confirmação de decisão humana.

---

## 16. Decisão de Renildo — Correção Tarifária Março 2027 + Páscoa 2027

**Contexto:** após a Rodada 13 — Páscoa 2027 (`RELATORIO_VISUAL_CONCORRENCIA_REVENUE_PASCOA_2027.md`), Renildo visualizou a tabela aberta de concorrentes e decidiu corrigir a base da Páscoa para ficar mais parelha com a Pousada Kia Ora — o concorrente núcleo mais caro coletado na rodada (motor equivalente médio R$ 441,07/diária). Ao corrigir a Páscoa, Renildo percebeu um problema de coerência: março comum estava com base R$ 607, e a Páscoa corrigida (R$ 529) ficaria **abaixo** de março comum, o que inverteria a lógica de um feriado forte ser mais barato que um mês comum. Por isso, decidiu aplicar a mesma base corrigida (R$ 529) também a março comum, resolvendo os dois pontos com um único ajuste de régua.

### Recomendação original (histórico)

Rodada 13 (`RELATORIO_VISUAL_CONCORRENCIA_REVENUE_PASCOA_2027.md`): veredito de posicionamento `ACIMA_DO_MERCADO_COM_RISCO`, diagnóstico preliminar `ESPERAR`, sinal de demanda `MÉDIO` com grau de confiança `BAIXO`. O relatório **não** recomendou correção nem simulou redução como decisão — apresentou apenas uma mesa de cenários de referência a pedido de Renildo (manter, −5%, −8%, −10%, −15%, −20%), sem indicar qual aplicar. A régua anterior da Villa (R$ 717) estava ≈62,6% acima da Kia Ora; o relatório também apontou que março comum (Rodada 12, base R$ 607) havia sido diagnosticado `MANTER`/`PROTEGER` nos três blocos, sem sinal de demanda `BAIXO` confirmado.

### Decisão aplicada

| Acomodação | Valor decidido (motor) |
|---|---|
| Organic / Fuego / Metallo | R$ 529 |
| Terra / Wood | R$ 608 |
| Acqua | R$ 661 |
| Luna | R$ 698 |
| Duplex Soleil | R$ 862 |

**Períodos de aplicação:**
- **Março comum:** 01/03/2027 a 26/03/2027 (noites de 01 a 25/03, check-out em 26/03).
- **Páscoa 2027:** 26/03/2027 a 29/03/2027 (noites de 26, 27 e 28/03, check-out em 29/03). Mínimo de 3 diárias mantido, sem alteração.

**Observação — cálculo de referência da correção da Páscoa:** a nova base (R$ 529) fica ≈20% acima do motor equivalente médio da Kia Ora (R$ 441,07) — R$ 529 ÷ R$ 441,07 ≈ 1,199×. Isso reduz o gap anterior de ≈62,6% para ≈20%, aproximando a Villa do concorrente núcleo mais caro coletado, mantendo posicionamento premium sem ficar tão descolada do mercado.

**Observação — coerência com março comum:** a extensão da mesma base a março comum não decorre de sinal de demanda `BAIXO` confirmado em março (Rodada 12 mostrou `MANTER`/`PROTEGER`, nunca `BAIXO`) — é uma correção de coerência tarifária, para que março comum não fique mais caro que a Páscoa corrigida. Não deve ser lida nem comunicada como liquidação ou promoção.

### Observações de rastreabilidade

- Esta correção **não** se aplica automaticamente a abril — qualquer extensão a abril exige nova decisão explícita.
- Esta correção **não** altera janeiro, fevereiro, Carnaval, Natal ou Réveillon — os Cards 5, 6 e 7 e a decisão do Carnaval (Card 2) permanecem como estavam, sem qualquer relação com este ajuste.
- Não deve ser anunciada como promoção pública — é correção de régua e coerência de posicionamento, aplicada manualmente por Renildo.
- O mínimo de noites não foi alterado em nenhum dos dois períodos, exceto a manutenção do mínimo de 3 diárias já vigente na Páscoa.
- A correção da Páscoa parte de uma leitura de mercado (Rodada 13, gap vs. Kia Ora); a correção de março comum parte de uma lógica de coerência interna (Páscoa não pode ficar mais barata que o mês comum que a envolve), não de nova coleta ou sinal de demanda confirmado em março.
- Esta é uma decisão gerencial de Renildo — não é recomendação automática da IA. O diagnóstico do Radar para a Páscoa foi `ESPERAR`, não `BAIXAR_COM_JUSTIFICATIVA`; e o diagnóstico para março (Rodada 12) foi `MANTER`/`PROTEGER`, não `BAIXAR_COM_JUSTIFICATIVA`.

**Status: `CORRECAO_TARIFARIA_MARCO_E_PASCOA_2027_APLICADA_RENILDO`**

Classificações específicas: `CORRECAO_TARIFARIA_MARCO_2027_APLICADA_RENILDO` (março comum) e `TARIFA_CORRIGIDA_PASCOA_2027_APLICADA_RENILDO` (Páscoa).

Esta é uma decisão gerencial de Renildo, já aplicada manualmente no motor de reservas antes deste registro. Registrada aqui em `ALERTAS_CONCORRENCIA_REVENUE.md` e também como card `DECIDIDO_APLICADO` em `DECISOES_REVENUE_PENDENTES_VILLA_ARAGUA.md`. **A IA não alterou nenhuma tarifa em nenhum sistema real** — este registro apenas documenta o que Renildo já fez, para manter o cérebro Villa Arágua IA sincronizado com a realidade.

---

## 17. Rodada 14 — Resultado (Abril 2027)

**Coletado em:** 2026-07-29, via Booking (Claude in Chrome), perfil casal/2 adultos/0 crianças/1 acomodação, âncoras aprovadas na Rodada 0. Dados completos em `COLETAS_CONCORRENCIA_REVENUE.csv`. Diagnóstico gerado via agente `villa-precificacao-calendario`, com consulta à skill `villa-aragua-pricing-revenue` — agente acionado de fato. Relatório visual completo em `RELATORIO_VISUAL_CONCORRENCIA_REVENUE_ABRIL_2027.md`. **Este é diagnóstico preliminar — nenhuma recomendação de alteração tarifária foi gerada.**

Objetivo: formato enxuto, com apenas duas amostras representativas — dias de semana e final de semana — para testar a hipótese de Renildo de que abril pode funcionar melhor com dois buckets de preço.

### Rodada 14A — Dias de semana, 19/04/2027 a 23/04/2027 (4 noites)

- Inclui Tiradentes (21/04, quarta-feira), tratado como dia comum — não como feriado forte.
- Núcleo disponível: 71,4% (5/7).
- Villa base: R$ 499/diária (bucket "Abril/2027" uniforme).
- Villa +49,8% acima da média motor equivalente núcleo.
- Villa apenas +13,8% acima do concorrente núcleo mais caro coletado (Kia Ora).
- Sinal de demanda: `MÉDIO`, confiança `MÉDIA`.
- Veredito de posicionamento: `ACIMA_DO_NUCLEO_MAS_DEFENSAVEL`.
- **Diagnóstico preliminar: `MANTER`.**

### Rodada 14B — Final de semana, 23/04/2027 a 25/04/2027 (2 noites)

- Núcleo disponível caiu para 42,9% (3/7).
- Kia Ora e Pousada Riviera Bombinhas — os dois concorrentes mais caros coletados na 14A — ficaram indisponíveis nesta amostra (`INDISPONIVEL_NAO_CONCLUSIVO`, não contam como sinal forte).
- Sinal de demanda: `MÉDIO`, confiança `BAIXA`.
- Veredito de posicionamento: `POSICIONAMENTO_INDEFINIDO_AGUARDAR_DADOS`.
- **Diagnóstico preliminar: `COMPARAR_MELHOR`.**

**Observação metodológica:** a queda do preço médio núcleo entre 14A e 14B parece ser artefato de composição amostral (os dois concorrentes mais caros saíram da amostra por indisponibilidade), não um sinal real de tarifa de fim de semana mais baixa. O dado confiável desta comparação é o índice de disponibilidade (71,4% → 42,9%), não a média de preço.

### Leitura da hipótese dos dois buckets

A hipótese de Renildo — dias de semana mais competitivos, finais de semana com tarifa mais preservada — ficou **parcialmente sustentada** pela disponibilidade menor no fim de semana, mas **ainda não confirmada por preço**, dado o viés de amostra da 14B. Antes de criar um bucket de final de semana mais alto, recomenda-se nova coleta específica de fim de semana em abril, capturando novamente Kia Ora e Riviera.

### Leitura de Tiradentes

Os dados coletados não contradizem tratar Tiradentes como dia comum (posição de Renildo) — não houve aviso de esgotamento amplo nem tarifa isolada de feriado visível. Mas a confiança é baixa, porque a coleta foi feita para o bloco inteiro de 4 noites (19–23/04), sem isolar a diária de 21/04 — o desenho da coleta não tem poder de detectar um pico isolado de uma única data, mesmo que ele exista.

### Decisão gerencial de Renildo — Rodada 14

**Renildo visualizou o diagnóstico preliminar das Rodadas 14A e 14B e decidiu:**

- Manter as tarifas atuais de abril/2027 neste momento.
- Manter a régua de dias de semana como está.
- Comparar melhor os finais de semana (nova coleta específica) antes de considerar subir a tarifa desse bucket.
- Não tratar Tiradentes como feriado forte sem novo sinal de mercado que justifique a mudança.

**Status: `ABRIL_2027_MANTER_DIAS_DE_SEMANA_COMPARAR_MELHOR_FINAIS_DE_SEMANA`**

Esta é uma decisão gerencial de Renildo, registrada aqui em `ALERTAS_CONCORRENCIA_REVENUE.md` — **não foi movida para `DECISOES_REVENUE_PENDENTES_VILLA_ARAGUA.md`** (esse arquivo permanece intocado nesta rodada) e **nenhuma tarifa foi alterada** no Stays, Booking, Airbnb ou Decolar. Os diagnósticos preliminares `MANTER` (Bloco 14A) e `COMPARAR_MELHOR` (Bloco 14B) permanecem registrados acima, agora acompanhados desta confirmação de decisão humana. Nenhuma simulação foi criada nesta rodada.
