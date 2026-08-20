# MAPA DO CÉREBRO IA VILLA ARÁGUA

**Projeto:** VILLA ARAGUA IA
**Gerado em:** 2026-07-16
**Última atualização:** 2026-08-13 — reorganização completa da estrutura deste mapa (escopo, vocabulário de status, tabela de agentes/módulos, separação Pousada x Casa, regras máximas, financeiro em cinco caixas, Marketing & Meta Ads IA, Operação Semi-Autônoma, fluxos principais e próximos passos). Nenhum conteúdo anterior foi apagado — todo o histórico de 2026-07-16 a 2026-08-06 (estado do projeto, inventário de arquivos, testes, aprendizados de Meta Ads, série "WhatsApp Rápido", propagação C1–C4) está preservado, na íntegra, no **Anexo A** ao final deste arquivo. Ver seção 16 para o changelog desta reorganização.
**Rodada de origem:** Rodada 4 — Automação WhatsApp segura; arquitetura dos agentes formalizada em `DEFINICAO_AGENTES_VILLA_ARAGUA_IA.md` e `MATRIZ_ROTEAMENTO_AGENTES_VILLA_ARAGUA.md`
**Propósito:** mapa central de inteligência da Villa Arágua IA — o que ela sabe, quais áreas apoia, quais agentes/módulos existem de fato, quais limites ela deve respeitar sempre, e quais decisões continuam humanas.

---

## 1. Objetivo deste arquivo

Este arquivo é o **mapa central da inteligência da Villa Arágua IA**. Ele existe para que Renildo (e qualquer assistente de IA — Claude, ChatGPT ou outro — que apoie a operação) consiga responder rapidamente:

- o que a IA da Villa Arágua sabe;
- quais áreas da operação ela apoia (atendimento, comercial, operacional, marketing, precificação, financeiro, experiência, risco, governança e aprendizado);
- quais agentes, papéis ou módulos existem de fato hoje, e quais são só candidatos;
- quais limites a IA deve respeitar sempre, sem exceção;
- quais fluxos já estão definidos e funcionando;
- quais decisões continuam — e sempre continuarão — humanas;
- quais documentos são fonte de verdade, e quais são só apoio ou histórico;
- quais próximos passos fazem sentido, em que ordem.

**Reforço explícito, válido para qualquer leitor deste arquivo, humano ou IA:** a Villa Arágua IA **não é autônoma em nenhuma frente**. Ela organiza, classifica, sugere e apoia — quem decide, aprova e envia é sempre um humano (Rene, Nubia ou Renildo). Este arquivo, por si só, não cria, conecta ou autoriza nenhuma automação.

---

## 2. Escopo deste mapa

Este mapa fala **apenas sobre a Villa Arágua**, que reúne dois produtos:

1. **Pousada Arágua** — pousada pequena, charmosa e acolhedora, 8 acomodações, próxima da Praia de Mariscal, em Bombinhas/SC. Café da manhã na suíte, piscina, churrasqueira, clima familiar.
2. **Casa Arágua Mariscal** — casa de temporada mais nova e premium, piscina privativa, churrasqueira, garagem, privacidade, até 6 pessoas, a poucos passos da praia.

**O que este mapa NÃO é:** não é o mapa do MANECO (projeto autoral de Renildo), não é mapa de vida pessoal ou financeira fora da Villa Arágua, e não é uma arquitetura geral de IA além do que apoia gestão, operação, marketing, atendimento, vendas e financeiro da Villa Arágua. O MANECO só aparece aqui quando estritamente necessário como contexto secundário (por exemplo, na regra financeira das cinco caixas, seção 9, onde ele precisa existir como caixa separada para não contaminar o resultado da Villa Arágua) — nunca como assunto principal.

---

## 3. O que a Villa Arágua IA sabe e apoia (visão executiva)

A Villa Arágua IA já apoia, hoje, sete frentes:

1. **Atendimento a hóspedes e interessados** — via Recepcionista IA em modo rascunho assistido (seção 5).
2. **Comercial e reservas** — qualificação de lead, orçamento, follow-up, sem nunca confirmar preço/disponibilidade sozinha.
3. **Operação da estadia** — check-in/check-out, regras da casa, Wi-Fi, piscina, churrasqueira, manutenção simples.
4. **Marketing e Meta Ads** — campanhas, criativos, textos, públicos, calendário comercial (seção 10).
5. **Precificação e calendário comercial** — sazonalidade, concorrência, ocupação, feriados.
6. **Financeiro** — leitura separada em cinco caixas, nunca um "lucro/prejuízo da pousada" único (seção 9).
7. **Governança, aprendizado e risco** — consolidar erros e casos especiais em melhoria de template; identificar e conter casos que precisam de humano.

A base de conhecimento por trás disso é grande — `CLAUDE.md` já mapeia as pastas de origem (`ACOMODACOES/`, `OPERACAO/`, `BASE DE CONHECIMENTO/`, `MARKETING E VENDAS/`, `RECEPCIONISTA IA/`, `REVENUE MANAGER/`, `CONCORRENTES/`, `BOMBINHAS/`, `FINANCEIRO/`, `DNA VILLA ARAGUA/`, etc.). O inventário completo de arquivos processados está na seção 14 (resumo) e, com todo o detalhe histórico, no Anexo A.

---

## 4. Vocabulário de status (classificação oficial)

A partir desta reorganização, todo agente, módulo, skill ou capacidade mencionado neste mapa deve usar um destes rótulos — nunca uma descrição vaga que deixe parecer que algo candidato já está funcionando:

| Status | Significado |
|---|---|
| **Existente** | Arquivo real (`.claude/agents/*.md` ou `.claude/skills/*/SKILL.md`) já criado, com regras e fluxo definidos. Pode ser invocado hoje no Claude Code. |
| **Em piloto** | Existente, e já em uso real controlado (mensagens/leads reais, com humano revisando cada saída antes de agir). |
| **Em formalização** | O comportamento já existe na prática (embutido em outro agente/skill, ou seguido manualmente), mas ainda não tem arquivo próprio dedicado. |
| **Candidato futuro** | Ideia com função, entradas e limites já pensados, mas **nenhum arquivo criado**. |
| **Hipótese** | Ainda menos maduro que candidato — mencionado uma vez, sem desenho completo. |
| **Não criado** | Foi avaliado e decidido explicitamente que ainda não deve ser criado (normalmente por falta de uso real que justifique). |
| **Descartado** | Foi avaliado e rejeitado — não deve ser recriado sem nova decisão explícita de Renildo. |
| **Bloqueado por segurança** | Existe como conceito, mas está proibido de operar (ex.: qualquer envio automático de WhatsApp, qualquer API/Zapier/Make conectado). |

---

## 5. Recepcionista IA — modo rascunho assistido (nunca autônoma)

> A Recepcionista IA está em **modo rascunho assistido**. Ela não envia mensagem sozinha.

Fluxo obrigatório, sempre nesta ordem:

1. hóspede ou lead escreve (WhatsApp, Instagram, Booking, Airbnb ou outro canal);
2. humano (Rene, Nubia ou Renildo) copia ou resume a mensagem;
3. humano cola a mensagem na IA;
4. IA classifica o caso (Operacional N1–N4, Comercial C1–C4, ou Lacuna);
5. IA sugere um rascunho de resposta;
6. humano revisa o rascunho;
7. humano ajusta se necessário;
8. humano envia manualmente pelo canal real.

A IA nunca pula um passo desse fluxo. Ela nunca envia WhatsApp automaticamente, nunca confirma reserva, nunca confirma disponibilidade, nunca decide preço, desconto ou reembolso.

**Estado real em 13/08/2026:** este fluxo está em **uso real diário**, não só em piloto teórico — leads reais chegam pelo CRM (`CRM_LEADS_VILLA_ARAGUA.md`), a IA gera o rascunho e a linha de registro, e nada é marcado como enviado até o humano confirmar explicitamente que enviou (protocolo "ENVIADO [nome] HH:MM"). Isso é o Modo Rascunho Assistido funcionando como desenhado, não uma exceção a ele.

---

## 6. Agentes e módulos da Villa Arágua IA

| Agente / Módulo | Status | Função | Pode fazer | Não pode fazer | Humano responsável |
|---|---|---|---|---|---|
| **1. Recepcionista IA / Atendimento Assistido** (`villa-recepcionista-rascunho`, `villa-orquestrador-triagem`) | Em piloto (uso real diário) | Classificar mensagem de hóspede/lead e sugerir rascunho de resposta | Classificar N1–N4/C1–C4, consultar bibliotecas, sugerir rascunho | Enviar mensagem, confirmar reserva/disponibilidade/preço | Rene (1ª linha) / Nubia (substituta) / Renildo (casos sensíveis) |
| **2. Comercial / Reservas** (`villa-comercial-reservas`) | Existente | Apoiar orçamento, dúvida de disponibilidade, follow-up e conversão | Diagnosticar perfil, indicar acomodação, redigir orçamento com valor já aprovado | Confirmar preço final ou disponibilidade sem validação humana; conceder desconto | Rene / Nubia (C1–C2) · Renildo (C3–C4) |
| **3. Operacional / Estadia** (`villa-operacional-estadia`) | Existente | Apoiar dúvidas durante a hospedagem: regras, check-in/out, piscina, estacionamento, churrasqueira, Wi-Fi, ar-condicionado, energia, manutenção simples | Responder com base na Biblioteca Oficial (N1–N2) | Autorizar exceção de regra da casa; resolver N3/N4 sozinho | Rene / Nubia (N1–N2) · Renildo (N3–N4) |
| **4. Marketing & Meta Ads IA** (`villa-marketing-meta-ads`) | Existente — campanhas reais em curso (ver seção 10) | Apoiar campanhas, criativos, textos, públicos, calendário comercial, análise de anúncios | Montar rascunho de campanha, aplicar checklist pré-publicação, analisar métrica real | Subir campanha sozinha, alterar orçamento, prometer resultado, decidir preço | Renildo (decisão de publicar/pausar/investir) |
| **5. Precificação / Calendário Comercial** (`villa-precificacao-calendario`) | Existente | Apoiar análise de sazonalidade, concorrência, ocupação, feriados e estratégia de preço | Levantar dado de mercado, montar leitura competitiva, sugerir faixa | Decidir preço final sozinho | Renildo |
| **6. Financeiro / Painel de Decisão** (`villa-rotina-gestao-operacional` + `villa-financial-five-boxes-classifier`) | Existente | Apoiar leitura de entradas, saídas, custos, reservas futuras, caixa, separação das cinco caixas financeiras | Classificar lançamento por caixa, montar painel mensal | Decidir uso do resultado; misturar as cinco caixas num número só | Renildo |
| **7. Gerente Geral / Rotina Operacional** (`villa-rotina-gestao-operacional`) | Em piloto (uso real diário) | Rodar rotina diária/semanal/mensal: reservas, check-in/out, leads pendentes, campanhas, financeiro, prioridades | Consolidar status de outros agentes/arquivos, preparar resumo de decisão | Decidir sozinho qualquer item que dependa de Renildo | Renildo (decide a partir do resumo) |
| **8. Operação Semi-Autônoma** (parcialmente coberta por `villa-operacional-estadia`) | Em formalização — ver seção 11 | Apoiar checklists, mensagens padrão, lock box, check-in autônomo, rotinas de limpeza/manutenção | O que já está documentado em `GUIA_CHECKIN_AUTONOMO.md` e na Biblioteca Oficial | Qualquer automação real de acesso físico ou eletrônico | Rene / Nubia / Renildo |
| **9. Governança & Aprendizado IA** (`villa-aprendizado-manual`) | Existente | Consolidar aprendizados dos atendimentos, erros, casos especiais e melhorias futuras de template | Sugerir novo template/regra a partir de registro real | Aprovar/persistir novo template sozinho | Renildo (aprova biblioteca) |
| **10. Experiência / Tom de Voz** (`villa-experiencia-tom`, skill `villa-aragua-humanizer-pt-br`) | Existente | Revisar mensagens para manter tom acolhedor, humano, claro e comercial sem pressão | Ajustar forma de um rascunho já correto em conteúdo | Mudar o conteúdo/dado da resposta | Rene / Nubia / Renildo (revisão final) |
| **11. Risco / Escalação** (`villa-risco-escalacao`) | Existente | Identificar casos que precisam de humano: conflito, reclamação grave, exceção, reembolso, desconto, urgência, risco jurídico/reputacional | Classificar risco, garantir que o alerta chegue ao humano certo | Resolver o conflito sozinho | Renildo (sempre, em caso de risco) |

**Nota sobre `video-factory-ia`:** existe como arquivo separado (`.claude/agents/video-factory-ia.md`), mas é um **branch**, não faz parte da árvore de atendimento ao hóspede/lead acima — faz só o handoff estratégico para produção de vídeo em outro repositório (`my-video`). Não deve ser confundido com os 11 módulos da tabela.

**Candidatos futuros / hipóteses, ainda sem arquivo:**

| Nome | Status | Por que ainda não existe |
|---|---|---|
| `villa-governanca-meta-business` (agente) | Candidato futuro | A skill `meta-business-security-audit` já cobre a função de relatório; agente próprio avaliado como prematuro |
| Biblioteca de Turismo/Concierge formal | Candidato futuro | `ROTEIROS_SUGERIDOS_BOMBINHAS.md` é a matéria-prima, ainda não virou biblioteca testada |
| `villa-ops-checklist-builder` | Não criado | Avaliado e considerado prematuro/redundante (decisão de 2026-07-29) |
| `villa-data-quality-checker` | Não criado | Só será reavaliado se houver padrão real e documentado de dado contraditório entre arquivos |
| Concierge digital para hóspedes | Hipótese | Só depois de processos testados em volume real |
| Integração real com WhatsApp | Bloqueado por segurança | Proibido até volume testado e aprovação explícita de Renildo |

---

## 7. Pousada Arágua x Casa Arágua Mariscal — separação obrigatória

A IA **nunca mistura** os dois produtos em texto comercial, atendimento ou análise de campanha. Antes de escrever ou analisar qualquer coisa, ela identifica primeiro qual produto está em jogo.

**Pousada Arágua vende:**
- acolhimento e charme;
- café da manhã na suíte;
- piscina;
- proximidade da Praia de Mariscal;
- clima familiar;
- experiência leve, pousada pequena e afetiva.

**Casa Arágua Mariscal vende:**
- casa completa;
- piscina privativa;
- churrasqueira;
- privacidade;
- garagem;
- conforto e liberdade;
- experiência mais premium;
- praia a poucos passos.

Regra prática: qualquer campanha, orçamento, criativo ou rascunho de atendimento declara logo no início qual dos dois produtos está tratando. Se a mensagem do lead for ambígua entre os dois, a primeira pergunta da IA é justamente essa.

---

## 8. Regras máximas da Villa Arágua IA

Nenhum agente, skill, humano ou IA pode violar:

1. A IA nunca envia mensagem sozinha.
2. A IA nunca confirma reserva sem validação humana.
3. A IA nunca decide preço final sozinha.
4. A IA nunca concede desconto sozinha.
5. A IA nunca autoriza reembolso sozinha.
6. A IA nunca promete disponibilidade sem confirmação humana ou fonte oficial.
7. A IA nunca inventa comodidade, distância, regra, valor ou condição.
8. A IA nunca mistura Pousada Arágua com Casa Arágua.
9. A IA nunca trata hipótese como regra oficial.
10. A IA nunca altera campanhas de Meta Ads automaticamente.
11. A IA nunca aumenta orçamento de campanha sozinha.
12. A IA nunca muda política comercial sem Renildo.
13. A IA sempre sinaliza quando uma decisão precisa de Renildo.
14. A IA sempre separa operação, marketing, financeiro e experiência do hóspede.
15. A IA deve preservar o tom humano, acolhedor e claro da Villa Arágua.

Estas 15 regras são o resumo executivo. O detalhamento fino por biblioteca (ex.: regra-mãe 17 de não citar valor, exceção do café da Casa Arágua, regra dos 3 minutos para retaguarda de N4) continua valendo e está preservado no Anexo A, seções 6 e 7 originais.

---

## 9. Financeiro — as cinco caixas

Qualquer análise financeira da Villa Arágua IA separa cinco caixas — nunca trata tudo como um único "lucro ou prejuízo da pousada":

1. **Resultado operacional da Villa Arágua** — Pousada Arágua + Casa Arágua Mariscal.
2. **Renda patrimonial** — imóveis, aluguéis, Casa Mar, apartamentos e outras rendas patrimoniais.
3. **Família / vida pessoal** — retiradas, escola, alimentação, saúde, lazer e despesas familiares.
4. **MANECO / investimento de futuro** — caixa separada, nunca misturada com o resultado da Villa Arágua.
5. **Saldo geral da travessia** — visão final de sustentabilidade do conjunto, só depois das quatro caixas acima estarem separadas.

**Regra central:**

> Nunca chamar tudo de lucro ou prejuízo da pousada. Primeiro analisar o resultado real da Villa Arágua (caixa 1), isolado das demais. Só depois analisar o saldo geral (caixa 5) — nunca o inverso, nunca partir do saldo geral para "descobrir" o resultado da pousada por dedução.

**Limitação conhecida:** os ledgers de `FINANCEIRO/` são simples (Data/Nome/Débito), sem categorização por caixa — a classificação em cinco caixas precisa ser feita manualmente a cada lançamento (`villa-financial-five-boxes-classifier` apoia isso, mas marca "ambíguo — decisão humana" quando não houver clareza).

---

## 10. Marketing & Meta Ads IA

Este módulo (`villa-marketing-meta-ads`) apoia Renildo em:

- planejamento de campanhas, separando sempre Pousada x Casa;
- textos de anúncios, públicos e criativos;
- promessas comerciais e CTAs;
- sazonalidade e calendário comercial;
- análise de custo por conversa e conversão em reserva;
- follow-up no WhatsApp e remarketing;
- campanhas de alta, média e baixa temporada.

**Limites — o que este módulo nunca faz:**
- não sobe campanha sozinho;
- não altera orçamento sozinho;
- não promete resultado;
- não decide preço;
- não cria oferta sem validação humana;
- não mistura produto, público e promessa.

**Estado real em 13/08/2026:** as campanhas do feriado de 7 de Setembro (`SET 26 QUENTE CWB SC` e `SET 26 FRIO CWB SC`) estavam com lançamento previsto para 05/08/2026. O CRM de leads (`CRM_LEADS_VILLA_ARAGUA.md`) já registra, a partir de 11/08/2026, diversos leads reais chegando via WhatsApp com atribuição a "Meta Ads 7SET" / público de Curitiba — ou seja, **há evidência de campanha real gerando lead real**, ainda que este mapa não tenha recebido uma auditoria formal de status de campanha desde 06/08/2026 (seção 15.2 do Anexo A). Recomenda-se confirmar com Renildo o status oficial de publicação antes de tratar isso como fato fechado neste mapa — sinalizado aqui para não deixar a informação desatualizada, sem forçar uma conclusão que ainda não foi auditada via Meta Ads conectado.

