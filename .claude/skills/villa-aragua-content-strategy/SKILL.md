# Villa Arágua — Content Strategy

Esta skill ensina a **decidir o que a Villa Arágua deve criar de conteúdo** — pilares, temas prioritários, clusters, jornada do hóspede, calendário e briefings — para site, blog, guia digital, Instagram, Meta Ads e WhatsApp. É uma skill de planejamento e priorização, não de produção de peça final.

**Regra mais importante da skill, acima de qualquer outra**: esta skill **nunca escreve o texto final, a legenda, o roteiro visual ou a mensagem de WhatsApp**. Ela decide o quê criar, para quem, em que formato, em que canal e por quê — e produz o briefing que outra skill executa. Se a resposta esperada é uma peça pronta (post, anúncio, artigo, mensagem), a skill certa é a de execução (ver seção de integração), não esta.

## Fontes da verdade (não alterar, só consultar)

- `DADOS_OFICIAIS_ATENDIMENTO_VILLA_ARAGUA.md` — todo dado real que pode ou não virar conteúdo (regras, comodidades, horários, política de cancelamento, distâncias).
- `HISTORIA_E_POSICIONAMENTO_VILLA_ARAGUA.md` — história desde 2007, posicionamento emocional, "Férias Pra Sempre", vocabulário institucional já validado.
- `ROTEIRO_RECEPCIONISTA_IA.md` e `PROMPT_RECEPCIONISTA_IA_WHATSAPP.md` — as dúvidas e fluxos reais que os hóspedes trazem no WhatsApp, matéria-prima direta para conteúdo de utilidade e FAQ.
- `AGENTE_IA_MARKETING_VENDAS_META_ADS_VILLA_ARAGUA.md` — funil comercial (anúncio → WhatsApp → reserva), estrutura de campanha (TOF/MOF/BOF) e objetivo de reduzir dependência de OTA — referência de para onde todo conteúdo estratégico aponta.
- `GUIA_DIGITAL_HOSPEDE_VILLA_ARAGUA.md` — conteúdo já estruturado da jornada do hóspede (chegada, check-in, Wi-Fi, café, estacionamento) — fonte direta para páginas de guia/FAQ.
- `BOMBINHAS/VILLA ARAGUA IA 📄 CONCIERGE BOMBINHAS.docx` — banco real de praias (Mariscal, Canto Grande, Tainha, Quatro Ilhas, Sepultura), restaurantes, cafés, trilhas, passeios e roteiros por perfil (casal, família, dia de chuva) — base dos clusters de região.
- `ACOMODACOES/` (fotos, docs de objeções e "quando indicar cada acomodação") e `ACOMODACOES/CASA ARAGUA/VILLA ARAGUA 📁 CASA ARÁGUA.docx` — diferenciais reais por produto/acomodação.
- `AVALIACOES/` (prints Google, Booking, TripAdvisor) — matéria-prima real de prova social, nunca depoimento inventado.
- `CHECKLIST_DECISOES_CAMPANHA_REABERTURA_VILLA_ARAGUA_2026.md` e `.claude/skills/villa-aragua-pricing-revenue/references/calendario-sazonalidade.md` — calendário comercial real (reabertura 01/08/2026, 7 de Setembro com pacote confirmado, classificação de temporada).
- `MARKETING E VENDAS/VILLA ARAGUA 📄 PERFIL DOS HÓSPEDES.docx` e `MARKETING E VENDAS/VILLA ARAGUA 📄 FOLLOW-UP DE LEADS.docx` — perfis de hóspede e cadência comercial, para alinhar conteúdo com o momento certo do funil.
- `MARKETING E VENDAS/CAMPANHAS META ADS/` — histórico de campanhas e criativos já produzidos, para identificar o que já foi coberto e o que ainda é lacuna.
- As referências das outras sete skills do projeto (ver seção de integração abaixo).

