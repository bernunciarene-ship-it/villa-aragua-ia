# Calendário e sazonalidade

Base para pensar preço e ocupação ao longo do ano. Onde o dado for oficial, está marcado; onde for hipótese/pendência, também está marcado — nunca tratar uma pendência como se fosse tarifa decidida.

## Situação atual (referência: hoje é 2026-07-07)

- A Pousada Arágua está em **campanha de reabertura**, com **data oficial de reabertura em 01/08/2026** (confirmado por Renildo em 2026-07-07, fonte: `CHECKLIST_DECISOES_CAMPANHA_REABERTURA_VILLA_ARAGUA_2026.md`).
- Isso significa que, neste momento, qualquer análise de preço/ocupação precisa considerar que a operação está **retomando**, não em regime normal — a base de comparação histórica (ticket médio, ocupação) é mais frágil até a reabertura estabilizar.
- **7 de Setembro de 2026** é o primeiro feriado oficialmente priorizado para venda, com pacote mínimo de 4 diárias (ver `pacotes-feriados.md`).
- Datas prioritárias além de setembro/7 de setembro (outubro, 12 de outubro, novembro, 20 de novembro, Natal, Réveillon, janeiro, fevereiro, Carnaval, março) **ainda não foram priorizadas oficialmente por Renildo** — estão como "a definir" em `CHECKLIST_DECISOES_CAMPANHA_REABERTURA_VILLA_ARAGUA_2026.md`. Trate como janela relevante (baseado no padrão histórico do Revenue Manager, ver abaixo), nunca como decisão tomada.

## Classificação de temporada (referência conceitual, fonte: `REVENUE MANAGER/...docx` e `CLAUDE.md`)

| Temporada | Meses/padrão | Como pensar preço |
|---|---|---|
| Alta temporada | Setembro a março, feriados nacionais, Réveillon, Carnaval, Dia dos Namorados | Datas prioritárias para revenue management — maior disposição de pagar, maior procura natural |
| Média temporada | Transição entre alta e baixa (ex.: abril, agosto pós-reabertura) | Observar ritmo de reservas antes de decidir se sobe, mantém ou cria oferta |

**Nota de reconciliação (2026-07-25):** esta classificação geral (para campanha/marketing) trata agosto como transição pós-reabertura. Para a régua percentual de preço da Pousada (`REGRA_APROVADA_RENILDO`, ver `matriz-precos-pousada-casa.md`), Renildo classificou especificamente **maio, junho e agosto como baixa temporada pura** — elegíveis ao multiplicador reduzido (1,50) do Duplex Soleil. As duas classificações coexistem para finalidades diferentes: esta tabela orienta tom/prioridade de campanha; a régua de `matriz-precos-pousada-casa.md` orienta o multiplicador de preço do Duplex Soleil.
| Baixa temporada | Demais meses fora do bloco set-mar e fora de feriados | Foco maior em casais; espaço para pacotes/condições, sempre com aprovação — nunca desconto automático |

**Atualização de 2026-07-24:** existe hoje tarifa diferenciada por temporada/feriado publicada no Stays para o período agosto/2026–abril/2027 (ver `tarifas-publicadas-2026-2027.md` e `INVENTARIO_TARIFAS_PUBLICADAS_AGO2026_ABR2027.md`, na raiz do projeto). Ela substitui, para esse período, a diária média flat de R$ 500,00 (Pousada) / R$ 990,00 (Casa) confirmada em 2026-07-07 como referência única. **Ainda assim, trate a tarifa publicada como "a confirmar no sistema", não como "preço aprovado"** — os valores foram transcritos de prints, não extraídos por integração. Para qualquer data fora da janela ago/2026–abr/2027, ou se o inventário não tiver o período exato, a diária média flat continua sendo a única referência disponível, e qualquer diferenciação adicional é **hipótese operacional a validar com Renildo**.

## Datas-chave para observar todo ano

- Férias escolares (janeiro/fevereiro e julho) — maior procura de famílias.
- Natal e Réveillon — alta temporada forte, decisão de preço deve considerar concorrência e ocupação com bastante antecedência.
- Carnaval — alta temporada, data móvel; confirmar todo ano a data exata antes de planejar campanha/pacote.
- Dia dos Namorados (12 de junho) — puxa perfil casal, baixa temporada mas com pico de procura pontual.
- 7 de Setembro — feriado prioritário confirmado para 2026, com pacote específico da Pousada (ver `pacotes-feriados.md`).
- 12 de Outubro e 20 de Novembro — feriados nacionais, ainda sem priorização/tarifa oficial para 2026.
- Campanhas de reabertura/reativação — usadas quando a operação volta de um período fechado ou de baixa atividade comercial (como agora, com reabertura em 01/08/2026); focam em aquecimento, reconexão com hóspedes antigos e geração de conversas, antes de pressionar por conversão imediata.

## Datas em que só vale abrir com ponto de equilíbrio

Nem toda data justifica abrir a operação a pleno custo (equipe, café da manhã, limpeza) se a ocupação prevista for baixa. Regra prática:

- Antes de comprometer recursos (equipe extra, compras, Meta Ads agressivo) para uma data específica, checar se a ocupação projetada cobre o custo operacional mínimo daquele período — ver `ponto-equilibrio-abertura.md`.
- Datas de baixa procura isolada (ex.: meio de semana em baixa temporada) podem justificar operação reduzida, oferta pontual (com aprovação) ou até não abrir uma unidade específica, em vez de operar no vermelho.
- Isso é uma decisão de Renildo/gestão, apoiada por dados — a IA nunca decide sozinha "não vamos abrir" para o hóspede; apenas sinaliza internamente quando os números não fecham.

## Como usar este calendário na prática

1. Antes de responder sobre preço para uma data específica, identificar em qual bloco de temporada ela cai (alta/média/baixa) e se é feriado priorizado.
2. Se a data cair em um feriado/período **não priorizado oficialmente ainda** (ex.: Natal, Réveillon 2026), não inventar tarifa nem pacote — usar a diária média conhecida como referência de posicionamento ("a partir de") e sinalizar que o valor exato depende de checagem com a equipe.
3. Sempre cruzar com `matriz-precos-pousada-casa.md` (qual produto) e `regras-desconto.md` (se houver pedido de condição especial) antes de comunicar qualquer valor.
