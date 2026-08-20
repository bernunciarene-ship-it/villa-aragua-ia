# CONSOLIDAÇÃO DAS PENDÊNCIAS — RODADA 1.5

Villa Arágua IA

## 1. Contexto

A Rodada 1 dos testes manuais da Recepcionista IA foi concluída com **15 temas testados** e **495 perguntas simuladas, todas aprovadas** (0 reprovadas no fechamento final). Ao longo do processo, três regras críticas foram criadas ou reforçadas para fortalecer a segurança da IA: **11B** (acesso), **11C** (suspeita de golpe/pagamento) e **16B/15B** (hóspede irritado).

Durante os testes, várias perguntas revelaram **lacunas de dado** — situações em que a IA respondeu com segurança (sem inventar, sem prometer, sem confirmar algo não documentado), mas onde falta uma decisão comercial ou operacional de Renildo para tornar a resposta mais precisa. Essas lacunas foram todas registradas no `PENDENCIAS_RENILDO_RODADA_1_VILLA_ARAGUA_IA.md`.

Este documento organiza essas pendências para que Renildo possa decidir com clareza **antes** de iniciar a Rodada 2 — Vendas e Conversão, que exige um nível maior de precisão comercial do que a Rodada 1 (focada em segurança operacional).

**Nenhuma pendência é resolvida neste documento.** Nenhuma regra nova foi criada. Nenhum arquivo operacional foi alterado.

---

## 2. Objetivo da Rodada 1.5

A Rodada 1.5 serve para:

- separar as pendências em críticas, médias e baixas;
- identificar quais decisões impactam venda, operação e promessa da IA;
- preparar Renildo para responder às decisões principais de forma objetiva;
- transformar **apenas** as decisões aprovadas em dados oficiais depois (em rodadas futuras, não nesta);
- evitar que a Rodada 2 teste conversão e vendas com dados comerciais ainda incompletos (ex.: preço de early check-in, taxa de limpeza da Casa, forma de pagamento).

---

## 3. Classificação geral das pendências

### 3.1 Pendências críticas antes da Rodada 2

Afetam diretamente venda, preço, promessa comercial, operação ou risco de conflito com o hóspede.

| Pendência | Por que é crítica | Decisão necessária de Renildo | Arquivos que serão atualizados depois |
|---|---|---|---|
| Taxa de limpeza e limpeza extra da Casa Arágua | Apareceu repetidamente em 3+ temas de teste (desconto, cancelamento da Casa, regras da Casa); afeta o valor final de venda e o que a IA pode confirmar ao negociar a Casa | Existe taxa separada? Valor? Obrigatória? Incluída na diária ou à parte? É devolvida em caso de cancelamento? Como funciona a limpeza extra durante a estadia (preço, disponibilidade)? | `DADOS_OFICIAIS`, `ROTEIRO`, `PROMPT`, `GUIA_DIGITAL` |
| Formas de pagamento (cartão parcelado, condição de entrada) | Impacta diretamente a conversão — o hóspede precisa saber como pode pagar antes de fechar reserva | A Villa aceita cartão? Em quantas vezes? Qual a condição mínima de entrada aceita? | mesmos acima |
| Remarcação, crédito futuro, redução de diárias, transferência de reserva, força maior | A política-base de cancelamento (7/21 dias, 90%) já está validada, mas sem esses detalhes a IA sempre escala — pode gerar fricção em negociações de venda ou retenção | Como funciona remarcação na prática (disponibilidade, diferença de valor)? Existe crédito futuro? Redução de diárias? Transferência para terceiro? Exceção por força maior/doença? | mesmos acima |
| Early check-in, late check-out, bagagem e uso de áreas antes/depois da estadia | Toda venda envolve expectativa de chegada/saída; bem definido, pode virar argumento comercial ("entrada antecipada mediante disponibilidade") em vez de fonte de atrito | Existe cobrança para early/late? É sempre mediante disponibilidade? Pode deixar bagagem antes/depois? Pode usar piscina/churrasqueira/café fora do período da estadia? | mesmos acima |
| Café da manhã da Casa Arágua (pacote) e restrições alimentares mais sérias | Café é diferencial comercial forte da Pousada; um pacote formal para a Casa é oportunidade de receita. Restrições alimentares (sem glúten, sem lactose, vegano, alergia) podem decidir o fechamento de vendas para famílias/grupos | Existe pacote de café para a Casa (valor, condições, antecedência)? Existe processo formal para restrições alimentares mais sérias? | mesmos acima |
| Regras de visitantes, festas, eventos e fornecedores externos | Pode virar oportunidade comercial (pequenos eventos na Casa) ou risco de conflito se não estiver claro antes de vender a Casa para esse público | A Casa permite ensaio fotográfico, casamento pequeno, DJ, fornecedor externo? Existe taxa de evento/visitante/caução? | mesmos acima |
| Acesso da Casa Arágua — fechadura eletrônica, lock box, senha, chave, fluxo real | É a promessa operacional mais sensível ao vender a Casa como "acesso independente"; ainda em fase de planejamento/instalação física (pendência de origem anterior à Rodada 1, registrada em `PENDENCIAS_CRITICAS_OPERACAO_REAL_VILLA_ARAGUA.md`, mas com impacto direto na comunicação comercial) | Qual o modelo da fechadura? Previsão de instalação? O lock box de apoio já tem localização definida? | mesmos acima + `PENDENCIAS_CRITICAS_OPERACAO_REAL_VILLA_ARAGUA.md` (fonte original) |
| Fluxo técnico mínimo para Wi-Fi, energia, ar-condicionado e piscina | Hoje a IA só escala (comportamento seguro), mas sem nenhum passo básico real para orientar o hóspede — pode prejudicar a experiência mesmo antes de qualquer venda. A referência cruzada quebrada ao Playbook já foi corrigida, mas o conteúdo técnico em si ainda não existe | Formalizar (ou não) o conteúdo de `OPERACAO/PROBLEMAS E SOLUÇÕES.docx` na base da IA; decidir o futuro do `PLAYBOOK_ATENDIMENTO_WHATSAPP.md` (atualizar, arquivar ou substituir) | `ROTEIRO`, `PROMPT` (+ auditoria do Playbook, sem alterá-lo agora) |

