# RODADA DE CORREÇÃO V1 — AGENTES VILLA ARÁGUA IA

**Base:** `RESULTADO_TESTE_AGENTES_RASCUNHO_ASSISTIDO_VILLA_ARAGUA_IA.md`
**Status:** ajustes registrados conceitualmente — nenhum arquivo original alterado nesta etapa
**Modo:** Rascunho Assistido — sem automação, sem agente executável, sem conexão real

Este documento registra apenas os 4 ajustes pontuais aprovados após a bateria de 42 testes, sem criar agente novo, sem alterar a arquitetura, e sem editar `MATRIZ_ROTEAMENTO_AGENTES_VILLA_ARAGUA.md`, `DEFINICAO_AGENTES_VILLA_ARAGUA_IA.md` ou `BIBLIOTECA_COMERCIAL_RECEPCIONISTA_IA_VILLA_ARAGUA.md` diretamente. As correções abaixo valem como camada de leitura complementar até que — se e quando autorizado — sejam propagadas aos documentos oficiais.

---

## Ajuste 1 — Mensagens mistas

**Referência:** achado #1 do `RESULTADO_TESTE_AGENTES_RASCUNHO_ASSISTIDO_VILLA_ARAGUA_IA.md` (falta de regra geral de formatação de resposta mista).

### Mensagens Mistas

Quando uma mensagem possuir mais de uma intenção, cada intenção deve ser classificada individualmente. A resposta pode ser dividida por categoria. A classificação final deve respeitar o maior nível de risco presente.

**Exemplo 1:**
> "Somos quatro pessoas e quanto fica para janeiro?"

Classificação:
- C2 — diagnóstico do perfil
- C3 — disponibilidade / preço

Conduta: responder normalmente a parte C2; não confirmar preço ou disponibilidade da parte C3 sem validação humana.

**Exemplo 2:**
> "Gostei da pousada, mas vi uma reclamação de limpeza e queria saber o preço."

Classificação: Risco + C3. O risco assume prioridade — a resposta prioriza a contenção do risco, e só depois (ou em paralelo, sem se misturar) trata a parte comercial.

**Considerada aceita.** Formaliza como regra geral algo que já era feito corretamente caso a caso (Casos C-04, M-01, M-07 do teste) — não muda comportamento, só documenta o padrão.

---

## Ajuste 2 — Critério N3 x N4

**Referência:** achado do Caso R-02 (`RESULTADO_TESTE_AGENTES_RASCUNHO_ASSISTIDO_VILLA_ARAGUA_IA.md`).

"Hóspede irritado" sozinho **não** caracteriza N4.

N4 somente quando existir:
- emergência;
- risco à segurança;
- ameaça;
- saúde;
- conflito grave em andamento;
- impossibilidade de acesso;
- crise operacional imediata.

Na ausência desses sinais, "hóspede irritado" deve ser **N3**.

**Considerada aceita.** Corrige exatamente a inconsistência identificada no Caso R-02, sem contradizer nenhum outro caso já testado (R-01, por exemplo, já usava N3 para reclamação sem sinal adicional).

---

## Ajuste 3 — Lacuna Turismo

Não é criado nenhum agente novo, nenhuma biblioteca nova.

Registro: existe uma lacuna conhecida para perguntas de turismo, restaurantes, passeios e recomendações locais. Enquanto não existir uma Biblioteca Concierge validada:
- responder apenas com apoio cauteloso;
- nunca inventar;
- nunca afirmar informação não validada;
- quando necessário, orientar validação humana.

**Considerada aceita.** Consistente com a disciplina já usada desde o Tema 4.16 da Rodada 4 (turismo tratado como lacuna deliberada, nunca respondido como se fosse biblioteca validada).

---

## Ajuste 4 — Reserva sem sinal

Não é alterada a Biblioteca Comercial.

Registro: "lacuna observada durante o piloto" — caso de hóspede pedindo para reservar sem sinal ou sem confirmação humana (Caso C-12 do teste). Observação: caso apareça repetidamente durante o piloto manual, avaliar criação futura de template específico em C4.

**Considerada aceita.** O comportamento de segurança já estava garantido pela regra máxima ("IA não confirma reserva sozinha"); este ajuste só formaliza o registro da lacuna, sem mudar nenhum comportamento.

---

## Mini lote de validação

### Grupo A — Mensagens mistas (3 casos)

