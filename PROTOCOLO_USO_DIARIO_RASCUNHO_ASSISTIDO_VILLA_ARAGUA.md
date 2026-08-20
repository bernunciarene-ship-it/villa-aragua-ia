# PROTOCOLO_USO_DIARIO_RASCUNHO_ASSISTIDO_VILLA_ARAGUA

**Projeto:** VILLA ARAGUA IA
**Rodada:** 4 — Automação WhatsApp segura (base original); atualizado no Lote 11 da série "WhatsApp Rápido"
**Tema:** 4.25 — Protocolo de uso diário do Rascunho Assistido
**Data de persistência original:** 2026-07-16
**Data de atualização:** 2026-08-05 (Lote 11)
**Modo:** Rascunho Assistido
**Status:** aprovado para piloto diário assistido; WhatsApp real não conectado; nenhuma automação criada.

**Arquivos-base:**
- `BIBLIOTECA_OFICIAL_RECEPCIONISTA_IA_VILLA_ARAGUA.md`
- `BIBLIOTECA_COMERCIAL_RECEPCIONISTA_IA_VILLA_ARAGUA.md`
- `MODO_RASCUNHO_ASSISTIDO_VILLA_ARAGUA.md`
- `DIARIO_BORDO_PILOTO_RECEPCIONISTA_IA_VILLA_ARAGUA.md` (registro diário do piloto, criado no Lote 11)
- `MAPA_CONTROLE_ATUAL_RECEPCIONISTA_IA_VILLA_ARAGUA.md` (diagnóstico pós-Lotes 1-10)

**WhatsApp real:** não conectado
**Zapier / Make / API / backend:** não conectados
**Automação real:** não autorizada

---

## 1. Diagnóstico

A Villa Arágua IA já tem, após os Lotes 1 a 10 da série "WhatsApp Rápido":

- Biblioteca Oficial persistida e testada (16 templates N2, 24 N3, 5 N4, além dos N1 originais);
- Biblioteca Comercial persistida e testada (38 códigos `PC-EXT`);
- 4 regras transversais e 2 alertas internos (mensagem com múltiplos temas, pressão comercial/reputacional, contradição/dado confuso, espanhol/portunhol, resposta em blocos, linguagem de execução autônoma);
- Modo Rascunho Assistido persistido;
- Teste cego aprovado (Lote 10 — 30/30 casos corretos em conteúdo, risco e escalonamento);
- bloqueio explícito de WhatsApp real e automação.

O próximo desafio não é criar mais biblioteca. É transformar tudo isso em **rotina segura de uso humano diário**, para que Rene, Nubia e Renildo consigam usar a IA no dia a dia sem confundir rascunho com decisão automática, com uma classificação e um fluxo de escalonamento que reflitam a biblioteca atual — não mais o esquema inicial da Rodada 4.

---

## 2. Objetivo do piloto diário assistido

Criar um procedimento simples para usar a Recepcionista IA durante um **piloto de 2 semanas** (prorrogável por mais 1 semana, se necessário).

**Volume inicial seguro:** 5 a 10 mensagens reais por dia usando o Modo Rascunho Assistido.

**Objetivo do piloto:** validar a **rotina humana de revisão** — não o conteúdo da biblioteca, que já foi validado nos Lotes 1 a 10 (incluindo teste cego). O piloto testa se Rene, Nubia e Renildo conseguem:

- economizar tempo real de atendimento;
- reduzir erro de resposta;
- manter padrão de comunicação;
- identificar lacunas reais no dia a dia;
- separar operação, comercial e pós-estadia;
- evitar decisões automáticas;
- proteger preço, disponibilidade, desconto, exceção e reputação;
- manter disciplina operacional sem sobrecarregar Renildo nem criar insegurança para Rene/Nubia.

**O que o piloto não deve tentar fazer:** conectar WhatsApp real, API, Zapier, Make ou qualquer automação; validar volume máximo de mensagens; testar temas que a biblioteca já validou tecnicamente — o piloto é sobre disciplina de uso, não sobre conteúdo.

---

## 3. Regra central

A IA só ajuda a escrever.

A IA não decide.

A IA não envia.

A IA não confirma preço.

A IA não confirma disponibilidade.

A IA não confirma pagamento.

A IA não concede desconto.

A IA não autoriza exceção.

A IA não libera acesso.

A mensagem final enviada ao hóspede é sempre responsabilidade humana.

