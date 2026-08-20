# Mapa de Controle Atual — Recepcionista IA Villa Arágua

*(Diagnóstico baseado no estado real dos arquivos após o fechamento dos Lotes 1 a 9 da série "WhatsApp Rápido". Registrado em 04/08/2026.)*

## 1. Resumo executivo

Depois de 9 lotes de teste (mais de 150 mensagens simuladas cobrindo pré-venda, estadia, pós-estadia e um lote transversal de pressão/contradição), a Recepcionista IA da Villa Arágua está em **fase madura de triagem**. A base hoje conta com **90 templates persistidos** (10 N1 + 16 N2 + 24 N3 + 5 N4 na Biblioteca Oficial + 35 na Biblioteca Comercial), 4 regras transversais, 3 alertas internos e uma nota cruzada entre templates de risco reputacional/financeiro. O Lote 9 confirmou que essa base já segura combinações complexas (pressão comercial, contradição, mistura de idiomas, múltiplos temas) sem precisar de templates novos — sinal de que a cobertura de conteúdo chegou a um ponto de estabilidade.

Ela **ainda não está pronta para envio automático** (isso nunca é o objetivo do Modo Rascunho Assistido) e **ainda não passou por teste cego** (todos os testes até aqui foram feitos avisando o tema do lote). Está pronta para **uso diário assistido em piloto controlado**, com Rene/Nubia/Renildo revisando cada rascunho antes de enviar, e o próximo passo natural é justamente validar essa maturidade com um teste cego antes de expandir o volume de uso real.

## 2. Cobertura por etapa da jornada do hóspede

| Etapa | Status | Principais templates/regras | Risco atual | Observação |
|---|---|---|---|---|
| Pré-venda | Bem coberto | `PC-C1/C2-XX`, `PC-N1-06/07/08/09/10` | Baixo | Base original + ajustes de tom |
| Objeção de preço | Bem coberto | `PC-EXT-18/19` | Baixo-médio | Diferencia OTA de outra pousada; nunca equipara automaticamente |
| OTA/Booking/Airbnb | Bem coberto | `PC-EXT-19` | Médio | Exige print com condições completas antes de qualquer comparação |
| Parcelamento/pagamento | Bem coberto | `PC-EXT-20`, item 51/52 | Médio | Sem boleto; 6x/10x com 7% de acréscimo; nunca "sem juros" |
| Pré-reserva | Bem coberto | `PC-EXT-21`, item 52 | Médio | Nunca segura data sem sinal validado |
| Composição de hóspedes | Bem coberto | `PC-EXT-31`, Regra 19 | Médio | Nunca fecha orçamento antes da composição final |
| Pousada x Casa | Bem coberto | Regra 18/20/22, `PC-EXT-03/04` | Médio | Travas de capacidade e configuração de camas bem testadas |
| Fotos | Bem coberto | `PC-EXT-13/14/22` | Baixo | Apenas fotos catalogadas; nunca "melhor" absoluto |
| Check-in | Bem coberto | `PC-N2-01/09`, `PC-N3-02/03` | Baixo | Horário 15h-22h consolidado |
| Chegada fora do padrão | Coberto com ressalva | `PC-N3-02` + complemento madrugada | Médio-alto | Madrugada sempre escala com prioridade |
| Acesso/senha/chave | Bem coberto | `PC-N3-01/12`, `PC-N4-01`, item 30 | Alto (mitigado) | Nunca envia dado sensível antes de pagamento validado |
| Estadia (dúvidas gerais) | Bem coberto | `PC-N1-08/09`, `PC-N2-XX` | Baixo | — |
| Café da manhã | Bem coberto | `PC-N2-04`, `PC-N3-08` | Baixo | Inclui variante "café mais cedo" |
| Limpeza/enxoval | Bem coberto | `PC-N2-04/06` | Baixo | Sem troca diária automática documentada |
| Manutenção | Bem coberto | `PC-N3-15/16/19` | Médio-alto | Nunca prazo/SLA; gás tratado como emergência |
| Wi-Fi | Bem coberto | `PC-N2-10` | Baixo | — |
| Piscina/churrasqueira | Coberto com ressalva | `PC-N2-08/13`, item 35 | Médio | Piscina privativa da Casa: horário pendente |
| Visitantes | Bem coberto | `PC-N3-04` | Médio | Nunca automático, mesmo autorizado |
| Barulho/conflito | Bem coberto | `PC-N3-17`, `PC-N4-04` | Alto (mitigado) | Confronto entre hóspedes é N4 |
| Reclamação durante estadia | Bem coberto | `PC-N3-10/20/21` | Alto (mitigado) | Reclamação repetida tem reconhecimento explícito |
| Cancelamento/remarcação | Bem coberto | `PC-EXT-23`, `PC-N3-09` | Médio-alto | Chuva não é motivo automático |
| Pedido financeiro | Bem coberto | `PC-EXT-33`, `PC-N3-05` | Alto (mitigado) | Sempre escala para Renildo |
| Pós-estadia (encerramento) | Bem coberto | `PC-EXT-34/35` | Baixo | — |
| Achados e perdidos | Coberto com ressalva | `PC-N2-15`, `PC-N3-22/23/24` | Médio-alto | Prazo de guarda e regra de envio ainda não documentados |
| Avaliação negativa | Bem coberto | `PC-EXT-27/33` + nota cruzada | Alto (mitigado) | Nunca negocia, nunca pede remoção |
| Nova reserva/retorno | Bem coberto | `PC-EXT-36/37/38` | Baixo-médio | Nunca desconto de fidelidade |
| Nota/recibo/comprovante | Pendente de dado oficial | `PC-N2-16` | Médio | Template declara lacuna com segurança, mas dado real ainda falta |
| Espanhol/portunhol | Bem coberto | Item 24 + regra transversal (Lote 9) | Baixo | Testado com sucesso em L9-10/11 |
| Mensagens com múltiplos temas | Bem coberto | Regra transversal (Lote 9) + protocolo de blocos | Médio | Testado com sucesso no caso mais denso do Lote 9 (L9-20) |

