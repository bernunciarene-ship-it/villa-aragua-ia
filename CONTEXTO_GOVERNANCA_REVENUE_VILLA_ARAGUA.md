# CONTEXTO E GOVERNANÇA DO MÓDULO REVENUE — VILLA ARÁGUA IA

**Status:** persistido
**Origem:** pacote "Villa Arágua IA — Revenue Management e Precificação", recebido de Renildo em 2026-07-24
**Encaixe no cérebro:** este módulo **não cria agente ou skill novos** — estende o agente `villa-precificacao-calendario` (`.claude/agents/`) e a skill `villa-aragua-pricing-revenue` (`.claude/skills/`), que já existiam e já cobriam esta função. Ver decisão registrada no final deste arquivo.

---

## 1. Escopo inicial

Este módulo trata somente da Villa Arágua como operação de hospedagem:

- Pousada Arágua
- Casa Arágua Mariscal

Nesta fase, ficam fora da decisão de preço:

- renda patrimonial;
- despesas familiares;
- MANECO;
- saldo geral da travessia.

Essas caixas voltam depois na análise financeira geral (ver regra de separação financeira, `CLAUDE.md` e `DNA VILLA ARAGUA/`), mas não devem contaminar a definição do preço operacional da hospedagem.

## 2. Objetivo

Criar um sistema simples, confiável e utilizável de precificação e Revenue Management para ajudar Renildo a:

- conhecer o custo real de cada operação;
- definir preço mínimo, preço-alvo e preço de oportunidade;
- monitorar concorrentes;
- ajustar preços conforme demanda, ocupação, antecedência e sazonalidade;
- preservar margem;
- evitar preços definidos só por intuição;
- melhorar rentabilidade;
- aumentar previsibilidade;
- tomar decisões mais rápidas e frias.

## 3. Governança obrigatória

A Villa Arágua IA pode:

- analisar;
- calcular;
- comparar;
- apresentar cenários;
- recomendar;
- explicar a recomendação;
- registrar riscos;
- aguardar decisão humana.

A Villa Arágua IA não pode:

- alterar tarifas automaticamente;
- publicar preço em canal real (Stays, Booking, Airbnb, WhatsApp);
- confirmar reserva;
- confirmar disponibilidade;
- conceder desconto;
- prometer exceção;
- falar preço final ao hóspede sem aprovação humana;
- substituir Renildo em decisão sensível.

Estas regras são as mesmas regras máximas já em vigor para todos os agentes da Villa Arágua IA (`DEFINICAO_AGENTES_VILLA_ARAGUA_IA.md`, seção 2) — este módulo não cria uma exceção nem uma segunda governança.

## 4. Princípio de implementação

A ordem do projeto é:

1. Método
2. Dados
3. Regras
4. Modelo de decisão
5. Skills
6. Agentes
7. Automação futura

Não criar automações reais no primeiro momento.

## 5. Separação de produtos

A análise deve sempre separar:

### Pousada Arágua

Acomodações:
- Apto Organic
- Suíte Fuego
- Suíte Metallo
- Suíte Terra
- Suíte Wood
- Suíte Acqua
- Apto Luna
- Duplex Soleil

### Casa Arágua Mariscal

Produto separado, mais premium:
- casa completa;
- piscina privativa;
- churrasqueira;
- privacidade;
- família/grupo;
- até 6 pessoas;
- praia próxima.

## 6. Régua interna da Pousada Arágua (`REGRA_APROVADA_RENILDO`) e posição da Casa Arágua (hipótese)

**Status: `REGRA_APROVADA_RENILDO`, 2026-07-25** — régua percentual da Pousada Arágua, base = Organic/Fuego/Metallo. Define a hierarquia matemática para análises futuras de precificação; não altera automaticamente tarifas já publicadas — ajuste real no motor continua exigindo decisão humana e aplicação manual por Renildo.

| Acomodação | Multiplicador | Quando vale |
|---|---|---|
| Organic / Fuego / Metallo | ×1,00 | base |
| Terra / Wood | ×1,15 | sempre |
| Acqua | ×1,25 | sempre |
| Luna | ×1,32 | sempre |
| Duplex Soleil | ×1,63 | média temporada, alta temporada, feriados, datas especiais, Natal, Réveillon, janeiro, Carnaval, Páscoa |
| Duplex Soleil (exceção) | ×1,50 | baixa temporada pura: **maio, junho, agosto** e outros períodos fracos definidos por Renildo |

Detalhe completo, correção do "+12%" para "+15%" em Terra/Wood, e validação cruzada com o inventário publicado em `.claude/skills/villa-aragua-pricing-revenue/references/matriz-precos-pousada-casa.md`.

**Ainda hipótese, não decisão fechada:** a posição da Casa Arágua frente ao Duplex Soleil. A Casa Arágua **não entra nesta régua percentual** — é produto separado, com régua própria. Em datas fortes, ela tende a precisar ficar acima do Duplex Soleil, salvo decisão humana registrada ou evidência comercial clara. Essa parte já foi parcialmente validada na prática para Carnaval 2027 e janeiro/2027 pós-06/01 (ver `DECISOES_REVENUE_PENDENTES_VILLA_ARAGUA.md`, cards 2 e 3), mas segue sendo decisão período a período, não regra geral aprovada.

## 7. Fontes deste módulo