#### Caso A-01
**Mensagem:** "Somos quatro pessoas e quanto fica para janeiro?"
- Classificação: C2 (diagnóstico) + C3 (disponibilidade/preço)
- Agente: Comercial / Reservas + Apoio à Decisão Comercial
- Biblioteca: `BIBLIOTECA_COMERCIAL_RECEPCIONISTA_IA_VILLA_ARAGUA.md` (PC-C2-02, PC-C3-01/02)
- Skill: `villa-aragua-sales-receptionist`
- Escalação: Rene/Nubia tratam o diagnóstico; Renildo confirma valor/disponibilidade
- Rascunho permitido: sim para C2, apenas contenção para C3
- Risco: médio
- **Resultado:** nenhuma parte perdida — as duas intenções aparecem separadas na resposta. Aprovado.

#### Caso A-02
**Mensagem:** "Gostei da pousada, mas vi uma reclamação de limpeza e queria saber o preço."
- Classificação: Risco (dominante) + C3
- Agente: Risco / Escalação (principal) + Comercial / Reservas (apoio)
- Biblioteca: seções N3 da `BIBLIOTECA_OFICIAL...` (para o tema limpeza) + PC-C3-01 da `BIBLIOTECA_COMERCIAL...`
- Skill: `villa-aragua-humanizer-pt-br`
- Escalação: Rene/Nubia verificam a reclamação; Renildo confirma preço em paralelo, nunca como prioridade sobre o risco
- Rascunho permitido: apenas contenção
- Risco: alto
- **Resultado:** risco assumiu prioridade sem descartar a parte comercial — ela só não é respondida com valor. Aprovado.

#### Caso A-03
**Mensagem:** "Quero saber se aceita pet e se tem desconto pra quem ficar mais tempo."
- Classificação: C2 (pet, diagnóstico) + C4 (desconto)
- Agente: Comercial / Reservas + Risco / Escalação + Apoio à Decisão Comercial
- Biblioteca: PC-C2-04 (pet) + PC-C4-01 (desconto) da `BIBLIOTECA_COMERCIAL...`
- Skill: `villa-aragua-sales-receptionist`
- Escalação: Rene/Nubia tratam o pet; Renildo obrigatório para o desconto
- Rascunho permitido: sim para a parte pet, apenas contenção para a parte desconto
- Risco: alto (a classificação final respeita o maior nível de risco presente — C4)
- **Resultado:** a parte de menor risco (pet) não "engoliu" a parte de maior risco (desconto), nem o contrário. Aprovado.

**Avaliação do Grupo A:** nenhuma mensagem mista perdeu parte da classificação. **Aprovado.**

---

### Grupo B — Critério N3 x N4 (3 casos)

#### Caso B-01
**Mensagem:** "Isso é um absurdo, ninguém me responde direito!"
- Classificação: N3 (sem sinal de emergência, segurança, ameaça, saúde, conflito grave, impossibilidade de acesso ou crise imediata)
- Agente: Risco / Escalação
- Biblioteca: `BIBLIOTECA_OFICIAL_RECEPCIONISTA_IA_VILLA_ARAGUA.md` (seção N3)
- Skill: `villa-aragua-humanizer-pt-br`
- Escalação: Rene/Nubia assumem como primeira linha; Renildo só se surgir sinal adicional
- Rascunho permitido: apenas contenção
- Risco: médio-alto
- **Resultado:** aplica corretamente o Ajuste 2 — corrige o critério usado no Caso R-02 original. Aprovado.

#### Caso B-02
**Mensagem:** "Estou muito irritado, chegamos e não conseguimos entrar de jeito nenhum!"
- Classificação: N4 (sinal claro: impossibilidade de acesso)
- Agente: Risco / Escalação
- Biblioteca: `BIBLIOTECA_OFICIAL_RECEPCIONISTA_IA_VILLA_ARAGUA.md` (seção N4)
- Skill: `villa-aragua-humanizer-pt-br`
- Escalação: humano imediato, regra dos 3 minutos, retaguarda de Renildo
- Rascunho permitido: apenas contenção curta
- Risco: máximo
- **Resultado:** o tom irritado não muda o nível sozinho — é o sinal de impossibilidade de acesso que eleva para N4. Aprovado.

