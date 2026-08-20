# Prompts prontos

Modelos de prompt que o router pode **executar diretamente** (invocando as skills na sequência indicada) ou **devolver ao usuário** para ele rodar manualmente, quando a execução direta não for possível ou não for o que foi pedido. Cada modelo já indica a skill principal e as de apoio.

## Prompt para análise de campanha

```
Use villa-aragua-campaign-analytics para analisar a campanha [nome/período].
Inclua: investimento, leads, conversas qualificadas, reservas, funil completo (ver funil-whatsapp-reserva.md).
Se envolver receita/margem, cruze com villa-aragua-pricing-revenue.
Se o resultado apontar criativo fraco, avalie com villa-aragua-creative-design-ads.
Se apontar copy fraca, avalie com villa-aragua-copywriting-conversion.
Termine com uma recomendação: manter, pausar, ajustar ou escalar (villa-aragua-campaign-analytics/references/decisoes-otimizacao.md).
```

## Prompt para resposta de WhatsApp

```
Use villa-aragua-sales-receptionist para responder este lead: [colar mensagem do lead].
Diagnostique o perfil (casal/família/grupo/hóspede antigo/sensível a preço) antes de responder.
Se a resposta envolver preço, desconto ou pacote, valide com villa-aragua-pricing-revenue antes.
Finalize passando por villa-aragua-humanizer-pt-br para garantir tom acolhedor e natural.
```

## Prompt para criação de anúncio

```
Use villa-aragua-copywriting-conversion para criar um anúncio de [Pousada Arágua / Casa Arágua] com o ângulo [ângulo/oferta].
Se houver preço/oferta envolvida, valide com villa-aragua-pricing-revenue antes de escrever.
Peça a direção visual com villa-aragua-creative-design-ads para a peça que acompanha o texto.
Finalize com villa-aragua-humanizer-pt-br.
Nunca misture oferta/diferencial da Pousada com o da Casa no mesmo anúncio.
```

## Prompt para calendário Instagram

```
Use villa-aragua-social-media-manager para montar o calendário de [período] do Instagram da Villa Arágua.
Equilibre os pilares (inspiração, utilidade, bastidores, prova social, oferta) conforme a proporção já validada.
Peça as legendas com villa-aragua-copywriting-conversion e a direção visual com villa-aragua-creative-design-ads.
Finalize cada legenda com villa-aragua-humanizer-pt-br antes de considerar pronta para publicar.
```

## Prompt para página SEO/IA

```
Use villa-aragua-content-strategy para definir o tema/briefing de uma página sobre [tema].
Passe o briefing para villa-aragua-ai-seo-geo estruturar (pergunta principal, resposta direta, FAQ, subtópicos).
Escreva o texto final com villa-aragua-copywriting-conversion.
Finalize com villa-aragua-humanizer-pt-br.
Nunca inventar dado turístico, preço, distância ou estabelecimento que não esteja em arquivo oficial.
```

## Prompt para planejamento de conteúdo

```
Use villa-aragua-content-strategy para planejar o conteúdo de [site/blog/guia digital/Instagram] do próximo período.
Rode /content:audit no que já existe antes de propor conteúdo novo.
Organize por cluster com /content:cluster e monte o calendário com /content:calendar.
Sinalize qualquer lacuna que dependa de dado ainda não confirmado.
```

## Prompt para análise de preço/pacote

```
Use villa-aragua-pricing-revenue para avaliar [preço/pacote/diária/desconto] de [Pousada Arágua / Casa Arágua].
Considere temporada, ocupação, concorrência (sem inventar número de concorrente) e ponto de equilíbrio.
Se o resultado for uma condição nova a comunicar, prepare a mensagem com villa-aragua-sales-receptionist.
Deixe claro que qualquer decisão final de preço/desconto é de Renildo/equipe.
```

## Prompt para follow-up

```
Use villa-aragua-sales-receptionist para montar a sequência de follow-up do lead [contexto: pediu orçamento e sumiu / disse que vai pensar / etc.].
Siga a cadência já validada (24h / 72h / 7 dias) sem repetir a mesma mensagem.
Se o comportamento do lead for difícil de entender, consulte villa-aragua-marketing-psychology antes de escrever a mensagem.
Finalize com villa-aragua-humanizer-pt-br.
```

## Prompt para avaliar criativo

```
Use villa-aragua-creative-design-ads para avaliar o criativo [descrição/anexo] da [Pousada Arágua / Casa Arágua].
Aplique o checklist de criativo (checklist-criativo.md) daquela skill.
Se o criativo já rodou como anúncio, cruze o desempenho com villa-aragua-campaign-analytics antes de decidir manter/trocar.
Se precisar reescrever o texto sobreposto, acione villa-aragua-copywriting-conversion + villa-aragua-humanizer-pt-br.
```

## Como decidir entre executar direto ou devolver o prompt

- **Executar direto**: quando o pedido já tem contexto suficiente (produto, canal, dado necessário) e a sequência de skills está clara — o router aciona as skills na ordem definida e entrega o resultado.
- **Devolver o prompt pronto**: quando falta uma decisão do usuário (ex.: "para qual produto?", "qual período?"), quando o pedido é genérico demais para executar sem mais contexto, ou quando o próprio usuário pediu só "me dá o comando certo" em vez de pedir a execução.

## Como usar este arquivo na prática

1. Escolher o modelo mais próximo do pedido recebido.
2. Preencher os colchetes `[...]` com o contexto real do pedido.
3. Decidir (ver seção acima) se executa direto ou devolve o prompt para o usuário rodar.
4. Sempre informar, ao final, quais skills foram usadas ou recomendadas — nunca deixar implícito.
