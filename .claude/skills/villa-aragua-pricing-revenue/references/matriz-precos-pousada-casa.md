# Matriz de preços — Pousada Arágua x Casa Arágua

Regra central: **todo valor citado precisa ser classificado mentalmente em uma destas quatro categorias antes de ser comunicado.** Nunca comunicar um valor sem saber em qual categoria ele está.

| Categoria | O que significa | Quem autoriza |
|---|---|---|
| **Preço aprovado** | Valor já confirmado por Renildo, documentado como oficial (ex.: diária média, taxa de limpeza, pacote de feriado já decidido) | Já autorizado — pode ser comunicado como está documentado |
| **Preço sugerido** | Estimativa de posicionamento (ex.: "a partir de", com base na diária média) quando ainda não há tarifa exata para aquele período específico | Pode ser usado como referência de conversa, nunca como valor fechado |
| **Preço mínimo aceitável** | Piso abaixo do qual não se deve vender sem escalar — protege margem e ponto de equilíbrio (ver `ponto-equilibrio-abertura.md`) | Não existe piso oficial documentado por acomodação — até que exista, qualquer valor abaixo da diária média conhecida deve ser tratado como "precisa de aprovação", nunca decidido sozinho |
| **Condição que precisa de autorização** | Qualquer desconto, parcelamento, pacote fora do já aprovado, redução de diárias, exceção operacional | Sempre Renildo/equipe — nunca a IA sozinha |

## Pousada Arágua

- **Diária média de referência (preço aprovado)**: R$ 500,00 — confirmado por Renildo em 2026-07-07, "não diferenciada ainda por baixa/alta/feriado". Usar como posicionamento ("a partir de"), nunca como tarifa fixa para qualquer data sem checagem real.
- **Diária por temporada (baixa/alta/feriado específico)**: publicada no Stays para ago/2026–abr/2027, transcrita em `tarifas-publicadas-2026-2027.md` — tratar como "preço publicado a confirmar", não como preço aprovado, até checagem direta no sistema. Fora dessa janela, segue **a definir**. Não inventar uma diária "de alta temporada" para período não coberto pelo inventário.
- **Café da manhã**: sempre incluso, servido na acomodação (8h–10h). Não é opcional na Pousada.
- **Estacionamento**: 1 vaga gratuita e identificada por acomodação, dentro da pousada — não é vaga extra, não é coberta.
- **Mínimo de diárias**: sem regra fixa fora de campanhas específicas — o pacote de 7 de Setembro tem mínimo de 4 diárias (ver `pacotes-feriados.md`); fora dele, mínimo de diárias por temporada segue "a definir".
- **Enxoval extra e reposição** (valores confirmados, uso quando o hóspede solicitar): jogo de cama R$ 30,00; toalha de banho R$ 15,00; toalha de rosto R$ 10,00; tapete de piso R$ 10,00. Troca completa por acomodação: Terra/Wood/Organic/Fuego/Metallo R$ 150,00; Acqua/Luna R$ 180,00; Soleil R$ 220,00. A IA pode informar esses valores, mas **não pode conceder cortesia, desconto ou isenção sozinha**.
- **Suítes e apartamentos**: cada unidade tem capacidade própria (Terra 3 · Acqua 4 · Wood 3 · Fuego 3 · Metallo 3 · Organic 2 · Luna 4 · Soleil 5).

### Régua percentual interna da Pousada Arágua — `REGRA_APROVADA_RENILDO` (2026-07-25)

Uso interno de Revenue — nunca citar estes multiplicadores ou percentuais ao hóspede. Para o hóspede, a resposta continua sendo a mesma de sempre: cada acomodação tem características diferentes, não "categoria X% mais cara que Y" (ver `comunicacao-preco-whatsapp.md`).

Esta regra define a hierarquia matemática da Pousada Arágua para **análises futuras** de precificação. Ela **não altera automaticamente** nenhuma tarifa já publicada — qualquer ajuste real no motor de reserva continua dependendo de decisão humana e aplicação manual por Renildo.

