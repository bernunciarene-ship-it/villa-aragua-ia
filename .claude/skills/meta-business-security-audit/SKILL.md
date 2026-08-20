# Villa Arágua — Meta Business Security Audit

Esta skill ensina a **auditar riscos de governança no Meta Business Manager** da Villa Arágua — contas de anúncio conectadas, acessos, moedas, e sinais de comprometimento — antes que uma campanha real seja publicada ou sempre que houver suspeita de acesso indevido. Ela nasceu de um achado real: durante uma tentativa de auditoria de campanha via Meta Ads conectado, foram encontradas contas de anúncio nomeadas genericamente como "Read-Only", em moedas incompatíveis com uma operação brasileira (USD, INR), com campanhas sem nenhuma relação com a Villa Arágua, e uma conta desativada pelo próprio Meta por atividade incomum. Ver `MAPA_DO_CEREBRO_IA_VILLA_ARAGUA.md`, seções 15.3, 18 e 20, para o registro completo do caso de origem.

**Regra mais importante da skill, acima de qualquer outra:** esta skill **nunca remove acesso, nunca revoga permissão, nunca altera qualquer conta e nunca publica ou pausa campanha**. Ela só observa e relata. Toda ação corretiva sobre o Business Manager é sempre humana, feita por quem tem acesso administrativo real — fora do escopo de qualquer agente ou skill deste projeto.

## Fontes da verdade (não alterar, só consultar)

- `MAPA_DO_CEREBRO_IA_VILLA_ARAGUA.md`, seção 15.3 ("Governança e segurança do Business Manager") — o caso real que originou esta skill, usado como referência do que é um achado grave.
- `MAPA_DO_CEREBRO_IA_VILLA_ARAGUA.md`, seção 18 (Riscos da arquitetura) — linha "Meta Ads / Business Manager comprometido" e "Publicar campanha com Business Manager inseguro".
- Ferramentas de integração conectadas ao Meta Ads (quando disponíveis nesta sessão) — usadas apenas em modo leitura (listar contas, listar campanhas). Nunca usar uma ferramenta de escrita/edição/publicação a partir desta skill.
- `.claude/agents/villa-risco-escalacao.md` — destino de escalação quando o achado for crítico.
- `.claude/skills/campaign-preflight-checklist/SKILL.md` — skill irmã, que consulta esta auditoria como um dos itens do checklist pré-publicação.

## Quando acionar esta skill

1. **Antes de qualquer publicação de campanha**, se não houver auditoria registrada nos últimos 30 dias (ou o período que Renildo definir).
2. Sempre que `villa-marketing-meta-ads` ou `campaign-preflight-checklist` encontrar algo estranho durante o trabalho normal (conta que não reconhece, erro inesperado de permissão, campanha "some" da lista esperada).
3. Periodicamente, como rotina de governança (ver `MAPA_DO_CEREBRO_IA_VILLA_ARAGUA.md`, seção 19, Fase 2 em diante).

## Como conduzir a auditoria

1. **Listar as contas de anúncio conectadas** (modo leitura) e, para cada uma, observar:
   - Nome da conta é reconhecível como Villa Arágua/Pousada Arágua, ou é genérico/vazio?
   - Moeda é compatível com a operação (BRL)? Moeda estrangeira (USD, INR, ou qualquer outra) sem explicação de negócio é sinal de atenção.
   - `business_name`/`business_id` correspondem ao negócio real da Villa Arágua, ou aparecem vazios/diferentes?
   - Status da conta: ativa, fechada, ou desativada por atividade incomum (motivo relatado pelo próprio Meta)?
2. **Para contas suspeitas, listar as campanhas** (modo leitura): campanhas com nome genérico ("Traffic Campaign", "Sales Campaign", ou qualquer nome sem relação com Pousada/Casa Arágua) dentro de uma conta que deveria pertencer à Villa Arágua são um sinal forte de conta não controlada pela operação real.
3. **Nunca tentar corrigir nada durante a auditoria** — nem remover, nem revogar, nem editar. Se a ferramenta de integração permitir uma ação de escrita, esta skill não a usa.
4. **Classificar o achado** usando a régua abaixo.

## Régua de classificação

- **Seguro:** nenhuma conta/campanha fora do padrão esperado; moedas e nomes consistentes com a operação real.
- **Atenção:** existe conta ou campanha estranha, mas sem sinal de atividade real ou dano (ex.: conta vazia, sem campanhas ativas, moeda estranha mas sem gasto aparente).
- **Crítico:** conta desativada por atividade incomum reportada pelo próprio Meta; conta com campanhas ativas e gasto não reconhecido; qualquer sinal de que alguém fora da operação da Villa Arágua tem acesso e está usando a conta.

## Formato de saída obrigatório

1. **Status geral:** seguro / atenção / crítico.
2. **Achados encontrados:** lista objetiva (conta, moeda, nome, status, campanhas encontradas).
3. **Impacto possível:** o que pode acontecer se o achado não for revisado (fraude de spend, exposição de dados, perda de controle de conta, campanha publicada em ambiente inseguro).
4. **Ação recomendada:** sempre uma recomendação de revisão humana no Business Manager real (nunca uma ação que a skill executaria sozinha).
5. **Decisão humana necessária:** especificar exatamente o que só Renildo (ou quem administra o Business Manager) pode decidir — remover acesso, revogar parceiro, investigar usuário.
6. **A campanha pode seguir para revisão ou deve ser bloqueada até auditoria humana?** Resposta direta: seguir / bloquear até revisão humana. Status **crítico** sempre bloqueia; **atenção** só bloqueia se a campanha estiver na mesma conta do achado; **seguro** libera para seguir o checklist normal (`campaign-preflight-checklist`).

## O que esta skill nunca faz

- Nunca remove acesso de usuário ou parceiro.
- Nunca altera permissão, conta, moeda ou configuração do Business Manager.
- Nunca publica, pausa ou edita campanha.
- Nunca confirma que um achado "crítico" foi resolvido — isso só é confirmado por um humano, depois da revisão real no Meta Business Suite.
- Nunca trata a ausência de acesso de auditoria (ex.: conta não consultável, erro de permissão) como "seguro por padrão" — declara a limitação e recomenda checagem manual.