### 3.2 Pendências médias

Melhoram clareza comercial e experiência, mas não travam a Rodada 2 — a IA já responde com segurança dizendo "preciso confirmar".

| Pendência | Impacto | Decisão necessária de Renildo | Pode esperar? |
|---|---|---|---|
| Detalhes da churrasqueira da Casa Arágua (horário, carvão, limpeza, taxa) | Clareza operacional/comercial da Casa | Segue o mesmo horário da Pousada? Carvão por conta do hóspede? Há taxa? Quem limpa? | Sim |
| Utensílios de churrasqueira (grelha, espetos, pegador, etc.) | Detalhe de venda | Quais itens são fornecidos na Casa? | Sim |
| Estacionamento da Casa: garagem coberta ou área aberta | Pequena expectativa visual/comercial | Confirmar o tipo de estacionamento | Sim |
| Lavanderia própria ou máquina de lavar na Casa | Conveniência para estadias longas | Confirmar existência | Sim |
| Quantidade de berços portáteis | Relevante para famílias com mais de um bebê | Confirmar quantidade disponível | Sim |
| Cama extra, colchão extra ou sofá-cama extra | Conforto adicional para grupos dentro da capacidade | Existe essa opção? | Sim |
| Itens de bebê: cadeira de alimentação, banheira | Diferencial para famílias | Existem esses itens? | Sim |
| Cardápio detalhado do café da manhã / porções por bandeja | Clareza de venda (já coberto por resposta segura) | Formalizar cardápio, se quiser usar como diferencial | Sim |
| Detalhes finos da política pet (espécies, peso, circulação em áreas) | Clareza para hóspedes com pet | Confirmar gatos/outras espécies, limite de kg, áreas permitidas | Sim |
| Supermercado maior próximo | Informação de conveniência | Confirmar nome/distância | Sim |

*Nota: "deixar bagagem antes do check-in" já está coberta pela pendência crítica de early/late check-out (seção 3.1) — não duplicada aqui.*

### 3.3 Pendências baixas

Detalhes úteis, mas que não travam venda nem operação imediata.

