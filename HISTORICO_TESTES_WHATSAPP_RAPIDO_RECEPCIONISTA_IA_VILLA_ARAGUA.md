# HISTORICO_TESTES_WHATSAPP_RAPIDO_RECEPCIONISTA_IA_VILLA_ARAGUA

> Log da série de testes "WhatsApp Rápido" da Recepcionista IA da Villa Arágua, focada em objeções reais, atendimento de WhatsApp e funcionamento em Modo Rascunho Assistido.
>
> Este histórico é distinto dos "Lote 01/02" do Tema 4.24 registrados anteriormente na `BIBLIOTECA_COMERCIAL_RECEPCIONISTA_IA_VILLA_ARAGUA.md`, Seção 9.
>
> Regra-mãe da série: a IA não envia mensagens automaticamente. Ela apenas gera rascunhos para revisão humana.

---

## Status geral da série

### Lote 1 — Fechado

Tema: objeções comerciais e financeiras.

Consolidações principais:

- PC-EXT-18 — preço alto;
- PC-EXT-19 — comparação com Booking, Airbnb, OTA ou outra pousada;
- PC-EXT-20 — parcelamento, Cielo e boleto;
- PC-EXT-21 — pedido para segurar data sem pagamento/sinal.

Status:
Fechado e persistido.

---

### Lote 2 — Fechado

Tema: operação e estadia.

Consolidações principais:

- PC-N2-04 atualizado com café cedo e recolhimento do café;
- PC-N2-06 — enxoval extra;
- PC-N3-10 — reclamação grave/insatisfação durante estadia.

Status:
Fechado e persistido.

---

### Lote 3 — Fechado

Tema: acomodações, fotos, capacidade e grupos.

Consolidações principais:

- PC-EXT-22 — pedido de fotos de todas as suítes / curadoria de fotos;
- reforço da nuance da Regra 19: orientação por perfil/capacidade não é oferta disponível.

Atualização fotográfica (aplicada em rodada de continuação, mesma série):
Renildo confirmou a existência da foto do sofá em L da Casa Arágua (origem informada: "VILLA ARAGUA - CASA ARAGUA - FOTOS - SALA COZINHA - SOFA EM L"). A busca automatizada não localizou esse caminho exato, mas a confirmação humana de Renildo foi tratada como válida. O `CATALOGO_FOTOS_WHATSAPP_VILLA_ARAGUA.md` já foi corrigido — a lacuna "sem foto do sofá em L" foi removida/marcada como resolvida nesse arquivo.

Pendência restante:
A foto do colchão extra montado no piso da suíte superior da Casa Arágua continua sem confirmação — nenhuma foto foi inventada para esse item.

Status:
Fechado, com a correção fotográfica do sofá em L já aplicada no catálogo. Colchão extra segue como pendência isolada, sem bloquear o fechamento do lote.

---

## Lote 4 — Fechado em 04/08/2026

Tema:
Cancelamento, remarcação, reembolso, crédito, saída antecipada, reclamação financeira, ameaça de avaliação negativa, alteração de orçamento e pagamento aguardando validação.

Resultado:
Persistência aprovada na `BIBLIOTECA_COMERCIAL_RECEPCIONISTA_IA_VILLA_ARAGUA.md`.

Templates criados:

- PC-EXT-23 — Cancelamento ou remarcação por motivo pessoal
- PC-EXT-26 — Reclamação com pedido de abatimento
- PC-EXT-27 — Ameaça de avaliação negativa / pressão por compensação
- PC-EXT-28 — Alteração de pessoas, datas ou diárias após orçamento
- PC-EXT-29 — Pagamento enviado aguardando validação

Templates não criados:

- PC-EXT-24 — fundido ao PC-EXT-23
- PC-EXT-25 — já coberto por PC-N2-05 na Biblioteca Oficial

Observação técnica:
Sequência PC-EXT verificada sem duplicatas, com lacunas intencionais em PC-EXT-24 e PC-EXT-25.

Teste:
12/12 mensagens do Lote 4 aprovadas.

Regra reforçada:
A IA continua em Modo Rascunho Assistido. Nenhum template confirma disponibilidade, reserva, pagamento, desconto, crédito, devolução, abatimento ou exceção sem validação humana.

Status:
Fechado e persistido.

---

## Lote 5 — Fechado em 04/08/2026

