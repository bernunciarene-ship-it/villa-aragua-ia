# AUDITORIA ARQUITETURAL — VIDEO FACTORY IA — VILLA ARÁGUA

**Status do documento:** Auditoria aprovada por Renildo, com ajustes obrigatórios incorporados.
**Status do agente:** EM FORMALIZAÇÃO — NÃO ATIVO EM PRODUÇÃO (ver seção 34).
**Gerado em:** 2026-07-24
**Natureza deste arquivo:** auditoria arquitetural. Não cria agente, não cria skill, não altera código Remotion, não move nem renomeia pastas/arquivos, não implementa integração entre projetos. Todo conteúdo abaixo é classificado explicitamente como **[FATO]**, **[DECISÃO APROVADA]**, **[PROPOSTA FUTURA]**, **[PENDÊNCIA]** ou **[HIPÓTESE]** — nenhuma proposta futura deve ser lida como regra já implementada.

---

## 0. Escopo e método

**[FATO]** Esta auditoria inspecionou:
- `CLAUDE.md` e `MAPA_DO_CEREBRO_IA_VILLA_ARAGUA.md`, neste projeto (`VILLA ARAGUA IA/`).
- As 12 skills de negócio em `VILLA ARAGUA IA/.claude/skills/`.
- Os 9 agentes formalizados em `VILLA ARAGUA IA/.claude/agents/`.
- `MAPA_DE_USO_DAS_SKILLS_VILLA_ARAGUA.md`, `DEFINICAO_AGENTES_VILLA_ARAGUA_IA.md`, `AUDITORIA_VISUAL_CRIATIVOS_BRIEFING_01_POUSADA_ARAGUA.md`.
- A pipeline técnica de vídeo real, localizada **fora** deste projeto, em `/Users/luisrenegomesreis/Desktop/my-video/` (repositório git próprio, `package.json`, `remotion.config.ts`), incluindo as 9 skills técnicas em `my-video/.claude/skills/` e seus arquivos de saída já gerados.

**[FATO]** Nenhuma menção a "Remotion", "Video Factory" ou pipeline audiovisual foi encontrada em nenhum `.md` da raiz de `VILLA ARAGUA IA/` antes desta auditoria (busca por grep, resultado vazio). Este é um domínio novo para este projeto.

---

## 1. Diagnóstico da lacuna atual

**[FATO]** A pipeline técnica em `my-video/` já foi executada estruturalmente hoje (2026-07-24): existem `storyboard-spec.json`, `composition-spec.json` (68 KB), `asset-manifest.json`, guidelines de arte, 3 previews de cena da Pousada Arágua (`pousada-scene-01/02/03-preview.png`) e relatórios de preflight.

**[FATO]** O gate determinístico de `remotion-composition-director` (arquivo `validation-rules.md` + `validator/validate-composition-spec.js`) valida exclusivamente **conformidade estrutural**: todos os campos obrigatórios presentes, valores numéricos, ranges normalizados válidos, crop fechado por breakpoint, safe area numérica por formato, tokens de tipografia completos por breakpoint, sombras com 6 parâmetros, e rejeição de linguagem qualitativa vaga ("suave", "leve", "aproximadamente") **dentro dos campos determinísticos**. O gate de saída é binário: `READY_FOR_ENGINEER` ou `NOT_READY`.

**[FATO]** O `remotion-video-reviewer` valida, antes do render: timing (±100ms da spec), sincronismo áudio/visual (<50ms), cor (HEX exato vs. guideline), tipografia (fonte/tamanho/peso exatos vs. spec), responsividade (sem overflow em 4 formatos), performance (FPS, memória, CPU) e ausência de erros de console. Também é validação de **fidelidade à especificação**, não de qualidade da especificação em si.

**Lacuna real:** nenhuma das duas etapas — nem nenhuma outra skill técnica — responde às perguntas "essa composição é visualmente forte?", "o produto é o protagonista visual?", "esse crop vende a acomodação?", "a fonte escolhida combina com o DNA da marca?", "o CTA tem peso visual suficiente?". Uma composição pode passar em 100% dos checks determinísticos e ainda assim ser comercialmente fraca — exatamente o problema relatado na motivação deste projeto. Essa lacuna é estrutural do pipeline `my-video`, não um bug: as skills Remotion são deliberadamente genéricas e reutilizáveis (evidência: a mesma pasta de skills gerou um preflight para "MANECO Skate Test 01"), portanto não incorporam nem podem incorporar critério de marca/negócio da Villa Arágua por padrão.

