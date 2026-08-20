# Relatório de Status — Recepcionista IA WhatsApp Villa Arágua (v1.3)

> **Nota de atualização**: este relatório foi superado por atualizações posteriores, incluindo cortesias gastronômicas, hierarquia comercial para hóspedes argentinos/hispânicos, regra de idioma português/espanhol e outras melhorias. Para refletir o estado atual real do cérebro da Villa Arágua, leia este relatório em conjunto com `AUDITORIA_GERAL_CEREBRO_VILLA_ARAGUA_V1.md`.

## 1. O que já foi criado

- Uma base de conhecimento validada (Fase 1) cobrindo distâncias, café da manhã, pet, escada/mezanino, capacidade e cozinha, com decisões oficiais registradas e aplicadas em rodadas de correção nos arquivos-fonte.
- Um painel de consolidação de dados oficiais, atualizado com duas camadas adicionais: diferenciais comerciais (piscina/área comum, área de lazer, natureza, histórico/credibilidade, localização) e estacionamento.
- Um roteiro operacional completo ("quando X → responder Y → se dúvida/risco → chamar humano") cobrindo todos os fluxos de atendimento, do primeiro contato ao pós-estadia.
- Um prompt pronto para automação de WhatsApp, em duas versões (completa e curta), já testado em múltiplas rodadas de simulação controlada.
- Três rodadas de revisão de regra aplicadas: (1) validação inicial de dados oficiais, (2) revisão da regra de pet (de "exigir consulta para grupo >3" para "questão de capacidade, não de pet"), e (3) adição da camada comercial (diferenciais + estacionamento).
- Testes controlados simulando conversas reais de WhatsApp, cobrindo pet, escadas/mezanino, diferenciais comerciais e estacionamento.

## 2. Arquivos que fazem parte da base da Recepcionista IA

| Arquivo | Papel |
|---|---|
| `CLAUDE.md` | Guia geral de comportamento para IA no projeto |
| `MAPA_GERAL_DA_VILLA.md` | Mapa executivo de navegação do negócio |
| `PLAYBOOK_ATENDIMENTO_WHATSAPP.md` | Playbook de atendimento (tom, fluxo, objeções, mensagens) |
| `CHECKLIST_ATENDIMENTO_DIARIO.md` | Checklist operacional diário |
| `DADOS_OFICIAIS_ATENDIMENTO_VILLA_ARAGUA.md` | Painel de dados oficiais validados (a fonte de verdade central) |
| `ARQUIVOS_A_CORRIGIR_DADOS_OFICIAIS.md` | Lista de correção da rodada 1 |
| `DECISOES_RENILDO_DADOS_OFICIAIS.md` | Ficha de decisões validadas por Renildo |
| `PLANO_CORRECAO_COMPLEMENTAR_DADOS_OFICIAIS.md` | Plano de correção complementar (rodada 2, incluindo Apto Soleil) |
| `RELATORIO_VALIDACAO_BASE_ATENDIMENTO_FASE_1.md` | Marco de validação da Fase 1 |
| `ROTEIRO_RECEPCIONISTA_IA.md` | Roteiro operacional de referência completo |
| `PROMPT_RECEPCIONISTA_IA_WHATSAPP.md` | Prompt pronto para copiar/colar (versão completa e curta) |
| Este arquivo (`RELATORIO_RECEPCIONISTA_IA_WHATSAPP_V1_3.md`) | Status consolidado da versão 1.3 |

## 3. Principais regras oficiais validadas

