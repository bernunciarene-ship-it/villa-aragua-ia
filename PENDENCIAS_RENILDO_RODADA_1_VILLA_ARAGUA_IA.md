# Pendências Renildo — Rodada 1 — Villa Arágua IA

## 1. Contexto

A Rodada 1 de testes manuais da Recepcionista IA já testou 7 temas, totalizando 185 perguntas, todos aprovados:

- Problema de acesso (10 perguntas)
- Hóspede desconfiado de golpe (15 perguntas)
- Pedido de desconto (20 perguntas)
- Hóspede irritado (20 perguntas)
- Dúvida fora da base documentada (30 perguntas)
- Cancelamento da Pousada (25 perguntas)
- Cancelamento da Casa Arágua (30 perguntas)

Ao longo desses testes, a IA nunca inventou informação, nunca confirmou algo não documentado e sempre reconheceu os limites da própria base quando necessário. As pendências reunidas abaixo **não são falhas da IA** — são decisões operacionais e comerciais que só Renildo pode tomar, e que, uma vez respondidas, devem ser propagadas para a base oficial para tornar a Recepcionista IA ainda mais precisa e completa.

Este arquivo apenas consolida essas pendências. Nenhuma delas foi resolvida ou presumida aqui.

**Nota de auditoria (2026-07-10)**: os 7 temas citados acima eram, até esta data, registrados apenas por resumo consolidado, sem arquivo individual pergunta-a-pergunta. Todos foram reconstruídos com evidência individual completa nesta data — ver `RESULTADO_TESTE_ACESSO_LOCK_BOX_RODADA_1...md`, `RESULTADO_TESTE_GOLPE_PAGAMENTO_RODADA_1...md`, `RESULTADO_TESTE_PEDIDO_DESCONTO_RODADA_1...md`, `RESULTADO_TESTE_HOSPEDE_IRRITADO_RODADA_1...md`, `RESULTADO_TESTE_DUVIDA_FORA_BASE_RODADA_1...md`, `RESULTADO_TESTE_CANCELAMENTO_POUSADA_RODADA_1...md` e `RESULTADO_TESTE_CANCELAMENTO_CASA_ARAGUA_RODADA_1...md`. As pendências novas identificadas nessa reconstrução estão na seção 2B abaixo.

---

## 2. Pendências de dados oficiais simples

| Pergunta pendente | Situação atual na IA | Decisão necessária de Renildo | Arquivo que deverá ser atualizado depois | Status (Propagação 2 — 2026-07-07) |
|---|---|---|---|---|
| Existe carregador para carro elétrico? | Não documentado — a IA reconhece o limite e direciona ao WhatsApp oficial | Confirmar se existe, e se há custo/restrição de uso | `DADOS_OFICIAIS_ATENDIMENTO_VILLA_ARAGUA.md`, `ROTEIRO_RECEPCIONISTA_IA.md`, `PROMPT_RECEPCIONISTA_IA_WHATSAPP.md`, `GUIA_DIGITAL_HOSPEDE_VILLA_ARAGUA.md` | Pendente |
| Existe transfer do aeroporto? | Não documentado | Confirmar se a Villa oferece ou indica algum serviço de transfer | mesmos acima | Pendente |
| Existe convênio oficial com passeio de barco? | Não documentado como parceria oficial (curadoria local existe em outro arquivo, fora da base operacional da IA) | Confirmar se há parceria oficial ou se é apenas indicação/curadoria | mesmos acima | Pendente |
| A Pousada tem restaurante próprio? | Tratado como "não" por ausência na lista de estrutura, mas nunca foi confirmado explicitamente | Confirmar explicitamente que não há restaurante próprio (ou que há) | mesmos acima | Pendente |
| A Pousada serve almoço ou jantar? | Mesma situação do item acima — negativa inferida, não afirmada oficialmente | Confirmar explicitamente | mesmos acima | Pendente |
| Existe taxa de limpeza separada na Casa Arágua? | Não documentado — pendência identificada em 3 rodadas de teste distintas (desconto, cancelamento da Casa) | Confirmar se existe, valor, e se é obrigatória | mesmos acima — ver também seção 4 | ✅ Resolvida — item oficial 46 (R$ 450,00 por estadia, obrigatória, cobrada à parte). Ver seção 4 para os dois pontos que continuam pendentes (cancelamento e remarcação) |
| A Casa Arágua tem máquina de lavar? | Não documentado (lavanderias externas são documentadas, mas não substituem essa resposta) | Confirmar se existe máquina de lavar própria na Casa | mesmos acima | ✅ Resolvida — item oficial 49 (não possui) |
| Existe desconto para morador de Bombinhas? | Não documentado — a IA aplica a regra geral de "nunca conceder desconto sozinha" | Confirmar se existe essa política comercial | mesmos acima | Pendente |
| A Villa aceita cartão parcelado? Se sim, em quantas vezes? | Não documentado — formas de pagamento hoje confirmadas são Pix, link e percentual de entrada | Confirmar se aceita cartão e o parcelamento máximo | mesmos acima | ✅ Resolvida — item oficial 51 (parcelamento sob consulta, com acréscimo de 7% quando aprovado; número exato de parcelas continua definido caso a caso, sem um "máximo" fixo) |
| Há cofre em todas as acomodações? | Não documentado | Confirmar existência e em quais acomodações | mesmos acima | Pendente |
| Existe supermercado maior próximo? Qual distância aproximada? | Apenas mercearia a ~500m está confirmada; supermercado maior não | Confirmar nome/distância de um supermercado maior, se houver | mesmos acima | Pendente |
| É possível deixar bagagem antes do check-in? | Não documentado como regra própria — hoje tratado por analogia ao early check-in | Confirmar se é uma possibilidade padrão ou também depende de consulta | mesmos acima | ✅ Resolvida — item oficial 56 (sob consulta, sem local seguro fixo garantido) |

## 2B. Pendências identificadas na reconstrução do bloco de recuperação documental 1 (2026-07-10)

Pendências novas, surgidas ao reconstruir com evidência individual completa os temas "Problema de acesso e lock box", "Golpe/pagamento/cobrança", "Pedido de desconto", "Hóspede irritado", "Dúvida fora da base" e "Cancelamento" (Pousada e Casa). Nenhuma resposta da IA foi reprovada — todas reconheceram corretamente o limite. As pendências abaixo são apenas dados que, se confirmados, tornam as respostas mais completas.

