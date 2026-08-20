# Painel de Decisão — Villa Arágua

*Painel simples (tabela/checklist, não ferramenta) para a rotina semanal e mensal do agente `villa-rotina-gestao-operacional`. Preenchido com dado real informado por Renildo/equipe ou puxado de outros agentes/arquivos — nunca com número estimado apresentado como fato. Onde não houver dado real, marcar "LACUNA / precisa de confirmação humana" ou "sem dado real ainda", conforme o caso.*

**Última rotina rodada:** 2026-07-29, período analisado 29/07/2026 a 05/08/2026 (pré-lançamento SET 26) — primeira rotina semanal real, rodada por `villa-rotina-gestao-operacional`. Status geral: **ATENÇÃO** (não por risco ativo, e sim porque a maior parte dos blocos abaixo ainda depende de dado que hoje só existe em planilha `.xlsx` binária ilegível pelas ferramentas do projeto, ou de CRM ainda não alimentado — ver detalhe em cada seção).

---

## 1. Resumo executivo

| Campo | Preenchimento |
|---|---|
| Período analisado | 29/07/2026 a 05/08/2026 |
| Status geral | Atenção |
| Principal avanço | Campanhas `SET 26 QUENTE CWB SC` e `SET 26 FRIO CWB SC` montadas e prontas, aguardando lançamento em 05/08/2026 |
| Principal problema | Ausência de dado real acessível nesta rodada para reservas/ocupação, leads e financeiro (arquivos `.xlsx` binários + CRM ainda vazio) |
| Decisão mais importante | Renildo definir forma de exportar dados financeiros/ocupação para texto e confirmar o lançamento das campanhas em 05/08/2026 |
| Prioridade da próxima semana/mês | Viabilizar dado real (exportação de planilhas + início de registro de leads) e lançar SET 26 com o `campaign-preflight-checklist` |

---

## 2. Reservas e ocupação

Separar sempre Pousada Arágua e Casa Arágua.

| Campo | Pousada Arágua | Casa Arágua |
|---|---|---|
| Reservas confirmadas | LACUNA / precisa de confirmação humana | LACUNA / precisa de confirmação humana |
| Reservas em negociação | LACUNA / precisa de confirmação humana | LACUNA / precisa de confirmação humana |
| Buracos no calendário | LACUNA / precisa de confirmação humana | LACUNA / precisa de confirmação humana |
| Feriados disponíveis | LACUNA / precisa de confirmação humana | LACUNA / precisa de confirmação humana |
| Risco de baixa ocupação | LACUNA / precisa de confirmação humana | LACUNA / precisa de confirmação humana |
| Oportunidade comercial | LACUNA / precisa de confirmação humana | LACUNA / precisa de confirmação humana |

*Motivo da lacuna: dado existe apenas em `ESTATISTICAS E RESERVAS/*.xlsx`, arquivo binário não legível pelas ferramentas desta rotina — precisa ser exportado/colado em texto por Renildo para a próxima rodada.*

---

## 3. Leads e comercial

*Fonte: `CRM_LEADS_VILLA_ARAGUA.md`.*

| Campo | Preenchimento |
|---|---|
| Leads recebidos | 0 registrados — `CRM_LEADS_VILLA_ARAGUA.md` está vazio (ver seção "Primeiros leads a registrar manualmente" nesse arquivo) |
| Leads qualificados | LACUNA / precisa de confirmação humana |
| Origem dos leads | LACUNA / precisa de confirmação humana |
| Campanhas relacionadas | Não aplicável ainda — SET 26 não publicada |
| Objeções principais | LACUNA / precisa de confirmação humana |
| Reservas geradas (status "convertido", nunca por dedução) | 0 — nenhum registro no CRM |
| Próximos follow-ups | LACUNA / precisa de confirmação humana |

---

## 4. Campanhas Meta Ads

| Campo | Preenchimento |
|---|---|
| Campanhas ativas | Nenhuma publicada. `SET 26 QUENTE CWB SC` e `SET 26 FRIO CWB SC` estão **montadas / aguardando lançamento em 05/08/2026** |
| Gasto | sem dado real ainda |
| Conversas | sem dado real ainda |
| Custo por conversa | sem dado real ainda |
| Qualidade dos leads | sem dado real ainda |
| Reservas atribuídas | sem dado real ainda |
| Decisão pendente | Nenhuma decisão de manter/ajustar/pausar/escalar cabe agora — campanha ainda não publicada |
| Decisão humana necessária | Confirmar lançamento em 05/08/2026 e rodar `campaign-preflight-checklist` antes de publicar |

**Observação obrigatória enquanto `SET 26 QUENTE CWB SC` e `SET 26 FRIO CWB SC` não forem publicadas:** este bloco fica como **"sem dado real ainda"** — nunca preencher gasto, conversas, custo por conversa ou qualquer métrica antes da publicação real. Ver `campaign-learning-register`, que só entra em uso 24h após a publicação. Confirmado em 2026-07-29: `campaign-learning-register` não foi usado nesta rotina.

