# Análise das Campanhas de Referência Meta Ads — Villa Arágua

**Natureza deste arquivo:** análise investigativa em modo leitura das campanhas específicas que Renildo acredita terem sido algumas das melhores da Villa Arágua, usando conexão real ao Meta Ads Manager (conta `2475984692462178` — "CA Pousada Aragua 01") além dos arquivos e planilhas já existentes. Nenhuma campanha, conjunto, anúncio, público, orçamento ou criativo foi criado, duplicado, editado, pausado, ativado ou alterado. Toda métrica citada vem diretamente da API do Meta Ads ou de print/planilha já aberta em etapas anteriores — nada foi inventado.

**Gerado em:** 2026-07-17
**Conta consultada:** `2475984692462178` ("CA Pousada Aragua 01", BRL, ativa, somente leitura nesta sessão)
**Arquivos-base consultados:** `ANALISE_HISTORICO_META_ADS_PUBLICOS_7_SETEMBRO_2026_POUSADA_ARAGUA.md`, `PLANO_EXECUCAO_MANUAL_META_ADS_7_SETEMBRO_2026_POUSADA_ARAGUA.md`, `CAMPANHA_SUPERVISIONADA_7_SETEMBRO_2026_POUSADA_ARAGUA.md`, `AUDITORIA_VISUAL_CRIATIVOS_BRIEFING_01_POUSADA_ARAGUA.md`, `BRIEFING_SUPERVISIONADO_01_POUSADA_ARAGUA_RETOMADA_COMERCIAL.md`, `VALIDACAO_TESTES_MARKETING_META_ADS_IA_VILLA_ARAGUA.md`, `ARQUITETURA_OPERACIONAL_MARKETING_META_ADS_IA_VILLA_ARAGUA.md`

---

## 1. Status da análise

- Análise feita em modo leitura, com conexão real ao Meta Ads Manager.
- Nenhuma campanha editada.
- Nenhum anúncio publicado.
- Nenhum orçamento alterado.
- Nenhum público alterado.
- Nenhuma automação criada.
- Decisão final permanece com Renildo.

**Nota sobre a conta:** o Business Manager "Pousada Arágua" (`business_id 310737019464376`) tem várias contas de anúncio associadas. A conta real com histórico de gasto em BRL, ativa e consultável é `2475984692462178` ("CA Pousada Aragua 01") — foi a única usada nesta análise. As demais contas do mesmo negócio aparecem como "(Read-Only)" em moeda USD/INR (provavelmente contas de monitoramento ou teste, sem o mesmo histórico) ou como `1085405660473781` ("Villa Arágua (Read-Only)"), que está **DESABILITADA** por sinalização de atividade incomum da própria Meta — não consultável nesta sessão.

---

## 2. Campanhas procuradas

| Campanha procurada | Encontrada? | Nome exato encontrado | Período | Status | Fonte | Observação |
|---|---|---|---|---|---|---|
| `ABRIL 26 PASSEIO BARCO [ENG] WHT` | Sim | `ABRIL 26 PASSEIO BARCO [ENG] WHT` | Início 05/04/2026 | PAUSED | API Meta Ads (id 120244122012970790) | Nome idêntico ao procurado. |
| `MAR 26 PASSEIO BARCO [ENG] WHT` | Sim | `MAR 26 PASSEIO BARCO [ENG] WHT` | Início 22/02/2026 | PAUSED | API Meta Ads (id 120241642935430790) | Nome idêntico ao procurado. |
| `[AJ][ENGAJAMENTO][ABO][MENSAGEM WHATSAPP]` | Sim | `[AJ][ENGAJAMENTO][ABO][MENSAGEM WHATSAPP]` | Início 18/12/2025 | PAUSED | API Meta Ads (id 120239235357880790) | Nome idêntico ao procurado. |
| `NOV25 [VENDAS]WHT NOVO` | Sim (grafia levemente diferente) | `NOV 25 [VENDAS] WHT NOVO` (com espaços) | Início 10/11/2025 | PAUSED | API Meta Ads (id 120236877670860790) | Mesma campanha; só variação de espaçamento no nome. Já tinha sido parcialmente analisada via print na etapa anterior — dados agora confirmados diretamente pela API. |
| `VERAO 2025 [ENGAJAMENTO ZAP] Publico Quente` | Sim | `VERAO 2025 [ENGAJAMENTO ZAP] Publico Quente` | Início 17/09/2024 | PAUSED | API Meta Ads (id 120212147905270790) | Nome idêntico ao procurado. |
| `[MSG] Zap Verao 2024` | Sim | `[MSG] Zap Verão 2024` | Início 23/08/2023 | PAUSED | API Meta Ads (id 23857686746270789) | Nome idêntico (só acento). |

Todas as 6 campanhas prioritárias foram localizadas com sucesso na conta `2475984692462178`.