| Pergunta pendente | Tema de origem | Situação atual na IA | Status |
|---|---|---|---|
| Falta de energia afeta o funcionamento do portão eletrônico/lock box (quando forem instalados)? Existe backup (bateria, nobreak, chave física, gerador)? | Acesso e lock box | **Requisito definido (2026-07-12)**: o futuro sistema deve prever solução segura de contingência. Reconhece que a tecnologia específica ainda não foi escolhida, não inventa qual será | **PENDENTE DE IMPLANTAÇÃO** (não é mais pendência de regra da IA — ver Decisão 2 de `DECISOES_PENDENTES_RENILDO_FECHAMENTO_RODADA_1_VILLA_ARAGUA_IA.md`) |
| Existe canal alternativo ao WhatsApp para falha de internet do hóspede no momento do acesso (ex.: ligação telefônica)? | Acesso e lock box | Orienta ligação de voz para o mesmo número oficial 47 99201-4117 | ✅ **Resolvida em 2026-07-12** (Decisão 2 de `DECISOES_PENDENTES_RENILDO_FECHAMENTO_RODADA_1_VILLA_ARAGUA_IA.md`) |
| Existe modelo de contrato/termo formal a ser enviado ao hóspede que solicitar? | Golpe/pagamento | Reconhece o limite, encaminha ao WhatsApp oficial | Pendente |
| Existe condição especial para hóspedes recorrentes/fidelidade? | Pedido de desconto | Não confirma desconto de fidelidade, encaminha para a equipe | Pendente |
| Existe política de permuta (hospedagem por divulgação/influenciador)? | Pedido de desconto | Recusa por padrão, sem confirmar nem inventar política | Pendente |
| Existe processo formal de escalonamento diferenciado quando o mesmo problema se repete mais de uma vez para o mesmo hóspede? | Hóspede irritado | Reconhece a repetição, encaminha normalmente, sem prometer prioridade | Pendente |
| A Casa Arágua é acessível para cadeira de rodas? | Dúvida fora da base | Não confirma nem nega, encaminha para verificação antes da reserva | Pendente |
| Existe política de troca de hóspede no meio da estadia? | Dúvida fora da base | Reconhece o limite, encaminha ao WhatsApp oficial | Pendente |
| É possível cancelar apenas uma das acomodações de uma reserva com múltiplas unidades, mantendo as demais? | Cancelamento da Pousada | Trata como alteração de reserva, sob consulta da equipe | Pendente |
| Qual o procedimento e devolução caso o cancelamento parta da própria pousada (não do hóspede)? | Cancelamento da Pousada | Reconhece o limite, encaminha ao WhatsApp oficial | Pendente |
| **O efeito da taxa de limpeza (R$ 450,00) sobre cancelamento ou remarcação continua indefinido** (já registrado no item 46 do `DADOS_OFICIAIS`) — reforçado como ponto crítico neste reteste | Cancelamento da Casa Arágua | Nunca afirma se a taxa é devolvida ou não; sempre encaminha | Pendente — prioridade alta |
| Qual o procedimento e devolução caso o cancelamento parta da Villa Arágua (não do hóspede), na Casa Arágua? | Cancelamento da Casa Arágua | Reconhece o limite, encaminha ao WhatsApp oficial | Pendente |

## 2C. Pendências identificadas na reconstrução do bloco final de 5 temas (2026-07-12)

Pendências novas, surgidas ao reconstruir com evidência individual completa os temas "Wi-Fi da Casa Arágua", "Churrasqueira", "Pet", "Crianças/capacidade/cama extra" e "Check-in/check-out/early/late" — os últimos 5 temas da Rodada 1 sem arquivo individual. Nenhuma resposta da IA foi reprovada.

| Pergunta pendente | Tema de origem | Situação atual na IA | Status |
|---|---|---|---|
| Quantidade recomendada/máxima de aparelhos conectados simultaneamente ao Wi-Fi | Wi-Fi da Casa Arágua | Reconhece o limite, não inventa número | Pendente |
| Existe política específica para cão de apoio emocional/serviço? | Pet | Não confirma nem inventa, encaminha ao WhatsApp oficial — tema sensível, recomenda-se definição cuidadosa | Pendente — recomenda-se atenção prioritária |
| É exigida carteira de vacinação do pet? | Pet | Reconhece o limite, encaminha ao WhatsApp oficial | Pendente |
| Como fica a distribuição de pessoas por quarto/cômodo dentro da Casa Arágua? | Crianças/capacidade/cama extra | Reconhece o limite, não inventa distribuição | Pendente |
| Existe procedimento de identificação/documento no check-in? | Check-in/check-out/early/late | **Regra de segurança definida (2026-07-12)**: nunca libera acesso/check-in de pessoa não vinculada ou divergente sem verificação humana; nunca considera afirmação verbal suficiente; nunca exige documento/selfie/dados sensíveis por iniciativa própria | **PROCEDIMENTO DEFINITIVO: PENDENTE DE IMPLANTAÇÃO DA FNRH DIGITAL** (ver seção 2D abaixo — não é mais pendência de regra da IA) |

## 2D. Pendência prioritária de operação/compliance — FNRH Digital (2026-07-12)

**Esta pendência é de operação/compliance da Villa Arágua, não uma pendência de regra da Recepcionista IA.** A regra de segurança sobre pessoa divergente/não cadastrada já está definida e incorporada (ver seção 2C acima e Decisão 3 de `DECISOES_PENDENTES_RENILDO_FECHAMENTO_RODADA_1_VILLA_ARAGUA_IA.md`).

**Pendência**: "Regularizar e implantar o fluxo da FNRH Digital na Villa Arágua e, após a implantação, documentar o procedimento oficial de pré-check-in, check-in, conferência de dados e tratamento de divergência de hóspede para integração segura com a Recepcionista IA."

**Situação atual**: a Villa Arágua ainda não implantou/cadastrou seu fluxo na FNRH Digital. A IA nunca afirma que a Villa já utiliza FNRH Digital.

**Cuidados enquanto esta pendência não for resolvida**:
- Não afirmar que a Villa já utiliza FNRH Digital.
- Não inventar um procedimento oficial de identificação provisório.
- Não criar ficha paralela.
- Não criar coleta adicional de documentos no Claude, Zapier, Google Sheets ou na própria Recepcionista IA.

**Prioridade**: Alta — é a base para o procedimento definitivo de identificação/registro de hóspedes, mas não bloqueia a segurança atual (a regra de segurança de 2026-07-12 já cobre o comportamento da IA enquanto a FNRH não for implantada).

**Arquivo que deverá ser atualizado depois da implantação**: `DADOS_OFICIAIS_ATENDIMENTO_VILLA_ARAGUA.md` (item 71), `ROTEIRO_RECEPCIONISTA_IA.md` (seção 11D), `PROMPT_RECEPCIONISTA_IA_WHATSAPP.md` (seção 11D).

### Detalhes operacionais da churrasqueira da Casa Arágua

Durante o teste do tema "Churrasqueira", a IA aprovou todos os 30 cenários e diferenciou corretamente Casa Arágua e Pousada Arágua. Porém, ficou identificada uma lacuna: a Casa Arágua tem churrasqueira exclusiva documentada, mas os detalhes operacionais específicos ainda não estão confirmados.