- **Distâncias**: Pousada Arágua ~130 metros da Praia de Mariscal; Casa Arágua ~250 metros.
- **Café da manhã**: incluído na Pousada Arágua (servido na suíte); não incluído por padrão na Casa Arágua (só em pacote especial ou sob consulta futura).
- **Pet** (regra revisada): pet de pequeno porte aceito em todas as acomodações da Pousada e na Casa Arágua. Suíte Wood é apenas uma boa opção quando o grupo cabe nela (até 3 pessoas) — grupo maior é resolvido por capacidade, não por restrição de pet. Não escalar por pet pequeno; escalar apenas em caso de porte grande, mais de um pet, comportamento especial, pedido de exceção ou dúvida real.
- **Escadas/mezaninos**: Suítes Metallo e Fuego — mezanino liberado apenas para hóspedes de 14 a 59 anos. Aptos Organic e Luna — indicar preferencialmente até 59 anos, evitar para idosos/mobilidade reduzida, e alertar (sem proibir) para famílias com crianças pequenas. Apto Soleil (duplex) — evitar para idosos/mobilidade reduzida/crianças pequenas, salvo confirmação explícita do hóspede, sem faixa etária rígida.
- **Estacionamento**: Pousada Arágua — 1 vaga gratuita por acomodação, dentro da pousada. Casa Arágua — estacionamento exclusivo para até 3 carros. Nunca confirmar cobertura da vaga; se vier mais carros que o permitido, verificar orientação.
- **Área comum/piscina**: a piscina é sempre área comum, nunca privativa de qualquer acomodação. Exclusivos de verdade: espelho d'água com espreguiçadeiras da Suíte Wood, e churrasqueira do Apto Soleil.
- **Diferenciais comerciais**: área comum de lazer (parquinho, redes, bancos, churrasqueira, quiosque, árvores nativas), cadeiras de praia e guarda-sol, natureza/árvores nativas — usados por gatilho de perfil (casal, família com crianças, comparação com apartamento, praticidade para praia), nunca despejados todos de uma vez.
- **Localização**: raio de ~500 metros com sorveteria, padaria, mercearia, restaurantes, pizzaria e farmácia; atendimento na areia "costuma haver" em períodos de maior movimento, nunca garantido.
- **Credibilidade/histórico**: Pousada Arágua existe desde 2007, com histórico de boas avaliações desde a época do Guia 4 Rodas — usado apenas como histórico, nunca como selo/nota/prêmio atual inventado.
- **Preço e disponibilidade**: só podem ser informados após confirmação externa real (calendário/sistema integrado ou humano) — nunca de forma especulativa.

## 4. O que a IA já pode responder com segurança

- Distância de cada produto até a praia.
- Regra de café da manhã por produto.
- Regra de pet (aceitação, quando a Wood é indicada, quando é questão de capacidade).
- Regra de idade/alerta de mezanino e escada por acomodação.
- Regra de estacionamento por produto.
- Diferenciação entre área comum e área exclusiva da piscina.
- Diferenciais comerciais por perfil de hóspede (casal, família, insegurança, comparação, praticidade).
- Histórico e credibilidade da pousada (sem inventar dados não confirmados).
- Fluxos completos de atendimento: novo lead, follow-up, pré-check-in, dúvidas na estadia, pós-estadia.

## 5. O que a IA nunca pode prometer

- Preço final ou disponibilidade sem confirmação externa real.
- Desconto ou condição especial de pagamento.
- Early check-in ou late check-out.
- Pet fora da regra (porte grande, mais de um pet, comportamento especial, exceção).
- Mais de 1 vaga de estacionamento por acomodação na Pousada, mais de 3 carros na Casa Arágua, ou que a vaga é coberta.
- Que a piscina é privativa ou exclusiva de qualquer acomodação.
- Monitoria infantil, recreação ou supervisão do parquinho.
- Nota, prêmio, selo atual, ranking ou número de avaliações não confirmados.
- Que restaurantes, farmácia, padaria, mercearia ou atendimento de praia estarão sempre abertos.
- Reembolso, cancelamento gratuito, autorização de festa/visitante, upgrade, ou qualquer exceção operacional.

## 6. Quando chamar humano

- Pedido de desconto além do padrão, cancelamento ou reembolso.
- Early check-in ou late check-out quando o hóspede insiste.
- Pet fora da regra (porte grande, mais de um pet, comportamento especial, pedido de exceção).
- Festa, evento ou visitantes fora da regra.
- Grupo maior que a capacidade máxima de qualquer acomodação (inclui conflito de vagas de estacionamento).
- Idoso/mobilidade reduzida/criança muito pequena pedindo unidade com escada/mezanino fora da regra segura.
- Mensagem de emergência real (palavra "URGENTE").
- Qualquer pergunta que exija dado não confirmado na base (preço, disponibilidade exata, cobertura de vaga, exceção operacional).

## 7. Testes realizados e status