---

## 2. Papel exato do Video Factory IA

**[DECISÃO APROVADA]** O Video Factory IA é um **agente de execução audiovisual** (Camada 2). Ele recebe um briefing estratégico já aprovado por Renildo e o transforma em produção audiovisual tecnicamente correta, visualmente forte e comercialmente útil, orquestrando as skills técnicas já existentes em `my-video/` e aplicando, entre duas delas, um gate qualitativo de negócio que hoje não existe (seção 9 e 18).

Ele produz apenas para: Pousada Arágua, Casa Arágua Mariscal, comunicação institucional da Villa Arágua.

---

## 3. O que ele não é

- Não é um novo agente de Marketing — não decide objetivo, público, promessa, oferta ou orçamento.
- Não escreve copy do zero — recebe copy já aprovada.
- Não é uma skill técnica nova — orquestra as 9 já existentes.
- Não substitui `villa-marketing-meta-ads`, `remotion-composition-director`, `remotion-video-reviewer` ou qualquer outra skill/agente já formalizado.
- Não produz para MANECO em nenhuma circunstância.

---

## 4. Relação com Marketing & Meta Ads IA

**[FATO]** O agente `villa-marketing-meta-ads` (`.claude/agents/villa-marketing-meta-ads.md`) já lista "criativo" e "roteiros de vídeo" entre suas saídas possíveis, e já usa `villa-aragua-creative-design-ads`, `villa-aragua-copywriting-conversion`, `villa-aragua-marketing-psychology` e `villa-aragua-humanizer-pt-br` como skills de apoio.

**[DECISÃO APROVADA]** Fluxo unidirecional: `villa-marketing-meta-ads` (ou Renildo diretamente) define/aprova objetivo, público, promessa, oferta, copy e conceito → esse pacote vira o briefing de entrada do Video Factory IA (seção 32) → Video Factory nunca redecide nenhum desses elementos, só os traduz em produção audiovisual. Sem duplicidade de função entre os dois agentes.

---

## 5. Relação com as skills de negócio

**[DECISÃO APROVADA]** Skills de negócio acionadas pelo Video Factory IA, sempre como lente de apoio/julgamento sobre um briefing já aprovado, nunca para redecidir estratégia:
- `villa-aragua-content-strategy`, `villa-aragua-growth-marketer`, `villa-aragua-marketing-psychology`, `villa-aragua-copywriting-conversion`, `villa-aragua-creative-design-ads`, `villa-aragua-humanizer-pt-br`.
- `villa-aragua-campaign-analytics` entra apenas depois da publicação real, quando houver métrica — consistente com `MAPA_DE_USO_DAS_SKILLS_VILLA_ARAGUA.md`.

Nenhuma skill de negócio é duplicada, ampliada ou alterada por esta arquitetura.

---

## 6. Relação com as skills técnicas de vídeo

**[FATO]** Mapeamento real (nomes verificados em `my-video/.claude/skills/`, sem renomear nada):

`remotion-style-replicator` → `remotion-art-director` → `remotion-storyboard` → `remotion-asset-manager` → `remotion-composition-director` → **[gate qualitativo do Video Factory — seção 9]** → `remotion-engineer` → `remotion-motion-blueprint` → `remotion-video-reviewer` → `remotion-render-manager`.

**[FATO]** Não existem skills separadas chamadas "Composition Validator" ou "Preflight Reviewer" — são sub-capacidades: o validador determinístico vive dentro de `remotion-composition-director/validator/`, e o preflight vive dentro da saída de `remotion-video-reviewer/output/preflight/`. O Video Factory IA deve referenciar essas 9 skills pelos nomes reais acima, nunca inventar nomes novos.

**[DECISÃO APROVADA — item 1 dos ajustes]** O agente Video Factory IA é definido em `VILLA ARAGUA IA/.claude/agents/`. O projeto `my-video` permanece como motor técnico Remotion separado. O acesso às skills técnicas por caminho absoluto de disco é **solução temporária de desenvolvimento**, não a arquitetura definitiva.