**Perguntas para decisão de Renildo**:
- A churrasqueira da Casa Arágua segue o mesmo horário da Pousada ou tem regra própria?
- O carvão é por conta do hóspede também na Casa?
- A Casa fornece utensílios básicos para churrasco?
- Quais utensílios são fornecidos: grelha, espetos, pegador, faca, tábua, acendedor, outros?
- Existe alguma taxa separada para uso da churrasqueira da Casa?
- A limpeza final da churrasqueira da Casa fica com a equipe ou há alguma orientação específica para o hóspede?
- Há alguma restrição específica para uso da churrasqueira da Casa em relação a visitantes, música, festas ou horário de silêncio?

**Observações complementares identificadas no teste consolidado de "Regras da Casa Arágua"**:
- A Casa Arágua possui um espaço próprio de lavanderia?
- O estacionamento exclusivo da Casa Arágua para até 3 carros é garagem coberta ou área aberta?

**Situação atual na IA**: a IA pode afirmar que a Casa Arágua possui churrasqueira exclusiva e estacionamento exclusivo para até 3 carros, mas não deve afirmar que é garagem coberta sem confirmação, nem afirmar que a Casa possui lavanderia própria ou máquina de lavar sem confirmação oficial. Deve reconhecer o limite e encaminhar ao WhatsApp oficial 47 99201-4117 quando o hóspede perguntar detalhes não documentados.

**Status (Propagação 2 — 2026-07-07): Parcialmente resolvida.**

- ✅ Resolvida — mesmo horário da Pousada ou regra própria: regra própria (respeita o horário de silêncio das 22h às 8h, sem o limite específico de 3 horas/uso até 22h da Pousada) — item oficial 48.
- ✅ Resolvida — carvão por conta do hóspede também na Casa — item oficial 48.
- ✅ Resolvida — a Casa fornece utensílios básicos para churrasco (resposta genérica) — item oficial 48.
- ❌ **Continua pendente** — quais utensílios exatos são fornecidos (grelha, espetos, pegador, faca, tábua, acendedor, outros): o item 48 explicitamente mantém a orientação de não detalhar a lista sem conferência final. Não foi resolvida pelos itens 46–70.
- ❌ **Continua pendente** — a limpeza final da churrasqueira da Casa fica com a equipe ou há orientação específica para o hóspede: não coberta pelos itens 46–70.
- ✅ Resolvida — restrição para uso da churrasqueira da Casa em relação a visitantes/festas/horário de silêncio — itens oficiais 48 e 66.
- ✅ Resolvida — a Casa Arágua possui espaço próprio de lavanderia: não possui — item oficial 49.
- ✅ Resolvida — estacionamento exclusivo da Casa Arágua é garagem coberta ou área aberta: área aberta/exclusiva — item oficial 50.

**Confirmado no reteste/reconstrução do tema "Regras da Casa Arágua" (2026-07-10)** — `RESULTADO_TESTE_REGRAS_DA_CASA_ARAGUA_RODADA_1_RECEPCIONISTA_IA_VILLA_ARAGUA.md`: as duas pendências abaixo seguem confirmadas como as únicas ainda em aberto neste bloco; nenhuma pendência nova de churrasqueira foi identificada. Foi adicionada, nesse mesmo reteste, uma pendência relacionada mas distinta: confirmar se existe caução para danos maiores na Casa Arágua fora do contexto de eventos (ver seção "Eventos comerciais..." abaixo).

**Reafirmado no reteste dedicado do tema "Churrasqueira" (2026-07-12)** — `RESULTADO_TESTE_CHURRASQUEIRA_RODADA_1_RECEPCIONISTA_IA_VILLA_ARAGUA.md`: as duas pendências abaixo continuam sendo as únicas em aberto neste bloco; nenhuma pendência nova foi identificada. A IA respondeu corretamente em cenários novos de segurança (fogo aceso sem supervisão, chuva, vento, criança por perto), sem inventar orientação perigosa.

**Prioridade**: Média — não bloqueia o atendimento, mas melhora a clareza comercial e operacional da Casa Arágua. As duas pendências remanescentes (utensílios detalhados e responsabilidade pela limpeza final da churrasqueira) continuam com a prioridade original.

**Arquivo que deverá ser atualizado depois**: `DADOS_OFICIAIS_ATENDIMENTO_VILLA_ARAGUA.md`, `ROTEIRO_RECEPCIONISTA_IA.md`, `PROMPT_RECEPCIONISTA_IA_WHATSAPP.md`, `GUIA_DIGITAL_HOSPEDE_VILLA_ARAGUA.md` — apenas para as duas pendências remanescentes.

### Eventos comerciais, fornecedores externos e visitantes rápidos

Durante o teste do tema "Visitantes / festas / silêncio", a IA aprovou todos os 50 cenários e demonstrou comportamento seguro. Porém, foram identificadas algumas decisões comerciais que podem ser formalizadas se Renildo quiser aumentar a precisão da IA.

**Perguntas para decisão de Renildo**:
- A Casa Arágua permite ensaio fotográfico com equipe externa?
- A Casa Arágua permite casamento pequeno ou mini-evento?
- A Casa Arágua permite fornecedor externo de decoração?
- A Casa Arágua permite cozinheiro ou churrasqueiro externo?
- A Casa Arágua permite DJ ou música contratada?
- A Pousada permite algum tipo de evento pequeno ou confraternização mediante autorização?
- Existe taxa de visitante?
- Existe taxa de evento?
- Existe caução para eventos, fornecedores ou uso especial?
- Como diferenciar visitante social de entregador ou prestador rápido?
- Entregador pode entrar ou deve aguardar na entrada?
- Visitante pode estacionar em vaga da Casa ou da Pousada?
- Existe alguma política específica para fornecedores externos acessarem a propriedade?

**Situação atual na IA**: a IA deve tratar qualquer visitante, festa, evento, fornecedor externo, ensaio fotográfico, casamento pequeno, DJ, decoração ou serviço contratado como situação que exige autorização prévia da equipe. A IA não deve prometer liberação, taxa, caução, cobrança, estacionamento, acesso ou exceção sem confirmação oficial. O WhatsApp oficial para confirmação é 47 99201-4117.

**Status (Propagação 2 — 2026-07-07): ✅ Resolvida.** Todas as perguntas desta subseção foram cobertas pelos itens oficiais 64 a 67: ensaio fotográfico, casamento pequeno, fornecedor de decoração, cozinheiro/churrasqueiro externo e DJ na Casa (item 66); evento pequeno na Pousada (item 67); ausência de taxa fixa de visitante e de evento, e de caução fixa de evento (itens 64 e 66); regra geral de visitante social, entregador e prestador rápido, e estacionamento de visitante (itens 64 e 65).