A rotina completa de lançamento (6 fases: estratégia → montagem → auditoria pré-publicação → publicação → auditoria pós-publicação → monitoramento 24h/48h/72h/7 dias) e os critérios de manter/pausar/aumentar verba estão preservados, sem alteração de conteúdo, no Anexo A (seção 15 original).

---

## 11. Operação Semi-Autônoma IA

Este módulo apoia:

- check-in e check-out;
- lock box e porteiro eletrônico;
- mensagens automáticas e respostas rápidas (sempre em modo rascunho, nunca envio automático);
- instruções de chegada;
- regras da Pousada e da Casa Arágua;
- limpeza e manutenção;
- piscina, enxoval, café da manhã, churrasqueira, estacionamento;
- emergências;
- rotina diária, semanal e mensal.

> Operação semi-autônoma não significa pousada fria. Significa menos improviso para Renildo, mais clareza para o hóspede e mais padrão para a operação.

**Status honesto:** hoje este módulo não tem um agente próprio dedicado — a função vive dentro de `villa-operacional-estadia` (dúvidas durante a estadia) e de arquivos de apoio como `GUIA_CHECKIN_AUTONOMO.md` e a Biblioteca Oficial. Classificado como **Em formalização** (seção 6) até que exista justificativa de uso real para separá-lo em agente próprio.

---

## 12. Fluxos principais

### Fluxo 1 — Atendimento de interessado
1. interessado chama (WhatsApp, Instagram, Booking, Airbnb);
2. humano cola a mensagem na IA;
3. IA identifica produto: Pousada ou Casa;
4. IA identifica intenção: dúvida, orçamento, data, preço, disponibilidade;
5. IA sugere resposta;
6. humano revisa;
7. humano envia;
8. caso relevante vira aprendizado (`villa-aprendizado-manual`).

### Fluxo 2 — Hóspede em estadia
1. hóspede relata dúvida ou problema;
2. humano cola a mensagem na IA;
3. IA classifica urgência (N1–N4);
4. IA consulta regras e protocolos (Biblioteca Oficial);
5. IA sugere resposta;
6. se for risco, conflito ou exceção, escala para Renildo (`villa-risco-escalacao`);
7. humano envia;
8. caso relevante vira registro.

### Fluxo 3 — Campanha de Meta Ads
1. Renildo define objetivo;
2. IA ajuda a separar produto (Pousada x Casa);
3. IA sugere campanha, público, criativo e texto;
4. Renildo valida;
5. humano sobe a campanha;
6. Renildo/equipe coletam resultados;
7. IA analisa métricas (`villa-aragua-campaign-analytics`, `campaign-learning-register`);
8. IA sugere melhorias — nunca aplica sozinha.

### Fluxo 4 — Rotina mensal
1. Renildo informa entradas e saídas;
2. IA separa nas cinco caixas (seção 9);
3. IA analisa a operação real da Villa Arágua (caixa 1);
4. IA analisa renda patrimonial (caixa 2);
5. IA analisa família (caixa 3);
6. IA analisa MANECO separado (caixa 4);
7. IA mostra o saldo geral (caixa 5);
8. IA recomenda prioridade do próximo mês — Renildo decide.

---

## 13. Próximos passos recomendados

### Curto prazo
- Confirmar com Renildo o status oficial de publicação das campanhas SET 26 (seção 10) e atualizar este mapa com o resultado da auditoria via Meta Ads conectado.
- Revisar e testar os 11 agentes reais em volume real de uso (lacuna mais antiga do projeto — ver Anexo A, seção 11 original).
- Formalizar a Operação Semi-Autônoma como módulo próprio, se o volume de uso justificar (seção 11).
- Manter a separação clara entre agentes reais e candidatos sempre que este mapa for atualizado (seção 4 e 6).

### Médio prazo
- Consolidar templates de atendimento e biblioteca de respostas rápidas a partir dos casos reais já processados no CRM.
- Rodar a rotina mensal de painel financeiro (`PAINEL_DECISAO_ROTINA_VILLA_ARAGUA.md`) em pelo menos um ciclo completo real.
- Estruturar checklists operacionais nascidos de uso real (não de uma skill geradora genérica).
- Organizar formalmente os aprendizados dos atendimentos já registrados em `villa-aprendizado-manual`.

### Futuro
- Avaliar concierge digital para hóspedes (Turismo/Concierge) — só depois de a biblioteca de turismo existir e ser testada.
- Avaliar automações reais somente depois de processos testados em volume.
- Avaliar integração com WhatsApp somente quando houver segurança e aprovação explícita de Renildo.
- Avaliar apoio operacional/gerencial adicional com base em custo, tempo liberado para Renildo e risco reduzido.

---

## 14. Inventário de arquivos-fonte (referência rápida)

O inventário completo, com todas as tabelas por categoria (núcleo do cérebro, testes, fechamentos/pendências, auditorias, legal, marketing/Meta Ads, automação futura, configuração), está preservado sem alteração no **Anexo A, seção 3 original**. Resumo rápido de onde procurar:

| Categoria | Onde está |
|---|---|
| Dados oficiais validados | `DADOS_OFICIAIS_ATENDIMENTO_VILLA_ARAGUA.md` |
| Bibliotecas de resposta (Operacional N1–N4, Comercial C1–C4/PC-EXT) | `BIBLIOTECA_OFICIAL_RECEPCIONISTA_IA_VILLA_ARAGUA.md`, `BIBLIOTECA_COMERCIAL_RECEPCIONISTA_IA_VILLA_ARAGUA.md` |
| Protocolos de uso | `MODO_RASCUNHO_ASSISTIDO_VILLA_ARAGUA.md`, `PROTOCOLO_USO_DIARIO_RASCUNHO_ASSISTIDO_VILLA_ARAGUA.md` |
| CRM de leads | `CRM_LEADS_VILLA_ARAGUA.md` |
| Painel de decisão da rotina | `PAINEL_DECISAO_ROTINA_VILLA_ARAGUA.md` |
| Definição canônica de C1–C4 | `ARQUITETURA_DO_SISTEMA_COMERCIAL_VILLA_ARAGUA.md`, seção 5 |
| Marketing / Meta Ads | pasta raiz, arquivos `*META_ADS*`, ver Anexo A seção 3.F e 15 |
| Testes e validação | Anexo A, seção 3.B e 9 |
| Legal / privacidade (não publicado) | Anexo A, seção 3.E |
| Configuração do projeto | `CLAUDE.md` |

**Não alterar sem autorização explícita de Renildo:** as duas bibliotecas de resposta, os dois protocolos de uso, `DADOS_OFICIAIS_ATENDIMENTO_VILLA_ARAGUA.md`, e nenhum dos scripts de teste (`teste_regressao_biblioteca.py`, `teste_regressao_biblioteca_comercial.py`).

---

## 15. Regras de escalação humana

### Rene
Primeira linha. Recebe: dúvidas operacionais simples (N1/N2); respostas comerciais simples (C1/C2); pedidos de informação/foto; triagem inicial de qualquer mensagem; rascunhos de contenção (N3/C3, que ele encaminha, não resolve sozinho); problemas de limpeza e manutenção de rotina.

### Nubia
Substituta de Rene, mesmas travas e mesmo escopo.

### Renildo
Decisão sensível, sempre. Recebe: preço e desconto; reembolso; reclamação com risco de avaliação negativa; conflito ou hóspede irritado sem solução simples; alta temporada / decisões de Casa Arágua fora do padrão; exceções de qualquer tipo; negociação sensível ou comparação de preço com concorrente; decisão comercial ou financeira; ajuste/aprovação de novos templates; retaguarda de N4 se ninguém assumir em até 3 minutos.

---

## 16. Changelog desta reorganização (2026-08-13)

- Reescrita a estrutura do início do arquivo (seções 1 a 15) seguindo o pedido explícito de revisão: separação clara "existente x candidato" (vocabulário de status, seção 4), Recepcionista IA descrita explicitamente como rascunho assistido (seção 5), tabela única de agentes/módulos com Pode/Não pode/Humano responsável (seção 6), separação obrigatória Pousada x Casa (seção 7), regras máximas na lista de 15 itens pedida (seção 8), financeiro em cinco caixas (seção 9), seção dedicada de Marketing & Meta Ads IA (seção 10), seção dedicada de Operação Semi-Autônoma (seção 11), 4 fluxos principais (seção 12), próximos passos em curto/médio/futuro (seção 13).
- Corrigido escopo: o mapa agora declara explicitamente, logo na seção 2, que fala só da Villa Arágua (Pousada + Casa), e que MANECO só entra como contexto secundário quando estritamente necessário (regra financeira das cinco caixas).
- Atualizada a contagem real de skills: 16 arquivos reais em `.claude/skills/` hoje (12 originais + `meta-business-security-audit`, `campaign-preflight-checklist`, `campaign-learning-register`, `villa-financial-five-boxes-classifier`, todas criadas em 2026-07-29 conforme Anexo A) — a menção antiga de "12 skills formais" era o valor histórico do momento em que a seção 5 original foi escrita.
- Atualizada a contagem real de agentes: 10 agentes na árvore de atendimento + 1 branch (`video-factory-ia`) = 11 arquivos em `.claude/agents/`.
- Sinalizado em Marketing & Meta Ads (seção 10) que o CRM de leads já mostra evidência de campanha real gerando lead real a partir de 11/08/2026, mas que isso ainda não foi confirmado por auditoria formal via Meta Ads conectado neste mapa — recomendado como próximo passo de curto prazo (seção 13), não afirmado como fato fechado.
- Sinalizado em Recepcionista IA (seção 5) que o modo rascunho assistido está em uso real diário em 13/08/2026, com o protocolo "ENVIADO [nome] HH:MM" como gatilho de confirmação humana antes de qualquer atualização de CRM — sem citar nome de hóspede/lead real neste mapa, conforme regra de conteúdo sensível (Anexo A, seção 14 original).
- **Nada foi apagado.** Todo o conteúdo original (seções 2 a 23 do arquivo anterior a esta reorganização — estado do projeto, inventário completo de arquivos, bibliotecas, skills, protocolos, testes, regras de escalação detalhadas, fluxo de uso manual, lacunas, agentes candidatos históricos, observações para outra IA, conteúdo sensível a evitar, aprendizado completo de Meta Ads SET 26, rotinas reais 17.1–17.8, riscos da arquitetura, plano de evolução em 4 fases, e os changelogs de 2026-07-29 a 2026-08-06) está preservado, sem edição de conteúdo, no **Anexo A** abaixo.
- Backup do arquivo completo, como estava antes desta reorganização, criado em `BACKUP_ANTES_REORGANIZACAO_MAPA_CEREBRO_2026-08-13/MAPA_DO_CEREBRO_IA_VILLA_ARAGUA.md`.

---

---

# ANEXO A — Histórico completo preservado (conteúdo íntegro anterior a 2026-08-13)

*A numeração de seções abaixo é a numeração ORIGINAL do arquivo antes desta reorganização (começa em "2." porque a seção "1. Objetivo deste arquivo" original foi substituída pela nova seção 1 acima — o conteúdo de ambas é equivalente em espírito, mas a versão nova é a vigente). Nada neste anexo foi reescrito ou resumido — é o registro histórico completo, preservado por decisão explícita de não apagar nada.*

## 2. Estado atual do projeto

- Biblioteca Operacional persistida e testada — `BIBLIOTECA_OFICIAL_RECEPCIONISTA_IA_VILLA_ARAGUA.md`. **Atualização 2026-08-05 (ver seção 21): após os Lotes 1 a 11 da série "WhatsApp Rápido", a biblioteca cresceu para 10 N1 + 16 N2 + 24 N3 + 5 N4, além de 4 regras transversais e 2 alertas internos — a contagem "25 templates (N1–N4)" abaixo é o valor histórico da Rodada 4 e não reflete mais o estado atual.**
- Biblioteca Comercial persistida e testada — `BIBLIOTECA_COMERCIAL_RECEPCIONISTA_IA_VILLA_ARAGUA.md`. **Atualização 2026-08-05 (ver seção 21): hoje com 35 códigos `PC-EXT` (sequência 01-23, 26-29, 31-38) — a contagem "21 templates (C1–C4)" abaixo é o valor histórico da Rodada 4.**
- Modo Rascunho Assistido persistido — `MODO_RASCUNHO_ASSISTIDO_VILLA_ARAGUA.md` (inalterado desde a criação original).
- Protocolo de Uso Diário persistido — `PROTOCOLO_USO_DIARIO_RASCUNHO_ASSISTIDO_VILLA_ARAGUA.md`. **Atualizado em 2026-08-05 (Lote 11) — ver seção 21.**
- Diário de Bordo do Piloto criado — `DIARIO_BORDO_PILOTO_RECEPCIONISTA_IA_VILLA_ARAGUA.md` (novo, Lote 11) — ver seção 21.
- Teste operacional aprovado — `teste_regressao_biblioteca.py`, 15/15 checagens, exit code 0.
- Teste comercial aprovado — `teste_regressao_biblioteca_comercial.py`, 19/19 checagens, exit code 0.
- WhatsApp real: **bloqueado**.
- Zapier: **bloqueado**.
- Make: **bloqueado**.
- API/backend: **bloqueados**.
- IA funcionando apenas como rascunho assistido — nenhuma decisão, nenhum envio automático.
- Piloto manual supervisionado (Tema 4.26) **pausado temporariamente** após o Registro 16, fora desta conversa, com registro em tabela simples. Detalhes em 2.1. **Superado em 2026-08-05: após a série "WhatsApp Rápido" (Lotes 1 a 11), a Recepcionista IA está com biblioteca validada, teste cego aprovado e rotina operacional documentada — pronta para o início de um novo piloto diário assistido de 2 semanas. Ver seção 21.**
- Arquitetura dos agentes **concluída e implementada** — 9 agentes + 1 branch (`video-factory-ia`) existem como arquivos reais em `.claude/agents/`, conectados às 12 skills de `.claude/skills/` (valor histórico — hoje são 11 agentes/16 skills, ver seção 6 do corpo novo). Detalhes em 2.2.
- Nenhum agente está conectado a canal real — todos seguem sendo arquivos de instrução para uso manual dentro do Claude Code, em Modo Rascunho Assistido.

### 2.1 — Fase encerrada/pausada: Piloto manual da Recepcionista IA

**Status:**

- Registros 06 a 16 concluídos e fechados.
- Piloto de mensagens reais/simuladas pausado temporariamente.
- Próxima fase: desenho arquitetural dos agentes da Villa Arágua, começando pelo Marketing & Meta Ads IA.

**Principais entregas concluídas:**

1. **GD-01 — Acessibilidade e mobilidade**
   - Status: concluída, testada e validada.
   - Resultado: correção da comunicação sobre escadas, degraus externos, rampa da Casa, ausência de barras de apoio e cuidado para não apresentar Pousada/Casa como adaptadas.
2. **DC-02 — Configuração de camas e acomodação da Casa Arágua**
   - Status: concluída, testada e validada.
   - Resultado: documentada a configuração da Casa Arágua — suíte no piso superior com cama queen; quarto no primeiro piso com cama queen; sofá em L na sala para acomodação; capacidade máxima mantida em até 6 pessoas; proibição de inventar cama auxiliar, colchão extra, beliche ou sofá-cama formal.
3. **DC-03 — Piscina da Pousada Arágua não aquecida**
   - Status: concluída, testada e validada.
   - Resultado: item 35 complementado para registrar que a piscina da Pousada Arágua não é aquecida, sem promessa de temperatura da água ou conforto térmico.

**Registros concluídos nesta etapa:**

- Registro 06 — Alta temporada, duas famílias, turismo e restaurante.
- Registro 07 — Piscina, suítes próximas da piscina e piscina não aquecida.
- Registro 08 — Comparação Acqua, Wood e Fuego.
- Registro 09 — Família com crianças, Pousada x Casa.
- Registro 10 — Praia, cadeiras, restaurantes, mercado e roteiro sem carro.
- Registro 11 — Objeção de preço, desconto e cancelamento.
- Registro 12 — Feriado 7 de Setembro, pet, Wi-Fi, estacionamento e early check-in.
- Registro 13 — Mobilidade reduzida.
- Registro 14 — Check-in tardio, Navegantes, entrada independente e transfer.
- Registro 15 — Casa Arágua para 6 amigos, camas, visitantes, piscina/churrasqueira e silêncio.
- Registro 16 — Lead do Instagram, fotos atuais, piscina aquecida, vista e confiança.

**Aprendizados principais:**

- Leads perguntam muito sobre detalhes concretos antes de reservar.
- Fotos, camas, piscina, café, localização, estacionamento e regras influenciam conversão.
- Objeções de confiança exigem transparência.
- Preço deve ser defendido por valor percebido, não por desconto automático.
- Instagram gera desejo visual, mas também exige cuidado com promessas.
- Marketing e atendimento precisam estar alinhados para não criar overpromise.
- Pousada Arágua e Casa Arágua precisam de comunicação separada.
- A Governança & Aprendizado IA será importante para evitar: subutilização de dados já documentados; invenção de detalhes plausíveis, mas não documentados.

### 2.2 — Fase concluída: Arquitetura dos Agentes internos

**Status (2026-07-24):** a fase antes descrita como "próxima" foi concluída. A arquitetura conceitual de `DEFINICAO_AGENTES_VILLA_ARAGUA_IA.md` (v1, 7 agentes) e `MATRIZ_ROTEAMENTO_AGENTES_VILLA_ARAGUA.md` virou 9 arquivos reais em `.claude/agents/`, todos com regras máximas, fluxo obrigatório e formato de saída embutidos no próprio arquivo:

- `villa-orquestrador-triagem.md` — triagem/roteamento, porta de entrada padrão.
- `villa-recepcionista-rascunho.md` — hub de rascunho assistido de ponta a ponta (classificação + risco + rascunho em um passe).
- `villa-comercial-reservas.md` — Comercial/Reservas (C1–C4).
- `villa-operacional-estadia.md` — Operacional/Estadia (N1–N4).
- `villa-risco-escalacao.md` — Risco/Escalação.
- `villa-experiencia-tom.md` — Experiência/Tom.
- `villa-precificacao-calendario.md` — corresponde ao "Agente de Apoio à Decisão Comercial" da v1 conceitual.
- `villa-marketing-meta-ads.md` — Marketing & Meta Ads IA (entrega a auditoria arquitetural que esta seção previa).
- `villa-aprendizado-manual.md` — Aprendizado Manual.

Um décimo arquivo, `video-factory-ia.md` (adicionado 2026-07-24), existe como **branch separado**: faz apenas o handoff estratégico para a produção técnica de vídeo, que roda em outro repositório (`my-video`) — não faz parte da árvore de atendimento ao hóspede/lead acima e não deve ser confundido com ela.