---

## 5. Operação

| Campo | Preenchimento |
|---|---|
| Check-ins/check-outs | LACUNA / precisa de confirmação humana |
| Problemas operacionais | LACUNA / precisa de confirmação humana |
| Limpeza | LACUNA / precisa de confirmação humana |
| Manutenção | LACUNA / precisa de confirmação humana |
| Piscina | LACUNA / precisa de confirmação humana |
| Café da manhã | LACUNA / precisa de confirmação humana |
| Enxoval | LACUNA / precisa de confirmação humana |
| Reclamações | LACUNA / precisa de confirmação humana |
| Elogios | LACUNA / precisa de confirmação humana |
| O que pode ser delegado | Checagem manual de manutenção/limpeza por Rene, para alimentar a próxima rotina |

*Motivo da lacuna: nenhum arquivo textual com esses dados foi disponibilizado nesta rodada; requer relato direto de quem está na operação.*

---

## 6. Financeiro — cinco caixas

*Classificação feita via `villa-financial-five-boxes-classifier`. Sempre nesta ordem — a caixa 1 é lida primeiro e isolada; a caixa 5 é sempre a última linha.*

| Caixa | Entradas | Saídas | Saldo | Alerta | Item que pode mascarar o resultado | Decisão necessária |
|---|---|---|---|---|---|---|
| 1. Resultado operacional da Villa Arágua | LACUNA | LACUNA | LACUNA | Sem dado real disponível | Não avaliável nesta rodada | Exportar `FINANCEIRO/*.xlsx` para texto e classificar via `villa-financial-five-boxes-classifier` |
| 2. Renda patrimonial | LACUNA | LACUNA | LACUNA | — | — | Idem acima |
| 3. Família / vida pessoal | LACUNA | LACUNA | LACUNA | — | — | Idem acima |
| 4. MANECO / investimento de futuro | LACUNA | LACUNA | LACUNA | — | — | Idem acima |
| 5. Saldo geral da travessia | LACUNA | LACUNA | LACUNA | Não deve ser estimado a partir das caixas 1–4 ainda vazias | — | Só calcular depois das caixas 1–4 estarem preenchidas com dado real |

*Motivo da lacuna: `FINANCEIRO/*.xlsx` são arquivos binários ilegíveis pelas ferramentas desta rotina; mesmo quando legíveis, os ledgers não vêm categorizados por caixa — exige exportação em texto + classificação manual item a item via `villa-financial-five-boxes-classifier`.*

---

## 7. Tempo de Renildo

| Campo | Preenchimento |
|---|---|
| Tarefas que Renildo fez | LACUNA / precisa de confirmação humana |
| Tarefas que poderiam ser delegadas | Exportação de planilhas; registro de leads no CRM; checagem de manutenção |
| Urgências evitáveis | LACUNA / precisa de confirmação humana |
| Processos que precisam ser criados | Rotina fixa de exportação de dados financeiros/ocupação; hábito de registro imediato de lead no CRM |
| Tempo preservado ou perdido | LACUNA / precisa de confirmação humana |

---

## 8. Decisões pendentes

| Decisão | Área | Impacto financeiro | Impacto em tempo | Risco | Depende de quem | Prazo |
|---|---|---|---|---|---|---|
| Confirmar lançamento de SET 26 (Quente e Fria) | Marketing | LACUNA — sem dado de custo/retorno ainda | Baixo, se checklist já pronto | Baixo, campanhas já montadas | Renildo | 05/08/2026 |
| Exportar `FINANCEIRO/` e `ESTATISTICAS E RESERVAS/` para texto | Financeiro/Operação | Alto — bloqueia toda leitura financeira e de ocupação | Médio (tarefa pontual) | Baixo | Renildo (ou delegar exportação mecânica) | Antes da próxima rotina semanal |
| Iniciar registro de leads no CRM | Comercial | Indireto — sem isso não há visibilidade de funil | Baixo, se virar hábito diário | Médio (perda de histórico de leads já em andamento) | Rene/Nubia | Imediato |
| Checar manutenção/pendência de preço não capturada | Operação/Preço | LACUNA | Baixo | LACUNA | Rene/Nubia | Antes da próxima rotina |

---

## 9. Próximos passos

| Fazer agora | Delegar | Acompanhar | Decidir depois | Transformar em processo |
|---|---|---|---|---|
| Nada de campanha — aguardar 05/08/2026 | Exportação de `.xlsx` para texto | Data de lançamento SET 26 | Ajuste de campanha, só após dado real pós-lançamento | Exportação semanal de planilhas antes da rotina |
| Iniciar registro de leads no CRM | Registro contínuo de leads | Preenchimento do CRM ao longo da semana | Investimento em MANECO (caixa 4), só após caixas 1–3 claras | Registro de lead no momento em que chega, não em lote |