**Auditoria de 2026-07-10**: o registro original desta subseção citava "todos os 50 cenários" do tema "Visitantes / festas / silêncio", mas não havia arquivo individual nem lista rastreável dessas 50 perguntas no banco de perguntas-base — o tema foi reclassificado como documentação incompleta e reconstruído com 30 perguntas individualmente registradas (`RESULTADO_TESTE_VISITANTES_FESTAS_SILENCIO_RODADA_1_RECEPCIONISTA_IA_VILLA_ARAGUA.md`). O reteste confirmou que os itens 64–67 seguem corretamente aplicados e identificou **uma pendência nova**: não há limite de frequência de visitas documentado ao longo de uma mesma estadia (ex.: visitante todos os dias). Também ficou em aberto, de forma geral (não restrita a eventos), se existe caução para danos maiores na Casa Arágua — a IA trata hoje como "avaliação caso a caso", o que é seguro, mas não há confirmação formal de que não existe caução.

**Prioridade**: Baixa a média — não bloqueia a operação padrão, mas pode virar oportunidade comercial ou evitar conflito se esses pedidos forem recorrentes.

**Arquivo que deverá ser atualizado depois**: `DADOS_OFICIAIS_ATENDIMENTO_VILLA_ARAGUA.md` (✅ já atualizado — Propagação 1), `ROTEIRO_RECEPCIONISTA_IA.md`, `PROMPT_RECEPCIONISTA_IA_WHATSAPP.md`, `GUIA_DIGITAL_HOSPEDE_VILLA_ARAGUA.md` — ainda pendentes de propagação.

### Detalhes finos da política pet

Durante o teste do tema "Pet", a IA aprovou todos os 30 cenários e demonstrou que a base atual é sólida. Porém, foram identificadas três pendências de dado que podem deixar a política ainda mais clara.

**Perguntas para decisão de Renildo**:
- A regra de "pet pequeno" inclui gatos e outras espécies ou há alguma particularidade?
- Existe alguma restrição de circulação de pet em áreas específicas além de recepção, cozinha e lavanderia, como piscina, jardim ou área de lazer?
- Existe um limite objetivo de peso em kg para definir "pet pequeno", ou a avaliação deve continuar qualitativa, caso a caso?

**Situação atual na IA**: a IA pode afirmar que pet pequeno é aceito, sem taxa, mediante aviso prévio, tanto na Pousada Arágua quanto na Casa Arágua. Para pet grande, mais de um pet, comportamento especial ou dúvidas específicas, deve pedir informações e encaminhar para confirmação pelo WhatsApp oficial 47 99201-4117.

**Status (Propagação 2 — 2026-07-07): ✅ Resolvida.** As três perguntas foram cobertas: pet pequeno inclui gato, sob aviso prévio e confirmação da equipe, outras espécies sob consulta (item oficial 60); circulação em jardim (sim, com supervisão) e piscina (cautela/sob consulta), áreas restritas mantidas em recepção/cozinha/lavanderia (item oficial 61); sem limite fixo em kg, avaliação continua qualitativa (item oficial 60).

**Prioridade**: Baixa a média — a base atual já é segura e impede autorização indevida, mas esses dados aumentariam a clareza operacional.

**Arquivo que deverá ser atualizado depois**: `DADOS_OFICIAIS_ATENDIMENTO_VILLA_ARAGUA.md` (✅ já atualizado — Propagação 1), `ROTEIRO_RECEPCIONISTA_IA.md`, `PROMPT_RECEPCIONISTA_IA_WHATSAPP.md`, `GUIA_DIGITAL_HOSPEDE_VILLA_ARAGUA.md` — ainda pendentes de propagação.

### Crianças, berço, cama extra e itens de bebê

Durante o teste do tema "Crianças / capacidade / cama extra", a IA aprovou todos os 40 cenários e demonstrou que a base atual é robusta, especialmente na distinção entre gratuidade infantil e capacidade máxima da acomodação. Porém, foram identificadas algumas pendências de dado que podem deixar a política ainda mais clara.

**Perguntas para decisão de Renildo**:
- Existe alguma solução de cama extra, colchão extra ou sofá-cama extra para grupos que ainda cabem na capacidade, mas querem mais conforto de cama?
- Quantos berços portáteis estão disponíveis?
- Existe cadeira de alimentação para bebê?
- Existe banheira de bebê?
- Existe alguma orientação oficial sobre segurança em escadas/mezaninos para crianças pequenas?
- Há algum portão de segurança, grade, proteção física ou apenas orientação verbal?
- Como deve ser tratada a tarifa de crianças acima de 6 anos: sempre tarifa normal conforme composição do grupo ou precisa de avaliação caso a caso?

**Situação atual na IA**: a IA pode afirmar que crianças até 6 anos são gratuitas, mas deve sempre respeitar a capacidade máxima de cada acomodação. A IA pode informar que há berço portátil gratuito mediante aviso prévio, mas não deve confirmar quantidade de berços, cama extra, colchão extra, sofá-cama extra, cadeira de alimentação, banheira ou proteção física em escadas/mezaninos sem confirmação oficial.

**Status (Propagação 2 — 2026-07-07): Parcialmente resolvida.**

- ✅ Resolvida — cama extra, colchão extra e sofá-cama extra: nenhum dos três existe como solução/serviço padrão — item oficial 63.
- ✅ Resolvida — quantidade de berços portáteis: 3 — item oficial 62.
- ✅ Resolvida — cadeira de alimentação para bebê: não existe — item oficial 63.
- ✅ Resolvida — banheira de bebê: não existe — item oficial 63.
- ✅ Resolvida — orientação oficial sobre segurança em escadas/mezaninos: não há proteção física documentada (portão/grade); a orientação é verbal, de atenção redobrada dos responsáveis — item oficial 63 (reforça o item 7 já oficial).
- ❌ **Continua pendente** — como deve ser tratada a tarifa de crianças acima de 6 anos (sempre tarifa normal conforme composição do grupo, ou avaliação caso a caso): não foi respondida nos Blocos 2 a 8 do questionário, portanto não está coberta pelos itens 46–70. *(Observação: o item oficial 45, já existente antes desta rodada, trata da gratuidade até 6 anos, mas não define explicitamente a regra para acima de 6 anos — como esse item está fora do intervalo 46–70, esta pendência não foi dada como resolvida nesta propagação, por segurança.)*

**Prioridade**: Média — a base atual já evita o risco mais crítico (ultrapassar capacidade); resta apenas a definição da tarifa de crianças acima de 6 anos.

**Arquivo que deverá ser atualizado depois**: `DADOS_OFICIAIS_ATENDIMENTO_VILLA_ARAGUA.md` (✅ já atualizado — Propagação 1, exceto tarifa de criança acima de 6 anos), `ROTEIRO_RECEPCIONISTA_IA.md`, `PROMPT_RECEPCIONISTA_IA_WHATSAPP.md`, `GUIA_DIGITAL_HOSPEDE_VILLA_ARAGUA.md` — ainda pendentes de propagação para os itens resolvidos.

### Early check-in, late check-out, bagagem e uso de áreas antes/depois da estadia

Durante o teste do tema "Check-in / check-out / early check-in / late check-out", a IA aprovou todos os 40 cenários e demonstrou que a base atual é sólida nos horários oficiais e nas restrições de acesso. Porém, foram identificadas pendências de dado que podem melhorar a clareza operacional.

