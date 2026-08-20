# Atribuição de canais

Como pensar de onde uma reserva realmente veio — e os limites reais dessa atribuição, que nunca devem ser escondidos numa análise.

## Canais a considerar

- **Meta Ads** (Instagram/Facebook pago) — campanhas ativas de Pousada, Casa Arágua e Remarketing.
- **Instagram orgânico** — conteúdo não pago (ver `villa-aragua-social-media-manager`).
- **WhatsApp direto** — contato que chegou sem clique rastreável (ex.: número salvo, indicação verbal).
- **Google** — busca orgânica ou Google Meu Negócio.
- **Booking** — reserva feita pela OTA (não é reserva direta, mas ainda é reserva da Villa Arágua).
- **Airbnb** — idem, outra OTA.
- **Decolar** — idem, quando aplicável.
- **Hóspede antigo** — reserva de quem já se hospedou antes, com ou sem campanha de reativação.
- **Indicação** — reserva por recomendação de outro hóspede/conhecido.

## Por que atribuição em turismo/hotelaria é sempre imperfeita

- **Múltiplos contatos**: a mesma pessoa pode ver um anúncio no Instagram, pesquisar no Google, salvar o WhatsApp e só reservar semanas depois — qualquer um dos pontos de contato poderia "levar o crédito".
- **Lead não lembra a origem**: quando perguntado, o hóspede pode dizer "vi vocês em algum lugar" sem precisar o canal exato.
- **Última reserva direta pode não ter vindo só do último clique**: alguém pode ter clicado num anúncio de remarketing, mas ter descoberto a Villa Arágua originalmente por indicação de um amigo meses antes.
- **OTA e direto podem se misturar na jornada**: o hóspede pode ver a Pousada no Booking, depois procurar o Instagram/WhatsApp para negociar direto — nesse caso, a "origem" comercial (o que trouxe a pessoa) e o "canal de fechamento" (onde a reserva foi processada) são diferentes e vale registrar os dois.

## Modelos simples de atribuição (usar o que for possível com o dado disponível)

1. **Primeiro contato**: atribuir a reserva ao canal onde a pessoa teve o primeiro ponto de contato conhecido (ex.: clicou num anúncio pela primeira vez). Bom para medir o que gera descoberta/topo de funil.
2. **Último contato**: atribuir ao canal que gerou a conversa que efetivamente terminou em reserva (ex.: clicou num anúncio de remarketing e fechou em seguida). Bom para medir o que fecha, mas esconde o esforço de descoberta anterior.
3. **Atribuição manual**: perguntar diretamente ao hóspede ("como você conheceu a Villa Arágua?") e registrar a resposta, mesmo que qualitativa — na ausência de rastreamento técnico robusto, esse é o modelo mais realista para a operação hoje.

**Recomendação prática**: usar atribuição manual como base (é o que a operação consegue coletar hoje pela conversa no WhatsApp) e primeiro/último contato como complemento quando houver dado de clique (ex.: relatório do Meta Ads mostrando que a pessoa veio de um anúncio específico).

## Como registrar sem inventar

- Se o lead não informou a origem e não há dado de clique, registrar como "origem não identificada" — nunca presumir um canal.
- Se houver mais de um canal plausível (ex.: cliente engajou com post orgânico e depois clicou em anúncio pago), registrar os dois e marcar como "atribuição dividida", em vez de forçar um único canal.
- Nunca atribuir a Meta Ads uma reserva que não tem nenhum rastro de clique/conversa vinda de campanha — isso infla artificialmente o ROAS da mídia paga.

## Cuidado especial: Pousada x Casa Arágua

Atribuir sempre por produto, nunca de forma genérica "veio da Villa Arágua" quando o dado permitir separar. Uma reserva da Casa Arágua atribuída à campanha errada (ex.: Campanha 1 — Pousada) distorce o CPA de ambas as campanhas.

## Cuidado especial: reserva direta x OTA

Reduzir dependência de OTA é objetivo estratégico explícito (`AGENTE_IA_MARKETING_VENDAS_META_ADS_VILLA_ARAGUA.md`). Isso não significa inflar artificialmente o número de "reserva direta" — uma reserva feita pelo Booking continua sendo Booking, mesmo que o hóspede tenha mandado uma mensagem de dúvida no WhatsApp antes. O critério é onde a reserva foi de fato processada/paga, não onde houve contato.

## Pendências conhecidas (sinalizar, não inventar)

- Não existe hoje comissão exata negociada com Booking/Airbnb/Decolar documentada nos arquivos oficiais — não inventar percentual ao comparar canal direto x OTA.
- A planilha `PLANILHA PRE RESERVAS E BOOKING.xlsx` existe, mas ainda não foi consolidada — qualquer proporção "X% direto, Y% OTA" hoje é hipótese, não dado.
- Não existe análise de preço/posicionamento dos concorrentes/OTAs monitorados — nunca comparar CPA por canal com concorrente nomeado (ver `villa-aragua-pricing-revenue/references/concorrentes-otas.md`).

## Como usar este arquivo na prática

1. Para cada reserva analisada, registrar o(s) canal(is) plausível(is) com o modelo de atribuição disponível (manual, primeiro contato, último contato).
2. Nunca forçar uma atribuição única quando há ambiguidade real — registrar como dividida ou não identificada.
3. Separar sempre por produto (Pousada x Casa) e por tipo de canal (pago x orgânico x OTA x indicação).
4. Ao comparar canais no relatório (`relatorio-semanal-mensal.md`), declarar qual modelo de atribuição foi usado — isso muda a leitura do resultado.
