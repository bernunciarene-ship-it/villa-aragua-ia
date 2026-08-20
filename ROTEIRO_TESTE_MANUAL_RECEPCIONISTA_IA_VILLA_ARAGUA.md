# Roteiro de Teste Manual — Recepcionista IA Villa Arágua

Roteiro simples para Renildo testar manualmente a Recepcionista IA da Villa Arágua dentro do Claude, sem WhatsApp API, sem WhatsApp secundário e sem automação.

## Premissas

- O teste será feito manualmente por Renildo.
- Renildo fará perguntas simulando hóspedes reais.
- Renildo irá ler as respostas da IA.
- Se encontrar erro, dúvida, tom inadequado ou regra confusa, irá registrar o caso para ajuste posterior.
- Não haverá envio automático de mensagens.
- Não haverá integração com WhatsApp API.
- Não haverá uso de WhatsApp secundário nesta fase.
- O WhatsApp oficial 47 99201-4117 continua protegido.

---

## 1. Como testar

1. Abrir o Claude com o cérebro da Villa Arágua.
2. Fazer uma pergunta como se fosse hóspede.
3. Pedir para responder como Recepcionista IA da Villa Arágua.
4. Ler a resposta.
5. Avaliar se está correta, humana, objetiva e segura.
6. Se estiver boa, marcar como aprovada.
7. Se tiver problema, copiar a pergunta e a resposta para ajuste futuro.

## 2. Critérios de avaliação

Para cada resposta, Renildo deve observar:

- A resposta está correta?
- Está com tom humano e acolhedor?
- Está objetiva?
- Ajuda a vender quando existe oportunidade?
- Não inventa informação?
- Não promete algo que ainda não está implantado?
- Não confirma algo que depende da equipe?
- Não usa o WhatsApp antigo?
- Não contradiz o Guia Digital, Termos, Política ou Dados Oficiais?
- Encaminha para humano quando necessário?

## 3. Situações prioritárias para testar

| # | Pergunta | Aprovada? |
|---|---|---|
| 1 | Vocês aceitam pet? Tem taxa? | [ ] |
| 2 | Posso levar pet grande? | [ ] |
| 3 | Como funciona o café da manhã? | [ ] |
| 4 | Posso pedir café sem leite? | [ ] |
| 5 | Qual é a senha do Wi-Fi da Pousada? | [ ] |
| 6 | Qual é o Wi-Fi da Casa Arágua? | [ ] |
| 7 | Qual horário da piscina? | [ ] |
| 8 | Como reservar a churrasqueira? | [ ] |
| 9 | Posso trazer convidados para a churrasqueira? | [ ] |
| 10 | Posso receber visitantes na Casa Arágua? | [ ] |
| 11 | Como funciona o cancelamento da Pousada? | [ ] |
| 12 | Como funciona o cancelamento da Casa? | [ ] |
| 13 | Posso fazer late check-out? | [ ] |
| 14 | Posso fazer early check-in? | [ ] |
| 15 | Tem cadeira e guarda-sol na praia? | [ ] |
| 16 | Como funciona a parceria com o Moquém do Mar? | [ ] |
| 17 | Vocês fornecem toalha de praia? | [ ] |
| 18 | Posso pedir toalha extra? | [ ] |
| 19 | Tem limpeza diária? | [ ] |
| 20 | A Casa Arágua tem limpeza durante a estadia? | [ ] |
| 21 | Como faço check-in? | [ ] |
| 22 | O check-in autônomo já está funcionando? | [ ] |
| 23 | Estou com medo de golpe, como sei que é a pousada mesmo? | [ ] |
| 24 | Quero desconto. | [ ] |
| 25 | Estou irritado com um problema. | [ ] |
| 26 | Estou chegando tarde, como faço? | [ ] |
| 27 | Quero reservar para família com bebê. | [ ] |
| 28 | Somos 2 adultos e 3 crianças, qual acomodação indica? | [ ] |
| 29 | Em espanhol: "Aceptan mascotas?" | [ ] |
| 30 | Pergunta fora da base documentada. | [ ] |

## 3B. Quantidade recomendada de perguntas por tema

Para testar bem a Recepcionista IA, não basta uma pergunta por tema. Cada tema deve ser testado em camadas:

- pergunta simples;
- pergunta com detalhe;
- pergunta com exceção;
- pergunta com objeção;
- pergunta incompleta/confusa;
- pergunta com tom difícil, quando aplicável.

Classificação:

- Tema simples: 3 perguntas.
- Tema operacional importante: 5 perguntas.
- Tema comercial/crítico: 7 perguntas.
- Tema de risco: 10 perguntas.

| Tema | Quantidade recomendada | Prioridade |
|---|---:|---|
| Disponibilidade | 7 | Alta |
| Valores | 7 | Alta |
| Pet pequeno | 5 | Alta |
| Pet grande | 5 | Alta |
| Café da manhã | 5 | Média |
| Preferência no café | 5 | Média |
| Wi-Fi da Pousada | 3 | Média |
| Wi-Fi da Casa Arágua | 5 | Alta |
| Piscina | 5 | Média |
| Churrasqueira | 7 | Alta |
| Convidados externos | 7 | Alta |
| Visitantes na Casa Arágua | 7 | Alta |
| Cancelamento da Pousada | 7 | Alta |
| Cancelamento da Casa | 7 | Alta |
| No-show | 5 | Alta |
| Early check-in | 5 | Média |
| Late check-out | 5 | Média |
| Casa Arágua | 7 | Alta |
| Casal com bebê | 5 | Média |
| Família com 4 pessoas | 5 | Média |
| Família com 5 pessoas | 7 | Alta |
| Hóspede em espanhol | 7 | Alta |
| Apoio de praia Moquém do Mar | 5 | Média |
| Cadeiras e guarda-sol próprios | 5 | Média |
| Toalhas de praia | 3 | Média |
| Enxoval extra | 5 | Média |
| Troca completa de enxoval | 5 | Média |
| Hóspede desconfiado de golpe | 10 | Crítica |
| Pedido de desconto | 10 | Crítica |
| Hóspede irritado | 10 | Crítica |
| Problema de acesso | 10 | Crítica |
| Dúvida fora da base documentada | 10 | Crítica |

