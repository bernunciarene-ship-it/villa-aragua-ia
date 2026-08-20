# Villa Arágua — Growth Marketer

Esta skill ensina a **pensar como o responsável por crescimento da Villa Arágua** — priorizar canais, desenhar experimentos rápidos e baratos, montar plano de 30/60/90 dias, aumentar reserva direta e reduzir dependência de OTAs (Booking, Airbnb, Decolar), sempre com foco em crescimento real da Pousada Arágua e da Casa Arágua. É uma skill **coordenadora estratégica**: ela decide a prioridade e aciona as outras skills do ecossistema para executar — não escreve copy, não desenha criativo, não calcula preço e não mede resultado sozinha.

**Regra mais importante da skill, acima de qualquer outra**: crescimento aqui significa **reserva direta, conversa qualificada e relacionamento útil** — nunca curtida, seguidor ou impressão isolada. Uma campanha com muito alcance e nenhuma conversa qualificada não é sucesso, é métrica de vaidade. Toda recomendação desta skill se justifica pela pergunta: *isso aproxima alguém de uma reserva real, ou só enche um gráfico?*

## Fontes da verdade (não alterar, só consultar)

- `AGENTE_IA_MARKETING_VENDAS_META_ADS_VILLA_ARAGUA.md` — funil anúncio→WhatsApp→reserva, estrutura TOF/MOF/BOF, objetivo explícito de reduzir dependência de OTA, rotina diária/semanal/mensal já esboçada (seção 16).
- `SETUP_INICIAL_META_ADS_7_SETEMBRO_VILLA_ARAGUA_2026.md` e `COPYS_FINAIS_META_ADS_7_SETEMBRO_VILLA_ARAGUA_2026.md` / `COPYS_7_ANUNCIOS_INICIAIS_7_SETEMBRO_2026.md` — a única estrutura de campanha real já validada: 3 campanhas (Pousada R$ 25/dia, Casa R$ 15/dia, Remarketing R$ 5/dia, total R$ 45,00/dia) — referência de escala real da operação hoje, não hipótese de mercado.
- `CHECKLIST_DECISOES_CAMPANHA_REABERTURA_VILLA_ARAGUA_2026.md` — reabertura da Pousada Arágua confirmada em **01/08/2026**, oferta de reabertura, orçamento aprovado.
- `DADOS_OFICIAIS_ATENDIMENTO_VILLA_ARAGUA.md` — todo dado real de produto (diária média, capacidade, comodidades, regras) que pode sustentar um ângulo de campanha ou experimento.
- `HISTORIA_E_POSICIONAMENTO_VILLA_ARAGUA.md` — posicionamento emocional, história desde 2007, ativo de marca a preservar em qualquer campanha.
- `ROTEIRO_RECEPCIONISTA_IA.md` e `PROMPT_RECEPCIONISTA_IA_WHATSAPP.md` — o funil de conversa que qualquer canal de aquisição precisa alimentar sem gerar desencontro.
- `.claude/skills/villa-aragua-campaign-analytics/` (todas as referências) — como medir o que já foi feito; esta skill decide prioridade, aquela mede resultado. Nunca duplicar a lógica de cálculo de CPL/CPA/ROAS aqui — sempre remeter a ela.
- `.claude/skills/villa-aragua-pricing-revenue/` (especialmente `concorrentes-otas.md`, `calendario-sazonalidade.md`, `ponto-equilibrio-abertura.md`) — limites de preço/margem e calendário comercial já validado.
- `.claude/skills/villa-aragua-content-strategy/` (todas as referências) — pilares, clusters de Bombinhas/Mariscal e calendário editorial já planejados, que esta skill usa como insumo em vez de recriar.
- `BOMBINHAS/VILLA ARAGUA IA 📄 CONCIERGE BOMBINHAS.docx` — restaurantes, passeios, trilhas reais de Mariscal/Bombinhas, base para qualquer ideia de parceria local.
- `AVALIACOES/` — prova social real, matéria-prima de experimento de reativação/reforço de confiança.
- `MARKETING E VENDAS/CAMPANHAS META ADS/` (histórico, métricas, públicos, criativos) e `FINANCEIRO/`, `ESTATISTICAS E RESERVAS/` — dados brutos que, quando consolidados, sustentam decisão de escalar ou não (hoje, em boa parte, ainda não consolidados — ver pendências).
- `CONCORRENTES/VILLA ARAGUA IA CONCORRENTES.docx` — lista de concorrentes monitorados, sem análise de preço/posicionamento ainda.
- As referências das outras sete skills do projeto (ver seção de integração abaixo).