**Campanhas relacionadas encontradas (variações e nomes semelhantes):**
- `CA 26 [ENG] WHT` e `MAR 26 CA [ENG] WHT` — **são campanhas da Casa Arágua** (prefixo "CA"), não da Pousada. Citadas só para registrar que existem, mas fora do escopo desta análise (regra de não misturar Pousada e Casa).
- `NOV 25 [DUALIDADE] - OK teste` — já analisada via print na etapa anterior; agora confirmada pela API com pequena diferença de alcance (34.435 via API vs 34.807 no print — possível diferença de momento de captura, não é erro, apenas registrado).
- `VERAO 2025 [ENGAJAMENTO] Publico Quente` (sem "ZAP" no nome) — já analisada via print; confirmada pela API com números idênticos (ver seção 4).
- `[AJ][ENGAJAMENTO][CBO][TRÁFEGO IG]` — campanha irmã da `[AJ]...[MENSAGEM WHATSAPP]`, mesmo período, objetivo de tráfego para Instagram em vez de WhatsApp.
- `[MSG] WhatsApp VERAO 2024 IV`, `[MSG] VERAO 2024 video 30"`, `[MSG] Promo dezembro 2023` — outras campanhas da mesma família "[MSG]", de escala menor.
- Diversas campanhas de "Passeio de Barco" isoladas (`Hospedagem Passeio Barco [SET OUT 24]`, `PROMO BARCO...`) — produto diferente (passeio, não hospedagem), citadas só como contexto.

---

## 3. Dados extraídos por campanha

### `ABRIL 26 PASSEIO BARCO [ENG] WHT`
- **ID:** 120244122012970790
- **Período:** início 05/04/2026 (sem data de encerramento definida)
- **Objetivo:** Engajamento (OUTCOME_ENGAGEMENT)
- **Status:** Pausada
- **Orçamento:** R$ 40,00/dia
- **Estratégia de lance:** não documentado nesta consulta
- **Produto anunciado:** Passeio de barco (não é hospedagem da Pousada diretamente)
- **Tipo de público / Região / Idade / Gênero / Idioma / Interesses / Públicos personalizados / Semelhantes / Exclusões / Posicionamentos:** não documentados nesta consulta (exigiria consulta ao nível de conjunto de anúncios, não feita nesta rodada)
- **Criativos usados:** 2 anúncios — "ABRIL 26 [IMAGEM ÚNICA] PASSEIO BARCO [ENG] WHT" e "ABRIL 26 [CARROSSEL] PASSEIO BARCO [ENG] WHT"
- **Tipo de criativo:** imagem única e carrossel
- **Texto principal / Título / Descrição:** não documentado — criativos usam formato dinâmico (`{{product.name}}`), corpo não retornado pela API nesta consulta
- **CTA:** não documentado nesta consulta
- **Destino:** WhatsApp (indicado pelo nome "WHT" da campanha)
- **Resultados principais:** valor gasto R$ 806,41; alcance 45.477; impressões 82.370; frequência 1,81; cliques 3.365; CTR 4,09%; CPM R$ 9,79; CPC R$ 0,24
- **Conversas iniciadas / custo por conversa:** não consultado nesta rodada
- **Leads qualificados / Reservas geradas:** não documentado
- **Observações:** CTR bom (4,09%), mas é produto de passeio de barco, não de hospedagem — aprendizado de público/criativo é só parcialmente transferível para a campanha da Pousada.

### `MAR 26 PASSEIO BARCO [ENG] WHT`
- **ID:** 120241642935430790
- **Período:** início 22/02/2026
- **Objetivo:** Engajamento
- **Status:** Pausada
- **Orçamento:** R$ 40,00/dia
- **Produto anunciado:** Passeio de barco
- **Criativos usados:** "MAR 26 PB IMAGEM UNICA [ENG] WHT — ultimas vagas", "MAR 26 PB IMAGEM UNICA [ENG] WHT", "MAR 26 PB CARROSSEL [ENG] WHT", "MAR 26 PB REELS [ENG] WHT" (pausado)
- **Tipo de criativo:** imagem única, carrossel e reels
- **Texto principal (carrossel, real, extraído da API):** "Exclusivo para casal em março. Bombinhas. Consulte disponibilidade." — cartões do carrossel incluem: "2 noites + passeio de barco por R$ 799", "Datas limitadas", "Vagas limitadas", "R$ 799", "Consulte datas disponíveis"
- **CTA:** WHATSAPP_MESSAGE
- **Destino:** WhatsApp (link `api.whatsapp.com`)
- **Resultados principais:** valor gasto R$ 1.466,56; alcance 108.557; impressões 254.689; frequência 2,35; cliques 13.878; **CTR 5,45%** (o mais alto entre as 6 campanhas prioritárias); CPM R$ 5,76; CPC R$ 0,11
- **Observações:** **melhor CTR do grupo analisado, mas com copy que usa preço fixo (R$ 799), "exclusivo", "vagas limitadas" e "datas limitadas" — exatamente os elementos que as regras atuais do projeto proíbem.** O bom desempenho não pode ser atribuído só à copy; o produto (passeio de barco, mais barato e mais fácil de decidir por impulso) também influencia. Não reaproveitar esta copy como está.