| Teste | Foco | Resultado |
|---|---|---|
| Teste controlado 1 | 5 cenários gerais (romântico, família com crianças, pet+grupo, preço sem calendário, idoso+escada) | 1 ajuste aplicado (guarda de disponibilidade/preço); 1 lacuna identificada (Organic/Luna sem alerta de criança) |
| Teste controlado 2 | 6 cenários de pet e escada (pós-revisão da regra de pet) | Todos aprovados; 1 ambiguidade menor identificada (confirmação do hóspede em Organic/Luna vs. escalonamento) |
| Teste controlado 3 | 8 cenários de diferenciais comerciais (charme, criança pequena, piscina comum x exclusiva, golpe, comparação com apartamento, praticidade) | Todos aprovados, incluindo os 2 testes mais críticos (piscina "privativa" da Acqua e área exclusiva da Wood) |
| Teste controlado 4 | 5 cenários de estacionamento | Todos aprovados, incluindo os 2 testes críticos (vaga coberta e excesso de carros na Casa Arágua) |

**Status geral dos testes**: aprovado em todas as rodadas, com ajustes aplicados a cada rodada anterior de identificação de risco.

## 8. Pendências futuras

- Corrigir os arquivos-fonte antigos que ainda refletem a regra anterior de pet (mais restritiva), incluindo `ACOMODACOES/Quando Indicar Cada Acomodação.docx` e sua cópia duplicada, `BASE DE CONHECIMENTO/Regras da Pousada e Casa Arágua.docx`, `RECEPCIONISTA IA/PERGUNTAS FREQUENTES (FAQ).docx`, `BASE DE CONHECIMENTO/Respostas Padrão WhatsApp.docx`, `BASE DE CONHECIMENTO/Base de Conhecimento_ Perguntas Frequentes.docx` e `BASE DE CONHECIMENTO/objecoes de venda (1).docx`.
- Integrar a Recepcionista IA com um calendário/motor de reservas real, para que as respostas de disponibilidade e preço deixem de depender de handoff manual.
- Testar em ambiente controlado (grupo piloto ou simulação supervisionada) antes de colocar em operação no WhatsApp oficial da Villa Arágua.
- Criar o Guia Digital do Hóspede de forma estruturada e integrá-lo ao fluxo de pré-check-in.
- Criar o fluxo de pré-check-in/check-in autônomo de forma mais detalhada, incluindo a integração real com lock box/porteiro eletrônico.

## 9. Veredito final

**"Recepcionista IA WhatsApp v1.5 — com Concierge Local / Guia de Bombinhas."**

---

## Atualização pós-relatório — Revisão final da regra de pet

Após a publicação deste relatório, a regra de pet foi revisada e corrigida em todo o projeto, em duas rodadas complementares:

- **Rodada 1**: correção de 8 arquivos-fonte antigos que ainda refletiam a regra anterior (mais restritiva) — `RECEPCIONISTA IA/PERGUNTAS FREQUENTES (FAQ).docx`, `ACOMODACOES/Quando Indicar Cada Acomodação.docx` (e sua cópia duplicada em `BASE DE CONHECIMENTO/`), `BASE DE CONHECIMENTO/Regras da Pousada e Casa Arágua.docx`, `BASE DE CONHECIMENTO/Respostas Padrão WhatsApp.docx`, `BASE DE CONHECIMENTO/Base de Conhecimento_ Perguntas Frequentes.docx`, `BASE DE CONHECIMENTO/objecoes de venda (1).docx` e `ACOMODACOES/OBJEÇÕES DE VENDAS E QUANDO MOSTRAR CADA ACOMODAÇÃO.docx`.
- **Rodada 2**: correção de mais 2 arquivos, encontrados em uma varredura complementar na pasta `OPERACAO/` — `OPERACAO/VILLA ARAGUA 📄 REGRAS DA VILLA ARÁGUA.docx` e `OPERACAO/VILLA ARAGUA 📁 OPERAÇÃO.docx`.

