# Orçamento contextual — mensagem inicial de orçamento

*Criado em 19/08/2026, aprovado por Renildo. Define a estrutura da **mensagem inicial de orçamento** (o primeiro envio de valor a um lead QL4, ou QL3 quando o orçamento já fizer sentido). Não se aplica a follow-up: FU1, FU2, encerramento leve, cadência e teto de contatos continuam 100% governados por `MATRIZ_FOLLOWUP_QL_WHATSAPP_VILLA_ARAGUA.md`, seção 10 — os dois sistemas convivem, este arquivo não substitui nem reescreve a Matriz.*

## Por que isso existe

Auditoria de 34 orçamentos da campanha 7 de Setembro (19/08/2026) encontrou 32/34 compostos só de produto + valor + parcelamento, sem nenhum ativo visual ou contextual registrado — e taxa de resposta pós-orçamento de 20,6%. A causalidade não foi provada (amostra insuficiente para isso), mas a Villa decidiu testar operacionalmente um formato mais contextual, sem mudar preço, produto ou campanha. Ver `CRM_LEADS_VILLA_ARAGUA.md`, campos de mensuração, para o acompanhamento.

## Estrutura — ordem comercial obrigatória (5 momentos)

Consolidado por decisão de Renildo em 20/08/2026 (reforço do padrão de 19/08). Para o **PRIMEIRO ORÇAMENTO**, quando houver ativo adequado ao perfil:

- **MOMENTO 1 — Acolhimento + recomendação**: recebe bem, contextualiza a viagem/data, recomenda a acomodação/produto principal.
- **MOMENTO 2 — Ativo visual**: envia a foto/vídeo coerente com o perfil (ver tabela abaixo).
- **MOMENTO 3 — Desejo / diferencial curto**: 1 diferencial forte, nunca a lista inteira.
- **MOMENTO 4 — Preço + parcelamento**: valor à vista + parcelamento, sempre transparente (ver seção Financeiro).
- **MOMENTO 5 — CTA / pergunta**: fecha com pergunta que avança a conversa.

Depois, se o hóspede continuar respondendo, entram novos diferenciais e ativos conforme perfil/dúvida (ver seção "Continuação — se o lead responder depois do orçamento" abaixo — é uma etapa posterior a este ciclo de 5, não o mesmo Momento 3 de diferencial curto acima).

**A ORDEM é obrigatória. A quantidade de mensagens não é.** Não é preciso enviar 5 mensagens separadas — os 5 momentos podem se combinar em menos envios (ex.: Momento 1+2 numa mensagem com foto anexada, Momento 3+4+5 na seguinte), mas a sequência lógica acolhimento→ativo→desejo→preço→CTA precisa ser preservada. O que este padrão proíbe é abrir com "produto + preço" puro, sem ativo nem desejo antes, quando há ativo coerente disponível.

Quando houver ativo visual adequado, o formato mais comum é **2 mensagens**:

- **Mensagem 1** — recomendação + contexto curto (Momento 1) + ativo (Momento 2, foto/vídeo)
- **Mensagem 2** — desejo/diferencial curto (Momento 3) + produto + período + valor à vista + parcelamento (Momento 4) + CTA (Momento 5)

Se não houver ativo coerente disponível para o perfil (**caso D — sem ativo visual**), ou o lead já estiver claramente com pressa/objetivo (ex.: "qual o valor da diária?"), seguir direto para desejo curto (se houver algo relevante em 1 frase) + preço — este padrão não obriga enviar imagem quando não há uma que sirva, e não atrasa o preço além disso.

## Perfil → ativo principal

| Perfil | Ativo principal | Diferencial / desejo |
|---|---|---|
| Casal | Foto da suíte, piscina | Mariscal, praia, descanso, refúgio |
| Família com criança | Piscina, parquinho/área de lazer | Café na suíte, praticidade, proximidade da praia |
| Grupo/família grande | Combinação de suítes, espaço | Estrutura para o grupo, áreas comuns |
| Casa Arágua (qualquer perfil) | Piscina, área externa | Privacidade, churrasqueira, casa completa, autonomia |
| Pet | Acomodação adequada | Política pet, praticidade |