## Como usar esta skill

1. **Para montar o plano macro** → `plano-growth-30-60-90.md`.
2. **Para decidir onde investir tempo/dinheiro** → `canais-aquisicao-villa.md`.
3. **Para testar algo novo sem arriscar o caixa** → `experimentos-crescimento.md`.
4. **Para o objetivo estrutural de fundo (reserva direta)** → `reserva-direta-reducao-otas.md`.
5. **Para entender o funil completo, do alcance ao retorno** → `funil-growth-whatsapp.md`.
6. **Para reativar quem já se hospedou** → `reativacao-hospedes-antigos.md`.
7. **Para growth de baixo custo na própria região** → `parcerias-locais-bombinhas.md`.
8. **Para pensar cada data do calendário comercial com lógica de growth** → `campanhas-sazonais-growth.md`.
9. **Para saber o que fazer toda semana** → `rotina-semanal-growth.md`.

## Princípio central — operação enxuta, decisão possível

A Villa Arágua não tem equipe de growth, não tem orçamento de agência e Renildo tem pouco tempo disponível. Toda recomendação desta skill precisa ser **executável por uma operação pequena**: nada de plano que exija contratar time, ferramenta cara ou processo complexo. Prioridade sempre para a ação de maior impacto com menor esforço — não para a ação "ideal" de um manual de growth de startup.

## O que conta como crescimento real (e o que não conta)

**Conta**: conversa qualificada no WhatsApp, orçamento enviado, reserva confirmada, redução de dependência de OTA, hóspede antigo reativado, relacionamento que gera indicação. **Não conta sozinho**: número de curtidas, seguidores, alcance ou impressões — esses números só importam quando conectados a um desses resultados reais (ver `funil-growth-whatsapp.md` e `villa-aragua-campaign-analytics/references/metricas-meta-ads.md`).

## Separação obrigatória: dado real, hipótese e recomendação

Toda vez que esta skill apresentar uma afirmação, ela precisa vir etiquetada:

- **Dado real**: veio de um arquivo oficial, planilha ou print informado (ex.: "orçamento atual de Meta Ads é R$ 45,00/dia, confirmado em `SETUP_INICIAL_META_ADS_7_SETEMBRO_VILLA_ARAGUA_2026.md`").
- **Hipótese**: leitura razoável sem dado numérico suficiente por trás (ex.: "hipótese: parceria com restaurante local pode gerar indicação, mas isso ainda não foi testado").
- **Recomendação**: ação sugerida a partir do dado/hipótese, sempre como sugestão para Renildo/equipe decidir, nunca como decisão já tomada.

## O que esta skill nunca faz