Uma visão executiva e visual de toda essa arquitetura (fluxo, regras máximas, hierarquia de fontes, os 9+1 agentes, as 12 skills (valor histórico — hoje são 11 agentes/16 skills, ver seção 6 do corpo novo), base de conhecimento e a porta de saída humana) foi publicada como artifact em 2026-07-24 — "Mapa do Cérebro — Villa Arágua IA".

**O que isto NÃO significa:** os agentes continuam sendo arquivos de instrução para uso manual dentro do Modo Rascunho Assistido. Nenhum está conectado a WhatsApp, Zapier, Make ou qualquer API real. "Implementado" aqui quer dizer "arquivo `.md` pronto para ser invocado no Claude Code", não "automação ativa" — as regras máximas da seção 7 continuam valendo integralmente.

**Itens da auditoria original — status:**

1. Papel exato de cada agente — definido, ver seção 12 e os próprios arquivos.
2. Limites de decisão — definidos em cada arquivo (nenhum sobe/pausa campanha, define preço final, concede desconto etc.).
3–7. Entradas/saídas entre agentes, uso dos aprendizados 06–16, separação Pousada/Casa, separação campanha/criativo/público/oferta — cobertas pela arquitetura, mas ainda **sem validação em volume real de uso**.
8. Riscos de duplicidade — mitigado pela hierarquia de prioridade da seção 13 do `DEFINICAO_AGENTES_VILLA_ARAGUA_IA.md` ("quando houver risco misturado com venda, o risco manda").
9. Documentos consultados — listados na ficha de cada agente (seção 12 abaixo).
10. Testes antes de considerar pronto — **pendente**, é a maior lacuna restante (ver seção 11).

**Próxima fase real:** retomar (ou formalmente encerrar) o piloto manual pausado no Registro 16 (seção 2.1), e testar os 9 agentes recém-implementados (valor histórico — hoje são 11 agentes/16 skills, ver seção 6 do corpo novo) em casos reais/simulados antes de qualquer decisão sobre automação futura.

### 2.3 — Papel definido no CLAUDE.md sem agente correspondente

O papel "Gerente Geral / Virtual" está descrito em `CLAUDE.md` (rotina diária/semanal/mensal, indicadores, pergunta central de sustentação da travessia para o MANECO), mas **não existe como arquivo em `.claude/agents/`**. Nenhum dos 9 agentes atuais cobre rotina de acompanhamento semanal/mensal transversal (valor histórico — hoje são 11 agentes/16 skills, ver seção 6 do corpo novo) — cada um cobre seu domínio (comercial, operacional, risco, marketing, preço, tom, aprendizado).

**Decisão registrada em 2026-07-29:** planejar `villa-rotina-gestao-operacional` como a implementação deste papel. Ele **não decide nada sozinho e não substitui nenhum agente especialista** — sua função é rodar os checklists de rotina (seção 17 abaixo), puxar status de outros agentes/arquivos, e apresentar a Renildo. **Criado como arquivo em `.claude/agents/villa-rotina-gestao-operacional.md` em 2026-07-29** (Fase 2 antecipada, aproveitando janela de tempo de Renildo antes do lançamento SET 26 — ver seção 20). É agente de **rotina e decisão assistida, não agente autônomo**: nunca publica campanha, nunca altera preço, nunca confirma disponibilidade/reserva, nunca concede desconto/reembolso, nunca mexe em acesso ou Business Manager. Ver Plano de Evolução (seção 19).

**Regra obrigatória de leitura financeira deste agente (DNA, seção 13, refinado em cinco caixas):** `villa-rotina-gestao-operacional` nunca deve apresentar os números da Villa Arágua como um "lucro/prejuízo da pousada" único e misturado. Ele deve sempre separar cinco caixas distintas:

1. **Resultado operacional da Villa Arágua** — receita e custo da operação em si (Pousada + Casa).
2. **Renda patrimonial** — o que vem de patrimônio, não da operação diária.
3. **Família / vida pessoal** — despesas e entradas da vida de Renildo, fora da operação.
4. **MANECO / investimento de futuro** — o que está sendo direcionado ou reservado para a travessia estratégica.
5. **Saldo geral da travessia** — a leitura consolidada de tudo isso junto, só depois das quatro caixas acima estarem separadas.

**Ordem obrigatória de leitura:** primeiro a operação real da Villa Arágua (caixa 1), isolada das demais; só depois o saldo geral da vida e da travessia (caixa 5). Nunca o inverso — nunca partir do saldo geral para "descobrir" o resultado da pousada por dedução.

---

## 3. Inventário de arquivos existentes

Além dos arquivos `.md`/`.py` listados abaixo (raiz do projeto), existem dezenas de arquivos-fonte originais (`.docx`, `.xlsx`, `.pdf`, imagens) organizados nas pastas descritas em `CLAUDE.md` (`ACOMODACOES/`, `OPERACAO/`, `BASE DE CONHECIMENTO/`, `MARKETING E VENDAS/`, `RECEPCIONISTA IA/`, `REVENUE MANAGER/`, `CONCORRENTES/`, `BOMBINHAS/`, `FINANCEIRO/`, `DNA VILLA ARAGUA/`, etc.). Eles não são listados individualmente aqui por serem **fonte bruta** — a matéria-prima original —, não parte da arquitetura já processada do cérebro IA. Ver `CLAUDE.md` para o mapa completo de pastas.

### 3.A — Núcleo do cérebro (Recepcionista IA, ativo, Rodada 4)

| Arquivo | Tipo | Função | Status | Quando usar | Quando não usar | Fonte | Agentes prováveis |
|---|---|---|---|---|---|---|---|
| `DADOS_OFICIAIS_ATENDIMENTO_VILLA_ARAGUA.md` | Dados/documentação | Painel de dados de atendimento validados por Renildo | Persistido, validado | Sempre que precisar de um fato confirmado (distância, capacidade, política, valor) | Nunca usar para inventar dado ausente | Principal | Todos |
| `BIBLIOTECA_OFICIAL_RECEPCIONISTA_IA_VILLA_ARAGUA.md` | Biblioteca | 25 templates operacionais (N1–N4) | Persistida e testada (15/15) | Mensagens operacionais pós-reserva (check-in, Wi-Fi, cancelamento, emergência) | Comercial ou turismo | Principal | Operacional, Orquestrador |
| `BIBLIOTECA_COMERCIAL_RECEPCIONISTA_IA_VILLA_ARAGUA.md` | Biblioteca | 21 templates comerciais (C1–C4) | Persistida e testada (19/19) | Mensagens pré-reserva/comerciais (escolha de acomodação, orçamento, desconto) | Nunca para citar valor comercial | Principal | Comercial, Orquestrador |
| `MODO_RASCUNHO_ASSISTIDO_VILLA_ARAGUA.md` | Protocolo | Fluxo humano de uso das bibliotecas | Persistido | Sempre — é o procedimento-mãe de qualquer uso da IA | Não é substituído por nada ainda | Principal | Todos |
| `PROTOCOLO_USO_DIARIO_RASCUNHO_ASSISTIDO_VILLA_ARAGUA.md` | Protocolo | Rotina diária/semanal do piloto, formato de colar mensagem e resposta, registro | Persistido; piloto em andamento (Tema 4.26) | No uso diário real da equipe | — | Principal | Todos |
| `ROTEIRO_RECEPCIONISTA_IA.md` | Roteiro operacional | Regras "quando X → responder Y → escalar Z", pré-Rodada 4 | Persistido (Rodada 1) | Referência de regra operacional detalhada, matéria-prima da Biblioteca Operacional | — | Apoio (predecessor) | Operacional |
| `PROMPT_RECEPCIONISTA_IA_WHATSAPP.md` | Prompt | Dois prompts prontos para uma futura ferramenta de automação | Persistido, **não usado** (automação bloqueada) | Referência de como o agente falaria, se algum dia conectado | Não usar em produção real ainda | Apoio | Orquestrador (referência futura) |
| `PLAYBOOK_ATENDIMENTO_WHATSAPP.md` | Playbook | Tom de voz, fluxo de vendas, indicação de acomodação, objeções | Persistido (Rodada 1) | Referência de tom e fluxo comercial | — | Apoio | Comercial, Experiência |
| `CHECKLIST_ATENDIMENTO_DIARIO.md` | Checklist | Passo a passo diário, complementar ao Playbook | Persistido | Apoio à rotina humana do dia a dia | — | Apoio | Todos |
| `MAPA_DE_USO_DAS_SKILLS_VILLA_ARAGUA.md` | Orquestração | Resume o roteamento das skills do projeto | Persistido | Para decidir qual skill carregar | — | Apoio | Orquestrador |
| `GUIA_DIGITAL_HOSPEDE_VILLA_ARAGUA.md` | Documentação | Guia entregue ao hóspede (base para site/PDF/QR) | Persistido, com `[PREENCHER]` pendente | Referência de conteúdo de jornada do hóspede | Não afirmar campos marcados `[PREENCHER]` | Apoio | Operacional, Experiência |
| `HISTORIA_E_POSICIONAMENTO_VILLA_ARAGUA.md` | Documentação | História e posicionamento institucional/emocional | Persistido | Textos institucionais, tom de marca | — | Apoio | Comercial, Experiência |
| `MAPA_GERAL_DA_VILLA.md` | Índice executivo | Resume os 10 pilares do negócio | Persistido | Orientação executiva rápida | Não substitui `CLAUDE.md` | Apoio | Orquestrador |
| `MIDIAS_E_LINKS_OFICIAIS_VILLA_ARAGUA.md` | Referência | Central de links e mídia oficiais | Persistido, com `[PREENCHER]` pendente | Antes de enviar qualquer link/mídia ao hóspede | Não inventar link não confirmado | Apoio | Operacional, Comercial |
| `GUIA_CHECKIN_AUTONOMO.md` | Guia operacional | Check-in autônomo (lock box, porteiro eletrônico) | Persistido | Dúvidas de acesso/check-in autônomo | — | Apoio | Operacional |
| `ROTEIROS_SUGERIDOS_BOMBINHAS.md` | Curadoria | Praias, gastronomia, passeios, dicas locais | Persistido, com `[PREENCHER]` pendente | Perguntas de turismo/concierge | Ainda é lacuna oficial na Biblioteca Comercial (ver seção 11) | Apoio | Turismo (futuro, ainda não formalizado) |

### 3.B — Testes e validação

| Arquivo | Tipo | Função | Status | Observação |
|---|---|---|---|---|
| `PERGUNTAS_TESTE_RECEPCIONISTA_IA_VILLA_ARAGUA.md` | Teste | Banco de perguntas simuladas (Rodada 1) | Persistido | Só perguntas, sem resposta |
| `ROTEIRO_TESTE_MANUAL_RECEPCIONISTA_IA_VILLA_ARAGUA.md` | Teste | Roteiro de teste manual dentro do Claude | Persistido | Base do formato usado em toda a Rodada 1 |
| `RESULTADO_TESTE_ACESSO_LOCK_BOX_...md` | Teste | Resultado — acesso e lock box | Aprovado (2026-07-10) | Bloco 1/7 |
| `RESULTADO_TESTE_CAFE_DA_MANHA_...md` | Teste | Resultado — café da manhã | Aprovado | — |
| `RESULTADO_TESTE_CANCELAMENTO_CASA_ARAGUA_...md` | Teste | Resultado — cancelamento Casa Arágua | Aprovado (2026-07-10) | Bloco 7/7 |
| `RESULTADO_TESTE_CANCELAMENTO_POUSADA_...md` | Teste | Resultado — cancelamento Pousada | Aprovado (2026-07-10) | Bloco 6/7 |
| `RESULTADO_TESTE_CHECKIN_CHECKOUT_EARLY_LATE_...md` | Teste | Resultado — check-in/checkout, early/late | Aprovado (2026-07-12) | — |
| `RESULTADO_TESTE_CHURRASQUEIRA_...md` | Teste | Resultado — churrasqueira | Aprovado (2026-07-12) | Bloco 3/5 |
| `RESULTADO_TESTE_CRIANCAS_CAPACIDADE_CAMA_EXTRA_...md` | Teste | Resultado — crianças, capacidade, cama extra | Aprovado (2026-07-12) | Bloco 5/5 |
| `RESULTADO_TESTE_DUVIDA_FORA_BASE_...md` | Teste | Resultado — dúvida fora da base documentada | Aprovado (2026-07-10) | Bloco 5/7 |
| `RESULTADO_TESTE_GOLPE_PAGAMENTO_...md` | Teste | Resultado — desconfiança de golpe/pagamento | Aprovado (2026-07-10) | Bloco 2/7 |
| `RESULTADO_TESTE_HOSPEDE_IRRITADO_...md` | Teste | Resultado — hóspede irritado | Aprovado (2026-07-10) | Bloco 4/7 |
| `RESULTADO_TESTE_PEDIDO_DESCONTO_...md` | Teste | Resultado — pedido de desconto | Aprovado (2026-07-10) | Bloco 3/7 |
| `RESULTADO_TESTE_PET_...md` | Teste | Resultado — pet | Aprovado (2026-07-12) | Bloco 4/5 |
| `RESULTADO_TESTE_REGRAS_DA_CASA_ARAGUA_...md` | Teste | Resultado — regras da Casa Arágua | Aprovado (2026-07-10) | — |
| `RESULTADO_TESTE_VISITANTES_FESTAS_SILENCIO_...md` | Teste | Resultado — visitantes/festas/silêncio | Aprovado (2026-07-10) | — |
| `RESULTADO_TESTE_WIFI_CASA_ARAGUA_...md` | Teste | Resultado — Wi-Fi Casa Arágua | Aprovado (2026-07-12) | Bloco 2/5 |
| `PLANO_E_RESULTADOS_RODADA_2_COMERCIAL_CONVERSAO_...md` | Teste | Rodada 2 — teste comercial e conversão | Encerrado (2026-07-13) | — |
| `CHECKLIST_TESTE_ZAP_B_FASE_2_VILLA_ARAGUA.md` | Checklist de teste | Teste do Zap B — aprovação humana + registro em planilha, sem envio livre | Persistido | Nenhuma API paga conectada |
| `REGISTRO_VALIDACAO_ZAP_B_FASE_2_VILLA_ARAGUA.md` | Registro | Resultado de um teste real feito fora desta sessão | Persistido | Registro factual, não criou automação |
| `teste_regressao_biblioteca.py` | Script | Regressão estrutural da Biblioteca Operacional | Aprovado — 15/15, exit 0 | Só lê `.md` e imprime; sem rede, sem escrita |
| `teste_regressao_biblioteca_comercial.py` | Script | Regressão estrutural da Biblioteca Comercial | Aprovado — 19/19, exit 0 | Só lê `.md` e imprime; sem rede, sem escrita |

### 3.C — Fechamentos, pendências e decisões

| Arquivo | Tipo | Função | Status |
|---|---|---|---|
| `FECHAMENTO_RODADA_1_RECEPCIONISTA_IA_VILLA_ARAGUA.md` | Fechamento | Status "Rodada 1 encerrada" | Persistido |
| `CONSOLIDACAO_PENDENCIAS_RODADA_1_5_VILLA_ARAGUA_IA.md` | Pendências | Consolidação da Rodada 1.5 | Persistido |
| `DECISOES_PENDENTES_RENILDO_FECHAMENTO_RODADA_1_VILLA_ARAGUA_IA.md` | Pendências | Backlog operacional pós-Rodada 1 | Persistido |
| `DECISOES_RENILDO_DADOS_OFICIAIS.md` | Decisões | Ficha de validação dos dados oficiais por Renildo | Persistido |
| `PENDENCIAS_CRITICAS_OPERACAO_REAL_VILLA_ARAGUA.md` | Pendências | Pendências críticas da operação real | Persistido |
| `PENDENCIAS_OPERACAO_ESTADIA_VILLA_ARAGUA.md` | Pendências | Pendências da operação da estadia | Persistido |
| `PENDENCIAS_RENILDO_RODADA_1_VILLA_ARAGUA_IA.md` | Pendências | Pendências da Rodada 1 | Persistido |
| `QUESTIONARIO_DECISOES_CRITICAS_RENILDO_RODADA_1_5.md` | Questionário | Decisões críticas da Rodada 1.5 | Persistido |
| `ARQUIVOS_A_CORRIGIR_DADOS_OFICIAIS.md` | Plano de correção | Lista de arquivos-fonte divergentes a corrigir | Persistido |
| `PLANO_CORRECAO_COMPLEMENTAR_DADOS_OFICIAIS.md` | Plano de correção | Pendências pós-correção dos 6 arquivos originais | Persistido |
| `RELATORIO_VALIDACAO_BASE_ATENDIMENTO_FASE_1.md` | Relatório | Validação da Base de Atendimento Fase 1 | Persistido |

### 3.D — Auditorias e relatórios de status

| Arquivo | Tipo | Função | Status |
|---|---|---|---|
| `AUDITORIA_GERAL_CEREBRO_VILLA_ARAGUA_V1.md` | Auditoria | Auditoria geral do cérebro (12 arquivos) | Persistida — é a referência mais atual sobre os relatórios "superados" abaixo |
| `AUDITORIA_OPERACAO_ESTADIA_VILLA_ARAGUA_V1.md` | Auditoria | Auditoria das pendências de operação da estadia | Persistida |
| `AUDITORIA_POS_INTEGRACAO_OPERACAO_ESTADIA_RECEPCIONISTA_IA_V1.md` | Auditoria | Integração das pendências x Recepcionista IA | Persistida |
| `AUDITORIA_FINAL_CHECKIN_AUTONOMO_VILLA_ARAGUA_V1.md` | Auditoria | Check-in autônomo | Persistida |
| `AUDITORIA_FINAL_TERMOS_PRIVACIDADE_VILLA_ARAGUA_V1.md` | Auditoria | Cruzamento Termos/Privacidade/Recepcionista IA | Persistida |
| `AUDITORIA_POLITICA_PRIVACIDADE_SITE_VILLA_ARAGUA_V1.md` | Auditoria | Política de Privacidade x LGPD | Persistida |
| `AUDITORIA_TERMOS_E_CONDICOES_SITE_VILLA_ARAGUA_V1.md` | Auditoria | Termos e Condições x regras oficiais | Persistida |
| `RELATORIO_CHECKIN_AUTONOMO_V1_1.md` | Relatório | Status Check-in Autônomo | Persistido |
| `RELATORIO_FECHAMENTO_TERMOS_PRIVACIDADE_E_RECEPCIONISTA_IA_V1.md` | Relatório | Fechamento Termos/Privacidade | Persistido |
| `RELATORIO_GUIA_DIGITAL_HOSPEDE_V1.md` | Relatório | Status Guia Digital | **Superado** — ler junto com `AUDITORIA_GERAL_CEREBRO_VILLA_ARAGUA_V1.md` |
| `RELATORIO_MIDIAS_E_LINKS_OFICIAIS_VILLA_ARAGUA_V1.md` | Relatório | Status Central de Mídias | **Superado** — idem |
| `RELATORIO_RECEPCIONISTA_IA_WHATSAPP_V1_3.md` | Relatório | Status Recepcionista IA WhatsApp | **Superado** — idem |
| `RELATORIO_ROTEIROS_SUGERIDOS_BOMBINHAS_V1.md` | Relatório | Status Roteiros Bombinhas | **Superado** — idem |