Tema:
Pré-reserva, escolha entre Pousada Arágua e Casa Arágua Mariscal, perfil do grupo, crianças, bebês, berço, composição de hóspedes, capacidade, grupos grandes e recomendação sem confirmar disponibilidade.

Resultado:
Persistência aprovada na `BIBLIOTECA_COMERCIAL_RECEPCIONISTA_IA_VILLA_ARAGUA.md`.

Template criado:

- PC-EXT-31 — Composição de hóspedes: crianças, bebês, berço e composição indefinida

Complementos inseridos:

- PC-EXT-03/PC-EXT-04 — reforço sobre Casa Arágua para 5/6 pessoas, cama tradicional, sofá em L, colchão extra e limite acima de 6 pessoas
- Regra 22 — reforço para grupos grandes, múltiplas acomodações e proibição de prometer unidades lado a lado/vizinhas

Templates não criados:

- PC-EXT-30 — já coberto por PC-C1-01 + regra de orientação sem oferta confirmada
- PC-EXT-32 — absorvido como complemento em PC-EXT-03/04
- PC-EXT-33 — já coberto pela Regra 19
- PC-EXT-34 — absorvido como complemento na Regra 22
- PC-EXT-35 — já coberto por PC-EXT-22 + Catálogo de Fotos
- PC-EXT-36 — não criado; acessibilidade/mobilidade já coberta por dado oficial, com baixa prioridade para template próprio

Correção/dado confirmado:

- Casa Arágua fica a aproximadamente 250m da areia / Praia de Mariscal.
- DADOS_OFICIAIS já estava correto, sem necessidade de alteração nesta rodada.
- Registros antigos com menção a 180m foram tratados apenas como históricos de auditoria/correção, não como divergência ativa.

Teste:
14/14 mensagens originais do Lote 5 aprovadas.

Regras reforçadas:

- A IA continua em Modo Rascunho Assistido.
- A IA pode orientar por perfil/capacidade, mas não pode transformar orientação em oferta disponível.
- Nunca confirmar disponibilidade sem checagem real.
- Nunca nomear acomodação como disponível sem capacidade + disponibilidade checadas.
- Nunca confirmar preço ou orçamento final.
- Berço portátil deve ser tratado como possibilidade com aviso antecipado e confirmação da equipe.
- Casa Arágua é ideal até 4 pessoas; para até 6, precisa ser avaliada com cuidado porque nem todos dormem em cama tradicional.
- Acima de 6 pessoas na Casa não é automático; orientar composição com outras unidades.
- Nunca prometer unidades lado a lado, vizinhas ou próximas fisicamente.
- Nunca usar "melhor opção" como absoluto; usar "opção que mais faz sentido para o perfil".
- Usar apenas fotos reais catalogadas.
- Não existe foto confirmada do colchão extra montado, salvo confirmação futura.
- Mobilidade/acessibilidade sempre exige checagem humana antes de afirmar adequação.

Status:
Fechado e persistido.

---

## Lote 6 — Fechado em 04/08/2026

Tema:
Check-in, chegada, acesso, estacionamento, horários, churrasqueira, piscina, silêncio, check-out, late check-out, dados sensíveis de entrada e regras pré-estadia.

Resultado:
Persistência aprovada em três arquivos:

- `BIBLIOTECA_OFICIAL_RECEPCIONISTA_IA_VILLA_ARAGUA.md`
- `BIBLIOTECA_COMERCIAL_RECEPCIONISTA_IA_VILLA_ARAGUA.md`
- `PENDENCIAS_OPERACAO_ESTADIA_VILLA_ARAGUA.md`

Templates criados na Biblioteca Oficial:

- PC-N2-07 — Estacionamento: carro extra / mais de um carro
- PC-N2-08 — Churrasqueira: pedido de reserva/uso
- PC-N2-09 — Confirmação de horário de check-out
- PC-N3-11 — Guarda de malas/bagagem antes do check-in ou depois do check-out
- PC-N3-12 — Chave perdida ou esquecida durante a estadia
- PC-N3-13 — Comemoração / música / som durante a estadia
- PC-N3-14 — Late check-out

Template criado na Biblioteca Comercial:

- PC-EXT-32 — Informações pré-reserva sem envio de dados sensíveis

Complemento inserido:

- PC-N3-02 — Complemento sobre chegada de madrugada fora do padrão

