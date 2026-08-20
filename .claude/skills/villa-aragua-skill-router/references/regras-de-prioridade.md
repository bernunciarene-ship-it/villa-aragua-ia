# Regras de prioridade

Regras que decidem quando incluir cada skill, quantas skills usar, e como resolver conflito — aplicadas depois de identificar a intenção (`matriz-intencoes-skills.md`) e antes de montar o fluxo final (`fluxos-de-trabalho.md`).

## Regras de inclusão obrigatória

- Se envolver **preço, desconto, pacote, diária, margem ou ponto de equilíbrio**, sempre incluir `villa-aragua-pricing-revenue`.
- Se envolver **WhatsApp, lead, objeção, follow-up ou reserva**, sempre incluir `villa-aragua-sales-receptionist`.
- Se envolver **análise de dados, campanha, ROAS, CPA, CPL, funil ou performance**, começar por `villa-aragua-campaign-analytics`.
- Se envolver **texto final para cliente/hóspede** (qualquer texto que vá ser lido por um hóspede ou lead real), usar `villa-aragua-humanizer-pt-br` como **última passada**, sempre.
- Se envolver **anúncio, headline, CTA ou landing page**, usar `villa-aragua-copywriting-conversion`.
- Se envolver **imagem, criativo, carrossel, story visual ou Meta Ads visual**, usar `villa-aragua-creative-design-ads`.
- Se envolver **Instagram orgânico, calendário ou comunidade**, usar `villa-aragua-social-media-manager`.
- Se envolver **site, blog, guia digital, clusters ou planejamento de conteúdo**, usar `villa-aragua-content-strategy`.
- Se envolver **Google, IA, citabilidade, SEO, FAQ ou página estruturada**, usar `villa-aragua-ai-seo-geo`.
- Se envolver **plano de crescimento, canais de aquisição, experimentos, reativação de hóspede antigo ou parceria local**, usar `villa-aragua-growth-marketer`.
- Se envolver **entender por que o lead hesita, compara preço ou some**, usar `villa-aragua-marketing-psychology`.

## Limites de quantidade

- **Tarefas simples**: no máximo 3 skills no total (1 principal + até 2 de apoio).
- **Tarefas complexas** (múltiplas etapas reais, ex.: campanha completa do zero): até 5 skills no total.
- Acima de 5 skills, é sinal de que o pedido deveria ser quebrado em mais de uma tarefa/fluxo, não resolvido de uma vez só.

## Regra de exclusão

**Nunca acionar uma skill que não contribui diretamente para a saída pedida.** Antes de incluir qualquer skill de apoio, checar: se essa skill fosse removida do fluxo, o resultado final ficaria pior ou incompleto? Se a resposta for não, ela não deveria estar na lista. Isso vale mesmo para skills "quase sempre úteis" como `villa-aragua-humanizer-pt-br` — se o pedido é puramente técnico/interno (ex.: uma tabela de métricas para o próprio Renildo ler, sem nenhum texto voltado a hóspede), a humanização pode não se aplicar.

## Regra de conflito

Quando duas skills parecerem sugerir caminhos diferentes (ex.: `villa-aragua-marketing-psychology` sugere um ângulo emocional forte, mas `villa-aragua-pricing-revenue` não confirma a oferta que sustentaria esse ângulo), **dados oficiais da Villa Arágua têm prioridade sobre qualquer recomendação estratégica**. Nenhuma skill de estratégia, growth ou psicologia pode "vencer" um dado confirmado em `DADOS_OFICIAIS_ATENDIMENTO_VILLA_ARAGUA.md` ou numa validação de `villa-aragua-pricing-revenue`.

## Regra de produto (Pousada x Casa)

Sempre que o pedido envolver os dois produtos ao mesmo tempo, o roteamento explicita que cada um segue tratamento separado dentro do mesmo fluxo — nenhuma skill de apoio deve "misturar" oferta/diferencial de Pousada e Casa Arágua na mesma peça, salvo comparação explícita e identificada (mesma regra já presente em todas as skills de execução).

## Regra de honestidade sobre skill inexistente

Se a tarefa exigir algo que nenhuma das 11 skills reais cobre (ex.: gestão de e-mail marketing, automação de PMS/channel manager), a resposta correta é: nomear a lacuna, sugerir a skill real mais próxima como aproximação parcial, e sinalizar que uma skill dedicada ainda não existe — nunca inventar que uma dessas skills faz algo que não faz.

## Como aplicar as regras em ordem

1. Identificar a intenção (`matriz-intencoes-skills.md`).
2. Checar as regras de inclusão obrigatória — alguma delas se aplica ao pedido?
3. Contar quantas skills isso já totaliza — está dentro do limite (3 simples / 5 complexa)?
4. Para cada skill candidata, aplicar a regra de exclusão (ela contribui de verdade?).
5. Se houver sinal de conflito entre recomendações, aplicar a regra de prioridade de dado oficial.
6. Montar a saída final conforme os formatos de `SKILL.md`.
