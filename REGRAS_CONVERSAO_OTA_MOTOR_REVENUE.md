# REGRAS DE CONVERSÃO OTA ↔ MOTOR — RADAR DE CONCORRÊNCIA REVENUE

**Status do módulo:** `EM_IMPLANTACAO_MANUAL_ASSISTIDA`
**Função:** metodologia obrigatória para nunca confundir preço visível de OTA (mercado) com preço de motor de reserva (o que a Villa Arágua efetivamente aplica). Todo cálculo do Radar de Concorrência passa por este arquivo.
**Fonte original da regra de canal:** `DECISOES_REVENUE_PENDENTES_VILLA_ARAGUA.md`, seção "Regra de canais" (decidida e aplicada por Renildo em 2026-07-25).

---

## 1. Regra de canal (configuração automática já ativa)

| Canal | Configuração sobre o motor |
|---|---|
| Booking | motor **+25%** |
| Airbnb | motor **+17,6%** |
| Decolar | motor **+17,6%** |

Essas OTAs são atualizadas automaticamente por essas regras já configuradas — a Villa Arágua não precisa (e a IA não deve tentar) alterar o preço em cada OTA manualmente. O motor de reserva (Stays) é a única tarifa que Renildo define diretamente.

## 2. Fórmulas obrigatórias

### 2.1 Preço visível da Villa a partir do motor

```
preco_booking_villa          = valor_motor_villa * 1.25
preco_airbnb_decolar_villa   = valor_motor_villa * 1.176
```

### 2.2 Valor de motor recomendado a partir de um preço-alvo de OTA

```
valor_motor_recomendado (a partir de preço-alvo Booking)          = preco_booking_desejado / 1.25
valor_motor_recomendado (a partir de preço-alvo Airbnb/Decolar)   = preco_ota_desejado / 1.176
```

### 2.3 Exemplo de aplicação (com dado real já decidido, não inventado)

Casa Arágua no Carnaval 2027 tem motor decidido em R$ 1.890 (`DECISOES_REVENUE_PENDENTES_VILLA_ARAGUA.md`, card 2):

- Preço visível no Booking = 1.890 × 1,25 = **R$ 2.362,50**
- Preço visível no Airbnb/Decolar = 1.890 × 1,176 = **R$ 2.222,64**

Se, ao pesquisar a concorrência, Renildo decidir que o preço-alvo ideal da Villa no Booking deveria ser R$ 2.500 para aquele período:

- Valor de motor recomendado = 2.500 / 1,25 = **R$ 2.000,00**

Se o preço-alvo ideal no Airbnb fosse R$ 2.200:

- Valor de motor recomendado = 2.200 / 1,176 = **R$ 1.870,75** (arredondar conforme prática comercial de Renildo)

## 3. Regra de leitura de concorrente pesquisado em OTA

**Preço de concorrente encontrado no Booking, Airbnb ou Decolar é sempre preço visível de mercado — nunca tratar como equivalente direto ao motor da Villa.**

Isso significa:

- Não comparar "preço de motor da Villa" com "preço de concorrente no Booking" diretamente — são duas bases diferentes (uma sem markup, outra com +25%).
- Para comparar de forma justa, sempre converter para o mesmo referencial: ou usar `preco_booking_villa` (Villa também com markup do mesmo canal) contra o preço do concorrente no Booking, ou converter o preço do concorrente para uma base "motor equivalente" quando fizer sentido para a análise (dividindo pelo markup típico daquele canal, assumindo que o concorrente segue lógica semelhante — isso é estimativa, não fato, e deve ser sinalizado como tal).
- O concorrente pode não usar a mesma lógica de markup da Villa — não presumir que o preço dele no Booking também é "motor dele + 25%" sem indicar que é suposição.

## 4. Regra de destino da recomendação

**A recomendação final para Renildo deve sempre ser em valor de motor de reserva (Stays), nunca em valor de OTA.**

Fluxo obrigatório de qualquer análise do Radar:

1. Coletar preço visível do(s) concorrente(s) no canal pesquisado (`COLETAS_CONCORRENCIA_REVENUE.csv`).
2. Montar a leitura de mercado: preço visível da Villa no mesmo canal vs. preço visível dos concorrentes no mesmo canal (mesma base, comparação justa).
3. Definir, a partir dessa leitura, um preço-alvo visível para a Villa naquele canal (se for o caso de ajuste).
4. Converter esse preço-alvo para valor de motor usando a fórmula da seção 2.2.
5. Entregar as duas leituras exigidas: comparação de mercado (visível x visível) **e** recomendação de motor (o número que Renildo realmente aplicaria no Stays).