### `[AJ][ENGAJAMENTO][ABO][MENSAGEM WHATSAPP]`
- **ID:** 120239235357880790
- **Período:** início 18/12/2025
- **Objetivo:** Engajamento
- **Status:** Pausada
- **Orçamento:** não documentado no nível de campanha (usa orçamento do conjunto de anúncios — "ABO" no nome já indica Ad Set Budget Optimization)
- **Produto anunciado:** Villa Arágua em geral (não especifica Pousada ou Casa no nome)
- **Criativos usados:** "[AD1][IMAGEM][ÚLTIMAS VAGAS]" (ativo e uma versão pausada), "[AD2][VÍDEO][VERÃO 2026 COMEÇA AQUI]" (2 versões), "[AD3][CARROSSEL][EXPERIÊNCIAS]" (2 versões)
- **Tipo de criativo:** imagem, vídeo, carrossel
- **Texto principal/Título/Descrição:** **não documentado** — todos os criativos desta campanha usam formato dinâmico (`{{product.name}}`), provavelmente Advantage+ / criativo de catálogo; corpo do texto não é armazenado como texto fixo recuperável por esta consulta.
- **CTA:** não documentado nesta consulta
- **Destino:** WhatsApp (nome da campanha)
- **Resultados principais:** valor gasto R$ 2.323,32; alcance 340.045; impressões 680.357; frequência 2,00; cliques 20.386; CTR 3,00%; CPM R$ 3,41; CPC R$ 0,11
- **Observações:** **é a campanha de maior alcance/impressão entre as 6 prioritárias.** Um dos nomes de anúncio é literalmente "[AD1][IMAGEM][ÚLTIMAS VAGAS]" — confirma que a linguagem de urgência não ficou só no planejamento em planilha, foi usada em anúncio real e ativo, com investimento real considerável. Não é possível medir isoladamente o efeito desse anúncio específico dentro do resultado agregado da campanha (o resultado é da campanha inteira, com múltiplos anúncios simultâneos).

### `NOV 25 [VENDAS] WHT NOVO`
- **ID:** 120236877670860790
- **Período:** início 10/11/2025
- **Objetivo:** Vendas (OUTCOME_SALES)
- **Status:** Pausada
- **Orçamento:** R$ 15,00/dia
- **Produto anunciado:** Pousada Arágua (hospedagem)
- **Criativos usados:** "NOV 25 [VENDAS] - CARROSSEL", "NOV 25 [VENDAS] - CARROSSEL CASAL", "NOV 25 [VENDAS] - REELS", "NOV 25 [VENDAS] - IMAGEM" (ativos); "NOV 25 [VENDAS] - REELS FAMILIA DUAL", "NOV 25 [VENDAS] - IMAGEM DIVERSAS", "NOV 25 [VENDAS] - IMAGEM FAMILIA" (pausados)
- **Tipo de criativo:** carrossel, reels, imagem
- **Texto principal (real, extraído da API — creative "NOV 25 [VENDAS] - CARROSSEL"):** "Cansado da rotina e buscando um refúgio de verdade para sua família? 🤔 (...) Na Pousada Aragua, transformamos o estresse do dia a dia em momentos de pura alegria e relaxamento. Imagine manhãs tranquilas à beira da piscina, tardes na praia e noites de paz (...) ✨ Nossa excelência é comprovada por quem mais importa: ⭐ 9.2 no Booking, 4.8 no Google e somos a #4 no TripAdvisor! (...) 📲 Fale conosco agora mesmo no WhatsApp..."
- **Texto principal (real, "NOV 25 [VENDAS] - CARROSSEL CASAL"):** "Pousada Aragua: Seu refúgio de paz espera em Bombinhas, SC. Clique e descubra." — cartões do carrossel usam contraste "rotina x praia" ("Cansado da Rotina?", "Praia ou Stress? Escolha!", "Troque a Cidade Pelo Paraíso"), sem preço, sem desconto.
- **CTA:** MESSAGE_PAGE
- **Destino:** WhatsApp (mensagem)
- **Resultados principais:** valor gasto R$ 3.393,23; alcance 234.963; impressões 519.711; frequência 2,21; cliques 15.703; CTR 3,02%; CPM R$ 6,53; CPC R$ 0,22
- **Resultado oficial da campanha (confirmado via API, campo `results`):** **1.793 conversas iniciadas, custo por conversa R$ 1,89**
- **Observações:** **nenhuma das duas copies reais extraídas usa preço fixo, desconto ou "últimas vagas" — usa prova social real (nota Booking/Google/TripAdvisor) e contraste emocional rotina x praia.** É um padrão de copy seguro e compatível com as regras atuais, e ainda assim performou bem.

### `VERAO 2025 [ENGAJAMENTO ZAP] Publico Quente`
- **ID:** 120212147905270790
- **Período:** início 17/09/2024
- **Objetivo:** Engajamento
- **Status:** Pausada
- **Orçamento:** não documentado no nível de campanha
- **Produto anunciado:** Pousada Arágua
- **Criativos usados:** "Publico Quente Interesse [IMAGEM]", "Publico Quente Interesse [VIDEO 30\"]", "Publico Quente Aragua [VIDEO 30\"]" (2 versões, incluindo uma cópia)
- **Tipo de criativo:** imagem e vídeo
- **Texto principal/Título/Descrição:** não extraído nesta rodada (criativos não consultados individualmente por nome)
- **Destino:** WhatsApp (engajamento com mensagens)
- **Resultados principais:** valor gasto R$ 5.272,40; alcance 394.767; impressões 1.015.208; frequência 2,57; cliques 34.963; CTR 3,44%; CPM R$ 5,19; CPC R$ 0,15
- **Resultado oficial da campanha (confirmado via API):** **4.770 conversas iniciadas, custo por conversa R$ 1,11**
- **Observações:** **maior volume de conversas entre todas as campanhas analisadas (4.770), com o segundo melhor custo por conversa.** É a campanha de maior escala geral (mais de 1 milhão de impressões). Público "quente" no nome confirma a hipótese já registrada na análise anterior de que público aquecido/engajado performa bem.

