# VIDEO_PRODUCTION_BRIEF — Contrato Portátil de Integração

**Status:** ativo — fonte única de verdade para o formato de entrada entregue por `VILLA ARAGUA IA` ao motor técnico `my-video`.
**Propriedade:** este documento pertence à governança de negócio (`VILLA ARAGUA IA`) — não altera, não substitui e não duplica `OUTPUT_CONTRACT.md` (que pertence a `my-video` e define apenas **onde** gravar artefatos técnicos).
**Não cria:** nenhum agente, nenhuma skill, nenhum código, nenhuma automação. Este contrato define um formato de dado, nada mais.

---

## 1. Por que este contrato existe

O agente Video Factory IA (ver `AUDITORIA_ARQUITETURAL_VIDEO_FACTORY_IA.md`, ainda **EM FORMALIZAÇÃO — NÃO ATIVO EM PRODUÇÃO**) precisa receber, de forma portátil e verificável, uma produção aprovada — sem depender de texto colado manualmente, memória de conversa, caminho absoluto de disco, nome livre ou interpretação informal. Este contrato formaliza esse pacote de entrada: `VIDEO_PRODUCTION_BRIEF`.

## 2. Formato: JSON + Markdown

- **`video-production-brief.json`** — única fonte de verdade, estruturada, validável.
- **`video-production-brief-review.md`** — folha de revisão humana, resumo derivado do JSON, **nunca** editada de volta para o JSON. Nunca duplica o JSON inteiro — só os campos definidos na seção 12.

Este par replica o padrão já em uso em todo o `my-video` (`composition-spec.json`/`composition-notes.md`, `storyboard-spec.json`/`storyboard.md`), evitando um formato novo para o pipeline técnico aprender.

---

## 3. Identificadores (herdados do `OUTPUT_CONTRACT.md` de `my-video` — não redefinidos aqui)

```
projectId: villa-aragua (único suportado por este contrato nesta fase)
productId (obrigatório): pousada | casa-aragua | institucional
productionId (obrigatório): minúsculo, letras/números/hífen, sem espaço, único dentro do productId
```

## 4. Máquina de estados (`status`)

```
DRAFT
  → STRATEGIC_APPROVED
    → ART_APPROVED
      → COMPOSITION_APPROVED
        → ENGINEERING
          → PREFLIGHT_APPROVED
            → RENDER_AUTHORIZED
              → RENDERED
                → ARCHIVED

REJECTED — alcançável a partir de qualquer estado não terminal (todos exceto RENDERED, ARCHIVED e o próprio REJECTED).
```

**`FINAL_APPROVED` foi removido** (decisão registrada em auditoria adversarial): não representava decisão distinta, não tinha objeto de aprovação próprio, nenhuma skill produzia artefato novo entre `PREFLIGHT_APPROVED` e ele, e `RENDER_AUTHORIZED` já é a aprovação final real — exige aprovador explicitamente autorizado (seção 6.3). Máquina reduzida de 10 para 9 estados + `REJECTED`.

Nenhum estado `*_REVIEW` no topo — o estado "em revisão" vive na evidência externa de aprovação (seção 6), nunca duplicado como estado de topo.

### 4.1 Gates nomeados (usados nos arquivos de aprovação externa e no validador)

```
strategic → art → composition → engineering → preflight → render
```

Seis gates, não cinco — `engineering` ganhou gate próprio nesta revisão (antes não tinha): a implementação do Engineer também exige aprovação humana explícita antes do preflight prosseguir.

### 4.2 Invariantes obrigatórias por transição

Toda invariante abaixo é verificada contra **evidência externa** (seção 6), nunca contra o campo `approvals.*` do próprio JSON (que é só espelho — seção 6.4).

