# Villa Arágua — Pricing & Revenue Strategy

Esta skill ensina a pensar **como um gerente de receita/hotelaria** para a Pousada Arágua e a Casa Arágua — estratégia de preço, pacotes, descontos, sazonalidade, concorrência e ponto de equilíbrio de abertura. Ela não substitui os arquivos oficiais do projeto; ela ensina como usá-los na prática ao analisar preço, montar pacote, avaliar desconto ou decidir se vale abrir uma data.

Esta skill é a contraparte estratégica da skill `villa-aragua-sales-receptionist` (que ensina **como vender** no WhatsApp). Esta aqui ensina **quanto cobrar, quando ajustar e o que proteger** antes que qualquer valor chegue ao hóspede.

## Fontes da verdade (não alterar, só consultar)

Sempre que houver dúvida ou conflito, estes arquivos têm prioridade sobre qualquer resumo desta skill:

- `DADOS_OFICIAIS_ATENDIMENTO_VILLA_ARAGUA.md` — dados validados de atendimento, incluindo taxas, café, enxoval, pagamento (itens 1–70).
- `CHECKLIST_DECISOES_CAMPANHA_REABERTURA_VILLA_ARAGUA_2026.md` — decisões mais recentes de tarifa, pacote, orçamento e datas (atualizado em 2026-07-07, é a fonte mais atual sobre preço).
- `REVENUE MANAGER/VILLA ARAGUA 📄 REVENUE MANAGER VILLA ARÁGUA.docx` — lógica de quando subir, manter ou reduzir preço.
- `AGENTE_IA_MARKETING_VENDAS_META_ADS_VILLA_ARAGUA.md` e `PLANO_CAMPANHA_REABERTURA_VILLA_ARAGUA_2026.md` — papel comercial da IA, estrutura de campanha, limites do que pode/não pode decidir.
- `COPYS_FINAIS_META_ADS_7_SETEMBRO_VILLA_ARAGUA_2026.md`, `SETUP_INICIAL_META_ADS_7_SETEMBRO_VILLA_ARAGUA_2026.md`, `MATRIZ_ANUNCIOS_FINAIS_7_SETEMBRO_VILLA_ARAGUA_2026.md`, `ESTRUTURA_CAMPANHA_META_ADS_7_SETEMBRO_VILLA_ARAGUA_2026.md`, `COPYS_7_ANUNCIOS_INICIAIS_7_SETEMBRO_2026.md` — exemplos reais já aprovados de pacote e comunicação de preço.
- `CONCORRENTES/VILLA ARAGUA IA CONCORRENTES.docx` — lista de concorrentes monitorados (hoje sem análise de preço).
- `FINANCEIRO/` — ledgers de custo/receita (simples, não categorizados por caixa — ver `ponto-equilibrio-abertura.md`).
- `CLAUDE.md` (raiz do projeto) — seção Revenue Manager e regra de separação financeira (DNA, seção 13).
- `INVENTARIO_TARIFAS_PUBLICADAS_AGO2026_ABR2027.md`/`.csv` e `DIAGNOSTICO_PRELIMINAR_REVENUE_VILLA_ARAGUA.md` (raiz do projeto) — tarifas publicadas ago/2026–abr/2027, transcritas de prints, com diagnóstico de manter/corrigir/revisar/proteger. Ver resumo em `tarifas-publicadas-2026-2027.md`.
- `DECISOES_REVENUE_PENDENTES_VILLA_ARAGUA.md` (raiz do projeto) — decisões humanas já tomadas e aplicadas sobre o diagnóstico acima (Páscoa 2027, Carnaval 2027, Casa Arágua jan/2027 e set-out/2026, regra de canais). É a fonte mais atual sempre que houver conflito com o inventário/diagnóstico originais.
- `CESTA_COMPETITIVA_REVENUE_VILLA_ARAGUA.md`, `COLETAS_CONCORRENCIA_REVENUE.csv`, `REGRAS_CONVERSAO_OTA_MOTOR_REVENUE.md` e `ALERTAS_CONCORRENCIA_REVENUE.md` (raiz do projeto) — Radar de Concorrência Revenue: cadastro de concorrentes, log de coleta manual, fórmulas OTA↔motor e modelo de alerta. Status `EM_IMPLANTACAO_MANUAL_ASSISTIDA`, ainda sem coleta real preenchida.