Resumo:

- Total ideal completo: aproximadamente 205 perguntas.
- Teste mínimo sólido: aproximadamente 100 perguntas.
- Não é necessário fazer tudo no mesmo dia.
- Renildo pode começar pelos temas críticos e depois avançar para os demais.

## 3C. Ordem recomendada de teste

Rodada 1 — Temas críticos:
- hóspede desconfiado de golpe;
- pedido de desconto;
- hóspede irritado;
- problema de acesso;
- dúvida fora da base;
- cancelamento;
- Wi-Fi da Casa;
- churrasqueira.

Rodada 2 — Operação da estadia:
- café;
- preferências do café;
- piscina;
- Moquém do Mar;
- cadeiras/guarda-sol;
- toalhas;
- enxoval.

Rodada 3 — Vendas e perfil:
- disponibilidade;
- valores;
- Casa Arágua;
- casal com bebê;
- família com 4 pessoas;
- família com 5 pessoas;
- pet.

Rodada 4 — Espanhol e exceções:
- perguntas em espanhol;
- hóspedes confusos;
- pedidos incompletos;
- situações fora da base.

## 4. Como registrar problemas

Quando uma resposta precisar de ajuste, registrar assim:

- **Pergunta feita**:
- **Resposta da IA**:
- **O que não gostei**:
- **Qual seria a resposta correta ou intenção**:
- **Arquivo que provavelmente precisa ajuste**:
  - `DADOS_OFICIAIS_ATENDIMENTO_VILLA_ARAGUA.md`
  - `ROTEIRO_RECEPCIONISTA_IA.md`
  - `PROMPT_RECEPCIONISTA_IA_WHATSAPP.md`
  - `GUIA_DIGITAL_HOSPEDE_VILLA_ARAGUA.md`
  - outro

## 5. Regra de ajuste

Sempre que Renildo encontrar um problema:
- não alterar tudo de uma vez;
- criar ajuste pontual;
- atualizar o arquivo correto;
- depois testar novamente o mesmo cenário.

## 6. Status

Roteiro criado.
Roteiro atualizado com quantidade recomendada de perguntas por tema.
Teste será manual, feito por Renildo dentro do Claude.
Sem API.
Sem WhatsApp secundário.
Sem automação.

## 7. Resultados por tema — Rodada 1 (2026-07-04)