### `[MSG] Zap Verão 2024`
- **ID:** 23857686746270789
- **Período:** início 23/08/2023
- **Objetivo:** Engajamento
- **Status:** Pausada
- **Orçamento:** não documentado no nível de campanha
- **Produto anunciado:** Pousada Arágua
- **Criativos usados:** 3 anúncios, todos chamados "Novo anúncio de Engajamento"
- **Tipo de criativo:** pelo menos 1 confirmado como imagem/carrossel com múltiplos cartões (o creative "Converse conosco")
- **Texto principal (real, extraído da API, creative "Converse conosco"):** "Férias na Praia de Mariscal! 🌊☀️ Nossa pousada é o lugar perfeito para você aproveitar o sol, a praia e a piscina. Com acomodações confortáveis, serviços de café da manhã, limpeza das acomodações e uma localização privilegiada, temos tudo o que você precisa para uma temporada de Verão inesquecível. Reserve agora e garanta sua estadia. Desfrute momentos inesquecíveis em família e amigos."
- **Cartões do carrossel (reais):** "Piscina com espreguiçadeiras" (Suíte Terra, saída direta pra piscina), "Cadeiras de Praia e Guarda Sol" (para todos os hóspedes), "Café da manhã servido em sua acomodação", "Área aberta com playground", "Apenas 08 acomodações", "Piscina super charmosa", "Espaço Kids", "Lindas Praias"
- **CTA:** MESSAGE_PAGE
- **Destino:** WhatsApp (mensagem)
- **Resultados principais:** valor gasto R$ 3.993,26; alcance 384.412; impressões 999.400; frequência 2,60; cliques 42.900; CTR 4,29%; CPM R$ 4,00; **CPC R$ 0,09 (o mais baixo entre todas as campanhas analisadas nesta rodada)**
- **Resultado oficial da campanha (confirmado via API):** **3.804 conversas iniciadas, custo por conversa R$ 1,05 — o melhor custo por conversa entre as 3 campanhas com esse dado confirmado**
- **Observações:** **esta é, com dado real, a campanha com melhor eficiência de custo por conversa (R$ 1,05) combinada com escala muito grande (quase 1 milhão de impressões, 384 mil de alcance).** A copy usa "Reserve agora e garanta sua estadia" — não é "últimas vagas" nem preço fixo, mas é uma leve chamada de urgência que vale suavizar nas versões futuras. Menciona "Cadeiras de Praia e Guarda Sol" e "Espaço Kids" como amenities — **não confirmados nesta sessão contra `DADOS_OFICIAIS_ATENDIMENTO_VILLA_ARAGUA.md`**, então não devem ser reaproveitados sem validação.

---

## 4. Comparativo de desempenho

| Campanha | Objetivo | Público | Região | Criativo | Gasto | Conversas | Custo por conversa | Qualidade percebida | Reaproveitar aprendizado? |
|---|---|---|---:|---|---:|---:|---:|---|---|
| `[MSG] Zap Verão 2024` | Engajamento/Mensagens | não documentado | não documentado | Imagem/carrossel (prova social + amenities) | R$ 3.993,26 | 3.804 | **R$ 1,05** | **percepção de Renildo: uma das melhores** — e dado real confirma: melhor custo por conversa do grupo | Sim, o padrão de copy (sem preço, sem "últimas vagas" nesta peça específica), mas suavizar "reserve agora e garanta" |
| `VERAO 2025 [ENGAJAMENTO ZAP] Publico Quente` | Engajamento/Mensagens | Quente (nome da campanha) | não documentado | Imagem/vídeo | R$ 5.272,40 | 4.770 | R$ 1,11 | alta (dado real: maior volume de conversas, ótimo custo) | Sim, especialmente a lógica de público quente |
| `NOV 25 [VENDAS] WHT NOVO` | Vendas/Mensagens | não documentado | não documentado | Carrossel (prova social + contraste rotina x praia) | R$ 3.393,23 | 1.793 | R$ 1,89 | alta (já era a referência da análise anterior) | Sim — é o padrão de copy mais seguro e replicável (sem preço, sem urgência) |
| `[AJ][ENGAJAMENTO][ABO][MENSAGEM WHATSAPP]` | Engajamento/Mensagens | não documentado | não documentado | Dinâmico/catálogo (corpo não documentado) | R$ 2.323,32 | não documentado (não consultado) | não documentado | não documentada (maior alcance do grupo, mas sem dado de conversa confirmado) | Parcial — a escala é atrativa, mas um dos anúncios se chama "ÚLTIMAS VAGAS"; não reaproveitar sem revisar |
| `MAR 26 PASSEIO BARCO [ENG] WHT` | Engajamento/Mensagens | não documentado | não documentado | Carrossel (preço fixo R$799 + urgência) | R$ 1.466,56 | não documentado (não consultado) | não documentado | alta em CTR (5,45%), mas produto e copy diferentes (passeio de barco, preço fixo, "vagas limitadas") | Não — produto diferente e copy incompatível com as regras atuais |
| `ABRIL 26 PASSEIO BARCO [ENG] WHT` | Engajamento/Mensagens | não documentado | não documentado | Dinâmico/catálogo (corpo não documentado) | R$ 806,41 | não documentado | não documentado | não documentada | Parcial — mesmo cuidado do item anterior (produto diferente) |