**Perguntas para decisão de Renildo**:
- Existe cobrança para early check-in? Se sim, qual valor ou critério?
- Existe cobrança para late check-out? Se sim, qual valor ou critério?
- Early check-in e late check-out são sempre apenas mediante disponibilidade?
- É permitido deixar bagagem antes do check-in?
- É permitido deixar bagagem depois do check-out?
- Existe algum local seguro/documentado para guardar bagagem?
- O hóspede pode usar piscina antes do check-in se chegar mais cedo?
- O hóspede pode usar churrasqueira antes do check-in?
- O hóspede pode usar piscina depois do check-out?
- O hóspede pode usar churrasqueira depois do check-out?
- O hóspede pode tomar café da manhã depois do check-out?
- Existe alguma janela de tolerância oficial para entrada, saída ou uso de áreas comuns?

**Situação atual na IA**: a IA pode afirmar que o check-in é a partir das 15h e o check-out até 11h. A IA deve tratar early check-in, late check-out, guarda de bagagem e uso de áreas antes/depois da estadia como situações dependentes de disponibilidade e confirmação pelo WhatsApp oficial 47 99201-4117. A IA não deve prometer gratuidade, cobrança, liberação, tolerância, guarda de bagagem ou uso de áreas sem confirmação oficial.

**Status (Propagação 2 — 2026-07-07): ✅ Resolvida.** Early check-in e late check-out são sob consulta e disponibilidade, sem valor fixo oficial; não existe tolerância oficial automática para check-out (item oficial 55). Guarda de bagagem antes do check-in ou depois do check-out é sob consulta (principalmente Pousada; Casa sob consulta específica), sem local seguro fixo garantido; uso de piscina/churrasqueira antes do check-in ou depois do check-out não é automático; café da manhã depois do check-out não é regra automática (item oficial 56). A decisão oficial, em todos os casos, é manter "sob consulta/disponibilidade" — não foi criada uma regra fixa ou valor monetário, o que já era esperado (ver também seção 6, que trata early check-in/late check-out como itens que devem permanecer caso a caso).

**Prioridade**: Média a alta — o tema afeta diretamente a expectativa operacional do hóspede, chegada, saída e possíveis conflitos.

**Arquivo que deverá ser atualizado depois**: `DADOS_OFICIAIS_ATENDIMENTO_VILLA_ARAGUA.md` (✅ já atualizado — Propagação 1), `ROTEIRO_RECEPCIONISTA_IA.md`, `PROMPT_RECEPCIONISTA_IA_WHATSAPP.md`, `GUIA_DIGITAL_HOSPEDE_VILLA_ARAGUA.md` — ainda pendentes de propagação.

### Café da manhã, restrições alimentares e pacote da Casa Arágua

Durante o teste do tema "Café da manhã", a IA aprovou todos os 40 cenários e demonstrou que a base atual é sólida no núcleo do tema: café incluso na Pousada, não incluso por padrão na Casa, horário das 8h às 10h e entrega na acomodação. Porém, foram identificadas pendências de dado que podem melhorar a clareza comercial e operacional.

**Perguntas para decisão de Renildo**:
- Existe cardápio detalhado oficial do café da manhã?
- Quais itens podem ser mencionados com segurança pela IA?
- Existe processo formal para restrições alimentares mais sérias, como sem glúten, sem lactose, vegano ou alergias?
- A equipe consegue atender preferências simples além de sem leite, sem queijo e mais frutas?
- Existe flexibilidade real para café fora do horário das 8h às 10h?
- Existe alguma possibilidade de café antecipado para quem sai muito cedo para passeio, aeroporto ou estrada?
- Existe possibilidade de café depois das 10h?
- Existe algum pacote especial de café para a Casa Arágua?
- Se sim, qual valor, condições, antecedência necessária e disponibilidade?
- O café da Casa, caso contratado, seria entregue na própria Casa?
- Existe café para visitantes?
- Existe café especial para aniversário, cesta romântica ou ocasião especial?
- A quantidade de porções por bandeja deve ser explicada como "conforme número de hóspedes da reserva" ou existe outra regra?

**Situação atual na IA**: a IA pode afirmar que o café da manhã está incluso na Pousada Arágua, é servido das 8h às 10h e é entregue diretamente na acomodação. A IA deve informar que a Casa Arágua não inclui café da manhã por padrão. Para pacote especial na Casa, restrições alimentares, horários fora da faixa, café para visitantes, café antes/depois da estadia ou pedidos especiais, a IA deve reconhecer o limite e encaminhar para confirmação pelo WhatsApp oficial 47 99201-4117.

**Status (Propagação 2 — 2026-07-07): Parcialmente resolvida.**

- ✅ Resolvida — cardápio detalhado oficial e itens que podem ser mencionados com segurança: pães variados, pão de queijo, frutas, suco, iogurte, granola, mel, manteiga, frios, café, leite e bolos, como composição habitual — item oficial 57.
- ✅ Resolvida — processo para restrições sérias (sem glúten, sem lactose, vegano, alergias): nenhuma é garantida, sempre sob consulta e aviso prévio — item oficial 58.
- ⚠️ **Parcialmente resolvida** — preferências simples além de sem leite/sem queijo/mais frutas: o item oficial 58 confirma essas três preferências como atendíveis sob aviso prévio, mas não define explicitamente se a equipe atende preferências simples *além* dessas três — recomenda-se manter esse recorte específico em aberto até nova decisão de Renildo.
- ✅ Resolvida — flexibilidade para café fora do horário 8h–10h, café antecipado e café depois das 10h: não são automáticos, somente sob consulta e disponibilidade — item oficial 59.
- ✅ Resolvida — pacote especial de café para a Casa Arágua, valor, condições, antecedência e entrega na própria Casa: R$ 80,00/pessoa, sob consulta, com solicitação antecipada, entrega na Casa possível sob consulta — item oficial 47.
- ✅ Resolvida — café para visitantes, café de aniversário e cesta romântica: nenhum automático, sempre sob consulta — item oficial 59.
- ❌ **Continua pendente** — quantidade de porções por bandeja ("conforme número de hóspedes da reserva" ou outra regra): não foi respondida nos Blocos 2 a 8 do questionário, portanto não está coberta pelos itens 46–70.
- ❌ **Nova pendência identificada no reteste do tema Café da manhã (2026-07-10)** — o valor de R$ 80,00/pessoa do café opcional da Casa Arágua (item 47) não define se é cobrado por dia de estadia, por período/café contratado, ou como valor único pela hospedagem. Também não está confirmado se é possível contratar o café da Casa em apenas um dos dias da estadia, nem se o cardápio do pacote da Casa é o mesmo cardápio habitual da Pousada (item 57). Detalhe completo em `RESULTADO_TESTE_CAFE_DA_MANHA_RODADA_1_RECEPCIONISTA_IA_VILLA_ARAGUA.md`. Enquanto não houver decisão, a IA trata como "sob consulta" — comportamento já validado como seguro no reteste.

