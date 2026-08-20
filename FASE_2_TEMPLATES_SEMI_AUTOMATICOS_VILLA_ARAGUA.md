# FASE 2 — TEMPLATES SEMI-AUTOMÁTICOS VILLA ARÁGUA

*Documento de planejamento. Nenhuma automação real foi criada, configurada ou conectada ao escrever este arquivo — nenhum Zap foi montado no Zapier, nenhuma conexão com WhatsApp foi feita. Nenhuma skill e nenhum arquivo existente foram alterados; este documento apenas se apoia neles.*

## 1. Objetivo da Fase 2

Automatizar tudo o que fica **entre** a mensagem do lead e o clique de enviar — registro do lead, classificação, geração de sugestão de resposta e organização da fila de aprovação — mantendo **100% humana** a leitura da mensagem recebida no WhatsApp e o envio da resposta aprovada. Isso vale tanto por regra de segurança do projeto ("WhatsApp não deve enviar resposta automática livre nesta fase") quanto por limitação técnica atual: o WhatsApp oficial (47 99201-4117) roda hoje no **app comum/Business gratuito**, sem API paga conectada — captura e envio automáticos de mensagem não são tecnicamente possíveis ainda (ver seção 8).

## 2. O que muda da Fase 1 para a Fase 2

- **Fase 1** (`FASE_1_FOLLOW_UP_MANUAL_ASSISTIDO_VILLA_ARAGUA.md`): tudo manual — um humano decide levar cada lead até a IA, sem padrão fixo de ferramenta.
- **Fase 2**: o mesmo espírito (IA sugere, humano aprova), mas padronizado em **três fluxos nomeados** ("Zaps") e com uma **fila diária visível** na própria planilha, em vez de depender de lembrar manualmente quais leads estão pendentes.

| | Fase 1 | Fase 2 |
|---|---|---|
| Registro do lead | Manual, sem padrão fixo | Zap A (já validado) |
| Sugestão de resposta | Gerada sob pedido | Gerada automaticamente junto com o registro (Zap A) |
| Saber quem está pendente de aprovação | Olhando a planilha inteira | Fila diária com critério fixo (seção 4) |
| Após aprovação | Sem padrão | Zap B preenche data/registro automaticamente |
| Envio no WhatsApp | Manual | Continua manual (seção 5 e pendência da seção 8) |

## 3. Fluxo de entrada (Zap A — já validado)

Já testado com sucesso fora desta sessão (Claude Desktop):

```
Humano relata o lead (mensagem recebida no WhatsApp, colada ou descrita para a IA)
        ↓
IA (Claude Desktop, usando PROMPT_OPERACIONAL_AUTOMACAO_WHATSAPP_VILLA_ARAGUA.md) lê, classifica e diferencia Pousada/Casa
        ↓
Zapier cria ou atualiza a linha na planilha oficial (LEADS_FOLLOW_UP_MANUAL_FASE_1_VILLA_ARAGUA_OFICIAL, aba LEADS)
        ↓
"Resposta sugerida pela IA" preenchida
        ↓
"Mensagem aprovada?" = Não
        ↓
"Última resposta enviada" = "Não enviada — sugestão aguardando aprovação humana."
```

Nenhuma mudança técnica é necessária aqui — este fluxo já funciona. A Fase 2 apenas o formaliza como a primeira etapa fixa do processo.

## 4. Fila diária de aprovação

**Critério de entrada na fila**: linha onde `Mensagem aprovada? = Não` **e** `Resposta sugerida pela IA` está preenchida (lead sem sugestão ainda não entra na fila — está incompleto, não pendente de aprovação).

**Ordenação sugerida**:
1. Primeiro, linhas com `Risco comercial? = Sim` (mais atenção, revisar com calma).
2. Depois, por `Data do próximo follow-up` mais próxima/vencida primeiro.

**As três ações possíveis de Renildo em cada linha da fila**:
- **Aprovar como está** — marca `Mensagem aprovada? = Sim`; copia o texto de "Resposta sugerida pela IA" e envia manualmente pelo WhatsApp real.
- **Editar antes de aprovar** — ajusta o texto (na própria célula ou anotando a versão final em "Observações"), só então marca `Mensagem aprovada? = Sim` e envia a versão editada.
- **Não aprovar agora** — deixa `Mensagem aprovada? = Não` (a linha continua na fila do dia seguinte) ou, se decidir parar de vez, muda `Estágio do lead` para "Não insistir mais" (a linha sai da fila).

## 5. Fluxo de saída (Zap B — novo, a configurar no Zapier)

**Trigger**: linha atualizada na planilha oficial, aba LEADS (Zapier: "New or Updated Spreadsheet Row").
**Filtro**: `Mensagem aprovada?` mudou de "Não" para "Sim".
**Ações**:
1. Preencher `Data do último contato` com a data de hoje, automaticamente.
2. (Opcional) Copiar o texto de "Resposta sugerida pela IA" para "Última resposta enviada", **apenas como valor padrão** — se Renildo enviou uma versão editada, ele mesmo corrige esse campo depois, manualmente.

**O que este Zap nunca faz**: enviar a mensagem pelo WhatsApp. Isso continua sendo um passo 100% humano — Renildo (ou quem for aprovar) copia o texto e envia pelo aplicativo de WhatsApp normal. Ver seção 8 para o porquê disso ser também uma limitação técnica, não só uma escolha de segurança.