| Pendência | Uso provável | Resposta atual segura da IA | Prioridade |
|---|---|---|---|
| Carregador para carro elétrico | Raro, público de nicho | Reconhece o limite, direciona ao WhatsApp oficial | Baixa |
| Desconto para morador de Bombinhas | Raro, público muito específico | Aplica regra geral de desconto (nunca concede sozinha) | Baixa |
| Convênio formal com passeio de barco | Ocasional, pergunta de concierge | Reconhece o limite, não inventa parceria oficial | Baixa |
| Transfer do aeroporto | Ocasional | Reconhece o limite | Baixa |
| Restaurante próprio na Pousada | Já resolvido por resposta segura (negativa bem estabelecida) | Já segura — formalizar apenas se quiser eliminar qualquer ambiguidade | Baixa |
| Kit pet detalhado (caminha, comedouro) | Baixo, maioria traz o próprio | Reconhece o limite | Baixa |
| Proteção física em escada/mezanino | Pergunta pontual de pais cautelosos | Já segura, orientação verbal aplicada corretamente | Baixa |
| Eventos raros e não recorrentes (casamento pequeno, ensaio fotográfico específico) | Raro, caso a caso | Já segura via escalonamento para a equipe | Baixa (a política *geral* de eventos/visitantes está em 3.1 — aqui trata-se apenas da ocorrência pontual e rara) |

---

## 4. Perguntas prioritárias para Renildo responder agora

### 4.1 Casa Arágua
- Existe taxa de limpeza? Valor? Obrigatória? Devolvida em cancelamento?
- Há limpeza durante a estadia? Como funciona a limpeza extra (preço, disponibilidade)?
- Existe pacote de café da manhã? Valor e condições?
- Como funciona o acesso: fechadura eletrônica, chave, senha, lock box — e qual a previsão real de instalação?
- Detalhes da churrasqueira: horário, carvão, utensílios, taxa, limpeza
- Existe máquina de lavar ou lavanderia própria?
- O estacionamento é garagem coberta ou área aberta?
- Eventos e fornecedores externos são permitidos? Em que condição?
- Visitantes: alguma regra específica além da autorização prévia geral?
- Capacidade: confirmar que não há exceção possível acima de 6 pessoas (já validado como regra — apenas formalizar oficialmente que não haverá revisão)

### 4.2 Pagamento, reserva e cancelamento
- Aceita cartão? Parcelamento em quantas vezes?
- Aceita Pix como forma principal? Alguma condição especial?
- É possível pagar tudo apenas no check-in?
- Qual a condição mínima de entrada para confirmar reserva?
- Como funciona remarcação (disponibilidade, diferença de valor)?
- Existe crédito futuro em vez de devolução?
- É possível transferir a reserva para outra pessoa?
- Existe flexibilidade por doença/força maior?
- É possível reduzir diárias de uma reserva já feita?

### 4.3 Check-in, check-out e uso de áreas
- Early check-in tem custo? Sempre mediante disponibilidade?
- Late check-out tem custo? Mesma lógica?
- Existe tolerância oficial de horário?
- Pode deixar bagagem antes do check-in ou depois do check-out?
- Pode usar piscina, churrasqueira ou tomar café antes do check-in ou depois do check-out?

### 4.4 Café da manhã
- Qual cardápio pode ser mencionado com segurança pela IA?
- Existe processo formal para restrições alimentares (sem glúten, sem lactose, vegano, alergias)?
- Existe horário especial ou exceção à faixa 8h-10h?
- Existe (ou pode existir) café vendido como pacote para a Casa Arágua?

### 4.5 Pet, crianças e famílias
- Existe limite de peso (kg) para "pet pequeno"?
- A regra de pet inclui gatos e outras espécies?
- Quais áreas permitem ou restringem a presença de pet?
- Quantos berços portáteis existem?
- Existe opção de cama extra, colchão extra ou sofá-cama?
- Existe cadeira de alimentação ou banheira de bebê?
- Existe alguma proteção física em escada/mezanino além da orientação verbal?

### 4.6 Visitantes, festas e silêncio
- Como diferenciar visitante social de entregador/prestador rápido?
- Fornecedores externos (fotógrafo, decorador, DJ, churrasqueiro) podem entrar? Em que condição?
- A Casa permite ensaio fotográfico ou casamento pequeno?
- Existe taxa de visitante ou de evento? Existe caução?
- Visitante pode estacionar em vaga da Casa ou da Pousada?

---

## 5. O que precisa virar dado oficial depois da decisão