| Transição | Exige (evidência externa) |
|---|---|
| `DRAFT → STRATEGIC_APPROVED` | Aprovação vigente do gate `strategic`: `APPROVED`, autor autorizado, `productionVersion` coerente, artefatos íntegros (SHA-256). |
| `STRATEGIC_APPROVED → ART_APPROVED` | O acima **e** aprovação vigente do gate `art`. |
| `ART_APPROVED → COMPOSITION_APPROVED` | O acima **e** aprovação vigente do gate `composition` **e** todos os 7 critérios essenciais do gate qualitativo (seção 7.1) em `PASS`, nenhum em `FAIL`. |
| `COMPOSITION_APPROVED → ENGINEERING` | Nenhuma aprovação nova — o Engineer começa assim que `COMPOSITION_APPROVED` é alcançado. |
| `ENGINEERING → PREFLIGHT_APPROVED` | Aprovação vigente do gate `engineering` **e** aprovação vigente do gate `preflight` — ambas, cumulativamente. |
| `PREFLIGHT_APPROVED → RENDER_AUTHORIZED` | Aprovação vigente do gate `render`, com `approvedBy` presente em `governance.approvalAuthorities.render` (lista não vazia). Ausência de evidência, lista vazia, ou `approvedBy` fora da lista **rejeita a transição**. |
| `RENDER_AUTHORIZED → RENDERED` | Confirmação factual de render concluído (relatório do `remotion-render-manager`) — registro de execução, não nova aprovação humana. |
| `RENDERED → ARCHIVED` | Nenhuma condição além de decisão operacional de arquivar. |
| Qualquer estado não terminal `→ REJECTED` | Sempre permitido — não exige pré-condição além de decisão humana de rejeitar. |

---

## 5. Campos do contrato

### 5.1 Obrigatórios

`contractVersion`, `productionVersion`, `projectId`, `productId`, `productionId`, `sourceBriefing`, `createdAt`, `updatedAt`, `createdBy`, `status`; `strategic.businessObjective`, `strategic.audience`, `strategic.corePromise`; `product.productName`, `product.productType`, `product.approvedValuePropositions`, `product.prohibitedClaims`; `creative.approvedCopy`, `creative.CTA`; **`technical.activeFormats`** (array não vazio, ex.: `["9:16"]` — ver seção 5.5), `technical.durationSeconds`, `technical.fps`; `assets[]` com pelo menos um item com `approved = true` e `rightsConfirmed = true`; `approvals.strategic` (espelho — seção 6.4); `governance.approvalAuthorities` (seção 6.3, lista não vazia para todo gate exigido, **desde a criação do contrato**).

### 5.2 Opcionais

`campaignId`, `previousProductionId`; `strategic.awarenessLevel`, `strategic.funnelStage`, `strategic.offer`, `strategic.seasonality`, `strategic.distributionChannel`, `strategic.organicOrPaid`, `strategic.budgetContext`, `strategic.successMetric`, `strategic.commercialPriority`; `product.mandatoryDisclaimers`, `product.differentiation`, `product.guestProfile`, `product.bookingChannel`, `product.whatsAppDestination`; `creative.creativeConcept`, `creative.hook`, `creative.headline`, `creative.supportingText`, `creative.tone`, `creative.visualMood`, `creative.visualReferences`, `creative.mandatoryScenes`, `creative.prohibitedScenes`, `creative.proofElements`, `creative.textDensity`, `creative.pacingIntent`, `creative.musicIntent`, `creative.voiceover`, `creative.subtitleRequirement`; `technical.format` (rótulo amigável, derivado de `activeFormats[0]` — nunca fonte, ver 5.5), `technical.width`, `technical.height`, `technical.platform`, `technical.safeAreaProfile`, `technical.outputPreset`, `technical.audioRequired`, `technical.captionsRequired`, `technical.thumbnailRequired`, `technical.renderRequired`, `technical.templateId`, `technical.pipelineMode` (default `"simple"` se ausente — `"premium"` não implementado nesta fase, só reservado); `assets[].scenePreference`, `assets[].notes`; `governance.institutionalComparativeApproval` (default `false`).

### 5.5 Formato — piloto de formato único (`pipelineMode = simple`)

**`technical.aspectRatio` foi removido** (era duplicata literal de `technical.format` — achado de auditoria adversarial). O campo autoritativo agora é **`technical.activeFormats`** (array, ex.: `["9:16"]` para o piloto `reel-acomodacoes-01`). `technical.format`, quando presente, é só rótulo derivado do primeiro item de `activeFormats` — nunca é lido por nenhuma skill técnica.

O conflito que motivou este ajuste era **de prosa, não de código**: `remotion-composition-director`'s validador determinístico (`validate-composition-spec.js`) já deriva os breakpoints exigidos a partir do que `spec.breakpoints` efetivamente contém — não impõe os 4 formatos por código. A cobertura dos 4 formatos (`portrait_9_16`, `portrait_4_5`, `square_1_1`, `landscape_16_9`) continua sendo o padrão esperado para `pipelineMode = premium`; para `pipelineMode = simple`, apenas os formatos listados em `technical.activeFormats` são exigidos.

### 5.3 Derivados (nunca preenchidos manualmente)