### 3.E — Legal / privacidade (não publicado)

| Arquivo | Tipo | Função | Status |
|---|---|---|---|
| `POLITICA_PRIVACIDADE_SITE_VILLA_ARAGUA_VERSAO_FINAL_REVISAR.md` | Legal | Versão final para revisão | **Não publicada no site** |
| `TERMOS_E_CONDICOES_SITE_VILLA_ARAGUA_VERSAO_FINAL_REVISAR.md` | Legal | Versão final para revisão | **Não publicada no site** |
| `CHECKLIST_VALIDACAO_POLITICA_PRIVACIDADE_VILLA_ARAGUA.md` | Checklist | Pontos a confirmar com Renildo | Persistido |
| `CHECKLIST_VALIDACAO_TERMOS_E_CONDICOES_VILLA_ARAGUA.md` | Checklist | Pontos a confirmar com Renildo | Persistido |

### 3.F — Marketing, vendas e Meta Ads

| Arquivo | Tipo | Função | Status |
|---|---|---|---|
| `AGENTE_IA_MARKETING_VENDAS_META_ADS_VILLA_ARAGUA.md` | Base estratégica | Agente de marketing/vendas/Meta Ads, complementar à Recepcionista IA | Persistido |
| `PLANO_CAMPANHA_REABERTURA_VILLA_ARAGUA_2026.md` | Plano | Campanha de reabertura da Pousada (01/08/2026) | Persistido |
| `CHECKLIST_DECISOES_CAMPANHA_REABERTURA_VILLA_ARAGUA_2026.md` | Checklist | Decisões de Renildo para a campanha | Persistido |
| `ESTRUTURA_CAMPANHA_META_ADS_7_SETEMBRO_VILLA_ARAGUA_2026.md` | Estrutura | Campanha do feriado 7 de setembro | Persistido |
| `MATRIZ_ANUNCIOS_FINAIS_7_SETEMBRO_VILLA_ARAGUA_2026.md` | Matriz | Anúncios finais 7 de setembro | Persistido |
| `COPYS_FINAIS_META_ADS_7_SETEMBRO_VILLA_ARAGUA_2026.md` | Copy | Pronta para colar no Gerenciador de Anúncios | Persistido |
| `SETUP_INICIAL_META_ADS_7_SETEMBRO_VILLA_ARAGUA_2026.md` | Setup | Orçamento R$ 45/dia, primeiro teste real | Persistido |
| `PACOTE_CONFIGURACAO_META_ADS_7_SETEMBRO_VILLA_ARAGUA_2026.md` | Configuração | Lote 1 (5 anúncios) pronto para o Gerenciador | Persistido |
| `MAPA_CELULAS_SET_26_7SET_META_ADS_VILLA_ARAGUA.md` | Mapeamento | Células da planilha Google Sheets de campanha | Persistido |
| `PREENCHIMENTO_ABA_SET_26_7SET_META_ADS_VILLA_ARAGUA.md` | Conteúdo | Preenchimento da aba da planilha | Persistido |
| `CONFIGURACAO_ZAP_CARGA_META_ADS_SET_26_7SET_VILLA_ARAGUA.md` | Documentação | Roteiro de montagem manual de um Zap de carga única | **Histórica/obsoleta — ver `ADENDO_STATUS_CAMPANHA_7_SETEMBRO_2026_OBSOLETA_POS_REVENUE_MANAGER.md`** — nenhum Zap criado/executado a partir dele |
| `PLANO_30_DIAS_VILLA_ARAGUA.md` | Plano executivo | 30 dias / 4 semanas, ligado ao DNA e ao MANECO | Persistido |
| `ADENDO_STATUS_CAMPANHA_7_SETEMBRO_2026_OBSOLETA_POS_REVENUE_MANAGER.md` | Adendo de status/governança | Registra que o primeiro ciclo de campanha Meta Ads do feriado 7 de Setembro 2026 (pacote fechado "R$ 1.997", Casa Arágua incluída, 3 campanhas) está obsoleto pós-Revenue Manager; não apaga o histórico, só documenta a mudança de status | Persistido (2026-07-29) |
| `REVISAO_HUMANA_PUBLICACAO_SET26_META_ADS.md` | Checklist operacional | Revisão humana pré-publicação das campanhas SET 26 (automações, Business Manager, decisão final) + checklist de pré-lançamento + rotina de pós-lançamento para 05/08/2026 | Persistido (2026-07-29) |
| `CRM_LEADS_VILLA_ARAGUA.md` | CRM leve | Registro manual de leads (campos, status padrão, uso semanal por `villa-rotina-gestao-operacional`) — nunca trata conversa/orçamento como reserva | Persistido (2026-07-29); em uso real diário a partir de agosto/2026 |
| `PAINEL_DECISAO_ROTINA_VILLA_ARAGUA.md` | Painel operacional | Estrutura padrão (9 seções) da rotina semanal/mensal de `villa-rotina-gestao-operacional` — resumo, reservas, leads, campanhas, operação, financeiro (cinco caixas), tempo de Renildo, decisões pendentes, próximos passos | Persistido (2026-07-29) |

### 3.G — Automação futura (conceitual, permanece bloqueada)

| Arquivo | Tipo | Função | Status |
|---|---|---|---|
| `ARQUITETURA_FOLLOW_UP_AUTOMATICO_VILLA_ARAGUA.md` | Manual estratégico/conceitual | Desenho futuro de follow-up automático | Conceitual — nenhuma conexão real feita |
| `FASE_1_FOLLOW_UP_MANUAL_ASSISTIDO_VILLA_ARAGUA.md` | Manual operacional | Envio 100% manual, com sugestão de IA | Conceitual/manual — nenhuma automação criada |
| `FASE_2_TEMPLATES_SEMI_AUTOMATICOS_VILLA_ARAGUA.md` | Planejamento | Templates semi-automáticos, fase futura | Conceitual — nenhum Zap montado |
| `PROMPT_OPERACIONAL_AUTOMACAO_WHATSAPP_VILLA_ARAGUA.md` | Manual compacto | Prompt operacional para uma futura automação | Conceitual — não é automação real |

### 3.H — Configuração do projeto

| Arquivo | Tipo | Função | Status |
|---|---|---|---|
| `CLAUDE.md` | Configuração | Instruções do projeto para qualquer IA assistente | Fonte de comportamento — sempre ativo |

---

## 4. Bibliotecas existentes

### 4.1 Biblioteca Operacional

- **Nome exato do arquivo:** `BIBLIOTECA_OFICIAL_RECEPCIONISTA_IA_VILLA_ARAGUA.md`
- **Função:** biblioteca de 25 templates de resposta operacional, organizados por nível de risco (N1–N4), para uso no Modo Rascunho Assistido.
- **Temas cobertos:** localização/distância da praia, Wi-Fi, check-in/check-out, cancelamento (Pousada e Casa), cama extra, regras da casa, visitantes, silêncio, emergência (SAMU/Polícia/Bombeiros), acesso/lock box, café da manhã, churrasqueira, pet, crianças/capacidade.
- **Limites:** nunca promete vista para o mar/frente-mar; nunca inventa dado fora de `DADOS_OFICIAIS_ATENDIMENTO_VILLA_ARAGUA.md`; N3/N4 nunca viram resposta final — sempre contenção + escalonamento.
- **Principais tipos de mensagem que responde:** dúvidas operacionais de hóspede já reservado ou em estadia.
- **Quando escalar para humano:** todo N3 (contenção, encaminha Rene/Nubia) e todo N4 (contenção + alerta de prioridade máxima, regra dos 3 minutos até retaguarda de Renildo).
- **Resultado do teste operacional:** `teste_regressao_biblioteca.py` — 15/15 checagens aprovadas, exit code 0.
- **Observações importantes:** predecessora direta é `ROTEIRO_RECEPCIONISTA_IA.md`; corrigida ao longo da Rodada 4 (distância da Casa Arágua, remoção do link de vídeo de chegada inexistente, ajuste de PC-N1-09).

### 4.2 Biblioteca Comercial

- **Nome exato do arquivo:** `BIBLIOTECA_COMERCIAL_RECEPCIONISTA_IA_VILLA_ARAGUA.md`
- **Função:** biblioteca de 21 templates de resposta comercial, organizados por categoria de risco (C1–C4), para reservas e escolha de acomodação.
- **Temas cobertos:** diferença Casa x Pousada, capacidade por acomodação, fotos, diagnóstico de perfil (família, casal, pet), datas relativas, orçamento, disponibilidade, taxa adicional, mínimo de diárias em feriado, desconto, condição especial, negociação sensível, alteração de política.
- **Limites:** nunca cita valor comercial de nenhum tipo — nem diária, nem pacote, nem taxa, nem serviço opcional já confirmado oficialmente; pet é só diagnóstico, nunca autorização; toda data relativa vira pergunta de confirmação de ano. Exceção: café da manhã da Casa Arágua não é caso de valor a esconder — é serviço inexistente (regra atualizada 2026-08-07), a IA responde diretamente que a Casa não oferece café.
- **Principais tipos de mensagem que responde:** dúvidas pré-reserva, escolha de acomodação, pedido de foto, pedido de orçamento (contenção, não valor).
- **Quando escalar para humano:** descrição histórica desta linha (Rodada 4). **Atualização 06/08/2026 (ver seção 23): a definição canônica de C1–C4 é `ARQUITETURA_DO_SISTEMA_COMERCIAL_VILLA_ARAGUA.md`, seção 5 — hoje, todo C2 (orçamento/disponibilidade normal) é organizado e encaminhado pela equipe, sem exigir Renildo; todo C3 (desconto/condição especial/exceção/negociação sensível) e todo C4 (conflito/risco grave) sempre exigem Renildo.**
- **Resultado do teste comercial:** `teste_regressao_biblioteca_comercial.py` — 19/19 checagens aprovadas, exit code 0.
- **Observações importantes:** dois lotes de teste em conversa (19 mensagens simuladas) precederam a persistência; identificou e corrigiu um erro de atribuição de "cozinha completa" a Metallo/Wood (que na verdade têm mini cozinha); regra de não citar nem valores já oficialmente confirmados (regra-mãe 17) foi decisão explícita de Renildo em 2026-07-16.

---

## 5. Skills existentes

Existem **12 skills formais** no projeto, em `.claude/skills/`. Todas seguem o mesmo padrão: uma "fonte da verdade" (arquivos oficiais que a skill nunca altera, só consulta) e uma regra mais importante explícita no topo do `SKILL.md`.

*(Nota da reorganização de 2026-08-13: este número — 12 — é o valor histórico do momento em que esta seção foi escrita, 2026-07-16/24. O total real hoje é 16, contando as 4 skills criadas em 2026-07-29 listadas no fim desta mesma tabela. Ver seção 6 do corpo novo deste mapa.)*

| Skill | Função | Entrada | Saída | Arquivos consultados (principais) | Quando usar | Limites/riscos | Agentes prováveis |
|---|---|---|---|---|---|---|---|
| `villa-aragua-sales-receptionist` | Responder como a Recepcionista IA venderia — diagnóstico de lead, Casa x Pousada, objeção, fechamento, follow-up | Mensagem de lead/hóspede | Rascunho de resposta comercial | `DADOS_OFICIAIS...`, `ROTEIRO_RECEPCIONISTA_IA.md` | Qualquer resposta de venda/atendimento WhatsApp | Nunca inventa preço/disponibilidade | Comercial, Orquestrador |
| `villa-aragua-pricing-revenue` | Pensar como gerente de receita — preço, pacote, desconto, sazonalidade, concorrência, ponto de equilíbrio | Pergunta de precificação/estratégia | Análise/recomendação de preço | `DADOS_OFICIAIS...`, `CHECKLIST_DECISOES_CAMPANHA_REABERTURA...` | Decisão de preço, pacote, desconto | Não decide preço final sozinha — é análise, decisão é de Renildo | Precificação/Calendário |
| `villa-aragua-humanizer-pt-br` | Melhorar a forma (tom) de um texto já com conteúdo certo | Texto comercial/atendimento | Texto humanizado | `ROTEIRO_RECEPCIONISTA_IA.md`, skill de vendas | Qualquer texto final antes de enviar | Só muda "como", nunca "o quê" — não pode inventar dado | Experiência/Tom |
| `villa-aragua-copywriting-conversion` | Escrever/revisar textos comerciais que convertem (site, Ads, CTAs) | Briefing de copy | Copy pronta | `DADOS_OFICIAIS...`, banco de copy aprovada | Peça de copy final para site/anúncio | Nunca inventa preço, regra, comodidade ou depoimento | Comercial |
| `villa-aragua-creative-design-ads` | Direção de arte comercial para criativos de Ads/Instagram | Briefing de criativo | Direção/roteiro visual | Copy aprovada, banco de criativos existentes | Criativo para Meta Ads/Instagram | Nunca sugere preço/promoção não confirmado | Comercial (apoio) |
| `villa-aragua-marketing-psychology` | Explicar por que o lead compra/hesita, com ética | Dúvida de comportamento do lead | Explicação/recomendação de abordagem | `DADOS_OFICIAIS...`, skills de venda/preço/copy | Entender fricção/objeção antes de agir | Nunca manipula, esconde informação ou cria escassez falsa | Experiência (apoio) |
| `villa-aragua-content-strategy` | Decidir o quê criar de conteúdo (pilares, calendário, briefing) | Necessidade de conteúdo | Briefing para outra skill executar | `DADOS_OFICIAIS...`, `HISTORIA_E_POSICIONAMENTO...` | Planejamento de conteúdo, não peça final | Não escreve texto final | Orquestrador (marketing) |
| `villa-aragua-ai-seo-geo` | Estruturar conteúdo para ser citável por buscas/IA (Google, ChatGPT, Perplexity) | Conteúdo já decidido | Estrutura otimizada | `DADOS_OFICIAIS...`, `GUIA_DIGITAL_HOSPEDE...` | Otimização de conteúdo já existente | Nunca promete ranking/citação garantida | Turismo/Conteúdo (futuro) |
| `villa-aragua-campaign-analytics` | Analisar performance de campanha e decidir manter/pausar/ajustar | Dados de campanha | Decisão prática de otimização | `AGENTE_IA_MARKETING...`, `SETUP_INICIAL_META_ADS...` | Análise de campanha já rodando | Nunca inventa métrica/ROAS/CPA | Precificação/Calendário (apoio) |
| `villa-aragua-growth-marketer` | Coordenar prioridade de canal e experimentos de crescimento | Objetivo de crescimento | Plano/priorização, aciona outras skills | `AGENTE_IA_MARKETING...`, `CHECKLIST_DECISOES_CAMPANHA...` | Planejamento estratégico de aquisição | Não escreve copy/criativo/preço sozinha | Orquestrador (marketing) |
| `villa-aragua-social-media-manager` | Planejar presença orgânica no Instagram | Necessidade de calendário/post orgânico | Calendário/pauta editorial | `DADOS_OFICIAIS...`, `HISTORIA_E_POSICIONAMENTO...` | Conteúdo orgânico, não tráfego pago | Nenhum post pode sugerir preço/promoção | Experiência (apoio) |
| `villa-aragua-skill-router` | Orquestrar: identificar intenção e escolher a(s) skill(s) certa(s) | Pedido amplo/ambíguo sobre Villa Arágua | Ordem de skills a acionar | Lista das 12 skills reais do ecossistema | Sempre que não estiver claro qual skill usar | Nunca inventa skill que não existe | Orquestrador (é o próprio orquestrador de skills) |
| `meta-business-security-audit` — **criada e testada em 2026-07-29** (ver seção 15.9/20/23; deixou de ser proposta) | Auditar contas de anúncio conectadas, acessos, moedas incomuns, contas genéricas sem relação com o negócio, contas desativadas por atividade incomum | Pedido de auditoria de Business Manager | Relatório de risco + recomendação de revisão humana | Achado real da seção 15.3 (contas "Read-Only" USD/INR, conta desativada) | Antes de publicar campanha, ou periodicamente | Nunca remove acesso sozinha — só relatório | Risco/Escalação, Marketing |
| `campaign-preflight-checklist` — **criada e testada em 2026-07-29** | Checklist de auditoria pré-publicação de campanha (Fase 3 da rotina, seção 15.6) | Campanha montada em rascunho | Checklist preenchido (Casa por engano? preço indevido? automações desligadas? públicos corretos? WhatsApp correto? orçamento correto? campanha antiga reaproveitada?) | Seção 15 (aprendizado SET 26) | Antes de qualquer publicação | Não publica — só verifica | Marketing |
| `campaign-learning-register` — **criada em 2026-07-29** (uso real segue condicionado a dado real pós-lançamento da SET 26) | Registrar campanha → lead → reserva de forma estruturada | Dado real pós-lançamento (conversa, origem, objeção, resultado) | Registro consolidado por campanha/conjunto/criativo | — | Depois de cada campanha rodar (24h/48h/72h/7 dias/encerramento) | Nunca altera/pausa campanha, nunca troca público/criativo, nunca decide otimização sozinha — alimenta decisão humana | Aprendizado Manual, Marketing, `villa-rotina-gestao-operacional` |
| `villa-financial-five-boxes-classifier` — **criada em 2026-07-29** | Classificar entradas/saídas financeiras nas cinco caixas do DNA (seção 2.3) | Lançamento financeiro (item + valor) | Classificação por caixa, subcategoria, alerta de possível mascaramento do resultado | `CLAUDE.md` (Financeiro), `FINANCEIRO/` (ledgers brutos, nunca alterados) | Rotina financeira/mensal, ou sempre que houver lançamento ambíguo | Nunca mistura as cinco caixas num resultado único; marca "ambíguo — decisão humana" quando não houver clareza | `villa-rotina-gestao-operacional` |

---

## 6. Protocolos existentes

### `MODO_RASCUNHO_ASSISTIDO_VILLA_ARAGUA.md`