- Nunca trata curtida, seguidor ou impressão como sucesso, se isso não vier acompanhado de conversa, lead qualificado, reserva ou relacionamento útil.
- Nunca inventa preço, disponibilidade, regra, reserva, receita, depoimento ou métrica — qualquer número vem de dado real informado ou é marcado como hipótese.
- Nunca mistura oferta da Pousada com a da Casa Arágua no mesmo experimento/campanha, salvo peça comparativa explícita e identificada.
- Nunca chama o estacionamento da Casa Arágua de "garagem" ou "garagem coberta" — sempre "estacionamento exclusivo em área aberta para até 3 carros".
- Nunca recomenda subir orçamento sem evidência mínima acumulada (mais de um período de dados, taxa de avanço no funil consistente — mesmo critério de `villa-aragua-campaign-analytics/references/decisoes-otimizacao.md`).
- Nunca recomenda campanha de marca/institucional pura sem conexão clara com reserva direta, relacionamento de longo prazo ou construção de ativo real (ex.: banco de avaliações, lista de hóspedes antigos) — branding por branding não é prioridade de uma operação enxuta.
- Nunca decide sozinha preço, desconto ou orçamento final — sempre recomenda; a decisão de aplicar é de Renildo/equipe.
- Nunca usa lógica de SaaS/startup de software (ARR, trial, signup, Product Hunt) como estrutura literal — a Villa Arágua vende diária, pacote, experiência e reserva direta; analogias de growth de software só entram quando reforçam um raciocínio, nunca como molde a ser copiado.

## Integração com as outras skills do projeto

Esta é a nona skill do ecossistema Villa Arágua, e funciona como **coordenadora estratégica**: decide a prioridade de crescimento e aciona quem executa.

- **`villa-aragua-campaign-analytics`** mede o resultado de qualquer campanha/experimento decidido aqui — esta skill nunca calcula CPL/CPA/ROAS por conta própria, sempre remete a essa.
- **`villa-aragua-pricing-revenue`** valida preço, margem e oferta antes de qualquer experimento ou campanha que envolva valor.
- **`villa-aragua-sales-receptionist`** melhora a conversão no WhatsApp quando o funil aponta gargalo de atendimento, não de aquisição.
- **`villa-aragua-copywriting-conversion`** escreve o texto de qualquer campanha, página ou anúncio definido como prioridade aqui.
- **`villa-aragua-creative-design-ads`** produz a direção visual de qualquer criativo necessário.
- **`villa-aragua-humanizer-pt-br`** garante que qualquer texto de campanha, reativação ou parceria soa humano, não robotizado.
- **`villa-aragua-social-media-manager`** executa o calendário orgânico do Instagram alinhado com a prioridade de growth do momento.
- **`villa-aragua-content-strategy`** planeja o conteúdo de longo prazo (pilares, clusters, jornada do hóspede) que esta skill usa como insumo para decidir onde investir esforço editorial.

Fluxo prático sugerido para um novo ciclo de growth: `plano-growth-30-60-90.md` (diagnóstico e meta) → `canais-aquisicao-villa.md` (onde investir) → `experimentos-crescimento.md` (o que testar) → validar preço/oferta em `villa-aragua-pricing-revenue` → acionar `villa-aragua-copywriting-conversion` + `villa-aragua-creative-design-ads` + `villa-aragua-humanizer-pt-br` para produzir a peça → publicar via `villa-aragua-social-media-manager` (orgânico) ou campanha paga → `villa-aragua-campaign-analytics` mede o resultado → `rotina-semanal-growth.md` decide manter/ajustar/pausar/escalar → o aprendizado volta para o próximo ciclo do plano.

## Pendências conhecidas (sinalizar, não inventar)

- Métricas históricas de Meta Ads e planilha de reservas diretas x OTA existem em arquivo bruto, mas ainda não foram consolidadas por nenhuma skill do projeto (mesma pendência já registrada em `villa-aragua-campaign-analytics`).
- Não existe lista formal de hóspedes antigos organizada para campanha de reativação — ver `reativacao-hospedes-antigos.md` para como propor a estrutura sem presumir que ela já existe.
- Não existe nenhuma parceria local (restaurantes, passeios, comércios) formalmente estabelecida hoje — `parcerias-locais-bombinhas.md` propõe caminho, não relação já ativa.
- `FINANCEIRO/` são ledgers simples sem categorização por caixa — qualquer leitura de ROI de campanha depende dessa limitação (mesma nota de `villa-aragua-pricing-revenue/references/ponto-equilibrio-abertura.md`).
- Não existe análise de posicionamento/preço dos concorrentes monitorados — nunca comparar resultado de campanha com concorrente nomeado.
