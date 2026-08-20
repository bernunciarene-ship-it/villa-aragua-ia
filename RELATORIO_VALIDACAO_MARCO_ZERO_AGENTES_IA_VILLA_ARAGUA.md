# Relatório de Validação — Marco Zero dos Agentes IA Villa Arágua

**Gerado em:** 2026-07-21
**Natureza deste arquivo:** relatório de validação técnica e operacional dos 9 subagentes instalados em `.claude/agents/`. Não altera nenhum agente, não cria agente novo, não automatiza envio, não decide preço, não confirma reserva, não concede desconto. Este arquivo não altera `DADOS_OFICIAIS_ATENDIMENTO_VILLA_ARAGUA.md`, `.claude/skills/` nem nenhum agente em `.claude/agents/`.

---

## 1. Lista dos 9 agentes instalados (confirmada)

Confirmado por leitura direta de `.claude/agents/` na raiz do projeto:

1. `villa-orquestrador-triagem`
2. `villa-recepcionista-rascunho`
3. `villa-comercial-reservas`
4. `villa-operacional-estadia`
5. `villa-risco-escalacao`
6. `villa-experiencia-tom`
7. `villa-precificacao-calendario`
8. `villa-marketing-meta-ads`
9. `villa-aprendizado-manual`

Todos com `model: sonnet` e uma `color` própria de identificação visual. Nenhum agente a mais, nenhum a menos.

---

## 2. Confirmação de ferramentas — nenhum agente edita, executa ou envia

Cada um dos 9 arquivos foi lido por inteiro. O cabeçalho `tools:` de todos os 9, sem exceção, é:

```yaml
tools: Read, Grep, Glob
```

**Nenhum agente possui `Write`, `Edit`, `Bash` ou qualquer ferramenta de execução, envio ou automação externa.** Isso significa, na prática:

- Nenhum agente pode alterar um arquivo do projeto (só ler).
- Nenhum agente pode rodar comando de sistema, script, API ou integração.
- Nenhum agente pode enviar mensagem a hóspede, lead, WhatsApp, Meta Ads ou qualquer plataforma.
- Tudo que um agente produz é **texto de saída para revisão humana** — nunca uma ação.

Essa restrição está reforçada dentro do próprio texto de cada agente, de forma idêntica nos 9 arquivos: *"Nunca envie mensagem ao hóspede, lead, fornecedor ou plataforma"*, *"Nunca decida preço final, desconto, reembolso, exceção, disponibilidade ou condição comercial"*, *"Todo rascunho deve ser revisado por humano antes de uso"*.

---

## 3. Função de cada agente, em linguagem simples

| Agente | O que ele faz, em uma frase |
|---|---|
| **villa-orquestrador-triagem** | Lê a demanda que chegou e diz qual dos outros agentes deve tratar o caso — é o "porteiro" que evita usar o agente errado. |
| **villa-recepcionista-rascunho** | Você cola uma conversa de WhatsApp inteira e ele devolve a classificação, o risco e um rascunho de resposta pronto para revisão. |
| **villa-comercial-reservas** | Foca só na parte comercial: lead perguntando data, valor, pacote — organiza o que falta saber e sugere o rascunho de resposta, sem fechar nada sozinho. |
| **villa-operacional-estadia** | Cuida das dúvidas de quem já está de reserva feita ou hospedado: check-in, Wi-Fi, piscina, churrasqueira, regras — o dia a dia da estadia. |
| **villa-risco-escalacao** | Entra quando o caso é delicado: reclamação, pedido de reembolso, conflito. Produz uma resposta de contenção rápida e diz que a decisão final é do Renildo. |
| **villa-experiencia-tom** | Não muda o conteúdo — só deixa o texto mais acolhedor, humano e no tom da marca antes de enviar. |
| **villa-precificacao-calendario** | Ajuda a pensar preço e calendário (temporada, feriado, concorrência) em cenários — mas quem decide o valor final é sempre o Renildo. |
| **villa-marketing-meta-ads** | Monta briefing de campanha, copy, criativo e público para Meta Ads/Instagram — só planejamento, nunca sobe ou altera campanha de verdade. |
| **villa-aprendizado-manual** | Olha para casos reais do piloto e sugere o que poderia virar novo modelo de resposta ou nova regra — mas quem aprova é sempre um humano. |

---

## 4. Ordem recomendada de uso no piloto