**Prioridade**: Média — a base atual já evita promessas indevidas; restam a quantidade de porções por bandeja, o recorte fino de preferências simples além das três já confirmadas, e a unidade de tempo/escopo do valor R$ 80,00 da Casa Arágua.

**Arquivo que deverá ser atualizado depois**: `DADOS_OFICIAIS_ATENDIMENTO_VILLA_ARAGUA.md` (✅ já atualizado — Propagação 1, exceto os dois pontos remanescentes), `ROTEIRO_RECEPCIONISTA_IA.md`, `PROMPT_RECEPCIONISTA_IA_WHATSAPP.md`, `GUIA_DIGITAL_HOSPEDE_VILLA_ARAGUA.md` — ainda pendentes de propagação para os itens resolvidos.

---

## 3. Pendências de política comercial e cancelamento

| Pergunta pendente | Pousada Arágua | Casa Arágua | Ambos | Status (Propagação 2 — 2026-07-07) |
|---|---|---|---|---|
| Como funciona a remarcação/troca de data na prática? | Pendente | Pendente | ✔ Regra hoje é idêntica em estrutura (segue o mesmo prazo de aviso do cancelamento), mas sem detalhamento operacional | ✅ Resolvida — item oficial 53: sob consulta, conforme antecedência, disponibilidade e diferença de tarifa. Formaliza a política ("sob consulta"), sem criar um procedimento operacional detalhado adicional |
| A nova data depende de disponibilidade? | Pendente | Pendente | ✔ | ✅ Resolvida — item oficial 53 |
| Se a nova data for mais cara, cobra diferença? | Pendente | Pendente | ✔ | ✅ Resolvida — item oficial 53 (tratado dentro de "diferença de tarifa", sob consulta, sem regra fixa de cobrança automática) |
| Se a nova data for mais barata, mantém valor, devolve diferença ou vira crédito? | Pendente | Pendente | ✔ | ✅ Resolvida — item oficial 53 (mesma lógica de "diferença de tarifa" sob consulta; não há regra automática de devolução/crédito) |
| Existe flexibilidade para doença/força maior? | Pendente | Pendente | ✔ — hoje não há nenhuma cláusula de força maior documentada para nenhum dos dois produtos | ✅ Resolvida — item oficial 54: tratado caso a caso, sem promessa automática de reembolso, crédito ou remarcação |
| Existe crédito para uso futuro em vez de devolução? | Pendente | Pendente | ✔ — hoje só existem duas opções documentadas: devolução de 90% dentro do prazo, ou nenhuma devolução após | ✅ Resolvida — item oficial 53: sob consulta; quando aprovado, prazo geralmente de 6 meses |
| É possível reduzir diárias de uma reserva já feita? | Pendente | Pendente | ✔ | ✅ Resolvida — item oficial 54: sob consulta; devolução/crédito não é automático |
| É possível transferir reserva para outra pessoa? | Pendente | Pendente | ✔ | ✅ Resolvida — item oficial 53: sob consulta e validação da equipe |
| Como tratar reserva ainda não confirmada por falta de pagamento? | Já parcialmente coberto — reserva só é considerada confirmada após pagamento validado | Mesma regra já se aplica | ✔ — resolvido em nível de princípio, mas vale confirmar se há algum procedimento adicional | ✅ Reforçada — item oficial 52 (reserva só confirmada após pagamento/sinal validado; check-in não liberado sem condição de entrada validada) |
| Como tratar exceções comerciais pedidas diretamente pelo hóspede? | Sempre escalar para humano (regra já existente) | Mesma regra | ✔ — já coberto pela regra de segurança, sem necessidade de mudança, mas fica registrado aqui para visibilidade | Sem alteração — já coberta pela regra de segurança existente; não fazia parte dos Blocos 2 a 8 |

**Nota**: os prazos-base de cancelamento já estão corretamente diferenciados e validados nos testes — **Pousada Arágua: 7 dias de antecedência; Casa Arágua: 21 dias de antecedência** — ambos com devolução de 90% dentro do prazo e nenhuma devolução após. Essa parte **não** é pendência; está confirmada e funcionando corretamente.

**Observação (Propagação 2 — 2026-07-07)**: todas as linhas desta tabela foram resolvidas ao nível de **decisão de princípio** ("sob consulta", "caso a caso", sem promessa automática) pelos itens oficiais 51 a 54. Nenhuma delas ganhou um procedimento operacional passo a passo mais detalhado do que isso — o que é consistente com as respostas de Renildo no questionário, que optou por manter flexibilidade caso a caso em vez de regras fixas.

---

## 4. Pendência específica da Casa Arágua — taxa de limpeza

Esta é considerada a pendência mais crítica da Rodada 1, por ter aparecido repetidamente em diferentes temas de teste (desconto, cancelamento da Casa) sem nunca ter sido confirmada:

- Existe taxa de limpeza separada na Casa Arágua?
- Ela é obrigatória para todas as reservas?
- Está incluída no valor da diária ou é cobrada à parte?
- Em caso de cancelamento, essa taxa é devolvida, retida ou tratada de forma diferente do restante do valor?
- Em caso de remarcação, a taxa permanece válida para a nova data?
- A Recepcionista IA pode mencionar essa taxa diretamente ao hóspede, ou deve sempre encaminhar esse assunto para a equipe confirmar?

**Status (Propagação 3 — 2026-07-12): ✅ Totalmente resolvida.** A pendência mais crítica da Rodada 1 foi integralmente respondida — valor, obrigatoriedade, cobrança à parte, efeito em cancelamento e efeito em remarcação. Ver Decisão 1 de `DECISOES_PENDENTES_RENILDO_FECHAMENTO_RODADA_1_VILLA_ARAGUA_IA.md`.

- ✅ Resolvida — existe taxa de limpeza separada: sim, R$ 450,00 por estadia — item oficial 46.
- ✅ Resolvida — é obrigatória para todas as reservas: sim — item oficial 46.
- ✅ Resolvida — está incluída na diária ou cobrada à parte: cobrada à parte — item oficial 46.
- ✅ Resolvida — a IA pode mencionar a taxa diretamente ao hóspede: sim, agora é dado oficial validado (item 46), a IA pode informar o valor com confiança.
- ✅ **Resolvida em 2026-07-12** — em caso de cancelamento sem check-in/uso da Casa, a taxa é devolvida integralmente (tratamento próprio, não segue o percentual de retenção da diária); com check-in/uso já ocorrido, sem promessa automática — item 46 atualizado, Decisão 1 de `DECISOES_PENDENTES_RENILDO_FECHAMENTO_RODADA_1_VILLA_ARAGUA_IA.md`.
- ✅ **Resolvida em 2026-07-12** — em caso de remarcação aprovada, a taxa já paga é transferida para a nova data, sem nova cobrança — item 46 atualizado, Decisão 1 de `DECISOES_PENDENTES_RENILDO_FECHAMENTO_RODADA_1_VILLA_ARAGUA_IA.md`.

