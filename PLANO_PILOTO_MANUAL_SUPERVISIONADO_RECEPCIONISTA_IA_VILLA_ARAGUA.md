# PLANO DO PILOTO MANUAL SUPERVISIONADO — RECEPCIONISTA IA VILLA ARÁGUA

**Versão:** v1
**Status:** plano e instrumentos de registro — piloto ainda não iniciado
**Modo:** Rascunho Assistido — sem automação, sem agente executável, sem conexão real
**Base:** `MATRIZ_ROTEAMENTO_AGENTES_VILLA_ARAGUA.md`, `DEFINICAO_AGENTES_VILLA_ARAGUA_IA.md`, `TESTE_AGENTES_RASCUNHO_ASSISTIDO_VILLA_ARAGUA_IA.md`, `RESULTADO_TESTE_AGENTES_RASCUNHO_ASSISTIDO_VILLA_ARAGUA_IA.md`, `RODADA_CORRECAO_V1_AGENTES_VILLA_ARAGUA.md`, `MODO_RASCUNHO_ASSISTIDO_VILLA_ARAGUA.md`, `PROTOCOLO_USO_DIARIO_RASCUNHO_ASSISTIDO_VILLA_ARAGUA.md`, `BIBLIOTECA_OFICIAL_RECEPCIONISTA_IA_VILLA_ARAGUA.md`, `BIBLIOTECA_COMERCIAL_RECEPCIONISTA_IA_VILLA_ARAGUA.md`

---

## 1. Objetivo do piloto

Validar, com mensagens reais e uso manual, se a Recepcionista IA consegue:

- classificar corretamente;
- escolher o agente correto;
- consultar a fonte correta;
- gerar rascunho seguro;
- reconhecer mensagens mistas;
- escalar para Rene, Nubia ou Renildo;
- reduzir tempo de resposta;
- identificar lacunas;
- preservar o controle humano.

**Reforço explícito:**
- o humano cola a mensagem;
- a IA gera análise e rascunho;
- o humano revisa;
- o humano envia manualmente;
- nada acontece automaticamente.

---

## 2. Escopo do piloto

Piloto curto e controlado:

- **30 mensagens reais**;
- duração recomendada de **7 a 14 dias**;
- participação de Rene, Nubia e Renildo;
- mensagens comerciais e operacionais;
- inclusão de casos simples, mistos e sensíveis;
- sem dados pessoais desnecessários;
- sem automação.

**Distribuição sugerida:**

| Tipo | Quantidade |
|---|---|
| Mensagens comerciais | 10 |
| Mensagens operacionais | 10 |
| Mensagens mistas | 5 |
| Mensagens de risco | 3 |
| Mensagens de Turismo/Concierge ou lacuna | 2 |
| **Total** | **30** |

Se a distribuição real do piloto for diferente (por exemplo, mais mensagens operacionais do que comerciais numa semana específica), **registrar o que de fato ocorreu, sem forçar casos artificiais** só para bater a meta da tabela. A distribuição acima é uma referência de cobertura, não uma cota obrigatória.

---

## 3. Regras máximas do piloto

- A IA não envia mensagem.
- A IA não confirma reserva.
- A IA não confirma disponibilidade.
- A IA não define preço.
- A IA não concede desconto.
- A IA não autoriza exceção.
- A IA não decide reembolso.
- A IA não resolve conflito delicado.
- Humano sempre revisa antes de qualquer envio.
- Risco misturado com venda: o risco manda.
- Mensagem mista deve ser classificada por partes (regra incorporada em `MATRIZ_ROTEAMENTO_AGENTES_VILLA_ARAGUA.md`, seção 11).
- N4 exige urgência concreta — emoção intensa isolada não caracteriza N4 (regra incorporada em `TESTE_AGENTES_RASCUNHO_ASSISTIDO_VILLA_ARAGUA_IA.md`, Caso R-02 corrigido).
- Turismo/Concierge sem informação validada deve ser tratado como lacuna, nunca respondido com invenção.
- Nenhum aprendizado altera biblioteca, matriz ou definição de agente automaticamente durante o piloto.

---

## 4. Fluxo diário do piloto

1. Humano recebe mensagem no canal real (WhatsApp, Instagram, Booking, Airbnb ou outro).
2. Remove ou evita dados pessoais desnecessários antes de colar a mensagem.
3. Cola a mensagem na Recepcionista IA, no formato da seção 5 abaixo.
4. A IA entrega classificação, agente, fonte, risco, escalação e rascunho.
5. Humano revisa.
6. Humano classifica o rascunho como:
   - usado sem alteração;
   - usado com pequena alteração;
   - usado com alteração relevante;
   - rejeitado.
7. Humano envia manualmente pelo canal real.
8. Humano registra o caso (ficha da seção 6).
9. Lacunas identificadas seguem para o Agente de Aprendizado Manual, apenas como registro.
10. Nenhuma regra, biblioteca, matriz ou definição de agente é alterada durante o piloto sem decisão separada e explícita.

---

## 5. Formato obrigatório da saída da Recepcionista IA