Se um desses arquivos for atualizado (nova decisão de Renildo, nova rodada de tarifas), esta skill deve ser revisada — ela é um resumo prático, não uma cópia congelada.

## Como usar esta skill

1. **Identificar o produto e a data** → `matriz-precos-pousada-casa.md` (qual produto, quais valores já aprovados) e `calendario-sazonalidade.md` (em qual temporada/feriado a data cai). Para o período agosto/2026–abril/2027, há tarifa publicada por período em `tarifas-publicadas-2026-2027.md` — tratar como preço a confirmar, não como preço aprovado.
2. **Se for feriado com pacote** → `pacotes-feriados.md` para estrutura, valores e o que nunca misturar entre Pousada e Casa.
3. **Se houver pedido de desconto/condição especial** → `regras-desconto.md` — quando considerar, quando recusar, quando escalar.
4. **Se envolver comparação com concorrente ou OTA** → `concorrentes-otas.md` para o contexto, e o Radar de Concorrência Revenue (`CESTA_COMPETITIVA_REVENUE_VILLA_ARAGUA.md`, `COLETAS_CONCORRENCIA_REVENUE.csv`, `REGRAS_CONVERSAO_OTA_MOTOR_REVENUE.md`, `ALERTAS_CONCORRENCIA_REVENUE.md`) para o método e o dado coletado. Nunca comparar preço de motor da Villa direto com preço visível de OTA de concorrente sem aplicar a conversão de `REGRAS_CONVERSAO_OTA_MOTOR_REVENUE.md`.
5. **Se a pergunta for sobre abrir ou não uma data/período** → `ponto-equilibrio-abertura.md` — lógica de custo fixo/variável e ocupação mínima.
6. **Ao escrever a resposta final para o hóspede** → `comunicacao-preco-whatsapp.md` para o tom e os modelos certos por situação.

## Princípio central — separar sempre as quatro categorias de preço

Antes de comunicar qualquer valor, classificar mentalmente:

| Categoria | Definição | Exemplo |
|---|---|---|
| **Preço aprovado** | Já confirmado por Renildo e documentado como oficial | Diária média Pousada R$ 500,00; Casa R$ 990,00; taxa de limpeza R$ 450,00; pacote 7/Set R$ 1.997,00/4 diárias |
| **Preço sugerido** | Estimativa de posicionamento quando não há tarifa exata para o período | "A partir de R$ 500,00", usado até confirmar disponibilidade real da data |
| **Preço mínimo aceitável** | Piso de proteção de margem — hoje não há piso oficial documentado por acomodação; até existir, tratar qualquer valor abaixo da diária média como "precisa de aprovação" | — |
| **Condição que precisa de autorização** | Desconto, parcelamento, pacote novo, redução de diárias, exceção operacional | Qualquer coisa fora do já listado como preço aprovado |

A IA **apoia** a decisão de preço — ela não decide desconto, tarifa nova ou exceção sozinha. Essa é a mesma regra já usada na Recepcionista IA, estendida para toda a estratégia de receita.

## Regras de segurança comercial (checagem final antes de qualquer análise, copy ou resposta)