- **Função:** define o procedimento humano que transforma as bibliotecas em uso real, sem nenhuma automação.
- **Regra central:** a IA só sugere; nunca envia; nunca decide; nunca tem acesso ao WhatsApp real.
- **Quem usa:** Rene e Nubia (primeira linha, copiam/colam, aprovam/editam N1–N3/C1–C2); Renildo (decisões sensíveis e retaguarda de N4/C4).
- **Passo a passo resumido:** hóspede escreve → humano copia a mensagem → IA classifica → IA sugere (rascunho se N1/N2/C1/C2; contenção + escalonamento se N3/N4/C3/C4) → humano revisa → humano envia manualmente.
- **O que a IA pode fazer:** classificar, consultar a biblioteca certa, gerar rascunho ou declarar "sem template dedicado".
- **O que a IA não pode fazer:** enviar mensagem, decidir preço/desconto/exceção, confirmar disponibilidade.
- **Quando escalar:** todo N3/N4 e todo C3/C4, conforme papel humano definido na biblioteca correspondente.
- **Como o humano revisa e envia:** lê o rascunho, decide aprovar sem edição / aprovar com edição / bloquear e reescrever — nunca copia e cola sem ler — e só então envia pelo WhatsApp real, fora desta conversa.

### `PROTOCOLO_USO_DIARIO_RASCUNHO_ASSISTIDO_VILLA_ARAGUA.md`

- **Função:** operacionaliza o Modo Rascunho Assistido em rotina de piloto (1–2 semanas), com formato padrão de entrada/saída e registro.
- **Regra central:** a IA só ajuda a escrever — não decide, não envia, não confirma preço, não confirma disponibilidade, não concede desconto, não autoriza exceção. A mensagem final é sempre responsabilidade humana.
- **Quem usa:** Rene (primeira linha), Nubia (substituta), Renildo (decisão sensível), a IA (só classificação e rascunho).
- **Passo a passo resumido:** colar mensagem + contexto no formato padrão (seção 6 do protocolo) → IA responde no formato padrão (classificação, template, rascunho, pode enviar direto?, escalonamento, risco) → humano revisa com checklist de 10 perguntas (seção 8) → humano envia → registro em tabela simples (seção 9).
- **O que a IA pode fazer:** classificar (Operacional N1–N4, Comercial C1–C4, ou Lacuna), sugerir rascunho, apontar risco.
- **O que a IA não pode fazer:** decidir, enviar, confirmar preço/disponibilidade, conceder desconto, autorizar exceção.
- **Quando escalar:** conforme papéis da seção 4 do protocolo — preço, desconto, exceção, negociação sensível, reclamação com risco e política comercial sempre vão para Renildo.
- **Como o humano revisa e envia:** checklist de 10 perguntas de segurança (seção 8) antes de copiar para o WhatsApp; se qualquer resposta sensível for "sim", não envia sem ajuste.

---

## 7. Regras máximas do projeto (versão original, Rodada 4)

Nenhum agente, humano ou IA, pode violar:

1. A IA não envia mensagem automaticamente.
2. A IA não confirma reserva sozinha.
3. A IA não define preço final sozinha.
4. A IA não concede desconto sozinha.
5. A IA não promete disponibilidade sem conferência humana.
6. A IA não altera regras da pousada.
7. A IA não decide reembolso.
8. A IA não resolve conflito delicado.
9. A IA não substitui Renildo, Rene ou Nubia.
10. Humano sempre revisa antes de enviar.
11. WhatsApp, Zapier, Make, API e backend seguem bloqueados.
12. A IA não cita valor de nenhum serviço, mesmo já confirmado oficialmente (regra-mãe 17 da Biblioteca Comercial). Exceção: café da manhã da Casa Arágua não é mais um caso desta regra — o serviço não existe em nenhuma condição (regra atualizada 2026-08-07), a IA responde diretamente que a Casa não oferece café, sem precisar escalar.
13. A IA não autoriza pet — trata só como dado de diagnóstico; porte grande ou mais de um pet sempre vai para checagem humana direta.
14. A IA nunca promete vista para o mar ou frente-mar (nem Pousada, nem Casa Arágua).
15. Turismo/concierge continua como lacuna — a IA não inventa recomendação específica sem base validada.

*(Nota da reorganização de 2026-08-13: a lista de 15 regras do corpo novo deste mapa, seção 8, é uma reformulação executiva desta mesma lista — não uma lista diferente. Esta versão original permanece aqui por ter redação/numeração citada em outros arquivos do projeto.)*

---

## 8. Regras de escalação humana (versão original, Rodada 4)

### Rene
Primeira linha. Recebe:
- dúvidas operacionais simples (N1/N2);
- respostas comerciais simples (C1/C2);
- pedidos de informação/foto;
- triagem inicial de qualquer mensagem;
- rascunhos de contenção (N3/C3) — que ele encaminha, não resolve sozinho;
- problemas de limpeza e manutenção de rotina.

### Nubia
Substituta de Rene, mesmas travas e mesmo escopo — operacional e comercial simples, sem decisão sensível.

### Renildo
Decisão sensível, sempre. Recebe:
- preço e desconto;
- reembolso;
- reclamação com risco de avaliação negativa;
- conflito ou hóspede irritado sem solução simples;
- alta temporada / decisões de Casa Arágua fora do padrão;
- exceções de qualquer tipo (pet fora do padrão, política, horário);
- negociação sensível ou comparação de preço com concorrente;
- decisão comercial ou financeira;
- ajuste/aprovação de novos templates nas bibliotecas;
- retaguarda de N4 se ninguém assumir em até 3 minutos (regra provisória, validada no Tema 4.9).

---

## 9. Testes já realizados

### 9.1 Teste operacional

**Testes manuais históricos (Rodada 1, 2026-07-10 a 2026-07-12):** 14 temas testados individualmente (`RESULTADO_TESTE_*`) — acesso/lock box, café da manhã, cancelamento Casa, cancelamento Pousada, check-in/checkout early/late, churrasqueira, crianças/capacidade/cama extra, dúvida fora da base, golpe/pagamento, hóspede irritado, pedido de desconto, pet, regras da casa, visitantes/festas/silêncio, Wi-Fi Casa. Todos aprovados, cada um com registro próprio.

**Teste estrutural automatizado (Rodada 4, Tema 4.21):** `teste_regressao_biblioteca.py` — 15 checagens (25 códigos de template presentes, distâncias oficiais, cama extra, SAMU/Polícia, cancelamento Pousada/Casa, ausência do vídeo de chegada inexistente, WhatsApp real bloqueado). **Resultado: 15/15 aprovado.**
- Pontos fortes: nenhuma divergência de dado oficial encontrada; correção do "cozinha equipada" indevido no PC-N1-09 confirmada.
- Pontos de atenção: nenhum registrado nesta rodada de teste.
- Situações que exigiram escalação: nenhuma — é teste estrutural, não simulação de conversa.

### 9.2 Teste comercial

**Lotes de simulação em conversa (Tema 4.24, Rodada 4):** Lote 01 (9 mensagens) e Lote 02 (10 mensagens) — 19 mensagens simuladas cobrindo família, casal, pet padrão e fora do padrão, data relativa, foto, foto+preço misto, valor, pacote fechado, mínimo de diárias (Réveillon e Carnaval), desconto, Pix, comparação de acomodações, pressão de preço/concorrente. **Resultado: aprovado nos dois lotes.**
- Pontos fortes: identificou e corrigiu a atribuição indevida de "cozinha completa" a Metallo/Wood; identificou o caso de pet fora do padrão (porte grande/múltiplos pets) como exigindo checagem humana direta.
- Pontos de atenção: valor do café da Casa (já oficialmente confirmado) quase virou exceção à regra de não citar preço — decisão final foi não abrir exceção (regra-mãe 17).
- Situações que exigiram escalação: todos os casos C3 (orçamento/disponibilidade) e C4 (desconto/negociação/pressão de concorrente).

**Teste estrutural automatizado (Tema 4.24):** `teste_regressao_biblioteca_comercial.py` — 19 checagens (categorias C1–C4, 21 códigos de template, regra de não citar valor, ausência de "R$" em texto entregável, pet como diagnóstico, desconto como encaminhamento, disponibilidade como checagem, correção do PC-C2-03, rótulo do PC-C4-04, bloqueio de automação). **Resultado: 19/19 aprovado.**

---

## 10. Fluxo atual de uso manual (versão original)

1. Humano recebe mensagem no WhatsApp, Instagram, Booking, Airbnb ou outro canal.
2. Humano cola a mensagem na IA, no formato padrão do protocolo (mensagem + contexto: produto, reserva, datas, pessoas, observação).
3. IA classifica (Operacional N1–N4, Comercial C1–C4, ou Lacuna).
4. IA consulta a Biblioteca Operacional ou Comercial (ou declara "sem template dedicado").
5. IA gera rascunho, ou contenção + destino de escalonamento se N3/N4/C3/C4.
6. Humano revisa (checklist de 10 perguntas do Protocolo de Uso Diário).
7. Humano ajusta se necessário.
8. Humano envia manualmente pelo canal real.
9. Caso relevante pode virar registro no piloto e, depois, candidato a novo template.

**Isso ainda não é automação.** Nenhum passo acima é executado por um sistema — todos dependem de uma pessoa copiar, colar e enviar.

---

## 11. Lacunas atuais (registradas na Rodada 4/24)

- Agentes internos já desenhados e implementados como arquivos (`.claude/agents/`, seção 2.2), mas **ainda não testados em volume real de uso** — é a maior lacuna restante, não mais o desenho em si.
- Matriz final de classificação unificada — parcialmente resolvida por `MATRIZ_ROTEAMENTO_AGENTES_VILLA_ARAGUA.md` (trilhas, C1–C4, N1–N4, escalação, skills), mas sem validação em casos reais além dos exemplos ilustrativos do próprio documento.
- Regra definitiva de roteamento entre Biblioteca Operacional, Comercial e Turismo/Concierge quando uma mensagem mistura os três (ex.: pergunta sobre localização + clima da região, observado no Tema 4.23).
- Padrão final de escalação testado em volume real (o piloto do Tema 4.26 está pausado após o Registro 16 — ver seção 2.1; retomada e avaliação de resultado ainda não agendadas).
- Rotina de aprendizado — como um erro registrado (seção 11 do Protocolo) vira de fato um ajuste de template.
- Atualização futura das bibliotecas — processo formal de versão v2 ainda não definido.
- Biblioteca de Turismo/Concierge — não existe ainda; hoje é tratada como lacuna deliberada (`ROTEIROS_SUGERIDOS_BOMBINHAS.md` é a matéria-prima, mas não virou biblioteca testada).
- Integração técnica futura (WhatsApp, Zapier, Make, API, backend) — permanece bloqueada e nem desenhada tecnicamente ainda, só mencionada como "não autorizada".
- Painel de acompanhamento do piloto — hoje é uma tabela simples manual (seção 9 do Protocolo), não uma ferramenta.
- Documentação de casos-limite — casos mistos (operacional + comercial na mesma mensagem) têm exemplos pontuais (Tema 4.23), mas não uma regra formal ainda.

---

## 12. Agentes candidatos (histórico do desenho — hoje implementados)

**Nota de 2026-07-24:** esta seção documenta o *desenho original* de cada agente. Todos os 7 candidatos abaixo já existem como arquivos reais em `.claude/agents/` (mais dois que não estavam previstos nesta lista original: `villa-marketing-meta-ads.md` e o branch `video-factory-ia.md`). A ficha completa e atualizada de cada um — com exemplos práticos, riscos e frase-guia — está em `DEFINICAO_AGENTES_VILLA_ARAGUA_IA.md`; o roteamento entre eles está em `MATRIZ_ROTEAMENTO_AGENTES_VILLA_ARAGUA.md`. O texto abaixo permanece como registro histórico do raciocínio inicial.

### Agente Orquestrador / Triagem
- **Função provável:** ler a mensagem recebida, classificar Operacional x Comercial x Turismo x Lacuna, e direcionar para a biblioteca/skill certa.
- **Arquivos que usaria:** `PROTOCOLO_USO_DIARIO_RASCUNHO_ASSISTIDO_VILLA_ARAGUA.md`, `MAPA_DE_USO_DAS_SKILLS_VILLA_ARAGUA.md`.
- **Skills que usaria:** `villa-aragua-skill-router`.
- **Decisões que poderia apoiar:** qual biblioteca/skill consultar primeiro.
- **Decisões que não poderia tomar:** qualquer resposta final ao hóspede.
- **Quando escalaria:** mensagem mista ou ambígua entre operação/comercial/turismo, sem classificação clara.

### Agente Comercial / Reservas
- **Função provável:** gerar rascunhos C1–C4 (diagnóstico, escolha de acomodação, contenção de orçamento/desconto).
- **Arquivos que usaria:** `BIBLIOTECA_COMERCIAL_RECEPCIONISTA_IA_VILLA_ARAGUA.md`, `DADOS_OFICIAIS_ATENDIMENTO_VILLA_ARAGUA.md`.
- **Skills que usaria:** `villa-aragua-sales-receptionist`, `villa-aragua-humanizer-pt-br`.
- **Decisões que poderia apoiar:** qual acomodação sugerir, como responder pedido de foto.
- **Decisões que não poderia tomar:** preço, disponibilidade, desconto.
- **Quando escalaria:** todo C3/C4.

### Agente Operacional / Estadia
- **Função provável:** gerar rascunhos N1–N4 (check-in, Wi-Fi, cancelamento, emergência).
- **Arquivos que usaria:** `BIBLIOTECA_OFICIAL_RECEPCIONISTA_IA_VILLA_ARAGUA.md`, `GUIA_CHECKIN_AUTONOMO.md`, `GUIA_DIGITAL_HOSPEDE_VILLA_ARAGUA.md`.
- **Skills que usaria:** `villa-aragua-humanizer-pt-br`.
- **Decisões que poderia apoiar:** qual template operacional usar.
- **Decisões que não poderia tomar:** qualquer exceção de regra da casa.
- **Quando escalaria:** todo N3/N4.

### Agente de Risco / Escalação
- **Função provável:** identificar N4/C4 e reclamações/hóspede irritado, garantir que a contenção + alerta cheguem ao humano certo (regra dos 3 minutos).
- **Arquivos que usaria:** ambas as bibliotecas (seções de N4/C4), `MODO_RASCUNHO_ASSISTIDO_VILLA_ARAGUA.md`.
- **Skills que usaria:** nenhuma skill formal específica ainda — comportamento hoje vive só nas bibliotecas.
- **Decisões que poderia apoiar:** para quem escalar (Rene/Nubia/Renildo).
- **Decisões que não poderia tomar:** resolver o conflito ele mesmo.
- **Quando escalaria:** sempre — é o próprio agente de escalação.

### Agente de Experiência / Tom
- **Função provável:** revisar tom antes do envio (acolhedor, "Férias Pra Sempre", sem robotização).
- **Arquivos que usaria:** `PLAYBOOK_ATENDIMENTO_WHATSAPP.md`, `HISTORIA_E_POSICIONAMENTO_VILLA_ARAGUA.md`.
- **Skills que usaria:** `villa-aragua-humanizer-pt-br`, `villa-aragua-marketing-psychology`.
- **Decisões que poderia apoiar:** ajuste de tom de um rascunho já correto em conteúdo.
- **Decisões que não poderia tomar:** mudar o conteúdo/dado da resposta.
- **Quando escalaria:** nunca decide sozinho — sempre entrega para revisão humana, como os demais.

### Agente de Precificação / Calendário
- **Função provável:** apoiar Renildo com análise de sazonalidade/concorrência quando ele decidir preço — nunca decidir sozinho.
- **Arquivos que usaria:** `DADOS_OFICIAIS_ATENDIMENTO_VILLA_ARAGUA.md`, `CHECKLIST_DECISOES_CAMPANHA_REABERTURA_VILLA_ARAGUA_2026.md`.
- **Skills que usaria:** `villa-aragua-pricing-revenue`, `villa-aragua-campaign-analytics`.
- **Decisões que poderia apoiar:** análise de quando subir/manter/reduzir preço.
- **Decisões que não poderia tomar:** o valor final — isso é sempre de Renildo.
- **Quando escalaria:** sempre entrega análise, nunca decisão, a Renildo.

### Agente de Aprendizado Manual
- **Função provável:** consolidar os registros do piloto (seção 9 do Protocolo) em candidatos a novo template ou correção de biblioteca.
- **Arquivos que usaria:** tabela de registro do piloto (ainda não é arquivo formal, é manual — ver seção 11).
- **Skills que usaria:** nenhuma ainda.
- **Decisões que poderia apoiar:** sugerir novo template para aprovação humana.
- **Decisões que não poderia tomar:** aprovar/persistir o novo template sozinho — isso segue exigindo autorização explícita, como em todos os Temas desta rodada.
- **Quando escalaria:** toda sugestão de novo template vai para revisão humana (Renildo aprova biblioteca).

---

## 13. Observações para o ChatGPT / Villa Arágua BOL

- **Fonte principal (nunca contradizer sem confirmar com o humano):** `DADOS_OFICIAIS_ATENDIMENTO_VILLA_ARAGUA.md`, `BIBLIOTECA_OFICIAL_RECEPCIONISTA_IA_VILLA_ARAGUA.md`, `BIBLIOTECA_COMERCIAL_RECEPCIONISTA_IA_VILLA_ARAGUA.md`, `MODO_RASCUNHO_ASSISTIDO_VILLA_ARAGUA.md`, `PROTOCOLO_USO_DIARIO_RASCUNHO_ASSISTIDO_VILLA_ARAGUA.md`.
- **Fonte de apoio (contexto, não substitui a principal em caso de conflito):** `ROTEIRO_RECEPCIONISTA_IA.md`, `PLAYBOOK_ATENDIMENTO_WHATSAPP.md`, `HISTORIA_E_POSICIONAMENTO_VILLA_ARAGUA.md`, `GUIA_DIGITAL_HOSPEDE_VILLA_ARAGUA.md`, `MIDIAS_E_LINKS_OFICIAIS_VILLA_ARAGUA.md`, `ROTEIROS_SUGERIDOS_BOMBINHAS.md`, as 12 skills de `.claude/skills/`.
- **Não alterar sem autorização explícita de Renildo:** as duas bibliotecas, os dois protocolos, `DADOS_OFICIAIS_ATENDIMENTO_VILLA_ARAGUA.md`, e nenhum dos dois scripts de teste.
- **Testadas e aprovadas:** Biblioteca Operacional (15/15) e Biblioteca Comercial (19/19), ambas com script de regressão estrutural verificável.
- **Implementados como arquivos, mas não testados em volume real:** os 9 agentes de `.claude/agents/` (seção 2.2) (valor histórico — hoje são 11 agentes/16 skills, ver seção 6 do corpo novo) e o branch `video-factory-ia`. "Implementado" significa que o arquivo `.md` existe e pode ser invocado no Claude Code — não significa testado em produção nem conectado a canal real.
- **Ainda conceituais / sem arquivo formal:** toda a linha de "automação futura" (seção 3.G); a Biblioteca de Turismo/Concierge completa (a SI-01 é só um apoio inicial, ver `SI_01_INSPIRACAO_DE_VIAGEM_RECEPCIONISTA_IA_VILLA_ARAGUA.md`).
- **Cuidados ao operar ou ampliar agentes:** nenhum agente pode enviar mensagem, decidir preço, confirmar disponibilidade, conceder desconto ou autorizar exceção — essas são as regras máximas da seção 7, e valem para qualquer agente novo ou existente. Qualquer agente novo deve declarar explicitamente quando escalaria para Rene, Nubia ou Renildo, seguindo o modelo de ficha da seção 4 de `DEFINICAO_AGENTES_VILLA_ARAGUA_IA.md`.
- **Objetivo permanece:** manter o projeto em Modo Rascunho Assistido, sem automação real, até que o piloto manual (Tema 4.26) seja retomado e prove valor, e Renildo autorize explicitamente qualquer próximo passo técnico.

