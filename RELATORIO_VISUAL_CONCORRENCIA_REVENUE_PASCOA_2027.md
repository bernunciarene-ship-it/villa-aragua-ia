# Radar de Concorrência Revenue — Páscoa 2027 (Pousada Arágua)

**Rodada 13.** Check-in 26/03/2027, check-out 29/03/2027 — 3 noites (26, 27 e 28/03). Canal: Booking. Perfil: casal, 2 adultos, 0 crianças, 1 acomodação. Pacote mínimo: 3 diárias.

**Status do relatório:** `RELATORIO_ANALITICO_SEM_ALTERACAO_TARIFARIA`. Nenhuma tarifa foi alterada. Nenhuma decisão foi criada automaticamente. Nada foi movido para `DECISOES_REVENUE_PENDENTES_VILLA_ARAGUA.md`. A tarifa da Villa para a Páscoa já está decidida e aplicada por Renildo (Card 1, `DECIDIDO_APLICADO`, 2026-07-25) — este relatório apenas lê essa decisão contra os dados de mercado agora coletados.

## Confirmação de governança

- Agente `villa-precificacao-calendario` acionado: **SIM** (invocação real nesta sessão, não simulada).
- Skill `villa-aragua-pricing-revenue` consultada pelo agente: **SIM**.
- Skill `villa-aragua-growth-marketer` consultada pelo agente: não foi necessária para este diagnóstico de precificação (não houve consulta de marketing/campanhas nesta rodada).
- Arquivos consultados: `CESTA_COMPETITIVA_REVENUE_VILLA_ARAGUA.md`, `COLETAS_CONCORRENCIA_REVENUE.csv`, `REGRAS_CONVERSAO_OTA_MOTOR_REVENUE.md`, `DECISOES_REVENUE_PENDENTES_VILLA_ARAGUA.md` (Card 1), relatórios visuais anteriores (Janeiro/Fevereiro/Março 2027) como referência de formato.
- Regras aplicadas: conversão Booking→motor (÷1,25), separação NÚCLEO/AMPLIADA/TETO_MERCADO/PENDENTE, uso exclusivo de preços públicos (sem login, sem clicar em reservar), comparação pacote-total vs. pacote-total (nunca diária isolada vs. pacote completo), e a nova classificação de indisponibilidade em 6 categorias (ver seção dedicada abaixo).

---

## 1. Tabela aberta — Concorrentes