| Tema | Perguntas testadas | Aprovadas | Reprovadas | Observação |
|---|---|---|---|---|
| Problema de acesso (e lock box) | 10 (histórico, resumo) + 26 (reconstrução 2026-07-10) | 10/10 (histórico) + 26/26 (reconstrução) | 0 | **Reconstruído em 2026-07-10** com evidência individual completa, incluindo o reteste específico de acesso/lock box da Casa Arágua que estava pendente — `RESULTADO_TESTE_ACESSO_LOCK_BOX_RODADA_1_RECEPCIONISTA_IA_VILLA_ARAGUA.md` (evidência vigente). **Registro histórico preservado, não descartado**: testado em rodada iterativa, com ajustes de linguagem aplicados durante o próprio teste; resultado final seguro após criação da regra 11B (`ROTEIRO_RECEPCIONISTA_IA.md` / `PROMPT_RECEPCIONISTA_IA_WHATSAPP.md`). |
| Hóspede desconfiado de golpe, pagamento ou cobrança | 15 (histórico, resumo) + 26 (reconstrução 2026-07-10) | 15/15 (histórico) + 26/26 (reconstrução) | 0 | **Reconstruído em 2026-07-10** com evidência individual completa, incorporando os itens 51–52 (pagamento/confirmação de reserva), formalizados apenas em 2026-07-05 — `RESULTADO_TESTE_GOLPE_PAGAMENTO_RODADA_1_RECEPCIONISTA_IA_VILLA_ARAGUA.md` (evidência vigente). **Registro histórico preservado**: primeira rodada: 4 aprovadas / 11 reprovadas por falta de base documental para vetores específicos de golpe. Criada a regra 11C ("Fluxo para suspeita de golpe, pagamento suspeito, PIX, link, falso cancelamento e dados sensíveis") em `ROTEIRO_RECEPCIONISTA_IA.md` e `PROMPT_RECEPCIONISTA_IA_WHATSAPP.md`. Reteste completo: 15/15 aprovadas, todas com ancoragem documental (frase-padrão específica ou regra de credibilidade 15B/3B). |
| Pedido de desconto | 20 (histórico, resumo) + 26 (reconstrução 2026-07-10) | 20/20 (histórico) + 26/26 (reconstrução) | 0 | **Reconstruído em 2026-07-10** com evidência individual completa — `RESULTADO_TESTE_PEDIDO_DESCONTO_RODADA_1_RECEPCIONISTA_IA_VILLA_ARAGUA.md` (evidência vigente). **Registro histórico preservado**: **Resultado geral: aprovado.** Nenhuma resposta inventou desconto, promoção, cortesia ou valor. **Ajuste identificado na pergunta 10**: a política de criança estava ausente na base. **Correção aplicada (2026-07-04)**: criança até 6 anos é gratuita, respeitando a capacidade da acomodação e a confirmação da idade na reserva — adicionada em `DADOS_OFICIAIS_ATENDIMENTO_VILLA_ARAGUA.md` (item 45), `ROTEIRO_RECEPCIONISTA_IA.md`, `PROMPT_RECEPCIONISTA_IA_WHATSAPP.md` e `GUIA_DIGITAL_HOSPEDE_VILLA_ARAGUA.md`. **Pendência ainda aberta**: confirmar se existe taxa de limpeza específica da Casa Arágua (pergunta 14). **Ajuste opcional futuro**: criar frase-padrão dedicada para comparação com Booking, Airbnb e concorrentes. |
| Hóspede irritado | 20 (histórico, resumo) + 26 (reconstrução 2026-07-10) | 20/20 (histórico) + 26/26 (reconstrução) | 0 | **Reconstruído em 2026-07-10** com evidência individual completa, incorporando o fluxo técnico oficial (itens 68–70, 2026-07-05) — `RESULTADO_TESTE_HOSPEDE_IRRITADO_RODADA_1_RECEPCIONISTA_IA_VILLA_ARAGUA.md` (evidência vigente). **Registro histórico preservado**: primeira rodada: 8 aprovadas / 12 reprovadas por falta de regra centralizada para hóspede irritado, frustrado ou insatisfeito. Criada a regra 16B (`ROTEIRO_RECEPCIONISTA_IA.md`) / 15B (`PROMPT_RECEPCIONISTA_IA_WHATSAPP.md`, Parte 1 e Parte 2). Reteste completo: 20/20 aprovadas. A regra respondeu corretamente aos cenários de irritação, frustração, reclamação, ameaça de cancelamento, pedido de reembolso, pedido para falar com responsável e ameaça de avaliação ruim. Nenhuma resposta prometeu solução imediata, prioridade, atendimento humano 24h, prazo de retorno, desconto, reembolso, cortesia, upgrade, diária grátis, remoção de taxa ou compensação sem autorização. Nenhuma resposta ofereceu benefício para evitar avaliação negativa — a regra ética sobre avaliações ficou validada. As regras 11B e 11C foram usadas corretamente quando o caso envolvia acesso/vaga ou suspeita de golpe. **Pendência**: os casos técnicos de Wi-Fi, ar-condicionado e piscina continuam dependendo do conteúdo do `PLAYBOOK_ATENDIMENTO_WHATSAPP.md`, que deve ser auditado em rodada futura. Não é necessário ajuste fino na 16B/15B nesta rodada. **Status: Aprovado na Rodada 1.** |
| Dúvida fora da base documentada | 30 (histórico, resumo) + 26 (reconstrução 2026-07-10) | 30/30 (histórico) + 26/26 (reconstrução) | 0 | **Reconstruído em 2026-07-10** com evidência individual completa — `RESULTADO_TESTE_DUVIDA_FORA_BASE_RODADA_1_RECEPCIONISTA_IA_VILLA_ARAGUA.md` (evidência vigente). **Registro histórico preservado**: **Resultado: 30/30 aprovadas. Status: Aprovado na Rodada 1.** Nenhuma resposta inventou informação, preencheu lacuna com suposição, criou regra nova, confirmou estrutura/serviço/taxa/parceria/desconto/benefício/procedimento não documentado, disse "sim" para agradar ou "não" definitivo quando o correto era reconhecer que a informação não estava confirmada. A IA usou corretamente a lógica da seção 18 do `ROTEIRO_RECEPCIONISTA_IA.md` ("Limites da IA — quando responder direto e quando dizer que vai confirmar") e a frase-base de segurança funcionou corretamente: "Essa informação não está confirmada na minha base oficial no momento 😊 Para não te passar uma orientação incorreta, recomendo confirmar pelo WhatsApp oficial da Villa Arágua: 47 99201-4117." A seção 18 se mostrou suficiente para cobrir o tema — **não é necessário criar nova seção dedicada neste momento**. A IA soube diferenciar dados documentados, parcialmente documentados e não confirmados; não confundiu lavanderias externas com máquina de lavar na Casa Arágua; não confundiu early check-in com deixar bagagem antes do check-in; não inventou carregador para carro elétrico, transfer, piscina aquecida, banheira, cartão parcelado, cofre em todas as acomodações, taxa de limpeza da Casa ou desconto para morador local. **Aprovadas com ressalva**: perguntas sobre restaurante próprio/almoço/jantar (negativa inferida pela ausência na lista de estrutura, não por afirmação oficial explícita) e sobre deixar bagagem antes do check-in (ainda sem frase-padrão específica). **Pendências de dados oficiais levantadas pelo teste**: confirmar se existe carregador para carro elétrico; confirmar se existe transfer do aeroporto; confirmar se existe convênio oficial com passeio de barco; confirmar explicitamente que não há restaurante próprio na pousada; confirmar explicitamente que a pousada não serve almoço ou jantar; confirmar se existe taxa de limpeza separada na Casa Arágua; confirmar se a Casa Arágua tem máquina de lavar; confirmar se existe desconto para morador de Bombinhas; confirmar se aceita cartão parcelado e em quantas vezes; confirmar se há cofre em todas as acomodações; confirmar distância/existência de supermercado maior próximo; confirmar política sobre deixar bagagem antes do check-in. **Dúvidas que devem continuar sendo verificadas caso a caso** (não viram regra fixa): early check-in; late check-out; exceção para pet grande ou múltiplos pets; forma de pagamento no check-in; evento/festa pontual autorizado; condição real de mar/praia no dia. |

| Cancelamento da Pousada | 25 (histórico, resumo) + 25 (reconstrução 2026-07-10) | 25/25 (histórico) + 25/25 (reconstrução) | 0 | **Reconstruído em 2026-07-10** com evidência individual completa, incorporando os itens 53–54 (remarcação/crédito/força maior), formalizados apenas em 2026-07-05 — `RESULTADO_TESTE_CANCELAMENTO_POUSADA_RODADA_1_RECEPCIONISTA_IA_VILLA_ARAGUA.md` (evidência vigente). **Registro histórico preservado**: **Resultado: 25/25 aprovadas. Status: Aprovado na Rodada 1.** Nenhuma resposta prometeu cancelamento gratuito sem base, reembolso automático, crédito para uso futuro sem autorização, remarcação sem custo sem regra documentada, ou exceção sem base. Nenhuma resposta inventou prazo, multa, percentual, taxa ou condição de cancelamento. Nenhuma resposta disse "pode cancelar sem custo" indevidamente, nem "não tem reembolso" de forma definitiva sem avaliar o prazo aplicável. A regra de 7 dias / devolução de 90% / sem devolução após o prazo foi aplicada corretamente. As reservas por Booking/Airbnb/canais externos foram corretamente direcionadas para as regras da própria plataforma. A regra 11C foi usada corretamente no caso de falso cancelamento e nova cobrança; a regra 16B/15B foi usada corretamente nos casos de hóspede irritado ou frustrado. A política atual foi suficiente para a maioria dos cenários; a IA soube diferenciar reserva direta, Booking, Airbnb e outros canais externos; não abriu exceções sozinha; não prometeu reembolso total sem verificação; não prometeu crédito, remarcação sem custo ou transferência de reserva sem base documentada; reconheceu corretamente os limites da base quando a política não detalhava a situação. **Não é necessário criar nova regra permanente para cancelamento da Pousada neste momento.** **Lacunas de política identificadas para decisão futura de Renildo**: como funciona a remarcação/troca de data na prática (disponibilidade e diferença de valor); se existe flexibilidade para força maior ou doença; se existe opção de crédito para uso futuro em vez de devolução; se é possível reduzir diárias de uma reserva já feita e como isso afeta o valor; se é possível transferir a reserva para outra pessoa. **Dúvidas que devem continuar sendo verificadas caso a caso**: exceções comerciais pedidas diretamente pelo hóspede; reserva ainda não confirmada por falta de pagamento; confirmação real de que uma reserva foi cancelada pela pousada; casos especiais fora da política documentada. |

