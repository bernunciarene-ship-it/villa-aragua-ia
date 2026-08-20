# Política Keep / Update / Merge / Kill

Regra de decisão para qualquer conteúdo já existente, aplicada depois da auditoria (`auditoria-conteudo.md`). Este arquivo define **o critério de decisão**; `auditoria-conteudo.md` define **o método de avaliação** que alimenta essa decisão.

## As seis classificações

### Manter (Keep)
Aplicar quando o conteúdo passa bem nos nove critérios de `auditoria-conteudo.md`: gera tráfego ou WhatsApp (ou, na ausência de dado de medição, cumpre claramente sua função de ajudar o hóspede), está atualizado, tem dado oficial, diferencia Pousada/Casa quando necessário, tem CTA, é citável, e não compete com outro conteúdo. **Nenhuma ação necessária.**

### Atualizar (Update)
Aplicar quando o tema e a estrutura ainda são bons, mas algo específico está desatualizado ou fraco:
- Dado desatualizado (preço de referência, regra, comodidade que mudou).
- Estrutura fraca em citabilidade (sem resposta direta, sem FAQ, sem H2 em pergunta — ver `seo-otimizacao-conteudo.md`).
- Falta de diferenciação clara entre Pousada e Casa num conteúdo que deveria ter.
**Ação**: gerar um brief de atualização (`brief-conteudo.md`) apontando exatamente o que precisa mudar, sem recriar o conteúdo do zero.

### Unir (Merge)
Aplicar quando duas ou mais peças competem pelo mesmo tema/pergunta (canibalização, ver `seo-otimizacao-conteudo.md`):
- Identificar qual das versões tem a base mais forte (mais completa, mais atualizada, mais citável).
- Consolidar o conteúdo das demais na versão mais forte.
- As versões unidas deixam de existir como páginas separadas (redirecionamento/remoção é decisão técnica de quem executa, não desta skill).
**Ação**: gerar um brief de fusão, listando o que cada versão original contribui para a versão final.

### Reaproveitar (Repurpose)
Aplicar quando o conteúdo em si é bom, mas está preso num formato que não aproveita todo o potencial:
- Existe só como post de Instagram, mas poderia virar página de FAQ também.
- Existe só como seção do guia digital, mas poderia virar artigo de blog citável.
**Ação**: ver `reaproveitamento-conteudo.md` para decompor em outros formatos, sem alterar o conteúdo de origem.

### Arquivar (Archive)
Aplicar quando o conteúdo está obsoleto, mas não há necessidade de removê-lo de vez:
- Campanha de feriado já encerrada (ex.: material de um Natal anterior).
- Conteúdo de uma fase superada da operação (ex.: comunicação de uma reabertura já consolidada há muito tempo).
**Ação**: sinalizar para revisão técnica (despublicar, mover para seção não indexada, ou manter como referência interna) — esta skill recomenda, não remove tecnicamente nada sozinha.

### Apagar (Kill) — somente com aprovação humana
Aplicar apenas quando o conteúdo não tem nenhum valor remanescente (nem histórico, nem de referência) e sua existência pode até confundir ou prejudicar (ex.: informação incorreta que não vale a pena corrigir, conteúdo que nunca deveria ter sido publicado).
**Regra inegociável**: esta skill **nunca decide apagar sozinha**. A classificação "apagar" é sempre uma recomendação a Renildo/equipe, com justificativa clara — a execução da exclusão é sempre humana e sempre aprovada antes.

## Árvore de decisão resumida

```
O conteúdo está correto e atualizado?
├─ Sim → Compete com outro conteúdo do mesmo tema?
│         ├─ Sim → UNIR
│         └─ Não → Está no formato que aproveita todo o potencial?
│                   ├─ Sim → MANTER
│                   └─ Não → REAPROVEITAR
└─ Não → O tema ainda é relevante?
          ├─ Sim → ATUALIZAR
          └─ Não → Tem algum valor de referência/histórico?
                    ├─ Sim → ARQUIVAR
                    └─ Não → Recomendar APAGAR (aprovação humana obrigatória)
```

## Cuidados obrigatórios em qualquer decisão desta política

- Nunca classificar como "apagar" sem justificativa explícita e sem marcar que depende de aprovação humana.
- Nunca "unir" conteúdo de Pousada com o de Casa Arágua — canibalização entre os dois produtos não se resolve fundindo-os, e sim diferenciando melhor (ou criando a página comparativa própria, se ainda não existir).
- Nunca "atualizar" um conteúdo inserindo dado não confirmado só para preencher uma lacuna — se o dado correto não está disponível, marcar como pendência.
- Toda decisão desta política deve conectar-se a uma ação concreta (brief de atualização, brief de fusão, plano de reaproveitamento) — nunca terminar só na classificação, sem próximo passo.

## Como usar este arquivo na prática

1. Partir da ficha de auditoria já preenchida (`auditoria-conteudo.md`).
2. Seguir a árvore de decisão para chegar à classificação.
3. Gerar a ação correspondente: brief de atualização/fusão (`brief-conteudo.md`), plano de reaproveitamento (`reaproveitamento-conteudo.md`), ou recomendação de arquivamento/exclusão (sinalizada para aprovação humana).
4. Registrar a decisão e a justificativa, para que a próxima auditoria (`/content:audit`) saiba o que já foi revisado e por quê.