| Grupo | Concorrente | Acomodação âncora | Status | Classificação da indisponibilidade | Preço total Booking (3 diárias) | Diária média Booking | Motor equivalente médio | Dif. R$ vs. Villa motor* | Dif. % vs. Villa motor* | Observação |
|---|---|---|---|---|---|---|---|---|---|---|
| NÚCLEO | Vila Boa Vida | Quarto Duplo Standard | Indisponível | `DATAS_PODEM_NAO_ESTAR_ABERTAS` | — | — | — | — | — | Sem datas alternativas nem aviso regional; Renildo alertou que este concorrente pode abrir tarifas mais perto da data. Não conta como sinal de demanda. |
| NÚCLEO | Vila Maciel | Apartamento Standard | Coletado | `COLETADO_COM_SUCESSO` | R$ 1.102,00 | R$ 367,33 | R$ 293,87 | −R$ 423,13 | −59,0% | "Temos só mais 2." |
| NÚCLEO | Pousada Kaloa Eco Village | Suíte Standard | Coletado | `COLETADO_COM_SUCESSO` | R$ 1.484,00 | R$ 494,67 | R$ 395,73 | −R$ 321,27 | −44,8% | Única tarifa exibida para 2 adultos. |
| NÚCLEO | Pousada Riviera Bombinhas | Suíte Loft Riviera | Indisponível | `INDISPONIVEL_NAO_CONCLUSIVO` | — | — | — | — | — | Sem datas alternativas nem aviso regional. Sem evidência conclusiva de esgotamento real. |
| NÚCLEO | Pousada dos Ingleses | Quarto Duplo Clássico | Coletado | `COLETADO_COM_SUCESSO` | R$ 1.166,00 (R$1.046 + R$120 taxas) | R$ 388,67 | R$ 310,93 | −R$ 406,07 | −56,6% | "Temos só mais 1." |
| NÚCLEO | Pousada Dom Capudi | Quarto Duplo | Coletado | `COLETADO_COM_SUCESSO` | R$ 1.368,00 | R$ 456,00 | R$ 364,80 | −R$ 352,20 | −49,1% | "Temos só mais 1." |
| NÚCLEO | Pousada Kia Ora Bombinhas | Quarto Duplo Deluxe c/ Vista Lateral do Mar | Coletado | `COLETADO_COM_SUCESSO` | R$ 1.654,00 | R$ 551,33 | R$ 441,07 | −R$ 275,93 | −38,5% | "Temos só mais 1." |
| AMPLIADA | Morada do Guaruça | Apartamento de 1 Quarto | Indisponível (real) | `ESGOTADO_CONFIRMADO` | — | — | — | — | — | Calendário comprovadamente aberto (datas alternativas com preço real 1–9/abr) — esgotamento real só para 26-29/03. |
| AMPLIADA | UP Hotel Boutique | Quarto Duplo Deluxe c/ Banheira | Indisponível (real) | `ESGOTADO_CONFIRMADO` | — | — | — | — | — | Aviso explícito do próprio Booking: "5 cama e café (b&bs) como este já estão indisponíveis". |
| TETO_MERCADO | Hotel/Pousada Atalaia do Mariscal | Suíte Superior | Indisponível | `INDISPONIVEL_NAO_CONCLUSIVO` | — | — | — | — | — | Sem datas alternativas nem aviso regional nesta página. Referência apenas, não entra em média. |
| PENDENTE | Vila dos Açores | — | Não coletado | — | — | — | — | — | — | Mantido pendente por decisão prévia de Renildo. Não usado em nenhuma média. |

*Diferença calculada contra a régua motor da Villa Organic/Fuego/Metallo (R$ 717,00/diária). Valores negativos = concorrente abaixo da Villa.

**Índice de disponibilidade núcleo:** 5/7 = **71,4%**. **Índice de disponibilidade total** (núcleo + ampliada + teto, excluindo pendente): 5/10 = **50,0%**.

---

## 2. Tabela — Villa Arágua (Pousada Arágua, pacote 3 diárias)

| Acomodação | Valor motor/diária | Total motor do pacote | Diária média motor | Total Booking estimado (×1,25) | Diária média Booking estimada | Mínimo de noites | Observação |
|---|---|---|---|---|---|---|---|
| Organic / Fuego / Metallo | R$ 717,00 | R$ 2.151,00 | R$ 717,00 | R$ 2.688,75 | R$ 896,25 | 3 | Card 1, `DECIDIDO_APLICADO`. |
| Terra / Wood | R$ 825,00 | R$ 2.475,00 | R$ 825,00 | R$ 3.093,75 | R$ 1.031,25 | 3 | Card 1, `DECIDIDO_APLICADO`. |
| Acqua | R$ 896,00 | R$ 2.688,00 | R$ 896,00 | R$ 3.360,00 | R$ 1.120,00 | 3 | Card 1, `DECIDIDO_APLICADO`. |
| Luna | R$ 946,00 | R$ 2.838,00 | R$ 946,00 | R$ 3.547,50 | R$ 1.182,50 | 3 | Card 1, `DECIDIDO_APLICADO`. |
| Duplex Soleil | R$ 1.169,00 | R$ 3.507,00 | R$ 1.169,00 | R$ 4.383,75 | R$ 1.461,25 | 3 | Card 1, `DECIDIDO_APLICADO`. |

Mínimo de 3 diárias coerente com o pacote de Páscoa especificado. Nenhum valor `DADO_NAO_ENCONTRADO`.

---