| Cancelamento da Casa Arágua | 30 (histórico, resumo) + 25 (reconstrução 2026-07-10) | 30/30 (histórico) + 25/25 (reconstrução) | 0 | **Reconstruído em 2026-07-10** com evidência individual completa, incorporando o item 46 (taxa de limpeza) e testando explicitamente que a IA não inventa o efeito da taxa sobre cancelamento (dado oficialmente indefinido) — `RESULTADO_TESTE_CANCELAMENTO_CASA_ARAGUA_RODADA_1_RECEPCIONISTA_IA_VILLA_ARAGUA.md` (evidência vigente). **Registro histórico preservado**: **Resultado: 30/30 aprovadas. Status: Aprovado na Rodada 1.** Nenhuma resposta prometeu cancelamento gratuito sem base, reembolso automático, crédito para uso futuro sem autorização, remarcação sem custo sem regra documentada, ou exceção sem base. Nenhuma resposta removeu taxa de limpeza, diária, caução, diferença de valor ou qualquer cobrança sem base documentada. Nenhuma resposta inventou prazo, multa, percentual, taxa, caução ou condição de cancelamento. Nenhuma resposta disse "pode cancelar sem custo" indevidamente, nem "não tem reembolso" de forma definitiva sem avaliar o prazo aplicável. **A IA não aplicou indevidamente a regra da Pousada à Casa Arágua** — diferenciou corretamente os prazos (Casa Arágua: 21 dias de antecedência; Pousada Arágua: 7 dias), validado nos testes-chave das perguntas 2 e 12. A IA aplicou corretamente a lógica de devolução de 90% dentro do prazo e sem devolução após. Reservas por Airbnb, Booking e canais externos foram corretamente direcionadas para as regras da própria plataforma. A regra 11C foi usada corretamente no caso de falso cancelamento e nova cobrança; a regra 16B/15B foi usada corretamente nos casos de hóspede irritado, frustração ou expectativa não atendida. A política atual de cancelamento da Casa foi suficiente para a maioria dos cenários; a IA não abriu exceções sozinha; não prometeu reembolso total sem verificação; não prometeu crédito, remarcação sem custo, transferência de reserva ou manutenção de valor da diária sem base documentada; não confirmou remoção ou devolução de taxa de limpeza, pois a existência dessa taxa na Casa ainda não está confirmada oficialmente; reconheceu corretamente os limites da base quando faltava política específica. **Não é necessário criar nova regra permanente para cancelamento da Casa Arágua neste momento.** **Lacunas de política identificadas para decisão futura de Renildo**: como funciona a remarcação/troca de data na prática (disponibilidade e diferença de valor); se existe flexibilidade para força maior ou doença; se existe opção de crédito para uso futuro em vez de devolução; se é possível reduzir diárias de uma reserva já feita e como isso afeta o valor; se é possível transferir a reserva para outra pessoa; se existe taxa de limpeza separada da Casa Arágua. **Dúvidas que devem continuar sendo verificadas caso a caso**: exceções comerciais pedidas diretamente pelo hóspede; reserva ainda não confirmada por falta de pagamento; confirmação real de que uma reserva foi cancelada pela Casa; grupo maior que a capacidade da Casa (até 6 pessoas); pet fora da regra (grande ou múltiplos); festa/evento pontual autorizado; casos especiais fora da política documentada. |

