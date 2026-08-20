# Villa Arágua — Financial Five Boxes Classifier

Esta skill ensina a **classificar entradas e saídas financeiras da Villa Arágua nas cinco caixas obrigatórias** definidas no DNA (seção 13) e formalizadas em `MAPA_DO_CEREBRO_IA_VILLA_ARAGUA.md`, seção 2.3. Ela existe porque os ledgers de `FINANCEIRO/` são simples (Data / Nome / Débito), sem categorização por caixa — esta skill é a camada de julgamento que falta entre o lançamento bruto e uma leitura financeira confiável.

**Regra mais importante da skill, acima de qualquer outra:** esta skill **nunca apresenta o resultado da Villa Arágua como um "lucro/prejuízo da pousada" único e misturado**. Toda classificação separa primeiro a operação real (caixa 1), isolada, e só depois as demais caixas. Quando um item não se encaixar com clareza em uma caixa, a resposta correta é marcar **"ambíguo — decisão humana necessária"**, nunca forçar uma classificação para fechar a conta.

## As cinco caixas (ordem obrigatória de leitura)

1. **Resultado operacional da Villa Arágua** — receita e custo da operação em si (Pousada Arágua e Casa Arágua, sempre separadas entre si dentro desta caixa).
2. **Renda patrimonial** — o que vem de patrimônio, não da operação diária.
3. **Família / vida pessoal** — despesas e entradas da vida de Renildo, fora da operação.
4. **MANECO / investimento de futuro** — o que está sendo direcionado ou reservado para a travessia estratégica.
5. **Saldo geral da travessia** — leitura consolidada de tudo, só depois das quatro caixas acima estarem separadas.

**Ordem obrigatória:** classificar e apresentar sempre a caixa 1 primeiro e isolada; a caixa 5 é sempre a última linha, nunca o ponto de partida.

## Fontes da verdade (não alterar, só consultar)

- `CLAUDE.md` — seção Financeiro (regra de separação obrigatória, DNA seção 13) e a limitação já conhecida de que os ledgers de `FINANCEIRO/` não vêm categorizados.
- `MAPA_DO_CEREBRO_IA_VILLA_ARAGUA.md`, seção 2.3 — definição das cinco caixas e a ordem de leitura, e seção 17.6 (rotina financeira) que consome esta skill.
- `FINANCEIRO/` — ledgers simples de custo/receita da pousada (fonte bruta a classificar, nunca alterada por esta skill).
- `.claude/agents/villa-rotina-gestao-operacional.md` — agente que aciona esta skill na rotina mensal (e, quando fizer sentido, semanal).
- `DADOS_OFICIAIS_ATENDIMENTO_VILLA_ARAGUA.md` — quando precisar confirmar se um valor é de Pousada ou Casa Arágua.

## Regras de classificação

- **Nunca misturar tudo como lucro ou prejuízo da pousada** — cada caixa é lida e reportada separadamente.
- Receita da **Pousada Arágua** e receita da **Casa Arágua** ficam separadas dentro da caixa 1 — nunca somadas como um número único sem discriminação.
- **Empréstimo, antecipação de recebível ou venda de ativo não são faturamento operacional** — entram como movimento de caixa, nunca como receita da caixa 1. Sinalizar sempre como possível item que mascara o resultado real se for lançado sem essa distinção.
- **Custos pessoais não entram como custo operacional da pousada** — vão para a caixa 3.
- **Gastos do MANECO não entram como prejuízo da Villa Arágua** — vão para a caixa 4, mesmo que financiados com caixa gerado pela operação.
- Quando houver dúvida real de classificação (item que poderia caber em mais de uma caixa, ou sem contexto suficiente), marcar **"ambíguo — decisão humana necessária"** e não decidir sozinha.

## Itens que a skill sabe classificar (ponto de partida — não é lista fechada)

