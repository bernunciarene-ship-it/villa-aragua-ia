# Villa Arágua — Campaign Preflight Checklist

Esta skill ensina a **rodar o checklist obrigatório antes de publicar qualquer campanha Meta Ads da Villa Arágua** — Pousada Arágua ou Casa Arágua. Ela nasceu do ciclo de campanha do feriado 7 de Setembro 2026 (`SETE 26 QUENTE CWB SC` e `SET 26 FRIO CWB SC`), registrado em `MAPA_DO_CEREBRO_IA_VILLA_ARAGUA.md`, seção 15, e existe para que a Fase 3 daquela rotina de lançamento (auditoria pré-publicação, seção 15.6) vire checklist de fato, não só texto corrido.

**Regra mais importante da skill, acima de qualquer outra:** esta skill **nunca publica, nunca pausa e nunca aprova campanha sozinha**. Ela só diz se a campanha está pronta para revisão humana, precisa de ajuste, ou deve ser bloqueada. A publicação continua sendo sempre um clique humano, de Renildo, depois de ler o resultado desta skill.

## Fontes da verdade (não alterar, só consultar)

- `MAPA_DO_CEREBRO_IA_VILLA_ARAGUA.md`, seção 15 (Aprendizado Meta Ads — Campanha SET 26), especialmente 15.2 (status de campanha e limitação de auditoria em rascunho), 15.4 (automações a recusar) e 15.5 (regra de obsolescência de campanhas antigas).
- `ADENDO_STATUS_CAMPANHA_7_SETEMBRO_2026_OBSOLETA_POS_REVENUE_MANAGER.md` — exemplo real de campanha antiga marcada como histórica/obsoleta; referência do que **não** pode ser reaproveitado.
- `.claude/skills/meta-business-security-audit/SKILL.md` — skill irmã, acionada como item deste checklist quando a auditoria de Business Manager não estiver recente.
- `.claude/agents/villa-marketing-meta-ads.md` — agente que aciona este checklist antes de qualquer publicação.
- `DADOS_OFICIAIS_ATENDIMENTO_VILLA_ARAGUA.md` e a skill `villa-aragua-pricing-revenue` — para checar coerência de preço/mínimo de diárias/disponibilidade, quando aplicável.

## Vocabulário oficial de status de campanha

Use exatamente estes rótulos (mesmo vocabulário do Mapa do Cérebro, seção 15.2/19):

`rascunho` · `publicada` · `em análise` · `ativa` · `pausada` · `encerrada` · `histórica/obsoleta`

**Lembrete crítico:** campanha em `rascunho` normalmente **não aparece plenamente** para auditoria via Meta Ads conectado/API. Se a integração não encontrar a campanha, isso não significa que ela não existe — significa que a auditoria pré-publicação deve ser feita por print/checklist manual (esta skill), não abandonada.

## Checklist obrigatório

Para cada item, responda apenas: **OK**, **AJUSTAR** (com o que falta) ou **BLOQUEADO** (com o motivo).

1. **Produto correto** — a campanha é claramente só Pousada Arágua ou só Casa Arágua? Nenhuma peça mistura os dois.
2. **Status da campanha** — está corretamente identificado (rascunho/publicada/em análise/ativa/pausada/encerrada/histórica-obsoleta)? Se rascunho, auditoria é por print/checklist manual, não por integração.
3. **Coerência período × preço × mínimo de diárias × disponibilidade** — o período anunciado é compatível com o que o Revenue Manager já decidiu para essa data? (consultar `villa-aragua-pricing-revenue` / `villa-precificacao-calendario` se houver dúvida).
4. **Ausência de preço indevido na copy** — nenhum valor, pacote fechado ou desconto aparece no texto, título, descrição ou criativo.
5. **Ausência de promessa de disponibilidade** — nenhuma frase confirma vaga, "última unidade" ou "disponível" sem ressalva de consulta.
6. **Criativo coerente com o produto** — nenhuma imagem/vídeo da Casa Arágua numa campanha da Pousada (ou vice-versa); nenhuma promessa de frente-mar/vista-mar não documentada.
7. **Público correto** — tipo de público (personalizado real, interesse, semelhante) é o que foi decidido para esta campanha, sem ampliação indevida.
8. **Localização correta** — praças incluídas/excluídas conferem com o planejado (ex.: excluir praças fora do plano).
9. **Orçamento correto** — valor total e divisão por conjunto conferem com o decidido; nenhum orçamento Advantage+/compartilhado ativado sem intenção.
10. **WhatsApp correto** — mensagem de boas-vindas aprovada está vinculada, ancora o período certo, não confirma preço nem disponibilidade.
11. **Automações da Meta recusadas quando inadequadas** — geração de texto por IA, mídia flexível, descrição dinâmica, retoques visuais automáticos, expansão de localização e "Aplicar agora" desligados quando a campanha exigir controle (ver seção 15.4 do Mapa do Cérebro).
12. **Business Manager auditado ou pendente de auditoria** — se não houver auditoria recente de `meta-business-security-audit`, este item fica **AJUSTAR** até ela rodar; se a auditoria retornou "crítico", este item fica **BLOQUEADO**.
13. **Campanha antiga não reaproveitada por engano** — nenhum texto, criativo ou configuração vem de campanha marcada como histórica/obsoleta (ex.: `ADENDO_STATUS_CAMPANHA_7_SETEMBRO_2026...`).
14. **Risco de misturar Pousada e Casa** — checagem final, cruzando os itens 1 e 6: nenhuma peça, público ou WhatsApp desta campanha vaza para o outro produto.

## Formato de saída obrigatório

1. **Checklist preenchido** — os 14 itens acima, cada um com OK/AJUSTAR/BLOQUEADO e uma frase de justificativa.
2. **Status final:** `pronto para revisão humana` / `ajustar antes de revisar` / `bloqueado`.
   - `bloqueado` se qualquer item estiver BLOQUEADO (especialmente item 12 crítico, ou qualquer mistura Pousada/Casa).
   - `ajustar antes de revisar` se houver um ou mais AJUSTAR sem nenhum BLOQUEADO.
   - `pronto para revisão humana` só quando todos os itens estiverem OK.
3. **Pontos de atenção** — lista curta do que mais precisa de olhar humano, mesmo quando o status geral for "pronto".
4. **Recomendação objetiva** — uma frase direta (ex.: "ajustar item 4 antes de seguir", "pode ir para revisão de Renildo").
5. **Decisão humana obrigatória** — reforçar que, mesmo com status "pronto para revisão humana", a publicação em si é sempre um clique humano, nunca desta skill.

## O que esta skill nunca faz

- Nunca publica, pausa ou edita a campanha.
- Nunca aprova a campanha sozinha, mesmo com todos os itens OK — o máximo que entrega é "pronta para revisão humana".
- Nunca confirma preço, disponibilidade ou condição comercial ao gerar o checklist.
- Nunca ignora o item 12 (Business Manager) só porque os demais itens estão OK.