---

## 14. Conteúdo sensível que NÃO deve ser incluído

Este arquivo, e qualquer arquivo derivado dele, não deve conter:

- senhas;
- tokens;
- API keys;
- credenciais;
- dados pessoais de hóspedes;
- telefones de hóspedes;
- conversas privadas completas;
- informações bancárias;
- qualquer dado sensível.

Nenhum exemplo real de hóspede foi usado neste inventário — os exemplos citados nas seções 9 e 10 vêm de mensagens simuladas nos testes da Rodada 4, não de conversas reais. Se algum exemplo real precisar ser usado no futuro, deve ser completamente anonimizado antes de sair deste projeto.

---

## 15. Aprendizado Meta Ads — Campanha SET 26 Pousada Arágua

**Status factual, para não haver ambiguidade:** as duas campanhas descritas nesta seção foram **montadas em rascunho** no Meta Ads Manager, com previsão de lançamento em **04/08/2026**. Nenhuma foi publicada. Nenhuma rodou. Não existe dado de gasto, alcance, conversa ou resultado — porque nada aconteceu ainda. Tudo abaixo é registro de estratégia, estrutura e aprendizado de processo, não relato de performance.

*(Nota da reorganização de 2026-08-13: este status é o registrado até a atualização de 06/08/2026, seção 23. Para o estado mais recente conhecido — evidência de campanha real gerando lead real no CRM a partir de 11/08/2026, ainda sem auditoria formal — ver seção 10 do corpo novo deste mapa.)*

### 15.1 — Contexto e status das campanhas

**Status atualizado em 2026-07-29:** Renildo informou que as duas campanhas já foram montadas de fato no Meta Ads, com lançamento previsto para **05/08/2026**. Status anterior era `rascunho`; status novo é `MONTADA / AGUARDANDO LANÇAMENTO EM 05/08/2026`. Nenhuma campanha foi publicada, alterada, teve orçamento modificado ou automação ativada por esta atualização — é só registro do que Renildo já fez fora desta conversa.

| Campanha | Nome exato | Objetivo | Orçamento | Estrutura | Status anterior | Status atual |
|---|---|---|---|---|---|---|
| Quente | `SET 26 QUENTE CWB SC` *(nome oficial confirmado em 2026-07-29 — `SETE 26 QUENTE CWB SC` foi erro de digitação em registros anteriores, corrigido aqui)* | Engajamento / WhatsApp | R$ 30/dia (CWB ≈R$14, SC ≈R$16) | 2 conjuntos (CWB Quente, SC Quente), ABO | Rascunho | **Montada / aguardando lançamento em 05/08/2026** |
| Fria/morna | `SET 26 FRIO CWB SC` | Engajamento / WhatsApp | R$ 20/dia | 1 conjunto único (CWB + SC Regional) | Rascunho | **Montada / aguardando lançamento em 05/08/2026** |

**Checklist humano de pré-publicação:** já existe e está pronto para uso em `REVISAO_HUMANA_PUBLICACAO_SET26_META_ADS.md` (checklists de automação por campanha, checklist de Business Manager, e campo de decisão final de Renildo) — esse arquivo também recebeu, na mesma data, o checklist específico de pré-lançamento e a rotina de pós-lançamento para o dia 05/08/2026.

**Criativos:** os três criativos herdados (`POUSADA_7SET_CAFE_01.jpg`, `POUSADA_7SET_PACOTE_DIRETO_01.jpg`, `POUSADA_7SET_PISCINA_01.webp`) foram **verificados visualmente** e aprovados — nenhum contém preço, pacote fechado, "R$1.997" ou promessa comercial antiga, apesar do nome do arquivo `PACOTE_DIRETO` sugerir isso.

**Governança do Business Manager:** segue em status **ATENÇÃO**, não crítico (achado da seção 15.3/18, reconfirmado em teste real) — não bloqueia o lançamento, mas a revisão de contas/acessos continua pendente de conferência humana antes ou em paralelo à publicação.

**Decisão de publicação:** continua sendo sempre humana — nenhuma automação ou agente decide publicar.

**Produto:** somente Pousada Arágua. Não Casa Arágua, não frente-mar, não vista-mar, sem preço no anúncio, sem desconto, sem "últimas vagas" fictícias, sem "mínimo de 4 diárias" escrito no anúncio (qualificado no WhatsApp, com humano revisando).

**Período comercial:** feriado de 7 de Setembro 2026, janela principal 4 a 8/9. Para Curitiba, reforça-se o feriado municipal de 8/9 como janela estendida. Para Santa Catarina, evita-se "escapada", "fim de semana" ou "até segunda" — linguagem que atrai estadias curtas desalinhadas com o mínimo de 4 diárias.

**Detalhamento de público e criativo de cada campanha, WhatsApp aprovado e regras de automação a recusar:** ver arquivos de trabalho da própria rodada (conversa que originou este registro) — este mapa documenta o aprendizado e a estrutura consolidada, não substitui o detalhamento linha a linha já validado com Renildo.

### 15.2 — Limitação de auditoria: campanhas em rascunho

**Aprendizado crítico, com impacto direto na arquitetura de agentes:** foi feita uma tentativa real de auditoria das duas campanhas via Meta Ads conectado (API/integração). O agente **não encontrou nenhuma das duas campanhas** em nenhuma das contas de anúncio conectadas — porque campanhas em status de rascunho não aparecem para agentes conectados via API/integração da forma como as campanhas publicadas/ativas aparecem.

**Regra nova, permanente, a partir de 2026-07-29:**

> Antes de pedir auditoria via Meta Ads conectado, verificar o status da campanha. Se estiver em rascunho, o agente deve pedir prints ou checklist manual — nunca deve concluir "a campanha não existe" ou inventar dados como se a tivesse visto. Se estiver publicada/em análise/ativa, o agente pode buscar via integração.

**Checklist de status x tipo de auditoria:**

| Status da campanha | Tipo de auditoria possível |
|---|---|
| Em rascunho | Por print/checklist manual — API/integração não enxerga |
| Em análise (recém-publicada) | Auditoria parcial via Meta Ads conectado (estrutura visível, entrega ainda não estabilizada) |
| Ativa | Auditoria completa com dados reais via Meta Ads conectado |
| Desativada/pausada | Auditoria histórica via Meta Ads conectado |
| Programada (agendada para data futura) | Verificar data/hora de início antes de qualquer leitura de performance |
| Rejeitada | Acionar `villa-risco-escalacao` e revisão de conformidade antes de qualquer nova tentativa de publicação |

Este checklist deve ser consultado por qualquer agente (`villa-marketing-meta-ads` em primeiro lugar) antes de prometer ou tentar uma auditoria via integração.

### 15.3 — Governança e segurança do Business Manager

Durante a tentativa de auditoria via integração (seção 15.2), foram identificadas, no mesmo negócio "Pousada Arágua" do Business Manager, contas de anúncio adicionais nomeadas genericamente como **"(Read-Only)"**, algumas em moedas incomuns para uma operação brasileira (USD, INR), com campanhas de nome genérico ("Traffic Campaign", "Sales Campaign") sem nenhuma relação com o histórico real da Villa Arágua — e uma conta **desativada pelo próprio Meta por atividade incomum** ("Your ad account was flagged because of unusual activity. All your ads have been paused.").

**Isto é registrado aqui como risco de governança do Business Manager, não como fato resolvido.** Nenhuma ação foi tomada sobre essas contas — nenhum acesso foi removido, nenhuma conta foi alterada. O padrão observado (contas "read-only" genéricas, moeda estrangeira, campanhas sem relação com o negócio real, conta sinalizada por atividade incomum) é consistente com cenários conhecidos de acesso indevido/comprometimento de Business Manager, e deve ser revisado por um humano com acesso administrativo ao Business Manager — fora do escopo desta IA.

**Agente/skill sugerida (candidata — ainda não criada, não existe hoje em `.claude/agents/` nem `.claude/skills/`):**

- Nome proposto: `villa-governanca-meta-business` (agente) ou `meta-business-security-audit` (skill).
- **Função que teria:** auditar periodicamente contas de anúncio conectadas, usuários com acesso, parceiros, permissões, contas read-only desconhecidas, moedas estranhas, campanhas genéricas sem relação com a Villa Arágua, contas desativadas por atividade incomum, e sinalizar risco de golpe/acesso indevido/Business Manager comprometido.
- **O que nunca faria:** remover acesso, revogar permissão ou alterar configuração de conta automaticamente — apenas gerar relatório e orientar revisão humana, seguindo a mesma régua de nenhuma automação real que vale para todos os agentes deste projeto (seção 7).
- **Status:** proposta registrada aqui para avaliação futura de Renildo; não foi criado nenhum arquivo de agente ou skill com este nome. Enquanto não existir, o achado de risco (acima) deve ser tratado manualmente por Renildo, com apoio de `villa-risco-escalacao` para garantir que o alerta não se perca.

*(Nota da reorganização de 2026-08-13: a skill `meta-business-security-audit` foi de fato criada em 2026-07-29, ver seção 5 acima e 15.9/20/23. O agente `villa-governanca-meta-business` permanece não criado.)*

### 15.4 — Aprendizados sobre Meta Ads (automações a recusar)

1. A pontuação/qualidade de anúncio da Meta não deve ser obedecida cegamente — pontuação baixa que vem de **recusar automações** (Advantage+, geração de texto por IA, mídia flexível, descrição dinâmica, retoques visuais, expansão de localização) deve ser **ignorada deliberadamente**, não corrigida.
2. A Meta tende a recomendar automações que aumentam entrega/alcance, mas que reduzem o controle estratégico sobre público, criativo e mensagem — especialmente arriscado numa campanha pequena (R$14-30/dia) onde cada real de verba precisa ir para o público certo.
3. Para campanha **quente**, controle é mais importante que pontuação — público personalizado real, sem semelhantes, sem interesses amplos, sem Advantage+.
4. Para campanha **fria/morna**, pode haver um pouco mais de abertura (interesses, não públicos personalizados), mas ainda com limites claros de localização, idade e exclusão de praças fora do plano.
5. Lista de automações a **não aceitar automaticamente** em nenhuma campanha deste ciclo: orçamento Advantage+, público Advantage+, geração de texto por IA da Meta, mídia flexível, descrição dinâmica, retoques visuais automáticos, expansão de localização para pessoas "apenas interessadas" na região, e qualquer recomendação "Aplicar agora" da Meta.
6. Aprendizado específico da campanha fria/morna (R$20/dia): "menos é mais" — combinar muitos interesses no mesmo conjunto tende a **ampliar**, não afunilar, o público. Beaches/Praias + Feriado juntos chegaram a um público estimado de ~2 milhões, considerado aceitável para este orçamento; interesses adicionais (Booking, Lodging, Hotel, Casal, Férias, Viagem em família) foram deliberadamente deixados de fora neste primeiro ciclo por serem genéricos demais ou já cobertos pelo enquadramento de "Beaches + Feriado".

### 15.5 — Campanhas antigas: regra de obsolescência permanente

Registrado com mais detalhe em `ADENDO_STATUS_CAMPANHA_7_SETEMBRO_2026_OBSOLETA_POS_REVENUE_MANAGER.md` (seção 3.F). Resumo para este mapa: campanhas antigas de 7 de Setembro que publicavam preço fechado ("4 diárias por R$ 1.997"), misturavam Pousada e Casa Arágua, ou seguiam lógica anterior ao Revenue Manager, são **históricas/obsoletas** e não devem ser reutilizadas como base direta para publicação — apenas como referência histórica de como a estratégia evoluiu. Nenhum desses arquivos foi apagado.

### 15.6 — Rotina recomendada de lançamento de campanha Meta Ads

Consolidação de processo, para ser seguida em qualquer campanha futura, não só nesta:

**Fase 1 — Estratégia:** definir produto (nunca misturar Pousada/Casa); definir período; definir público; definir orçamento; definir promessa; confirmar datas/feriados regionais; validar com calendário comercial e `villa-precificacao-calendario`.

**Fase 2 — Montagem:** criar campanha e conjuntos; configurar públicos; subir criativos; configurar WhatsApp; **desligar todas as automações da seção 15.4**; salvar como rascunho.

**Fase 3 — Auditoria pré-publicação (por print/checklist manual — ver 15.2):** revisar se não há Casa Arágua por engano; checar se não há preço/desconto indevido; checar se automações estão desligadas; checar públicos; checar mensagens de WhatsApp; checar orçamento; checar se campanha antiga não foi reaproveitada (seção 15.5).

**Fase 4 — Publicação:** publicar apenas na data planejada; garantir que os itens publicados pertencem só à campanha correta; aguardar análise da Meta.

**Fase 5 — Auditoria pós-publicação (via Meta Ads conectado — ver 15.2):** verificar status, entrega, erros de configuração, primeiros dados.

**Fase 6 — Monitoramento:**
- **24h:** gasto, alcance, impressões, conversas iniciadas, custo por conversa, qualidade dos leads, perguntas recebidas no WhatsApp.
- **48h:** comparar quente vs. frio; comparar imagem única vs. carrossel; avaliar se o frio está trazendo curiosos demais; avaliar se o quente está gerando leads mais qualificados.
- **72h:** decidir manter/pausar/ajustar criativo; avaliar entrada de Reels; avaliar necessidade de remarketing.
- **7 dias:** avaliar reserva gerada, custo por reserva, qualidade dos leads, origem, impacto no calendário, decisão de aumentar/manter/encerrar verba.

### 15.7 — Critérios de decisão

- **Manter** se: custo por conversa aceitável; leads perguntam pelo período correto; há conversas qualificadas; não há confusão Pousada x Casa; não há pressão excessiva por desconto.
- **Pausar criativo** se: gasto sem conversa; comentários negativos; criativo atraindo público fora do período; lead perguntando majoritariamente preço baixo; criativo gerando confusão com Casa.
- **Aumentar verba** se: conversas qualificadas; custo por conversa saudável; WhatsApp dando conta do volume; disponibilidade real; margem preservada.
- **Subir Reels** se: imagem e carrossel já têm dados iniciais; campanha quente precisa de renovação; frequência subindo; custo por conversa piorando; há vídeo pronto e coerente.
- **Criar remarketing** se: volume suficiente de engajamento; visualizações de vídeo; cliques/conversas não convertidas; disponibilidade ainda aberta para o período.

### 15.8 — Nota estratégica

A Villa Arágua IA não deve buscar campanha bonita ou pontuação alta da Meta como fim em si. Ela deve proteger: margem; coerência comercial; reserva direta; clareza entre Pousada e Casa Arágua; tempo do Renildo; qualidade dos leads; e a travessia financeira que sustenta a família e o MANECO (ver `CLAUDE.md` e `DNA VILLA ARAGUA/DNA Villa Arágua (1).txt` para o contexto estratégico de fundo).

### 15.9 — Agentes e skills atualizados com este aprendizado

Os agentes e skills abaixo já existem como arquivos reais (seções 2.2 e 5) e devem incorporar, na próxima revisão de conteúdo de cada um, os aprendizados desta seção 15 — nenhum arquivo de agente/skill foi reescrito automaticamente ao gerar este registro, esta lista é o mapa do que precisa ser revisado:

- **Agentes:** `villa-marketing-meta-ads` (principal — automações a recusar, checklist de status de campanha, rotina de lançamento); `villa-precificacao-calendario` (coerência de mínimo de diárias e período com o Revenue Manager); `villa-comercial-reservas` (qualificação de período/perfil no WhatsApp sem confirmar preço/disponibilidade); `villa-experiencia-tom` (tom das mensagens de boas-vindas aprovadas); `villa-risco-escalacao` (achado de governança do Business Manager, seção 15.3); `villa-aprendizado-manual` (consolidar este ciclo como aprendizado permanente); `villa-orquestrador-triagem` (é o agente real de triagem/roteamento do projeto — **nota de precisão:** o pedido original desta atualização citou "villa-skill-router" como agente; o nome real do agente é `villa-orquestrador-triagem`, e existe também uma skill separada chamada `villa-aragua-skill-router` em `.claude/skills/`, que é quem decide qual skill acionar. Os dois nomes foram unificados aqui para não introduzir um agente inexistente no mapa).
- **Skills:** `villa-aragua-campaign-analytics`, `villa-aragua-copywriting-conversion`, `villa-aragua-creative-design-ads`, `villa-aragua-marketing-psychology`, `villa-aragua-sales-receptionist`, `villa-aragua-humanizer-pt-br`, `villa-aragua-growth-marketer`, `villa-aragua-pricing-revenue` (nomes reais, todas já existentes em `.claude/skills/`, conferidas nesta mesma rodada de trabalho via `villa-aragua-skill-router`).
- **Decisão de 2026-07-29 (segunda atualização do dia):** criar agora a skill `meta-business-security-audit` (Fase 1, ver seções 5, 18 e 19) — deixa de ser só candidata. O **agente** `villa-governanca-meta-business` continua **não criado**; a governança do Business Manager segue via skill + `villa-risco-escalacao`, sem agente próprio por enquanto.

---

## 16. Changelog

### 2026-07-29
- Adicionada seção 15 ("Aprendizado Meta Ads — Campanha SET 26 Pousada Arágua"), com subseções de status das campanhas (15.1), limitação de auditoria de campanhas em rascunho (15.2), governança e segurança do Business Manager (15.3), aprendizados sobre automações da Meta (15.4), regra de obsolescência de campanhas antigas (15.5), rotina de lançamento em 6 fases (15.6), critérios de decisão (15.7), nota estratégica (15.8) e lista de agentes/skills a atualizar (15.9).
- Adicionada linha em 3.F para `ADENDO_STATUS_CAMPANHA_7_SETEMBRO_2026_OBSOLETA_POS_REVENUE_MANAGER.md`; `CONFIGURACAO_ZAP_CARGA_META_ADS_SET_26_7SET_VILLA_ARAGUA.md` marcada como histórica/obsoleta (não apagada).
- Nenhum arquivo de agente ou skill foi reescrito automaticamente — a seção 15.9 é o mapa do que precisa ser incorporado na próxima revisão de conteúdo de cada um.
- Nenhuma campanha foi publicada, editada ou alterada no Meta Ads real. Nenhum dado de performance foi registrado, porque nenhuma campanha rodou ainda.