## 3. Resumo executivo

- **Média núcleo Booking (5 coletados):** R$ 1.354,80/pacote.
- **Mediana núcleo Booking:** R$ 1.368,00/pacote (Dom Capudi).
- **Média motor equivalente núcleo:** R$ 361,28/diária.
- **Média ampliada Booking:** não calculável — os 2 concorrentes ampliados (Morada do Guaruça, UP Hotel Boutique) estão com `ESGOTADO_CONFIRMADO`, sem preço coletável nesta rodada.
- **Referência de teto:** não calculável nesta rodada — Atalaia do Mariscal indisponível (`INDISPONIVEL_NAO_CONCLUSIVO`), sem preço coletável.
- **Índice de disponibilidade núcleo:** 71,4% (5/7).
- **Índice de disponibilidade total:** 50,0% (5/10, excluindo pendente).
- **Sinal de demanda: MÉDIO.** Dois esgotamentos confirmados na faixa ampliada e mensagens de escassez ("só mais 1/2") em 3 dos 5 núcleo disponíveis indicam alguma pressão de demanda, mas a disponibilidade núcleo em 71,4% ainda é alta para um feriado forte a 8 meses de distância — não sustenta uma leitura de ALTO.
- **Grau de confiança do sinal de demanda: BAIXO.** A amostra ampliada é pequena (apenas 2 concorrentes, ambos esgotados, sem meio-termo para calibrar); mensagens "só mais X" são prática padrão de exibição de escassez em OTAs, não estoque real auditável; Vila Boa Vida (núcleo) ficou de fora da leitura por alerta específico de Renildo; não há referência de teto nesta rodada; e a data ainda está distante o suficiente para o cenário mudar de forma relevante.

---

## 4. Veredito de posicionamento

**`ACIMA_DO_MERCADO_COM_RISCO`** (para Organic/Fuego/Metallo e Terra/Wood).

A régua motor da Villa (R$ 717,00/diária para Organic/Fuego/Metallo) está aproximadamente **1,98× acima** da média motor equivalente do núcleo coletado (R$ 361,28/diária) — um gap muito maior do que o observado nas rodadas anteriores (Janeiro, Fevereiro, Março 2027), em que a Villa costumava estar alinhada ou próxima do núcleo. Comparando pacote total vs. pacote total, o valor Booking estimado da Villa (R$ 2.688,75) supera todos os 5 concorrentes núcleo coletados, com folga de 38,5% a 59,0%.

Não se trata de um veredito de "preço errado" — é o reconhecimento de que o gap é grande demais para ser chamado de "defensável" sem reserva, especialmente porque esta rodada não tem dado de teto nem de ampliada com preço para sustentar uma leitura de "próxima do teto premium". A decisão original de Renildo (Card 1) corrigiu um erro de régua identificado internamente (tarifa de Páscoa abaixo do mês base) — não foi ancorada em benchmarking de concorrência. Este é o primeiro momento em que esse benchmarking é feito, e ele revela um posicionamento bem acima do núcleo.

---

## 5. Diagnóstico preliminar

**`ESPERAR`**

Não é leitura de "manter porque está correto" nem de "corrigir porque está errado" — é reconhecimento de que: (a) a tarifa já foi decidida e aplicada por Renildo (Card 1, `DECIDIDO_APLICADO`); (b) esta rodada é apenas diagnóstica; (c) o período ainda está a 8 meses de distância; e (d) o grau de confiança do sinal de demanda é BAIXO. `MANTER` seria inadequado por implicar uma leitura de "bem posicionada frente ao mercado coletado", o que o gap de quase 2× não sustenta. `BAIXAR_COM_JUSTIFICATIVA` seria prematuro dado o contexto de feriado forte e a possibilidade real de Vila Boa Vida (e Vila dos Açores) ainda abrirem tarifas mais competitivas perto da data — o que mudaria a leitura de posicionamento.

---

## 6. Leitura específica da Páscoa 2027

