# Guia digital, blog e site

Orientação de qual conteúdo vira página fixa de site, artigo de blog, seção de guia digital, ou FAQ — e como cada um se conecta ao WhatsApp e ao Instagram.

**Pendência conhecida**: não existe hoje um blog ou site com conteúdo publicado neste projeto — este arquivo planeja a estrutura para quando esse canal existir, usando `GUIA_DIGITAL_HOSPEDE_VILLA_ARAGUA.md` como o documento mais próximo de "conteúdo de site" já estruturado.

## Páginas fixas do site (institucionais, não mudam com frequência)

- **Página inicial** — posicionamento da marca, "Férias Pra Sempre", link para Pousada e Casa separadamente.
- **Pousada Arágua** — página de produto, diferenciais reais, as 8 acomodações.
- **Casa Arágua** — página de produto, diferenciais reais (nunca "garagem").
- **Sobre nós / História** — baseada em `HISTORIA_E_POSICIONAMENTO_VILLA_ARAGUA.md` (desde 2007, Mariscal).
- **Guia de Bombinhas/Mariscal** — página pilar de região, ponto de entrada para os clusters (`clusters-bombinhas-mariscal.md`).
- **Como reservar / Reserva direta** — argumento de valor da reserva direta, CTA para WhatsApp.
- **Contato** — WhatsApp oficial, sem inventar outro canal.

## Artigos de blog (conteúdo que se renova, bom para SEO)

Estrutura de artigo por cluster (ver `clusters-bombinhas-mariscal.md`), por exemplo:
- "Praia de Mariscal: o que esperar e por que ela é ideal para família"
- "O que fazer em Bombinhas em dia de chuva"
- "Pousada Arágua ou Casa Arágua: qual escolher" (ver `conteudo-pousada-casa.md`)
- "Onde ficar em Bombinhas: por que Mariscal"
- Artigos sazonais (ver `temas-sazonais-feriados.md`), publicados com antecedência suficiente para captar busca antes da data.

Cada artigo deve ter um objetivo claro (que etapa da jornada ele serve, ver `jornada-conteudo-hospede.md`) e um CTA coerente com esse objetivo — artigo de descoberta não força CTA de reserva imediata; artigo de decisão sim.

## Guia digital (hóspede já reservado ou em estadia)

Já existe uma base real e validada em `GUIA_DIGITAL_HOSPEDE_VILLA_ARAGUA.md` — esta skill não recria esse conteúdo, apenas organiza como ele se conecta à estratégia geral:
- Seções de guia digital cobrem: chegada, check-in, Wi-Fi, café da manhã, estacionamento, regras — todas etapa 6/7 da jornada (`jornada-conteudo-hospede.md`).
- Conteúdo do guia digital pode (e deve) ser reaproveitado em formato reduzido no WhatsApp (mensagens automáticas de pré-chegada) e no Instagram (destaque "Como reservar"/"Guia rápido"), sempre mantendo os dados sensíveis (senha de Wi-Fi, senha de lock box) fora de qualquer conteúdo público.

## FAQ da Pousada

Baseada nas dúvidas reais documentadas em `ROTEIRO_RECEPCIONISTA_IA.md`/`DADOS_OFICIAIS_ATENDIMENTO_VILLA_ARAGUA.md`: café da manhã, piscina comum, estacionamento, distância da praia, capacidade por acomodação, pet, criança. Ver estrutura de perguntas equivalente em `duvidas-objeções-como-conteudo.md`.

## FAQ da Casa Arágua

Baseada nas mesmas fontes, com as particularidades da Casa: piscina privativa, taxa de limpeza (R$ 450,00), estacionamento exclusivo em área aberta (nunca "garagem"), capacidade até 6 pessoas. Café da manhã não é oferecido pela Casa em nenhuma condição (regra atualizada 2026-08-07).

## Páginas comparativas

- "Pousada Arágua x Casa Arágua" (ver `conteudo-pousada-casa.md`).
- "Reservar direto x Booking/Airbnb/Decolar" — argumento de valor (atendimento próximo, sem intermediário), nunca comparação de preço com número inventado (ver `villa-aragua-pricing-revenue/references/concorrentes-otas.md`).

## Páginas de feriado

Página temporária ou seção reaproveitável por data (7 de Setembro, Natal, Réveillon, Carnaval) — conteúdo alinhado com `temas-sazonais-feriados.md`, sempre validando oferta com `villa-aragua-pricing-revenue` antes de publicar valor.

## Conteúdos reaproveitáveis entre canais

| Conteúdo de origem | Reaproveitamento no WhatsApp | Reaproveitamento no Instagram |
|---|---|---|
| Página "Pousada x Casa" | Resposta resumida quando o lead está indeciso (`villa-aragua-sales-receptionist`) | Carrossel comparativo (`villa-aragua-social-media-manager`) |
| Artigo de região (ex.: praias) | Resposta a dúvida de concierge durante a estadia | Post/reel de dica de Mariscal |
| Seção do guia digital (check-in, Wi-Fi) | Mensagem automática de pré-chegada | Destaque "Guia rápido" |
| FAQ Pousada/Casa | Respostas padrão de objeção (`villa-aragua-sales-receptionist`) | Caixa de perguntas / destaque de dúvidas |
| Artigo sazonal/feriado | Mensagem de campanha (`AGENTE_IA_MARKETING_VENDAS_META_ADS_VILLA_ARAGUA.md`) | Post/story de contagem regressiva real |

## Como usar este arquivo na prática

1. Definir se o conteúdo é institucional (página fixa), renovável (blog) ou de suporte pós-reserva (guia digital/FAQ).
2. Verificar se já existe uma versão do conteúdo em outro documento oficial (ex.: Guia Digital) antes de propor um novo do zero — reaproveitar sempre que possível.
3. Planejar o reaproveitamento entre canais desde a origem, evitando recriar o mesmo conteúdo do zero para cada canal.
4. Gerar o briefing (`briefings-para-outras-skills.md`) especificando o formato de destino (página de site, artigo, seção de guia, FAQ).