**Atualização**: a skill `villa-aragua-ai-seo-geo` já existe no projeto (`.claude/skills/villa-aragua-ai-seo-geo/`) e recebe desta skill os temas/clusters priorizados para estruturar busca orgânica e citabilidade por IA generativa — ver seção de integração abaixo. Ainda não existe, porém, blog ou site com conteúdo publicado neste projeto — esta skill continua planejando pensando nesses canais como destino a construir, não como infraestrutura já existente.

## Como usar esta skill

1. **Antes de qualquer plano de conteúdo** → `pilares-conteudo-villa.md` — os 12 pilares estratégicos da marca.
2. **Para pensar por etapa da jornada do hóspede** → `jornada-conteudo-hospede.md`.
3. **Para temas de região (Bombinhas/Mariscal)** → `clusters-bombinhas-mariscal.md`.
4. **Para ajudar o lead a escolher entre os dois produtos** → `conteudo-pousada-casa.md`.
5. **Para calendário comercial e feriados** → `temas-sazonais-feriados.md`.
6. **Para decidir o que vira página fixa, artigo de blog ou seção de guia digital** → `guia-digital-blog-site.md`.
7. **Para transformar dúvida/objeção real em tema de conteúdo** → `duvidas-objeções-como-conteudo.md`.
8. **Para organizar tudo isso no tempo** → `calendario-conteudo-mensal.md`.
9. **Para entregar o plano pronto para execução** → `briefings-para-outras-skills.md`.
10. **Para auditar o que já existe e decidir manter/atualizar/unir/arquivar/apagar** → `auditoria-conteudo.md` (critérios) + `politica-keep-update-merge-kill.md` (regra de decisão).
11. **Para estruturar topic clusters completos (pilar + satélites)** → `clusters-topicos.md`.
12. **Para brifar qualquer conteúdo novo com todos os campos necessários** → `brief-conteudo.md`.
13. **Para o plano editorial macro em três fases** → `calendario-30-60-90.md`.
14. **Para transformar um conteúdo em várias peças por canal** → `reaproveitamento-conteudo.md`.
15. **Para revisar um conteúdo com checklist de otimização** → `seo-otimizacao-conteudo.md`.

## Motor de Conteúdo da Villa Arágua

Esta camada da skill organiza o trabalho em seis modos de uso — invocáveis como comandos de raciocínio (`/content:audit`, `/content:cluster`, `/content:brief`, `/content:calendar`, `/content:repurpose`, `/content:seo`) ou simplesmente pedidos em linguagem natural ("audita o conteúdo da Casa Arágua", "monta o cluster de Mariscal"). Cada modo tem um arquivo de referência dedicado e um objetivo de função clara — nenhum conteúdo entra no motor sem servir a pelo menos uma destas funções: **atrair, educar, comparar, converter, ajudar o hóspede ou apoiar reserva direta**.

### `/content:audit` — auditar conteúdo existente
Revisa o que já existe (site, blog, guia digital, FAQs, posts antigos, conteúdo de feriado, conteúdo de região) e classifica cada peça como manter, atualizar, unir, reaproveitar, arquivar ou apagar (apagar sempre com aprovação humana). Ver `auditoria-conteudo.md` e `politica-keep-update-merge-kill.md`.

### `/content:cluster` — estruturar topic clusters
Organiza um pilar em página pilar + conteúdos satélites, com perguntas respondidas, intenção de busca, público, CTA e links internos. Ver `clusters-topicos.md` (complementa, sem substituir, `clusters-bombinhas-mariscal.md` e `pilares-conteudo-villa.md`).

### `/content:brief` — brifar um conteúdo novo
Gera o briefing completo de uma peça específica antes de qualquer execução — título provisório, objetivo, público, etapa da jornada, intenção de busca, produto, dados oficiais, objeção respondida, CTA, links internos, prova social e skill de execução. Ver `brief-conteudo.md` (complementa `briefings-para-outras-skills.md`, que foca no formato de entrega por skill).

### `/content:calendar` — planejar no tempo
Monta o plano editorial de 30/60/90 dias, separado por canal (site, blog, guia digital, Instagram, WhatsApp, campanhas, apoio a Meta Ads). Ver `calendario-30-60-90.md` (plano macro em fases) e `calendario-conteudo-mensal.md` (execução mês a mês, já existente).

