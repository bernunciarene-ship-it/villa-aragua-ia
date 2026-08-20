# ARQUITETURA DO SISTEMA COMERCIAL VILLA ARÁGUA

## Constituição do Sistema Comercial

> Toda definição conceitual do Sistema Comercial Villa Arágua nasce neste documento.
>
> Nenhum documento operacional poderá redefinir conceitos estabelecidos aqui.
>
> Bibliotecas, Jornadas, Templates, CRM, Playbook, Agentes, Skills e Integrações apenas consomem essas definições.
>
> Toda mudança conceitual exige:
> - mapa de impacto;
> - aprovação explícita de Renildo;
> - atualização do changelog.
>
> Esta Arquitetura constitui a Fonte Única da Verdade para todos os conceitos comerciais.

---

**Natureza:** documento conceitual, estrutural e durável — anterior a agentes, skills, templates, CRM ou qualquer tecnologia.

> A referência cultural e de princípios deste sistema está em `MANIFESTO_DA_OPERACAO_COMERCIAL_VILLA_ARAGUA.md`. Esta Arquitetura não repete a filosofia do Manifesto — define como o sistema comercial funciona conceitualmente, à luz dela.

**Regra de precedência:** em caso de conflito entre este documento e o futuro `MAPA_DO_CEREBRO_COMERCIAL_VILLA_ARAGUA.md`, esta Arquitetura prevalece — o Mapa Comercial é implementação documental dos conceitos aqui definidos, não o contrário. Arquitetura e Mapa Comercial têm changelogs separados (seção 22).

---

## 0. Perguntas que este documento responde

1. Como funciona o Sistema Comercial da Villa Arágua, de forma independente de tecnologia?
2. O que a Villa Arágua deve fazer comercialmente agora, diante de cada lead, conversa, risco, estágio e resultado?

---

## 1. Identidade do Sistema

**Nome conceitual:** Sistema Comercial da Villa Arágua.

- **Propósito:** organizar como a Villa Arágua pensa e age comercialmente diante de qualquer lead, conversa ou situação — do primeiro contato ao relacionamento pós-estadia.
- **Fronteiras:** cobre da entrada do lead até o resultado (reserva, perda ou nutrição) e o relacionamento pós-venda. Não cobre a operação da estadia em si, nem a execução técnica de campanhas.
- **O que pertence ao sistema:** leads, conversas, qualificação, risco comercial, decisão comercial, follow-up, registro comercial, resultado, relacionamento.
- **O que não pertence ao sistema:** execução operacional da estadia, execução técnica de anúncios, ferramenta de armazenamento (planilha, CRM, banco de dados).

---

## 2. Relação entre Cérebro IA e Sistema Comercial

- O **Cérebro IA** responde **"como responder"** — é a camada de resposta e tom.
- O **Sistema Comercial** responde **"o que fazer comercialmente agora"** — é a camada de decisão.
- Os dois se conectam (a decisão comercial informa qual resposta é apropriada), mas não se substituem.
- Relação com o atendimento: o atendimento executa a conversa; este sistema decide o que fazer com o resultado dela.
- Relação com a operação: a operação começa quando este sistema produz um resultado "reservado".
- Relação com o marketing: marketing gera a origem; este sistema começa a atuar quando existe um lead.
- Relação com o Revenue Management: informa preço e cenário; não decide.
- Relação com humanos: opera sob revisão e confirmação humana — Rene, Nubia e Renildo, conforme sensibilidade (seção 14).

---

## 3. Modelo Mental do Sistema

```text
Quem chega assume o papel de Lead sobre um Contato.
Quando conversa, gera uma Conversa.
Quando demonstra intenção, recebe uma classificação QL.
Quando envia uma mensagem, essa mensagem recebe uma classificação C.
Quando existe uma situação operacional, ela recebe uma classificação N.
Quando avança ou recua no processo, muda de estágio comercial.
Quando a equipe age, registra uma ação.
Quando o ciclo termina, existe um resultado.
Quando já se hospedou, passa a existir relacionamento — e o Contato permanece.
```

**Protagonismo (ordem conceitual):**

```text
Hóspede/lead
↓
Equipe
↓
IA
↓
Tecnologia
```

O hóspede/lead é o protagonista. A equipe conduz. A IA apoia. A tecnologia é a última camada — nunca substitui as anteriores.