Normalmente **1 ativo principal**, no máximo 1–3 imagens coerentes. Nunca mandar pacote grande de fotos sem função comercial clara — a pergunta interna antes de enviar é sempre "essa imagem ajuda **esse** hóspede específico a desejar ou entender melhor a estadia?". Se não, não enviar (ex.: família com criança não recebe só foto romântica de suíte sem piscina/parquinho).

## Recomendação principal (quando há 2+ suítes possíveis)

Não abrir com "Fuego ou Terra, qual prefere?" por padrão. Quando os dados forem suficientes para indicar uma preferência (perfil, composição, orçamento pedido), recomendar primeiro:

"Pelo perfil de vocês, eu começaria pela *Fuego*..."
"Se preferirem algo um pouco mais espaçoso, também tenho a *Terra*."

Não esconder a alternativa — só organizar a ordem, reduzindo carga de decisão.

## Trabalhar em camadas — nunca despejar tudo de uma vez

Não mandar de uma vez: suíte + piscina + praia + café + parquinho + Bombinhas + passeio + estacionamento + churrasqueira + todos os diferenciais juntos. Primeiro envio: **1 diferencial forte + 1 ativo coerente** (Momentos 1–3). Só depois, se o hóspede demonstrar interesse ou dúvida, aprofundar — é a seção seguinte.

## Continuação — se o lead responder depois do orçamento

Se o lead responder ou demonstrar dúvida/interesse após os 5 momentos do primeiro orçamento, entregar o que ele pedir especificamente (mais fotos, vídeo, diferença entre suítes, piscina, parquinho, praia, estacionamento, café da manhã, churrasqueira, localização, pet, passeios, Bombinhas, Mariscal, privacidade). Se ele não pedir nada específico, usar 1 diferencial adicional coerente com o perfil — nunca despejar a lista inteira de uma vez.

## Fonte dos ativos — nunca recriar

Este arquivo não tem nem cria códigos de foto. Os ativos reais vêm de:

- `SELECOES_WHATSAPP_VILLA_ARAGUA.md` — Pousada Arágua, códigos `AT-*`
- `SELECOES_WHATSAPP_CASA_ARAGUA.md` — Casa Arágua, códigos `CAS-*`
- `BIBLIOTECA_VISUAL_VILLA_ARAGUA.md` — biblioteca visual geral
- `SELECOES_WHATSAPP_TURISMO_BOMBINHAS.md` — só turismo, códigos `TUR-*`, nunca no lugar da foto da acomodação

Regras já vigentes nessas fontes continuam valendo integralmente (nunca misturar foto Casa com Pousada; `TUR-MARISCAL-02` exclusiva da Pousada; nunca associar foto da Casa a café da manhã; etc. — ver skill principal, seção "Fotos e mensagens aprovadas").

## Financeiro — sem exceção

A camada de desejo/visual nunca substitui nem atrasa o preflight do item 51. Antes de escrever a Mensagem 2 (ou a mensagem única, se não houver ativo), consultar sempre `DADOS_OFICIAIS_ATENDIMENTO_VILLA_ARAGUA.md`, item 51: valor à vista → faixa → número de parcelas → cálculo ×1,07 → arredondamento → copy final. Nunca citar 7%/juros/acréscimo/adicional ao hóspede. Se houver qualquer dúvida sobre o valor, bloquear o preço — a mensagem de desejo pode ser enviada isoladamente enquanto o preço é confirmado, nunca o contrário (nunca inventar valor pra não atrasar a experiência).

## Formato WhatsApp

Segue integralmente `villa-aragua-humanizer-pt-br` (`formatacao-whatsapp.md`, `anti-robo-whatsapp.md`): sem `▎`, sem blockquote/`>`, *asteriscos literais*, blocos curtos, linha em branco entre pensamentos, emoji variado (1–3 por mensagem/conjunto), Humanizer como passada final — **preservando a ordem dos 5 momentos (ordem obrigatória, contagem de mensagens flexível)** (ver trava 9.1 em `anti-robo-whatsapp.md`).

