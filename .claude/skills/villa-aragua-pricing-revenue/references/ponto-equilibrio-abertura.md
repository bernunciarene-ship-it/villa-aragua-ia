# Ponto de equilíbrio de abertura

## Por que isso importa agora

A Pousada Arágua está em processo de reabertura, com data oficial em **01/08/2026** (confirmado 2026-07-07). Isso torna a lógica de ponto de equilíbrio especialmente relevante neste momento: reabrir tem custo (equipe, café da manhã, limpeza, Meta Ads) mesmo antes da ocupação normalizar — é preciso saber a partir de que ocupação a operação deixa de dar prejuízo.

## Limitação conhecida dos dados financeiros

As planilhas em `FINANCEIRO/` são ledgers simples (colunas Data/Nome/Débito), **sem categorização por caixa** — não é possível hoje extrair automaticamente "custo de café da manhã do mês" ou "custo de limpeza do mês" sem classificar manualmente cada lançamento primeiro. Isso significa: **não inventar um número de custo operacional mensal ou de ponto de equilíbrio em R$** — a lógica abaixo é o *método* para calcular, não o resultado já calculado.

Além disso, a regra de separação financeira do DNA (seção 13, já resumida em `CLAUDE.md`) exige nunca misturar como "resultado da pousada": (1) operação Villa Arágua, (2) renda patrimonial, (3) família/vida pessoal, (4) MANECO. Qualquer cálculo de ponto de equilíbrio deve isolar apenas o caixa 1 (operação).

## Categorias de custo a considerar

Ao montar (com Renildo/equipe) um cálculo de ponto de equilíbrio para um período de abertura, mapear:

- Equipe (recepção, limpeza, apoio operacional).
- Café da manhã (insumos servidos na suíte).
- Limpeza (rotina + limpeza final, incluindo o caso específico da Casa Arágua, que cobra R$ 450,00 de taxa de limpeza final por estadia — receita, não custo, mas precisa ser líquida dos custos reais de limpeza).
- Lavanderia (enxoval, toalhas — ver valores de reposição em `matriz-precos-pousada-casa.md`).
- Água e luz.
- Manutenção da piscina.
- Manutenção geral (reparos, equipamentos).
- Meta Ads (orçamento confirmado atual: R$ 45,00/dia, ~R$ 1.350,00/mês se mantido o valor — fonte: `CHECKLIST_DECISOES_CAMPANHA_REABERTURA_VILLA_ARAGUA_2026.md`, 2026-07-07).

## Lógica de cálculo (método, não resultado pronto)

1. **Custo fixo do período** = soma de equipe + manutenção básica + Meta Ads, independente da ocupação.
2. **Custo variável por diária ocupada** = café da manhã + limpeza + lavanderia + água/luz proporcional à ocupação.
3. **Receita por diária** = diária média do produto (R$ 500,00 Pousada / R$ 990,00 Casa, como referência hoje disponível) menos custo variável daquela diária.
4. **Ocupação mínima para empatar** = custo fixo do período ÷ (receita por diária − custo variável por diária), por unidade/acomodação disponível no período.
5. Comparar a ocupação mínima calculada com a ocupação projetada (leads no funil, histórico de reservas do período equivalente, se houver) para decidir se vale abrir a pleno custo, abrir reduzido, ou não abrir uma unidade específica.

## "Abrir e lucrar" x "abrir para não perder dinheiro"

Duas perguntas diferentes, que não devem ser confundidas:

- **Abrir e lucrar**: a ocupação projetada supera o ponto de equilíbrio com margem suficiente para gerar lucro real na operação — decisão de expandir esforço comercial (mais Meta Ads, mais pacotes) nesse período faz sentido.
- **Abrir para não perder dinheiro**: a ocupação projetada só cobre o custo fixo, sem margem — ainda pode valer a pena abrir (para manter presença, atender hóspedes já fidelizados, gerar avaliações, aquecer para o período seguinte), mas não é hora de investir pesado em aquisição paga nem de ceder desconto.
- Se a ocupação projetada fica **abaixo** do ponto de equilíbrio mesmo no cenário conservador, a decisão de abrir/operar reduzido/concentrar em uma única unidade é de Renildo — a IA sinaliza o número, não decide sozinha fechar ou não abrir.

## Como isso se conecta com o restante da skill

- Se a ocupação projetada para uma data está baixa, isso é justamente o gatilho que o Revenue Manager usa para "reduzir preço ou criar oferta" (ver `regras-desconto.md` e `CLAUDE.md`, seção Revenue Manager) — mas sempre com aprovação, nunca decidido pela IA.
- Datas de alta ocupação projetada (ex.: 7 de Setembro, com pacote já confirmado) tendem a superar o ponto de equilíbrio com folga — não é o momento de oferecer condição especial adicional.
- Ao montar orçamento de Meta Ads por campanha/data, cruzar com esta lógica: "a campanha não deve gerar demanda maior do que a operação consegue atender com segurança" (fonte: `CHECKLIST_DECISOES_CAMPANHA_REABERTURA_VILLA_ARAGUA_2026.md`) — isso também é, na prática, uma checagem de capacidade vs ponto de equilíbrio.