### 2026-07-24 (entrada anterior, preservada)
- Os 9 agentes internos previstos na v1 (mais o branch `video-factory-ia`) saíram da fase conceitual e existem como arquivos reais em `.claude/agents/`, com as 12 skills conectadas (valor histórico — hoje são 11 agentes/16 skills, ver seção 6 do corpo novo).
- Piloto manual do Registro 16 seguia pausado, retomada não agendada (ver seções 2.1 e 2.2).

**Continuação deste changelog:** a segunda atualização do dia 2026-07-29 (evolução arquitetural — rotinas, riscos e plano de fases) está registrada na seção 20, ao final do documento, junto das seções novas que ela descreve (17, 18, 19), em vez de aqui, para manter a entrada perto do conteúdo que ela resume.

---

## 17. Rotinas reais

Cada rotina abaixo tem objetivo, gatilho, entrada, agente/skill acionada, saída esperada e o ponto exato onde a decisão volta para Renildo — nenhuma rotina decide sozinha.

### 17.1 — Rotina diária
- **Objetivo:** acompanhar reservas, check-ins/check-outs do dia, mensagens pendentes, problemas urgentes.
- **Quando roda:** todo dia.
- **Entrada:** mensagens do dia, calendário de reservas.
- **Agente/skill:** `villa-recepcionista-rascunho` (mensagens), `villa-risco-escalacao` (se houver urgência).
- **Saída esperada:** rascunhos revisados, lista de pendências do dia.
- **Decisão humana obrigatória:** toda mensagem antes de enviar; toda urgência N3/N4.

### 17.2 — Rotina semanal
- **Objetivo:** revisar leads da semana, campanhas ativas, ajustes de preço pendentes, manutenção.
- **Quando roda:** semanal (dia fixo a definir com Renildo).
- **Entrada:** registros de lead da semana, status de campanha (se publicada), calendário de preço.
- **Agente/skill:** `villa-rotina-gestao-operacional` *(criado em 2026-07-29)*, apoiado por `villa-marketing-meta-ads`, `villa-precificacao-calendario`, `campaign-learning-register`.
- **Saída esperada:** resumo semanal — leads, conversão, campanhas, preço, manutenção.
- **Decisão humana obrigatória:** qualquer ajuste de preço, verba ou pausa de campanha.

### 17.3 — Rotina mensal
- **Objetivo:** fechamento de faturamento, custos, ocupação, prioridades do mês seguinte.
- **Quando roda:** mensal.
- **Entrada:** ledgers de `FINANCEIRO/`, ocupação do mês, resultado de campanhas.
- **Agente/skill:** `villa-rotina-gestao-operacional` *(criado em 2026-07-29 — implementação do papel "Gerente Geral/Virtual", seção 2.3)*, apoiado por `villa-financial-five-boxes-classifier` *(criado em 2026-07-29)* e por `PAINEL_DECISAO_ROTINA_VILLA_ARAGUA.md` (seção 6 do painel, cinco caixas).
- **Saída esperada:** leitura financeira separada nas cinco caixas definidas na seção 2.3 (resultado operacional da Villa Arágua; renda patrimonial; família/vida pessoal; MANECO/investimento de futuro; saldo geral da travessia) — **nunca** apresentada como um único "lucro/prejuízo da pousada". Primeiro a operação real (caixa 1), separada; só depois o saldo geral da vida e da travessia (caixa 5). Mais prioridades do próximo mês.
- **Decisão humana obrigatória:** toda decisão financeira e toda prioridade estratégica.

### 17.4 — Rotina pré-campanha
- **Objetivo:** montar e auditar campanha antes de publicar.
- **Quando roda:** antes de qualquer publicação de Meta Ads.
- **Entrada:** briefing de campanha (produto, período, público, orçamento, promessa).
- **Agente/skill:** `villa-marketing-meta-ads` → `campaign-preflight-checklist` → `meta-business-security-audit` (se não rodou recentemente).
- **Saída esperada:** checklist preenchido, campanha em rascunho pronta para revisão.
- **Decisão humana obrigatória:** publicar ou não publicar.

### 17.5 — Rotina pós-campanha
- **Objetivo:** monitorar e decidir manter/ajustar/pausar/aumentar verba.
- **Quando roda:** 24h/48h/72h/7 dias após publicação (seção 15.6, Fase 6).
- **Entrada:** dados reais via Meta Ads conectado (nunca em campanha ainda em rascunho — ver 15.2).
- **Agente/skill:** `villa-marketing-meta-ads`, `campaign-learning-register`.
- **Saída esperada:** decisão registrada (manter/pausar criativo/aumentar verba/subir Reels/remarketing), conforme critérios da seção 15.7.
- **Decisão humana obrigatória:** qualquer mudança de verba, criativo ou público.

### 17.6 — Rotina financeira
- **Objetivo:** manter separação entre as cinco caixas financeiras (seção 2.3) — nunca misturar como resultado único da pousada.
- **Quando roda:** mensal, ou quando houver lançamento não categorizado.
- **Entrada:** ledgers simples de `FINANCEIRO/` (hoje sem categorização — limitação já conhecida, ver `CLAUDE.md`).
- **Agente/skill:** `villa-financial-five-boxes-classifier` *(criado em 2026-07-29)*.
- **Saída esperada:** lançamentos classificados por caixa (operação/patrimônio/família/MANECO/saldo geral).
- **Decisão humana obrigatória:** toda classificação ambígua; toda decisão de uso do resultado.

### 17.7 — Rotina operacional semi-autônoma
- **Objetivo:** apoiar decisões operacionais recorrentes (limpeza, manutenção, problemas comuns) com menos dependência direta de Renildo.
- **Quando roda:** conforme demanda operacional.
- **Entrada:** mensagem/registro operacional.
- **Agente/skill:** `villa-operacional-estadia`, `villa-risco-escalacao` se N3/N4.
- **Saída esperada:** rascunho de resposta ou encaminhamento operacional.
- **Decisão humana obrigatória:** toda exceção de regra da casa; todo N3/N4.

### 17.8 — Rotina de aprendizado manual
- **Objetivo:** transformar registros do piloto (atendimento) e da campanha (marketing) em candidatos a novo template/regra.
- **Quando roda:** após cada ciclo relevante (piloto de atendimento ou campanha encerrada).
- **Entrada:** registros de `villa-recepcionista-rascunho` e de `campaign-learning-register`.
- **Agente/skill:** `villa-aprendizado-manual`.
- **Saída esperada:** hipótese de novo template/regra, nunca aplicada sozinha.
- **Decisão humana obrigatória:** toda aprovação de novo template ou regra (Renildo).

---

## 18. Riscos da arquitetura (atualizado 2026-07-29)

| Risco | Descrição | Impacto | Trava de segurança | Agente/skill responsável | Decisão humana necessária |
|---|---|---|---|---|---|
| Automação indevida | Aceitar Advantage+, geração de texto por IA, mídia flexível, descrição dinâmica, expansão de localização ou "Aplicar agora" da Meta sem perceber | Perda de controle de público/criativo/mensagem, custo maior por lead pior | Lista de automações a recusar (seção 15.4) embutida em `villa-marketing-meta-ads` | `villa-marketing-meta-ads` | Toda automação sugerida pela Meta antes de aceitar |
| IA prometer preço/disponibilidade | Qualquer agente confirmar preço final, desconto ou disponibilidade sem fonte/humano | Promessa comercial que a operação não pode cumprir | Regra máxima 3/4/5 (seção 7), presente em todos os agentes | Todos | Toda confirmação de preço/disponibilidade |
| Misturar Pousada e Casa Arágua | Promessa, campanha, preço ou criativo tratando os dois produtos como um só | Diluição de posicionamento, confusão comercial | Regra de separação obrigatória em `villa-marketing-meta-ads` e no roteamento | `villa-marketing-meta-ads`, `villa-orquestrador-triagem` | Sempre que uma peça envolver os dois produtos |
| Meta Ads / Business Manager comprometido | Contas "Read-Only" desconhecidas, moeda estranha, conta desativada por atividade incomum (achado real, seção 15.3) | Risco de fraude de spend, exposição de dados, perda de controle da conta | `meta-business-security-audit` — só relatório, nunca remove acesso | `villa-risco-escalacao` + skill nova | Revisão de acesso no Business Manager é sempre humana, fora desta IA |
| Publicar campanha com Business Manager inseguro | Subir anúncio sem checar governança da conta primeiro | Campanha rodando sob risco de conta comprometida | `campaign-preflight-checklist` inclui checagem de governança antes de publicar | `villa-marketing-meta-ads` | Publicar ou não publicar |
| Campanha em rascunho não aparecer em auditoria via API | Achado real desta sessão — agente concluiu erradamente que campanha "não existia" | Relatório de auditoria incorreto/fabricado | Checklist de status (seção 15.2) — obrigatório antes de qualquer auditoria via integração | `villa-marketing-meta-ads` | Confirmar status real da campanha antes de pedir auditoria |
| Excesso de arquitetura, pouca prática | Criar agentes/skills teóricos sem uso real (ex.: `villa-ops-checklist-builder`, `villa-data-quality-checker`, avaliadas e não criadas nesta rodada) | Mapa cresce, operação real não muda | Regra de exclusão: só criar skill/agente com uso real imediato demonstrado | `villa-aprendizado-manual` sinaliza duplicidade/excesso | Toda criação de agente/skill nova passa por esta pergunta antes de existir |

---

## 19. Plano de evolução em fases (original)

### Fase 1 — essencial para agora
- Absorver aprendizado SET 26 (seção 15) nos agentes/skills impactados (seção 15.9).
- Criar skill `campaign-preflight-checklist`.
- Criar skill `meta-business-security-audit`.
- Organizar status de campanha: rascunho, publicada, em análise, ativa, pausada/desativada, encerrada, histórica/obsoleta (seção 15.2 já cobre isso — formalizar como vocabulário oficial do projeto).
- Confirmar marcação de campanhas antigas com preço/Casa Arágua/lógica pré-Revenue Manager como históricas/obsoletas (já feito via `ADENDO_STATUS_CAMPANHA_7_SETEMBRO_2026...`).
- **Não criar nesta fase:** `villa-ops-checklist-builder`, `villa-data-quality-checker`, agente próprio de governança Meta Business (`villa-governanca-meta-business`) — avaliados e considerados prematuros/redundantes (seção 3 da análise arquitetural de 2026-07-29).

### Fase 2 — próximos 30 dias
- ~~Criar agente `villa-rotina-gestao-operacional`~~ **Feito em 2026-07-29** (seção 2.3), com a leitura financeira em cinco caixas já embutida desde a primeira versão do arquivo — antecipado da Fase 2 para a Fase 1/2, aproveitando janela de tempo de Renildo antes do lançamento SET 26.
- Ativar rotina semanal e mensal (seções 17.2, 17.3) **na prática** — o agente existe, falta rodá-lo em caso real.
- ~~Criar skill `campaign-learning-register`~~ **Feito em 2026-07-29** — colocar em uso real assim que SET 26 publicar (até lá, segue sem dado real para registrar; tentativa de uso prematuro em 2026-07-29 foi corretamente recusada, sem inventar métrica).
- ~~CRM leve de leads~~ **Feito em 2026-07-29** — `CRM_LEADS_VILLA_ARAGUA.md`, arquivo próprio (não só "dentro do registro de campanha" como previsto originalmente — ficou mais claro como arquivo independente).
- ~~Criar `villa-financial-five-boxes-classifier`~~ **Feito em 2026-07-29.**
- ~~Painel simples de decisão~~ **Feito em 2026-07-29** — `PAINEL_DECISAO_ROTINA_VILLA_ARAGUA.md`, 9 seções (resumo, reservas/ocupação, leads/comercial, campanhas Meta Ads, operação, financeiro cinco caixas, tempo de Renildo, decisões pendentes, próximos passos).
- Restam desta fase: ativar as rotinas em caso real (item acima) e testar o conjunto completo (agente + 3 skills + 2 arquivos operacionais) numa rotina semanal/mensal de verdade.

### Fase 3 — próximos 90 dias
- Testar os 9 agentes em volume real (valor histórico — hoje são 11 agentes/16 skills, ver seção 6 do corpo novo) (lacuna mais antiga do projeto, seção 11).
- Biblioteca de objeções comerciais (a partir do que `campaign-learning-register` e `villa-aprendizado-manual` acumularem).
- Biblioteca de problemas operacionais recorrentes.
- Primeiros checklists operacionais nascidos de uso real (não de uma skill geradora genérica).
- Reavaliar `villa-data-quality-checker` **só se** houver padrão real e documentado de dado contraditório entre arquivos.

### Fase 4 — estrutura avançada
- Revenue Manager mais completo (histórico de rodadas já é a base).
- Dashboard leve.
- Integrações controladas (sempre com aprovação humana antes de qualquer ação real).
- Consulta confiável de disponibilidade.
- Concierge digital (Turismo/Concierge, lacuna já registrada na seção 11).
- Qualquer automação interna real só depois de volume testado e aprovação explícita de Renildo — nunca antes.

---

## 20. Changelog — segunda atualização do dia (2026-07-29, continuação da seção 16)

- Adicionada seção 2.3 (papel "Gerente Geral/Virtual" do CLAUDE.md sem agente correspondente — decisão de planejar `villa-rotina-gestao-operacional`, com a regra explícita das cinco caixas financeiras: resultado operacional da Villa Arágua, renda patrimonial, família/vida pessoal, MANECO/investimento de futuro, e saldo geral da travessia — nesta ordem de leitura).
- Adicionadas 3 linhas na tabela de skills (seção 5): `meta-business-security-audit` e `campaign-preflight-checklist` (criar agora, Fase 1), `campaign-learning-register` (schema definido, uso real na Fase 2).
- Atualizada a seção 15.9: a skill `meta-business-security-audit` deixou de ser "candidata" e passou a "criar agora"; o agente `villa-governanca-meta-business` permanece não criado.
- Adicionada seção 17 (Rotinas reais — diária, semanal, mensal, pré-campanha, pós-campanha, financeira, operacional semi-autônoma, aprendizado manual), com a rotina mensal (17.3) e a rotina financeira (17.6) já referenciando as cinco caixas da seção 2.3.
- Adicionada seção 18 (Riscos da arquitetura, 7 riscos com trava/responsável/decisão humana).
- Adicionada seção 19 (Plano de evolução em 4 fases).
- Decisão confirmada de **não criar nesta rodada**: `villa-ops-checklist-builder`, `villa-data-quality-checker`, e o agente `villa-governanca-meta-business` — apenas a skill `meta-business-security-audit` foi aprovada para criação (ainda não criada como arquivo; é decisão de mapa, não execução).
- Nenhuma seção existente foi apagada. Nenhum arquivo de agente ou skill foi criado de fato nesta rodada — esta atualização é só arquitetural/de planejamento, como solicitado.

### 2026-07-29 (terceira atualização do dia — Fase 1 testada e status de campanha atualizado)
- As duas skills da Fase 1 (`meta-business-security-audit`, `campaign-preflight-checklist`) foram criadas de fato e testadas em caso real/controlado (as duas campanhas SET 26); os 3 agentes previstos (`villa-marketing-meta-ads`, `villa-risco-escalacao`, `villa-precificacao-calendario`) foram editados cirurgicamente com as regras da seção 15.
- Teste real confirmou a limitação de auditoria de rascunho (seção 15.2) na prática: nenhuma das duas campanhas apareceu via Meta Ads conectado, exatamente como previsto.
- Auditoria real de Business Manager confirmou o achado da seção 15.3: status **atenção** (4 contas "Read-Only" em moeda estranha, 1 conta desativada por atividade incomum), estável e reproduzível em duas rodadas de checagem.
- Seção 15.1 atualizada: nome oficial da campanha quente corrigido para `SET 26 QUENTE CWB SC`; criativos herdados verificados visualmente e aprovados (sem preço embutido); status das duas campanhas passou de `rascunho` para `MONTADA / AGUARDANDO LANÇAMENTO EM 05/08/2026`, por decisão/ação de Renildo fora desta conversa.
- Criado `REVISAO_HUMANA_PUBLICACAO_SET26_META_ADS.md` (checklist de revisão humana pré-publicação) e depois estendido com checklist de pré-lançamento e rotina de pós-lançamento para 05/08/2026.
- Nenhuma campanha foi publicada, alterada, teve orçamento/automação modificados. Nenhum acesso do Business Manager foi removido ou alterado.

### 2026-07-29 (quarta atualização do dia — Fase 2 controlada antecipada)
- Criado `.claude/agents/villa-rotina-gestao-operacional.md` — implementação real do papel "Gerente Geral/Virtual" (seção 2.3): agente de rotina diária/semanal/mensal, com a leitura financeira em cinco caixas embutida desde a primeira versão, que agrega status de outros agentes e nunca decide sozinho (nunca publica campanha, nunca altera preço, nunca confirma disponibilidade/reserva, nunca mexe em acesso/Business Manager).
- Criado `.claude/skills/campaign-learning-register/SKILL.md` — registra aprendizado real de campanha (24h/48h/72h/7 dias/encerramento), com os 24 campos definidos por Renildo; ainda não otimiza campanha sozinha, só registra e recomenda análise humana. Uso real segue dependente de dado real pós-lançamento da SET 26 (ainda não publicada).
- Ambos criados **antes do lançamento SET 26** (05/08/2026), por aproveitamento pontual da janela de tempo de Renildo — não é alteração das campanhas SET 26 nem dos arquivos que as documentam (`REVISAO_HUMANA_PUBLICACAO_SET26_META_ADS.md` não foi tocado, exceto pela atualização de status já registrada na entrada anterior deste changelog).
- Atualizadas as referências "(a criar)" nas seções 2.3, 5, 17.2, 17.3 e 19 para refletir que os dois itens agora existem como arquivos reais — nenhuma seção foi apagada, só as anotações de status foram corrigidas.
- Seção 19 (Fase 2) marca os dois itens como concluídos antecipadamente; os demais itens da Fase 2 (`villa-financial-five-boxes-classifier`, CRM leve de leads, painel simples) seguem pendentes.
- Nenhuma campanha foi publicada, alterada, teve orçamento/automação modificados. Nenhum acesso do Business Manager foi removido ou alterado.

