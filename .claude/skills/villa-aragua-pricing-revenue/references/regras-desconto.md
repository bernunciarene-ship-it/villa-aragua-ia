# Estratégia de desconto

Princípio central (fonte: `AGENTE_IA_MARKETING_VENDAS_META_ADS_VILLA_ARAGUA.md` e `DADOS_OFICIAIS_ATENDIMENTO_VILLA_ARAGUA.md`): **a IA apoia decisões de preço, não decide desconto sozinha.** Preço, desconto, disponibilidade e exceção operacional continuam sendo decisão de Renildo/equipe.

## Quando NÃO dar desconto

- Como primeira resposta a "tem desconto?" — reforçar valor antes de falar em preço (ver `comunicacao-preco-whatsapp.md`).
- Em datas de alta procura, ocupação forte ou poucas unidades disponíveis — condições que, segundo o Revenue Manager, indicam manter ou até subir preço, não reduzir.
- Só porque o lead mencionou "vi mais barato" em outro canal/concorrente — comparação de canal não é motivo automático de desconto (ver `concorrentes-otas.md`).
- Para "fechar rápido" uma conversa — nunca ofereça condição especial apenas para acelerar a resposta do lead; isso corrói margem sem necessidade.
- Sem confirmar antes: período exato, número de diárias, forma de pagamento. Sem esses três dados, não há base nem para avaliar se uma condição é possível.

## Quando considerar desconto (sempre como sugestão, nunca como decisão própria da IA)

- Reserva direta (fora de OTA) — argumento de valor mais forte que desconto: atendimento próximo do início ao fim da estadia, sem taxa de plataforma.
- Pagamento à vista — pode ser um caminho de negociação, mas o formato/percentual precisa ser confirmado com a equipe; não existe percentual fixo oficial documentado.
- Hóspede antigo / recorrente — pode receber comunicação de reativação com tom mais pessoal, mas isso não é sinônimo automático de desconto (ver `follow-up.md` da skill `villa-aragua-sales-receptionist`).
- Fechamento de pacote com mínimo de diárias maior do que o padrão — pode justificar uma condição especial, mas segue sob consulta.
- Última hora (data muito próxima, baixa ocupação, leads não convertendo) — é justamente a situação em que o Revenue Manager indica "reduzir preço ou criar oferta" (ver `CLAUDE.md`, seção Revenue Manager); ainda assim, quem decide o valor final é Renildo/equipe.

## O que já está oficialmente definido (preço aprovado, não é "desconto")

- **Parcelamento no cartão**: número de parcelas segue a tabela oficial por faixa de valor à vista (`DADOS_OFICIAIS_ATENDIMENTO_VILLA_ARAGUA.md`, item 51 — até R$1.300 → 3x; até R$1.600 → 4x; até R$2.000 → 5x; acima de R$2.000 → 6x, teto absoluto, sem opção de 10x); há acréscimo interno de **7%** usado só no cálculo, nunca citado ao hóspede — nunca prometer parcelamento sem juros.
- **Criança até 6 anos gratuita**: é política de precificação já validada, não um desconto concedido pela IA — ainda assim, sempre confirmar idade e capacidade da acomodação.
- **Redução de diárias após reserva confirmada**: sob consulta, depende de antecedência, canal de venda e disponibilidade — devolução ou crédito não é automático.

## Como proteger margem

- Nunca ser a primeira a mencionar a palavra "desconto" — só responder se o lead perguntar.
- Reforçar sempre o que está incluso antes de falar em valor: localização, estrutura, café da manhã (Pousada), privacidade e piscina privativa (Casa), atendimento próximo.
- Tratar reserva direta como o principal argumento de valor frente a OTAs — a "vantagem" que se oferece é serviço e proximidade, não preço mais baixo.
- Nunca inventar comparação de preço com concorrente específico (ver `concorrentes-otas.md`) para justificar desconto.
- Nunca empilhar duas condições especiais na mesma negociação (ex.: desconto + parcelamento sem juros) sem validação da equipe.

## Como responder "tem desconto?" sem desvalorizar a pousada

Resposta-padrão (já validada, fonte: `objecoes-vendas.md` da skill `villa-aragua-sales-receptionist`):

> "Podemos verificar conforme o período, número de diárias e forma de pagamento 😊 Me confirme o período e o número de pessoas que vejo se existe alguma condição possível."

Isso evita dois erros comuns: (1) dizer "não" de forma seca, que soa rígido; (2) dizer "sim" sem saber se há margem, que compromete a negociação antes mesmo de ter os dados. A resposta mantém a porta aberta sem prometer nada.

## Quando escalar para autorização humana

- Pedido de desconto além do padrão, cancelamento ou reembolso.
- Pedido de condição especial combinando múltiplos benefícios (desconto + parcelamento + brinde, por exemplo).
- Lead comercial grande (ex.: grupo fechando várias acomodações, agência, evento) pedindo tarifa corporativa/atacado.
- Qualquer negociação em que o lead insista após a resposta-padrão de "posso verificar".
- Redução de diárias, remarcação ou crédito futuro solicitados pelo hóspede.