**Esta pendência está totalmente resolvida.** A IA agora aplica a regra oficial de cancelamento/remarcação da taxa de limpeza, sem inventar nem promissas indevidas fora dos cenários definidos.

---

## 5. Pendência técnica operacional — `PLAYBOOK_ATENDIMENTO_WHATSAPP.md`

O teste do tema "Hóspede irritado" aprovou integralmente o **tom** da Recepcionista IA diante de problemas técnicos comuns (Wi-Fi, ar-condicionado, energia, piscina), mas o **conteúdo técnico** desses fluxos depende do `PLAYBOOK_ATENDIMENTO_WHATSAPP.md`, que na época ainda **não havia sido auditado** — esse arquivo não fazia parte dos arquivos de referência testados até aquele ponto da Rodada 1.

O arquivo foi lido e auditado pela primeira vez no teste do tema "Wi-Fi da Casa Arágua". O resultado confirma a suspeita e revela um problema mais sério do que uma simples pendência de conteúdo:

### Referência quebrada ao `PLAYBOOK_ATENDIMENTO_WHATSAPP.md`

**Achado**: `ROTEIRO_RECEPCIONISTA_IA.md` e `PROMPT_RECEPCIONISTA_IA_WHATSAPP.md` apontam para a **seção 6** do `PLAYBOOK_ATENDIMENTO_WHATSAPP.md` como se essa seção tivesse fluxo técnico para problemas de Wi-Fi, ar-condicionado, energia, piscina e lock box.

**Problema**: a seção 6 real do `PLAYBOOK_ATENDIMENTO_WHATSAPP.md` é **"Como indicar cada acomodação"** e não contém fluxo técnico algum. O Playbook inteiro (12 seções) também não possui fluxo operacional suficiente para troubleshooting de Wi-Fi, internet, roteador, ar-condicionado, energia, piscina ou técnico — a referência está incorreta/quebrada.

**Risco**: a IA pode ficar sem passo a passo operacional real para problemas técnicos e depender apenas de escalonamento manual. O comportamento atual é seguro, pois ela não inventa (reconhece o limite e escala para o WhatsApp oficial), mas o documento citado não cumpre a função indicada pelo Roteiro/Prompt.

**Achado complementar**: o `PLAYBOOK_ATENDIMENTO_WHATSAPP.md` também parece defasado em relação à Base de Atendimento Fase 1 — sua seção 12 ("Dados que precisam ser padronizados por Renildo") ainda cita a distância antiga da Casa Arágua ("~180 metros", já corrigida para 250m em `DADOS_OFICIAIS_ATENDIMENTO_VILLA_ARAGUA.md`) e a política antiga de pet (só a Suíte Wood, já superada) — ambas já resolvidas e propagadas há tempo nos demais arquivos oficiais.

**Status: Parcialmente resolvido (2026-07-04).**

**Explicação**: a referência cruzada quebrada foi corrigida nos arquivos operacionais `ROTEIRO_RECEPCIONISTA_IA.md` e `PROMPT_RECEPCIONISTA_IA_WHATSAPP.md` (Parte 1 e Parte 2). A IA não aponta mais para a seção 6 do `PLAYBOOK_ATENDIMENTO_WHATSAPP.md` como se ela tivesse fluxo técnico — a orientação foi substituída por uma regra segura: acolher o hóspede, pedir informações objetivas e encaminhar pelo WhatsApp oficial 47 99201-4117, sem inventar diagnóstico, senha, código, localização de equipamento, prazo, técnico imediato, prioridade ou compensação. O `PLAYBOOK_ATENDIMENTO_WHATSAPP.md` em si não foi alterado, e nenhum novo fluxo técnico detalhado foi criado.

**Status (Propagação 2 — 2026-07-07): Parcialmente resolvida — o fluxo técnico em si foi criado; a auditoria do Playbook como documento geral continua pendente.**

**Ainda pendente**:
- Auditar o `PLAYBOOK_ATENDIMENTO_WHATSAPP.md` como documento geral.
- Decidir se ele será atualizado, arquivado como histórico ou substituído.
- Decidir se o conteúdo técnico de `OPERACAO/PROBLEMAS E SOLUÇÕES.docx` deve ser formalizado na base operacional da IA.

**Resolvido nesta rodada** (não fazem mais parte do "ainda pendente"):
- ~~Criar, se necessário, um fluxo técnico seguro para Wi-Fi, ar-condicionado, energia, piscina, acesso e equipamentos.~~ — ✅ **Resolvida** — itens oficiais 68, 69 e 70 (Wi-Fi, energia, ar-condicionado, piscina e churrasqueira; acionamento e critério de escalonamento Renildo x equipe x IA). Acesso/lock box continua tratado separadamente pela regra 11B/item 30, não fazia parte do escopo do Bloco 8.
- ~~Esse fluxo futuro não deve prometer prazo, técnico imediato, prioridade, desconto, reembolso, cortesia ou compensação.~~ — ✅ **Resolvida** — item oficial 69 confirma explicitamente: sem técnico de plantão, sem prazo fixo, sem compensação automática.

Recomenda-se uma auditoria futura dedicada a esse arquivo, cobrindo especificamente:

- Wi-Fi
- Ar-condicionado
- Energia
- Piscina
- Lock box / acesso, caso ainda haja referência técnica desatualizada ali (dado que a regra 11B já trata o tema de acesso separadamente)
- Outros problemas técnicos comuns não listados aqui

---

## 6. Dúvidas que devem continuar caso a caso

As situações abaixo foram testadas e aprovadas, mas foram identificadas como **decisões pontuais que provavelmente não devem virar regra fixa/automática**, e sim continuar sendo sempre escaladas para verificação humana:

- Early check-in
- Late check-out
- Exceção para pet de porte grande ou múltiplos pets
- Festa/evento pontual autorizado
- Exceções comerciais em geral
- Condição real do mar/praia no dia (clima, vento, segurança para banho)
- Confirmação real de que uma reserva foi cancelada pela Villa (quando o hóspede questiona isso)
- Grupo maior que a capacidade máxima da Casa Arágua (6 pessoas)
- Casos especiais fora da política documentada

---

## 7. Priorização sugerida