## 6. Papel de cada skill/ferramenta na Fase 2

Já documentado em detalhe em `PROMPT_OPERACIONAL_AUTOMACAO_WHATSAPP_VILLA_ARAGUA.md`, seção 17 ("Ferramentas e papéis") — este documento não duplica aquele conteúdo, apenas reforça que a Fase 2 usa exatamente essas mesmas ferramentas e papéis (VS Code/Claude Code, Claude Desktop, Zapier, Google Sheets, IA, Humano), sem adicionar nenhuma ferramenta nova.

## 7. Regras de segurança que não mudam

Todas as regras já fixadas em `PROMPT_OPERACIONAL_AUTOMACAO_WHATSAPP_VILLA_ARAGUA.md` (seção 4) continuam valendo integralmente na Fase 2, sem exceção — em especial:
- Não inventar preço, disponibilidade, desconto ou pacote.
- Nunca aplicar pacote da Pousada Arágua automaticamente à Casa Arágua.
- Pet sempre "sob consulta" ou "precisa validação humana", nunca confirmado genericamente.
- Nunca urgência falsa.
- Casa Arágua: estacionamento exclusivo em área aberta para até 3 carros — nunca "garagem coberta".

A automação da Fase 2 acelera o *registro e a sugestão* — ela não reduz nenhuma dessas checagens, e a aprovação humana continua sendo o ponto onde qualquer erro é pego antes de chegar ao hóspede.

## 8. Pendência em aberto — canal técnico de WhatsApp

A Fase 2, como desenhada aqui, **não resolve** a captura automática da mensagem recebida nem o envio automático da mensagem aprovada — ambos continuam manuais, porque o número oficial roda hoje no WhatsApp Business App gratuito, que não tem API/webhook.

Para automatizar essas duas pontas no futuro (o que corresponderia às Fases 3-5 de `ARQUITETURA_FOLLOW_UP_AUTOMATICO_VILLA_ARAGUA.md`), seria necessário contratar uma API paga de WhatsApp Business. Opções conhecidas do mercado, citadas aqui só como referência de nome — **sem recomendação de qual escolher**, decisão que depende de orçamento e prazo que não estão documentados neste projeto:
- Twilio
- 360dialog
- Meta Cloud API (diretamente, via Meta Business)

Enquanto essa decisão não for tomada, a Fase 2 é o nível máximo de automação seguro e tecnicamente viável.

## 9. Checklist prático para configurar o Zap B no Zapier

*(Para quem for configurar de fato no Zapier — esta sessão não tem acesso para criar o Zap.)*

Para o roteiro detalhado de como testar o Zap B com segurança (linha de teste, travas de duplicidade, critérios de validação), ver `CHECKLIST_TESTE_ZAP_B_FASE_2_VILLA_ARAGUA.md`.

- [ ] Confirmar que a conexão Zapier ↔ Google Sheets já usada no Zap A também tem permissão de leitura/escrita na mesma planilha oficial.
- [ ] Criar novo Zap com trigger "New or Updated Spreadsheet Row" na aba `LEADS`.
- [ ] Adicionar filtro: continuar somente se `Mensagem aprovada?` = "Sim".
- [ ] Adicionar ação "Update Spreadsheet Row": preencher `Data do último contato` com a data atual.
- [ ] (Opcional) Adicionar ação para copiar `Resposta sugerida pela IA` para `Última resposta enviada`, só se decidido que esse valor padrão é útil.
- [ ] Testar com uma linha de teste (marcada claramente como TESTE, conforme `PROMPT_OPERACIONAL_AUTOMACAO_WHATSAPP_VILLA_ARAGUA.md`, seção 9) antes de usar com lead real.
- [ ] Confirmar que o Zap **não** tem nenhuma ação de envio de WhatsApp configurada.

## 10. Confirmações finais

- **Arquivo criado**: `FASE_2_TEMPLATES_SEMI_AUTOMATICOS_VILLA_ARAGUA.md`
- **Caminho**: `/Users/luisrenegomesreis/Desktop/VILLA ARAGUA IA/FASE_2_TEMPLATES_SEMI_AUTOMATICOS_VILLA_ARAGUA.md`
- **Nenhuma skill foi alterada. Nenhum arquivo existente foi alterado.** Este é um arquivo novo, isolado.
- **Nenhuma automação real foi criada nesta tarefa** — nenhum Zap foi configurado de fato, nenhuma conexão com WhatsApp foi feita.

### Arquivos de referência usados (lidos, não alterados)

- `PROMPT_OPERACIONAL_AUTOMACAO_WHATSAPP_VILLA_ARAGUA.md`
- `ARQUITETURA_FOLLOW_UP_AUTOMATICO_VILLA_ARAGUA.md`
- `FASE_1_FOLLOW_UP_MANUAL_ASSISTIDO_VILLA_ARAGUA.md`
- `MAPA_DE_USO_DAS_SKILLS_VILLA_ARAGUA.md`

### Pendência sinalizada

Canal técnico de WhatsApp (API paga) ainda não decidido — ver seção 8. Nenhuma automação de captura/envio real de WhatsApp deve ser construída antes dessa decisão.