**Velocidade de mudança de cada elemento:**

| Elemento | Velocidade | Observação |
|---|---|---|
| QL | Lenta | característica de fundo do lead; muda com maturação real da intenção |
| C | Rápida | pode mudar a cada mensagem |
| N | Conforme a situação | surge apenas quando há componente operacional |
| Estágio | Conforme o processo | avança/recua conforme o lead avança/recua na jornada |
| Resultado | Fecha o ciclo | não retrocede — abre um novo ciclo (nutrição/reativação) em vez de reabrir o antigo |
| Relacionamento | Contínuo | continua existindo depois que o ciclo comercial termina |

---

## 4. Entidades Comerciais

*(Entidade = "coisa" que existe no sistema, independente de estado. Não vinculada a nenhum software.)*

1. **Contato** — entidade **permanente**: a pessoa real, identificada por nome/telefone/canal. Nasce no primeiro registro; nunca "termina" enquanto a Villa mantiver relação com ela; pode acumular vários ciclos comerciais ao longo do tempo.
2. **Lead** — **papel temporário** que um Contato assume quando há uma oportunidade comercial em aberto. Nasce quando o Contato demonstra interesse; termina quando o ciclo se resolve (converte, perde ou entra em nutrição) — o Contato permanece, o papel de Lead se encerra até uma nova oportunidade surgir.
3. **Conversa** — sequência de mensagens trocadas com um Contato. Nasce na primeira mensagem; muda a cada nova troca; pode reabrir mesmo após período de silêncio.
4. **Produto** — Pousada Arágua ou Casa Arágua Mariscal (nunca tratados como o mesmo produto). Nasce quando identificado na conversa; pode mudar se o Contato troca de interesse.
5. **Oportunidade** — representa **um ciclo comercial** de um Contato: nasce quando o Contato (no papel de Lead) demonstra interesse em um Produto; muda conforme avança de estágio; termina em Resultado. **Um mesmo Contato pode ter várias Oportunidades ao longo do tempo** (ciclos diferentes, em datas diferentes). No piloto manual, existe no máximo **uma Oportunidade ativa principal por vez** por Contato — evita conduzir dois ciclos simultâneos e confundir prioridade. Quando o ciclo de uma Oportunidade termina, o **relacionamento com o Contato continua** independentemente do resultado.
6. **Orçamento** — valores estruturados para uma Oportunidade. Nasce quando preparado; muda se revisado; termina quando aceito, recusado ou expira. **A IA não prepara valor sozinha** — o orçamento é estruturado pela equipe com apoio da IA, e o valor final é sempre validado por humano (princípio já estabelecido no Manifesto: "Reserva, pagamento, preço, desconto e exceção são humanos").
7. **Reserva** — compromisso formalizado de estadia, ligado a uma Oportunidade. **Só existe após confirmação humana** — a IA nunca declara uma reserva existente.
8. **Hóspede** — o Contato, no momento em que sua Oportunidade resulta em Reserva confirmada e passa a ocupar (ou vai ocupar) a acomodação.
9. **Estadia** — período efetivo de ocupação. Pertence ao domínio operacional, referenciada aqui por fechar o ciclo comercial.
10. **Relacionamento** — vínculo do Contato com a Villa que continua **depois** que cada ciclo de Oportunidade termina. Nunca "termina" de fato — pode ficar dormente e ser reativado, gerando uma nova Oportunidade no futuro.
11. **Campanha** — iniciativa de marketing que gera Contatos/Leads. Fronteira com marketing, não pertence ao sistema comercial em si.
12. **Canal** — meio de relação com o Contato. Este documento separa três papéis de canal, que podem ou não coincidir na prática:
    - **Canal de origem** — onde o Contato chegou pela primeira vez (ex.: Meta Ads, indicação).
    - **Canal atual de conversa** — onde a conversa está acontecendo agora (ex.: WhatsApp).
    - **Canal de conversão/reserva** — onde a Reserva de fato se formaliza (ex.: Booking, WhatsApp, presencial).
13. **Responsável humano** — Rene, Nubia ou Renildo, conforme sensibilidade.
14. **Decisão** — escolha comercial tomada (seção 7).
15. **Ação** — o que é efetivamente feito (seção 8).
16. **Resultado** — desfecho do ciclo da Oportunidade (seção 9).

---

## 5. Estados do Sistema

