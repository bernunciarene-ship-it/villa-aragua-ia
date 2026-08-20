# Schema e dados estruturados

Orientação segura para sugerir dados estruturados (schema.org) — esta skill **nunca aplica código**, apenas recomenda o que seria adequado, sempre como sugestão a validar tecnicamente antes de publicar.

## Regra mais importante deste arquivo

Schema é uma promessa técnica de que "o que está marcado corresponde exatamente ao que está visível na página". Marcar algo que não aparece visivelmente é enganoso e pode prejudicar a confiança técnica do site (além de ser contra as diretrizes das próprias ferramentas de busca). Por isso, toda sugestão de schema aqui é condicionada a existir o conteúdo real e visível correspondente.

## Tipos de schema possíveis, e quando cada um faz sentido

### LodgingBusiness / Hotel
- Faz sentido para: página institucional da Pousada Arágua e da Casa Arágua (cada uma com sua própria marcação, nunca uma só cobrindo os dois produtos como se fossem a mesma unidade).
- Conteúdo que precisaria estar visível na página antes de marcar: nome, endereço/região, descrição, comodidades reais (as mesmas listadas em `DADOS_OFICIAIS_ATENDIMENTO_VILLA_ARAGUA.md`).
- Cuidado: não marcar "amenity" que não está confirmada (ex.: não marcar piscina privativa na página da Pousada).

### LocalBusiness
- Faz sentido para: a Villa Arágua como marca guarda-chuva, ou para o Google Perfil da Empresa (fora do escopo desta skill, mas conceitualmente relacionado).
- Mesmo cuidado: dados de contato (WhatsApp oficial) só se estiverem realmente visíveis na página.

### FAQPage
- Faz sentido para: qualquer página com bloco de FAQ visível (ver `faq-pousada-casa-bombinhas.md`).
- Regra obrigatória: **a resposta marcada no schema precisa ser exatamente a mesma que aparece visível na página** — nunca uma versão resumida ou diferente só para o schema.
- Nunca criar FAQPage para perguntas que a página não responde de fato.

### BreadcrumbList
- Faz sentido para: qualquer página dentro de uma hierarquia clara (ex.: Início > Acomodações > Casa Arágua).
- Baixo risco — é estrutural, não faz afirmação de fato sobre o negócio.

### TouristDestination ou TouristAttraction
- Faz sentido, com cautela, para: página de guia de Bombinhas/Mariscal (`guia-bombinhas-mariscal.md`), quando ela descrever a região como destino.
- Cuidado: normalmente esse schema é mais adequado para a página institucional/de turismo (órgão oficial de turismo), não para o site de uma hospedagem falando de terceiros — usar apenas se fizer sentido estrutural real, e sinalizar como algo a validar com um especialista técnico antes de aplicar.

### Product ou Offer
- **Uso mais delicado desta lista.** Só sugerir se:
  1. Houver preço/oferta já aprovado por `villa-aragua-pricing-revenue`;
  2. Esse preço estiver **visível na própria página** (não escondido, não diferente do que aparece para o usuário);
  3. A oferta for real e vigente no momento da publicação (nunca oferta expirada ou hipotética).
- Se qualquer uma dessas três condições não for atendida, a recomendação correta é **não sugerir este schema agora**.

## O que nunca fazer, em qualquer schema

- Não marcar conteúdo que não aparece visivelmente na página.
- Não inventar rating/nota (ex.: "4.9 estrelas") sem que isso venha de uma fonte real e visível (Google, Booking, TripAdvisor) devidamente referenciada.
- Não inventar review/depoimento — só usar avaliação real de `AVALIACOES/`, com o texto exato, nunca reescrito para caber no schema.
- Não inventar preço ou disponibilidade.
- Não usar schema de forma enganosa para tentar aparentar mais completude do que a página realmente tem.
- Não criar FAQPage com resposta que não está na página.
- Sempre sugerir validação técnica (por quem cuida do site) antes de publicar qualquer marcação — esta skill não implementa código.

## Como apresentar uma sugestão de schema

Formato recomendado ao propor:

```
SUGESTÃO DE SCHEMA (a validar tecnicamente antes de aplicar)
Página: [nome]
Tipo sugerido: [LodgingBusiness / FAQPage / BreadcrumbList / etc.]
Campos que teriam correspondência visível na página: [lista]
Campos que NÃO devem ser incluídos ainda (motivo): [ex.: "rating — não há nota agregada confirmada/visível ainda"]
Status: sugestão editorial, requer implementação e validação técnica antes de publicar
```

## Como usar este arquivo na prática

1. Só considerar schema depois que a página já existe e está com o conteúdo final visível (nunca marcar antes do conteúdo existir).
2. Escolher o tipo mais adequado da lista acima, verificando as três condições do `Product`/`Offer` com rigor extra.
3. Apresentar como sugestão formatada (ver modelo acima), nunca como implementação já feita.
4. Encaminhar para validação técnica humana antes de qualquer aplicação real no site.