1. **`villa-orquestrador-triagem`** — sempre o primeiro passo quando não estiver óbvio qual agente usar. Ele classifica (Comercial / Operacional / Risco / Tom / Preço / Marketing / Aprendizado / Lacuna) e indica o próximo agente.
2. **Agente de conteúdo correspondente** — conforme a classificação:
   - Comercial → `villa-comercial-reservas` (ou `villa-recepcionista-rascunho` se for uma conversa inteira colada de uma vez).
   - Operacional → `villa-operacional-estadia`.
   - Risco/reclamação → `villa-risco-escalacao` (pula direto para cá se o caso já chegar visivelmente sensível — não precisa passar pelo orquestrador antes).
3. **`villa-experiencia-tom`** — passada final de forma, sempre depois que o conteúdo já foi decidido pelo agente correto, antes de Rene/Nubia enviarem.
4. **`villa-precificacao-calendario`** e **`villa-marketing-meta-ads`** — usados fora do fluxo reativo de WhatsApp, em momentos de planejamento (semanal/mensal), não em resposta a uma mensagem específica.
5. **`villa-aprendizado-manual`** — usado no fechamento do dia/semana, para consolidar casos reais em possíveis templates ou regras novas, sempre com aprovação do Renildo antes de qualquer mudança virar oficial.

---

## 5. Cinco testes práticos

**Nota de execução importante:** tentei invocar os agentes diretamente nesta sessão pela ferramenta de subagentes e recebi o erro `Agent type 'villa-comercial-reservas' not found. Available agents: claude, claude-code-guide, Explore, general-purpose, Plan, statusline-setup` — ou seja, **esta interface específica não reconhece os subagentes de `.claude/agents/` como invocáveis via essa ferramenta**. Isso é coerente com o `README_INSTALACAO.md`, que descreve o uso dentro do **Claude Code no terminal/VSCode**, pedindo algo como *"Use o agente villa-recepcionista-rascunho para..."* diretamente no prompt — um caminho diferente do usado aqui.

Por isso, os 5 testes abaixo foram feitos como **simulação manual fiel**: apliquei exatamente as regras, o fluxo e o formato de "Saída obrigatória" definidos no arquivo real de cada agente ao cenário de teste. Isso valida se o *desenho* do agente produz uma saída seguro e coerente — mas **não substitui um teste real dentro do Claude Code/VSCode**, que é o próximo passo recomendado antes de considerar o piloto tecnicamente validado de ponta a ponta.

---

### Teste 1 — WhatsApp comercial simples (`villa-comercial-reservas`)

**Cenário:** lead manda "Oi, vocês tem vaga pra um final de semana em agosto? Somos eu e minha esposa."

**Saída simulada:**
1. **Diagnóstico do lead:** casal, sem data exata, sem menção a criança ou pet, sem indicar produto.
2. **Produto mais provável:** Pousada Arágua — hipótese operacional baseada no perfil casal, não confirmada pelo lead.
3. **Dados faltantes:** data exata do fim de semana em agosto, se há criança/pet, motivo da viagem (descanso, comemoração).
4. **Risco comercial:** baixo (equivalente a C1/C2 — ainda não pediu valor).
5. **Rascunho para humano revisar:** "Oi! Que bom que você chegou até a gente 😊 Adoraria te ajudar a organizar isso certinho — qual fim de semana de agosto vocês estão pensando?"
6. **Observação para Renildo:** nenhuma pendência sensível; seguir qualificação normal antes de falar em disponibilidade/valor.

**Resultado:** ✅ aprovado — respeita a regra de não confirmar disponibilidade nem preço, e devolve pergunta de qualificação em vez de resposta pronta.

---

### Teste 2 — WhatsApp operacional simples (`villa-operacional-estadia`)

**Cenário:** hóspede já hospedado escreve "O Wi-Fi não está pegando no meu quarto, o que eu faço?"

**Saída simulada:**
1. **Classificação N1–N4:** N2 (dúvida simples, já com reserva ativa).
2. **Tema operacional:** Wi-Fi.
3. **O que sabemos:** fluxo oficial documentado — confirmar rede/senha, reiniciar roteador, reiniciar equipamento principal, acionar suporte se não resolver.
4. **Lacunas:** qual acomodação, se já tentou reiniciar o roteador.
5. **Risco:** baixo, mas pode virar reclamação se não resolvido dentro da meta de 30 minutos.
6. **Rascunho para humano revisar:** "Oi! Poxa, vamos resolver isso rapidinho 😊 Consegue me confirmar o nome da rede que aparece no seu celular? Enquanto isso já vou verificar o roteador por aqui."
7. **Escalação necessária:** só se não resolver em até 30 minutos — aí aciona manutenção/Renildo.