*(Estado é diferente de entidade — é a "situação atual" que uma entidade assume.)*

### Estado de maturidade (QL) — característica do Contato/Lead
QL1 · QL2 · QL3 · QL4 · NQ

### Estado de risco comercial (C) — característica da mensagem/situação
C1 · C2 · C3 · C4

#### Classificação comercial canônica C1–C4

**C1 — Atendimento simples**

Critérios: pergunta simples; informação comercial ou de produto; dúvida de baixo risco; situação sem preço sensível, exceção, conflito ou negociação.

Responsabilidade: a IA classifica e sugere rascunho; Rene/Nubia revisam e enviam.

Exemplos: diferença entre Pousada e Casa; estrutura; capacidade; localização geral; café da manhã; piscina; dúvida simples sobre acomodação.

**C2 — Atendimento comercial normal**

Critérios: qualificação; comparação comercial; pergunta normal de preço; pedido normal de orçamento; orientação comercial dentro das regras; análise de produto, datas, pessoas ou perfil da viagem.

Responsabilidade: a IA organiza e sugere; Rene/Nubia conduzem dentro das regras; a IA nunca confirma preço, disponibilidade, reserva, pagamento ou acesso.

Exemplos: "Qual o valor?"; "Quero orçamento"; comparação Pousada x Casa; pedido normal de datas e pessoas; envio de orçamento dentro da política, após checagem humana.

**C3 — Negociação ou exceção sensível**

Critérios: desconto; abatimento; crédito; condição especial; exceção; negociação relevante; preço sensível; alteração fora da política; compensação.

Responsabilidade: Rene/Nubia coletam e registram; Renildo decide; a IA não negocia e não promete.

Exemplos: pedido de desconto; condição especial de pagamento; exceção de política; pedido de crédito; abatimento; compensação.

**C4 — Conflito ou risco grave**

Critérios: ameaça; reclamação grave; pressão reputacional; conflito; cobrança contestada; dano contestado; risco elevado; situação sensível com potencial jurídico, financeiro ou reputacional.

Responsabilidade: a IA sugere contenção; Rene/Nubia não resolvem sozinhos; Renildo é obrigatório.

Exemplos: ameaça de avaliação negativa; conflito grave; cobrança contestada; dano contestado; reclamação grave; pressão para decisão sob ameaça.

**Regras de interpretação de C:**
- C mede complexidade e risco comercial da situação atual.
- C não mede maturidade do lead.
- QL mede maturidade do lead.
- Estágio mostra onde o processo comercial está.
- C não substitui QL.
- C não substitui Estágio.
- Um lead pode mudar de C durante a mesma oportunidade.
- Um lead QL4 pode estar em C2, C3 ou C4, conforme a mensagem atual.
- Pergunta normal de preço não é automaticamente C3.
- Pedido normal de orçamento não é automaticamente C3.
- Desconto e exceção são C3.
- Conflito ou risco grave são C4.

**Status e precedência:** a Arquitetura é a fonte oficial de C1–C4. Biblioteca Comercial, Matriz de Roteamento, Jornada, Templates, CRM, agentes, skills e integrações consomem essa definição — nenhum desses componentes pode redefinir C1–C4. **Os documentos consumidores ainda serão atualizados em rodadas posteriores. Até essa propagação, divergências antigas permanecem mapeadas, mas a definição canônica passa a ser a desta Arquitetura.**

### Estado de risco operacional (N) — característica da situação
N1 · N2 · N3 · N4

### Estado processual (estágio da Oportunidade)
1. Novo
2. Em qualificação
3. Orçamento
4. Aguardando retorno
5. Negociação/validação
6. Reservado
7. Perdido
8. Nutrição

### Estado financeiro
Sem valor definido · Valor em análise · Valor aprovado internamente · Valor enviado · Valor aceito pelo hóspede · Pagamento pendente · Pagamento em validação · Pagamento validado

### Estado de reserva
Não solicitada · Solicitada · Em validação · Confirmada · Cancelada · Perdida

**Regras de leitura:**
- Entidade e estado são coisas diferentes.
- **QL é maturidade; não é estágio.** QL4 não significa reserva confirmada, nem estágio "Reservado".
- **C/N é risco (comercial ou operacional); não é maturidade.** Um Contato QL4 pode gerar uma mensagem C1; um Contato QL1 pode gerar uma mensagem C4.
- **Valor aceito pelo hóspede não significa pagamento validado.**
- **Pagamento validado nunca deve ser inferido pela IA** — só existe após confirmação humana explícita.
- **"Reservado" só existe após confirmação humana.**
- **SLA interno da equipe não é follow-up ao lead** — são conceitos diferentes: um é prazo de resposta da equipe, outro é recontato comercial ao Contato.