| Acomodação | Multiplicador sobre a base | Quando vale |
|---|---|---|
| Organic / Fuego / Metallo | base × 1,00 (100%) | sempre — é a própria base |
| Terra / Wood | base × 1,15 | sempre |
| Acqua | base × 1,25 | sempre |
| Luna | base × 1,32 | sempre |
| Duplex Soleil | base × 1,63 | média temporada, alta temporada, feriados, datas especiais, Natal, Réveillon, janeiro, Carnaval, Páscoa |
| Duplex Soleil (exceção comercial) | base × 1,50 | baixa temporada pura: **maio, junho, agosto** e outros períodos fracos definidos por Renildo — reduz para melhorar conversão sem quebrar a hierarquia |

**Correção registrada:** a referência anterior de Terra/Wood como "+12%" estava incorreta — o padrão correto e aprovado é **+15%**.

**Validação cruzada com o inventário publicado (`INVENTARIO_TARIFAS_PUBLICADAS_AGO2026_ABR2027.csv`):** ao recalcular a razão entre cada grupo e a base (Organic/Fuego/Metallo) em todos os 18 períodos do inventário, os multiplicadores batem com a régua acima (Terra/Wood ≈1,15 · Acqua ≈1,25 · Luna ≈1,32 · Duplex ≈1,63) em praticamente todos os períodos, incluindo Agosto/2026, Março/2027 e Abril/2027. Isso indica que **a exceção de 1,50 no Duplex Soleil ainda não foi aplicada em nenhuma tarifa publicada até agora** — está disponível como ferramenta, mas nenhuma decisão registrada em `DECISOES_REVENUE_PENDENTES_VILLA_ARAGUA.md` a usou ainda.

**Oportunidade a considerar (não é erro, não corrigir sozinho):** Agosto/2026 é explicitamente classificado como baixa temporada pura pela regra aprovada, elegível ao multiplicador 1,50 do Duplex Soleil (399 × 1,50 = R$ 598,50). A tarifa hoje publicada para Agosto/2026 usa o multiplicador 1,63 (R$ 650) — dentro da regra, já que a exceção é opcional ("pode ter multiplicador reduzido para melhorar conversão", não obrigatório). Sinalizar a Renildo como opção disponível para maio, junho e agosto, nunca aplicar automaticamente.

**Ponto fora da régua a checar com Renildo:** Suíte Acqua em Dezembro/2026 (dias 1–18) está em R$ 768 — pela régua (base R$ 629 × 1,25), o valor esperado seria R$ 786. Diferença de R$ 18 (~2,3% abaixo do padrão). Não corrigir sozinho; sinalizar como possível inconsistência pontual.

Se o hóspede perguntar se uma suíte específica é mais cara/barata que outra, a resposta ao hóspede não usa esta régua — ver item 27 de `DADOS_OFICIAIS_ATENDIMENTO_VILLA_ARAGUA.md`: Terra e Wood podem ser citadas como *tendência relativa* de custo-benefício, nunca como afirmação absoluta ou percentual exato.

## Casa Arágua