**Resultado:** ✅ aprovado — segue exatamente o fluxo oficial de Wi-Fi do `CLAUDE.md`/`OPERACAO/`, sem inventar passo técnico novo.

---

### Teste 3 — Reclamação sensível (`villa-risco-escalacao`)

**Cenário:** hóspede reclama "A piscina estava suja quando chegamos e ninguém avisou, isso estragou nosso primeiro dia."

**Saída simulada:**
1. **Tipo de risco:** reclamação operacional com impacto na primeira impressão da estadia.
2. **Gravidade:** média-alta.
3. **Por que é sensível:** compromete o início da experiência e tem risco real de virar avaliação negativa.
4. **Quem deve decidir:** Renildo (qualquer gesto de boa vontade ou compensação).
5. **Resposta de contenção para humano revisar:** "Poxa, sinto muito por isso — não é o que a gente quer que vocês vivam aqui. Já vou verificar com a nossa equipe o que aconteceu com a piscina e volto com uma solução."
6. **Próximos passos internos:** confirmar com o piscineiro o que houve, checar se já foi resolvido, considerar retorno ao hóspede depois da estadia.
7. **Registro sugerido para aprendizado:** candidato a checklist de pré-chegada — conferir piscina antes de cada check-in.

**Resultado:** ✅ aprovado — reconhece o problema sem assumir culpa indevida, não promete reembolso/desconto, escala corretamente para Renildo.

---

### Teste 4 — Campanha Meta Ads (`villa-marketing-meta-ads`)

**Cenário:** "Preciso de um briefing de campanha para a Casa Arágua Mariscal, focado em outubro, público de casais."

**Saída simulada:**
1. **Produto:** Casa Arágua Mariscal.
2. **Objetivo da campanha:** gerar conversas qualificadas no WhatsApp para outubro (baixa/média temporada, foco casal).
3. **Público:** casais 25–55 anos buscando privacidade e tranquilidade — hipótese operacional, a validar com dado real de público.
4. **Promessa:** privacidade, casa completa, piscina privativa, churrasqueira — nunca citar "piscina aquecida" (não documentado para a Casa).
5. **Criativo:** imagem real da casa/piscina privativa, sem sugerir vista-mar ou distância exata da praia.
6. **Texto principal:** foco em "só para vocês dois", sem preço, sem urgência.
7. **CTA:** convite para conversa no WhatsApp, não para "reservar agora".
8. **WhatsApp / próxima conversa:** a Recepcionista precisa confirmar exatamente o que o anúncio prometeu, sem inventar diferencial novo.
9. **Métrica principal:** conversas qualificadas geradas, não apenas cliques.
10. **Riscos de promessa:** citar piscina aquecida, garagem coberta (termo desatualizado) ou distância exata da praia.
11. **Aprovações necessárias:** Renildo aprova orçamento, oferta e criativo final antes de qualquer publicação real.

**Resultado:** ✅ aprovado — mantém a separação Pousada x Casa, não decide orçamento nem sobe campanha, sinaliza riscos de promessa corretamente.

---

### Teste 5 — Aprendizado manual de um caso real (`villa-aprendizado-manual`)

**Cenário:** registro do piloto — "Hóspede perguntou três vezes seguidas sobre política de pet de porte grande antes de decidir reservar, e não existe um texto padrão específico para isso na Biblioteca Comercial."

**Saída simulada:**
1. **Registro analisado:** dúvida recorrente sobre pet de porte grande, sem template de resposta padrão.
2. **Padrão identificado:** lacuna específica — pet "fora do padrão documentado" (porte grande) trava a qualificação do lead.
3. **Lacuna ou oportunidade:** falta resposta padrão para pet de porte não coberto pela regra geral.
4. **Candidato a template:** texto de acolhimento que direciona para consulta prévia sem negar nem confirmar de antemão.
5. **Regra candidata:** "pet de porte grande sempre encaminhado para checagem humana antes de qualquer resposta."
6. **Risco de duplicidade:** checar se `DADOS_OFICIAIS_ATENDIMENTO_VILLA_ARAGUA.md` já cobre isso antes de criar template novo.
7. **Precisa de aprovação de Renildo:** sim — antes de qualquer template novo entrar em uso.
8. **Próximo teste sugerido:** simular a mesma pergunta com pet de porte pequeno, para comparar as duas respostas.

**Resultado:** ✅ aprovado — não aprova o template sozinho, não altera fonte oficial, devolve apenas uma hipótese para revisão humana.