**Nunca**:
- inventar preço, disponibilidade, desconto ou condição comercial não documentada;
- prometer desconto ou parcelamento sem o acréscimo oficial de 7%; citar o percentual de 7% ao hóspede; oferecer parcelamento fora da tabela de faixas por valor (`DADOS_OFICIAIS_ATENDIMENTO_VILLA_ARAGUA.md`, item 51 — teto absoluto 6x, sem opção de 10x);
- prometer early check-in ou late check-out (sob consulta, sem valor fixo oficial);
- misturar pacote, tarifa ou condição da Pousada com a da Casa Arágua;
- ignorar a taxa de limpeza da Casa Arágua (R$ 450,00) ao apresentar valor da Casa;
- chamar o estacionamento da Casa Arágua de "garagem coberta" (é área aberta, exclusiva, até 3 carros);
- confirmar pet fora da regra oficial sem checar `DADOS_OFICIAIS_ATENDIMENTO_VILLA_ARAGUA.md`;
- criar urgência falsa sobre disponibilidade ou preço para pressionar fechamento;
- afirmar comparação de preço com concorrente específico sem dado real checado (ver `concorrentes-otas.md`);
- tratar uma pendência ("a definir" nos arquivos-fonte) como se fosse decisão tomada — isso vale especialmente para diárias por temporada, datas prioritárias além de 7 de Setembro, e análise de concorrentes.

**Sempre**:
- sinalizar explicitamente quando uma condição depende de aprovação do gestor (Renildo/equipe);
- diferenciar Pousada Arágua e Casa Arágua em qualquer análise ou copy comercial;
- basear qualquer sugestão de preço/pacote novo na diária média já aprovada, deixando claro que é proposta, não tarifa publicada;
- considerar o contexto atual da operação (reabertura em 01/08/2026, campanha ativa, orçamento de Meta Ads R$ 45,00/dia) ao pensar em prioridades de venda.

## Como usar em conjunto com a skill `villa-aragua-sales-receptionist`

As duas skills resolvem perguntas diferentes e se complementam:

- **`villa-aragua-sales-receptionist`** ensina *como conduzir a conversa* com o hóspede — diagnóstico do lead, tom de voz, condução até a reserva, follow-up.
- **`villa-aragua-pricing-revenue`** (esta skill) ensina *quanto cobrar e por quê* — de onde vem o valor que a Recepcionista IA comunica, quando um desconto pode ser considerado, se vale abrir uma data, como se posicionar frente a concorrentes/OTAs.

Na prática: use `villa-aragua-pricing-revenue` para decidir/validar o valor e a condição comercial, e `villa-aragua-sales-receptionist` (em especial `objecoes-vendas.md` e `respostas-whatsapp.md`) para escrever a mensagem final ao hóspede. Os modelos de mensagem em `comunicacao-preco-whatsapp.md` desta skill são específicos de preço/pacote e devem ser lidos como extensão de `respostas-whatsapp.md`, não como substituto do tom geral já definido na skill de vendas.

## Pendências conhecidas (não tratar como dado oficial)

- Diária diferenciada por baixa/média/alta temporada e por feriado específico — **parcialmente resolvida em 2026-07-24**: existe tarifa publicada no Stays para ago/2026–abr/2027 (ver `tarifas-publicadas-2026-2027.md`), mas ainda não confirmada linha a linha no sistema. Até confirmar, tratar como "publicado", não como "aprovado".
- Casa Arágua com preço abaixo do Duplex Soleil em datas fortes e tarifa de Páscoa 2027 abaixo do mês base — **resolvido em 2026-07-25** para Páscoa, Carnaval, Casa Arágua jan/2027 (a partir de 07/01) e Casa Arágua set/out 2026 base; ver `DECISOES_REVENUE_PENDENTES_VILLA_ARAGUA.md`. Réveillon 2026 e Casa Arágua 01–06/01/2027 seguem como estão — período confirmado reservado, não deve ser alterado.
- Markup de canal (Booking/Decolar/Airbnb sobre o motor) — **resolvido em 2026-07-25**, ver `matriz-precos-pousada-casa.md`, seção "Regra de canais".
- Datas prioritárias de venda além de setembro/7 de Setembro (outubro, novembro, Natal, Réveillon, Carnaval, março) — ainda não priorizadas oficialmente.
- Análise comparativa de preço/posicionamento dos concorrentes monitorados — ainda não existe.
- Consolidação da planilha de reservas diretas x OTAs — ainda não existe.
- Ponto de equilíbrio calculado em R$ — os ledgers financeiros não estão categorizados por caixa; esta skill fornece o método, não o número pronto.

Quando qualquer uma dessas pendências for resolvida nos arquivos-fonte, esta skill deve ser atualizada.