---

## 4. Papéis da equipe

| Pessoa | Papel | Pode aprovar sozinho? | Deve escalar quando? | Não pode decidir | Observações |
|---|---|---|---|---|---|
| **Rene** | Primeira linha — recebe, cola na IA, revisa, envia | Sim, para N1/N2/comercial simples, dentro dos templates | Preço, desconto, exceção, item de valor, reclamação com risco, qualquer dúvida | Preço, desconto, exceção, cobrança, dano, avaliação | Segue exatamente os templates; nunca "melhora" o texto criando promessa nova |
| **Nubia** | Substituta de Rene, mesmo fluxo | Sim, mesmas condições de Rene | Mesmos critérios de Rene | Mesmos limites de Rene | Assume integralmente o papel sempre que Rene estiver ausente |
| **Renildo** | Decisão sensível, financeira, reputacional | Sim, para tudo, incluindo exceções | Não escala — é o destino final da escalada | — | Também aprova mudanças na biblioteca e no protocolo |
| **IA Recepcionista** | Rascunhadora e organizadora | Nunca | Sempre "sinaliza" ao classificar N3/N4/comercial sensível — quem decide o envio é humano | Qualquer coisa | Só sugere; nunca envia; nunca decide; nunca confirma sozinha |

A IA deve sempre devolver: classificação; template usado ou lacuna; rascunho sugerido; nível de risco; destino de escalonamento, se houver (ver seção 10).

---

## 5. Classificação operacional por nível

| Nível | Quem revisa | Quem pode enviar | Tempo-alvo interno de revisão | Exemplos | Escalonamento obrigatório |
|---|---|---|---|---|---|
| **N1 — Simples** | Rene/Nubia | Rene/Nubia | Até 5 min | Localização, Wi-Fi, horário de piscina da Pousada | Não |
| **N2 — Operacional simples** | Rene/Nubia | Rene/Nubia | Até 10 min | Café da manhã, limpeza/enxoval, achados e perdidos simples, estacionamento | Não, salvo dúvida |
| **N3 — Sensível** | Rene/Nubia revisam, atentos ao gatilho de escalada | Rene/Nubia, exceto quando o próprio template pede Renildo | Até 15 min | Chegada fora do padrão, early check-in, reclamação, item de valor | Sim, se envolver pedido financeiro, item de valor ou reclamação repetida |
| **N4 — Crítico** | Rene/Nubia contêm, Renildo decide | Só Renildo, ou Rene/Nubia com aprovação explícita de Renildo | Imediato (minutos) | Gás, confronto entre hóspedes, hóspede sem acesso, segurança | Sempre |
| **Comercial simples** | Rene/Nubia | Rene/Nubia | Até 10 min | Orientação por perfil, fotos catalogadas, coleta de datas | Não |
| **Comercial financeiro** | Rene/Nubia coletam dados; Renildo decide valor | Só Renildo confirma valor/desconto | Até 1 hora | Desconto, parcelamento especial, equiparação de preço | Sempre |
| **Pós-estadia simples** | Rene/Nubia | Rene/Nubia | Até 10 min | Agradecimento, convite à avaliação, indicação de amigo | Não |
| **Pós-estadia sensível** | Rene/Nubia registram; Renildo decide | Só Renildo | Até 1 hora, priorizado no mesmo dia | Avaliação negativa, reembolso, dano/cobrança pós-saída | Sempre |

**Importante:** os tempos acima são metas internas de organização da equipe, **nunca promessas ao hóspede** — não devem ser comunicados como SLA externo em nenhuma hipótese.

---

## 6. Fila diária de atendimento

| Período | Quem olha | O que prioriza | Quando chama Renildo | Como evitar acúmulo |
|---|---|---|---|---|
| **Manhã** | Rene | Mensagens acumuladas da noite; check-ins do dia; cafés/horários | Se houver N4 ou pedido financeiro pendente da noite | Responder N1/N2 primeiro, deixar N3 para o meio do dia se não for urgente |
| **Meio do dia** | Rene ou Nubia | Reservas em andamento, dúvidas comerciais, check-outs do dia | Reclamações com risco reputacional | Revisar a fila a cada 2-3 horas |
| **Fim da tarde** | Nubia (ou quem estiver disponível) | Chegadas do dia, pendências comerciais em aberto | Qualquer caso N3/N4 não resolvido até aqui | Fechar o dia com a fila zerada ou pendências claramente registradas |
| **Noite** | Sob demanda — **não é plantão para mensagens comuns** | Apenas emergências reais (gás, acesso, segurança) | Sempre, se for N4 | Mensagens não urgentes esperam até a manhã seguinte |
| **Finais de semana** | Escala reduzida (Rene ou Nubia, alternando) | Check-ins/check-outs do período, emergências | Mesma regra de N4 | Definir previamente quem está de sobreaviso |
| **Alta temporada** | Reforço de atenção nos horários de pico (chegada 15h-22h) | Priorizar acesso/chegada e reclamações | Renildo mais disponível nesse período | Revisar a fila a cada 1-2h só nesse período |