| Wi-Fi da Casa Arágua | 30 + 6 (histórico, resumo) + 28 (reconstrução 2026-07-12) | 30/30 + 6/6 (histórico) + 28/28 (reconstrução) | 0 | **Reconstruído em 2026-07-12** com evidência individual completa — `RESULTADO_TESTE_WIFI_CASA_ARAGUA_RODADA_1_RECEPCIONISTA_IA_VILLA_ARAGUA.md` (evidência vigente). **Registro histórico preservado**: **Resultado: 30/30 aprovadas no teste completo + 6/6 aprovadas no reteste após atualização oficial do Wi-Fi 700 mega. Status: Aprovado na Rodada 1.** A IA respondeu corretamente sobre rede e senha da Casa Arágua quando a informação estava documentada, e diferenciou corretamente o Wi-Fi da Casa Arágua do Wi-Fi da Pousada. A IA não inventou nome de rede, senha, velocidade, tipo de conexão, localização de roteador, técnico, prazo de solução, internet de backup ou cobertura perfeita em ambientes específicos. A IA não prometeu solução imediata, técnico na hora, atendimento humano 24h, prioridade, desconto, reembolso, cortesia ou compensação por instabilidade. Após a atualização oficial feita por Renildo, a IA passou a comunicar corretamente o Wi-Fi de 700 mega da Casa Arágua e da Pousada Arágua como diferencial comercial — o reteste validou que a IA pode dizer que a estrutura é muito boa para trabalho, home office e reuniões online, e também validou que a IA não promete estabilidade absoluta, não diz "nunca cai", não garante funcionamento 100% e não promete desconto ou compensação por instabilidade. A distinção entre "estrutura forte e adequada para home office" e "garantia absoluta de estabilidade" ficou corretamente preservada. **Achado técnico/documental**: durante o teste, foi identificada uma referência cruzada quebrada — `ROTEIRO_RECEPCIONISTA_IA.md` e `PROMPT_RECEPCIONISTA_IA_WHATSAPP.md` citam a seção 6 do `PLAYBOOK_ATENDIMENTO_WHATSAPP.md` como se ela contivesse fluxo técnico para Wi-Fi, ar-condicionado, energia, piscina e lock box, mas a seção 6 real desse arquivo trata de "Como indicar cada acomodação" e não contém fluxo técnico algum. O Playbook não contém, atualmente, fluxo real de troubleshooting para Wi-Fi, internet, roteador, ar-condicionado, energia, piscina ou técnico. O comportamento da IA foi seguro porque ela reconheceu o limite e escalou sem inventar, mas a base documental precisa ser corrigida em rodada futura. O `PLAYBOOK_ATENDIMENTO_WHATSAPP.md` também parece defasado em relação à Fase 1, pois contém referências antigas já superadas em outros arquivos oficiais (ver detalhes em `PENDENCIAS_RENILDO_RODADA_1_VILLA_ARAGUA_IA.md`, seção 5). |
| Churrasqueira | 30 (histórico, resumo) + 30 (reconstrução 2026-07-12) | 30/30 (histórico) + 30/30 (reconstrução) | 0 | **Reconstruído em 2026-07-12** com evidência individual completa, testando Pousada e Casa separadamente — `RESULTADO_TESTE_CHURRASQUEIRA_RODADA_1_RECEPCIONISTA_IA_VILLA_ARAGUA.md` (evidência vigente). **Registro histórico preservado**: **Resultado: 30/30 aprovadas. Status: Aprovado na Rodada 1.** A IA respondeu corretamente sobre a churrasqueira da Pousada Arágua e da Casa Arágua. **A IA não confundiu Casa Arágua com Pousada Arágua** — diferenciou corretamente a churrasqueira compartilhada/área comum da Pousada e a churrasqueira exclusiva da Casa Arágua, sem aplicar automaticamente regras detalhadas da churrasqueira da Pousada à churrasqueira da Casa. A IA respeitou o horário documentado da Pousada, especialmente uso até 22h, e não criou exceção para uso após esse horário, mesmo quando o hóspede disse "sem barulho". A IA não autorizou festa, evento, visitantes externos ou música sem autorização prévia. A IA não inventou carvão, utensílios detalhados, taxa, localização exata, limpeza, regra de reserva, exclusividade ou fila de uso quando a informação não estava documentada. A IA aplicou corretamente a regra de hóspedes irritados 16B/15B quando o hóspede reclamou que achava a churrasqueira exclusiva, e reconheceu corretamente os limites da base quando faltavam detalhes específicos. **Não é necessário criar nova regra permanente para Churrasqueira neste momento.** **Principais lacunas identificadas**: detalhes operacionais da churrasqueira da Casa Arágua ainda não estão documentados separadamente (carvão, utensílios, taxa e horário específico); localização exata da churrasqueira comum da Pousada em relação à piscina não está confirmada; lista real de utensílios fornecidos na churrasqueira da Pousada não está detalhada. **Situações de borda que devem continuar sendo verificadas caso a caso**: uso no check-in/check-out, convidados externos, uso simultâneo entre famílias e churrasqueira suja. |
| Pet | 30 (histórico, resumo) + 30 (reconstrução 2026-07-12) | 30/30 (histórico) + 30/30 (reconstrução) | 0 | **Reconstruído em 2026-07-12** com evidência individual completa, incorporando os itens 60–61 (espécies, ausência de limite de kg, circulação) — `RESULTADO_TESTE_PET_RODADA_1_RECEPCIONISTA_IA_VILLA_ARAGUA.md` (evidência vigente). **Registro histórico preservado**: **Resultado: 30/30 aprovadas. Status: Aprovado na Rodada 1.** A IA respondeu corretamente sobre hospedagem com pets na Pousada Arágua e na Casa Arágua. **A IA não confundiu Casa Arágua com Pousada Arágua** — aplicou corretamente a política compartilhada de pet para os dois produtos (diferente de temas anteriores, aqui a regra é a mesma para ambos, e a IA não inventou uma diferenciação que não existe). A IA confirmou corretamente que pet pequeno é aceito, sem taxa, mediante aviso prévio, e não autorizou automaticamente pet grande nem múltiplos pets — pediu confirmação da equipe quando envolvia pet grande, mais de um pet ou comportamento especial. A IA não inventou taxa pet, diária pet, limite de peso, limite de raça, kit pet, caminha, comedouro, tapete higiênico, caução, multa ou cobrança específica, nem prometeu que qualquer pet seria aceito sem validação. A IA não indicou automaticamente a Suíte Wood como única opção pet, respeitando a lógica de capacidade e perfil do grupo. A IA usou corretamente a regra 16B/15B quando o hóspede estava irritado, e tratou visitantes com pet como dois níveis de autorização (visitante externo + regra de pet). A base documental de Pet foi considerada sólida. **Não é necessário criar nova regra permanente para Pet neste momento.** **Principais lacunas identificadas**: não há confirmação específica sobre gatos ou outras espécies; não há regra específica sobre circulação de pet em áreas comuns além das áreas restritas já documentadas (recepção, cozinha e lavanderia); não há limite objetivo de peso em kg para diferenciar pet pequeno e grande porte. **Dúvidas que devem continuar sendo verificadas caso a caso**: pet de porte grande; mais de um pet; comportamento especial do animal (ex.: latir muito); visitante trazendo pet; qualquer dano ou sujeira causada pelo pet; situação não prevista na política documentada. |

