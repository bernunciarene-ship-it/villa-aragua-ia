# Auditoria — Operação da Estadia Villa Arágua (v1)

Auditoria completa do arquivo `PENDENCIAS_OPERACAO_ESTADIA_VILLA_ARAGUA.md`, baseada na leitura integral do seu estado atual (13 seções). Nenhum arquivo foi alterado nesta auditoria.

---

## 1. O que está confirmado

| Item | Dado confirmado |
|---|---|
| Café da manhã | 8h às 10h, entregue na acomodação, horário escolhido pelo hóspede no check-in, sensação de "café na acomodação" sem prometer "café na cama" literal |
| Wi-Fi Rede 1 (Pousada) | Rede "Pousada Aragua", senha "feriasprasempre" |
| Churrasqueira | 1 acomodação por vez, até 3h de uso, até 22h, sem taxa, carvão por conta do hóspede, utensílios básicos fornecidos, convidados externos só com confirmação, controle via Google Agenda |
| Política de reserva/cancelamento | Pousada: 7 dias / Casa: 21 dias de antecedência; devolução de 90% dentro do prazo; sem devolução após; no-show até 00h do dia seguinte; canais externos seguem política do canal |
| WhatsApp oficial | 47 99201-4117 (único válido); número antigo 47 99103-4001 explicitamente invalidado |
| Dados bancários/Pix | CNPJ, favorecido, banco, agência e conta confirmados |
| Piscina | 9h às 21h, crianças acompanhadas, botão de emergência, regras de convivência, espreguiçadeiras de uso comum |
| Parceria Moquém do Mar | Renovada, com pulseiras de identificação; cadeiras conforme número de hóspedes + 1 guarda-sol por acomodação; exceção do Apto Soleil registrada |
| Cadeiras/guarda-sóis próprios da pousada | 45 cadeiras, 20 guarda-sóis, retirada/devolução autônoma, preferencialmente em horário de recepção presencial |
| Enxoval extra (valores) | Jogo de cama R$30, toalha de banho R$15, toalha de rosto R$10, tapete de piso R$10; troca completa por acomodação (R$150 a R$220 conforme unidade); sem quantidade mínima |
| Política de peças manchadas/danificadas | Texto oficial criado e aprovado |
| Casa Arágua (limpeza) | Sem serviço padrão de limpeza/troca de enxoval durante a estadia; extras sob consulta |
| Diferença Pousada x Casa | Lista comparativa registrada (seção 6) |

## 2. O que está planejado/em definição (ainda não é regra fechada)

- **Regra de troca/limpeza intermediária a partir de 4 diárias**: a direção e a intenção estão confirmadas, mas o próprio arquivo registra que "essa regra ainda deve ser validada operacionalmente antes de virar comunicação final" — **não deve ser tratada como regra 100% fechada** até essa validação.
- **Detalhes operacionais finais da parceria com o Moquém do Mar** (se houver ajustes futuros).
- **Exceção/ajuste operacional do Apto Soleil** no apoio de praia — mencionado como "pode ter ajuste", sem regra fixa ainda.
- **Automação futura da churrasqueira via Google Agenda**: direção definida, integração real ainda não existe.
- **Automação futura do café da manhã (coleta de preferências pela IA)**: ideia registrada, sem integração real ainda.

## 3. Lista de pendências

- Wi-Fi Rede 2 da Pousada (nome e senha).
- Wi-Fi da Casa Arágua (nome e senha).
- Validação final da política de limpeza intermediária da pousada.
- Forma de cobrança/registro interno dos itens extras de enxoval.
- Valores de reposição por peça danificada/extraviada (tabela futura, se Renildo quiser criar).
- Nomes, endereços, horários e links das 2 lavanderias próximas.

## 4. Contradições encontradas

**Nenhuma contradição factual foi encontrada.** Todos os dados numéricos e regras (horários, valores, prazos, WhatsApp oficial, quantidades) são consistentes em todas as seções em que aparecem — não há nenhum caso de um mesmo dado divergindo entre duas partes do arquivo.

Um ponto que **poderia ser lido como contradição, mas não é**: a seção 13 (Status) lista "Direção de limpeza/enxoval da pousada" como "confirmado/documentado", enquanto a seção 9 e a própria seção 13 (em "Pendentes") registram que a "validação final da política de limpeza intermediária" ainda está pendente. Isso é coerente na prática (a **direção/valores** estão confirmados; a **validação operacional final** do timing exato da troca intermediária é que ainda está em aberto), mas a redação pode gerar confusão para quem ler rápido. Recomenda-se deixar essa distinção mais explícita antes da integração.

## 5. Duplicidades encontradas

1. **Duplicidade real e significativa — Café da manhã (seções 1 e 2)**: a seção 1.4 ("Preferências simples"), 1.6 ("Mensagem sobre preferências") e 1.7 ("Ideia de automação futura") repetem quase palavra por palavra o conteúdo da seção 2 ("Preferências e restrições do café da manhã"). A mensagem da seção 1.6 é **idêntica** à da seção 2. A seção 1.4 já contém uma nota de cross-reference ("Ver seção 2 para o detalhamento completo"), o que sugere a intenção original de a seção 1 ser um resumo e a seção 2 o detalhamento — mas, na prática, o conteúdo foi duplicado integralmente em vez de apenas referenciado. **Recomendação**: antes da integração, consolidar em uma única fonte (por exemplo, manter o detalhamento completo só na seção 2, e deixar a seção 1.4 apenas com 1-2 linhas de resumo + link cruzado), para evitar que uma futura atualização edite uma cópia e esqueça a outra.