---

## 7. Escalonamento obrigatório para Renildo

| Caso | Por que vai para Renildo | Informação mínima para decidir | Rascunho provisório permitido, sem promessa |
|---|---|---|---|
| Desconto | Decisão financeira, nunca da IA | Produto, datas, motivo do pedido | "Vou levar sua solicitação para a equipe avaliar." |
| Reembolso | Decisão financeira crítica | Número da reserva, motivo | "Questões de valores são avaliadas separadamente pela equipe." |
| Crédito | Decisão financeira | Reserva original, novo período pretendido | Mesmo padrão de reembolso |
| Abatimento | Decisão financeira | Motivo da reclamação vinculada | Mesmo padrão |
| Compensação | Decisão financeira/reputacional | Descrição do problema | "Vou registrar e encaminhar com prioridade." |
| Cobrança contestada | Risco financeiro + reputacional | Número da reserva, valor, contexto | "A equipe vai revisar o caso com atenção antes de qualquer encaminhamento." |
| Dano contestado | Mesmo padrão de cobrança | Descrição do dano, posição do hóspede | Mesmo padrão |
| Avaliação negativa | Risco reputacional | O que motivou, se já publicada | "Quero entender melhor o que aconteceu." |
| Ameaça reputacional | Risco reputacional alto | Contexto completo — nunca mencionar a ameaça na resposta | "Vou levar isso com prioridade para a equipe." |
| Negociação sob pressão | Risco de ceder indevidamente | Natureza da pressão (urgência, comparação, ameaça) | Resposta calma, sem entrar em leilão |
| Item de valor | Risco reputacional + logístico | Acomodação, data, descrição detalhada | "Encaminho para a equipe verificar com prioridade." |
| Conflito grave | Segurança física/emocional | Localização, acomodações envolvidas | "Por favor, não vá até lá diretamente." |
| Exceção financeira | Decisão comercial | Qual exceção, contexto | "Isso não é algo que decido por aqui." |
| Reclamação repetida | Risco reputacional acumulado | Histórico do problema | "Você tem razão em cobrar retorno." |
| Caso fora da política | Nenhum template cobre | Descrição completa da situação | Resposta neutra de acolhimento, sem inventar regra |
| Dúvida sobre liberar acesso sem pagamento validado | Segurança + financeiro | Nome da reserva, status do pagamento | "As instruções são enviadas pela equipe após confirmação." |
| Rene/Nubia inseguros sobre qualquer caso | Prevenção de erro | O caso inteiro, tal como está | Não enviar nada até checar com Renildo |

---

## 8. Autonomia de Rene/Nubia

Podem revisar e enviar sem Renildo, **desde que o rascunho esteja dentro do template e sem nenhuma promessa extra**:

- Dúvidas comerciais simples.
- Coleta de datas/pessoas.
- Envio de fotos catalogadas.
- Orientação Pousada x Casa sem disponibilidade confirmada.
- Check-in/check-out padrão.
- Café da manhã padrão.
- Limpeza/enxoval simples.
- Wi-Fi simples.
- Manutenção simples sem promessa de prazo.
- Churrasqueira sob consulta.
- Visitantes sob consulta, sem autorizar.
- Achados e perdidos simples.
- Agradecimento pós-check-out.
- Indicação de amigo.
- Nova reserva sem desconto.

**Limites válidos para todos os itens acima:**
- Nunca confirmar disponibilidade.
- Nunca prometer preço.
- Nunca prometer desconto.
- Nunca prometer exceção.
- Nunca liberar acesso.
- Nunca confirmar item achado/não achado sem checagem real.

---

## 9. Como colar a mensagem na IA

Formato padrão:

```text
Mensagem do hóspede:
"[colar exatamente a mensagem recebida]"

Contexto:
Produto: Pousada / Casa / não sei
Reserva: confirmada / não confirmada / não sei
Data da estadia: [se souber]
Número de pessoas: [se souber]
Observação importante: [se houver]
```

Exemplo:

```text
Mensagem do hóspede:
"Quero saber se tem disponibilidade para 20 a 27 de dezembro e quanto fica para 4 pessoas."

Contexto:
Produto: não sei
Reserva: não confirmada
Data da estadia: 20 a 27 de dezembro
Número de pessoas: 4
Observação importante: lead novo
```

---

## 10. Como a IA deve responder

A resposta da IA deve seguir este padrão:

```text
Classificação:
N1 / N2 / N3 / N4 / Comercial simples / Comercial financeiro / Pós-estadia simples / Pós-estadia sensível / Lacuna

Template usado:
[código do template] ou "sem template dedicado"

Rascunho sugerido:
[texto para revisão humana]

Pode enviar direto?
Sim, com revisão / Não, precisa escalar

Escalonamento:
Rene / Nubia / Renildo / não necessário

Observação de risco:
[se houver]
```

---

## 11. Checklist de revisão do rascunho

**Checklist para Rene/Nubia (todo rascunho, antes de enviar):**
1. A IA prometeu algo que depende da equipe?
2. Confirmou disponibilidade sem checagem real?
3. Confirmou pagamento sem validação?
4. Citou preço sem checagem?
5. Ofereceu desconto, crédito ou compensação?
6. Enviou dado sensível antes da hora?
7. Pareceu que a própria IA verificou/decidiu algo sozinha?
8. Pediu dados demais?
9. Soou fria ou robótica?
10. O tom está adequado?
11. Precisa escalar para Renildo?

Se qualquer resposta for "sim" em ponto sensível, não enviar sem ajuste.

**Checklist adicional para Renildo (casos sensíveis/N4):**
1. O rascunho evita acusar ou negar responsabilidade indevidamente?
2. Está livre de qualquer promessa financeira?
3. O tom está neutro e maduro?
4. A ameaça, se houver, foi contida sem ser mencionada na resposta?
5. A decisão final está clara como sendo humana, não da IA?
6. Vale a pena registrar este caso como aprendizado futuro?

---

## 12. Protocolo de erro e aprendizado

Quando a IA errar, o humano deve:

1. Não enviar a resposta como está.
2. Marcar o tipo de erro (ver categorias abaixo).
3. Corrigir manualmente antes de enviar ao hóspede.
4. Registrar o erro no `DIARIO_BORDO_PILOTO_RECEPCIONISTA_IA_VILLA_ARAGUA.md`.
5. Classificar a natureza do erro:
   - erro pontual de redação;
   - erro de classificação;
   - falta de template;
   - falta de dado oficial;
   - caso para pendência;
   - caso para Renildo decidir regra nova.
6. Só persistir qualquer aprendizado (template, regra, pendência) **depois da aprovação explícita de Renildo** — nunca automaticamente a partir do registro diário.

**Categorias de erro:**
- Promessa indevida.
- Risco mal classificado.
- Escalonamento errado.
- Dado oficial inventado.
- Tom inadequado.
- Excesso de resposta (tentou resolver tudo de uma vez).
- Pergunta de dado desnecessário.
- Idioma ruim.
- Frase que parece execução autônoma.
- Template insuficiente.

---

## 13. O que fazer quando não há template

Se não houver template, a IA deve declarar:

"Sem template dedicado."

Depois disso, pode sugerir uma resposta de contenção segura, mas sem transformar isso em regra oficial.

Modelo:

```text
Classificação:
Lacuna — Comercial / Operacional / Pós-estadia

Template:
Sem template dedicado

Rascunho seguro:
[resposta curta e neutra]

Recomendação:
Registrar como candidato a novo template, para avaliação de Renildo.
```

---

## 14. Indicadores simples de qualidade

Medir semanalmente, sem complicar (registrados no fechamento semanal do Diário de Bordo):

- Número de rascunhos usados na semana.
- % aprovados sem ajuste.
- % aprovados com ajuste.
- % rejeitados.
- Tempo médio de revisão (estimativa simples, não cronômetro exato).
- Número de escalonamentos para Renildo.
- Principais tipos de erro (top 3 da semana).
- Temas mais frequentes (top 3).
- Pendências recorrentes.
- Casos de risco evitados (quantas vezes o checklist pegou algo antes do envio).
- Tempo economizado estimado (percepção qualitativa: ajudou muito / ajudou pouco / não ajudou).