---

## 6. Riscos do piloto

- **Risco técnico confirmado nesta sessão:** os agentes não foram testados dentro do ambiente onde de fato rodarão (Claude Code no terminal/VSCode) — o teste real de invocação (`Use o agente villa-x para...`) ainda precisa ser feito lá antes de considerar o piloto tecnicamente validado.
- **Rascunho tratado como resposta final:** maior risco de uso incorreto é Rene/Nubia copiarem e enviarem o rascunho sem revisar — os agentes dependem 100% da revisão humana, pois não têm poder de envio.
- **Pular o orquestrador:** usar direto o agente "errado" (ex.: tratar uma reclamação como operacional simples) pode gerar uma resposta mais fraca do que a de `villa-risco-escalacao`.
- **Sobreposição de nomenclatura:** o `villa-orquestrador-triagem` usa N1–N4 e C1–C4 — a mesma nomenclatura já usada pela Biblioteca Comercial da Recepcionista IA. É preciso garantir que as duas classificações continuem coerentes entre si, e não confundir com o QL1–QL4/NQ criado depois para qualificação de leads (namespaces diferentes, propósitos diferentes).
- **Dependência da qualidade da fonte oficial:** como nenhum agente inventa dado, se um arquivo oficial estiver desatualizado (ex.: "garagem" na Casa Arágua), o agente pode herdar a imprecisão se não for orientado a usar o termo corrigido.
- **Excesso de agentes por tarefa:** sem necessidade real, rodar vários agentes para o mesmo caso simples desperdiça tempo — o fluxo recomendado (seção 4) existe justamente para evitar isso.
- **Falsa sensação de automação:** por serem "agentes de IA", pode surgir a tentação de pular a revisão humana com o tempo — reforçar que **nenhum agente decide preço, desconto, reembolso, disponibilidade ou reserva**, sempre.

---

## 7. Regra de uso diário — Renildo, Rene e Nubia

1. **Na dúvida sobre qual agente usar, comece pelo `villa-orquestrador-triagem`.**
2. **Reclamação, conflito ou pedido de reembolso/desconto vai direto para `villa-risco-escalacao`** — não esperar classificação prévia se o caso já é visivelmente sensível.
3. **Nenhum rascunho é enviado sem leitura humana antes.** Todo texto gerado é ponto de partida, nunca resposta pronta para copiar e colar sem checar.
4. **Nenhum agente decide preço, desconto, reembolso, disponibilidade ou reserva.** Se algum rascunho parecer estar decidindo isso, pare e revise manualmente — não é o comportamento esperado.
5. **Passe pelo `villa-experiencia-tom` antes de enviar** qualquer mensagem que pareça seca, robótica ou fria — sem mudar o conteúdo decidido.
6. **Ao final do dia (ou da semana), registre 1–3 casos reais** e leve para o `villa-aprendizado-manual` — isso é o que constrói o aprendizado do piloto ao longo do tempo.
7. **Nenhuma pendência ("LACUNA / precisa de confirmação humana") deve ser respondida no impulso** — sempre buscar a confirmação real antes de responder ao hóspede/lead.

---

## 8. Conclusão — os agentes estão prontos para piloto assistido?

**Sim, com uma ressalva.** Os 9 agentes estão **prontos para uso em piloto assistido/rascunho** — a arquitetura de segurança está correta e consistente nos 9 arquivos (somente `Read, Grep, Glob`, nenhuma ferramenta de escrita, execução ou envio; regras máximas idênticas e reforçadas em todos; toda saída aponta explicitamente para revisão humana e escalação a Renildo quando necessário). As 5 simulações práticas confirmam que o desenho de cada agente produz saída coerente, segura e alinhada às regras do projeto.

A ressalva: **o teste real de invocação dentro do Claude Code (terminal/VSCode)** — o ambiente para o qual os agentes foram de fato desenhados, conforme `README_INSTALACAO.md` — ainda não foi feito, porque esta sessão não reconhece os agentes customizados como invocáveis pela ferramenta usada aqui. Antes de declarar o Marco Zero **totalmente** encerrado, recomenda-se que Renildo/Rene/Nubia façam pelo menos os mesmos 5 testes diretamente no Claude Code, digitando algo como "Use o agente villa-comercial-reservas para..." — validando que a invocação real funciona exatamente como a simulação prevista aqui.

**Status do Marco Zero: aprovado para piloto assistido, com teste real de invocação pendente como próximo passo imediato.**