---

## 6. Eventos do Sistema

| Evento | Quem gera | Quem confirma | Estados que pode alterar | Exige registro? | Exige escalonamento? |
|---|---|---|---|---|---|
| Contato/Lead entrou | Canal/pessoa | — | Estágio → Novo | Sim | Não |
| Lead respondeu | Contato | — | Estágio, C | Sim | Não |
| Produto identificado | IA (sugestão) / humano | Rene/Nubia | Produto | Sim | Não |
| Dados coletados | IA / humano | Rene/Nubia | Maturidade (subsídio ao QL) | Sim | Não |
| QL sugerido | IA | — | (proposta, não estado ainda) | Sim | Não |
| QL confirmado | Rene/Nubia | Rene/Nubia | QL | Sim | Não |
| Risco identificado | IA | Humano revisa | C/N | Sim | Se C4/N4 |
| Orçamento estruturado | Equipe com apoio da IA | Humano | Estado financeiro | Sim | Não |
| Orçamento enviado | Humano (envio manual) | — | Estado financeiro, Estágio → Orçamento | Sim | Não |
| Objeção recebida | Contato | — | C | Sim | Se recorrente/sensível |
| Desconto solicitado | Contato | Renildo decide | — (aguarda decisão) | Sim | Sim, sempre |
| Follow-up realizado | Humano (com base na Matriz) | — | Último contato | Sim | Não |
| Lead respondeu ao follow-up | Contato | — | Estágio, C | Sim | Não |
| Pagamento informado | Contato | Humano/Financeiro | Estado financeiro → pendente/validação | Sim | Se dúvida |
| Pagamento validado | Humano/Financeiro | Humano/Financeiro | Estado financeiro → validado | Sim | Não |
| Reserva confirmada | Humano | Humano | Estado de reserva → confirmada, Estágio → Reservado | Sim | Não |
| Oportunidade perdida | Humano (decisão) | Humano | Estágio → Perdido, Resultado | Sim | Não |
| Oportunidade movida para nutrição | Humano | Humano | Estágio → Nutrição | Sim | Não |
| Hóspede fez check-in | Operação | Operação | Estadia iniciada | Sim (domínio operacional) | Conforme N |
| Hóspede fez check-out | Operação | Operação | Estadia encerrada | Sim | Conforme N |
| Pós-venda realizado | Humano | Humano | Relacionamento | Sim | Não |
| Reativação iniciada | Humano/IA (sugestão) | Humano | Relacionamento → nova Oportunidade possível | Sim | Não |

---

## 7. Decisões Comerciais

### Decisões simples (Rene/Nubia revisam e executam)
Identificar produto · confirmar QL sugerido · sugerir próxima pergunta · escolher template · realizar follow-up de rotina · definir prioridade de atendimento.

### Decisões sensíveis (exigem Renildo)
Decidir desconto · decidir preço fora de tabela · decidir exceção de regra · validar pagamento em caso de dúvida · confirmar reserva sensível/fora de padrão · decidir compensação · encerrar conflito · definir perda em caso disputado.

### Sugestões da IA (nunca são decisão final)
Classificar QL · classificar C/N · sugerir próxima pergunta · sugerir template · sugerir follow-up · sugerir prioridade · apoiar a estruturação do orçamento (sem definir o valor final).

| Decisão | Quem sugere | Quem confirma | Quem executa | Quem registra |
|---|---|---|---|---|
| Identificar produto | IA | Rene/Nubia | Rene/Nubia | Rene/Nubia |
| Classificar QL | IA | Rene/Nubia | — | Rene/Nubia |
| Estruturar orçamento | IA (apoio) | Equipe/Renildo (valor final) | Rene/Nubia | Rene/Nubia |
| Decidir desconto | — | Renildo | Renildo | Renildo/Rene registra |
| Decidir preço | — | Renildo | Renildo | Renildo/Rene registra |
| Validar pagamento | — | Humano (financeiro) | Humano | Humano |
| Confirmar reserva | — | Humano | Humano | Humano |
| Definir perda | IA sugere | Rene/Nubia (ou Renildo se disputado) | Rene/Nubia | Rene/Nubia |
| Mover para nutrição | IA sugere | Rene/Nubia | Rene/Nubia | Rene/Nubia |