| Item | Caixa provável | Observação |
|---|---|---|
| Hospedagem Pousada Arágua | 1 (operação) | Receita, subcategoria "Pousada" |
| Hospedagem Casa Arágua | 1 (operação) | Receita, subcategoria "Casa" — nunca somar com a linha acima sem discriminar |
| Booking, Airbnb | 1 (operação) | Receita de canal, com comissão associada (ver linha "comissão") |
| WhatsApp, Pix, cartão | 1 (operação) | Meio de recebimento, não altera a caixa — só confirma canal de entrada |
| Comissão (Booking/Airbnb) | 1 (operação) | Custo direto da operação, associado ao canal |
| Limpeza, manutenção, café da manhã, enxoval | 1 (operação) | Custo operacional direto |
| Energia, água, internet | 1 (operação) | Custo operacional — **ambíguo se o imóvel também for residência**: marcar decisão humana se não houver separação clara de medidor/uso |
| Funcionário | 1 (operação) | Custo operacional, se ligado à operação da pousada/casa |
| Imposto operacional | 1 (operação) | Custo operacional direto |
| Aluguel de imóvel | Depende — 1 se for imóvel usado na operação, 3 se for moradia pessoal | **Ambíguo por padrão** até confirmação |
| Renda patrimonial | 2 (patrimônio) | Nunca somada à receita operacional |
| Escola, mercado, saúde, lazer, gasolina (uso pessoal) | 3 (família/vida pessoal) | Nunca entra como custo da pousada |
| MANECO (qualquer gasto rotulado como tal) | 4 (MANECO) | Nunca tratado como prejuízo da Villa Arágua |
| Consultoria, design, roteiro (ligados ao MANECO) | 4 (MANECO) | Se ligado à operação da pousada em vez do MANECO, mover para caixa 1 — confirmar contexto |
| Viagem | Depende — 3 (pessoal) ou 4 (MANECO) conforme o motivo | **Ambíguo por padrão** até confirmação |
| Dívida, empréstimo, antecipação | Movimento de caixa, não é receita/despesa operacional de nenhuma caixa | Sinalizar sempre como possível mascarador do resultado real; anotar em qual caixa o valor efetivamente entrou/saiu quando usado |
| Obra | Depende — 1 se for reforma da operação, 3/4 se for pessoal/MANECO | **Ambíguo por padrão** até confirmação |
| Venda de ativo | Movimento de caixa (não é receita operacional) | Mesma regra do empréstimo — nunca contar como faturamento da caixa 1 |

## Formato de saída obrigatório

Para cada item analisado:

1. **Item analisado:**
2. **Valor, se houver:**
3. **Caixa financeira:** (1 a 5, ou "ambíguo — decisão humana necessária")
4. **Subcategoria:** (ex.: Pousada/Casa dentro da caixa 1; tipo de gasto pessoal dentro da caixa 3)
5. **Justificativa curta:**
6. **Recorrente ou pontual:**
7. **Impacto no caixa:** (entrada/saída, e se afeta liquidez imediata ou é só contábil)
8. **Decisão humana necessária, se houver:**
9. **Alerta se o item puder mascarar o resultado real da pousada:** (ex.: empréstimo lançado como receita, gasto do MANECO lançado como custo operacional, aluguel de moradia lançado como custo da pousada)

Ao final de um lote de itens, sempre fechar com a leitura por caixa, na ordem 1→2→3→4→5, nunca começando pela 5.

## O que esta skill nunca faz

- Nunca apresenta um número único de "lucro/prejuízo da pousada" misturando as cinco caixas.
- Nunca trata empréstimo, antecipação ou venda de ativo como faturamento operacional.
- Nunca classifica um item ambíguo sozinha só para "fechar a conta" — declara a ambiguidade.
- Nunca altera lançamento em `FINANCEIRO/` — só lê e classifica.
- Nunca decide o que fazer com o resultado (investir, guardar, gastar) — isso é sempre decisão de Renildo.
