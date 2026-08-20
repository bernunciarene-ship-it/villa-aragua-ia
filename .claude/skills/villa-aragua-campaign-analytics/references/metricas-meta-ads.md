# Métricas Meta Ads

Como ler as métricas nativas do Gerenciador de Anúncios antes de qualquer cálculo de retorno. Estas métricas vêm sempre do que o usuário fornecer (print, exportação, planilha) — esta skill nunca as inventa nem as busca sozinha.

## Métrica mais importante: lead barato não é o objetivo, lead que avança é

Antes de olhar qualquer número isolado, fixar o critério (já validado em `SETUP_INICIAL_META_ADS_7_SETEMBRO_VILLA_ARAGUA_2026.md`, seção de avaliação): o melhor anúncio não é necessariamente o de menor custo por mensagem — é o que gera conversa que avança para orçamento e reserva. Um CPM/CPC baixo com leads que nunca respondem no WhatsApp é pior do que um CPM mais alto com leads que qualificam e reservam. Toda leitura de métrica desta skill se subordina a essa pergunta: **esse número, sozinho, diz se o lead avançou no funil? Se não, ele é só metade da história.**

## O que observar por nível

| Nível | O que é | Por que importa |
|---|---|---|
| **Campanha** | Agrupamento por objetivo/produto (ex.: Campanha 1 — Pousada Arágua, Campanha 2 — Casa Arágua, Campanha 3 — Remarketing) | Nunca comparar desempenho entre campanhas de produtos diferentes como se fossem a mesma coisa — Pousada e Casa têm público, oferta e ticket diferentes |
| **Conjunto de anúncios** | Recorte por público/posicionamento dentro da campanha | Onde normalmente se decide ajuste de público (ver `analise-criativos-publicos.md`) |
| **Anúncio** | Peça individual (criativo + copy + CTA) | Nível onde se compara desempenho de copy/criativo específico |
| **Criativo** | Imagem, vídeo ou carrossel usado no anúncio | Ver `analise-criativos-publicos.md` para critério de comparação |
| **Público** | Frio, remarketing, engajamento, lookalike | Público errado explica boa parte de CPL alto ou lead desqualificado |
| **Posicionamento** | Feed, Stories, Reels, Audience Network etc. | Desempenho pode variar muito por posicionamento; não presumir que todos entregam igual |
| **Período analisado** | Janela de datas da análise | Sempre declarar o período — sem isso, qualquer número fica sem contexto (campanha nova precisa de tempo de aprendizado, ver `decisoes-otimizacao.md`) |

## Glossário de métricas

- **Investimento**: valor efetivamente gasto no período — a base de qualquer cálculo de custo (CPL, CPA, ROAS).
- **Alcance**: número de contas únicas que viram o anúncio — indica tamanho de audiência atingida, não engajamento.
- **Impressões**: número total de exibições (uma conta pode ver o mesmo anúncio várias vezes) — impressões muito acima do alcance sinalizam frequência alta.
- **Frequência**: impressões ÷ alcance — média de vezes que a mesma pessoa viu o anúncio. Frequência alta sem novo lead pode indicar fadiga de criativo (ver `decisoes-otimizacao.md`).
- **CPM (custo por mil impressões)**: investimento ÷ (impressões ÷ 1000) — indica custo de exibir o anúncio, não custo de resultado.
- **CTR (taxa de cliques)**: cliques ÷ impressões — indica se o criativo/copy desperta interesse suficiente para clicar.
- **CPC (custo por clique)**: investimento ÷ cliques — quanto custa cada clique, independente do que acontece depois.
- **Custo por conversa**: investimento ÷ número de conversas iniciadas no WhatsApp — a métrica mais próxima do início real do funil comercial (ver `funil-whatsapp-reserva.md`).
- **Número de conversas**: quantas pessoas de fato abriram uma conversa no WhatsApp a partir do anúncio — diferente de clique (nem todo clique vira conversa) e diferente de lead qualificado.
- **Qualidade das conversas**: não é uma métrica nativa do Meta Ads — é uma avaliação qualitativa feita a partir do funil (quantas dessas conversas tinham perfil real, período definido, intenção de reservar) — ver `funil-whatsapp-reserva.md` e `analise-criativos-publicos.md`.

## Como ler as métricas em conjunto (nunca isoladamente)

1. **CPM baixo + CTR baixo**: anúncio barato de exibir, mas não desperta clique — provável problema de criativo/copy, não de público.
2. **CTR alto + custo por conversa alto**: desperta clique, mas não converte em conversa — pode ser desalinhamento entre a promessa do anúncio e o que a pessoa espera ao clicar (ver `villa-aragua-copywriting-conversion` e `villa-aragua-creative-design-ads`).
3. **Custo por conversa baixo + qualidade de conversa baixa**: lead barato, mas fora do perfil ou sem intenção real — sinal de público mal segmentado (ver `analise-criativos-publicos.md`), não de sucesso da campanha.
4. **Frequência alta + queda de CTR ao longo do tempo**: fadiga de criativo — mesmo público já viu o anúncio demais (ver `decisoes-otimizacao.md`, quando trocar criativo).
5. **Todas as métricas de topo boas (CPM, CTR, CPC) mas poucas reservas no fim do funil**: o problema não está no anúncio — está em algum ponto entre o clique e a reserva (ver `funil-whatsapp-reserva.md`).

## Como usar este arquivo na prática

1. Confirmar que o período analisado está claro e que os dados vieram de fonte real (print/exportação — ver `checklist-dados-campanha.md`).
2. Organizar os números por nível (campanha → conjunto → anúncio → criativo → público → posicionamento), nunca misturando Pousada e Casa Arágua na mesma linha.
3. Ler as métricas em conjunto, nunca isoladamente (ver seção anterior).
4. Cruzar com `funil-whatsapp-reserva.md` antes de qualquer conclusão — métrica de Meta Ads sozinha não diz se a campanha está funcionando de verdade, porque não mostra o que aconteceu depois do clique.