2. **Duplicidade parcial de conteúdo — Praia/Moquém do Mar (seção 8)**: o bloco "8.1 Parceria com Moquém do Mar" e o bloco solto "## Diferencial comercial — Apoio de praia com Moquém do Mar" (logo abaixo de 8.2) cobrem informações semelhantes (regra da parceria, cuidados de não prometer quantidade ilimitada/outras praias) com mensagens diferentes, mas conceitos sobrepostos. Não é uma cópia literal como o caso do café, mas há redundância de conceito entre a "regra operacional" (8.1) e o "discurso comercial" (bloco de diferencial). Isso não chega a ser um problema grave — são propósitos diferentes (regra interna vs. mensagens de marketing) — mas vale revisar juntos na hora de integrar para não gerar 2 fontes de mensagens ligeiramente diferentes sobre o mesmo assunto.

3. **Inconsistência de estrutura/numeração**: o bloco "## Diferencial comercial — Apoio de praia com Moquém do Mar" usa nível de título `##` (mesmo nível dos "## 8.", "## 9." etc.), mas não tem número — quebra o padrão de numeração sequencial do documento. O mesmo vale para o subtítulo `# Piscina, Praia, Limpeza e Enxoval — Villa Arágua` (nível `#`, mais alto que os `##` das seções), que funciona como um agrupador visual, mas mistura dois níveis de hierarquia Markdown no mesmo documento. Recomenda-se padronizar (ex.: transformar o bloco de diferencial comercial em "### 8.3" e manter o agrupador de "Piscina, Praia..." apenas como comentário/nota, não como título de nível 1) antes de qualquer exportação ou geração automática de sumário.

## 6. Recomendações de integração futura nos arquivos principais

- **Café da manhã, Wi-Fi (Rede 1), churrasqueira, piscina**: podem ser integrados a `DADOS_OFICIAIS_ATENDIMENTO_VILLA_ARAGUA.md`, `ROTEIRO_RECEPCIONISTA_IA.md`, `PROMPT_RECEPCIONISTA_IA_WHATSAPP.md` e `GUIA_DIGITAL_HOSPEDE_VILLA_ARAGUA.md` **desde já** — são regras fechadas e sem pendência bloqueante.
- **Política de reserva/cancelamento e dados bancários**: prontos para integração em `DADOS_OFICIAIS_ATENDIMENTO_VILLA_ARAGUA.md`, `ROTEIRO_RECEPCIONISTA_IA.md` e `PROMPT_RECEPCIONISTA_IA_WHATSAPP.md` — atenção especial para **não publicar dados bancários** em nenhum material aberto (Guia Digital público, site, Meta Ads).
- **Parceria Moquém do Mar / cadeiras e guarda-sóis**: pronta para integração comercial em `ROTEIRO_RECEPCIONISTA_IA.md`, `PROMPT_RECEPCIONISTA_IA_WHATSAPP.md`, `GUIA_DIGITAL_HOSPEDE_VILLA_ARAGUA.md` e, quando fizer sentido, em materiais de Meta Ads — **recomenda-se resolver a duplicidade do item 5.2 antes** de copiar as mensagens para os arquivos principais, para levar apenas uma versão consolidada.
- **Enxoval extra e política de peças manchadas**: prontos para integração em `GUIA_DIGITAL_HOSPEDE_VILLA_ARAGUA.md` e no fluxo de atendimento da IA (`ROTEIRO`/`PROMPT`) — já têm valores e texto oficial fechados.
- **Limpeza intermediária da pousada**: **aguardar a validação operacional final** antes de integrar como regra fixa nos arquivos principais — hoje só deve circular como informação interna de planejamento.
- **Casa Arágua (limpeza)**: pronta para integração.
- **Wi-Fi Rede 2, Wi-Fi Casa Arágua, lavanderias**: **não integrar ainda** — seguem como `[PREENCHER]`.

## 7. Veredito final

**Pronto para integração parcial.** A maior parte do conteúdo do arquivo (café da manhã, Wi-Fi Rede 1, churrasqueira, política de reserva/cancelamento, piscina, parceria de praia, cadeiras/guarda-sóis próprios, enxoval extra e política de peças danificadas) está confirmada, consistente e sem contradições factuais — pode ser integrada aos arquivos principais nesta forma.

Antes da integração, recomenda-se apenas:
1. Resolver a duplicidade de conteúdo entre as seções 1 e 2 (café da manhã).
2. Consolidar as duas fontes de mensagens sobre a parceria de praia (seção 8.1 e o bloco de diferencial comercial).
3. Deixar explícito que a "limpeza intermediária" ainda não tem validação operacional final, para não ser integrada como regra fixa antes da hora.
4. Ajustar a hierarquia de títulos Markdown para manter a numeração sequencial sem quebras.

Nenhum desses pontos é bloqueante para uma integração parcial imediata dos itens já fechados — são ajustes de organização e clareza, não de conteúdo incorreto.