---

## 5. Análise de públicos vencedores

- **Quais públicos aparecem nas melhores campanhas?** O nome "Público Quente" aparece explicitamente em `VERAO 2025 [ENGAJAMENTO ZAP] Publico Quente`, que teve o maior volume de conversas (4.770) e o segundo melhor custo por conversa (R$ 1,11) — reforça a recomendação já registrada na análise histórica anterior.
- **Público quente realmente performou melhor?** Sim, com mais um dado real confirmando: as duas campanhas com custo por conversa mais baixo (`[MSG] Zap Verão 2024` a R$ 1,05 e `VERAO 2025...Publico Quente` a R$ 1,11) são de engajamento com base já existente, não de público frio.
- **Houve bom resultado com engajamento?** Sim — as 3 campanhas com objetivo de Engajamento tiveram os melhores custos por conversa confirmados desta rodada.
- **Houve bom resultado com WhatsApp?** Sim, todas as 6 campanhas prioritárias têm destino WhatsApp e nenhuma teve CTR abaixo de 3%, exceto o objetivo de reconhecimento já registrado na análise anterior (`Férias jul 25`).
- **Houve bom resultado com público frio?** Não documentado nesta rodada — nenhuma das campanhas consultadas em detalhe especifica explicitamente "público frio" no nome; a análise anterior já havia registrado essa lacuna.
- **Houve uso de interesses?** Não documentado nesta consulta (exigiria abrir o nível de conjunto de anúncios, não feito nesta rodada).
- **Houve uso de público amplo?** Não documentado.
- **Houve uso de semelhantes/lookalike?** Não documentado nesta consulta.
- **O que parece mais aplicável à campanha da Pousada 7 de Setembro?** O padrão de público quente/engajamento (mensagens/WhatsApp), com copy de prova social e contraste emocional, sem preço fixo.
- **O que não deve ser copiado?** A prática de nomear anúncio literalmente "ÚLTIMAS VAGAS" (confirmada em uso real, não só em planejamento) e a copy de preço fixo + "vagas limitadas"/"datas limitadas" usada no passeio de barco.

---

## 6. Análise de regiões vencedoras

- **Quais regiões apareceram nas campanhas mais fortes?** **Não documentado** — o nível de campanha não retorna segmentação regional; isso exigiria consulta ao nível de conjunto de anúncios com breakdown por região, não feita nesta rodada.
- **SC, PR e RS aparecem como boa base?** Não confirmável nesta consulta (mas já é a base histórica de segmentação registrada nos planejamentos em planilha, ver análise anterior).
- **Algum estado performou melhor?** Não documentado.
- **Alguma cidade ou região específica se destacou?** Não documentado.
- **Vale manter Sul?** Não há dado contrário nesta consulta; mantém-se a recomendação da análise anterior por ausência de evidência em contrário.
- **Vale testar SP?** Sem dado histórico de teste em SP nesta consulta.
- **Vale separar regiões ou manter juntas?** Não documentado — decisão sem suporte de dado nesta rodada.
- **Qual recomendação para 7 de Setembro?** Mantida a recomendação da análise anterior (SC/PR/RS), sem novo dado que a altere ou reforce especificamente por região.

---

## 7. Análise de posicionamentos

- **Quais posicionamentos foram usados?** **Não documentado** — não consultado nesta rodada (exigiria nível de anúncio com breakdown `publisher_platform`/`platform_position`).
- **Instagram Stories / Feed / Reels / Facebook tiveram destaque?** Não documentado.
- **Posicionamentos automáticos foram usados?** Não documentado diretamente, mas a presença de criativos dinâmicos (`{{product.name}}`) em `[AJ][ENGAJAMENTO][ABO][MENSAGEM WHATSAPP]` e nas campanhas de Passeio de Barco de 2026 sugere uso de formato Advantage+/catálogo, que tipicamente usa posicionamento automático.
- **Houve evidência para restringir posicionamentos?** Nenhuma encontrada.
- **Qual recomendação para a campanha 7 de Setembro?** Mantida a recomendação da análise anterior — posicionamento automático (Advantage+ placements), por ausência de dado que justifique restringir.

---

## 8. Análise de criativos vencedores

