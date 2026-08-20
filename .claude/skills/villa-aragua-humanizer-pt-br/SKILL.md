# Villa Arágua — Humanizer PT-BR

Esta skill ensina a **melhorar a forma** de textos comerciais e de atendimento da Villa Arágua — WhatsApp, follow-up, orçamento, objeção, copy de Meta Ads, Instagram, resposta a avaliação do Google, mensagem a hóspede, guia digital — tornando-os mais humanos, naturais e acolhedores, na voz da marca.

**Regra mais importante da skill, acima de qualquer outra**: humanizar muda **como** algo é dito, nunca **o que** é dito. Esta skill nunca inventa preço, regra, comodidade, disponibilidade ou benefício. Todo dado citado num texto humanizado precisa ter origem em um arquivo oficial da Villa Arágua ou em uma das outras duas skills do projeto — se não tiver, não entra no texto.

## Fontes da verdade (não alterar, só consultar)

- `ROTEIRO_RECEPCIONISTA_IA.md` — tom de voz oficial (seção 2) e dezenas de mensagens já aprovadas para cada momento da jornada do hóspede.
- `PROMPT_RECEPCIONISTA_IA_WHATSAPP.md` — prompt de produção da Recepcionista IA.
- `DADOS_OFICIAIS_ATENDIMENTO_VILLA_ARAGUA.md` — todo dado que pode ou não ser afirmado (preço, regra, comodidade).
- `HISTORIA_E_POSICIONAMENTO_VILLA_ARAGUA.md` — o próprio histórico de ajuste de tom da marca (texto institucional antes/depois), referência direta de calibragem.
- `GUIA_DIGITAL_HOSPEDE_VILLA_ARAGUA.md` — tom editorial usado em material mais longo (guia, site).
- `AGENTE_IA_MARKETING_VENDAS_META_ADS_VILLA_ARAGUA.md`, `COPYS_FINAIS_META_ADS_7_SETEMBRO_VILLA_ARAGUA_2026.md`, `SETUP_INICIAL_META_ADS_7_SETEMBRO_VILLA_ARAGUA_2026.md`, `COPYS_7_ANUNCIOS_INICIAIS_7_SETEMBRO_2026.md` — exemplos reais já aprovados de copy comercial.
- As referências de `villa-aragua-sales-receptionist` (diagnóstico, objeções, respostas WhatsApp) e `villa-aragua-pricing-revenue` (preço aprovado/sugerido/mínimo/autorização) — fonte de conteúdo comercial correto a ser humanizado.

Se um desses arquivos for atualizado, esta skill deve ser revisada — ela ensina a forma, as outras fontes continuam donas do conteúdo.

## Como usar esta skill

1. **Calibrar o tom** → `tom-de-voz-villa-aragua.md` antes de escrever qualquer coisa — os seis ingredientes da voz Villa Arágua e o vocabulário que combina/não combina com a marca.
2. **Se for mensagem de WhatsApp** → `anti-robo-whatsapp.md` — mensagens curtas, uma pergunta por vez, sem cara de formulário — e `formatacao-whatsapp.md` — padrão obrigatório de saída (sem `▎`/blockquote, negrito com `*asteriscos*` literais, linha em branco entre ideias, emoji variado e contextual, entrega em template copiável).
3. **Se for copy de Meta Ads ou Instagram** → `humanizacao-meta-ads.md`.
4. **Se for resposta a avaliação do Google** → `respostas-avaliacoes-google.md`.
5. **Se for mensagem ao hóspede (pré-estadia, durante, pós-estadia)** → `mensagens-hospedes.md`.
6. **Antes de finalizar qualquer texto** → rodar `checklist-humanizacao.md` — as dez perguntas de revisão.
7. **Para ver o padrão aplicado na prática** → `exemplos-antes-depois.md`.

## Integração com as outras skills do projeto

Esta é a terceira skill do ecossistema Villa Arágua, e as três se encaixam assim:

- **`villa-aragua-sales-receptionist`** decide *como conduzir a conversa* comercial — diagnóstico do lead, produto certo, objeção, follow-up. É a fonte do **conteúdo comercial** a ser humanizado.
- **`villa-aragua-pricing-revenue`** decide *quanto cobrar e por quê* — preço aprovado, sugerido, mínimo aceitável, condição que precisa de autorização. É a fonte do **dado de preço** a ser humanizado.
- **`villa-aragua-humanizer-pt-br`** (esta skill) não decide conteúdo nem preço — ela pega o conteúdo já certo, vindo das outras duas skills (ou de um arquivo oficial), e melhora **a forma como ele é dito**, para soar como uma pessoa da Villa Arágua escrevendo, não uma IA respondendo.

Na prática: use `villa-aragua-sales-receptionist` e `villa-aragua-pricing-revenue` para chegar ao conteúdo certo (o que dizer, quanto cobrar, quando escalar); use esta skill por cima, como última passada, para garantir que o texto final soa humano antes de ser enviado ou publicado.

## O que esta skill nunca faz

- Nunca adiciona preço, desconto, disponibilidade, comodidade ou promessa que não estava no texto original ou numa fonte oficial.
- Nunca remove uma frase de segurança obrigatória (ex.: "posso verificar", "vou confirmar com a equipe") só para deixar o texto mais fluido — a cautela comercial continua, só a forma muda.
- Nunca cria urgência falsa para tornar um anúncio ou follow-up "mais persuasivo".
- Nunca usa clichê de propaganda de turismo (ver lista de vocabulário a evitar em `tom-de-voz-villa-aragua.md`).
- Nunca decide sozinha uma condição comercial nova — isso é sempre papel de `villa-aragua-pricing-revenue` e, em última instância, de Renildo/equipe.

## Pendência conhecida

Não existe, nos arquivos oficiais do projeto, um padrão real e já aprovado de resposta a avaliações do Google — `respostas-avaliacoes-google.md` foi construído a partir do tom de voz geral da marca e da regra de segurança já existente sobre avaliação negativa, e deve ser tratado como sugestão até validação de Renildo.
