# Experimentos de crescimento

Modelo para testar hipóteses de forma rápida e barata, sem comprometer caixa ou operação. Um experimento é uma aposta pequena e com prazo definido — não uma campanha permanente.

## Modelo de experimento

```
EXPERIMENTO DE GROWTH — VILLA ARÁGUA
Hipótese: [frase clara do tipo "se fizermos X, esperamos Y"]
Produto: [ ] Pousada Arágua  [ ] Casa Arágua  [ ] Ambos (com métricas separadas)
Canal: [Meta Ads / Instagram / WhatsApp / parceria / conteúdo / outro]
Público: [casal / família / grupo / hóspede antigo / geral]
Oferta ou ângulo: [o que está sendo testado — nunca oferta inventada; se envolver valor, validar antes com villa-aragua-pricing-revenue]
Duração: [prazo definido, ex.: 7-14 dias]
Orçamento: [valor real disponível, ou "sem custo direto" se for esforço/tempo]
Métrica de sucesso: [conversa qualificada, taxa de resposta, reserva — nunca curtida/alcance isolado]
Critério para manter: [o que precisa acontecer para continuar]
Critério para pausar: [o que indica que não está funcionando]
Aprendizado esperado: [o que queremos descobrir, independente do resultado ser bom ou ruim]
```

## Por que todo experimento precisa de prazo e critério definidos antes de começar

Sem isso, a tendência natural é continuar um experimento ruim por otimismo, ou abandonar um bom cedo demais por ansiedade. Definir os critérios de manter/pausar antes de rodar remove essa subjetividade — depois, a decisão é só olhar o dado e aplicar o critério já combinado (ver `villa-aragua-campaign-analytics/references/decisoes-otimizacao.md`).

## Exemplos de experimento (estrutura, não resultado — nenhum número abaixo é dado real)

### Campanha para hóspedes antigos
- Hipótese: reativar hóspedes antigos com mensagem pessoal gera reserva mais barata e mais rápida que público frio.
- Canal: WhatsApp direto (se houver lista) ou Instagram/remarketing.
- Público: hóspede antigo.
- Ângulo: reconexão, "voltar a Mariscal", sem oferta obrigatória (só se houver aprovação de condição especial).
- Duração: 14 dias.
- Orçamento: baixo/sem custo direto se for só WhatsApp; baixo se envolver impulsionamento.
- Métrica de sucesso: taxa de resposta e reservas geradas por esse público, comparado a público frio no mesmo período.
- Critério para manter: taxa de resposta/reserva visivelmente melhor que a média de público frio.
- Critério para pausar: nenhuma resposta relevante após o prazo, mesmo com abordagem ajustada uma vez.
- Aprendizado esperado: se hóspede antigo é, de fato, o canal de menor custo/maior confiança que a teoria sugere.

### Teste Casa Arágua para grupos
- Hipótese: comunicar a Casa Arágua como opção para grupos de amigos (não só família) amplia o público qualificado.
- Canal: Meta Ads (conjunto de anúncio segmentado) ou Instagram.
- Público: grupo de amigos, 25-45 anos.
- Ângulo: privacidade, espaço, estacionamento para até 3 carros (nunca "garagem"), cozinha completa.
- Duração: 7-14 dias.
- Orçamento: fatia pequena do orçamento já existente da Campanha 2 — Casa Arágua.
- Métrica de sucesso: conversas qualificadas desse público específico.
- Critério para manter: volume de conversa qualificada compatível com o custo por conversa já observado em outros públicos da Casa.
- Critério para pausar: leads fora do perfil (ex.: pedido de evento/festa) ou custo por conversa muito acima do padrão.
- Aprendizado esperado: se "grupo de amigos" é um público que vale segmentar separado de "família".

### Teste Pousada para famílias
- Hipótese: destacar café da manhã + área de lazer (playground, redes) gera mais conversa qualificada de famílias que destacar só a suíte.
- Canal: Meta Ads ou Instagram.
- Público: famílias com crianças.
- Ângulo: praticidade + estrutura para criança, sem prometer monitoria/recreação.
- Duração: 7-14 dias.
- Métrica de sucesso: conversas qualificadas de perfil família.
- Critério para manter/pausar: comparação direta com o criativo/ângulo anterior usado para o mesmo público.
- Aprendizado esperado: qual ângulo (café x estrutura de lazer) comunica melhor para esse perfil.

### Remarketing para quem pediu preço
- Hipótese: quem perguntou preço e sumiu responde melhor a um lembrete com prova social do que a repetição da mesma oferta.
- Canal: Meta Ads (remarketing) + follow-up de WhatsApp (`villa-aragua-sales-receptionist/references/follow-up.md`).
- Público: quem iniciou conversa mas não fechou.
- Ângulo: reforço de confiança (avaliação real, história desde 2007), não repetição de preço.
- Duração: 14 dias.
- Métrica de sucesso: taxa de reengajamento (resposta ao remarketing/follow-up).
- Aprendizado esperado: se prova social reativa melhor do que insistência em preço/oferta.

### Conteúdo sobre Mariscal
- Hipótese: conteúdo de utilidade sobre a região (praias, dia de chuva) atrai gente na etapa de descoberta, mesmo sem falar da Villa Arágua diretamente.
- Canal: Instagram orgânico ou blog (ver `villa-aragua-content-strategy/references/clusters-bombinhas-mariscal.md`).
- Público: geral (topo de funil).
- Duração: contínuo, mas avaliar em ciclos de 30 dias.
- Métrica de sucesso: salvamentos, compartilhamentos, cliques para o perfil/WhatsApp.
- Aprendizado esperado: se conteúdo de região (sem venda direta) gera tráfego/conversa relevante o suficiente para justificar o tempo investido.

### Parceria com restaurante
- Hipótese: uma indicação cruzada com um restaurante já citado no concierge (ex.: Moquém) gera reconhecimento mútuo e possíveis indicações de hóspede.
- Canal: parceria local (ver `parcerias-locais-bombinhas.md`).
- Duração: sem prazo fixo — é relação, não campanha; avaliar em 60-90 dias.
- Métrica de sucesso: menções/indicações mútuas percebidas, não um número fechado.
- Aprendizado esperado: se vale formalizar mais parcerias desse tipo.

### Sequência de WhatsApp para lead que sumiu
- Hipótese: variar o gancho de cada mensagem de follow-up (já usado em `villa-aragua-sales-receptionist/references/follow-up.md`) aumenta taxa de resposta comparado a mensagens repetidas.
- Canal: WhatsApp.
- Duração: um ciclo completo de follow-up (24h/72h/7 dias) por lead.
- Métrica de sucesso: taxa de resposta em cada etapa do follow-up.
- Aprendizado esperado: qual gancho (disponibilidade, urgência real, deixar a porta aberta) performa melhor em qual etapa.

## Como decidir quantos experimentos rodar por vez

Regra para operação enxuta: **no máximo 1-2 experimentos simultâneos**, nunca mais — mais que isso dilui orçamento/tempo de atenção e torna impossível saber o que gerou qual resultado. Ver `rotina-semanal-growth.md` para como escolher qual experimento priorizar a cada ciclo.

## Como usar este arquivo na prática

1. Escrever a hipótese antes de qualquer outra coisa — se não é possível formular uma frase clara de "se X, então Y", o experimento não está maduro para rodar.
2. Preencher todos os campos do modelo antes de começar, especialmente os critérios de manter/pausar.
3. Escolher só 1-2 experimentos por ciclo, alinhados com o plano de `plano-growth-30-60-90.md`.
4. Ao final do prazo, aplicar o critério já definido — nunca redefinir o critério depois de ver o resultado.
