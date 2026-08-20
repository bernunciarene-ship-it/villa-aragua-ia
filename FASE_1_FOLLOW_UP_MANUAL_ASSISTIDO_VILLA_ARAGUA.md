# FASE 1 — FOLLOW-UP MANUAL ASSISTIDO VILLA ARÁGUA

*Manual operacional. Envio 100% manual, com sugestão de IA e aprovação humana antes de qualquer mensagem sair. Nenhuma automação, integração com WhatsApp API, CRM, Make, Zapier ou n8n foi criada ao escrever este arquivo. Nenhum arquivo original da Villa Arágua e nenhuma skill foram alterados — este documento apenas se apoia neles e em `ARQUITETURA_FOLLOW_UP_AUTOMATICO_VILLA_ARAGUA.md`.*

## 1. Objetivo da Fase 1

Testar, na prática e com risco zero, se o follow-up com apoio de IA melhora a conversão de leads da Villa Arágua — sem nenhuma automação técnica. Nesta fase, a IA (via `villa-aragua-skill-router` e as skills de execução) **sugere**; um humano **revisa, aprova e envia** manualmente pelo WhatsApp normal. O objetivo é aprender o que funciona (mensagens, cadência, argumentos) antes de qualquer investimento em automação real.

## 2. O que esta fase faz

- Ajuda a identificar leads que precisam de retorno.
- Sugere mensagens de follow-up.
- Ajuda a classificar o estágio do lead.
- Ajuda a entender objeções.
- Ajuda a melhorar a conversão direta (reserva sem intermediário de OTA).
- Registra aprendizados para uma futura automação (Fase 2 em diante, ver `ARQUITETURA_FOLLOW_UP_AUTOMATICO_VILLA_ARAGUA.md`).

## 3. O que esta fase não faz

- Não envia mensagens automaticamente.
- Não usa WhatsApp API.
- Não integra CRM.
- Não decide desconto sozinha.
- Não confirma disponibilidade.
- Não promete condição comercial.
- Não substitui aprovação humana em nenhuma etapa.

## 4. Fluxo manual recomendado

```
1. Humano identifica lead parado (sem resposta, orçamento sem retorno, objeção não resolvida)
        ↓
2. Humano informa o contexto à IA (o que já foi dito, perfil do lead, produto de interesse)
        ↓
3. villa-aragua-skill-router escolhe as skills certas para o caso
        ↓
4. villa-aragua-sales-receptionist cria a sugestão de mensagem
        ↓
5. villa-aragua-pricing-revenue valida, se houver preço, desconto ou pacote envolvido
        ↓
6. villa-aragua-humanizer-pt-br ajusta o tom
        ↓
7. Humano revisa a sugestão final
        ↓
8. Humano envia pelo WhatsApp (canal oficial, manualmente)
        ↓
9. Resultado é registrado manualmente (seção 12)
```

Nenhuma etapa deste fluxo é pulada — mesmo quando a sugestão da IA parecer "óbvia" o suficiente para enviar direto, a revisão humana (passo 7) é obrigatória nesta fase.

## 5. Campos mínimos para registrar cada lead

| Campo | Preenchimento |
|---|---|
| Nome | |
| Data da entrada | |
| Canal de origem | Meta Ads / Instagram / WhatsApp direto / indicação / hóspede antigo / não identificado |
| Pousada ou Casa | |
| Datas desejadas | |
| Número de adultos | |
| Número de crianças | |
| Pet | Sim / Não / Não informado — nunca confirmar acomodação com pet sem checar regra oficial |
| Orçamento enviado? | Sim/Não |
| Valor enviado? | Só preencher com valor realmente enviado, nunca estimado |
| Última mensagem do lead | |
| Última resposta enviada | |
| Estágio do lead | Ver seção 6 |
| Próximo follow-up sugerido | |
| Resultado | Respondeu / Não respondeu / Reservou / Perdido |
| Observações | |

## 6. Estágios práticos do lead na Fase 1

- Novo lead
- Pediu preço sem datas
- Informou datas
- Orçamento enviado
- Sumiu após orçamento
- Objeção de preço
- Comparando com OTA
- Família
- Casal
- Pet
- Interesse Pousada
- Interesse Casa
- Quase reserva
- Reserva perdida
- Reserva confirmada
- Não insistir mais