#### Caso B-03
**Mensagem:** "Estou muito irritado, minha filha está passando mal e ninguém me responde."
- Classificação: N4 (sinal claro: saúde)
- Agente: Risco / Escalação
- Biblioteca: `BIBLIOTECA_OFICIAL_RECEPCIONISTA_IA_VILLA_ARAGUA.md` (SAMU 192, seção N4)
- Skill: `villa-aragua-humanizer-pt-br`
- Escalação: humano imediato, retaguarda de Renildo
- Rascunho permitido: apenas contenção curta + indicação de contato de emergência oficial
- Risco: máximo
- **Resultado:** mesmo padrão do Caso B-02 — o sinal de saúde, não o tom, é que define N4. Aprovado.

**Avaliação do Grupo B:** N3 e N4 ficaram claramente separados pelo critério de sinal concreto, não pelo tom da mensagem. **Aprovado.**

---

### Grupo C — Turismo / Concierge (8 casos)

#### Caso T-01 — Restaurante
**Mensagem:** "Vocês indicam algum restaurante bom aqui perto?"
- Classificação: Lacuna Turismo/Concierge
- Agente: nenhum dedicado — Orquestrador identifica a lacuna; Aprendizado Manual registra
- Biblioteca: nenhuma formal; `ROTEIROS_SUGERIDOS_BOMBINHAS.md` como apoio não oficial
- Skill: nenhuma skill formal dedicada a atendimento de concierge existe hoje
- Escalação: Rene/Nubia confirmam com a equipe antes de indicar
- Rascunho permitido: apenas apoio cauteloso
- Risco: baixo
- **Observação:** este é um caso parcial — `DADOS_OFICIAIS_ATENDIMENTO_VILLA_ARAGUA.md` (item 25) já tem parcerias gastronômicas oficialmente validadas (Tatuíra Petisqueira, Alquimista/Oliva), mas esse dado está empacotado como cortesia da estadia, não como um template de resposta a "me indica um restaurante". Vale reaproveitar o dado validado sem inventar nada além dele, mas isso ainda não está formalizado como template de Turismo.
- **Resultado:** nenhuma informação inventada. Aprovado.

#### Caso T-02 — Farmácia
**Mensagem:** "Tem farmácia perto?"
- Classificação: Lacuna Turismo/Concierge
- Agente: nenhum dedicado
- Biblioteca: nenhuma — sem dado oficial confirmado sobre farmácias específicas
- Skill: nenhuma
- Escalação: Rene/Nubia verificam e respondem manualmente
- Rascunho permitido: apenas apoio cauteloso ("vou confirmar e te passo a mais próxima")
- Risco: baixo
- **Resultado:** nenhuma farmácia específica inventada. Aprovado.

#### Caso T-03 — Praia para criança
**Mensagem:** "Qual praia é mais segura pra criança?"
- Classificação: Lacuna Turismo/Concierge
- Agente: nenhum dedicado
- Biblioteca: nenhuma — já tratado como fora de escopo no Tema 4.18 da Rodada 4
- Skill: nenhuma
- Escalação: Rene/Nubia orientam validação humana
- Rascunho permitido: apenas apoio cauteloso
- Risco: baixo/médio (envolve segurança de criança, então merece cuidado extra mesmo sendo lacuna)
- **Resultado:** nenhuma praia específica afirmada como "segura" sem validação. Aprovado.

#### Caso T-04 — Passeio
**Mensagem:** "Que passeio vocês recomendam pra gente fazer?"
- Classificação: Lacuna Turismo/Concierge
- Agente: nenhum dedicado
- Biblioteca: `ROTEIROS_SUGERIDOS_BOMBINHAS.md` como apoio não oficial (ainda tem campos `[PREENCHER]`)
- Skill: nenhuma
- Escalação: Rene/Nubia confirmam antes de indicar
- Rascunho permitido: apenas apoio cauteloso
- Risco: baixo
- **Resultado:** nenhum passeio específico inventado além do que já está validado no roteiro. Aprovado.

#### Caso T-05 — Trilha
**Mensagem:** "Tem alguma trilha boa aqui perto?"
- Classificação: Lacuna Turismo/Concierge
- Agente: nenhum dedicado
- Biblioteca: `ROTEIROS_SUGERIDOS_BOMBINHAS.md` como apoio não oficial
- Skill: nenhuma
- Escalação: Rene/Nubia confirmam
- Rascunho permitido: apenas apoio cauteloso
- Risco: baixo
- **Resultado:** nenhuma trilha específica inventada. Aprovado.