## 3. Temas que a IA pode rascunhar com segurança

**Comercial simples:** orientação por perfil (casal, família, criança); diferença Pousada x Casa; localização; Wi-Fi/velocidade; diferenciais (natureza, sombra); envio de fotos catalogadas; primeiro atendimento e coleta de datas/pessoas.

**Operação simples:** horário de check-in/check-out; café da manhã (padrão e mais cedo); Wi-Fi instável; reposição de item básico; piscina da Pousada; churrasqueira (coleta de dados); estacionamento (regra padrão); insetos.

**Pós-estadia simples:** agradecimento e convite à avaliação (sem insatisfação pendente); item esquecido simples (coleta de dados); nova intenção de reserva (coleta de dados); indicação de amigo.

**Dúvidas comuns:** regras da casa, silêncio, pet, capacidade documentada, parcelamento/Cielo, cancelamento padrão (sem exceção).

**Coleta de dados** (sempre sem prometer nada): composição de hóspedes, datas, produto, número da reserva, descrição de item perdido, print de OTA, motivo de cancelamento.

## 4. Temas que sempre escalam para Renildo

- Desconto, abatimento, crédito, reembolso ou compensação (qualquer contexto: durante estadia, pós-estadia, hóspede recorrente).
- Cobrança extra ou dano contestado após a saída (`PC-N4-05`).
- Avaliação negativa — ameaça, já publicada, ou combinada com pedido financeiro.
- Negociação sob pressão (comparação agressiva, urgência artificial, "fechamento condicionado a desconto").
- Item de valor esquecido ou contestação de item não localizado.
- Conflito grave / risco de confronto entre hóspedes (`PC-N4-04`).
- Exceção financeira de qualquer tipo (early check-in/late check-out tratados como exceção não são financeiros, mas se vierem acompanhados de cobrança/compensação, escalam).
- Qualquer caso fora da política documentada onde não exista template de resposta segura.
- Emergência de segurança (gás com cheiro, invasão, emergência médica) — escala em paralelo para Renildo como retaguarda.

## 5. Temas que escalam para Rene ou Nubia

- Checagem de disponibilidade real (calendário/Stays).
- Confirmação/validação de comprovante de pagamento.
- Coordenação de check-in/check-out (horários, early/late sob avaliação operacional, não financeira).
- Limpeza extra e reposição de enxoval (sob consulta).
- Ajuste de café da manhã (cedo, preferências).
- Reserva/confirmação de churrasqueira.
- Orientação de estacionamento em caso de carro extra.
- Autorização de visitantes sob consulta.
- Achados e perdidos simples (item comum, não de valor).
- Manutenção de rotina (Wi-Fi, AC, chuveiro, TV) — primeira linha antes de eventual escalonamento a Renildo se persistir.
- Dúvidas de estadia que exigem confirmação local (ex.: piscina privativa da Casa, item de cozinha disponível).

## 6. Pendências reais ainda abertas

*(Baseado exclusivamente no que está documentado em `PENDENCIAS_OPERACAO_ESTADIA_VILLA_ARAGUA.md`, seções 14 a 16 — nenhuma pendência nova inventada aqui.)*

### Pendências prioritárias
- **Tipo de documento pós-estadia (nota fiscal x recibo) e procedimento de emissão** — não documentado. É a pendência mais urgente: impede resposta completa mesmo com `PC-N2-16` já cobrindo a interação com segurança.
- **Tipo de fornecimento de gás da Casa Arágua (botijão/encanado) e procedimento oficial** — não documentado. Envolve risco de segurança; `PC-N3-16` mitiga a resposta, mas o dado de fundo falta.
- **Horário da piscina privativa da Casa Arágua** — não documentado, gera resposta sempre condicionada ("encaminho para a equipe confirmar").