### `/content:repurpose` — reaproveitar um conteúdo em várias peças
Pega um conteúdo principal já validado e decompõe em página de site, artigo, FAQ, post/carrossel/reels/stories de Instagram, mensagem de WhatsApp, resposta da Recepcionista IA, copy de anúncio e mensagem para hóspede antigo — sem recriar do zero em cada canal. Ver `reaproveitamento-conteudo.md`.

### `/content:seo` — otimizar para busca e citabilidade
Checklist de otimização de qualquer página/artigo antes de publicar (H1, H2 em forma de pergunta, resposta direta, FAQ, links internos, title, meta description, alt text). Ver `seo-otimizacao-conteudo.md` — esta skill decide o que otimizar editorialmente; a estrutura técnica avançada de citabilidade por IA e schema continua sendo `villa-aragua-ai-seo-geo`.

**Regra de fundo dos seis modos**: nenhum deles decide preço/oferta (isso é sempre `villa-aragua-pricing-revenue`), nenhum escreve a peça final (isso é sempre a skill de execução indicada), e nenhum promete ranking ou posição garantida em busca/IA (isso é sempre tratado como objetivo de clareza e utilidade, nunca como garantia).

## Princípio central — conteúdo é ponte, não vitrine

Toda decisão desta skill responde a uma pergunta: esse conteúdo ajuda alguém a decidir vir para a Villa Arágua, ou é só ocupar espaço? Conteúdo bom é útil mesmo para quem ainda não vai reservar (dica de praia, resposta a dúvida real) e, ao mesmo tempo, sempre deixa um caminho claro de volta para o WhatsApp quando a pessoa estiver pronta. Conteúdo que não serve a nenhum dos dois objetivos não entra no plano.

## Os quatro tipos de conteúdo (nunca misturar sem intenção)

- **Informativo**: responde uma dúvida real (horário, regra, distância, o que fazer em dia de chuva) — não vende, ajuda.
- **Inspiracional**: desperta desejo de viver a experiência (clima de férias, bastidores, região) — não informa dado prático, transmite sensação.
- **Comparativo**: ajuda a decidir entre opções (Pousada x Casa, Villa Arágua x reserva por OTA) — sempre com critério real, nunca comparação inventada.
- **Comercial**: conecta diretamente com reserva (oferta de feriado, CTA de reserva direta) — a menor fatia do plano, nunca o conteúdo dominante.

Todo tema desta skill se classifica em pelo menos um desses tipos — se um conteúdo tenta ser os quatro ao mesmo tempo, geralmente fica fraco em todos.

## O que esta skill nunca faz

- Nunca escreve a peça final — decide o quê, para quem, por quê e em que formato; quem escreve é a skill de execução correspondente.
- Nunca inventa preço, disponibilidade, regra, comodidade, depoimento ou dado turístico (horário de restaurante, existência de passeio, distância) — todo dado turístico vem de `BOMBINHAS/VILLA ARAGUA IA 📄 CONCIERGE BOMBINHAS.docx` ou de arquivo oficial equivalente.
- Nunca mistura diferencial/oferta da Pousada com o da Casa Arágua no mesmo conteúdo, salvo peça comparativa explícita e claramente identificada.
- Nunca chama o estacionamento da Casa Arágua de "garagem" ou "garagem coberta" — sempre "estacionamento exclusivo em área aberta para até 3 carros".
- Nunca transforma o plano de conteúdo em lista só de peças promocionais — todo calendário/plano equilibra informativo, inspiracional, comparativo e comercial.
- Nunca prioriza um tema só porque "parece ter volume de busca" sem also considerar relevância comercial real para a Villa Arágua — SEO/alcance é critério de priorização, não o único.

## Integração com as outras skills do projeto

Esta é a oitava skill do ecossistema Villa Arágua. Ela **decide o que criar e por quê**; a execução acontece nas outras skills, nesta cadeia:

- **`villa-aragua-content-strategy`** (esta skill) decide o que criar e por quê — tema, prioridade, cluster, briefing, calendário, e a decisão de manter/atualizar/unir/arquivar/apagar conteúdo já existente.
- **`villa-aragua-ai-seo-geo`** recebe o tema/briefing definido aqui e estrutura para busca orgânica e citabilidade por IA generativa (pergunta principal, resposta direta, FAQ, subtópicos, sugestão de dado estruturado) — decide a estrutura, não o tema.
- **`villa-aragua-copywriting-conversion`** escreve o texto final (artigo, página, CTA) a partir do briefing e da estrutura definidos.
- **`villa-aragua-humanizer-pt-br`** humaniza qualquer texto produzido, garantindo que soa como a Villa Arágua e não como conteúdo genérico de turismo.
- **`villa-aragua-social-media-manager`** adapta o tema/pilar definido aqui para o formato e a rotina do Instagram — esta skill decide o tema, aquela decide como ele vira post/story/reels.
- **`villa-aragua-creative-design-ads`** orienta a direção visual de qualquer peça que precise de imagem/vídeo.
- **`villa-aragua-sales-receptionist`** transforma o interesse gerado pelo conteúdo em conversa de WhatsApp e usa as FAQs/respostas diretas desta skill como base de resposta — o conteúdo precisa preparar o terreno para exatamente essa conversa, sem prometer o que a Recepcionista IA não vai confirmar depois.
- **`villa-aragua-campaign-analytics`** mede o resultado do conteúdo que virou campanha ou peça publicada (tráfego, leads, reservas, quando houver dado) — retroalimentando esta skill sobre o que gerou avanço real no funil, para priorizar melhor no próximo ciclo e para embasar `auditoria-conteudo.md`.
- **`villa-aragua-pricing-revenue`** valida qualquer preço, pacote ou condição que um conteúdo comercial/sazonal pretenda citar — nenhum valor entra em briefing, cluster ou conteúdo reaproveitado sem essa checagem.

Fluxo prático sugerido para um novo ciclo de conteúdo: `pilares-conteudo-villa.md` + `jornada-conteudo-hospede.md` (o que falta cobrir) → `/content:audit` (o que já existe e o que fazer com isso) → `/content:cluster` ou os temas concretos (`clusters-bombinhas-mariscal.md` / `conteudo-pousada-casa.md` / `temas-sazonais-feriados.md` / `duvidas-objeções-como-conteudo.md`) → `/content:brief` (briefing completo) → `villa-aragua-ai-seo-geo` estrutura para busca/IA → `villa-aragua-pricing-revenue` valida qualquer valor → a skill de execução certa produz a peça → `/content:repurpose` decompõe em outras peças por canal → `/content:calendar` organiza tudo no tempo (`calendario-30-60-90.md` + `calendario-conteudo-mensal.md`) → publicar → `villa-aragua-campaign-analytics` mede o resultado → o aprendizado volta para o próximo `/content:audit`.

## Pendências conhecidas (sinalizar, não inventar)

- Não existe hoje blog nem site com conteúdo publicado — esta skill planeja para esse destino, sem presumir infraestrutura já existente. `villa-aragua-ai-seo-geo` já existe e recebe os temas priorizados aqui para estruturar quando esse conteúdo for publicado.
- Não existe análise de concorrência de conteúdo/SEO (`CONCORRENTES/` é só lista de links do Booking, sem análise de posicionamento) — esta skill não compara conteúdo com concorrente nomeado.
- Não existe histórico consolidado de quais conteúdos/campanhas já geraram melhor resultado (`MARKETING E VENDAS/CAMPANHAS META ADS/HISTORICO CAMPANHAS META ADS/` ainda não foi lido/consolidado por nenhuma skill) — priorização de tema por desempenho passado é hipótese até essa consolidação existir, e a auditoria (`auditoria-conteudo.md`) precisa sinalizar essa limitação sempre que faltar dado de tráfego/conversão real.
- O documento-fonte da Casa Arágua ainda usa "garagem" — esta skill sempre usa o termo corrigido "estacionamento exclusivo em área aberta".