- `INVENTARIO_TARIFAS_PUBLICADAS_AGO2026_ABR2027.csv` — dado bruto, machine-readable.
- `INVENTARIO_TARIFAS_PUBLICADAS_AGO2026_ABR2027.md` — mesmo dado, agrupado por régua de acomodação, legível.
- `DIAGNOSTICO_PRELIMINAR_REVENUE_VILLA_ARAGUA.md` — leitura, alertas e ordem de trabalho sugerida.
- `.claude/skills/villa-aragua-pricing-revenue/references/tarifas-publicadas-2026-2027.md` — versão resumida desta mesma informação, para uso direto pela skill.

**Aviso de proveniência, válido para todo o módulo:** os valores do inventário foram **transcritos visualmente de prints do Stays/Arágua**, não extraídos por integração. Antes de qualquer alteração real de tarifa, confirmar os valores diretamente no sistema. Nenhum destes arquivos deve ser tratado como fonte de dado oficial no mesmo nível de `DADOS_OFICIAIS_ATENDIMENTO_VILLA_ARAGUA.md` até essa confirmação.

## 8. Decisão de encaixo no cérebro Villa Arágua IA (2026-07-24)

O pacote original propunha um agente novo (`villa-revenue-orquestrador.md`) e um arquivo de skill novo (`villa-aragua-pricing-revenue.md`). Ao conferir a arquitetura real do projeto, os dois já existiam:

- `.claude/agents/villa-precificacao-calendario.md` — já é o "Agente de Apoio à Decisão Comercial" da v1 (`DEFINICAO_AGENTES_VILLA_ARAGUA_IA.md`, seção 10), com a mesma função descrita para o orquestrador de Revenue proposto.
- `.claude/skills/villa-aragua-pricing-revenue/` — já existe como skill madura, com `SKILL.md` e 7 arquivos de referência (matriz de preços, calendário/sazonalidade, pacotes de feriado, regras de desconto, concorrentes/OTAs, ponto de equilíbrio, comunicação de preço no WhatsApp).

Decisão: **não duplicar**. Este módulo estende os dois arquivos existentes em vez de criar novos. Detalhe da extensão:

1. Novo arquivo de referência na skill: `tarifas-publicadas-2026-2027.md`.
2. Atualização de `matriz-precos-pousada-casa.md` e `calendario-sazonalidade.md` para registrar que a diária diferenciada por temporada, antes tratada como "a definir", agora tem tarifas publicadas transcritas — com o aviso de proveniência da seção 7 acima.
3. Atualização de `villa-precificacao-calendario.md` para citar as novas fontes e incorporar o vocabulário de diagnóstico (seção 9) e a regra Casa Arágua x Duplex Soleil (seção 6) como critério sugerido.

Isso mantém a arquitetura do cérebro Villa Arágua IA sem crescer artificialmente — o objetivo original do pacote (apoiar decisão de preço) é entregue pelos mesmos arquivos que já faziam isso, agora com dado real.

## 9. Vocabulário de diagnóstico

Toda recomendação de preço deste módulo deve usar um destes estados, não texto livre:

- `MANTER`
- `CORRIGIR_AGORA`
- `SUBIR_COM_CAUTELA`
- `SUBIR_COM_PRIORIDADE`
- `BAIXAR_COM_JUSTIFICATIVA`
- `COMPARAR_CONCORRENCIA`
- `PROTEGER`
- `NAO_MEXER_RESERVADO`
- `AGUARDAR_DADOS`

## 10. Próxima fase depois do inventário

Antes de criar qualquer automação:

- importar histórico de reservas;
- calcular diária média real;
- separar Pousada x Casa;
- separar canais;
- calcular comissões;
- estimar custo variável por reserva;
- calcular preço mínimo;
- cruzar com calendário e concorrência.

## 11. Importante

Não alterar reservas já confirmadas. Quando um período aparece reservado no inventário (ex.: Réveillon 2026 e janeiro 2027 da Casa Arágua), o diagnóstico deve virar aprendizado para futuras datas, nunca alteração retroativa.

## 12. Sub-módulo: Radar de Concorrência Revenue (adicionado 2026-07-25)

**Status:** `EM_IMPLANTACAO_MANUAL_ASSISTIDA`. Objetivo: substituir gradualmente a necessidade de ferramenta externa (tipo BeBook) por coleta assistida/manual, links diretos e análise estruturada dentro do próprio cérebro Villa Arágua IA — sem scraping automático e sem alteração automática de preço.

Arquivos: `CESTA_COMPETITIVA_REVENUE_VILLA_ARAGUA.md`, `COLETAS_CONCORRENCIA_REVENUE.csv`, `REGRAS_CONVERSAO_OTA_MOTOR_REVENUE.md`, `ALERTAS_CONCORRENCIA_REVENUE.md`. Não criou agente nem skill novos — conectado ao mesmo `villa-precificacao-calendario` e à mesma `villa-aragua-pricing-revenue` desta seção 8.

Regra central do sub-módulo: preço de concorrente em OTA é preço visível de mercado, nunca equivalente direto ao motor da Villa (Stays) — toda recomendação de concorrência precisa vir em duas leituras (comparação de mercado + valor de motor recomendado), usando as fórmulas de `REGRAS_CONVERSAO_OTA_MOTOR_REVENUE.md`.
