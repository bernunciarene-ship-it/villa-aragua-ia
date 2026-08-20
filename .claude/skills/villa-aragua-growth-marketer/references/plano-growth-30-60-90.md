# Plano Growth 30, 60 e 90 dias

Modelo para estruturar o esforço de crescimento em três horizontes, do diagnóstico à decisão. Pensado para uma operação enxuta — o plano precisa caber no tempo real que Renildo/equipe tem disponível, não no tempo ideal de um manual de growth.

## Estrutura do plano (usar nos três horizontes)

```
PLANO GROWTH — VILLA ARÁGUA
Horizonte: [ ] 30 dias  [ ] 60 dias  [ ] 90 dias
Produto(s): [ ] Pousada Arágua  [ ] Casa Arágua  [ ] Ambos (com plano separado por produto)

1. DIAGNÓSTICO INICIAL
   - Onde a operação está agora: ocupação, campanhas ativas, dependência de OTA (dado real ou "não consolidado ainda")
   - Momento do calendário comercial (reabertura/feriado/baixa-média-alta temporada — ver villa-aragua-pricing-revenue/calendario-sazonalidade.md)
   - Principal gargalo identificado (aquisição, conversão no WhatsApp, ou retenção/retorno)

2. META PRINCIPAL
   - Uma meta central, realista e mensurável (ex.: "aumentar reservas diretas confirmadas", "reduzir tempo médio de resposta", "reativar X hóspedes antigos")
   - Nunca meta de vaidade (seguidores, curtidas, alcance) como meta principal isolada

3. CANAIS PRIORITÁRIOS
   - 1 a 3 canais escolhidos com base em canais-aquisicao-villa.md, nunca todos ao mesmo tempo

4. CAMPANHAS
   - Campanhas Meta Ads planejadas no período, sempre separadas por produto (Pousada/Casa)

5. CONTEÚDO
   - Temas/pilares do período, vindos de villa-aragua-content-strategy (se disponível) ou villa-aragua-social-media-manager

6. WHATSAPP
   - Ajustes esperados no funil de atendimento (tempo de resposta, follow-up, objeções) — acionar villa-aragua-sales-receptionist

7. HÓSPEDES ANTIGOS
   - Ação de reativação prevista no período (ver reativacao-hospedes-antigos.md)

8. PARCERIAS LOCAIS
   - Parceria(s) a explorar no período, se fizer sentido (ver parcerias-locais-bombinhas.md)

9. MÉTRICAS
   - Quais métricas acompanhar (remeter a villa-aragua-campaign-analytics — nunca recalcular fórmula aqui)

10. ROTINA SEMANAL
   - Referência a rotina-semanal-growth.md

11. DECISÃO AO FIM DO HORIZONTE
   - [ ] Manter   [ ] Ajustar   [ ] Matar experimento/canal
   - Justificativa com base em evidência real, não em impressão isolada
```

## Os três horizontes — o que muda entre eles

### 30 dias — validar
Foco em descobrir o que funciona com o menor risco possível. Testar 1-2 canais/experimentos por vez (ver `experimentos-crescimento.md`), nunca todos de uma vez — com orçamento pequeno (referência real: R$ 45,00/dia total já validado em `SETUP_INICIAL_META_ADS_7_SETEMBRO_VILLA_ARAGUA_2026.md`), não dá para diluir em muitas frentes. Meta típica: identificar 1-2 canais/ângulos que geram conversa qualificada de forma consistente.

### 60 dias — consolidar
Foco em repetir o que os primeiros 30 dias mostraram que funciona, com ajustes (público, copy, criativo — ver `villa-aragua-campaign-analytics/references/decisoes-otimizacao.md`), e começar a estruturar o que ainda não existe (ex.: lista de hóspedes antigos, primeira parceria local). Meta típica: taxa de conversão do funil estabilizando ou melhorando, com dado de mais de um período.

### 90 dias — escalar com critério
Só escalar orçamento/esforço nos canais com evidência acumulada de 60 dias — nunca escalar por resultado de uma semana isolada. Meta típica: reserva direta crescendo como proporção do total, com pelo menos um canal secundário (parceria, reativação, conteúdo) já rodando de forma estável.

## Como isso se conecta com a operação real da Villa Arágua hoje

Referência real disponível para calibrar o primeiro ciclo de 30/60/90 dias: a Pousada Arágua reabre em **01/08/2026** (confirmado), com estrutura de 3 campanhas já validada (Pousada, Casa, Remarketing) e orçamento de R$ 45,00/dia. Um plano de 30 dias hoje começaria naturalmente com o ciclo de reabertura; os 60 dias seguintes cobririam a consolidação pós-reabertura; os 90 dias já alcançariam a proximidade do 7 de Setembro (feriado com pacote confirmado).

## Regra de decisão ao fim de cada horizonte

- **Manter**: evidência consistente de avanço no funil (não só métrica de topo) ao longo do período — ver `villa-aragua-campaign-analytics/references/funil-whatsapp-reserva.md`.
- **Ajustar**: sinal misto — algo funciona parcialmente (ex.: bom CTR, conversa fraca) — ajustar público/copy/criativo antes de decidir manter ou matar.
- **Matar**: sem sinal de avanço no funil depois de tempo/orçamento suficiente para o algoritmo/canal aprender — não continuar por apego ou ansiedade de ter "algo rodando".

## Como usar este arquivo na prática

1. Rodar o diagnóstico inicial antes de definir qualquer meta — nunca copiar meta de outro período sem checar o momento atual.
2. Escolher poucos canais/experimentos por horizonte (ver `canais-aquisicao-villa.md` e `experimentos-crescimento.md`).
3. Cruzar com o calendário comercial real (`campanhas-sazonais-growth.md`) para não competir com ele.
4. Fechar cada horizonte com a decisão explícita de manter/ajustar/matar, alimentando o próximo ciclo do plano.
