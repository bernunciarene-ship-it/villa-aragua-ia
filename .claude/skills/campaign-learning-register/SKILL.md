# Villa Arágua — Campaign Learning Register

Esta skill ensina a **registrar aprendizado real de campanhas Meta Ads da Villa Arágua** — transformar dado real (gasto, alcance, conversa, objeção, reserva) em registro estruturado para análise humana posterior. Ela nasceu do ciclo de campanha do feriado 7 de Setembro 2026 (`SET 26 QUENTE CWB SC` e `SET 26 FRIO CWB SC`), registrado em `MAPA_DO_CEREBRO_IA_VILLA_ARAGUA.md`, seção 15, e do modelo de registro já usado em `REVISAO_HUMANA_PUBLICACAO_SET26_META_ADS.md`, seção 10.

**Regra mais importante da skill, acima de qualquer outra:** esta skill **ainda não otimiza campanha sozinha**. Ela só transforma dado real em registro estruturado e recomenda análise humana — nunca pausa, nunca altera verba, nunca troca público ou criativo por conta própria. Toda decisão de ajuste continua sendo de Renildo.

## Fontes da verdade (não alterar, só consultar)

- `MAPA_DO_CEREBRO_IA_VILLA_ARAGUA.md`, seção 15 (Aprendizado Meta Ads) e seção 19 (Plano de evolução — esta skill nasce como Fase 1/2).
- `REVISAO_HUMANA_PUBLICACAO_SET26_META_ADS.md`, seção 10 — schema original que esta skill formaliza.
- `.claude/agents/villa-marketing-meta-ads.md` — agente que fornece o contexto de campanha (estrutura, público, criativo) para o registro.
- `.claude/agents/villa-rotina-gestao-operacional.md` — agente que consome este registro na rotina semanal/mensal.
- `.claude/skills/campaign-preflight-checklist/SKILL.md` — skill irmã, usada antes da publicação; esta aqui só entra em uso depois que a campanha publica e gera dado real.
- Dados reais de campanha informados por Renildo ou obtidos via integração conectada ao Meta Ads (quando disponível) — sempre em modo leitura.

## Quando usar

- Após 24h de campanha publicada.
- Após 48h.
- Após 72h.
- Após 7 dias.
- Ao encerrar a campanha.
- Quando houver conversa relevante de lead (objeção forte, pergunta recorrente, sinal de qualidade alta ou baixa).
- Quando houver reserva atribuída à campanha.
- Quando houver objeção importante que se repete entre leads.

**Antes de qualquer campanha publicar, esta skill não tem dado para registrar** — não force um registro com número estimado ou hipotético. Se acionada antes da hora, responda que ainda não há dado real e aponte para o momento certo (24h após publicação, no mínimo).

## Campos obrigatórios do registro

| Campo | Preenchimento |
|---|---|
| Data | |
| Campanha | |
| Conjunto | |
| Criativo | |
| Produto | Pousada Arágua / Casa Arágua — nunca os dois juntos no mesmo registro |
| Público | |
| Gasto | |
| Alcance | |
| Impressões | |
| Cliques | |
| Conversas no WhatsApp | |
| Custo por conversa | |
| Leads qualificados | |
| Reservas geradas | |
| Receita estimada | |
| Objeções | |
| Dúvidas frequentes | |
| Qualidade do lead | |
| Decisão tomada | |
| Aprendizado | |
| Possível ajuste em copy | |
| Possível ajuste em público | |
| Possível ajuste em criativo | |
| Possível ajuste em atendimento | |
| Possível ajuste em preço/revenue | |
| Decisão humana necessária | |

Nunca preencher um campo com valor inventado — se o dado não foi informado, o campo fica em branco com a marcação "LACUNA / precisa de confirmação humana", nunca com uma estimativa apresentada como fato.

## Como conduzir o registro

1. Confirmar que existe dado real (não rodar sobre campanha ainda em rascunho ou recém-publicada sem 24h).
2. Preencher os campos objetivos primeiro (data, campanha, conjunto, criativo, produto, público, métricas numéricas).
3. Preencher os campos qualitativos (objeções, dúvidas, qualidade do lead) com base no que foi de fato relatado — nunca supor tom ou intenção do lead sem informação.
4. Gerar a leitura curta e a hipótese de aprendizado (ver saída abaixo).
5. Se o volume de dado for pequeno (poucas conversas, poucas horas de veiculação), dizer isso explicitamente — não tratar amostra pequena como conclusão forte.

## Formato de saída obrigatório

1. **Registro estruturado** — tabela ou lista com todos os campos acima preenchidos ou marcados como lacuna.
2. **Leitura curta do que aconteceu** — 2 a 4 frases, sem inflar o resultado.
3. **Hipótese de aprendizado** — o que este registro sugere, deixando claro que é hipótese, não regra.
4. **Decisão recomendada para Renildo avaliar** — nunca uma decisão já tomada pela skill.
5. **Aviso de volume de dado**, sempre que aplicável: se a amostra for pequena (poucas conversas, poucas horas/dias de veiculação), dizer claramente "ainda não há volume suficiente para uma leitura forte" em vez de apresentar uma tendência como confirmada.

## O que esta skill nunca faz

- Nunca altera campanha.
- Nunca pausa campanha.
- Nunca aumenta verba.
- Nunca troca público.
- Nunca troca criativo.
- Nunca promete preço.
- Nunca confirma disponibilidade.
- Nunca mistura Pousada Arágua e Casa Arágua no mesmo registro ou na mesma leitura.
- Nunca decide otimização sozinha — o máximo que entrega é uma recomendação para Renildo avaliar.