Nenhum caminho de output é armazenado no contrato. A fórmula de derivação (definida e implementada em `my-video/OUTPUT_CONTRACT.md`, não duplicada aqui) é:

```
Villa Arágua: output/{projectId}/{productId}/{productionId}/{artifactType}/
```

O campo `output.derivationFormulaRef` só guarda a referência textual a essa fórmula (`"OUTPUT_CONTRACT.md (my-video)"`), nunca o caminho já resolvido. Qualquer skill técnica deriva o caminho na hora, a partir de `projectId`/`productId`/`productionId`/`artifactType` — nunca lendo um caminho gravado no brief.

### 5.4 Imutáveis após `RENDER_AUTHORIZED`

`projectId`, `productId`, `productionId`, todo o bloco `product.*`, `creative.approvedCopy`, `creative.CTA`, `product.prohibitedClaims`, `product.mandatoryDisclaimers`. Qualquer mudança nesses campos depois de `RENDER_AUTHORIZED` não edita o contrato existente — gera nova `productionVersion` (seção 9).

---

## 6. Modelo de aprovações — evidência externa (fonte primária)

**Mudança estrutural desta revisão:** aprovação deixou de ser um campo escrito dentro do próprio JSON do briefing (isso era autoatestação — achado central da auditoria adversarial) e passou a ser um **arquivo externo, imutável, por decisão**, dentro da própria produção em `my-video/output/`.

### 6.1 Localização e nomenclatura

```
output/{caminho canônico da produção}/approvals/{gate}-v{productionVersion}-{decision}-{timestamp}.json
```

Exemplo para `reel-acomodacoes-01`:
```
output/villa-aragua/pousada/reel-acomodacoes-01/approvals/composition-v1-approved-20260724T180000.json
output/villa-aragua/pousada/reel-acomodacoes-01/approvals/composition-v1-rejected-20260724T183000.json
```

`{gate}` é um dos 6 gates nomeados (seção 4.1): `strategic`, `art`, `composition`, `engineering`, `preflight`, `render`. `{timestamp}` é `YYYYMMDDTHHmmss`, UTC ou com timezone explícito no conteúdo do arquivo.

### 6.2 Estrutura do arquivo de aprovação

```json
{
  "approvalId": "composition-v1-20260724T180000",
  "projectId": "villa-aragua",
  "productId": "pousada",
  "productionId": "reel-acomodacoes-01",
  "productionVersion": 1,
  "gate": "composition",
  "decision": "APPROVED",
  "approvedBy": "Renildo",
  "approvedAt": "2026-07-24T18:00:00-03:00",
  "artifactRefs": [
    { "path": "composition/composition-spec.json", "sha256": "<hex de 64 caracteres>" }
  ],
  "supersedesApprovalId": null,
  "notes": ""
}
```

`decision` aceita só **`APPROVED` | `REJECTED`** — não existe `PENDING` nem `REVISE` como arquivo: a **ausência** de arquivo de aprovação para um gate já significa pendente; um "pedido de revisão" não gera arquivo de aprovação, só feedback fora deste registro formal (ex.: em `notes` de uma rejeição, ou em conversa), até que uma nova composição seja submetida e então aprovada ou rejeitada de fato.

**Campos removidos por serem redundantes (achado de auditoria):** não existe `approvalVersion` — o esquema do arquivo de aprovação evolui junto com `contractVersion`, não precisa de versionamento próprio.

### 6.3 Autorização por gate (`governance.approvalAuthorities`)

```json
"governance": {
  "approvalAuthorities": {
    "default": ["Renildo"],
    "render": ["Renildo"]
  }
}
```

**Decisão registrada:** em vez de uma lista por gate (6 chaves, `strategic`/`art`/`composition`/`engineering`/`preflight`/`render`), que seria repetição do mesmo nome 6 vezes para um negócio com um único decisor, o contrato usa **`default`** (aplicado a todos os gates exceto `render`) **+ `render`** como chave própria — porque `render` é o único gate cuja lista de autorizados já tinha exigência textual anterior e cujo risco (custo de reverter um render indevido) justifica poder divergir da lista padrão no futuro, sem que isso seja assumido implicitamente. `governance.renderAuthorizedApprovers` (campo antigo) é **removido**, absorvido por `approvalAuthorities.render`.

O validador nunca presume que a lista `default` autoriza `render` automaticamente nem o contrário — cada gate resolve sua própria lista (`approvalAuthorities[gate] || approvalAuthorities.default`).