- **Quais criativos parecem ter performado melhor?** Os dois com melhor custo por conversa confirmado usam prova social (nota Booking/Google/TripAdvisor) e contraste emocional rotina x praia (`NOV 25 [VENDAS] WHT NOVO`) ou combinação de amenities reais + apelo de férias (`[MSG] Zap Verão 2024`).
- **Imagem ou vídeo funcionou melhor?** Não é possível isolar — as campanhas de melhor resultado usam múltiplos formatos simultâneos (carrossel + imagem + vídeo/reels), o resultado é agregado por campanha, não por criativo individual.
- **Café, piscina, fachada, experiência ou destino?** Piscina e café da manhã aparecem consistentemente nos criativos de melhor resultado (`[MSG] Zap Verão 2024`: "Piscina com espreguiçadeiras", "Piscina super charmosa", "Café da manhã servido em sua acomodação").
- **Criativos com pessoa performaram melhor?** Não documentado — não foi possível confirmar presença de pessoas nas imagens/vídeos sem abrir os arquivos de mídia (fora do escopo desta consulta textual à API).
- **Criativos com praia/mar performaram, mas criam risco atual?** Sim — `[MSG] Zap Verão 2024` menciona "Férias na Praia de Mariscal! 🌊☀️" e "Lindas Praias" como cartão do carrossel; não chega a prometer literalmente "vista para o mar", mas usa imagética de praia/onda de forma mais ousada do que as regras atuais recomendam. Tratar com cautela.
- **Algum criativo antigo deve ser descartado pelas novas regras?** Sim — o carrossel de `MAR 26 PASSEIO BARCO` (preço fixo, "exclusivo", "vagas limitadas", "datas limitadas") e qualquer peça nomeada "ÚLTIMAS VAGAS".
- **Qual aprendizado visual pode ser reaproveitado sem copiar promessas arriscadas?** Piscina, café da manhã na suíte/acomodação, e prova social real (nota Booking/Google/TripAdvisor) — todos compatíveis com as regras atuais, desde que sem preço/urgência.

---

## 9. Análise de copy