### Alta prioridade
- ~~Taxa de limpeza da Casa Arágua~~ — ✅ **totalmente resolvida em 2026-07-12** — item oficial 46 (valor, obrigatoriedade e efeitos em cancelamento/remarcação) (ver seção 4)
- ~~Contingência de acesso — canal alternativo de contato~~ — ✅ **resolvida em 2026-07-12** — ligação de voz pelo número oficial (ver seção 2B); tecnologia física de contingência segue **pendente de implantação**
- ~~Identificação no check-in / pessoa não cadastrada — regra de segurança~~ — ✅ **resolvida em 2026-07-12** — ver seção 2C; procedimento definitivo depende da **implantação da FNRH Digital** (nova pendência prioritária, ver seção 2D)
- ~~Cartão parcelado / formas de pagamento~~ — ✅ **resolvida em 2026-07-07** — item oficial 51
- ~~Remarcação e diferença de valor~~ — ✅ **resolvida em 2026-07-07** — item oficial 53
- ~~Crédito para uso futuro~~ — ✅ **resolvida em 2026-07-07** — item oficial 53
- Auditoria do `PLAYBOOK_ATENDIMENTO_WHATSAPP.md` como documento geral *(ainda pendente — ver seção 5)*
- ~~Correção da referência cruzada quebrada ao Playbook em `ROTEIRO_RECEPCIONISTA_IA.md` e `PROMPT_RECEPCIONISTA_IA_WHATSAPP.md`~~ — **concluída em 2026-07-04** (ver seção 5)
- ~~Definição de um fluxo técnico seguro para Wi-Fi e problemas operacionais comuns (Wi-Fi, ar-condicionado, energia, piscina)~~ — ✅ **resolvida em 2026-07-07** — itens oficiais 68–70 (ver seção 5)
- Wi-Fi da Casa *(nota: já confirmado e propagado — ver observação abaixo)*

### Média a alta prioridade
- ~~Early check-in, late check-out, bagagem e uso de áreas antes/depois da estadia~~ — ✅ **resolvida em 2026-07-07** — itens oficiais 55–56 *(engloba e amplia a pendência "Deixar bagagem antes do check-in", listada abaixo)*

### Média prioridade
- Restaurante próprio / almoço / jantar
- ~~Máquina de lavar da Casa~~ — ✅ **resolvida em 2026-07-07** — item oficial 49
- Cofre nas acomodações
- ~~Deixar bagagem antes do check-in~~ — ✅ **resolvida em 2026-07-07** — item oficial 56
- Detalhes operacionais da churrasqueira da Casa Arágua *(parcialmente resolvida em 2026-07-07 — itens 48–50; reteste concluído em 2026-07-10 dentro do tema "Regras da Casa Arágua", `RESULTADO_TESTE_REGRAS_DA_CASA_ARAGUA_RODADA_1_RECEPCIONISTA_IA_VILLA_ARAGUA.md`; restam utensílios detalhados e limpeza final, ver seção 2)*
- Crianças, berço, cama extra e itens de bebê *(parcialmente resolvida em 2026-07-07 — itens 62–63; resta a tarifa de criança acima de 6 anos, ver seção 2)*
- Café da manhã, restrições alimentares e pacote da Casa Arágua *(parcialmente resolvida em 2026-07-07 — itens 47, 57–59; reteste concluído em 2026-07-10, `RESULTADO_TESTE_CAFE_DA_MANHA_RODADA_1_RECEPCIONISTA_IA_VILLA_ARAGUA.md`; restam quantidade de porções por bandeja, recorte fino de preferências simples e unidade de tempo/escopo do valor R$ 80,00 da Casa, ver seção 2)*

### Baixa a média prioridade
- ~~Detalhes finos da política pet: espécies (gatos e outras), áreas de circulação além de recepção/cozinha/lavanderia, e limite objetivo de peso em kg~~ — ✅ **resolvida em 2026-07-07** — itens oficiais 60–61
- Transfer e passeio de barco
- Eventos comerciais, fornecedores externos e visitantes rápidos *(resolvida em 2026-07-07 — itens oficiais 64–67; reteste concluído em 2026-07-10, `RESULTADO_TESTE_VISITANTES_FESTAS_SILENCIO_RODADA_1_RECEPCIONISTA_IA_VILLA_ARAGUA.md`; restam limite de frequência de visitas e caução para danos maiores fora do contexto de eventos, ver seção 2)*

### Baixa prioridade
- Carregador para carro elétrico
- Desconto para morador de Bombinhas
- Supermercado maior próximo

**Observação sobre Wi-Fi da Casa**: o Wi-Fi da Casa Arágua (rede e senha) já foi confirmado e propagado para `DADOS_OFICIAIS_ATENDIMENTO_VILLA_ARAGUA.md`, `ROTEIRO_RECEPCIONISTA_IA.md`, `PROMPT_RECEPCIONISTA_IA_WHATSAPP.md` e `GUIA_DIGITAL_HOSPEDE_VILLA_ARAGUA.md` em rodada anterior à Rodada 1 de testes atual. Mantido aqui na lista de alta prioridade apenas como referência de contexto — **não é mais uma pendência em aberto**.

---

## 8. Próximo passo sugerido

Após Renildo responder as pendências acima, os dados confirmados devem ser propagados com cuidado, um item por vez, para:

- `DADOS_OFICIAIS_ATENDIMENTO_VILLA_ARAGUA.md`
- `ROTEIRO_RECEPCIONISTA_IA.md`
- `PROMPT_RECEPCIONISTA_IA_WHATSAPP.md`
- `GUIA_DIGITAL_HOSPEDE_VILLA_ARAGUA.md`, quando fizer sentido para o hóspede final
- `ROTEIRO_TESTE_MANUAL_RECEPCIONISTA_IA_VILLA_ARAGUA.md`, quando a atualização for resultado direto de um teste já registrado

Recomenda-se seguir o mesmo padrão já validado nesta Rodada 1: cada pendência resolvida deve virar uma atualização pontual e documentada, sem misturar temas, preservando a rastreabilidade de quando e por que cada dado passou a ser oficial.

---

## Status

Arquivo de consolidação criado em 2026-07-04. Nenhuma pendência foi resolvida, presumida ou inventada neste documento na criação — apenas organizada para decisão futura de Renildo.

**Propagação 2 (2026-07-07)**: Renildo respondeu os Blocos 2 a 8 do `QUESTIONARIO_DECISOES_CRITICAS_RENILDO_RODADA_1_5.md`, e essas decisões foram transformadas em dado oficial nos itens 46 a 70 de `DADOS_OFICIAIS_ATENDIMENTO_VILLA_ARAGUA.md` (Propagação 1). Este arquivo foi atualizado para dar baixa nas pendências cobertas por esses itens, marcando cada uma com ✅ Resolvida, ⚠️ Parcialmente resolvida ou mantendo-a em aberto quando não coberta. Nenhuma pendência foi marcada como resolvida sem cobertura clara nos itens 46–70. As pendências resolvidas ainda precisam ser propagadas para `ROTEIRO_RECEPCIONISTA_IA.md`, `PROMPT_RECEPCIONISTA_IA_WHATSAPP.md`, `GUIA_DIGITAL_HOSPEDE_VILLA_ARAGUA.md` e, quando aplicável, `ROTEIRO_TESTE_MANUAL_RECEPCIONISTA_IA_VILLA_ARAGUA.md` — próximo passo: Propagação 3.