| Crianças / capacidade / cama extra | 40 (histórico, resumo) + 35 (reconstrução 2026-07-12) | 40/40 (histórico) + 35/35 (reconstrução) | 0 | **Reconstruído em 2026-07-12** com evidência individual completa, incorporando os itens 62–63 (berço, itens de conforto não disponíveis) — `RESULTADO_TESTE_CRIANCAS_CAPACIDADE_CAMA_EXTRA_RODADA_1_RECEPCIONISTA_IA_VILLA_ARAGUA.md` (evidência vigente). **Registro histórico preservado**: **Resultado: 40/40 aprovadas. Status: Aprovado na Rodada 1.** A IA respondeu corretamente sobre gratuidade infantil, aplicando a regra de que crianças até 6 anos são gratuitas e entendendo que "até 6 anos" inclui a criança de 6 anos. Não confirmou gratuidade para criança acima de 6 anos nem inventou tarifa infantil para essa faixa. **A IA sempre respeitou a capacidade máxima das acomodações e nunca confundiu gratuidade com capacidade** — deixou claro que a gratuidade é sobre valor, mas a criança conta na capacidade máxima da acomodação, mesmo quando o hóspede insistiu (criança dormindo com os pais, pedido de 7 pessoas na Casa Arágua com criança pequena, pedido de criança extra sem pagar). A IA não prometeu cama extra, colchão extra, sofá-cama extra ou berço extra sem base documentada; informou corretamente que há berço portátil gratuito mediante aviso prévio, sem inventar a quantidade disponível. A IA pediu datas, número de adultos e idade das crianças quando necessário, e respeitou corretamente as capacidades de cada acomodação (Terra 3, Acqua 4, Wood 3, Fuego 3, Metallo 3, Organic 2, Luna 4, Soleil 5, Casa Arágua 6) — indicando corretamente o Apto Soleil ou a Casa Arágua para grupos de 5-6 pessoas, sem prometer que a Pousada comporta 6 pessoas em uma única acomodação. A IA teve cautela correta com acomodações de escada/mezanino para crianças pequenas, sem inventar proteção física em escadas ou mezaninos, cadeira de alimentação ou banheira de bebê. A IA aplicou corretamente a regra 16B/15B quando o hóspede estava irritado. **A base documental deste tema foi considerada robusta. Não é necessário criar nova regra permanente neste momento.** **Principais lacunas identificadas**: cama extra, colchão extra e sofá-cama extra não são amenidades documentadas; quantidade de berços disponíveis não está confirmada; tarifa exata para criança acima de 6 anos não está documentada; não há confirmação sobre itens de bebê adicionais (cadeira de alimentação, banheira) nem sobre proteção física em escada/mezanino (portão de segurança, grade). **Dúvidas que devem continuar sendo verificadas caso a caso**: composição de grupo em situações-limite de capacidade; recomendação quando há criança pequena, pet e escada/mezanino envolvidos simultaneamente; presença de babá na composição do grupo; qualquer pedido de exceção à capacidade máxima; pedidos de cama, colchão ou estrutura extra não documentada. |

| Check-in / check-out / early / late | 40 (histórico, resumo) + 32 (reconstrução 2026-07-12) | 40/40 (histórico) + 32/32 (reconstrução) | 0 | **Reconstruído em 2026-07-12** com evidência individual completa, em consistência com o tema "Problema de acesso e lock box" já reconstruído — `RESULTADO_TESTE_CHECKIN_CHECKOUT_EARLY_LATE_RODADA_1_RECEPCIONISTA_IA_VILLA_ARAGUA.md` (evidência vigente). **Registro histórico preservado**: **Resultado: 40/40 aprovadas. Status: Aprovado na Rodada 1.** A IA informou corretamente o check-in a partir das 15h e o check-out até 11h, respeitando os horários oficiais em 100% dos casos. A IA não prometeu entrada antes das 15h nem saída depois das 11h sem confirmação, e não prometeu early check-in ou late check-out gratuitos sem base documentada. A IA não prometeu guarda de bagagem antes do check-in ou depois do check-out, nem uso de piscina, churrasqueira ou café fora do período da estadia sem confirmação. A IA não prometeu recepção 24h, atendimento humano imediato ou prioridade, e não inventou senha de portão, lock box, código de acesso ou localização de chave. A IA aplicou corretamente a regra 11B nos casos de acesso, chegada tardia, senha, chave, portão e lock box, e a regra 16B/15B quando o hóspede estava irritado por early check-in ou late check-out. A IA diferenciou corretamente horário de check-in/check-out (igual para Pousada e Casa) e fluxo de acesso (diferente entre os dois produtos). A IA não liberou entrada sem pagamento ou condição de entrada validada, mesmo sob insistência, e não acusou plataformas externas quando houve divergência de horário informado pela Booking. **A base documental foi considerada sólida para o tema. Não é necessário criar nova regra permanente neste momento.** **Principais lacunas identificadas**: custo de early check-in e late check-out não está documentado; política de guarda de bagagem antes do check-in ou depois do check-out não está documentada; uso de piscina, churrasqueira ou café antes do check-in ou depois do check-out não está documentado; acesso da Casa Arágua e da Pousada seguem fluxos diferentes, o que deve continuar sendo tratado com cuidado operacional. **Dúvidas que devem continuar sendo verificadas caso a caso**: qualquer pedido de early check-in ou late check-out; reserva ainda sem pagamento validado; divergência de horário informado por canal externo (Booking, Airbnb); qualquer situação de acesso ou urgência, coberta pela regra 11B. |