Um lead pode acumular mais de um estágio ao mesmo tempo (ex.: "família" + "interesse Casa" + "objeção de preço") — o estágio operacional (o que decide a próxima ação) é sempre o mais avançado no funil, os demais são contexto para calibrar o tom.

## 7. Cadência manual sugerida

- **Primeiro retorno**: leve e prestativo — sem cobrança, só reabrindo a porta.
- **Segundo retorno**: ajuda prática ou reforço de um benefício real.
- **Terceiro retorno**: encerramento elegante, deixando a porta aberta sem insistir mais.
- **Reativação futura**: somente quando fizer sentido (feriado novo, hóspede antigo, temporada relevante) — não é parte da cadência imediata.

Esta cadência é uma referência de **tom e intenção**, não uma regra rígida de horas nesta fase — a decisão de quando exatamente enviar cada retorno é sempre humana, caso a caso. Não usar pressão. Não usar urgência falsa.

## 8. Modelos de mensagens por situação

Exemplos sem preço e sem disponibilidade inventada — ponto de partida para adaptar, não texto pronto para copiar e colar sem revisão:

**Lead pediu preço e sumiu**:
> "Oi! Fico à disposição se quiser continuar por aqui 😊 Consigo te ajudar com mais alguma informação sobre a Villa Arágua?"

**Lead recebeu orçamento e não respondeu**:
> "Olá 😊 Conseguiu dar uma olhada nas opções que te passei? Fico à disposição para qualquer dúvida."

**Lead pediu preço sem informar datas**:
> "Consigo te ajudar com certeza 😊 Pra eu confirmar o valor certinho, me conta as datas de entrada e saída e quantas pessoas seriam?"

**Família em dúvida**:
> "Para famílias, a gente costuma pensar em espaço e praticidade — me conta as idades das crianças que já te oriento na melhor opção entre a Pousada e a Casa 😊"

**Casal em dúvida**:
> "Para um casal, a Pousada Arágua costuma ser bem procurada — clima tranquilo e café da manhã servido na acomodação. Posso te contar mais?"

**Lead com pet**:
> "Boa pergunta 😊 Pet é aceito em acomodações específicas, sob consulta prévia. Me conta um pouco sobre o porte e o perfil do pet que já verifico com a equipe."

**Lead comparando com Booking/Airbnb**:
> "Entendo 😊 Os valores podem variar bastante conforme o canal. Reservando direto com a gente, o atendimento é próximo do início ao fim da estadia. Posso verificar as opções para o período de vocês?"

**Lead da Casa Arágua**:
> "A Casa Arágua é uma casa completa e privativa, com piscina própria e espaço para até 6 pessoas. Posso te passar mais detalhes — me confirma as datas que você tem em mente?"

**Lead da Pousada Arágua**:
> "A Pousada Arágua fica bem pertinho da praia, com café da manhã servido na própria acomodação. Quer que eu verifique a disponibilidade para as datas de vocês?"

**Encerramento elegante**:
> "Sem problema 😊 Vou deixar nosso atendimento em aberto por aqui. Se quiser retomar em qualquer momento, é só me chamar que verifico a disponibilidade atualizada para vocês."

## 9. Checklist antes de enviar qualquer follow-up

- [ ] Produto correto: Pousada ou Casa?
- [ ] Datas confirmadas?
- [ ] Pessoas confirmadas?
- [ ] Crianças confirmadas?
- [ ] Pet confirmado?
- [ ] Valor autorizado?
- [ ] Desconto autorizado?
- [ ] Disponibilidade confirmada?
- [ ] Mensagem sem urgência falsa?
- [ ] Tom humano?
- [ ] O lead pediu para não receber mais mensagem?
- [ ] Já reservou?
- [ ] Já recusou claramente?

Se qualquer resposta apontar risco (ex.: "desconto não autorizado", "já reservou"), o follow-up não sai — volta para revisão humana antes de qualquer envio.

## 10. Regras de bloqueio

Não enviar follow-up se:

- O lead pediu para parar.
- O lead já reservou.
- O lead recusou claramente.
- Há reclamação ou assunto sensível em aberto.
- Falta disponibilidade confirmada.
- Falta autorização de preço/desconto.
- A mensagem depender de dado turístico não validado (estabelecimento, distância, horário não confirmados).
- Houver risco de misturar Pousada e Casa na mesma mensagem.
- Nunca aplicar pacote da Pousada Arágua automaticamente à Casa Arágua.

