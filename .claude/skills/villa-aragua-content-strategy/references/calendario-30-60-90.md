# Calendário 30/60/90 dias

Plano editorial macro em três fases — acionado pelo modo `/content:calendar`. Diferente de `calendario-conteudo-mensal.md` (que organiza a execução semana a semana dentro de um mês), este arquivo pensa o **arco de construção do motor de conteúdo** ao longo de 90 dias, por canal. Também é diferente do plano de `villa-aragua-growth-marketer/references/plano-growth-30-60-90.md` (que pensa canais de aquisição, orçamento e experimentos de growth) — aqui o foco é **o que produzir e organizar de conteúdo**, não onde investir mídia.

## Como as três fases se diferenciam

- **30 dias — fundação**: conteúdos essenciais e páginas de maior impacto (as que mais gente precisa encontrar primeiro).
- **60 dias — clusters e comparação**: expandir para topic clusters completos e conteúdo comparativo/decisório.
- **90 dias — otimização e sazonalidade**: revisar o que já existe, reaproveitar em outros formatos, fechar FAQs e cobrir conteúdo sazonal.

## Fase 1 — Primeiros 30 dias (fundação)

| Canal | O que priorizar |
|---|---|
| Site | Páginas essenciais: Pousada Arágua, Casa Arágua, Sobre nós/História, Contato/Reserva direta |
| Blog | 1-2 artigos-âncora (ex.: "Onde ficar em Mariscal com crianças", "Praia de Mariscal: o que esperar") |
| Guia digital | Garantir que `GUIA_DIGITAL_HOSPEDE_VILLA_ARAGUA.md` está organizado e pronto para virar página/seção, sem reinventar o conteúdo já validado |
| Instagram | Calendário semanal básico já em rotina (ver `villa-aragua-social-media-manager`) |
| WhatsApp | FAQs essenciais prontas para a Recepcionista IA usar (`faq-pousada-casa-bombinhas.md`, da skill `villa-aragua-ai-seo-geo`) |
| Campanhas | Alinhar conteúdo com a campanha ativa no momento (ex.: reabertura, se for o período) |
| Apoio a Meta Ads | Conteúdo institucional (Sobre nós, páginas de produto) pronto para servir de destino de clique, mesmo que o anúncio leve direto ao WhatsApp |

## Fase 2 — 60 dias (clusters e comparação)

| Canal | O que priorizar |
|---|---|
| Site | Página comparativa Pousada x Casa; página "O que fazer em Bombinhas"; página de reserva direta completa |
| Blog | Satélites dos clusters de `clusters-topicos.md` (viagem com crianças, viagem em casal, grupos) |
| Guia digital | Seções reaproveitadas em formato de FAQ pública (ver `reaproveitamento-conteudo.md`) |
| Instagram | Conteúdo comparativo (carrossel Pousada x Casa) e prova social mais recorrente |
| WhatsApp | Respostas de objeção mais refinadas, alimentadas pelo que os clusters já cobriram |
| Campanhas | Conteúdo de apoio para a próxima data comercial relevante (ver `temas-sazonais-feriados.md`) |
| Apoio a Meta Ads | Página de destino específica por público (família/casal/grupo), quando fizer sentido para o anúncio |

## Fase 3 — 90 dias (otimização, reaproveitamento e sazonalidade)

| Canal | O que priorizar |
|---|---|
| Site | Rodar `/content:audit` no que já foi publicado; aplicar `seo-otimizacao-conteudo.md` em todas as páginas |
| Blog | Fechar lacunas identificadas na auditoria; unir conteúdos que competem entre si |
| Guia digital | Revisão de atualidade (dados ainda batem com `DADOS_OFICIAIS_ATENDIMENTO_VILLA_ARAGUA.md`?) |
| Instagram | Reaproveitar os conteúdos de maior desempenho em novos formatos (ver `reaproveitamento-conteudo.md`) |
| WhatsApp | FAQ consolidada e revisada, incorporando as dúvidas reais observadas nos 60 dias anteriores |
| Campanhas | Conteúdo sazonal específico da próxima janela comercial (feriado seguinte, temporada) |
| Apoio a Meta Ads | Revisar quais páginas/conteúdos de apoio geraram melhor resultado (via `villa-aragua-campaign-analytics`, quando houver dado) e replicar o padrão |

## Como este calendário se conecta com a operação real da Villa Arágua

Referência de calibração para o primeiro ciclo real: a Pousada Arágua reabre em **01/08/2026** (confirmado em `CHECKLIST_DECISOES_CAMPANHA_REABERTURA_VILLA_ARAGUA_2026.md`). Um primeiro ciclo de 30/60/90 dias hoje naturalmente começaria cobrindo a reabertura na Fase 1 (páginas essenciais + conteúdo institucional), a Fase 2 já se aproximando do 7 de Setembro (feriado com pacote confirmado, exclusivo da Pousada), e a Fase 3 revisando o que funcionou no período de maior movimento.

## Regras permanentes em qualquer fase

- Nunca inventar preço, disponibilidade, estabelecimento ou dado turístico em qualquer conteúdo planejado nas três fases.
- Sempre diferenciar Pousada Arágua e Casa Arágua — nenhuma fase mistura oferta dos dois produtos no mesmo conteúdo, salvo peça comparativa explícita.
- Nunca chamar o estacionamento da Casa Arágua de "garagem" ou "garagem coberta".
- Nenhuma fase deve virar só conteúdo comercial — a proporção de tipos de conteúdo (`pilares-conteudo-villa.md`) se mantém em todas as fases.

## Como usar este arquivo na prática (`/content:calendar`)

1. Identificar em qual fase (30/60/90) a operação está, considerando o que já foi produzido até agora.
2. Usar a tabela da fase correspondente para escolher prioridades por canal.
3. Cruzar com `temas-sazonais-feriados.md` para não competir com o calendário comercial real.
4. Detalhar a execução semana a semana com `calendario-conteudo-mensal.md`, que continua sendo o nível de organização tática dentro de cada fase.