---

## 8. Ações Comerciais

Perguntar · esclarecer · orientar · apresentar produto · coletar dados · apoiar a estruturação de orçamento · encaminhar para orçamento · enviar orçamento · responder objeção · fazer follow-up · escalar · pausar · encerrar · nutrir · reativar · pós-venda · registrar · revisar.

Cada ação tem objetivo, condição de uso, responsável, risco e resultado esperado — detalhamento operacional pertence aos processos de implementação (Funil, Matriz, Biblioteca), não a este documento conceitual.

---

## 9. Resultados Comerciais

- **Convertido** — a Oportunidade vira Reserva confirmada (sempre por humano).
- **Perdido** — ciclo da Oportunidade fechado sem conversão, com motivo.
- **Sem resposta** — silêncio persistente após cadência completa.
- **Fora do perfil** — NQ, não se encaixa no que a Villa oferece.
- **Nutrição** — Oportunidade sem fechamento, Contato mantido em contato leve.
- **Reativação futura** — Relacionamento reaberto após período dormente, podendo gerar nova Oportunidade.
- **Reserva confirmada / cancelada** — só após confirmação humana.
- **Pós-venda concluído** — relacionamento mantido após a estadia.

**Regra:** resultado só é registrado após confirmação humana do desfecho real. A IA pode sugerir, nunca inferir ou declarar um resultado.

---

## 10. Máquina de Decisão Comercial

```text
Mensagem ou evento
↓
Leitura inicial de risco
↓
Identificação do Contato/Lead
↓
Identificação do produto
↓
Leitura do histórico
↓
Sugestão de QL
↓
Classificação C/N
↓
Estado comercial atual (estágio da Oportunidade)
↓
Regra aplicável
↓
Próxima ação sugerida
↓
Responsável humano
↓
Revisão
↓
Execução manual
↓
Registro
↓
Novo estado
```

- **Onde pode ser interrompido:** logo na "Leitura inicial de risco" (gatilho evidente de risco pula direto para contenção/escalonamento), ou em qualquer decisão sensível que aguarda Renildo.
- **Quando vai para Renildo:** sempre que a regra aplicável envolver preço, desconto, exceção, pagamento, reembolso, compensação, conflito ou reserva fora do padrão.
- **Quando termina:** quando o "Novo estado" é registrado e não há próxima ação pendente.
- **Como recomeça:** a próxima mensagem ou evento reinicia o ciclo a partir da "Leitura inicial de risco", sempre considerando o histórico e o estado atual.

---

## 11. Fronteiras entre Domínios

- **Marketing** — gera demanda e origem (campanha, canal de origem). Termina quando o Contato/Lead existe.
- **Comercial** (este sistema) — qualifica, acompanha e conduz a decisão, do Lead ao Resultado.
- **Atendimento** — responde e orienta dentro da conversa (execução do "como dizer").
- **Operação** — entrega a estadia, a partir da Reserva confirmada.
- **Financeiro** — valida valores, pagamentos e resultado financeiro.
- **Revenue Management** — recomenda preço e cenário; não decide.
- **Pós-venda** — mantém relacionamento após a estadia.
- **Aprendizado** — analisa padrões do piloto e sugere melhoria, sem decidir sozinho.

---

## 12. Regras que nunca podem ser quebradas (Invariantes)

- A IA nunca envia.
- A IA nunca confirma disponibilidade.
- A IA nunca confirma reserva.
- A IA nunca valida pagamento.
- A IA nunca define preço final.
- A IA nunca concede desconto.
- A IA nunca libera acesso (chave, senha, endereço).
- A IA nunca cria exceção.
- A IA nunca altera estado sensível sem humano.
- A IA nunca prepara valor de orçamento sozinha.
- Pousada Arágua e Casa Arágua Mariscal nunca são tratadas como o mesmo produto.
- Registro Comercial não é Diário de Bordo.
- SLA interno da equipe não é follow-up ao lead.
- QL não é estágio.
- C/N não é maturidade.
- Reserva só existe após confirmação humana.
- Valor aceito não é pagamento validado.
- Pagamento validado nunca é inferido pela IA.
- Aprendizado nunca vira regra sem aprovação de Renildo.
- **Nenhum conceito comercial pode possuir duas definições oficiais dentro do projeto.** QL, C, Estágio, Ativo Comercial, Follow-up e Registro Comercial possuem uma única fonte de verdade. Documentos operacionais, agentes, skills e integrações apenas consomem essas definições.
- **Em caso de divergência entre a Arquitetura e qualquer documento operacional, a Arquitetura prevalece.** A correção deve ser feita no documento consumidor, mediante rodada própria e aprovação explícita de Renildo. Nenhuma IA pode reconciliar ou alterar conceitos automaticamente.