**Total: 10 arquivos corrigidos em todo o projeto** (8 arquivos-fonte antigos + 2 arquivos da pasta OPERAÇÃO), todos agora refletindo a regra oficial vigente: pet de pequeno porte é aceito em todas as acomodações da Pousada Arágua e também na Casa Arágua; a Suíte Wood é uma boa opção quando o grupo cabe em até 3 pessoas (por capacidade, não por exigência de pet); grupos maiores são direcionados por capacidade/conforto; consulta humana só é necessária em casos fora do padrão (pet grande, mais de um pet, comportamento especial, pedido de exceção, dúvida real ou conflito de capacidade).

As pastas de backup (`BACKUP_ANTES_CORRECAO_DADOS_OFICIAIS/` e `BACKUP_REVISAO_PET_2026_07_02/`, incluindo a subpasta `OPERACAO_PET_FINAL/`) foram preservadas com o estado anterior de cada arquivo corrigido.

Uma varredura final em toda a pasta do projeto, ignorando as pastas de backup, **não encontrou nenhuma divergência restante** relacionada à regra de pet.

**A regra de pet pode ser considerada 100% encerrada e validada em todo o projeto.**

---

## Atualização v1.5 — Concierge Local / Guia de Bombinhas

Foi adicionada à base da Recepcionista IA uma nova camada comercial: **Concierge Local / Guia de Bombinhas**, registrada em `DADOS_OFICIAIS_ATENDIMENTO_VILLA_ARAGUA.md`, `ROTEIRO_RECEPCIONISTA_IA.md` e `PROMPT_RECEPCIONISTA_IA_WHATSAPP.md`.

Com essa camada, a IA agora sabe usar esse diferencial como argumento comercial quando o hóspede pergunta sobre praias, passeios, restaurantes, vento, clima, opções para famílias, opções para casais, ou faz comparação com Airbnb/apartamento sem atendimento.

O atendimento local deve ser sempre comunicado como disponível **durante os horários de atendimento da recepção** — nunca como um serviço 24 horas.

A IA **não pode**: prometer atendimento 24h de concierge/recepção; garantir condição de vento, mar, clima ou estacionamento; prometer reserva em restaurantes ou passeios sem confirmação; ou inventar parceria oficial com restaurantes, passeios ou serviços locais não documentada. Deve usar linguagem segura ("podemos orientar", "costuma ser melhor", "em geral", "dependendo do vento/clima", "podemos indicar opções").

**Status atualizado: "Recepcionista IA WhatsApp v1.5 — com Concierge Local / Guia de Bombinhas."**

---

## Atualização v1.6 — Objetividade e comunicação do mezanino

**Esta é uma mudança de estilo/comunicação, não de regra operacional ou comercial.** Nenhuma regra de segurança foi removida ou enfraquecida.

Renildo definiu que as respostas da Recepcionista IA no WhatsApp devem ficar mais objetivas, já que os hóspedes leem cada vez menos e têm pouco tempo — mantendo o tom acolhedor, humano, simpático, seguro e comercial sem pressão. Isso foi registrado em `ROTEIRO_RECEPCIONISTA_IA.md`, `PROMPT_RECEPCIONISTA_IA_WHATSAPP.md` e `DADOS_OFICIAIS_ATENDIMENTO_VILLA_ARAGUA.md`:

- Respostas simples devem ter, preferencialmente, 2 a 4 parágrafos curtos.
- Evitar respostas longas no primeiro contato.
- Oferecer até 2 opções por vez, salvo quando o hóspede pedir mais alternativas.
- Evitar explicar regras internas sem necessidade ou repetir detalhes técnicos.
- Fechar sempre com uma pergunta clara para avançar a conversa.

**Regra específica sobre mezanino**: a regra interna de segurança de **14 a 59 anos** (Suítes Fuego e Metallo) continua **exatamente a mesma e não foi removida**. O que mudou é apenas a forma de comunicá-la: a IA não deve mais citar a faixa etária em respostas comuns, usando em vez disso a frase natural "há escada/mezanino, então é importante todos estarem confortáveis com esse formato". A faixa etária só deve ser mencionada com mais clareza quando houver criança pequena, idoso, pessoa com mobilidade reduzida, ou um pedido específico que exija recusa ou redirecionamento para outra acomodação.

**Status atualizado: "Recepcionista IA WhatsApp v1.6 — objetividade no WhatsApp e comunicação natural da regra de mezanino."**

---

## Atualização v1.7 — Correção Fuego/Metallo: pufe para casal com filho menor