1. **A Villa está bem posicionada para a Páscoa?** Está posicionada em um patamar de preço bem acima da média núcleo coletada — não é uma leitura simples de "sim" ou "não"; depende de quanto do gap é justificável por marca/experiência e quanto é risco.
2. **O pacote de 3 diárias é competitivo?** Em disponibilidade, sim — a Villa segue vendendo enquanto 2 dos 7 núcleo já não têm vaga (ainda que de forma não conclusiva) e ambos os ampliados esgotaram de fato. Em preço, não é um pacote "competitivo" no sentido de barato — é um pacote de posicionamento elevado dentro do grupo.
3. **O valor total é defensável?** Parcialmente. É defensável pelo contexto de feriado forte e por a faixa ampliada (categoria acima do núcleo) estar esgotada. Mas não há evidência de mercado desta rodada que confirme isso de forma robusta — a confiança do sinal é baixa.
4. **Há risco de estar barato demais?** Não. O risco é o oposto — a Villa está acima, não abaixo, do núcleo coletado.
5. **Há risco de estar caro demais?** Sim, existe risco relevante a monitorar (não a agir agora). O gap de quase 2× é bem maior que o observado em Janeiro/Fevereiro/Março, e a régua de Páscoa nunca foi ancorada em benchmarking de concorrência — foi uma correção de erro interno de régua.
6. **O sinal de demanda é confiável ou distorcido por datas não abertas?** Parcialmente confiável. O sinal não depende das indisponibilidades ambíguas (Vila Boa Vida, Riviera, Atalaia) — ele se apoia nos 5 núcleo efetivamente coletados (com estoque baixo em 3 deles) e nos 2 esgotamentos confirmados da ampliada. Ainda assim, a amostra ampliada é pequena e a data está distante, o que mantém o grau de confiança em BAIXO.
7. **Algum concorrente valida um preço mais alto?** Kia Ora é o núcleo mais caro coletado (R$ 1.654,00/pacote, motor equiv. R$ 441,07/diária), mas ainda fica 38,5% abaixo da régua motor da Villa.
8. **Algum concorrente puxa a média para baixo de forma pouco comparável?** Vila Maciel (R$ 1.102,00/pacote) é o mais barato do núcleo coletado — categoria "Apartamento Standard" com nota de qualidade Booking 3/5, produto mais simples que a régua da Villa. Não é incomparável a ponto de ser descartado, mas contribui para puxar a média núcleo para baixo.
9. **Melhor caminho — manter/proteger/subir/baixar/esperar/comparar melhor?** **Esperar.** Reavaliar com nova coleta mais perto da data, com atenção especial para Vila Boa Vida e Vila dos Açores, que podem abrir tarifas e mudar a leitura de posicionamento.

---

## 7. Cuidado: indisponível não é sempre esgotado

Esta rodada introduziu, pela primeira vez no Radar, uma classificação obrigatória de 6 categorias para toda indisponibilidade coletada — justamente porque Renildo alertou que nem toda "indisponível" no Booking significa esgotamento real, especialmente para Vila Boa Vida e Vila dos Açores, concorrentes que podem abrir datas/tarifas mais perto do check-in.

**Concorrentes que ficaram indisponíveis nesta rodada, e como foram lidos:**