---

## 15. Limites do piloto

Não entram no piloto assistido inicial, mesmo que a biblioteca já os cubra tecnicamente:

- Envio automático.
- Respostas sem revisão humana.
- Acesso/chave/senha sem revisão redobrada.
- Pagamento não validado.
- Reclamação grave.
- Avaliação negativa.
- Desconto/reembolso.
- Cobrança/dano.
- Emergência (gás, segurança).
- Item de valor.
- Exceções fora da política.

Esses casos podem usar a IA apenas como apoio pontual de rascunho, sempre com revisão humana forte e Renildo quando necessário — nunca como fluxo de rotina simples do piloto.

Também não fazer neste piloto: conectar WhatsApp real; usar Zapier, Make, API ou backend; permitir que a IA responda ao hóspede diretamente; usar a IA como decisão final; testar com hóspede irritado sem humano experiente revisando.

---

## 16. Rotina semanal de manutenção

**30 a 45 minutos, toda semana, Renildo:**
1. Revisar os erros registrados no Diário de Bordo.
2. Revisar os escalonamentos da semana (fizeram sentido?).
3. Decidir pendências (algo virou dado oficial definido?).
4. Aprovar ou negar novos aprendizados propostos.
5. Limpar duplicidades (dois registros do mesmo aprendizado).
6. Atualizar a biblioteca **somente se necessário** — seguindo sempre o protocolo já validado (backup, verificação de código livre, teste, confirmação).
7. Revisar 5 mensagens aleatórias da semana, independentemente de terem gerado erro.
8. Avaliar se a IA está ficando burocrática (respostas frias, distantes) ou permissiva demais (relaxando travas com o tempo).

---

## 17. Registro diário do piloto

O registro diário de uso **não é feito neste documento** — é feito em `DIARIO_BORDO_PILOTO_RECEPCIONISTA_IA_VILLA_ARAGUA.md`, criado no Lote 11 especificamente para esse fim, com os campos: Data, Horário, Quem revisou, Tipo de mensagem, Nível de risco, Template/regra usado, Rascunho aprovado?, Ajuste feito?, Escalou para Renildo?, Motivo, Aprendizado, Precisa persistir?, Observação.

Tempo máximo recomendado para o preenchimento diário: 5 a 10 minutos ao final do dia.

---

## 18. Critérios de sucesso e de alerta

**O piloto será considerado bom se:**
- Rene e Nubia conseguirem usar sem confusão;
- Renildo for acionado só quando necessário;
- N3/N4 e casos comerciais/pós-estadia sensíveis forem escalados corretamente;
- nenhuma resposta inventar preço ou disponibilidade;
- nenhuma exceção for concedida pela IA;
- houver economia real de tempo;
- o tom das respostas ficar mais padronizado;
- surgirem lacunas claras para eventuais novos templates.

**O piloto deve ser pausado ou revisado se acontecer:**
- humano copiar e colar sem ler;
- IA sugerir preço;
- IA confirmar disponibilidade;
- IA conceder desconto;
- IA criar exceção;
- IA confundir Casa e Pousada;
- hóspede reclamar de resposta automática/fria;
- Rene ou Nubia ficarem inseguros sobre quando escalar;
- Renildo receber mais problema em vez de menos.

---

## 19. Decisão do Tema 4.25 e atualização do Lote 11

O Protocolo de uso diário do Rascunho Assistido foi aprovado originalmente em 2026-07-16 (Tema 4.25) e **atualizado em 2026-08-05 (Lote 11)** para refletir a biblioteca e as regras consolidadas nos Lotes 1 a 10, incluindo classificação por nível atualizada, matriz de papéis com tempo-alvo, fila diária por período, escalonamento detalhado para Renildo, autonomia explícita de Rene/Nubia, protocolo de erro categorizado e indicadores simples de qualidade.

Ele define como Rene, Nubia e Renildo devem usar as bibliotecas Oficial e Comercial no atendimento real, sem automação.

Status:
- pronto para piloto diário assistido de 2 semanas;
- persistido em arquivo;
- sem WhatsApp conectado;
- sem automação;
- humano continua no controle.