**[PENDÊNCIA]** Registrar explicitamente:
- Caminho absoluto (`/Users/luisrenegomesreis/Desktop/my-video/.claude/skills/...`) não deve ser tratado como parte permanente da arquitetura.
- A solução final deve ser portátil — não pode depender de um diretório específico desta máquina.
- A integração futura entre `VILLA ARAGUA IA` e `my-video` deve ocorrer por configuração, workspace formal ou contrato estruturado entre os dois projetos (ex.: um arquivo de configuração que declare onde vive o motor técnico, versionável e substituível).
- Até essa integração portátil existir, qualquer execução do Video Factory IA depende de configuração manual do caminho, feita conscientemente por quem opera o agente.

---

## 7. Entradas obrigatórias

**[PROPOSTA FUTURA — modelo de briefing completo na seção 32]**
- Briefing estratégico aprovado por Renildo (produto, objetivo, público, promessa, oferta/CTA, copy, conceito visual, formato/duração, referências visuais).
- Identificação explícita: Pousada Arágua **ou** Casa Arágua **ou** institucional — nunca ambíguo, nunca misto.
- Lista de assets já aprovados e existentes (o agente nunca gera, baixa ou deriva asset novo).
- Formatos/breakpoints alvo (9:16, 4:5, 1:1, 16:9 — conforme já suportado por `remotion-composition-director`).

---

## 8. Saídas obrigatórias

- Storyboard (`remotion-storyboard`).
- Guidelines de arte (`remotion-art-director`) e spec de estilo (`remotion-style-replicator`).
- Asset manifest + asset report (`remotion-asset-manager`).
- Composition spec + notes (`remotion-composition-director`).
- **Relatório do gate qualitativo visual/comercial** (novo, seção 9 e 18) — APROVADO / REVISAR / REJEITADO.
- Motion spec (`remotion-motion-blueprint`).
- Implementação Remotion (`remotion-engineer`).
- Review report + checklist + performance report (`remotion-video-reviewer`).
- Relatório final de produção (modelo na seção 33).

---

## 9. Gates de aprovação humana

**[DECISÃO APROVADA]** Sequência completa de gates, todos bloqueadores:

1. Aprovação do briefing estratégico por Renildo — antes do agente começar.
2. Aprovação humana do storyboard + direção de arte.
3. Saída determinística `READY_FOR_ENGINEER` do `remotion-composition-director` (gate técnico existente, inalterado).
4. **Gate qualitativo visual e comercial do Video Factory IA** (item 3 dos ajustes — detalhado na seção 18): classificação APROVADO / REVISAR / REJEITADO. **O Engineer só pode começar quando este gate estiver APROVADO.** Este gate não é uma skill nova — usa `villa-aragua-creative-design-ads`, `villa-aragua-marketing-psychology`, `villa-aragua-copywriting-conversion` e as regras do DNA da Villa Arágua como lentes de julgamento, dentro do próprio Video Factory IA.
5. Aprovação do `remotion-video-reviewer` (técnico + visual + sincronismo + performance).
6. Aprovação final explícita de Renildo antes do `remotion-render-manager` renderizar.
7. Publicação sempre manual, fora do agente, fora desta arquitetura.

---

## 10. Limites de decisão

O Video Factory IA **pode**: interpretar briefing aprovado, selecionar pipeline (simples ou premium), acionar as 9 skills técnicas existentes, organizar storyboard, selecionar assets já aprovados, aplicar o gate qualitativo, definir composição/tipografia/movimento dentro das especificações determinísticas das skills técnicas, gerar preflight, implementar via `remotion-engineer`, validar lint/TypeScript, preparar render, produzir relatório de produção.

O Video Factory IA **não pode**: escolher preço final, decidir desconto, inventar promoção, decidir orçamento de Meta Ads, definir sozinho o público final, inventar benefício ou amenidade, misturar Pousada e Casa, usar assets do MANECO, alterar o DNA da marca, publicar conteúdo, subir campanha, renderizar antes do gate 6 (seção 9), modificar documento-fonte sem autorização, criar skill nova sem lacuna demonstrada.

---

## 11. Documentos-fonte consultados

`CLAUDE.md`, `MAPA_DO_CEREBRO_IA_VILLA_ARAGUA.md`, `MAPA_DE_USO_DAS_SKILLS_VILLA_ARAGUA.md`, `DEFINICAO_AGENTES_VILLA_ARAGUA_IA.md`, `.claude/agents/villa-marketing-meta-ads.md`, `AUDITORIA_VISUAL_CRIATIVOS_BRIEFING_01_POUSADA_ARAGUA.md`, `DNA VILLA ARAGUA/DNA Villa Arágua (1).txt` (referenciado pelo CLAUDE.md para regras de marca), e os 9 `SKILL.md` de `my-video/.claude/skills/`.

