# DIAGNÓSTICO PRELIMINAR DE REVENUE MANAGEMENT — VILLA ARÁGUA

**Status:** persistido — leitura preliminar sobre `INVENTARIO_TARIFAS_PUBLICADAS_AGO2026_ABR2027.md/.csv`
**Regra de leitura:** este diagnóstico aponta o que **manter, corrigir, revisar e proteger** — ele não decide nada sozinho. Toda ação segue a governança de `CONTEXTO_GOVERNANCA_REVENUE_VILLA_ARAGUA.md`: a IA analisa, Renildo decide.
**Atualização de 2026-07-25:** os alertas 1 a 4 abaixo já têm decisão humana registrada e aplicada — ver `DECISOES_REVENUE_PENDENTES_VILLA_ARAGUA.md` (cards 1–4) para os valores decididos. O texto original de cada alerta foi mantido como histórico da recomendação; não foi reescrito.

---

## Leitura geral

A tabela da Pousada Arágua tem uma lógica clara de escada tarifária:

1. Organic / Fuego / Metallo
2. Terra / Wood
3. Acqua
4. Luna
5. Duplex Soleil

A estrutura mensal também faz sentido: baixa temporada → retomada → média temporada → pré-temporada → dezembro → Natal → Réveillon → janeiro → fevereiro → março → abril.

O ponto que mais exige atenção é a **Casa Arágua**. Ela não deve ser apenas mais uma acomodação dentro da régua da pousada. Ela é outro produto, com proposta premium, privacidade e casa completa — e a análise abaixo mostra vários períodos em que o preço publicado ainda não reflete isso.

---

## Alertas de prioridade alta

### 1. Semana Santa / Páscoa 2027 — Pousada com preço abaixo do mês base

**Status: `DECIDIDO_APLICADO` em 2026-07-25 — ver `DECISOES_REVENUE_PENDENTES_VILLA_ARAGUA.md`, card 1.**

Em março/2027, algumas tarifas de Páscoa aparecem **abaixo** da tarifa base do próprio mês:

| Produto | Março base | Páscoa atual | Diagnóstico |
|---|---|---|---|
| Organic / Fuego / Metallo | R$ 607 | R$ 595 | corrigir |
| Terra / Wood | R$ 698 | R$ 684 | corrigir |
| Acqua | R$ 759 | R$ 744 | corrigir |
| Luna | R$ 801 | R$ 785 | corrigir |
| Duplex Soleil | R$ 989 | R$ 970 | corrigir |

A Casa Arágua está coerente na Páscoa: R$ 1.549 contra R$ 1.385 do mês base.

**Recomendação:** corrigir Páscoa primeiro. Feriado não deve ficar abaixo do preço normal.

### 2. Carnaval 2027 — Casa quase igual ao Duplex Soleil

**Status: `DECIDIDO_APLICADO` em 2026-07-25 — ver `DECISOES_REVENUE_PENDENTES_VILLA_ARAGUA.md`, card 2.**

No Carnaval/2027:

| Produto | Valor atual |
|---|---|
| Duplex Soleil | R$ 1.620 |
| Casa Arágua | R$ 1.649 |

Diferença de apenas R$ 29. Isso enfraquece o posicionamento da Casa Arágua como produto premium.

**Faixa de estudo** para datas abertas da Casa Arágua no Carnaval: R$ 1.850 a R$ 1.950.

### 3. Janeiro 2027 — Casa Arágua abaixo do Duplex Soleil

**Status: `DECIDIDO_APLICADO` em 2026-07-25 — ver `DECISOES_REVENUE_PENDENTES_VILLA_ARAGUA.md`, card 3. Casa Arágua confirmada reservada de 28/12/2026 a 06/01/2027; a decisão vale a partir de 07/01/2027.**

Em janeiro/2027 após a virada:

| Produto | Valor atual |
|---|---|
| Casa Arágua | R$ 1.624 |
| Duplex Soleil | R$ 1.744 |

A Casa aparece abaixo do Duplex, o que pode ser incoerente com a proposta da marca.

**Faixa de estudo** para datas abertas da Casa em janeiro: R$ 1.790 a R$ 1.890.

### 4. Casa Arágua em setembro/outubro 2026

**Status: `DECIDIDO_APLICADO` em 2026-07-25 — ver `DECISOES_REVENUE_PENDENTES_VILLA_ARAGUA.md`, card 4.**

A Casa aparece abaixo do Duplex em períodos base:

| Período | Casa Arágua | Duplex Soleil |
|---|---|---|
| Setembro base | R$ 684 | R$ 732 |
| Outubro base | R$ 743 | R$ 813 |

Pode ser aceitável como estratégia de baixa/média temporada, mas precisa ser **decisão consciente**, não consequência automática da régua.

---

## Alertas de prioridade média

### Outubro 2026 — feriado com aumento tímido

| Produto | Base | Feriado | Aumento |
|---|---|---|---|
| Organic / Fuego / Metallo | R$ 499 | R$ 529 | baixo |
| Terra / Wood | R$ 574 | R$ 608 | baixo |
| Acqua | R$ 624 | R$ 661 | baixo |
| Luna | R$ 659 | R$ 698 | baixo |
| Duplex Soleil | R$ 813 | R$ 862 | baixo |

**Recomendação:** comparar concorrência antes de mexer, mas marcar como revisão.

---

## O que manter por enquanto

Não mexer imediatamente em:

- Agosto/2026;
- Setembro base/2026;
- Novembro base/2026;
- Dezembro 1–18/2026;
- Natal/2026;
- Abril/2027.

Também proteger:

- Réveillon;
- Janeiro;
- Carnaval;
- feriados prolongados.

---

## Ordem recomendada de trabalho

1. Corrigir Páscoa 2027 da Pousada.
2. Reposicionar Casa Arágua no Carnaval 2027.
3. Revisar Casa Arágua em janeiro 2027 para datas abertas.
4. Revisar Casa Arágua em setembro/outubro 2026.
5. Revisar outubro 2026 com concorrência.
6. Só depois ajustar baixa temporada.

---

## Regra de decisão sugerida — Regra Casa Arágua

**Em datas fortes, a Casa Arágua deve ser maior que o Duplex Soleil.**

Datas fortes:

- Réveillon;
- Janeiro;
- Carnaval;
- Semana Santa / Páscoa;
- feriados prolongados;
- Natal;
- alta temporada.

Exceção somente com:

- baixa procura comprovada;
- concorrência muito pressionada;
- data muito próxima;
- decisão humana registrada;
- reserva já confirmada que não deve ser alterada.

**Status desta regra:** sugerida por este diagnóstico, não é tarifa aprovada — precisa de validação explícita de Renildo antes de virar critério oficial do agente `villa-precificacao-calendario`.

---

## Importante

Não alterar reservas já confirmadas. Quando um período aparece reservado (ex.: Réveillon 2026 e possivelmente janeiro 2027 da Casa Arágua), o diagnóstico deve virar **aprendizado para futuras datas**, não alteração retroativa.