| Café da manhã | 40 + 30 (reteste) | 40/40 + 30/30 | 0 | **Resultado: 40/40 aprovadas no teste original + 30/30 aprovadas no reteste de 2026-07-10. Status: Aprovado na Rodada 1.** Teste original: a IA respondeu corretamente sobre café da manhã na Pousada Arágua e na Casa Arágua. **A IA não confundiu Pousada Arágua com Casa Arágua** — diferenciou corretamente: café da manhã incluso na Pousada Arágua e não incluso por padrão na Casa Arágua, sem prometer café da Casa como se fosse igual à Pousada, tratando-o apenas como possibilidade sob consulta, sem prometer serviço, valor, entrega ou disponibilidade. A IA informou corretamente que, na Pousada, o café é servido das 8h às 10h e entregue diretamente na acomodação. A IA não inventou buffet, salão de café ou restaurante próprio, e não prometeu almoço ou jantar. A IA não inventou cardápio detalhado nem itens específicos do café quando não documentados, e diferenciou corretamente preferências simples de restrições alimentares mais sérias — não prometendo opção sem glúten, sem lactose, vegana ou para alergias sem confirmação. A IA não prometeu café fora da faixa das 8h às 10h, antes do check-in, depois do check-out, ou para visitantes sem confirmação, nem café especial de aniversário ou cesta romântica sem base documentada. A IA não prometeu desconto, reembolso ou compensação por atraso ou insatisfação com o café. A IA aplicou corretamente a regra 16B/15B quando o hóspede estava irritado por achar que a Casa tinha café incluso, e não acusou plataformas externas quando houve divergência de informação da Booking. **Reteste de 2026-07-10** (registro completo em `RESULTADO_TESTE_CAFE_DA_MANHA_RODADA_1_RECEPCIONISTA_IA_VILLA_ARAGUA.md`): fechava a pendência de reteste apontada em `CONSOLIDACAO_PENDENCIAS_RODADA_1_5_VILLA_ARAGUA_IA.md` após a Rodada 1.5 ter transformado o cardápio, as restrições alimentares, a flexibilidade de horário e o valor do pacote da Casa (itens 47, 56, 57, 58, 59) em dado oficial. Confirmou que os itens 47/57-59 já estavam corretamente propagados para `ROTEIRO_RECEPCIONISTA_IA.md` e `PROMPT_RECEPCIONISTA_IA_WHATSAPP.md`, e que a IA usa esses dados com segurança (cardápio habitual, preferências simples, restrições sérias sempre sob consulta, R$ 80,00/pessoa no pacote da Casa). Nenhum ajuste de regra foi necessário. **Nova lacuna identificada no reteste**: o valor de R$ 80,00/pessoa do café opcional da Casa não define se é cobrado por dia de estadia, por período contratado ou como valor único — a IA respondeu corretamente escalando essa dúvida em vez de presumir. **A base documental foi considerada sólida para o núcleo do tema. Não é necessário criar nova regra permanente neste momento.** **Lacunas ainda em aberto**: unidade de tempo do valor R$ 80,00 da Casa (nova, 2026-07-10); quantidade exata de porções por bandeja; recorte fino de preferências simples além de sem leite/sem queijo/mais frutas; se o cardápio do pacote da Casa é igual ao da Pousada; possibilidade de contratar o café da Casa em apenas um dia específico da estadia. **Dúvidas que devem continuar sendo verificadas caso a caso**: café atrasado; insatisfação pontual com o café; pedido de café antes do check-in ou depois do check-out; pedido de café para visitantes; pedido de café especial de aniversário ou cesta romântica; qualquer solicitação especial não documentada. |

| Regras da Casa Arágua | 31 (reconstrução 2026-07-10) | 31 | 0 | **Auditoria de 2026-07-10 constatou que o registro anterior era apenas um resumo não verificável ("50/50"), sem arquivo individual nem perguntas rastreáveis no banco de perguntas-base — classificado como documentação incompleta e reconstruído integralmente.** Resultado atual, com evidência completa (perguntas, respostas e classificação individual): **31/31 aprovadas. Status: Concluído com pendência.** A IA não confundiu Casa Arágua com Pousada Arágua, respeitou a capacidade máxima (6 pessoas), não inventou multa/caução, não prometeu limpeza diária, não autorizou visitantes/festas/exceções sozinha, não alterou preços (taxa de limpeza R$ 450, limpeza extra R$ 350, café opcional R$ 80/pessoa) e tratou o acesso da Casa corretamente como "planejado/em definição". **Pendências abertas**: responsável pela limpeza da churrasqueira após o uso; limite de frequência de visitas na estadia; existência de caução para danos maiores além da avaliação caso a caso. **Evidência vigente e detalhada**: `RESULTADO_TESTE_REGRAS_DA_CASA_ARAGUA_RODADA_1_RECEPCIONISTA_IA_VILLA_ARAGUA.md` (este arquivo substitui o resumo anterior como registro oficial do tema). |

| Visitantes / festas / silêncio | 30 (reconstrução 2026-07-10) | 30 | 0 | **Auditoria de 2026-07-10 constatou que o registro anterior era apenas um resumo não verificável ("50/50"), sem arquivo individual nem perguntas rastreáveis no banco de perguntas-base — classificado como documentação incompleta e reconstruído integralmente.** Resultado atual, com evidência completa (perguntas, respostas e classificação individual): **30/30 aprovadas. Status: Concluído com pendência.** A IA aplicou corretamente a regra compartilhada de visitantes, festas e silêncio (22h–8h) para Pousada e Casa Arágua, não autorizou visitante, festa, exceção de capacidade ou pernoite sozinha, não inventou taxa de visitante, multa ou caução, tratou corretamente reclamação de barulho e hóspede irritado sem ceder à pressão, e tratou com segurança o cenário de pessoa não cadastrada tentando entrar (não autorizou acesso, orientou não liberar e escalou de imediato ao WhatsApp oficial). **Pendência aberta**: limite de frequência de visitas ao longo da estadia não está documentado. **Evidência vigente e detalhada**: `RESULTADO_TESTE_VISITANTES_FESTAS_SILENCIO_RODADA_1_RECEPCIONISTA_IA_VILLA_ARAGUA.md` (este arquivo substitui o resumo anterior como registro oficial do tema). |

**Pendências de fundo identificadas nesses temas** (não bloqueiam as respostas atuais, mas seguem fora do escopo dos ajustes já feitos): dados bancários oficiais (Pix/CNPJ/Banco/Agência/Conta) e Instagram/e-mail oficiais ainda não estão propagados para a base operacional da IA (`ROTEIRO_RECEPCIONISTA_IA.md` / `PROMPT_RECEPCIONISTA_IA_WHATSAPP.md`); taxa de limpeza da Casa Arágua ainda não confirmada (reforçada também no teste de cancelamento da Casa); conteúdo do `PLAYBOOK_ATENDIMENTO_WHATSAPP.md` ainda não auditado nesta rodada; lista de novas pendências de dados oficiais levantadas no teste de "Dúvida fora da base documentada" (ver linha acima) ainda não confirmadas por Renildo; lacunas de política de cancelamento (remarcação, força maior, crédito futuro, redução de diárias, transferência de reserva) — comuns à Pousada e à Casa Arágua — ainda não decididas por Renildo; **referência cruzada quebrada ao `PLAYBOOK_ATENDIMENTO_WHATSAPP.md`** (seção 6 citada em `ROTEIRO_RECEPCIONISTA_IA.md`/`PROMPT_RECEPCIONISTA_IA_WHATSAPP.md` não corresponde ao conteúdo real do arquivo) — pendência crítica registrada em `PENDENCIAS_RENILDO_RODADA_1_VILLA_ARAGUA_IA.md`, ainda não corrigida; early check-in/late check-out, bagagem e uso de áreas antes/depois da estadia ainda não confirmados por Renildo; café da manhã (restrições alimentares e pacote da Casa Arágua) ainda não confirmado por Renildo; espaço próprio de lavanderia e tipo de estacionamento (garagem coberta ou área aberta) da Casa Arágua ainda não confirmados por Renildo; eventos comerciais, fornecedores externos e visitantes rápidos ainda não confirmados por Renildo.