---

## 12. Arquivos que pode criar

**[PROPOSTA FUTURA, condicionada à ativação — seção 34]** Storyboards, guidelines, manifests, composition specs, motion specs, relatórios de gate qualitativo, review reports, relatório final de produção — todos dentro de uma estrutura de output segregada por projeto/marca (seção 15 e ajuste 2), nunca em pasta compartilhada sem namespace.

---

## 13. Arquivos que pode modificar

Apenas seus próprios artefatos de output gerados durante a mesma execução (specs intermediárias, storyboard, composition spec) — nunca arquivos de outra skill fora do fluxo, nunca documento-fonte de negócio.

---

## 14. Arquivos que nunca pode modificar sem autorização

`CLAUDE.md`, `MAPA_DO_CEREBRO_IA_VILLA_ARAGUA.md`, `MAPA_DE_USO_DAS_SKILLS_VILLA_ARAGUA.md`, qualquer `SKILL.md` (de negócio ou técnica), qualquer `.claude/agents/*.md`, `DADOS_OFICIAIS_ATENDIMENTO_VILLA_ARAGUA.md`, as duas Bibliotecas (Operacional/Comercial), assets de origem, `remotion.config.ts`, `package.json`.

---

## 15. Separação entre Pousada Arágua e Casa Arágua

**[DECISÃO APROVADA]** Herdada da regra já vigente em `MAPA_DE_USO_DAS_SKILLS_VILLA_ARAGUA.md` (seção 7): nunca misturar posicionamento, promessas, amenities, imagens, textos, públicos ou preços dos dois produtos na mesma peça, salvo peça explicitamente comparativa e identificada como tal. Todo briefing de entrada declara um produto único (seção 7).

**[DECISÃO APROVADA — item 2 dos ajustes, pré-requisito de ativação]** Isolamento físico obrigatório de outputs, também entre Villa Arágua e MANECO — ver estrutura mínima na seção 27.

---

## 16. Critérios técnicos de qualidade

Herdados sem alteração do `remotion-composition-director` e `remotion-video-reviewer`: todos os campos obrigatórios presentes e numéricos; crop fechado por breakpoint; safe area numérica por formato; z-index único; sombras com 6 parâmetros; timing ±100ms; sincronismo <50ms; zero erros de console; FPS médio >25; responsividade sem overflow em 9:16, 4:5, 1:1, 16:9.

---

## 17. Critérios visuais de qualidade (novo — gate do Video Factory)

Ver lista completa na seção 18 (o gate avalia visual e comercial em conjunto, por decisão do ajuste 3).

---

## 18. Critérios comerciais de qualidade — Gate Qualitativo Visual e Comercial

**[DECISÃO APROVADA — item 3 dos ajustes]** Gate posicionado entre `remotion-composition-director` e `remotion-engineer`. Não é uma skill nova — é uma etapa de julgamento dentro do próprio Video Factory IA, usando como lentes: `villa-aragua-creative-design-ads`, `villa-aragua-marketing-psychology`, `villa-aragua-copywriting-conversion`, as regras do DNA da Villa Arágua, e a separação obrigatória Pousada x Casa.

Critérios mínimos avaliados, cada um com nota/observação, não apenas sim/não:
1. Força visual da composição.
2. Protagonismo do produto (a acomodação/casa é o elemento dominante, não um detalhe).
3. Clareza da promessa central.
4. Qualidade do crop (o crop favorece o produto, não corta elemento essencial).
5. Hierarquia tipográfica (o que deve ser lido primeiro é lido primeiro).
6. Legibilidade (contraste, tamanho, densidade de texto).
7. Posicionamento dos textos (não conflita com o foco visual).
8. Excesso de sobreposição (texto sobre texto, texto sobre elemento crítico da imagem).
9. Equilíbrio entre imagem e texto.
10. Uso de espaço negativo (a composição respira ou está poluída).
11. Coerência da fonte com o tom "Férias Pra Sempre" da marca.
12. Peso visual do CTA (visível, mas não agressivo).
13. Clareza nos primeiros 2 segundos (para formato vídeo/reels).
14. Adequação ao público declarado no briefing.
15. Coerência comercial geral com o objetivo do briefing.
16. Ausência de overpromise (nenhuma promessa não documentada — vista-mar, piscina aquecida, exclusividade não confirmada).
17. Consistência com o briefing estratégico aprovado.