- **Vila Boa Vida** (núcleo) — todas as 5 categorias mostraram "Não disponível no nosso site para as suas datas", sem seção de datas alternativas e sem aviso de esgotamento regional. Como Renildo alertou especificamente sobre este concorrente, a leitura aplicada foi `DATAS_PODEM_NAO_ESTAR_ABERTAS` — ou seja, a ausência de disponibilidade a 8 meses de uma data de Páscoa provavelmente reflete um calendário ainda não aberto para esse período, não uma pousada pequena genuinamente esgotada com quase um ano de antecedência. **Não contou como sinal de demanda.**
- **Pousada Riviera Bombinhas** (núcleo) — mesmo padrão: todas as 3 categorias indisponíveis, sem datas alternativas, sem aviso regional. Sem alerta prévio específico sobre este concorrente, mas aplicando o mesmo cuidado metodológico (distância de 8 meses, ausência de qualquer evidência de calendário aberto), a leitura foi `INDISPONIVEL_NAO_CONCLUSIVO`. **Não contou como sinal de demanda.**
- **Morada do Guaruça** (ampliada) — aqui o padrão foi oposto e muito mais forte: a página mostrou que o calendário está comprovadamente aberto e funcionando (seção "Datas alternativas" com preços reais para 1 a 9 de abril), só não havia vaga especificamente para 26-29/03. Isso é evidência direta de esgotamento real para esta janela, não de calendário fechado. Classificado `ESGOTADO_CONFIRMADO`. **Contou como sinal de demanda.**
- **UP Hotel Boutique** (ampliada) — todas as 4 categorias indisponíveis, e a própria página do Booking exibiu o aviso: *"Oferta limitada em Bombinhas nas suas datas: 5 cama e café (b&bs) como este já estão indisponíveis no nosso site"* — um sinal de esgotamento regional vindo diretamente da plataforma, não inferido por nós. Classificado `ESGOTADO_CONFIRMADO`. **Contou como sinal de demanda.**
- **Hotel/Pousada Atalaia do Mariscal** (teto) — todas as 9 categorias indisponíveis, sem datas alternativas nem aviso regional nesta página específica. Classificado `INDISPONIVEL_NAO_CONCLUSIVO`. Como é referência de teto (peso "não usar"), isso não afeta nenhuma média, mas também significa que não há referência de teto nesta rodada.

**Como isso afeta a confiança do diagnóstico:** o sinal de demanda MÉDIO relatado neste relatório se apoia exclusivamente nos dados com evidência forte — os 5 núcleo efetivamente coletados (com estoque baixo em 3 deles) e os 2 esgotamentos confirmados da ampliada. Ele não depende das 3 indisponibilidades ambíguas (Vila Boa Vida, Riviera, Atalaia), o que é metodologicamente correto, mas também significa que a amostra confirmada é pequena. Por isso o grau de confiança foi classificado como BAIXO, não ALTO — e a recomendação é reavaliar com nova coleta mais perto da data, quando Vila Boa Vida e Vila dos Açores tiverem maior probabilidade de ter aberto seus calendários.

---

## Comparativo com rodadas anteriores

| Rodada | Período | Veredito | Diagnóstico | Sinal de demanda |
|---|---|---|---|---|
| 9 (Jan) | 9A-9D | PROTEGER / MANTER | — | MÉDIO (9D, tendência de queda) |
| 10 (Carnaval) | 05-10/02 | ACIMA_DO_NUCLEO_MAS_DEFENSAVEL | PROTEGER | Alto esgotamento núcleo |
| 11 (Fev pós-Carnaval) | 11A-11D | — | MANTER (11B/C/D), PROTEGER (11A) | MISTO/CONTRADITÓRIO (11D) |
| 12 (Março) | 12A-12C | — | MANTER (12A/B), PROTEGER (12C) | MÉDIO aquecendo (12C) |
| **13 (Páscoa)** | **26-29/03** | **ACIMA_DO_MERCADO_COM_RISCO** | **ESPERAR** | **MÉDIO (confiança BAIXA)** |

A Páscoa é a primeira rodada da série em que a Villa aparece claramente acima do núcleo coletado, e a primeira em que a classificação de indisponibilidade separa explicitamente esgotamento real de calendário possivelmente fechado — o que reduz (corretamente) a confiança atribuída ao sinal de demanda, mesmo com dois esgotamentos confirmados.

---

**Importante:** nenhuma tarifa foi alterada nesta rodada. Nenhuma decisão foi criada automaticamente. Nada foi movido para `DECISOES_REVENUE_PENDENTES_VILLA_ARAGUA.md`. Este diagnóstico é preliminar — a decisão final é de Renildo.