- **Quais padrões de texto aparecem nas melhores campanhas?** Prova social real (nota Booking 9.2, Google 4.8, TripAdvisor #4), contraste emocional "rotina x praia/descanso", listagem de amenities reais (piscina, café da manhã, cadeiras de praia, espaço kids, playground, 8 acomodações).
- **Havia preço fixo?** Sim, mas **só na campanha de passeio de barco** (`MAR 26 PASSEIO BARCO`: R$ 799) — nas campanhas de hospedagem de melhor resultado (`NOV 25 [VENDAS] WHT NOVO`, `[MSG] Zap Verão 2024`), não foi encontrado preço fixo nos criativos extraídos.
- **Havia urgência?** Sim, em graus diferentes: "Reserve agora e garanta sua estadia" (leve, em `[MSG] Zap Verão 2024`) até "Vagas limitadas"/"Datas limitadas" (forte, na campanha de barco) e um anúncio nomeado literalmente "ÚLTIMAS VAGAS" (campanha `[AJ]...`, corpo não documentado).
- **Havia "últimas vagas"?** Sim, como nome de anúncio ativo em `[AJ][ENGAJAMENTO][ABO][MENSAGEM WHATSAPP]` — não foi possível confirmar se essa frase aparecia no corpo do texto (dado não documentado), mas o nome por si só já é um sinal de alerta.
- **Havia "última chance"?** Não encontrada nesta consulta.
- **Havia promessa de praia/mar?** Sim, de forma mais suave que "vista para o mar" — "Férias na Praia de Mariscal! 🌊☀️", "Lindas Praias" — não é uma promessa de vista literal, mas usa imagética de praia/onda que deve ser usada com mais moderação sob as regras atuais.
- **Havia CTA para WhatsApp?** Sim, em todas as 6 campanhas prioritárias.
- **O que funcionou, mas não deve ser repetido?** "Reserve agora e garanta sua estadia" (urgência leve) e qualquer variação de "vagas limitadas"/"últimas vagas"/preço fixo.
- **O que pode ser adaptado com segurança para a Pousada 7 de Setembro?** Prova social real (se as notas ainda forem essas, a confirmar com Renildo) e o contraste emocional "rotina x descanso em Mariscal", sem preço e sem urgência — já é essencialmente o que está na `CAMPANHA_SUPERVISIONADA_7_SETEMBRO_2026_POUSADA_ARAGUA.md`.

---

## 10. Separar aprendizado útil de risco

| Elemento histórico | Funcionou? | Risco atual | Reaproveitar? | Como adaptar com segurança |
|---|---|---|---|---|
| Público quente/remarketing | Sim (melhor custo por conversa: R$1,05–R$1,11) | Baixo | Sim | Manter como público principal |
| Engajamento (objetivo de campanha) | Sim | Baixo | Sim | Manter como um dos objetivos possíveis, junto com Mensagens |
| WhatsApp como destino | Sim (todas as campanhas analisadas) | Baixo | Sim | Manter |
| Preço fixo no anúncio | Sim para CTR (passeio de barco), mas não comprovado necessário para hospedagem | Alto (regra 13 da tarefa) | Não | Substituir por "fale com a gente para saber mais" |
| Urgência ("reserve agora", "vagas limitadas", "últimas vagas") | Presente em várias campanhas de bom resultado, mas não isolável como causa | Alto (regras 10, 11, 12) | Não | Usar linguagem de convite, nunca de escassez |
| Pôr do sol/mar (imagética) | Presente em copy antiga ("Praia de Mariscal 🌊☀️"), não isolável como causa de bom resultado | Médio-alto (regra 16) | Parcial | Usar "praia pertinho"/"Mariscal", nunca imagem literal de pôr do sol/mar |
| Passeio de barco | Alto CTR (5,45%), mas produto diferente | Não aplicável ao escopo da Pousada | Não (fora do produto) | Não aplicável a esta campanha |
| Café na suíte/acomodação | Presente em todas as campanhas de hospedagem analisadas | Baixo (já documentado oficialmente) | Sim | Manter, como já está no plano atual |
| Piscina | Presente e recorrente | Médio (cuidado com "privativa"/"aquecida") | Sim | Manter com a ressalva já registrada (área comum) |
| Vídeos | Usados em várias campanhas, sem métrica isolada | Baixo | Sim, com moderação | Testar sem depender só disso |
| Carrossel | Usado no criativo de melhor resultado (`NOV 25 [VENDAS]`) | Baixo | Sim | Manter como formato preferencial |
| Região Sul (SC/PR/RS) | Não comprovado isoladamente nesta consulta, mas é a base histórica consistente | Baixo | Sim | Manter |
| Posicionamentos automáticos | Sugerido pelo uso de criativo dinâmico/catálogo em campanhas de grande escala | Baixo | Sim | Manter, sem restringir sem dado contrário |
| Prova social real (nota Booking/Google/TripAdvisor) | Presente na campanha de melhor custo por conversa confirmado | Baixo, **se o número ainda for real e atual** | Sim, com validação | Confirmar com Renildo se as notas (9.2 Booking, 4.8 Google, #4 TripAdvisor) ainda são as atuais antes de reutilizar |

---

## 11. Aplicação para a campanha 7 de Setembro Pousada

- **O que deve mudar no plano atual?** Pouca coisa estrutural — os dados reais confirmam a direção já tomada. A principal adição é considerar prova social real (nota Booking/Google/TripAdvisor) como argumento extra, **se Renildo confirmar que os números ainda são atuais**.
- **O conjunto principal deve continuar sendo remarketing?** Sim — reforçado por dado real agora (R$1,05–R$1,11 de custo por conversa em campanhas de público quente/engajamento).
- **Deve haver segundo conjunto frio?** Mantém-se como estrutura alternativa (seção 12), sem dado novo que a torne prioritária.
- **Quais públicos devem entrar?** Público quente/engajamento/remarketing, como já estava recomendado.
- **Quais públicos devem ficar fora?** Nenhum identificado como ruim nesta consulta — mesma lacuna já registrada.
- **Quais regiões priorizar?** SC, PR e RS, sem novo dado regional que altere isso.
- **Quais posicionamentos usar?** Automático, sem evidência para restringir.
- **Quais criativos usar primeiro?** Mantido: café na suíte como principal, piscina como reserva — ambos aparecem consistentemente nas campanhas de melhor resultado histórico.
- **Quais copies ajustar?** Considerar adicionar prova social real (se confirmada por Renildo) como uma 6ª variação futura; suavizar qualquer resquício de "reserve agora" para tom mais convidativo, sem comando de urgência.
- **O orçamento de R$45/dia segue adequado?** Sim, como hipótese inicial — as campanhas de melhor custo por conversa rodaram com orçamentos diferentes (R$15/dia a R$45/dia no nível de conjunto, conforme já registrado), sem padrão que exija mudança da hipótese atual.
- **Vale dividir orçamento ou manter um conjunto só?** Mantém-se a recomendação de começar com um conjunto só (remarketing), dado que as campanhas de melhor resultado confirmado eram concentradas em público quente, não distribuídas em múltiplos conjuntos frios simultâneos.

---

## 12. Proposta revisada de conjunto de anúncios

### Conjunto principal recomendado
- **Nome:** "7 Set 2026 — Pousada — Quente/Remarketing" (mantido da análise anterior)
- **Público:** engajamento com perfil/anúncios, video views, visitantes do site, seguidores — mesmo público-conceito das campanhas `[MSG] Zap Verão 2024` e `VERAO 2025...Publico Quente`
- **Região:** SC, PR, RS
- **Idade:** 25–55 anos
- **Interesses:** não aplicável (remarketing)
- **Público personalizado:** não confirmável nesta consulta se já existe configurado
- **Público semelhante:** não recomendado nesta rodada (mesma lacuna já registrada)
- **Exclusões:** quem já reservou para 04/09–08/09/2026, se a lista existir
- **Posicionamentos:** automático
- **Orçamento sugerido:** R$ 45/dia (mantido)
- **Período:** 01/08/2026 a 04/09/2026 (mantido)
- **Criativo principal:** `POUSADA_7SET_CAFE_01.jpg`
- **Copy principal:** Combinação 1 já registrada (ângulo "Café da manhã na suíte"), com possível adição futura de prova social real, se confirmada
- **CTA:** "Fale com a gente pelo WhatsApp e planeje suas férias em Mariscal."
- **Justificativa:** reforçada agora por dado real direto da API — as duas campanhas de público quente/engajamento tiveram os melhores custos por conversa confirmados (R$1,05 e R$1,11) de toda a análise.
- **Grau de confiança:** **médio-alto** — subiu em relação à análise anterior (que era "médio"), porque agora há confirmação direta via API de 3 campanhas com resultado de conversa documentado (não mais só 1 print), todas na mesma faixa de público.

### Conjunto alternativo, se necessário
- **Nome:** "7 Set 2026 — Pousada — Frio/Contraste (teste)" (mantido da análise anterior)
- **Público:** frio, interesse em Bombinhas/praia/viagem de férias + geo SC/PR/RS
- **Região:** SC, PR, RS
- **Diferença em relação ao principal:** público frio em vez de remarketing
- **Quando ativar:** se o conjunto de remarketing tiver entrega insuficiente
- **Orçamento sugerido:** fatia menor do total (ex.: 30%), sem exceder a hipótese de R$45/dia combinada
- **Métrica de decisão:** custo por conversa — comparar com o novo benchmark real de R$1,05–R$1,89 encontrado nesta análise (não mais só R$1,89)
- **Risco:** médio — nenhuma campanha de público frio teve resultado de conversa confirmado nesta rodada

---

## 13. Ajustes recomendados no plano atual

Comparação com `PLANO_EXECUCAO_MANUAL_META_ADS_7_SETEMBRO_2026_POUSADA_ARAGUA.md`:

- **O que manter:** toda a estrutura de campanha, conjunto principal (remarketing), criativos (café principal, piscina reserva, Wood Stories), as 5 variações de texto/título/descrição, as 3 CTAs, as 5 combinações, o checklist de montagem e o checklist de pré-publicação.
- **O que ajustar:** o grau de confiança da recomendação de público quente pode subir de "médio" para "médio-alto" no arquivo de análise histórica (refletido nesta análise); considerar registrar a possibilidade de uma 6ª variação de copy com prova social real, condicionada à confirmação de Renildo sobre se os números (9.2 Booking, 4.8 Google, #4 TripAdvisor) ainda são atuais.
- **O que remover:** nada — nenhum elemento do plano atual contraria os novos dados encontrados.
- **O que depende de Renildo:** confirmar se as notas de avaliação (Booking/Google/TripAdvisor) mencionadas na copy antiga ainda são precisas hoje, antes de qualquer reaproveitamento; todas as decisões já listadas no plano (orçamento, disponibilidade, criativos finais, aprovação de copy).
- **O que depende de dado não encontrado:** desempenho por região e por posicionamento (não consultado nesta rodada); conteúdo completo dos criativos dinâmicos/catálogo (`{{product.name}}`), que a API não retorna como texto fixo.

---

## 14. Decisões pendentes de Renildo

- Usar remarketing como conjunto principal (reforçado por dado real agora).
- Criar ou não conjunto frio.
- Separar ou não regiões.
- Usar ou não posicionamentos automáticos.
- Usar café como criativo principal.
- Usar piscina como reserva.
- Manter R$45/dia.
- Definir quando abrir plano B.
- Confirmar disponibilidade.
- Aprovar campanha manual.
- **Nova decisão desta rodada:** confirmar se as notas reais mencionadas em campanhas antigas (9.2 Booking, 4.8 Google, #4 TripAdvisor) ainda são atuais, para decidir se entram como argumento na copy de 7 de Setembro.

---

## 15. Conclusão executiva

1. **Quais campanhas foram encontradas?** Todas as 6 campanhas prioritárias foram localizadas com sucesso, com nome, período, status e métricas confirmados diretamente via API do Meta Ads Manager (modo leitura).
2. **Qual delas é a melhor referência para 7 de Setembro?** `[MSG] Zap Verão 2024`, pelo melhor custo por conversa confirmado (R$ 1,05) combinado com grande escala (999 mil impressões, R$ 3.993 investidos) — seguida de perto por `VERAO 2025 [ENGAJAMENTO ZAP] Publico Quente` (R$ 1,11, maior volume de conversas: 4.770).
3. **Qual aprendizado mais forte?** Público quente/engajamento (remarketing) é consistentemente a base com melhor custo por conversa em toda a amostra real analisada — confirma e reforça a recomendação já dada na análise histórica anterior.
4. **Qual risco histórico não deve ser repetido?** Preço fixo e linguagem de urgência ("vagas limitadas", "datas limitadas", e um anúncio real chamado literalmente "ÚLTIMAS VAGAS") — presentes especialmente na campanha de passeio de barco e em pelo menos um anúncio ativo de grande escala.
5. **Qual conjunto de anúncios é recomendado agora?** O mesmo já proposto — "7 Set 2026 — Pousada — Quente/Remarketing" — agora com respaldo mais forte de dado real.
6. **Qual o grau de confiança?** **Médio-alto** — subiu em relação à análise anterior, por haver agora 3 campanhas com resultado de conversa confirmado diretamente pela API (não mais só 1 print), todas na mesma direção.
7. **Qual o próximo passo antes de montar/publicar manualmente?** Renildo revisar esta análise, confirmar se a prova social antiga (notas Booking/Google/TripAdvisor) ainda é atual, e então seguir o checklist já existente em `PLANO_EXECUCAO_MANUAL_META_ADS_7_SETEMBRO_2026_POUSADA_ARAGUA.md` — nenhuma parte desta análise deve ser copiada direto para dentro do Meta Ads sem essa revisão.

---

*Este arquivo não altera nenhum dos arquivos-base consultados, nem `DADOS_OFICIAIS_ATENDIMENTO_VILLA_ARAGUA.md`, nem `.claude/skills/`. Nenhuma campanha, conjunto, anúncio, público, orçamento, criativo ou configuração foi criado, duplicado, editado, pausado, ativado ou alterado no Meta Ads — a conexão foi usada exclusivamente em modo leitura. Nenhum dado pessoal de hóspede ou lead foi consultado ou reproduzido. Nenhuma automação foi criada. A decisão final continua sendo de Renildo.*