```markdown
## Classificação

Trilha:
Nível:
Agente principal:
Agentes de apoio:
Risco:

## Fontes consultadas

Arquivos:
Skills:

## Pode gerar rascunho?

[Sim / Sim com ressalva / Apenas contenção / Escalar antes]

## Escalação

Responsável:
Motivo:

## Rascunho sugerido

[Texto para revisão humana]

## Observação interna

[Cuidado antes do envio]
```

---

## 6. Ficha de registro de cada mensagem

### Registro [número]

**Data e horário:**
**Pessoa que operou:** Rene / Nubia / Renildo
**Canal de origem:** WhatsApp / Instagram / Booking / Airbnb / outro
**Produto:** Pousada Arágua / Casa Arágua / não identificado
**Mensagem anonimizada:**
> [texto]

**Classificação da IA:**
**Agente principal:**
**Agentes de apoio:**
**Nível de risco:**
**Escalação indicada:**

**Resultado do rascunho:**
- [ ] usado sem alteração;
- [ ] usado com pequena alteração;
- [ ] usado com alteração relevante;
- [ ] rejeitado;
- [ ] não enviado por decisão humana.

**Alteração humana realizada:**
**Motivo da alteração:**
**Tempo estimado sem IA:**
**Tempo real usando IA:**
**Tempo estimado economizado:**
**Houve erro ou lacuna?**
**Descrição do erro ou lacuna:**
**Precisa de revisão futura?**
**Observação:**

---

## 7. Indicadores do piloto

| Indicador | Como medir | Meta inicial |
|---|---|---|
| Classificação correta | Casos corretos ÷ total | ≥ 90% |
| Rascunhos aproveitados | Sem alteração + pequena alteração | ≥ 80% |
| Escalações corretas | Escalações corretas ÷ casos sensíveis | 100% |
| Falhas críticas | Promessa indevida, desconto, preço, reembolso, exceção | 0 |
| Mensagens mistas corretas | Casos mistos corretamente separados | 100% |
| Turismo reconhecido como lacuna | Casos sem invenção | 100% |
| Tempo economizado | Soma estimada por caso | Registrar, sem meta rígida inicial |
| Intervenções de Renildo | Quantidade e motivo | Medir |
| Lacunas novas | Quantidade | Medir |
| Rascunhos rejeitados | Quantidade e motivo | ≤ 10%, salvo casos sensíveis |

---

## 8. Critérios de interrupção

O piloto deve ser interrompido para revisão se ocorrer:

- confirmação indevida de preço;
- confirmação indevida de disponibilidade;
- concessão de desconto;
- autorização de exceção;
- decisão de reembolso;
- ausência de escalação em risco;
- informação inventada;
- contradição com dados oficiais;
- uso repetido do agente errado;
- confusão recorrente entre N3 e N4;
- falha que possa prejudicar hóspede ou marca.

**Interromper não significa abandonar o projeto. Significa pausar, registrar e corrigir.**

---

## 9. Critérios de aprovação

O piloto será aprovado se:

- não houver falha crítica;
- 100% dos riscos forem escalados corretamente;
- 100% das mensagens mistas forem reconhecidas;
- 100% das lacunas de Turismo/Concierge forem tratadas sem invenção;
- pelo menos 80% dos rascunhos forem aproveitados sem alteração ou com pequena alteração;
- a equipe considerar o fluxo utilizável;
- houver evidência de economia de tempo;
- as lacunas encontradas forem registradas sem alteração automática de regras.

**Classificações finais possíveis:**

1. Aprovado para continuidade manual;
2. Aprovado com ajustes;
3. Suspenso para revisão.

---

## 10. Relatório final do piloto

Ao final do período, os registros deste plano alimentam um novo arquivo:

`RESULTADO_PILOTO_MANUAL_SUPERVISIONADO_RECEPCIONISTA_IA_VILLA_ARAGUA.md`

O relatório deverá conter:

- total de mensagens;
- distribuição por tipo;
- agentes mais acionados;
- rascunhos usados sem alteração;
- rascunhos editados;
- rascunhos rejeitados;
- escalações por pessoa;
- falhas;
- lacunas;
- tempo economizado;
- perguntas recorrentes;
- recomendações;
- decisão final.

Este arquivo ainda não existe — será criado somente após a execução real do piloto, mediante autorização.

---

## 11. Aprendizado para o futuro Agente Mentor

O piloto deve gerar evidências para um futuro Agente de Governança e Aprendizado (ainda não criado — ver `MATRIZ_ROTEAMENTO_AGENTES_VILLA_ARAGUA.md`, seção 15, lista de agentes não criados nesta fase), incluindo:

- perguntas mais frequentes;
- respostas mais editadas;
- agentes mais acionados;
- documentos mais consultados;
- lacunas recorrentes;
- regras que geraram dúvida;
- escalações evitáveis;
- oportunidades comerciais percebidas.

**O futuro Mentor apenas analisará e recomendará. Não alterará regras automaticamente.**

---

## 12. Status

Este documento é:

- plano v1;
- piloto manual;
- supervisionado;
- sem automação;
- sem conexão com canais;
- com humano no controle;
- etapa posterior à arquitetura (Matriz, Definição dos Agentes, testes e correções) e anterior a qualquer automação.