**Classificações permitidas:** `APROVADO`, `REVISAR`, `REJEITADO`. Only `APROVADO` libera o `remotion-engineer` para começar.

---

## 19. Critérios de tipografia

Dentro do gate (seção 18, item 5/6/11): a fonte deve estar entre as já definidas por `remotion-art-director`/`remotion-style-replicator` para o projeto; hierarquia clara entre título/subtítulo/CTA; peso e tamanho compatíveis com o tom "acolhedor, simples, humano" do CLAUDE.md — nunca fontes que transmitam frieza corporativa ou urgência agressiva.

## 20. Critérios para texto sobre imagem

Contraste suficiente para legibilidade em todos os formatos; nunca sobrepor rosto, produto principal ou elemento de prova social; usar overlay/gradiente (já suportado pelo schema de `remotion-composition-director`) quando o fundo variar em luminosidade.

## 21. Critérios de safe area

Herdados do schema determinístico já existente (`safe_area` por breakpoint, numérico, obrigatório) — o gate qualitativo verifica adicionalmente se o valor definido é suficiente para a plataforma de destino (Stories/Reels cortam topo/base para UI nativa).

## 22. Critérios para seleção e crop de assets

Apenas assets já aprovados por `remotion-asset-manager`; crop deve favorecer o produto como protagonista (item 2 do gate); nunca cortar elemento que comunique a promessa central; seguir o padrão já usado na auditoria visual manual (`AUDITORIA_VISUAL_CRIATIVOS_BRIEFING_01_POUSADA_ARAGUA.md`) — preferir imagem real, sem pessoas quando gerar risco de exposição, nunca imagem de IA.

## 23. Critérios de CTA

CTA deve ter peso visual claro (item 12 do gate), nunca competir com o elemento hero, texto do CTA vem do briefing aprovado (o agente não inventa CTA), nunca cria urgência falsa (herdado das regras de proteção comercial do `MAPA_DE_USO_DAS_SKILLS_VILLA_ARAGUA.md`).

## 24. Critérios para preflight

Preflight técnico (herdado do `remotion-video-reviewer`) + preflight visual/comercial (gate da seção 18) juntos formam o preflight completo exigido antes do Engineer prosseguir para render.

## 25. Critérios para motion

Herdados do `remotion-motion-blueprint`: determinístico, frame-accurate, sem linguagem qualitativa; o gate qualitativo (seção 18, item 13) verifica adicionalmente clareza nos primeiros 2 segundos, relevante especialmente para Reels/Stories.

## 26. Critérios para aprovação do Engineer

O `remotion-engineer` só inicia implementação quando: (a) `remotion-composition-director` retornar `READY_FOR_ENGINEER`, e (b) o gate qualitativo da seção 18 retornar `APROVADO`. Se `REVISAR` ou `REJEITADO`, o fluxo retorna para composição/storyboard, nunca avança para código.

---

## 27. Riscos de duplicidade

**[FATO]** Baixo — as skills técnicas Remotion não sobrepõem função com nenhuma das 12 skills de negócio. O único ponto de atenção é nomenclatura: nomes conceituais do briefing original ("Composition Validator", "Preflight Reviewer") não são skills próprias (seção 6) — o documento final do agente deve usar os 9 nomes reais.

## 28. Riscos de overpromise

**[HIPÓTESE — a confirmar em teste]** Se o Video Factory herdar um asset ou composição sem reforçar as regras de proteção comercial (nunca vista-mar, nunca piscina aquecida na Pousada, nunca misturar Pousada/Casa, nunca urgência falsa), pode aprovar tecnicamente um vídeo com promessa proibida. Mitigação: o gate da seção 18 (item 16) e a herança explícita das regras do `MAPA_DE_USO_DAS_SKILLS_VILLA_ARAGUA.md` seção 7 são obrigatórias na formalização do agente.

## 29. Riscos de consumo excessivo de créditos

**[HIPÓTESE]** Alto se toda execução rodar a cadeia completa de 9 skills + gate qualitativo + 4 breakpoints + motion completo, mesmo para uma peça simples. Mitigação: dois modos de pipeline (seções 30 e 31), escolhidos conforme complexidade do briefing.

## 30. Pipeline simples para Villa Arágua