### 6.4 `approvals.*` dentro do JSON principal — espelho, nunca fonte

O objeto `approvals.<gate> = { status, approvedBy, approvedAt, notes }` **continua existindo no JSON principal**, mas agora é só um **espelho derivado**, escrito pelo agente **somente depois** de validar a evidência externa correspondente — nunca escrito diretamente por decisão humana ou por inferência do agente. Cada entrada ganha dois campos novos de rastreabilidade:

```
approvals.<gate> = {
  status: PENDING | APPROVED | REJECTED,
  approvedBy: string | null,
  approvedAt: string | null,
  notes: string | null,
  syncedFromApprovalId: string | null,
  syncedAt: string | null
}
```

Toda sincronização deve ser informada explicitamente (nunca silenciosa) — ao atualizar `approvals.*`, o agente relata: qual arquivo de evidência foi lido, qual era o estado anterior do espelho, e qual passou a ser.

### 6.5 Revogação e supersessão

Nunca editar um arquivo de aprovação existente. Revogar ou substituir uma decisão é sempre um **novo arquivo**, com `supersedesApprovalId` apontando para o `approvalId` que ele substitui — preservando toda a cadeia. A decisão vigente de um gate é aquela cujo `approvalId` **não é referenciado** por nenhum `supersedesApprovalId` de outro arquivo do mesmo gate (o "topo" da cadeia) — nunca decidida por data de modificação do arquivo (`mtime`), que não é confiável nem portátil.

---

## 7. Gate qualitativo (`qualityGate`)

Posicionado entre `remotion-composition-director` e `remotion-engineer` (ver auditoria arquitetural, seção 9 e 18). Usa como lentes de julgamento `villa-aragua-creative-design-ads`, `villa-aragua-marketing-psychology` e `villa-aragua-copywriting-conversion`. **Não é uma skill nova.**

```
qualityGate = {
  status: PENDING | APPROVED | REVISE | REJECTED,
  reportRef: string | null,        (referência ao relatório narrativo completo, ex.: "reports/quality-gate-report.md")
  evaluatedBy: string | null,
  evaluatedAt: string | null,
  criteria: { <17 chaves> : PENDING | PASS | FLAG | FAIL }
}
```

### 7.1 Os 17 critérios em dois níveis — essencial (bloqueia) e diagnóstico (não bloqueia)

**Revisão operacional (piloto):** manter os 17 critérios do schema, mas dividir qual subconjunto bloqueia avanço de estado. Nenhum critério novo foi criado — só a classificação de quais bloqueiam mudou, de 3 para 7.

**GATE ESSENCIAL — os 7 abaixo precisam estar todos em `PASS` para `qualityGate` permitir `COMPOSITION_APPROVED`. Qualquer um em `FAIL` bloqueia:**

| Critério (chave) |
|---|
| **`coerenciaComercial`** |
| **`ausenciaOverpromise`** |
| **`aderenciaBriefing`** |
| **`legibilidade`** |
| **`protagonismoProduto`** |
| **`clarezaPrimeiros2Segundos`** |
| **`pesoVisualCTA`** |

**GATE COMPLETO — diagnóstico, não bloqueia sozinho:**

`forcaVisual`, `clarezaPromessa`, `qualidadeCrop`, `hierarquiaTipografica`, `posicionamentoTextos`, `excessoSobreposicao`, `equilibrioImagemTexto`, `espacoNegativo`, `coerenciaFonte`, `adequacaoPublico`.

Esta classificação (quais 7 são essenciais) é fixa neste contrato — não pode ser reclassificada dentro de um brief individual, exatamente para impedir que uma produção "rebaixe" um critério de segurança comercial só para aprovar mais rápido. O validador mínimo (seção 15) codifica esta mesma lista de 7 — mudar a lista aqui sem atualizar o validador quebra a consistência entre documento e enforcement.

### 7.2 Regras do gate

- `FAIL` em qualquer um dos **7 critérios essenciais** impede `qualityGate.status = APPROVED` e bloqueia `COMPOSITION_APPROVED`.
- `FAIL` num critério **diagnóstico** não bloqueia sozinho, mas deve ser registrado com justificativa em `reportRef` — várias `FAIL` diagnósticas acumuladas são sinal de risco, mesmo sem bloquear tecnicamente.
- `FLAG` em qualquer critério, essencial ou diagnóstico, exige justificativa registrada em `reportRef`.
- `qualityGate.status = APPROVED` exige `reportRef` não nulo.
- `evaluatedBy` e `evaluatedAt` são obrigatórios assim que `status` sai de `PENDING`.