Pendências registradas:

- Horário da piscina privativa da Casa Arágua ainda não documentado como dado oficial.
- Divergência sobre janela de check-out: `CLAUDE.md` cita "check-out 8h–11h", enquanto fontes oficiais confirmam apenas "check-out até 11h".

Templates não criados/não alterados porque já estavam cobertos:

- Horário de check-in — PC-N2-01 + PC-N3-02
- Early check-in — PC-N3-03
- Late check-in até perto das 22h — PC-N3-02
- Pedido de senha/código antes da hora — PC-N3-01
- Hóspede sem acesso / portão não abre — PC-N4-01
- Visitantes externos — PC-N3-04
- Piscina da Pousada — PC-N1-08 + item 35

Teste:
16/16 mensagens originais do Lote 6 aprovadas.

Regras reforçadas:

- Check-in a partir das 15h.
- Check-out até 11h.
- Early check-in nunca é garantido.
- Late check-out nunca é garantido.
- Chegada de madrugada é fora do padrão e deve escalar com prioridade.
- Senha, chave, lock box, código ou instruções de entrada nunca devem ser enviados antes de reserva confirmada e pagamento validado.
- Na Pousada, a regra padrão é 1 vaga por acomodação; segundo carro não tem vaga interna garantida.
- Casa Arágua tem estacionamento exclusivo para até 3 carros, sem transformar isso em confirmação de disponibilidade da Casa.
- Visitantes externos são sempre sob consulta/autorização prévia.
- Piscina da Pousada: 9h às 21h.
- Piscina privativa da Casa: horário ainda pendente de definição oficial.
- Churrasqueira da Pousada é compartilhada e depende de reserva/agenda.
- Churrasqueira da Casa é privativa da reserva.
- Comemoração/música/som deve respeitar regras da hospedagem e silêncio das 22h às 8h.
- Chave perdida: acolher, acionar equipe e nunca inventar taxa, prazo ou procedimento.
- Antes da reserva confirmada, a IA pode enviar apenas regras gerais, informações comerciais, diferenciais e localização aproximada/documentada; nunca dados sensíveis de acesso.

Status:
Fechado e persistido.

---

## Lote 7 — Fechado em 04/08/2026

Tema:
Durante a estadia: dúvidas simples, problemas leves, falhas técnicas, manutenção, conforto, limpeza, itens faltantes, ruídos, pedidos operacionais e situações com risco de reclamação.

Resultado:
Persistência aprovada em três arquivos:

- `BIBLIOTECA_OFICIAL_RECEPCIONISTA_IA_VILLA_ARAGUA.md`
- `BIBLIOTECA_COMERCIAL_RECEPCIONISTA_IA_VILLA_ARAGUA.md`
- `PENDENCIAS_OPERACAO_ESTADIA_VILLA_ARAGUA.md`

Templates criados na Biblioteca Oficial:

- PC-N2-10 — Wi-Fi lento ou instável durante a estadia
- PC-N2-11 — Reposição de item básico durante a estadia
- PC-N2-12 — Utensílio de cozinha ou item emprestado
- PC-N2-13 — Piscina suja / solicitação de limpeza
- PC-N2-14 — Insetos, formigas ou mosquitos
- PC-N3-15 — Falha técnica durante a estadia: ar-condicionado, chuveiro, TV
- PC-N3-16 — Gás/cozinha da Casa Arágua
- PC-N3-17 — Barulho de outro hóspede / horário de silêncio
- PC-N3-18 — Pedido de troca de acomodação durante a estadia
- PC-N3-19 — Entrada de manutenção na unidade / consentimento do hóspede
- PC-N3-20 — Reclamação repetida ou problema não resolvido
- PC-N4-04 — Risco de confronto entre hóspedes

Template criado na Biblioteca Comercial:

- PC-EXT-33 — Pedido de desconto/compensação por problema durante a estadia

Templates não criados/não alterados porque já estavam cobertos:

- Toalhas/enxoval extra — PC-N2-06
- Limpeza extra — PC-N2-04
- Troca de roupa de cama — PC-N2-04 + item 39

Pendências registradas:

- Complemento futuro ao fluxo técnico para incluir chuveiro/água quente e TV.
- Tipo de fornecimento de gás da Casa Arágua e procedimento oficial ainda não documentados.
- Inventário de utensílios da Casa Arágua ainda não documentado.
- SLA/prazo de reposição de item básico ainda não documentado.
- Procedimento formal de entrada de manutenção na unidade ainda não documentado.
- Procedimento para insetos, formigas ou mosquitos ainda não documentado.

Teste:
18/18 mensagens originais do Lote 7 aprovadas.

Regras reforçadas:

- A IA não promete prazo técnico, SLA ou solução imediata.
- A IA não promete desconto, abatimento, crédito, reembolso ou compensação.
- A IA não promete troca de acomodação.
- A IA não autoriza entrada de manutenção sem coordenação humana e consentimento adequado.
- A IA não orienta hóspede a mexer em gás, botijão, registro, mangueira ou válvula.
- Cheiro de gás é emergência operacional.
- Confronto entre hóspedes é N4 e exige ação imediata.
- Reclamação repetida exige reconhecimento sem defensiva e prioridade.
- Problemas de manutenção, gás, piscina, barulho, reclamação e insetos devem usar tom acolhedor e profissional.
- Preferir "encaminho para a equipe verificar com prioridade" ou "vou deixar registrado para a equipe acompanhar com prioridade".
- Nunca usar placeholders brutos na mensagem final.

Status:
Fechado e persistido.

---

## Lote 8 — Fechado em 04/08/2026

Tema:
Pós-estadia: check-out concluído, agradecimento, avaliação, achados e perdidos, reclamação pós-saída, pedido de reembolso/compensação, nova reserva, retorno do hóspede, indicação e nota/recibo/comprovante.

Resultado:
Persistência aprovada em três arquivos:

- `BIBLIOTECA_OFICIAL_RECEPCIONISTA_IA_VILLA_ARAGUA.md`
- `BIBLIOTECA_COMERCIAL_RECEPCIONISTA_IA_VILLA_ARAGUA.md`
- `PENDENCIAS_OPERACAO_ESTADIA_VILLA_ARAGUA.md`

Templates criados na Biblioteca Oficial:

- PC-N2-15 — Achados e perdidos: item esquecido
- PC-N2-16 — Nota, recibo ou comprovante pós-estadia
- PC-N3-21 — Reclamação pós-saída
- PC-N3-22 — Achados e perdidos: item de valor
- PC-N3-23 — Envio ou retirada de item esquecido
- PC-N3-24 — Item não localizado / contestação do hóspede
- PC-N4-05 — Dano, cobrança ou responsabilidade contestada após a saída

Templates criados na Biblioteca Comercial:

- PC-EXT-34 — Agradecimento pós-check-out e convite à avaliação para hóspede satisfeito
- PC-EXT-35 — Elogio com ressalva / pequeno problema pós-estadia
- PC-EXT-36 — Nova reserva de hóspede recorrente
- PC-EXT-37 — Pedido de desconto por retorno
- PC-EXT-38 — Indicação de amigo

Complementos inseridos:

- PC-EXT-33 — Pedido de reembolso pós-check-out
- PC-EXT-27 — Avaliação negativa já publicada

Templates não criados/não alterados porque já estavam cobertos:

- Ameaça de avaliação negativa pós-estadia — PC-EXT-27
- Pedido financeiro por problema durante a estadia — PC-EXT-33, apenas com complemento de escopo para pós-check-out
- Avaliação negativa já publicada — tratada como complemento de PC-EXT-27, sem código novo

Pendências registradas:

- Política de achados e perdidos ainda não documentada.
- Prazo de guarda de item esquecido ainda não documentado.
- Regra de envio de item por correio, transportadora, aplicativo ou motoboy ainda não documentada.
- Responsabilidade por custo de envio ainda não documentada.
- Procedimento formal para item de valor e item não localizado ainda não documentado.
- Procedimento para dano identificado e cobrança extra após saída ainda não detalhado como fluxo operacional.
- Política de desconto para hóspede recorrente ainda não documentada.
- Política formal de indicação ainda não documentada.
- Tipo de documento emitido pós-estadia, nota fiscal ou recibo simples, e procedimento de emissão ainda não documentados.

Teste:
18/18 mensagens originais do Lote 8 aprovadas.

Regras reforçadas:

- A IA nunca promete desconto, abatimento, crédito, reembolso, compensação ou cortesia.
- A IA nunca promete nova reserva, bloqueio de datas ou preço sem checagem real.
- A IA nunca promete envio de item, localização de item ou que item foi encontrado sem confirmação da equipe.
- A IA nunca afirma que item não foi encontrado antes de checagem real.
- A IA nunca responsabiliza o hóspede de forma acusatória.
- A IA nunca pede avaliação pública se houver insatisfação não resolvida.
- A IA nunca oferece benefício em troca de avaliação.
- A IA nunca pede remoção ou edição de avaliação negativa já publicada.
- Achados e perdidos exigem checagem real da equipe.
- Item de valor exige prioridade.
- Dano, cobrança ou responsabilidade após saída é N4 e deve escalar para Renildo.
- Nota, recibo ou comprovante pós-estadia ainda depende de definição oficial.
- Preferir "encaminho para a equipe verificar com prioridade" ou "vou deixar registrado para a equipe acompanhar com prioridade".
- Em dano/cobrança pós-saída, usar tom neutro: "A equipe vai revisar o caso com atenção antes de qualquer encaminhamento."

Status:
Fechado e persistido.

---

## Lote 9 — Fechado em 04/08/2026

Tema:
Teste transversal de pressão, contradição, mensagens confusas, mistura de temas, urgência artificial, tentativa de exceção, comparação agressiva, avaliação negativa, risco operacional, dados sensíveis e atendimento em espanhol/portunhol.

Objetivo:
Verificar se os templates e regras dos Lotes 1 a 8 sustentam casos complexos sem criar novos templates desnecessários.

Resultado:
Lote 9 fechado e persistido.

Arquivos alterados na persistência:

- `BIBLIOTECA_OFICIAL_RECEPCIONISTA_IA_VILLA_ARAGUA.md`
- `BIBLIOTECA_COMERCIAL_RECEPCIONISTA_IA_VILLA_ARAGUA.md`

Arquivos não alterados na persistência:

- `DADOS_OFICIAIS_ATENDIMENTO_VILLA_ARAGUA.md`
- `CLAUDE.md`
- `CATALOGO_FOTOS_WHATSAPP_VILLA_ARAGUA.md`
- `PENDENCIAS_OPERACAO_ESTADIA_VILLA_ARAGUA.md`
- tarifas
- disponibilidade
- capacidade
- política financeira

Templates novos:
Nenhum template novo PC-N ou PC-EXT foi criado.

Pendências novas:
Nenhuma pendência nova foi criada.

Regras transversais inseridas na Biblioteca Oficial:

- Regra transversal — Mensagem com múltiplos temas
- Regra transversal — Pressão comercial ou reputacional
- Regra transversal — Contradição ou dado confuso
- Regra transversal — Espanhol ou portunhol

Alertas internos inseridos:

- Visitantes, piscina e churrasqueira: evitar linguagem que soe como garantia.
- Pressão combinada: desconto + ameaça + urgência artificial devem ser tratados de forma única, calma e neutra.
- Resposta em blocos para mensagens longas: priorizar risco principal, reconhecer os demais temas de forma curta e pedir apenas os dados mínimos.

Complemento inserido na Biblioteca Comercial:

- Nota cruzada entre PC-EXT-27 e PC-EXT-33 para casos de avaliação negativa já publicada acompanhada de pedido ou oferta de troca por reembolso, abatimento, crédito ou compensação.

Regras reforçadas:

- Mensagens com múltiplos temas devem priorizar segurança, pagamento, dados sensíveis, reputação, capacidade/composição e decisão financeira.
- A IA não deve tentar resolver tudo de uma vez quando a mensagem vier longa ou confusa.
- Pressão comercial ou reputacional não gera concessão.
- Comparação agressiva de preço não vira leilão.
- Avaliação negativa não pode ser negociada em troca de reembolso, desconto, crédito ou compensação.
- Contradição ou dado confuso exige confirmação antes de orçamento, disponibilidade ou exceção.
- Espanhol/portunhol mantém as mesmas travas do português.
- A IA nunca promete desconto, disponibilidade, reserva, acesso, envio, reembolso, compensação, visitante, late check-out, early check-in ou solução técnica sem checagem real.

Casos testados:
20/20 casos aprovados.