A versão v1.6 corrigiu a **forma de comunicar** a regra de mezanino, mas revelou uma interpretação excessivamente restritiva: em simulações controladas, a IA passou a tratar qualquer criança menor de 14 anos como motivo automático para **não indicar** a Suíte Fuego ou a Suíte Metallo, redirecionando sempre para a Suíte Acqua.

Renildo corrigiu essa interpretação com uma informação oficial nova: além da cama de casal e do mezanino, **Fuego e Metallo possuem um pufe que abre como colchão de solteiro confortável**, que pode ser usado por um filho menor de 14 anos (não bebê) sem envolver o mezanino. Isso foi registrado em `DADOS_OFICIAIS_ATENDIMENTO_VILLA_ARAGUA.md`, `ROTEIRO_RECEPCIONISTA_IA.md`, `PROMPT_RECEPCIONISTA_IA_WHATSAPP.md` e `MIDIAS_E_LINKS_OFICIAIS_VILLA_ARAGUA.md`, diferenciando com clareza 3 conceitos:

1. **Uso do mezanino** — liberado apenas para 14 a 59 anos (regra de segurança mantida, sem alteração).
2. **Capacidade da acomodação** — Fuego e Metallo acomodam até 3 pessoas.
3. **Uso do pufe** — alternativa de colchão de solteiro para filho menor de 14 anos, sem envolver o mezanino.

**Regra comercial corrigida**: a IA não deve mais dizer que Fuego/Metallo "não são indicadas" apenas porque a criança tem menos de 14 anos. Para o perfil casal + filho menor (não bebê), a IA deve apresentar preferencialmente 2 caminhos — Fuego/Metallo (com pufe) e Suíte Acqua (térrea, mais espaçosa) como comparação — sem transformar a Acqua na única solução. A Acqua continua sendo priorizada apenas quando houver bebê/criança muito pequena, mobilidade reduzida, idoso, ou desconforto declarado com escada/mezanino.

**Status atualizado: "Recepcionista IA WhatsApp v1.7 — correção Fuego/Metallo: pufe para casal com filho menor."**

---

## Atualização v1.8 — Bebê/criança pequena (Terra/Wood), berço portátil, Duplex Soleil até 5 pessoas e ajuste na resposta de credibilidade

O teste final de regressão da v1.7 (10 conversas) não encontrou falhas de regra, mas Renildo identificou 4 pontos de refinamento comercial e de comunicação, aplicados em `DADOS_OFICIAIS_ATENDIMENTO_VILLA_ARAGUA.md`, `ROTEIRO_RECEPCIONISTA_IA.md`, `PROMPT_RECEPCIONISTA_IA_WHATSAPP.md`, `MIDIAS_E_LINKS_OFICIAIS_VILLA_ARAGUA.md` e `GUIA_DIGITAL_HOSPEDE_VILLA_ARAGUA.md`:

1. **Bebê/criança pequena — Terra e Wood como alternativas econômicas**: a Suíte Acqua continua sendo a opção mais confortável/principal para casal com bebê ou criança pequena, mas a Suíte Terra e a Suíte Wood também podem ser ótimas alternativas mais econômicas, especialmente sem disponibilidade na Acqua ou com objeção de valor. A Acqua nunca deve ser apresentada como única solução.
2. **Berço portátil gratuito**: novo diferencial oficial — a Villa Arágua oferece berço portátil gratuito, mediante aviso com antecedência para organização. Não prometer sem antecedência nem inventar quantidade disponível.
3. **Duplex Soleil até 5 pessoas**: reforçado como alternativa dentro da pousada para grupos como 2 adultos + 3 filhos, com cozinha completa e churrasqueira própria — sempre mencionado junto com a Casa Arágua (até 6 pessoas) quando o perfil buscar mais privacidade/autonomia.
4. **Credibilidade/medo de golpe — remoção do "acima de 9"**: a resposta padrão para insegurança/medo de golpe deixou de mencionar "avaliações historicamente acima de 9", por poder soar técnico demais ou exigir comprovação imediata. A resposta agora usa apenas tradição (desde 2007, Guia 4 Rodas) e presença digital atual (redes sociais, Google, canais oficiais). O dado "acima de 9" permanece registrado apenas como observação interna em `DADOS_OFICIAIS_ATENDIMENTO_VILLA_ARAGUA.md`, não mais como frase padrão ao hóspede.