## Exemplos de referência

**Casal:**

Mensagem 1 — "Oi, Cris! Pela viagem de vocês dois, acho que a *Suíte Fuego* combina muito bem com esses dias em Mariscal 🌿 Ela é uma opção gostosa pra casal, e vocês ficam pertinho da praia. Vou te mostrar um pouquinho dela: [ativo]"

Mensagem 2 — "Pra *03 a 07 de setembro (4 diárias)*: *Suíte Fuego* — *R$ 1.946,00 à vista* ou *até 5x de R$ 416,00* no cartão. Já inclui *café da manhã servido na suíte* ☕️ Se quiser algo um pouco mais espaçoso, também tenho a *Terra* como alternativa. Essa proposta faz sentido pra vocês?"

**Família com criança:**

Mensagem 1 — "Oi, [nome]! Como vocês vêm em família, quis te mostrar primeiro uma parte que costuma fazer diferença com criança 🌿 [piscina/parquinho] Além da acomodação, vocês conseguem aproveitar bem a estrutura da Pousada e ficam pertinho da praia."

Mensagem 2 — "Pra estadia de vocês, a opção que eu indicaria primeiro é a *[suíte]*: *[período] — [X] diárias* — *R$ X à vista* ou *até Nx de R$ X*. Já inclui *café da manhã servido na suíte* ☕️ Quer que eu te mostre também a suíte por dentro?"

**Casa Arágua:**

Mensagem 1 — "Oi, [nome]! Pela proposta da viagem de vocês, a *Casa Arágua Mariscal* pode fazer bastante sentido 🏡 O grande diferencial aqui é ter mais *privacidade*, com *piscina e churrasqueira* só de vocês. [foto piscina/área externa]"

Mensagem 2 — "Pra *[período]*: *Casa Arágua Mariscal* — *R$ X à vista* ou *até Nx de R$ X*. Se quiser, te mostro também os ambientes internos e como fica a distância até a praia 🌊"

**Sem ativo visual adequado (caso D):** quando não houver foto coerente disponível para aquele perfil específico no momento, seguir os Momentos 1, 3, 4 e 5 numa mensagem única, sem pular direto para "produto + preço" cru — o desejo/diferencial curto continua vindo antes do valor.

Mensagem única — "Oi, [nome]! Pela sua viagem pra Mariscal, acho que a *[suíte/produto]* combina bem com o que vocês estão buscando — [1 diferencial curto coerente com o perfil]. Pra *[período] — [X] diárias*: *R$ X à vista* ou *até Nx de R$ X*. [Se Pousada: já inclui *café da manhã servido na suíte* ☕️] Faz sentido pra vocês, ou quer que eu te mostre outra opção?"

## Trava final — o que este padrão NÃO significa

- Mandar várias fotos sem contexto.
- Esconder ou atrasar o preço além do necessário para dar 1 diferencial + 1 ativo (normalmente 2 mensagens; nunca mais que isso só para "alongar" a proposta).
- Alongar o atendimento artificialmente.
- Transformar toda proposta em texto emocional sem preço claro — desejo nunca substitui preço.
- Exagerar benefícios ou inventar diferenciais não documentados nas fontes oficiais.

## Teste operacional em andamento

Marcado como **TESTE OPERACIONAL — ORÇAMENTO CONTEXTUAL**, período inicial 7–10 dias a partir de 19/08/2026. Coorte de comparação: 34 orçamentos anteriores, 7 respostas pós-orçamento estritas (20,6%). Sem meta artificial definida — acompanhar via campos de mensuração no `CRM_LEADS_VILLA_ARAGUA.md`.

*(Consolidação de 20/08/2026: a ordem dos 5 momentos foi reforçada e destravada de "obrigatoriamente 2 mensagens" para "ordem obrigatória, contagem de mensagens flexível", em resposta a atendimentos que estavam voltando ao formato antigo de texto+preço. Ver também `respostas-whatsapp.md`, seção "Lead vindo de campanha", que teve nota de roteamento adicionada para não competir com este padrão.)*