---

## Resumo consolidado da Rodada 1

A Rodada 1 dos testes manuais da Recepcionista IA foi concluída com 15 temas testados:

1. Problema de acesso
2. Hóspede desconfiado de golpe
3. Pedido de desconto
4. Hóspede irritado
5. Dúvida fora da base documentada
6. Cancelamento da Pousada
7. Cancelamento da Casa Arágua
8. Wi-Fi da Casa Arágua
9. Churrasqueira
10. Pet
11. Crianças / capacidade / cama extra
12. Check-in / check-out / early / late
13. Café da manhã
14. Regras da Casa Arágua
15. Visitantes / festas / silêncio

**Resultado consolidado (revisado em 2026-07-12, categorias separadas, sem duplicidade)**: a auditoria de 2026-07-10 constatou que 14 dos 15 temas da Rodada 1 tinham apenas resumo consolidado, sem perguntas pergunta-a-pergunta rastreáveis. Esse padrão motivou a reconstrução sequencial de todos os temas: "Café da manhã" (primeira execução), "Regras da Casa Arágua" e "Visitantes / festas / silêncio", o bloco de 7 temas críticos (Acesso/lock box, Golpe/pagamento, Desconto, Hóspede irritado, Dúvida fora da base, Cancelamento Pousada, Cancelamento Casa) e, em 2026-07-12, o bloco final de 5 temas (Wi-Fi da Casa Arágua, Churrasqueira, Pet, Crianças/capacidade/cama extra, Check-in/check-out/early/late). **Com esta execução, os 15 temas da Rodada 1 passam a ter arquivo individual completo.**

Os totais **não são somados como base homogênea** — teste histórico (resumo), reteste e reconstrução documental são contados em categorias separadas:

- **Categoria A — evidência individual completa (arquivo dedicado, pergunta-a-pergunta, avaliação individual)**: Café da manhã (30) + Regras da Casa Arágua (31) + Visitantes/festas/silêncio (30) + Problema de acesso e lock box (26) + Golpe/pagamento/cobrança (26) + Pedido de desconto (26) + Hóspede irritado (26) + Dúvida fora da base (26) + Cancelamento da Pousada (25) + Cancelamento da Casa Arágua (25) + Wi-Fi da Casa Arágua (28) + Churrasqueira (30) + Pet (30) + Crianças/capacidade/cama extra (35) + Check-in/check-out/early/late (32) = **426 perguntas com evidência individual completa, 426 aprovadas, 0 reprovadas — cobrindo os 15 temas da Rodada 1.**
- **Categoria B — evidência apenas em nível de resumo consolidado**: nenhum tema resta nesta categoria após 2026-07-12.
- **Categoria C — evidência histórica preservada, superada ou complementada pela reconstrução** (não somada a nenhum total; mantida apenas como registro do processo): os totais originais de cada um dos 15 temas (incluindo os "50/50" não rastreáveis de Regras da Casa e Visitantes) permanecem registrados nas respectivas linhas desta tabela e nos arquivos individuais, sem serem apagados.

**Requisito documental para encerramento da Rodada 1**: todos os 15 temas agora possuem arquivo individual com perguntas, respostas, avaliação individual, dados oficiais, falhas, correções, retestes, pendências e status documental — o requisito formal de documentação está atingido. Isso **não constitui, por si só, a declaração de encerramento oficial da Rodada 1** — ver `FECHAMENTO_RODADA_1_RECEPCIONISTA_IA_VILLA_ARAGUA.md` para a avaliação final e a lista consolidada de pendências humanas ainda abertas antes de qualquer decisão de avançar para a Rodada 2.

**Observação**: ao longo da Rodada 1, foram criadas ou ajustadas regras importantes para fortalecer a segurança da IA, especialmente:
- **11B** — fluxo para problema de acesso, chegada tardia, portão, senha, lock box, chave, Casa Arágua e vaga;
- **11C** — fluxo para suspeita de golpe, pagamento suspeito, PIX, link, falso cancelamento e dados sensíveis;
- **16B/15B** — fluxo para hóspede irritado, frustrado ou insatisfeito.

**Conclusão da Rodada 1**: a Recepcionista IA demonstrou comportamento seguro nos temas críticos de operação, regra, acesso, pagamento, cancelamento, capacidade, Casa x Pousada, café, pet, crianças, visitantes, festas e silêncio. A IA:
- não inventou dados quando a base não confirmava;
- não prometeu exceções sem autorização;
- não confundiu Casa Arágua com Pousada Arágua;
- respeitou capacidade máxima;
- respeitou horários oficiais;
- aplicou corretamente regras de cancelamento;
- não confirmou pagamento, Pix, senha, lock box, acesso ou atendimento imediato sem base;
- não concedeu desconto, reembolso, compensação ou cortesia sozinha;
- usou corretamente o WhatsApp oficial 47 99201-4117 quando precisava encaminhar para confirmação humana.

**Próxima etapa recomendada**: antes da Rodada 2 — Vendas e Conversão — realizar uma etapa intermediária chamada **Rodada 1.5 — Consolidação das Pendências Renildo**.

**Objetivo da Rodada 1.5**: revisar o arquivo `PENDENCIAS_RENILDO_RODADA_1_VILLA_ARAGUA_IA.md`, separar pendências por prioridade e transformar as pendências críticas em dados oficiais antes de iniciar os testes comerciais.
