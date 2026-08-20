# RODADA DE CORREÇÃO V1 — AGENTE MARKETING & CAMPANHAS META ADS VILLA ARÁGUA

**Base:** `RESULTADO_TESTE_AGENTE_MARKETING_CAMPANHAS_META_ADS_VILLA_ARAGUA.md`
**Status:** ajustes aplicados nos dois arquivos autorizados
**Modo:** apoio estratégico — sem automação, sem acesso à conta Meta Ads, sem publicação

Este documento registra os 3 ajustes aprovados após a bateria de 38 testes, aplicados apenas em:
1. `AGENTE_MARKETING_CAMPANHAS_META_ADS_VILLA_ARAGUA.md`
2. `TESTE_AGENTE_MARKETING_CAMPANHAS_META_ADS_VILLA_ARAGUA.md`

Nenhum outro arquivo foi alterado — dados oficiais, bibliotecas, skills e a Recepcionista IA permanecem intocados.

---

## Ajuste 1 — Histórico antes de explicação estrutural

**Referência:** achado do Caso D-03 (`RESULTADO_TESTE_AGENTE_MARKETING_CAMPANHAS_META_ADS_VILLA_ARAGUA.md`).

Incorporado em `AGENTE_MARKETING_CAMPANHAS_META_ADS_VILLA_ARAGUA.md`, Etapa 6 — Histórico:

> O agente não pode aceitar como estrutural uma explicação sobre desempenho de produto, público, campanha ou canal sem antes consultar o histórico disponível da própria Villa Arágua.

Exemplos de conclusões que não devem ser aceitas automaticamente: "Casa Arágua naturalmente gera poucos leads e reservas de alto valor"; "Pousada sempre gera mais volume"; "Famílias convertem melhor"; "Esse público é naturalmente mais caro"; "Esse formato sempre performa melhor".

Conduta correta: verificar histórico documentado → comparar campanhas equivalentes → avaliar produto, oferta, preço, criativo, público e atendimento → declarar quando não houver dados suficientes → tratar a explicação como hipótese, não como verdade.

> Explicação plausível não é evidência. Sem histórico suficiente, registrar como hipótese a testar.

**Considerado aceito.** Corrige exatamente a lacuna do Caso D-03, sem contradizer nenhum outro caso já testado.

---

## Ajuste 2 — Uso correto da referência de R$45/dia

**Referência:** achado do Caso H-02.

Incorporado em `AGENTE_MARKETING_CAMPANHAS_META_ADS_VILLA_ARAGUA.md`, Etapa 14 — Orçamento:

> O valor de R$45 por dia é uma referência registrada em um caso real da Villa Arágua. Ele não deve ser tratado como orçamento padrão, mínimo, máximo, piso ou teto para todas as campanhas.

O agente analisa orçamento com base em: objetivo, produto, período, disponibilidade, margem, caixa, histórico, duração, quantidade de públicos, quantidade de criativos, capacidade operacional, maturidade da campanha.

> Referência histórica orienta a análise, mas não substitui o diagnóstico financeiro e comercial de cada campanha.

Nos cenários conservador, provável e otimista: não usar automaticamente R$45/dia; citar apenas quando relevante como comparação histórica; Renildo decide o valor final.

**Considerado aceito.** Corrige o risco de ancoragem identificado no Caso H-02, sem alterar o princípio de que "o agente recomenda, Renildo decide".

---

## Ajuste 3 — Handoff de Qualidade dos Leads

**Referência:** lacuna estrutural registrada no resumo executivo do resultado do teste (mecanismo de troca de dados entre Recepcionista IA e Agente Marketing nunca operacionalizado).

Incorporado em `AGENTE_MARKETING_CAMPANHAS_META_ADS_VILLA_ARAGUA.md`, nova subseção "Handoff de Qualidade dos Leads" dentro da seção 26 (Relação com a Recepcionista IA):

- objetivo: permitir que a Recepcionista IA gere informação agregada e anonimizada para o Agente Marketing avaliar qualidade dos leads;
- sem integração automática, sem transferência de conversa privada, sem dado pessoal, sem conexão de sistemas — **handoff manual e supervisionado**;
- classificação simples de qualidade: **Lead A (Qualificado)**, **Lead B (Potencial)**, **Lead C (Baixa aderência)**, **Lead D (Não avaliável)**;
- formato fixo "Resumo Manual de Qualidade dos Leads" (campos agregados: período, campanha/origem, produto, totais por classificação, datas/produto mais procurados, objeções, pedidos de desconto, orçamentos enviados, reservas confirmadas, motivos de perda, limitações dos dados);
- o Agente Marketing pode usar o resumo para revisar público, copy, promessa, produto, calendário, preço (como hipótese) e destino/atendimento;
- o Agente Marketing não pode acessar conversa automaticamente, reclassificar pessoa por dado pessoal, concluir causa sem evidência, atribuir reserva sem rastreamento, ou alterar campanha automaticamente.

**Considerado aceito.** Fecha a lacuna estrutural identificada, sem criar nenhuma integração técnica — o handoff continua 100% manual.

---

## Atualização da bateria de testes

Em `TESTE_AGENTE_MARKETING_CAMPANHAS_META_ADS_VILLA_ARAGUA.md`:

1. **Caso D-03 revisado** (seção 7) — agora exige checagem de histórico da Casa Arágua antes de aceitar "baixo volume, alto valor" como padrão; trata a explicação como hipótese até confirmação; novo "erro grave" acrescentado.
2. **Caso H-02 revisado** (seção 11) — agora exige que R$45/dia seja citado só como referência histórica, nunca como orçamento padrão; cenário construído a partir do diagnóstico do caso; novo "erro grave" acrescentado.
3. **Novo Grupo J — Handoff de Qualidade dos Leads** (seção 13, 6 casos): J-01 (muitos Leads C e poucas reservas), J-02 (poucos Leads A com reservas de alto valor), J-03 (leads sem origem conhecida), J-04 (Recepcionista envia conversas completas com dados pessoais — deve ser rejeitado), J-05 (muitas objeções de preço — preço tratado como hipótese, não causa automática), J-06 (muitos leads pedem datas indisponíveis — calendário revisado antes de aumentar orçamento).
4. Total de casos atualizado de **38 para 44**.
5. Resumo por grupos, tabela final (seção 16), critérios de aprovação (seção 15) e critérios de falha crítica (seção 17) atualizados para refletir os 3 ajustes.

---

## Resumo final

**Ajustes aceitos:** 3 de 3.

**Ajustes rejeitados:** nenhum.

**Impacto na arquitetura:** nenhum estrutural. Os 3 ajustes são esclarecimentos, uma correção de critério (histórico antes de explicação estrutural), uma correção de calibragem (orçamento) e uma formalização de um mecanismo já previsto em princípio (handoff de qualidade de leads) — não criam agente novo, não alteram a sequência de 17 etapas, não tocam bibliotecas, dados oficiais ou skills.

**Necessidade de nova execução:** sim — mini lote de validação com os 8 casos afetados (D-03, H-02, J-01 a J-06), registrado em `RESULTADO_RODADA_CORRECAO_V1_AGENTE_MARKETING_META_ADS_VILLA_ARAGUA.md`.

Nenhuma automação, campanha, publicação ou integração foi criada por este documento.