### Pendências médias
- **Política de achados e perdidos (prazo de guarda) e regra de envio/custo por correio/transportadora/app** — falta definir expectativa clara para o hóspede.
- **Procedimento formal de entrada de manutenção na unidade (consentimento/coordenação)** — hoje coberto por regra de bom senso (`PC-N3-19`), mas sem procedimento formalizado.
- **Divergência sobre janela de check-out** (`CLAUDE.md` cita "8h-11h", fontes oficiais confirmam só "até 11h") — não afeta a segurança da resposta, mas é uma inconsistência documental a resolver.

### Pendências baixas
- Inventário de utensílios de cozinha da Casa Arágua.
- SLA de reposição de item básico (papel higiênico etc.).
- Política de desconto para hóspede recorrente e política formal de indicação — hoje resolvidas com "nunca prometer", o que já é seguro; formalizar é melhoria, não urgência.
- Complemento futuro ao item 68 (incluir chuveiro/água quente e TV explicitamente no fluxo técnico) — já coberto na prática por `PC-N3-15`.

## 7. Regras-mãe consolidadas

- **Modo Rascunho Assistido**: a IA nunca envia mensagem real; todo envio é feito por Rene, Nubia ou Renildo.
- Nunca confirmar disponibilidade sem checagem real.
- Nunca confirmar reserva sem pagamento/sinal validado.
- Nunca enviar senha, chave, lock box, código ou instrução de entrada antes de reserva confirmada e pagamento validado.
- Nunca prometer desconto, abatimento, crédito, reembolso ou compensação.
- Nunca decidir cobrança, dano ou responsabilidade — sempre escalar.
- Nunca negociar sob ameaça (reputacional, financeira ou de urgência artificial).
- Nunca orientar manuseio técnico perigoso (gás, elétrica).
- Mensagens com múltiplos temas priorizam o risco principal antes de qualquer outro assunto (regra transversal, Lote 9).
- Espanhol/portunhol mantêm exatamente as mesmas travas do português (regra transversal, Lote 9).
- Pousada Arágua e Casa Arágua são produtos diferentes — nunca tratados como intercambiáveis.
- Casa Arágua acima de 6 pessoas nunca é automática; configuração de camas para 5-6 pessoas nunca é cama tradicional garantida.

## 8. Pontos de atenção antes do uso real

- **IA tentar ser prestativa demais**: risco confirmado no Lote 9 (L9-20) — tendência a tentar resolver tudo de uma mensagem longa, mesmo com regra transversal de priorização já em vigor. Requer atenção humana constante nas primeiras semanas.
- **Mensagem longa com muitos temas misturados**: mitigado por regra transversal, mas ainda exige revisão humana cuidadosa — é o padrão de erro mais provável.
- **Hóspede pressionando por exceção** (early check-in, late check-out, desconto, troca de acomodação): templates seguram bem, mas o tom precisa continuar soando acolhedor, não burocrático.
- **Pedido de acesso com pagamento não validado**: maior risco de segurança único do sistema — testado e seguro, mas é o ponto que exige mais vigilância operacional real (comprovantes falsos, pressão de urgência).
- **Reclamação com ameaça de avaliação**: bem coberto, mas Renildo precisa estar disponível para responder com agilidade — o template pede escalonamento imediato, e a experiência real depende da rapidez humana.
- **Item de valor esquecido**: risco reputacional alto se a resposta demorar, mesmo estando bem coberto textualmente.
- **Nota fiscal/recibo**: única pendência que gera resposta genuinamente incompleta ao hóspede hoje ("vou encaminhar" sem prazo real) — vale decisão de Renildo com alguma urgência.
- **Casa Arágua acima da capacidade ideal**: testado exaustivamente (Lotes 3, 5, 9), mas é um ponto onde a pressão comercial (querer vender) pode tentar contornar a trava — vigilância humana constante recomendada.

## 9. Diagnóstico de prontidão

### A IA está pronta para teste cego?
**Ainda não foi testada cegamente — mas a base está pronta para esse teste.** Todos os 9 lotes até aqui informaram o tema com antecedência, o que ajuda a IA a se preparar mentalmente para o contexto. O Lote 9 (transversal, com mistura e pressão) é a evidência mais forte de que a cobertura aguenta, mas classificação sem aviso prévio de tema ainda não foi validada. Recomendação: sim, avançar para o teste cego agora — é o próximo passo lógico, não um bloqueio.