### 2026-07-29 (quinta atualização do dia — Fase 2B: estrutura financeira/comercial/gestão)
- **Correção de contexto registrada:** as campanhas SET 26 ainda não foram lançadas (previsão 05/08/2026). Uma tentativa de rodar `campaign-learning-register` antes da publicação foi corretamente recusada nesta mesma data — sem inventar gasto, alcance, conversas ou qualquer métrica — e serve de exemplo real do comportamento esperado da skill.
- Criado `.claude/skills/villa-financial-five-boxes-classifier/SKILL.md` — classifica lançamentos financeiros nas cinco caixas (seção 2.3), com tabela de itens conhecidos (hospedagem, comissão, limpeza, funcionário, MANECO, dívida, venda de ativo etc.), regra de nunca tratar empréstimo/antecipação/venda de ativo como faturamento operacional, e marcação "ambíguo — decisão humana necessária" quando não houver clareza.
- Criado `CRM_LEADS_VILLA_ARAGUA.md` — CRM leve de leads, 19 campos, status padrão (novo/respondido/em negociação/aguardando retorno/perdido/convertido), regra de nunca tratar conversa ou orçamento como reserva.
- Criado `PAINEL_DECISAO_ROTINA_VILLA_ARAGUA.md` — painel de 9 seções para a rotina semanal/mensal de `villa-rotina-gestao-operacional`, com o bloco de campanhas Meta Ads explicitamente marcado como "sem dado real ainda" enquanto SET 26 não publicar.
- Editado `.claude/agents/villa-rotina-gestao-operacional.md` — adicionados `villa-financial-five-boxes-classifier`, `CRM_LEADS_VILLA_ARAGUA.md` e `PAINEL_DECISAO_ROTINA_VILLA_ARAGUA.md` como apoio; novas regras explícitas (nunca confundir lead com reserva, nunca confundir entrada de caixa com lucro operacional, nunca confundir gasto familiar/MANECO com custo da pousada, nunca usar `campaign-learning-register` antes da publicação real, toda rotina separa operação/comercial/financeiro/risco/MANECO e termina em "decisões que dependem de Renildo").
- Seção 19 (Fase 2) atualizada — os 4 itens restantes da fase (`villa-financial-five-boxes-classifier`, CRM leve, painel simples, e a leitura financeira em cinco caixas já embutida no agente) estão **concluídos**; resta ativar tudo em rotina real.
- Toda esta etapa foi antecipada pela janela de tempo de Renildo antes do lançamento SET 26. Nenhuma campanha SET 26 foi alterada. `REVISAO_HUMANA_PUBLICACAO_SET26_META_ADS.md` não foi tocado. Nenhum registro de campanha (`campaign-learning-register`) foi criado ou preenchido com dado real ou estimado. Nenhuma automação foi ativada. Nenhum acesso do Business Manager foi alterado.

### 2026-07-29 (sexta atualização do dia — primeira rotina semanal real)
- A primeira rotina semanal real do agente `villa-rotina-gestao-operacional` foi rodada em 2026-07-29.
- O arquivo `PAINEL_DECISAO_ROTINA_VILLA_ARAGUA.md` deixou de ser apenas template e passou a ter a primeira versão real preenchida.
- O arquivo `CRM_LEADS_VILLA_ARAGUA.md` recebeu a seção "Primeiros leads a registrar manualmente".
- A rotina foi rodada sem consultar Meta Ads.
- Nenhuma campanha SET 26 foi alterada.
- Nenhum dado de campanha foi inventado.
- Como SET 26 ainda não foi publicada, o bloco de campanhas permanece "sem dado real ainda".
- Foram registradas lacunas explícitas onde faltam dados reais, especialmente reservas, ocupação, financeiro, leads e tempo de Renildo.
- A rotina confirmou que a próxima melhoria operacional é exportar/organizar os dados das planilhas e alimentar o CRM com leads reais.

---

## 21. Atualização — Série "WhatsApp Rápido" da Recepcionista IA (Lotes 1 a 11, 2026-08-04/05)

*(Nova seção, 2026-08-05. Não substitui nem apaga nenhuma seção anterior deste arquivo — as seções 1 a 20 permanecem como registro histórico da Rodada 4 e da arquitetura de agentes/Meta Ads.)*

### 21.1 — Estado atual da Recepcionista IA

A Recepcionista IA da Villa Arágua está em **Modo Rascunho Assistido**.

Isso significa:
- a IA apenas classifica, organiza e sugere rascunhos;
- a IA nunca envia mensagem automaticamente;
- todo envio real é humano;
- Rene/Nubia revisam mensagens simples;
- Renildo decide casos sensíveis;
- a IA não confirma disponibilidade, pagamento, acesso, preço, desconto, reembolso, crédito, exceção ou responsabilidade.

### 21.2 — Marco do projeto

A série "WhatsApp Rápido" está com:
- **Lotes 1 a 9:** biblioteca validada, persistida e registrada.
- **Lote 10:** teste cego aprovado.
- **Lote 11:** rotina operacional de uso diário documentada.
- **Piloto diário assistido pronto para iniciar.**

### 21.3 — Resultado do Lote 10 (teste cego)

- Teste cego com 30 mensagens simuladas, sem indicação prévia de tema, risco ou template.
- 28 aprovadas sem ajuste.
- 2 aprovadas com ajuste de linguagem.
- 0 reprovadas.
- 100% sem falha de conteúdo, risco ou escalonamento.

Aprendizado persistido:
- Alerta interno sobre linguagem de execução autônoma, inserido na Biblioteca Oficial.
- Evitar frases como "já verifico", "vou confirmar", "vou reservar".
- Preferir "encaminho para a equipe verificar", "a equipe confirma conforme disponibilidade e regra".
- Acesso/chave/senha/endereço completo só depois de reserva confirmada e pagamento validado.

### 21.4 — Resultado do Lote 11 (rotina operacional)

- Protocolo de uso diário atualizado (`PROTOCOLO_USO_DIARIO_RASCUNHO_ASSISTIDO_VILLA_ARAGUA.md`).
- Diário de bordo do piloto criado (`DIARIO_BORDO_PILOTO_RECEPCIONISTA_IA_VILLA_ARAGUA.md`).
- Rotina operacional pronta para uso real controlado.
- Piloto sugerido: 2 semanas.
- Volume inicial seguro: 5 a 10 mensagens reais por dia.
- Foco do piloto: validar disciplina humana de revisão, não automatizar envio.

### 21.5 — Documentos centrais atuais da Recepcionista IA

1. **`MODO_RASCUNHO_ASSISTIDO_VILLA_ARAGUA.md`**
   Função: documento conceitual do modo de operação. Define que a IA apenas sugere rascunhos e nunca envia automaticamente.
2. **`PROTOCOLO_USO_DIARIO_RASCUNHO_ASSISTIDO_VILLA_ARAGUA.md`**
   Função: documento operacional. Define como Rene, Nubia e Renildo usam a IA diariamente.
3. **`DIARIO_BORDO_PILOTO_RECEPCIONISTA_IA_VILLA_ARAGUA.md`**
   Função: registro vivo do piloto diário assistido. Usado para registrar mensagens reais, ajustes, erros, escalonamentos e aprendizados.
4. **`BIBLIOTECA_OFICIAL_RECEPCIONISTA_IA_VILLA_ARAGUA.md`**
   Função: base de templates operacionais N1/N2/N3/N4, regras transversais e alertas internos.
5. **`BIBLIOTECA_COMERCIAL_RECEPCIONISTA_IA_VILLA_ARAGUA.md`**
   Função: base comercial e financeira PC-EXT para pré-venda, objeções, pagamento, cancelamento, remarcação, desconto, recorrência, indicação e pós-estadia comercial.
6. **`DADOS_OFICIAIS_ATENDIMENTO_VILLA_ARAGUA.md`**
   Função: fonte oficial de dados estáveis e operacionais documentados. Não deve ser alterada sem autorização explícita.
7. **`PENDENCIAS_OPERACAO_ESTADIA_VILLA_ARAGUA.md`**
   Função: lista de lacunas operacionais ainda não documentadas oficialmente.
8. **`CATALOGO_FOTOS_WHATSAPP_VILLA_ARAGUA.md`**
   Função: controle de fotos reais catalogadas que podem ser usadas no atendimento.
9. **`HISTORICO_TESTES_WHATSAPP_RAPIDO_RECEPCIONISTA_IA_VILLA_ARAGUA.md`**
   Função: registro histórico dos lotes testados, decisões tomadas, persistências e aprendizados.
10. **`MAPA_CONTROLE_ATUAL_RECEPCIONISTA_IA_VILLA_ARAGUA.md`**
    Função: diagnóstico congelado pós-Lotes 1 a 9. Não é o mapa vivo principal; é referência histórica de controle.

### 21.6 — Arquitetura humana

**IA Recepcionista**
- classifica;
- identifica risco;
- sugere template/regra;
- cria rascunho;
- aponta escalonamento;
- nunca envia;
- nunca decide;
- nunca confirma.

**Rene**
- primeira linha;
- revisa e envia N1, N2 e comercial simples;
- aciona Renildo quando houver risco, financeiro, exceção ou dúvida.

**Nubia**
- substituta de Rene;
- mesmas permissões e limites;
- atua quando Rene estiver ausente.

**Renildo**
- decisor sensível;
- aprova desconto, reembolso, crédito, abatimento, compensação, cobrança, dano, avaliação negativa, exceção, item de valor, conflito grave, caso fora da política e alterações de biblioteca/protocolo.

### 21.7 — Regras-mãe

- A IA nunca envia automaticamente.
- A IA nunca confirma disponibilidade.
- A IA nunca confirma reserva.
- A IA nunca valida pagamento.
- A IA nunca libera acesso.
- A IA nunca envia senha, chave, lock box, código, endereço completo ou instruções de entrada antes de reserva confirmada e pagamento validado.
- A IA nunca promete desconto.
- A IA nunca promete reembolso.
- A IA nunca promete crédito.
- A IA nunca promete compensação.
- A IA nunca decide cobrança, dano ou responsabilidade.
- A IA nunca negocia sob ameaça.
- A IA nunca orienta manuseio técnico perigoso.
- A IA nunca inventa política, dado oficial, horário, preço, disponibilidade ou regra.
- A IA nunca cria template ou pendência sem aprovação explícita.

### 21.8 — Escalonamento obrigatório para Renildo

Sempre vai para Renildo:
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

### 21.9 — Piloto diário assistido

A Recepcionista IA está pronta para início do piloto diário assistido.

Parâmetros:
- duração sugerida: 2 semanas;
- volume inicial: 5 a 10 mensagens reais por dia;
- foco inicial: mensagens simples e médias;
- casos sensíveis podem usar a IA como apoio, mas sempre com revisão forte e escalonamento;
- o objetivo é validar a rotina humana, não testar automação.

Entram no começo:
- dúvidas comerciais simples;
- coleta de datas/pessoas;
- orientação Pousada x Casa;
- fotos catalogadas;
- café da manhã padrão;
- check-in/check-out padrão;
- Wi-Fi simples;
- limpeza/enxoval simples;
- achados e perdidos simples;
- agradecimento pós-check-out;
- indicação de amigo;
- nova reserva sem desconto.

Ficam fora do piloto simples inicial:
- desconto;
- reembolso;
- avaliação negativa;
- cobrança/dano;
- gás;
- acesso sem pagamento validado;
- item de valor;
- conflito;
- exceção fora da política;
- envio automático.

### 21.10 — Processo de aprendizado

Todo erro ou ajuste real deve seguir o fluxo:
1. não enviar o rascunho errado;
2. corrigir manualmente;
3. registrar no Diário de Bordo;
4. classificar o tipo de erro;
5. decidir se é erro pontual, falta de template, falta de dado oficial, pendência ou regra nova;
6. só persistir depois de aprovação explícita de Renildo;
7. sempre criar backup antes de editar qualquer arquivo;
8. nunca alterar dados oficiais ou bibliotecas sem autorização.

### 21.11 — Indicadores do piloto

Acompanhar semanalmente:
- número de rascunhos usados;
- aprovados sem ajuste;
- aprovados com ajuste;
- rejeitados;
- escalonamentos para Renildo;
- principais temas;
- principais erros;
- pendências recorrentes;
- casos de risco evitados;
- tempo economizado estimado.

### 21.12 — Status final

**Status: pronto para piloto diário assistido.**

A Recepcionista IA **não** está pronta para envio automático. **Não** está pronta para integração com WhatsApp. **Não** pode operar sem revisão humana.

---

## 22. Changelog — atualização de 2026-08-05 (série "WhatsApp Rápido", Lotes 1 a 11)

- Adicionada seção 21 (Atualização — Série "WhatsApp Rápido", Lotes 1 a 11): estado atual da Recepcionista IA, marco do projeto, resultado do Lote 10 (teste cego 30/30), resultado do Lote 11 (rotina operacional), documentos centrais atualizados, arquitetura humana, regras-mãe, escalonamento obrigatório para Renildo, parâmetros do piloto diário assistido, processo de aprendizado e indicadores.
- Atualizada a seção 2 (Estado atual do projeto): notas de atualização adicionadas às linhas sobre Biblioteca Operacional, Biblioteca Comercial, Protocolo de Uso Diário e status do piloto — os valores antigos da Rodada 4 (25 templates N1-N4, 21 templates C1-C4, piloto pausado) foram marcados como históricos, sem serem apagados, com ponteiro para a seção 21 com os números atuais (10 N1 + 16 N2 + 24 N3 + 5 N4 na Biblioteca Oficial; 35 códigos PC-EXT na Biblioteca Comercial).
- Nenhuma seção existente foi apagada. Nenhum template PC-N ou PC-EXT foi criado. Nenhuma pendência nova foi criada. Nenhum arquivo além deste (`MAPA_DO_CEREBRO_IA_VILLA_ARAGUA.md`) foi alterado nesta rodada.

---

## 23. Atualização — Propagação C1–C4 canônica e primeira mensagem de campanha (06/08/2026)

*(Nova seção, 06/08/2026. Não substitui nem apaga nenhuma seção anterior deste arquivo — as seções 1 a 22 permanecem como registro histórico.)*

**Contexto:** após a Auditoria do Piloto Comercial Real de 06/08/2026, Renildo aprovou três frentes de correção pequena e controlada: (A) propagação da definição canônica de C1–C4; (B) consolidação da primeira mensagem de campanha; (C) registro factual do início do piloto no Diário de Bordo.

### 23.1 — Propagação C1–C4

A definição canônica de C1–C4 é `ARQUITETURA_DO_SISTEMA_COMERCIAL_VILLA_ARAGUA.md`, seção 5 (vigente desde 05/08/2026): C1 = atendimento simples; C2 = atendimento comercial normal (qualificação, preço e orçamento normais); C3 = desconto, condição especial, exceção e negociação sensível; C4 = conflito ou risco grave.

Nesta rodada, essa definição foi propagada para os arquivos que ainda usavam a classificação anterior (C3 = orçamento/disponibilidade; C4 = desconto/negociação):
- `MATRIZ_ROTEAMENTO_AGENTES_VILLA_ARAGUA.md` — seção 6 (tabela e regras comerciais), seção 11 (exemplos de mensagem mista) e seção 13 (Exemplos 1 e 4) corrigidos.
- `.claude/agents/villa-orquestrador-triagem.md` — bloco "Use C1–C4 para comercial" reescrito com a definição canônica e referência explícita à Arquitetura.
- `.claude/agents/villa-recepcionista-rascunho.md` — passo 3 do fluxo obrigatório passou a citar a Arquitetura como fonte da classificação C1–C4.
- `teste_regressao_biblioteca_comercial.py` — reescrito para verificar os 22 códigos e blocos atuais da Biblioteca Comercial (C1: 5, C2: 11, C3: 5, C4: 1), com as frases de checagem atualizadas para o texto vigente. Resultado após a correção: **20/20 checagens aprovadas.**
- Este arquivo (`MAPA_DO_CEREBRO_IA_VILLA_ARAGUA.md`) — linha da seção 4.2 (Biblioteca Comercial) anotada, sem apagar o histórico.
- `MAPA_DO_CEREBRO_COMERCIAL_VILLA_ARAGUA.md` — seções 4 e 6 corrigidas (ver changelog daquele mapa).

**Buscas negativas realizadas após a edição** (confirmando ausência da semântica antiga fora de registro histórico/changelog explicitamente rotulado): nenhuma ocorrência de orçamento normal classificado como C3, nenhuma ocorrência de desconto classificado como C4, e nenhuma ocorrência de conflito grave classificado abaixo de C4, nos arquivos listados acima.

**Não alterados nesta rodada** (fora do escopo explícito aprovado por Renildo): `BIBLIOTECA_COMERCIAL_RECEPCIONISTA_IA_VILLA_ARAGUA.md` e `ARQUITETURA_DO_SISTEMA_COMERCIAL_VILLA_ARAGUA.md` já estavam alinhados à definição canônica (nenhuma mudança necessária); documentos históricos de rodadas anteriores (`RODADA_CORRECAO_V1_AGENTES_VILLA_ARAGUA.md`, `DEFINICAO_AGENTES_VILLA_ARAGUA_IA.md`, `RESULTADO_TESTE_AGENTES_RASCUNHO_ASSISTIDO_VILLA_ARAGUA_IA.md` e a cópia de agentes em `AGENTES IA/villa-aragua-claude-code-agents/.claude/agents/`) permanecem com a semântica antiga, como registro histórico — não fazem parte da lista mínima aprovada para esta rodada.

### 23.2 — Primeira mensagem de campanha

Regra oficial consolidada: a campanha/origem é contexto comercial conhecido — antes de perguntar qualquer coisa, ler Produto, Período, Campanha e dados já enviados pelo lead, e perguntar apenas o dado realmente faltante. Implementada em `TEMPLATES_OPERACIONAIS_QL_C_VILLA_ARAGUA.md` (`T-QL1-ORIGEM-POUSADA-01`/`T-QL1-ORIGEM-CASA-01`, agora reconhecendo também período/datas quando a campanha já os define) — ver changelog daquele arquivo para o detalhe completo. Valores/ofertas do 7 de Setembro permanecem temporários, vinculados à campanha, e não foram transformados em template estrutural permanente.

### 23.3 — Diário de Bordo

`DIARIO_BORDO_PILOTO_RECEPCIONISTA_IA_VILLA_ARAGUA.md` recebeu registro factual do início do piloto real em 06/08/2026, separando fatos observados, aprendizados já confirmados (compatíveis com regras já oficiais) e hipóteses em teste (imagem institucional, imagem em follow-up, imagem de despedida, sequência emocional de imagens, follow-up de redirecionamento de datas, templates sazonais) — nenhuma hipótese foi transformada em regra oficial.

### 23.4 — Limites preservados

Nenhum campo novo no CRM. Nenhuma `BIBLIOTECA_VISUAL_VILLA_ARAGUA.md` criada. Nenhuma hipótese visual formalizada. Nenhum novo estágio, nível QL ou cadência criado. Nenhum Playbook criado. WhatsApp continua desconectado, nenhuma automação ativada, nenhuma ampliação de autonomia da Recepcionista IA.

Backup de todos os arquivos editados nesta rodada criado em `BACKUP_ANTES_PROPAGACAO_C1C4_PRIMEIRA_MENSAGEM_2026-08-06/` antes de qualquer edição. Aprovação: Renildo.
</content>