---

## 8. Modelo de assets

```
asset = {
  assetId: string,
  path: string (relativo à raiz de my-video, nunca absoluto),
  type: image | video | audio,
  productId: pousada | casa-aragua | institucional,
  approved: boolean,
  intendedUse: string,
  scenePreference: string | null (opcional),
  cropRestrictions: string | null,
  peopleVisible: boolean,
  rightsConfirmed: boolean,
  notes: string | null
}
```

Regras: `approved = true` e `rightsConfirmed = true` são obrigatórios para o asset entrar na produção; `path` nunca contém prefixo de máquina (`/Users/...`) — seção 10; `productId` do asset deve bater com `productId` da produção, **salvo** produção `institucional` com `governance.institutionalComparativeApproval = true`; nenhum asset sob `maneco/` pode aparecer em produção `villa-aragua`, sem exceção.

---

## 9. Versionamento

- **`contractVersion`** (semver do schema deste contrato, não da produção): MAJOR = quebra de compatibilidade; MINOR = campo opcional novo; PATCH = correção textual.
- **`productionVersion`** (inteiro, por produção): começa em `1`. Incrementa sempre que um campo imutável (seção 5.4) precisar mudar depois que qualquer `approvals.*` já saiu de `PENDING`.
- Incrementar `productionVersion` **invalida** todas as `approvals` a partir do gate afetado pela mudança, voltando-as para `PENDING` — nunca preserva aprovação antiga sobre conteúdo novo.
- Nenhuma versão é sobrescrita — cada `productionVersion` gera seu próprio arquivo (`video-production-brief-v1.json`, `-v2.json`, ...), preservando as anteriores.
- **`RENDER_AUTHORIZED` torna a versão corrente imutável.** Mudança depois disso exige nova `productionVersion`, nunca edição do arquivo já aprovado.
- **Nova versão da mesma produção** (`productionVersion` incrementado, mesmo `productionId`) ≠ **nova produção** (novo `productionId`, `productionVersion = 1`, opcionalmente referenciando a anterior via `previousProductionId`). Use nova produção quando a peça é conceitualmente diferente; use nova versão quando é correção/ajuste da mesma peça.

---

## 10. Portabilidade

O contrato **nunca** contém caminho absoluto de máquina (`/Users/...`). Todo `assets[].path` é relativo à raiz do projeto `my-video` (ex.: `public/assets/villa-aragua/reels02/arquivo.webp`).

**[PROPOSTA FUTURA — não implementada nesta sessão]** A resolução do prefixo absoluto de disco fica fora do contrato, num arquivo de configuração local não versionado (`video-factory.local.json`) ou variável de ambiente (`MY_VIDEO_ROOT`) — qualquer uma das duas resolve o alias para um caminho real nesta máquina. Nenhum dos dois foi criado nesta sessão; nenhum código de resolução foi escrito.

---

## 11. Autorização de render

`governance.approvalAuthorities.render` (seção 6.3) é **obrigatório desde a criação do contrato** (não só na hora do render). Não existe lista padrão silenciosa — se a lista estiver ausente, vazia, ou se o `approvedBy` da aprovação vigente do gate `render` não estiver nela, a transição para `RENDER_AUTHORIZED` é **rejeitada** (seção 4.2).

---

## 12. Modelo da folha de revisão humana (`video-production-brief-review.md`)

Documento de revisão, não fonte de verdade. Contém **apenas**: `projectId`, `productId`, `productionId`, `contractVersion`, `productionVersion`, `status`, objetivo, público, promessa, oferta, copy aprovada, CTA, conceito criativo, especificação técnica resumida, assets principais, claims proibidos, aprovações, resultado do gate qualitativo, pendências, decisão solicitada a Renildo. Cabeçalho obrigatório: `sourceJsonFile`, `sourceContractVersion`, `sourceProductionVersion`, `generatedOrReviewedAt`, e o aviso: **"Documento de revisão humana. Alterações neste arquivo não modificam o contrato JSON."** Enquanto não existir geração automática, este arquivo é um **snapshot de revisão**, não um documento sincronizado — cada nova leitura/aprovação humana gera (ou atualiza manualmente) um novo snapshot, sem pretender espelhar o JSON em tempo real.

---

## 13. Separação entre Pousada Arágua e Casa Arágua