---

## 13. Arquitetura em Camadas

| Camada | Função | Responsabilidade | Dependências |
|---|---|---|---|
| 1. Entrada | Captar o Contato/Lead/mensagem | Não perder contato | Canais de marketing/atendimento |
| 2. Contexto | Reunir histórico | Não repetir pergunta já respondida | Registro Comercial |
| 3. Qualificação | Sugerir QL | Ler maturidade real | Funil (critérios) |
| 4. Risco | Classificar C/N | Detectar risco cedo | Regras de risco |
| 5. Decisão | Aplicar regra e sugerir ação | Coerência da próxima ação | Matriz/Biblioteca |
| 6. Resposta | Formular rascunho | Tom e conteúdo corretos | Biblioteca de templates |
| 7. Humana | Revisar e decidir | Controle final | Rene/Nubia/Renildo |
| 8. Registro | Gravar o que ocorreu | Rastreabilidade | Registro Comercial |
| 9. Acompanhamento | Monitorar follow-up/cadência | Não deixar Contato esquecido | Matriz |
| 10. Resultado | Fechar o ciclo da Oportunidade | Fechamento correto | Humano |
| 11. Aprendizado | Analisar padrões | Não virar regra sozinho | Aprovação de Renildo |
| 12. Integração futura | Conectar tecnologia | Nunca remover revisão humana | Decisão de governança futura |

---

## 14. Controle Humano

- **Rene** — primeira linha; revisa rascunhos simples; confirma/corrige QL; envia mensagens; registra.
- **Nubia** — substituta de Rene, mesmas permissões.
- **Renildo** — decide casos sensíveis (C3/C4, desconto, exceção, compensação, conflito); aprova mudanças estruturais; interrompe o sistema se necessário.

---

## 15. Papel da Inteligência Artificial

**A IA pode:** ler, classificar, sugerir, organizar, comparar, apontar risco, propor rascunho, propor próxima ação, apoiar a estruturação de orçamento, registrar candidato (a template/regra), explicar a decisão sugerida.

**A IA não pode:** decidir, enviar, confirmar, cobrar, prometer, negociar, liberar acesso, definir valor final de orçamento, persistir regra sozinha, alterar estado sensível sem humano.

---

## 16. Modelo Mínimo de Informação

| Dado | Categoria |
|---|---|
| Identificação do Contato | Obrigatório desde o início |
| Canal de origem | Obrigatório desde o início |
| Canal atual de conversa | Obrigatório quando disponível |
| Produto | Obrigatório quando disponível |
| Datas | Obrigatório quando disponível |
| Número de pessoas | Obrigatório quando disponível |
| Histórico | Obrigatório quando disponível |
| QL | Obrigatório quando disponível (sugerido pela IA, confirmado por humano) |
| C/N | Obrigatório quando disponível (classificado pela IA, revisado por humano) |
| Estágio da Oportunidade | Obrigatório quando disponível |
| Responsável | Obrigatório quando disponível |
| Próxima ação | Obrigatório quando disponível |
| Último contato | Obrigatório quando disponível |
| Canal de conversão/reserva | Obrigatório quando a Reserva se formaliza |
| Resultado | Opcional até o fechamento do ciclo |
| Dados de pagamento | Sensível — exclusivamente humano |
| Confirmação de reserva | Exclusivamente humano |

*Nota: "Oportunidade" permanece entidade conceitual nesta fase — não deve ainda virar campo obrigatório do Registro Comercial.*

---

## 17. Métricas Conceituais

Volume de Contatos/Leads · origem · produto · distribuição QL · tempo interno de resposta (SLA) · avanço de estágio · orçamento enviado · follow-up realizado · resposta ao follow-up · conversão · perda · motivo de perda · escalonamento · participação de Renildo · tempo liberado · satisfação do hóspede · retrabalho.

