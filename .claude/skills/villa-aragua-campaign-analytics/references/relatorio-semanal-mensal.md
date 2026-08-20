# Relatório semanal e mensal

Modelo para consolidar a análise em um documento único, sempre separando Pousada e Casa Arágua, e sempre terminando em uma decisão prática.

## Modelo de relatório

```
RELATÓRIO DE CAMPANHA — VILLA ARÁGUA
Período analisado: [datas]
Produto(s): [ ] Pousada Arágua   [ ] Casa Arágua   [ ] Ambos (com números separados)

1. RESUMO EXECUTIVO
   - 2-4 frases: o que aconteceu no período, qual a leitura principal, qual a decisão recomendada.

2. CAMPANHAS ATIVAS
   - Nome da campanha | Produto | Objetivo | Status (ativa/pausada/em teste)

3. INVESTIMENTO
   - Investimento total do período | por campanha | (dado real, com fonte: print/exportação de [data])

4. LEADS E FUNIL
   - Leads recebidos | respondidos | qualificados
   - Orçamentos enviados | follow-ups feitos
   - Reservas confirmadas | reservas perdidas (com motivo, quando disponível)
   - Taxas de conversão por etapa (ver `funil-whatsapp-reserva.md`)

5. CONVERSAS QUALIFICADAS
   - Número de conversas | qualidade (perfil real, dentro do público-alvo, com intenção clara)

6. RECEITA
   - Receita reservada | Receita recebida | (nunca somar as duas como se fossem a mesma coisa)
   - ROAS bruto (declarar sobre qual receita) | ROI (só se houver custo operacional disponível)

7. PRINCIPAIS OBJEÇÕES
   - Lista das objeções mais frequentes no período (ver `villa-aragua-sales-receptionist/references/objecoes-vendas.md`)

8. MELHORES CRIATIVOS
   - Criativo/anúncio | por que se destacou (avanço no funil, não só CTR/CPC)

9. PIORES CRIATIVOS
   - Criativo/anúncio | hipótese do porquê (público, copy, criativo, fadiga)

10. RECOMENDAÇÕES PARA A PRÓXIMA SEMANA/MÊS
    - Lista objetiva de ações sugeridas

11. DECISÃO
    - [ ] Manter   [ ] Pausar   [ ] Ajustar   [ ] Escalar   [ ] Testar nova hipótese
    - Justificativa em 1-2 frases, com base em `decisoes-otimizacao.md`
```

## Regras de preenchimento

- Todo número no relatório precisa vir de dado informado — se uma seção não tem dado suficiente, escrever "sem dado suficiente para esta seção" em vez de estimar.
- Pousada e Casa Arágua sempre em blocos separados quando o relatório cobrir os dois produtos — nunca somar leads/receita/reservas dos dois numa linha única.
- Toda menção a receita precisa dizer se é reservada ou recebida.
- A seção 11 (decisão) é obrigatória — um relatório sem decisão final é só uma lista de números, não cumpre o objetivo desta skill.

## Diferença entre relatório semanal e mensal

- **Semanal**: foco operacional — o que ajustar nos próximos dias (criativo, público, orçamento, follow-up). Rotina alinhada com `AGENTE_IA_MARKETING_VENDAS_META_ADS_VILLA_ARAGUA.md`, seção 16 ("Semanal: analisar métricas, comparar criativos, sugerir novos testes, revisar públicos, atualizar calendário comercial").
- **Mensal**: foco estratégico — consolidar aprendizados do mês, comparar receita e investimento, avaliar datas futuras, planejar o mês seguinte (mesma fonte, rotina "Mensal"). O relatório mensal deve revisitar as decisões semanais tomadas no período e avaliar se produziram o resultado esperado.

## Como este relatório se conecta com o calendário comercial

Ao fechar um relatório em período de feriado, reabertura ou alta temporada (ver `villa-aragua-pricing-revenue/references/calendario-sazonalidade.md` e `villa-aragua-social-media-manager/references/calendario-editorial.md`), sinalizar isso explicitamente no resumo executivo — um resultado fraco em baixa temporada tem leitura diferente de um resultado fraco em 7 de Setembro (data com pacote e demanda historicamente mais forte).

## Como usar este arquivo na prática

1. Reunir os dados disponíveis usando `checklist-dados-campanha.md`.
2. Preencher o modelo seção a seção, marcando "sem dado suficiente" onde faltar informação.
3. Nunca pular a seção de decisão — usar `decisoes-otimizacao.md` para justificar a escolha entre manter/pausar/ajustar/escalar/testar.
4. Encaminhar as recomendações da seção 10 para a skill de execução correta (pricing, receptionist, copywriting, creative ou humanizer).