| Decisão de Renildo | Arquivo oficial a atualizar | Precisa atualizar prompt? | Precisa reteste? |
|---|---|---|---|
| Taxa de limpeza e limpeza extra da Casa | `DADOS_OFICIAIS`, `ROTEIRO`, `GUIA_DIGITAL` | Sim (`PROMPT`) | ✅ Concluído — taxa de limpeza, limpeza extra e café retestados em "Regras da Casa Arágua" (`RESULTADO_TESTE_REGRAS_DA_CASA_ARAGUA_RODADA_1...md`); acesso/fechadura/lock box da Casa também retestado em 2026-07-10 (ver linha "Acesso da Casa" abaixo) |
| Formas de pagamento / cartão parcelado | `DADOS_OFICIAIS`, `ROTEIRO` | Sim | ✅ Reteste concluído em 2026-07-10 — `RESULTADO_TESTE_GOLPE_PAGAMENTO_RODADA_1_RECEPCIONISTA_IA_VILLA_ARAGUA.md` |
| Remarcação, crédito futuro, transferência, força maior | `DADOS_OFICIAIS`, `ROTEIRO` | Sim | ✅ Reteste concluído em 2026-07-10 — `RESULTADO_TESTE_CANCELAMENTO_POUSADA_RODADA_1...md` e `RESULTADO_TESTE_CANCELAMENTO_CASA_ARAGUA_RODADA_1...md` |
| Early check-in, late check-out, bagagem, uso de áreas | `DADOS_OFICIAIS`, `ROTEIRO`, `GUIA_DIGITAL` | Sim | Sim — reteste check-in/check-out |
| Café da manhã da Casa e restrições alimentares | `DADOS_OFICIAIS`, `ROTEIRO`, `GUIA_DIGITAL` | Sim | ✅ Reteste concluído em 2026-07-10 — `RESULTADO_TESTE_CAFE_DA_MANHA_RODADA_1_RECEPCIONISTA_IA_VILLA_ARAGUA.md` (restam pendências pontuais: porções por bandeja e unidade de tempo do valor R$ 80 da Casa) |
| Visitantes, festas, eventos, fornecedores externos | `DADOS_OFICIAIS`, `ROTEIRO`, `GUIA_DIGITAL` | Sim | ✅ Reteste concluído em 2026-07-10 — `RESULTADO_TESTE_VISITANTES_FESTAS_SILENCIO_RODADA_1_RECEPCIONISTA_IA_VILLA_ARAGUA.md` (resta pendência pontual: limite de frequência de visitas) |
| Acesso da Casa (fechadura/lock box/senha) | `DADOS_OFICIAIS`, `ROTEIRO`, `GUIA_DIGITAL` | Sim | ✅ Reteste concluído em 2026-07-10 — `RESULTADO_TESTE_ACESSO_LOCK_BOX_RODADA_1_RECEPCIONISTA_IA_VILLA_ARAGUA.md` (confirma que o acesso da Casa segue "planejado/em definição", nunca implantado) |
| Fluxo técnico Wi-Fi/energia/ar-condicionado/piscina | `ROTEIRO`, `PROMPT` | Sim | Sim — reteste problema técnico |
| Pendências médias (churrasqueira, estacionamento, lavanderia, berço, cama extra, itens de bebê, pet fino, café detalhado) | `DADOS_OFICIAIS`, `ROTEIRO`, `PROMPT`, `GUIA_DIGITAL`, conforme o item | Depende do item | ✅ Retestes pontuais concluídos em 2026-07-12 — `RESULTADO_TESTE_CHURRASQUEIRA_RODADA_1...md`, `RESULTADO_TESTE_PET_RODADA_1...md`, `RESULTADO_TESTE_CRIANCAS_CAPACIDADE_CAMA_EXTRA_RODADA_1...md` (restam pendências pontuais registradas em cada arquivo) |
| Pendências baixas | Atualização simples quando confirmado, sem urgência | Depende do item | Não obrigatório — pode validar no próximo teste geral do tema |

Sempre que uma decisão for incorporada, também atualizar `ROTEIRO_TESTE_MANUAL_RECEPCIONISTA_IA_VILLA_ARAGUA.md` (registro do reteste) e `PENDENCIAS_RENILDO_RODADA_1_VILLA_ARAGUA_IA.md` (remover ou marcar a pendência como resolvida).

---

## 6. Retestes necessários após resolver pendências