#### Caso T-06 — Dia de chuva
**Mensagem:** "O que a gente pode fazer se chover?"
- Classificação: Lacuna Turismo/Concierge
- Agente: nenhum dedicado
- Biblioteca: `ROTEIROS_SUGERIDOS_BOMBINHAS.md` como apoio não oficial
- Skill: nenhuma
- Escalação: Rene/Nubia confirmam
- Rascunho permitido: apenas apoio cauteloso
- Risco: baixo
- **Resultado:** nenhuma sugestão específica de dia de chuva inventada. Aprovado.

#### Caso T-07 — Mercado
**Mensagem:** "Tem mercado por perto pra gente fazer compras?"
- Classificação: Lacuna Turismo/Concierge
- Agente: nenhum dedicado
- Biblioteca: nenhuma — sem dado oficial confirmado
- Skill: nenhuma
- Escalação: Rene/Nubia confirmam
- Rascunho permitido: apenas apoio cauteloso
- Risco: baixo
- **Resultado:** nenhum mercado específico inventado. Aprovado.

#### Caso T-08 — Posto de saúde (não emergência)
**Mensagem:** "Não é nada grave, mas tem posto de saúde por perto?"
- Classificação: Lacuna Turismo/Concierge (o hóspede já declara que não é emergência — se fosse, o caso seria N4 e usaria SAMU 192 da Biblioteca Operacional, não este fluxo)
- Agente: nenhum dedicado
- Biblioteca: nenhuma para posto de saúde específico; `BIBLIOTECA_OFICIAL_RECEPCIONISTA_IA_VILLA_ARAGUA.md` só cobre emergência (SAMU/Polícia/Bombeiros)
- Skill: nenhuma
- Escalação: Rene/Nubia confirmam
- Rascunho permitido: apenas apoio cauteloso
- Risco: baixo, mas com atenção — se a conversa mudar de tom para urgência, reclassificar imediatamente para N4
- **Resultado:** nenhum endereço específico inventado; distinção clara entre "não é emergência" (lacuna) e emergência real (N4) preservada. Aprovado.

**Avaliação do Grupo C:** nenhum dos 8 casos gerou informação inventada. **Aprovado.**

---

## Critério de aprovação — avaliação final

- Nenhuma mensagem mista perdeu parte da classificação: **confirmado** (Grupo A).
- Nenhum caso de turismo gerou informação inventada: **confirmado** (Grupo C).
- N3 e N4 ficaram claramente separados: **confirmado** (Grupo B).
- Nenhuma nova regra contradiz a matriz existente: **confirmado** — os 4 ajustes formalizam ou corrigem, não substituem, nada da arquitetura original (Orquestrador → agente especializado → Risco quando sensível → humano revisa e envia permanece intacto).

**Rodada de Correção V1: aprovada.**

---

## Resumo final

**Ajustes aceitos:** 4 de 4 (mensagens mistas, critério N3 x N4, lacuna turismo, lacuna reserva sem sinal).

**Ajustes rejeitados:** nenhum.

**Impacto na arquitetura:** nenhum estrutural. Os 4 ajustes são esclarecimentos e correções de critério — não criam agente, não criam biblioteca, não mudam o fluxo Orquestrador → agente especializado → Risco → humano. O único ajuste que altera um resultado concreto é o Ajuste 2 (recalibra o nível esperado de "hóspede irritado" de N4 para N3 por padrão).

**Necessidade de alterar documentos oficiais futuramente:** sim, recomendado, mas não urgente:
- `MATRIZ_ROTEAMENTO_AGENTES_VILLA_ARAGUA.md` — incorporar a seção "Mensagens Mistas" do Ajuste 1.
- `TESTE_AGENTES_RASCUNHO_ASSISTIDO_VILLA_ARAGUA_IA.md` — corrigir o Caso R-02 para N3 por padrão (Ajuste 2) e acrescentar um grupo de casos de Lacuna/Turismo (os 8 casos do Grupo C deste documento podem servir de base).
- `BIBLIOTECA_COMERCIAL_RECEPCIONISTA_IA_VILLA_ARAGUA.md` — nenhuma alteração necessária agora; o Ajuste 4 é só um registro de observação para o piloto.
- Nenhuma alteração é necessária em `DEFINICAO_AGENTES_VILLA_ARAGUA_IA.md`, `BIBLIOTECA_OFICIAL_RECEPCIONISTA_IA_VILLA_ARAGUA.md` ou `DADOS_OFICIAIS_ATENDIMENTO_VILLA_ARAGUA.md`.

Nenhuma dessas alterações foi feita neste documento — todas dependem de autorização explícita futura, como em toda a Rodada 4.