## 11. Como usar as skills na Fase 1

- **`villa-aragua-skill-router`**: escolhe o caminho — qual skill principal e quais de apoio para cada situação de follow-up.
- **`villa-aragua-sales-receptionist`**: conduz a conversa — diagnóstico, tom, condução até a reserva.
- **`villa-aragua-pricing-revenue`**: protege preço, desconto e margem — nenhum valor entra numa mensagem sem passar por ela.
- **`villa-aragua-humanizer-pt-br`**: ajusta o tom final, sem mudar o conteúdo comercial.
- **`villa-aragua-campaign-analytics`**: ajuda a entender a origem e a qualidade do lead (de qual campanha veio, se está avançando no funil).
- **`villa-aragua-copywriting-conversion`**: ajuda em mensagens mais persuasivas quando fizer sentido (ex.: remarketing sazonal), sempre sem exagero.
- **`villa-aragua-marketing-psychology`**: ajuda a entender objeções e o comportamento de decisão do hóspede, para calibrar a abordagem com ética.

## 12. Como registrar aprendizados

Para cada follow-up enviado, registrar:

- Qual mensagem foi enviada?
- O lead respondeu?
- Fechou reserva?
- Qual objeção apareceu?
- Qual argumento funcionou?
- Qual argumento não funcionou?
- O lead era Pousada ou Casa?
- Origem do lead?
- Observação para futura automação (ex.: "essa mensagem gerou resposta rápida, boa candidata a template aprovado na Fase 2").

## 13. Métricas simples da Fase 1

- Número de leads acompanhados.
- Número de follow-ups enviados.
- Taxa de resposta.
- Taxa de reserva após follow-up.
- Principais objeções.
- Leads por origem.
- Pousada x Casa (sempre separados, nunca somados).
- Motivos de perda.
- Aprendizados para automação futura.

Nenhuma dessas métricas deve ser estimada — só contam números realmente registrados durante a Fase 1 (mesma régua de `villa-aragua-campaign-analytics`: dado real, nunca inventado).

## 14. Pendências antes da Fase 2

- Validar a ferramenta futura: planilha, CRM, Make, Zapier ou n8n (ver `ARQUITETURA_FOLLOW_UP_AUTOMATICO_VILLA_ARAGUA.md`, seção 11).
- Criar banco oficial de preços consultável (hoje vive em `DADOS_OFICIAIS_ATENDIMENTO_VILLA_ARAGUA.md` e nas referências de `pricing-revenue`, sem um banco único).
- Criar banco oficial de disponibilidade (não existe hoje nenhuma fonte automatizada — toda checagem é manual).
- Criar biblioteca de mensagens aprovadas (os modelos da seção 8 são ponto de partida, não biblioteca validada).
- Definir responsável humano fixo pela revisão/aprovação e pelo registro dos leads.
- Definir política oficial de desconto (hoje é "sob consulta", sem regra fechada por canal/antecedência).
- Definir política oficial de pet (hoje é "acomodações específicas, sob consulta prévia" — sem lista fechada e pública).
- **Definir data oficial de reabertura** — ver pendência crítica na seção 15.
- Definir regras de feriados e alta temporada além do que já está confirmado (7 de Setembro tem pacote definido; demais datas ainda não).
- Testar com leads reais por tempo suficiente antes de qualquer automação.

## 15. Pendência crítica: data oficial de reabertura

**Existe possível inconsistência entre reabertura em agosto/2026 e setembro/2026. Não usar nenhuma data em campanhas, copies, follow-ups ou calendário comercial sem validação em fonte oficial.**

Registro factual do que foi verificado até agora (para orientar essa validação, não para encerrá-la): todos os arquivos oficiais consultados no projeto (`CHECKLIST_DECISOES_CAMPANHA_REABERTURA_VILLA_ARAGUA_2026.md`, `PLANO_CAMPANHA_REABERTURA_VILLA_ARAGUA_2026.md`, `ESTRUTURA_CAMPANHA_META_ADS_7_SETEMBRO_VILLA_ARAGUA_2026.md`, `SETUP_INICIAL_META_ADS_7_SETEMBRO_VILLA_ARAGUA_2026.md`, `COPYS_FINAIS_META_ADS_7_SETEMBRO_VILLA_ARAGUA_2026.md`, `MATRIZ_ANUNCIOS_FINAIS_7_SETEMBRO_VILLA_ARAGUA_2026.md`) registram a **data de reabertura como 01/08/2026**, e o **feriado de 7 de Setembro** como uma campanha comercial separada, posterior à reabertura, com pacote próprio exclusivo da Pousada Arágua. Não foi encontrado, em nenhum arquivo do projeto, um registro alternativo de "reabertura em setembro" como data.