- **Diária média de referência (preço aprovado)**: R$ 990,00 — confirmado por Renildo em 2026-07-07, "não diferenciada ainda por baixa/alta/feriado".
- **Diária por temporada**: publicada no Stays para ago/2026–abr/2027 (mesma observação da Pousada acima). **Atenção:** o diagnóstico de `DIAGNOSTICO_PRELIMINAR_REVENUE_VILLA_ARAGUA.md` aponta que, em várias datas fortes (Réveillon 2026, janeiro e Carnaval 2027), a diária publicada da Casa está abaixo ou quase igual à do Duplex Soleil — não tratar isso como posicionamento correto sem checar o diagnóstico antes de comunicar.
- **Mínimo de diárias**: 4 diárias (confirmado para o período de 7 de Setembro; tratar como referência geral da Casa até indicação em contrário).
- **Café da manhã**: **não oferecido em nenhuma condição** — não incluso, não sob consulta, não como adicional pago (regra atualizada 2026-08-07, revoga o valor anterior de R$ 80,00/pessoa). Nunca prometer, sugerir, cotar ou verificar café da manhã para a Casa.
- **Taxa de limpeza final**: **R$ 450,00 por estadia** (preço aprovado, obrigatória, cobrada à parte — aplicável a todas as reservas da Casa). Não confundir com limpeza durante a estadia (que não existe como serviço padrão).
- **Limpeza extra durante a estadia**: R$ 350,00 por limpeza, sob consulta, sujeita à disponibilidade da equipe — não é garantida automaticamente.
- **Estacionamento**: exclusivo e gratuito, até 3 carros, área aberta — **nunca dizer "garagem coberta"**.
- **Capacidade máxima**: até 6 pessoas — grupos maiores não cabem na Casa; nesse caso, avaliar combinação com acomodações da Pousada.

## Diferença de diária Pousada x Casa — como explicar

A Casa custa mais por diária (R$ 990,00 vs R$ 500,00 de referência) porque vende um produto diferente, não porque é "a versão cara da Pousada":

- Piscina **privativa** (Casa) vs piscina de área comum (Pousada).
- Casa completa e exclusiva para o grupo vs suíte dentro de uma pousada com outros hóspedes circulando.
- Estacionamento exclusivo para até 3 carros (Casa) vs 1 vaga por acomodação (Pousada).
- Em compensação, a Pousada inclui café da manhã todos os dias sem custo extra; a Casa não oferece café da manhã em nenhuma condição e tem taxa de limpeza obrigatória — o pacote de valor é diferente, não é "Casa = Pousada mais cara".

## Regra de canais (decidida e aplicada em 2026-07-25)

Markup sobre o motor (Stays), válido para Pousada e Casa:

| Canal | Regra |
|---|---|
| Booking | motor **+25%** |
| Decolar | motor **+17,6%** |
| Airbnb | motor **+17,6%** |

Fonte: `DECISOES_REVENUE_PENDENTES_VILLA_ARAGUA.md`, seção "Regra de canais". Usar sempre que for necessário comparar ou explicar diferença de preço entre canais — nunca inventar um percentual diferente. Fórmulas de conversão OTA↔motor e a metodologia completa do Radar de Concorrência estão em `REGRAS_CONVERSAO_OTA_MOTOR_REVENUE.md` (raiz do projeto).

## Regra Casa Arágua x Duplex Soleil — status atualizado em 2026-07-25

A hipótese "em data forte, Casa Arágua deve valer mais que o Duplex Soleil" (`DIAGNOSTICO_PRELIMINAR_REVENUE_VILLA_ARAGUA.md`) foi **parcialmente validada por decisão humana concreta**: no Carnaval 2027 e em janeiro/2027 (a partir de 07/01), Renildo decidiu e aplicou Casa Arágua em R$ 1.890, acima do Duplex Soleil nas mesmas datas (ver `DECISOES_REVENUE_PENDENTES_VILLA_ARAGUA.md`, cards 2 e 3). Isso ainda não é uma regra geral aprovada para toda data forte — cada período segue precisando de decisão própria.

## Regra de ouro — nunca misturar as duas matrizes

- Pacote, diária ou condição aprovada para um produto **nunca** se aplica automaticamente ao outro. Exemplo real: o pacote de R$ 1.997,00/4 diárias é exclusivo da Pousada Arágua — a Casa Arágua fica fora dessa oferta por decisão explícita de Renildo (2026-07-07).
- Antes de citar qualquer valor, perguntar internamente: "isso é da Pousada ou da Casa?" — e nunca responder com o valor do outro produto.
- Adultos e crianças: crianças até 6 anos são gratuitas em ambos os produtos — sempre confirmar idade, número de pessoas e datas antes de aplicar isso a um orçamento, respeitando a capacidade máxima de cada acomodação/da Casa.