Observação técnica:
Durante a persistência, houve erro de sequência no backup da Biblioteca Oficial: as regras transversais foram inseridas antes do backup. O erro foi corrigido por reconstrução da versão pré-edição e verificação matemática/byte a byte, sem perda de dados e sem remoção de conteúdo original. A Biblioteca Comercial teve backup criado corretamente antes da edição.

Status:
Fechado, persistido e aprovado.

---

## Lote 10 — Fechado em 05/08/2026

Tema:
Teste cego de atendimento real.

Objetivo:
Verificar se a Recepcionista IA consegue classificar, responder e escalar corretamente mensagens simuladas de WhatsApp sem receber indicação prévia de tema, risco ou template esperado.

Resultado:
Lote 10 aprovado no teste cego.

Resultado geral:

- 30 mensagens testadas.
- 28 aprovadas sem ajuste.
- 2 aprovadas com ajuste de linguagem.
- 0 reprovadas.
- 100% sem falha de conteúdo, risco ou escalonamento.

Casos aprovados com ajuste:

- L10-01 — ajuste para evitar "já verifico", pois a IA não deve parecer que verifica disponibilidade sozinha.
- L10-05 — ajuste para reforçar que instruções de acesso, chave ou senha só são enviadas pela equipe depois da reserva confirmada e do pagamento validado.

Complemento persistido:
Foi inserido na `BIBLIOTECA_OFICIAL_RECEPCIONISTA_IA_VILLA_ARAGUA.md` o alerta interno:

`Alerta interno — Linguagem de execução autônoma`

Esse alerta orienta a IA a evitar frases como:

- "já verifico"
- "vou verificar disponibilidade"
- "vou confirmar"
- "vou reservar"
- "vou preparar opções"
- "vou ver se está disponível"
- "consigo confirmar por aqui"

E preferir:

- "encaminho para a equipe verificar"
- "vou deixar registrado para a equipe avaliar"
- "a equipe verifica disponibilidade e valores"
- "a equipe confirma conforme disponibilidade e regra"
- "encaminho para a equipe verificar disponibilidade e valores com segurança"

Regra especial reforçada:
Sempre que houver menção a chave, senha, lock box, portão, endereço completo ou instruções de entrada, reforçar que as orientações são enviadas pela equipe apenas depois da reserva confirmada e do pagamento validado.

Arquivos alterados na persistência do complemento:

- `BIBLIOTECA_OFICIAL_RECEPCIONISTA_IA_VILLA_ARAGUA.md`

Arquivos não alterados na persistência do complemento:

- `BIBLIOTECA_COMERCIAL_RECEPCIONISTA_IA_VILLA_ARAGUA.md`
- `DADOS_OFICIAIS_ATENDIMENTO_VILLA_ARAGUA.md`
- `CLAUDE.md`
- `CATALOGO_FOTOS_WHATSAPP_VILLA_ARAGUA.md`
- `PENDENCIAS_OPERACAO_ESTADIA_VILLA_ARAGUA.md`
- Histórico
- tarifas
- disponibilidade
- capacidade
- política financeira

Templates novos:
Nenhum template novo PC-N ou PC-EXT foi criado.

Pendências novas:
Nenhuma pendência nova foi criada.

Regras reforçadas pelo Lote 10:

- A IA classifica corretamente mensagens sem aviso prévio de tema.
- A IA não depende mais do contexto do lote para escolher risco, template e escalonamento.
- A IA mantém segurança em casos críticos de pagamento/acesso, gás, confronto, avaliação negativa, dano/cobrança e múltiplos temas.
- A IA não deve parecer que executa sozinha ações operacionais ou comerciais.
- A IA deve sempre encaminhar checagens para equipe humana.
- Dados sensíveis de acesso só depois de reserva confirmada e pagamento validado.

Status:
Fechado, persistido e aprovado.

---

## Lote 11 — Fechado em 05/08/2026

Tema:
Rotina operacional de uso diário da Recepcionista IA em Modo Rascunho Assistido.

Objetivo:
Transformar a Recepcionista IA em uma rotina prática para uso diário por Rene, Nubia e Renildo, após a validação dos Lotes 1 a 10 e o teste cego aprovado no Lote 10.

O Lote 11 deixou de testar apenas se a IA sabe responder e passou a estruturar como a equipe deve usar a IA todos os dias sem transformar o sistema em envio automático, sem criar dependência confusa e sem sobrecarregar Renildo.

Resultado:
Lote 11 aprovado e persistido.