Dito isso, **o risco real e confirmado** é de **confusão narrativa**, não de dado contraditório: vários materiais de copy/campanha usam a palavra "reabertura" (bastidores da reabertura, remarketing de reabertura, "a Villa Arágua está voltando") **dentro da campanha do feriado de 7 de Setembro** — o que pode levar quem lê rapidamente (humano ou IA) a associar "reabertura" à data de setembro, como aconteceu no teste da skill-router. Por isso, mesmo com a evidência documental apontando para 01/08/2026, este documento **não fecha a questão** — trata como pendência formal:

- Nenhuma campanha, copy, follow-up ou calendário comercial desta Fase 1 deve declarar uma data de reabertura sem reconfirmar diretamente com Renildo qual data usar em comunicação pública.
- Ao usar a palavra "reabertura" em qualquer mensagem de follow-up, deixar claro no material interno (não necessariamente na mensagem ao lead) se está se referindo à reabertura da operação (01/08, conforme fonte) ou à campanha comercial do feriado de 7 de Setembro — para não repetir a confusão internamente.
- Esta pendência deve ser copiada/referenciada em qualquer novo material de campanha, copy ou calendário criado a partir de agora, até ser formalmente resolvida por Renildo.

---

## Confirmações finais

- **Arquivo criado**: `FASE_1_FOLLOW_UP_MANUAL_ASSISTIDO_VILLA_ARAGUA.md`
- **Caminho**: `/Users/luisrenegomesreis/Desktop/VILLA ARAGUA IA/FASE_1_FOLLOW_UP_MANUAL_ASSISTIDO_VILLA_ARAGUA.md`
- **Nenhuma skill foi alterada. Nenhum arquivo existente foi alterado.** Este é um arquivo novo, isolado.
- **Nenhuma automação real foi criada** — nenhum WhatsApp API, CRM, Make, Zapier ou n8n foi acessado ou configurado.

### Resumo do conteúdo

Manual de 15 seções para conduzir o follow-up 100% manual da Villa Arágua com apoio de IA: fluxo de aprovação humana obrigatória (seção 4), campos mínimos de registro de lead (seção 5), 16 estágios práticos (seção 6), cadência sem hora rígida (seção 7), 10 modelos de mensagem sem preço/disponibilidade inventados (seção 8), checklist de 13 pontos antes de qualquer envio (seção 9), 8 regras de bloqueio (seção 10), papel de cada skill (seção 11), registro de aprendizado (seção 12), métricas simples (seção 13), pendências antes da Fase 2 (seção 14) e a pendência crítica de data de reabertura (seção 15).

### Pendências críticas

1. **Data oficial de reabertura** (seção 15) — evidência documental aponta para 01/08/2026, mas tratada como pendência formal de reconfirmação por causa do risco de confusão narrativa com a campanha de 7 de Setembro. Nenhuma comunicação pública deve fixar essa data sem checagem direta com Renildo.
2. Ausência de banco oficial de preços e de disponibilidade consultável (hoje dependem de leitura manual de arquivo).
3. Ausência de política fechada de desconto e de pet (hoje ambas são "sob consulta", sem regra pública definida).
4. Nenhuma biblioteca de mensagens aprovada ainda — os modelos da seção 8 são rascunho inicial, não texto validado por Renildo.

### Próximo passo recomendado

Começar a Fase 1 de fato: escolher 3 a 5 leads reais parados (qualquer estágio da seção 6), rodar o fluxo da seção 4 ponta a ponta em cada um, e registrar o resultado (seção 12) por pelo menos algumas semanas antes de avaliar a Fase 2. Em paralelo, levar a pendência crítica da seção 15 diretamente para Renildo confirmar por escrito qual data usar como "reabertura" em qualquer material público futuro.