### A IA está pronta para uso diário assistido?
**Sim, em piloto controlado.** A base de 90 templates, as regras transversais e o protocolo já documentado (`MODO_RASCUNHO_ASSISTIDO_VILLA_ARAGUA.md`, `PROTOCOLO_USO_DIARIO_RASCUNHO_ASSISTIDO_VILLA_ARAGUA.md`) sustentam o uso real assistido, com Rene/Nubia/Renildo revisando cada rascunho. O piloto manual de 1-2 semanas já estava previsto nesses documentos desde a Rodada 4 — a cobertura de conteúdo hoje é significativamente maior do que quando esse protocolo foi criado.

### A IA está pronta para envio automático?
**Não.** Envio automático não está autorizado nem é o modelo do projeto — não há WhatsApp real conectado, nem Zapier/Make/API/backend conectados, por decisão explícita e reiterada em todos os lotes. A IA gera apenas rascunhos; a decisão final e o envio são sempre humanos. Mesmo com a biblioteca madura, a natureza de negócio (pagamentos, acesso físico, reputação, exceções) exige supervisão humana permanente — automação completa não é uma meta de curto prazo deste projeto.

## 10. Próximos lotes recomendados

### Lote 10 — Teste cego de atendimento real
**Objetivo:** rodar 30 mensagens simuladas sem avisar o tema, misturando pré-venda, operação, reclamação, pós-estadia, pressão, espanhol, dados confusos e exceções.
**Resultado esperado:** verificar se a IA classifica corretamente (nível de risco, produto, escalonamento) sem saber previamente qual lote/tema está sendo testado — é o teste mais próximo de uso real.
**Prioridade:** alta.

### Lote 11 — Rotina operacional de uso
**Objetivo:** transformar a Recepcionista IA em rotina prática de uso por Rene, Nubia e Renildo — fila de revisão, quem aprova o quê, como registrar erro, como atualizar biblioteca, como escalar, como medir qualidade.
**Resultado esperado:** procedimento operacional formalizado para o dia a dia.
**Prioridade:** alta, mas em segundo lugar.

**Qual deve vir primeiro: Lote 10.** A rotina operacional (Lote 11) só vale a pena formalizar depois de confirmar, via teste cego, que a IA classifica corretamente sem o "aviso prévio" que todos os lotes anteriores deram. Além disso, `PROTOCOLO_USO_DIARIO_RASCUNHO_ASSISTIDO_VILLA_ARAGUA.md` já existe desde a Rodada 4 como rascunho inicial de rotina — o Lote 11 deve atualizar e expandir esse documento à luz da biblioteca atual (muito maior), não criá-lo do zero. Fazer isso depois do teste cego evita retrabalho caso o Lote 10 revele ajustes de classificação necessários.

## 11. Quadro final de controle

| Área | Status atual | Risco | Próxima ação |
|---|---|---|---|
| Comercial | Maduro | Baixo-médio | Teste cego (Lote 10) |
| Operação | Maduro | Baixo-médio | Teste cego (Lote 10) |
| Financeiro | Bem contido (sempre escala) | Médio-alto | Manter escalonamento rígido para Renildo |
| Segurança/acesso | Bem contido | Alto (mitigado) | Vigilância humana contínua no piloto |
| Reclamações | Maduro | Médio-alto | Monitorar tempo de resposta humana |
| Pós-estadia | Maduro | Médio | Definir procedimento de nota fiscal |
| Casa Arágua | Bem coberto, com travas testadas | Médio | Manter vigilância sobre pressão comercial |
| Pousada Arágua | Bem coberto | Baixo | — |
| Espanhol/portunhol | Bem coberto e testado (Lote 9) | Baixo | — |
| Aprendizado/manual | Ativo (9 lotes documentados) | Baixo | Formalizar rotina de atualização (Lote 11) |
| Uso diário | Pronto para piloto assistido | Médio (depende de disciplina humana) | Rodar Lote 10, depois Lote 11 |

## 12. Conclusão

Em nove lotes, a Villa Arágua construiu uma biblioteca de 90 templates mais quatro regras transversais que já resistem a pressão comercial, ameaça reputacional, contradição, mistura de temas e troca de idioma — o tipo de teste que normalmente expõe falhas de um sistema de atendimento ainda não apareceu no Lote 9. O que falta não é mais conteúdo: é validar essa maturidade num teste sem aviso prévio (Lote 10) e depois transformar tudo isso em rotina viva de uso diário (Lote 11), apoiando-se no protocolo que já existe desde a Rodada 4.

A decisão que cabe a Renildo agora é dupla: primeiro, aprovar o Lote 10 (teste cego) como próximo passo, e segundo, decidir com alguma urgência o procedimento de nota fiscal/recibo — é a única pendência que hoje deixa a IA genuinamente incompleta diante de um pedido real do hóspede, todas as outras já têm resposta segura mesmo sem o dado final definido.