- Uma produção possui exatamente um `productId`.
- Pousada e Casa nunca se misturam na mesma produção.
- Produção `institucional` é a única exceção possível, e mesmo assim exige `governance.institutionalComparativeApproval = true` com aprovação estratégica explícita referenciada em `approvals.strategic.notes`.
- Cada cena (`creative.mandatoryScenes`) e cada asset mantêm identificação clara de produto — nenhum campo de `product.approvedValuePropositions` de um produto pode aparecer implicitamente atribuído ao outro.
- Nenhum diferencial exclusivo (ex.: "café na suíte" é só Pousada; "piscina privativa" é só Casa) pode ser atribuído ao produto errado — validação obrigatória cruzando `creative.approvedCopy`/`creative.headline` com `product.approvedValuePropositions` do produto declarado.

---

## 14. O que este contrato não faz

Não cria o agente Video Factory IA. Não altera nenhuma skill de negócio. Não altera composições, assets de origem, `remotion.config.ts` ou dependências. Não renderiza, não publica.

---

## 15. Validador mínimo (`validate-video-production.js`)

**Localização:** `my-video/scripts/validate-video-production.js` — Node puro (`fs`, `path`, `node:crypto`), sem dependência nova, seguindo o mesmo padrão de exit codes do validador já existente (`remotion-composition-director/validator/validate-composition-spec.js`).

**Uso** (executar a partir da raiz de `my-video`):

```
node scripts/validate-video-production.js \
  --brief <path relativo do video-production-brief.json> \
  --production-root <path relativo da raiz da produção em output/> \
  --action <strategic|art|composition|engineering|preflight|render>
```

Ou, via `npm run validate:brief -- --brief ... --production-root ... --action ...`.

`--action` é cumulativo: validar `--action preflight`, por exemplo, também exige que `strategic`, `art`, `composition` e `engineering` estejam com evidência externa válida — não só o gate imediatamente anterior.

**Exit codes:** `0` = válido para a ação pedida; `1` = inválido por regra de contrato; `2` = erro de execução/configuração (args ausentes, arquivo não encontrado, JSON malformado).

**Saída:** relatório JSON no stdout, uma entrada por regra, cada uma `PASS` | `FAIL` | `NOT_APPLICABLE`. O script nunca corrige nada — só valida e informa, conforme decisão explícita desta revisão.

**Cobertura:** identificadores (`projectId`/`productId`/`productionId`/`productionVersion`/`contractVersion`), `technical.activeFormats`, paths relativos e proteção contra path traversal, `approved`/`rightsConfirmed` dos assets, ausência de MANECO, ausência de produto cruzado, namespace de output correto, ausência de path legado (`.claude/skills/*/output/`), evidência externa encadeada de cada gate exigido pela ação, autor autorizado por gate, `productionVersion` coerente entre briefing e aprovação, integridade SHA-256 de cada artefato referenciado, cadeia de supersessão sem ambiguidade, coerência de `status`, e os 7 critérios essenciais do gate qualitativo (seção 7.1) quando a ação exigir o gate `composition`.

---

## 16. Fronteira de responsabilidade (VILLA ARAGUA IA -> my-video)

### 16.1 Onde VILLA ARAGUA IA encerra

VILLA ARAGUA IA encerra sua responsabilidade quando, para a producao alvo:

1. O `video-production-brief.json` esta valido neste contrato.
2. Existe evidencia externa vigente de `strategic` com `decision = APPROVED`.
3. Todos os hashes referenciados em `artifactRefs` da aprovacao vigente batem com os arquivos atuais.
4. O `production root` esta definido no namespace canonico de my-video:
  `output/villa-aragua/{productId}/{productionId}/`.

### 16.2 Onde my-video inicia

my-video inicia sua responsabilidade quando:

1. Recebe o briefing aprovado no `production root` da producao.
2. Valida a evidencia estrategica externa com `scripts/validate-video-production.js`.
3. Identifica o proximo gate pendente na sequencia `strategic -> art -> composition -> engineering -> preflight -> render`.
4. Aciona somente a skill tecnica adequada para o gate corrente.

### 16.3 Regra de autoridade canonica do agente

- A versao executavel canonica do Video Factory IA e a de my-video.
- Copias fora de my-video devem ser camada fina de handoff/documentacao, sem duplicar pipeline tecnico completo.
- Mudancas de orquestracao tecnica devem ocorrer somente no agente canonico de my-video, para evitar divergencia.
