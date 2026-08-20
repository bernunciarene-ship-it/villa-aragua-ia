# Decisões de otimização

Regras práticas para transformar análise em ação. Esta skill recomenda; a decisão de aplicar (principalmente preço, desconto e orçamento) é sempre de Renildo/equipe (mesma régua de `AGENTE_IA_MARKETING_VENDAS_META_ADS_VILLA_ARAGUA.md`).

## Princípio geral: nem toda decisão é sobre a campanha

Antes de mexer em criativo, público ou orçamento, confirmar (via `funil-whatsapp-reserva.md`) se o gargalo está mesmo na campanha ou em outro ponto do funil (atendimento, preço, disponibilidade). Trocar criativo não resolve tempo de resposta lento; ajustar preço não resolve criativo fraco.

## Quando manter a campanha

- Taxa de avanço no funil (qualificação, orçamento, reserva) estável ou em melhora ao longo de mais de um período de análise.
- Métricas de topo (CPM, CTR) dentro do esperado para o público e formato.
- Ainda dentro do período mínimo de aprendizado do algoritmo (normalmente os primeiros dias de uma campanha/conjunto novo) — decisões precipitadas nessa fase tendem a interromper o aprendizado antes de ele estabilizar.

## Quando pausar

- Investimento consistente sem nenhuma conversa qualificada por um período razoável (mais de poucos dias, com volume de investimento suficiente para o algoritmo ter aprendido) — nunca pausar após 1-2 dias isolados só por ansiedade de curto prazo.
- Custo por conversa/CPA subindo de forma consistente ao longo de várias semanas, sem sinal de estabilização.
- Oferta da campanha ficou desatualizada (ex.: pacote de feriado encerrado) e não há nova oferta aprovada para substituir.
- Erro identificado na campanha (produto errado, dado incorreto, promessa que a operação não confirma) — pausar imediatamente até corrigir, independente de métrica.

## Quando ajustar público

- Leads chegando fora do perfil-alvo de forma recorrente (grupo maior que a capacidade, pedido de evento/festa, pergunta claramente fora do que o produto oferece).
- Frequência alta (mesmo público vendo o anúncio muitas vezes) sem geração de novo lead — sinal de que o público já foi "esgotado" para aquele criativo.
- Alta parcela de leads "sensível a preço" ou sem intenção real — pode indicar público frio demais ou mal segmentado (ver `analise-criativos-publicos.md`).

## Quando trocar criativo

- CTR caindo de forma consistente com frequência subindo (fadiga de criativo).
- Criativo com bom CTR mas conversa de baixa qualidade — a imagem/vídeo pode estar prometendo algo diferente do que a copy/oferta real entrega.
- Criativo genérico demais ou desatualizado frente ao que já existe de material real (ver `villa-aragua-creative-design-ads`).

## Quando trocar copy

- CTR baixo com criativo visualmente forte — o texto pode não estar comunicando o diferencial certo.
- Copy gerando expectativa que não corresponde à conversa real no WhatsApp (desencontro entre anúncio e atendimento).
- Objeção recorrente que poderia ser antecipada/neutralizada já na copy (ver `villa-aragua-copywriting-conversion/references/provas-objeções.md`).

## Quando subir orçamento (escalar)

Só escalar com evidência mínima acumulada — nunca escalar por um resultado bom isolado de 1-2 dias. Evidência mínima razoável:
- Mais de um período de análise (ex.: 2 semanas) com taxa de avanço no funil consistente ou em melhora.
- CPA (quando calculável) dentro de uma margem que o negócio suporta, considerando a diária e o custo variável do produto (ver `villa-aragua-pricing-revenue`).
- Capacidade operacional real para atender o volume adicional de leads/reservas gerado (ver `ponto-equilibrio-abertura.md` — a campanha não deve gerar demanda maior do que a operação consegue atender com segurança).

## Quando reduzir orçamento

- Investimento gerando leads acima da capacidade de resposta em tempo hábil (tempo médio de resposta subindo por sobrecarga).
- Baixa temporada ou período com ocupação já suficiente, onde o marginal de mais investimento não compensa (ver `villa-aragua-pricing-revenue/references/calendario-sazonalidade.md` e `ponto-equilibrio-abertura.md`).
- Resultado consistentemente abaixo do esperado sem resposta a ajustes de público/criativo/copy já testados.

## Quando criar remarketing

- Volume suficiente de pessoas que engajaram, clicaram ou iniciaram conversa sem fechar (base mínima para o remarketing ter alcance relevante).
- Existência de oferta ou prova social nova para reforçar com esse público (evitar repetir o mesmo anúncio de topo de funil para quem já conhece a marca).
- Quando o setup já validado (`SETUP_INICIAL_META_ADS_7_SETEMBRO_VILLA_ARAGUA_2026.md`) prevê ativar remarketing só a partir do momento em que há público engajado suficiente — não ativar remarketing antes de existir base para isso.

## Quando revisar preço/oferta

- Objeção de preço aparecendo com frequência incomum, mesmo com leads qualificados e dentro do perfil.
- Taxa de fechamento (orçamento enviado → reserva) caindo sem outra explicação aparente no funil.
- Sempre encaminhar essa decisão para `villa-aragua-pricing-revenue` — esta skill identifica o sintoma (objeção de preço, queda na taxa de fechamento), não decide o novo valor.

## Quando revisar o atendimento da Recepcionista IA

- Tempo médio de resposta acima do esperado.
- Queda na taxa de qualificação (leads respondidos que não avançam para qualificação) — pode indicar abordagem inicial fraca, não campanha ruim.
- Objeção recorrente sem resposta eficaz documentada — encaminhar para `villa-aragua-sales-receptionist` revisar o roteiro/objeção.
- Desencontro identificado entre o que o anúncio promete e o que a conversa confirma — sinal de que campanha e atendimento estão dessincronizados.

## Como usar este arquivo na prática

1. Partir do gargalo identificado em `funil-whatsapp-reserva.md` e `analise-criativos-publicos.md`.
2. Verificar qual critério desta lista se aplica — nunca decidir por impressão isolada de um dia.
3. Formular a recomendação como ação clara (manter, pausar, ajustar público, trocar criativo, trocar copy, subir orçamento, reduzir orçamento, criar remarketing, revisar preço, revisar atendimento).
4. Encaminhar a execução para a skill correspondente — esta skill nunca decide preço final nem reescreve peça sozinha.