**Status atualizado: "Recepcionista IA WhatsApp v1.8 — bebê/criança pequena (Terra/Wood), berço portátil, Duplex Soleil até 5 pessoas e ajuste na resposta de credibilidade."**

---

## Validação v1.8 — Teste final de regressão

A Recepcionista IA WhatsApp v1.8 passou por um teste final de regressão com 12 conversas simuladas, cobrindo todas as correções acumuladas desde a v1.5. **Resultado: 10 dos 12 cenários passaram sem nenhuma ressalva.**

As seguintes correções recentes funcionaram de forma consistente em todos os testes:

1. Bebê/criança pequena com Acqua como opção principal + Suíte Terra/Wood como alternativas mais econômicas.
2. Berço portátil gratuito, mediante aviso com antecedência.
3. Fuego/Metallo com pufe para casal com filho menor (sem descartar automaticamente pela idade da criança).
4. Duplex Soleil acomodando até 5 pessoas.
5. Casa Arágua (até 6 pessoas) e Duplex Soleil (até 5 pessoas) apresentados corretamente juntos para famílias grandes.
6. Credibilidade sem menção a "avaliações acima de 9" na resposta padrão ao hóspede.
7. Atendimento em espanhol e português funcionando corretamente, sem portunhol.
8. Regra de pet pequeno aplicada corretamente, sem mencionar a Suíte Wood sem necessidade.
9. Objetividade nas respostas (parágrafos curtos, até 2 opções, pergunta final clara).
10. Cortesias gastronômicas (Tatuíra e Alquimista/Oliva) usadas com as ressalvas corretas, sem prometer disponibilidade.

**Dois limites remanescentes foram identificados** (não são falhas de regra, e sim limites reais de dado):

1. **Ausência de resposta absoluta para "qual acomodação é mais econômica"**: nenhum arquivo documenta valores fixos por acomodação. A orientação é tratar "mais econômica" como tendência comercial relativa (ex.: Terra/Wood tendem a ser mais econômicas que Acqua para o mesmo perfil), nunca como promessa de preço.
2. **Check-in Autônomo ainda depende de pendências críticas reais**: mapa de vagas, horário da recepção, política de envio da senha do lock box, canal oficial de emergência, e passo a passo real do porteiro eletrônico/lock box.

**Veredito**: **"Recepcionista IA WhatsApp v1.8 aprovada em nível documental para teste controlado real, desde que não responda disponibilidade, preço ou check-in autônomo completo sem dados confirmados."**

---

## Validação final v1.8 — Recepcionista IA pronta para teste controlado

A Recepcionista IA WhatsApp v1.8 passou no teste final de regressão em **10 dos 12 cenários sem ressalvas**. Os 2 pontos restantes não são falhas de regra, e sim **limites reais de dados ainda não preenchidos**:

1. A resposta absoluta sobre "qual acomodação é mais econômica" depende de tarifa real por data — nenhum arquivo documenta valores fixos por acomodação.
2. O check-in autônomo depende de pendências operacionais reais (mapa de vagas, horário da recepção, política de senha do lock box, canal oficial de emergência, passo a passo do porteiro eletrônico/lock box).

Após o teste, foi adicionada a regra de **"acomodação mais econômica"** em `DADOS_OFICIAIS_ATENDIMENTO_VILLA_ARAGUA.md`, `ROTEIRO_RECEPCIONISTA_IA.md` e `PROMPT_RECEPCIONISTA_IA_WHATSAPP.md`, com a seguinte orientação:

- Nunca afirmar "a mais barata" sem consultar tarifa real.
- Usar a Suíte Terra e a Suíte Wood como tendência relativa de custo-benefício, nunca como afirmação absoluta.
- Sempre pedir o período da viagem antes de responder sobre valor.
- Não inventar preço.
- Não prometer valor menor.

**Veredito**: **"Recepcionista IA WhatsApp v1.8 aprovada em nível documental para teste controlado real, desde que preço, disponibilidade e check-in autônomo completo dependam de dados confirmados."**