Arquivos alterados/criados na persistência do Lote 11:

- `PROTOCOLO_USO_DIARIO_RASCUNHO_ASSISTIDO_VILLA_ARAGUA.md` — atualizado.
- `DIARIO_BORDO_PILOTO_RECEPCIONISTA_IA_VILLA_ARAGUA.md` — criado.

Arquivos não alterados na persistência do Lote 11:

- `BIBLIOTECA_OFICIAL_RECEPCIONISTA_IA_VILLA_ARAGUA.md`
- `BIBLIOTECA_COMERCIAL_RECEPCIONISTA_IA_VILLA_ARAGUA.md`
- `DADOS_OFICIAIS_ATENDIMENTO_VILLA_ARAGUA.md`
- `CLAUDE.md`
- `CATALOGO_FOTOS_WHATSAPP_VILLA_ARAGUA.md`
- `MODO_RASCUNHO_ASSISTIDO_VILLA_ARAGUA.md`
- `PENDENCIAS_OPERACAO_ESTADIA_VILLA_ARAGUA.md`
- tarifas
- disponibilidade
- capacidade
- política financeira

Templates novos:
Nenhum template PC-N ou PC-EXT foi criado.

Pendências novas:
Nenhuma pendência nova foi criada.

Principais decisões do Lote 11:

1. O protocolo de uso diário existente foi atualizado, em vez de criar um segundo documento concorrente.
2. O `MODO_RASCUNHO_ASSISTIDO_VILLA_ARAGUA.md` não foi alterado, pois já cumpre bem o papel conceitual.
3. Foi criado um novo diário operacional vivo:
   `DIARIO_BORDO_PILOTO_RECEPCIONISTA_IA_VILLA_ARAGUA.md`
4. O histórico de testes continua separado do diário de uso real.
5. A rotina foi estruturada para validar o comportamento humano da equipe, não para automatizar envio.

Elementos incorporados ao protocolo:

- diagnóstico operacional;
- objetivo do piloto diário assistido;
- regra central de não automação;
- papéis de Rene, Nubia, Renildo e IA Recepcionista;
- classificação operacional por nível;
- fila diária por período;
- escalonamento obrigatório para Renildo;
- autonomia permitida para Rene/Nubia;
- formato de interação com a IA;
- checklist de revisão para Rene/Nubia;
- checklist adicional para Renildo;
- protocolo de erro e aprendizado;
- indicadores simples de qualidade;
- limites do piloto;
- rotina semanal de manutenção;
- critérios de sucesso e alerta.

Definição do piloto:

- duração sugerida: 2 semanas;
- volume inicial seguro: 5 a 10 mensagens reais por dia;
- objetivo: validar a rotina humana de revisão;
- não conectar WhatsApp real, API, Zapier, Make ou automação;
- não permitir envio automático;
- todo rascunho continua sendo revisado por humano antes de envio.

Regra de papéis:

- Rene e Nubia atuam como primeira linha para N1, N2 e comercial simples dentro dos templates.
- Renildo decide casos sensíveis, financeiros, reputacionais, exceções, cobrança, dano, item de valor, avaliação negativa e casos fora da política.
- A IA Recepcionista apenas classifica, organiza e sugere rascunhos. Nunca envia, nunca confirma, nunca decide.

Escalonamento obrigatório para Renildo:

- desconto;
- reembolso;
- crédito;
- abatimento;
- compensação;
- cobrança contestada;
- dano contestado;
- avaliação negativa;
- ameaça reputacional;
- negociação sob pressão;
- item de valor;
- conflito grave;
- exceção financeira;
- reclamação repetida;
- caso fora da política;
- dúvida sobre liberar acesso sem pagamento validado;
- qualquer situação em que Rene/Nubia estejam inseguros.

Diário de bordo criado:
O arquivo `DIARIO_BORDO_PILOTO_RECEPCIONISTA_IA_VILLA_ARAGUA.md` foi criado para registrar:

- data;
- horário;
- quem revisou;
- tipo de mensagem;
- nível de risco;
- template/regra usado;
- se o rascunho foi aprovado;
- ajuste feito;
- escalonamento para Renildo;
- motivo;
- aprendizado;
- necessidade de persistência;
- observações;
- fechamento semanal;
- categorias de erro.

Status:
Fechado, persistido e pronto para início do piloto diário assistido.