Nunca pular direto para "sugiro motor = X" sem mostrar a leitura de mercado que originou o número.

## 4.1 Regra de coleta — Pousada Arágua: perfil casal define a base (`REGRA_APROVADA_RENILDO`, 2026-07-25)

Para a Pousada Arágua, toda pesquisa de concorrência usa sempre o mesmo perfil:

- 2 adultos;
- casal;
- uma acomodação;
- preço visível no canal pesquisado.

**Não buscar concorrente separado para cada suíte da pousada neste primeiro momento.** A concorrência define só a **base casal de mercado** — o preço encontrado vira âncora da categoria base (Organic/Fuego/Metallo = 100%). A partir dessa âncora, a régua interna já aprovada (`matriz-precos-pousada-casa.md`) projeta as demais categorias — a concorrência não é pesquisada de novo para Terra/Wood, Acqua, Luna ou Duplex Soleil.

| Etapa | O que fazer |
|---|---|
| 1. Coletar | Preço visível do concorrente, perfil casal/2 adultos/1 unidade, no canal pesquisado (`COLETAS_CONCORRENCIA_REVENUE.csv`: `hospedes = 2`, `unidade_villa_referencia = base (Organic/Fuego/Metallo)`) |
| 2. Ancorar | Esse preço é a âncora de mercado da categoria base — nunca de uma suíte específica |
| 3. Converter | Comparar com o preço visível da própria Villa no mesmo canal para a base (`valor_motor_base_villa × markup do canal`, seção 2.1) |
| 4. Definir motor-base | Se houver ajuste, converter o preço-alvo visível de volta a motor (seção 2.2) |
| 5. Projetar régua | A partir do motor-base decidido, aplicar a régua interna aprovada: Terra/Wood ×1,15 · Acqua ×1,25 · Luna ×1,32 · Duplex Soleil ×1,63 (×1,50 em baixa temporada pura — maio, junho, agosto — ou baixa demanda definida por Renildo) |

**Casa Arágua não segue esta regra.** A Casa Arágua tem pesquisa própria, com perfil de casa/apartamento inteiro, preferencialmente **4 a 6 hóspedes** — nunca usar o perfil casal da Pousada para pesquisar concorrente da Casa, e nunca projetar a Casa pela régua interna da Pousada.

### Exemplo ilustrativo (números fictícios, só para mostrar o pipeline completo — não é dado real)

1. Coleta: concorrente ilustrativo, Booking, casal/2 adultos/1 unidade, diária visível **R$ 480,00**.
2. Preço visível da própria Villa no Booking para a base hoje: motor R$ 399 × 1,25 = **R$ 498,75**. Leitura de mercado: Villa acima do concorrente nesse canal.
3. Renildo decide um preço-alvo visível de R$ 470,00 no Booking para a base → motor-base recomendado = 470 / 1,25 = **R$ 376,00**.
4. Projeção pela régua interna a partir do motor-base R$ 376,00:

| Categoria | Cálculo | Motor recomendado |
|---|---|---|
| Organic/Fuego/Metallo (base) | 376 × 1,00 | R$ 376,00 |
| Terra/Wood | 376 × 1,15 | R$ 432,40 |
| Acqua | 376 × 1,25 | R$ 470,00 |
| Luna | 376 × 1,32 | R$ 496,32 |
| Duplex Soleil (alta/feriado) | 376 × 1,63 | R$ 612,88 |
| Duplex Soleil (baixa pura) | 376 × 1,50 | R$ 564,00 |

Uma única coleta (perfil casal, categoria base) gera recomendação para as 8 acomodações da Pousada. Isso continua sendo recomendação — Renildo decide e aplica manualmente no motor.

## 5. Regras que continuam valendo (herdadas da governança geral do Revenue)

- A IA não decide preço final.
- A IA calcula, compara, recomenda e explica — Renildo decide.
- Renildo aplica manualmente no motor de reserva.
- As OTAs são atualizadas automaticamente pelas regras de canal já configuradas — a IA nunca tenta simular ou sugerir uma alteração direta em Booking/Airbnb/Decolar.
- Nenhuma automação de coleta (scraping) existe ou deve ser criada nesta fase — toda coleta em `COLETAS_CONCORRENCIA_REVENUE.csv` é manual/assistida.