*(Fórmulas de cálculo não fazem parte desta camada conceitual — pertencem à implementação.)*

---

## 18. Princípios para Implementação Futura

Este documento continua válido mesmo que o sistema use Markdown, planilha, Notion, Airtable, HubSpot, Supabase, banco de dados, integração com WhatsApp, ou qualquer outro software, porque:

- Conceitos não dependem da ferramenta.
- Entidades não dependem da ferramenta.
- Estados não dependem da ferramenta.
- Regras não dependem da ferramenta.
- Automação nunca remove revisão humana sem nova decisão de governança.
- Migração de tecnologia deve preservar histórico e rastreabilidade.

---

## 19. Relação com Documentos Futuros

Depois de aprovada, esta arquitetura dá origem a:

1. Mapa do Cérebro Comercial (implementação documental dos conceitos aqui definidos).
2. Governança documental.
3. Correção de Funil, Matriz e Biblioteca.
4. Registro Comercial (hoje chamado CRM).
5. Atualização de agentes.
6. Atualização de skills.
7. Testes.
8. Piloto comercial.
9. Integração futura.

Esta arquitetura define conceitos; os documentos de implementação definem onde esses conceitos vivem hoje. Em caso de conflito entre esta Arquitetura e o Mapa Comercial, esta Arquitetura prevalece.

---

## 20. Riscos Conceituais

| Risco | Severidade |
|---|---|
| Confundir Contato com Lead (permanente x temporário) | Alto |
| Confundir Lead com Reserva | Alto |
| Confundir entidade com estado | Alto |
| Confundir QL com estágio | Alto |
| Confundir C com "temperatura" de anúncio | Médio |
| Confundir N com problema puramente comercial | Médio |
| Confundir follow-up com atraso interno da equipe | Alto |
| Confundir canal de origem com canal de conversão | Médio |
| Criar automação antes de processo maduro | Alto |
| Registrar estado sem confirmação humana | Alto |
| Duplicar conceitos em documentos diferentes | Médio |
| Depender demais de uma ferramenta específica | Médio |
| Excesso de complexidade para o time | Médio |
| Processo pesado para Rene/Nubia | Médio |
| IA assumir poder decisório de fato | Alto |
| Tratar "Oportunidade" como campo obrigatório antes da hora | Baixo |

---

## 21. Roadmap Conceitual

- **Etapa A — Arquitetura:** este documento.
- **Etapa B — Mapa Comercial:** implementação documental dos conceitos.
- **Etapa C — Governança:** precedência de fontes.
- **Etapa D — Processos:** Funil, Matriz, Biblioteca.
- **Etapa E — Registro:** Registro Comercial (CRM).
- **Etapa F — Inteligência:** agentes e skills.
- **Etapa G — Validação:** testes.
- **Etapa H — Operação:** piloto manual.
- **Etapa I — Tecnologia:** integração futura.

---

## 22. Changelog

*(Changelog próprio desta Arquitetura — independente do changelog do futuro Mapa Comercial.)*

- **2026-08-05 — Claude (a pedido de Renildo):** criação do documento com o conteúdo conceitual aprovado, incorporando os ajustes de Contato/Lead, Oportunidade, separação de canais e demais decisões desta rodada.
- **05/08/2026 — Claude (a pedido de Renildo):** Definição canônica de C1–C4 e Regra da Fonte Única. Conteúdo: definição oficial de C1 (atendimento simples); definição oficial de C2 (atendimento comercial normal, incluindo pergunta normal de preço e pedido normal de orçamento); definição oficial de C3 (negociação ou exceção sensível, incluindo desconto e exceção); definição oficial de C4 (conflito ou risco grave); regras de interpretação separando C, QL e Estágio; inserção da Regra da Fonte Única na seção 12 (nenhum conceito comercial com duas definições oficiais); definição de precedência da Arquitetura sobre documentos operacionais em caso de divergência. **Observação:** documentos consumidores (Biblioteca Comercial, Matriz de Roteamento de Agentes, `villa-orquestrador-triagem.md`, script de teste, Mapa do Cérebro IA, Mapa do Cérebro Comercial) ainda aguardam atualização em rodadas próprias — nenhum deles foi alterado nesta rodada.