**[PROPOSTA FUTURA]** Para peças recorrentes (ex.: 1 formato, sem motion complexo, storyboard curto): `storyboard` → `art-director`/`style-replicator` (se já existente, reaproveitar) → `asset-manager` → `composition-director` → **gate qualitativo** → `engineer` → `video-reviewer` (checklist reduzido) → `render-manager`. Menos breakpoints, menos iterações.

## 31. Pipeline premium para projetos mais complexos

**[PROPOSTA FUTURA]** Para peças institucionais ou datas estratégicas (ex.: campanha de feriado, vídeo institucional): pipeline completa nos 4 breakpoints, `motion-blueprint` detalhado, gate qualitativo com revisão mais extensa, `video-reviewer` completo (timing/sync/performance/responsividade nos 4 formatos).

## 32. Modelo de briefing de entrada

**[PROPOSTA FUTURA]**
```
Produto: [Pousada Arágua | Casa Arágua | Institucional]
Objetivo da peça:
Público:
Promessa central (já aprovada):
Oferta/CTA (já aprovado):
Copy aprovada (texto principal, título, descrição):
Conceito visual/referências:
Formato(s) e duração:
Assets aprovados disponíveis:
Aprovação do briefing por: Renildo — [data]
```

## 33. Modelo de relatório final

**[PROPOSTA FUTURA]**
```
Projeto:
Produto (Pousada/Casa/Institucional):
Pipeline usada (simples/premium):
Status de cada gate (1 a 7, seção 9):
Gate qualitativo — classificação e observações (seção 18):
Riscos identificados:
Pendências antes do render:
Aprovação final de Renildo: [pendente/concedida]
Arquivos gerados (com caminho, dentro da estrutura segregada da seção 27):
```

## 34. Status proposto do agente

**[DECISÃO APROVADA]** **EM FORMALIZAÇÃO — NÃO ATIVO EM PRODUÇÃO.**

Motivos:
- Auditoria aprovada.
- Arquitetura definida.
- Falta persistir o agente (`.claude/agents/video-factory-ia.md`, ainda não criado).
- Falta implementar isolamento físico de outputs por projeto/marca (seção 15, pré-requisito de ativação, não opcional).
- Falta validar o contrato de integração entre `VILLA ARAGUA IA` e `my-video` (hoje é caminho absoluto temporário, seção 6).
- Falta testar o novo gate qualitativo (seção 18) em pelo menos um caso real antes de considerar o agente pronto.

## 35. Próximo passo recomendado

Não criar o agente ainda. Ordem recomendada:
1. Implementar a separação física de outputs em `my-video/` (estrutura da seção 27) — pré-requisito de ativação.
2. Desenhar o contrato de integração portátil entre os dois projetos (seção 6).
3. Só então formalizar `video-factory-ia.md` em `.claude/agents/`, incorporando os gates da seção 9 e o gate qualitativo da seção 18.
4. Testar o pipeline simples (seção 30) em uma peça real da Pousada Arágua antes de liberar para uso recorrente.

---

## Isolamento obrigatório entre projetos — estrutura mínima (referência da seção 15/27)

**[DECISÃO APROVADA — item 2 dos ajustes, pré-requisito de ativação, não melhoria opcional]**

```
my-video/
  output/
    villa-aragua/
      pousada/
      casa-aragua/
      institucional/
    maneco/
    sandbox/
    tests/
```

Aplica-se a: preflights, previews, reports, manifests, storyboards, composition specs, motion specs, renders, thumbnails, arquivos temporários, outputs de reviewer. Nenhum artefato de MANECO pode aparecer dentro dos outputs da Villa Arágua e vice-versa. **Fato observado nesta auditoria:** hoje existe `my-video/.claude/skills/remotion-video-reviewer/output/preflight/maneco-preflight.html` na mesma pasta usada pelos artefatos da Pousada Arágua — evidência concreta da mistura que esta estrutura deve eliminar antes da ativação do Video Factory IA.

## Templates — capacidade futura

**[PROPOSTA FUTURA — não criar agora]** Seleção de templates aprovados, reutilização de estruturas existentes, separação entre template e conteúdo, catálogo por formato e objetivo. Exemplos futuros: Reel Pousada, Reel Casa Arágua, Meta Ads, Stories, vídeo institucional, datas especiais, acomodações, benefícios, localização, prova social. Não criar Template Selector nem skill nova nesta fase — apenas registrado como evolução possível.