- ~~Reteste Casa Arágua — taxa de limpeza, café, limpeza extra~~ — ✅ concluído em 2026-07-10 (`RESULTADO_TESTE_REGRAS_DA_CASA_ARAGUA_RODADA_1_RECEPCIONISTA_IA_VILLA_ARAGUA.md`)
- ~~Reteste acesso/fechadura/lock box da Casa Arágua~~ — ✅ concluído em 2026-07-10 (`RESULTADO_TESTE_ACESSO_LOCK_BOX_RODADA_1_RECEPCIONISTA_IA_VILLA_ARAGUA.md`)
- ~~Reteste pagamento e condição de entrada~~ — ✅ concluído em 2026-07-10 (`RESULTADO_TESTE_GOLPE_PAGAMENTO_RODADA_1_RECEPCIONISTA_IA_VILLA_ARAGUA.md`)
- ~~Reteste cancelamento (Pousada e Casa)~~ — ✅ concluído em 2026-07-10 (`RESULTADO_TESTE_CANCELAMENTO_POUSADA_RODADA_1...md`, `RESULTADO_TESTE_CANCELAMENTO_CASA_ARAGUA_RODADA_1...md`)
- Reteste early check-in / late check-out / bagagem (fora do escopo desta execução — tema 12, ainda não iniciado)
- ~~Reteste café da manhã e restrições alimentares~~ — ✅ concluído em 2026-07-10 (`RESULTADO_TESTE_CAFE_DA_MANHA_RODADA_1_RECEPCIONISTA_IA_VILLA_ARAGUA.md`)
- ~~Reteste visitantes / eventos / fornecedores~~ — ✅ concluído em 2026-07-10 (`RESULTADO_TESTE_VISITANTES_FESTAS_SILENCIO_RODADA_1_RECEPCIONISTA_IA_VILLA_ARAGUA.md`)
- ⚠️ Reteste fluxo técnico básico — **parcialmente concluído**: Wi-Fi retestado em 2026-07-12 (`RESULTADO_TESTE_WIFI_CASA_ARAGUA_RODADA_1...md`); energia, ar-condicionado e piscina continuam sem reteste dedicado (não fazem parte de nenhum dos 15 temas originais da Rodada 1 — avaliar se merecem tema próprio em rodada futura)
- Reteste comercial geral da Casa Arágua antes da Rodada 2 (ainda pendente — recomenda-se revisão consolidada de todos os arquivos `RESULTADO_TESTE_*` relacionados à Casa antes da Rodada 2)

---

## 7. Recomendação de sequência

1. Consolidar pendências neste arquivo (concluído).
2. Renildo responder primeiro as pendências críticas (seção 3.1 / seção 4).
3. Atualizar `DADOS_OFICIAIS_ATENDIMENTO_VILLA_ARAGUA.md` com as decisões.
4. Atualizar `ROTEIRO_RECEPCIONISTA_IA.md`, `PROMPT_RECEPCIONISTA_IA_WHATSAPP.md` e `GUIA_DIGITAL_HOSPEDE_VILLA_ARAGUA.md` apenas onde necessário.
5. Fazer reteste rápido das decisões incorporadas (seção 6).
6. Só depois iniciar a Rodada 2 — Vendas e Conversão.

---

## 8. Conclusão

A Recepcionista IA já está segura para não inventar respostas, não prometer exceções e não confundir Casa Arágua com Pousada Arágua — isso foi validado em 495 perguntas na Rodada 1. Mas a Rodada 2 exige mais **precisão comercial**: preço, forma de pagamento, pacotes, e diferenciais de venda não podem ficar apenas como "vou verificar com a equipe" se o objetivo é medir conversão de forma realista.

Por isso, as pendências críticas listadas na seção 3.1 devem ser decididas por Renildo **antes** dos testes de conversão da Rodada 2.

---

## Status

Arquivo de consolidação criado em 2026-07-04, a partir da leitura de `PENDENCIAS_RENILDO_RODADA_1_VILLA_ARAGUA_IA.md`, `ROTEIRO_TESTE_MANUAL_RECEPCIONISTA_IA_VILLA_ARAGUA.md`, `DADOS_OFICIAIS_ATENDIMENTO_VILLA_ARAGUA.md`, `ROTEIRO_RECEPCIONISTA_IA.md`, `PROMPT_RECEPCIONISTA_IA_WHATSAPP.md` e `GUIA_DIGITAL_HOSPEDE_VILLA_ARAGUA.md`. Nenhuma pendência foi resolvida, nenhuma regra nova foi criada, e nenhum arquivo existente foi alterado nesta etapa.
