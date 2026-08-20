# TEMPLATES OPERACIONAIS QL/C — VILLA ARÁGUA

**Subtítulo:** Guia único de atendimento manual, primeiros 15 minutos e follow-up.
**Status:** Versão 1.0 — Piloto manual assistido.
**Data:** 05/08/2026.
**Modo:** Rascunho Assistido — nenhum envio automático.

**Natureza deste arquivo:** camada de execução tática do Sistema Comercial da Villa Arágua. Não redefine nenhum conceito — organiza, em um único documento, o que já está aprovado em `ARQUITETURA_DO_SISTEMA_COMERCIAL_VILLA_ARAGUA.md` (C1–C4), `FUNIL_QUALIFICACAO_LEADS_WHATSAPP_QL_VILLA_ARAGUA.md` (QL1–QL4/NQ e lógica de qualificação), `CRM_LEADS_VILLA_ARAGUA.md` (Estágio e 20 campos), `GUIA_ATIVOS_COMERCIAIS_WHATSAPP_VILLA_ARAGUA.md` (ativos), `MATRIZ_FOLLOWUP_QL_WHATSAPP_VILLA_ARAGUA.md` (cadência) e `BIBLIOTECA_COMERCIAL_RECEPCIONISTA_IA_VILLA_ARAGUA.md` (conteúdo-base). Nenhuma dessas fontes foi alterada para a criação deste documento.

**Fontes lidas integralmente antes desta criação:** as 7 fontes acima, na versão vigente em 05/08/2026, mais a proposta consolidada dos 35 Templates Operacionais, a Matriz de Uso Rápido e os 24 testes simulados já produzidos e aprovados nesta mesma rodada de trabalho.

---

## 1. Manifesto rápido de uso

*Uma página. Ler antes de qualquer atendimento.*

- A IA lê, classifica e sugere.
- Rene/Nubia revisam e enviam casos simples.
- Renildo decide C3, C4, exceções e casos sensíveis.
- Nenhuma mensagem é enviada automaticamente.
- Nenhuma disponibilidade é confirmada pela IA.
- Nenhuma reserva é confirmada pela IA.
- Nenhum pagamento é validado pela IA.
- Nenhum desconto, crédito ou compensação é prometido.
- Nenhuma chave, senha, endereço completo ou acesso é liberado pela IA.
- Nunca repetir dado que o lead já informou.
- Fazer apenas a próxima pergunta realmente necessária.
- Foto só entra quando ajuda a conversa.
- Registrar sempre a Próxima ação no CRM.

> **"A tecnologia organiza. A equipe decide. A hospitalidade permanece humana."**

---

## 2. Fluxo resumido

```text
Mensagem recebida
↓
Ler o que já foi informado
↓
Identificar Produto
↓
Classificar QL
↓
Classificar C
↓
Confirmar Estágio
↓
Escolher Template
↓
Definir se precisa de foto
↓
Revisar e enviar manualmente
↓
Atualizar CRM
↓
Registrar Próxima ação
↓
Aplicar Follow-up somente pela Matriz oficial
```

**Regra central:** não seguir um roteiro fixo. Perguntar apenas o próximo dado realmente necessário.

---

## 3. Uso rápido — "O hóspede disse..."

*30 casos mais comuns. Formato: Situação → Template → QL → C → Estágio → Mensagem → Imagem → Registro mínimo → Próxima ação → Follow-up → Renildo?. Nenhuma mensagem aqui é diferente da ficha oficial correspondente (seção 4) — esta tabela é atalho de consulta, não fonte nova.*

| Situação | Template | QL | C | Estágio | Mensagem | Imagem | Registro mínimo | Próxima ação | Follow-up | Renildo? |
|---|---|---|---|---|---|---|---|---|---|---|
| "Oi" | T-QL1-ACOLHER-01 | QL1 | C2 | Novo | "Que bom receber seu contato 😊 Quais datas vocês estão pensando?" | Nenhuma | QL, Estágio, Canal | Aguardar Datas | QL1, opcional | Não |
| Meta Ads Pousada, campanha sem período† | T-QL1-ORIGEM-POUSADA-01 | QL1 | C2 | Novo | "Que bom receber seu contato 😊 Vi que você chegou até a Pousada Arágua. Quais datas vocês estão pensando?" | Nenhuma | Produto=Pousada, Campanha | Aguardar Datas | QL1, opcional | Não |
| Meta Ads Pousada, campanha COM período† | T-QL1-ORIGEM-POUSADA-01 (variação, campo 12) | QL3 | C2 | Novo | "Olá! 😊 Claro! Vi que você veio pela nossa campanha do feriado de 7 de Setembro, de 04 a 08/09. Me conta só quantas pessoas estarão na viagem e se haverá alguma criança?" | Nenhuma | Produto=Pousada, Datas, Campanha | Aguardar Pessoas/Criança | QL3, 24-48h/3 dias (Matriz seção 5) | Não |
| Meta Ads Casa, campanha sem período† | T-QL1-ORIGEM-CASA-01 | QL1 | C2 | Novo | "Que bom receber seu contato 😊 Vi que você chegou até a Casa Arágua Mariscal. Quais datas vocês estão pensando?" | Nenhuma | Produto=Casa, Campanha | Aguardar Datas | QL1, opcional | Não |
| Meta Ads Casa, campanha COM período† | T-QL1-ORIGEM-CASA-01 (variação, campo 12) | QL3 | C2 | Novo | "Olá! 😊 Claro! Vi que você veio pela nossa campanha do feriado de 7 de Setembro, de 04 a 08/09. Me conta só quantas pessoas estarão na viagem e se haverá alguma criança?" | Nenhuma | Produto=Casa, Datas, Campanha | Aguardar Pessoas/Criança | QL3, 24-48h/3 dias (Matriz seção 5) | Não |
| Origem sem produto | T-QL1-ORIGEM-INDEFINIDO-01 | QL1 | C2 | Novo | "Que bom receber seu contato 😊 Quais datas vocês estão pensando?" | Nenhuma | Canal de origem | Aguardar Datas | QL1, opcional | Não |
| "Qual o valor?" | T-QL2-PRECO-01 | QL2 | C2 | Em qualificação | "O valor depende do período, do número de pessoas e da opção de hospedagem 😊 Quais datas vocês estão pensando?" | Nenhuma | QL, C | Aguardar Datas | 3 dias/7 dias | Não |
| Informou Datas | T-QL2-PESSOAS-01 | QL2 | C2 | Em qualificação | "E quantas pessoas estarão na viagem?" | Nenhuma | Datas | Aguardar Pessoas | 3 dias/7 dias | Não |
| Informou Pessoas | T-QL2-PESSOAS-01 (variação) | QL2 | C2 | Em qualificação | "Quais datas vocês estão pensando?" | Nenhuma | Número de pessoas | Aguardar Datas | 3 dias/7 dias | Não |
| Datas+Pessoas, Produto indefinido | T-QL2-PRODUTO-01 | QL3 | C2 | Em qualificação | "Vocês estão considerando a Pousada Arágua ou a Casa Arágua Mariscal?" | Nenhuma | Datas, Pessoas | Aguardar Produto (obrigatória) | 24-48h/3 dias | Não |
| Pousada identificada | T-QL2-POUSADA-01 | QL2 | C2 | Em qualificação | "A Pousada Arágua tem suítes individuais, com café da manhã servido na acomodação." + dado faltante | Depende da dúvida | Produto=Pousada | Aguardar dado faltante | Matriz 10.1 | Não |
| Casa identificada | T-QL2-CASA-01 | QL2 | C2 | Em qualificação | "A Casa Arágua Mariscal é completa e privativa, com piscina para o grupo." + dado faltante | Depende da dúvida | Produto=Casa | Aguardar dado faltante | Matriz 10.2 | Não |
| Pediu fotos (sem produto) | T-QL1-FOTO-01 | QL1 | C2 | Novo | "Consigo mostrar sim 😊 Quais datas vocês estão pensando?" | Nenhuma | Observações curtas | Aguardar Datas | QL1, opcional | Não |
| Estrutura ("o que está incluso?") | T-QL2-ESTRUTURA-01 | QL2 | C1 | Em qualificação | "Na Pousada Arágua, o café da manhã é servido na própria suíte... Na Casa Arágua, a piscina e a churrasqueira são privativas." | Nenhuma | — | Nenhuma obrigatória | Não aplicável | Não |
| Criança | T-QL2-CRIANCA-01 | QL2 | C2 | Em qualificação | "Vai ter criança na viagem? Se sim, qual a idade — isso ajuda a indicar a opção mais adequada." | AT-POU-FAMILIA-01 (após confirmação) | Observações curtas | Aguardar idade | Matriz QL2/QL3 | Não |
| Pet | T-QL2-PET-01 | QL2 | C2 | Em qualificação | "Vocês vêm com pet? Se sim, qual o porte e quantos pets — a equipe confirma se a acomodação atende." | Nenhuma | Observações curtas | Aguardar detalhe | Matriz QL2 | Só se fora do padrão |
| Dúvida específica (QL3) | T-QL3-DUVIDA-01 | QL3 | C1* | Em qualificação | Roteador — template C1 do tema perguntado | Depende da dúvida | Observações curtas | Retomar dado faltante | Segue cadência QL3 | Não |
| Primeiro ativo (QL3) | T-QL3-ATIVO-01 | QL3 | C2 | Em qualificação | "Essa é a piscina da Pousada Arágua 😊 ... Vocês já têm as datas e quantas pessoas seriam?" (ou variação Casa) | AT-POU-PISCINA-01 / AT-CAS-PISCINA-01 | Observações curtas | Observar reação | Matriz QL3 | Não |
| Dados completos | T-QL4-DADOS-01 | QL4 | C2 | Orçamento | "Vou deixar as informações organizadas para a equipe avaliar." | Nenhuma | Orçamento enviado?=Não | SLA interno da equipe | — | Não |
| Pediu orçamento (dados completos) | T-QL4-DADOS-01 | QL4 | C2 | Orçamento | "Vou deixar as informações organizadas para a equipe avaliar." | Nenhuma | Orçamento enviado?=Não | SLA interno da equipe | — | Não |
| Orçamento enviado | T-QL4-ORCAMENTO-01 | QL4 | C2 | Orçamento | "Que bom que chegou! Fico à disposição para qualquer dúvida 😊" | Nenhuma | Orçamento enviado?=Sim | Aguardar reação | 24h | Não |
| Dúvida pós-orçamento | T-QL4-DUVIDA-01 | QL4 | C2* | Orçamento | Roteador — depende do tema (estrutura, valor, composição) | Depende da dúvida | Observações curtas | Aguardar decisão | Matriz seção 4 | Depende |
| Silêncio pós-orçamento | T-QL4-FOLLOWUP-01 / T-QL4-ENCERRAR-01 | QL4 (mantém) | C2 | Aguardando retorno | "Oi! Passando só pra saber se o orçamento chegou certinho pra você 😊" | Nenhuma | Próximo follow-up | Aguardar resposta | Matriz seção 4 | Não |
| Pedido de reserva | T-QL4-RESERVA-01 | QL4 | C2 | Negociação/validação | "A conversa segue por aqui, mas a reserva só fica confirmada depois do pagamento ou sinal validado pela equipe." | Nenhuma | Estágio=Negociação/validação | Aguardar validação humana | Matriz seção 4 | Depende do valor |
| Desconto | T-C3-DESCONTO-01 | Independente | C3 | Negociação/validação* | "Entendo o pedido. O pedido será encaminhado para avaliação de Renildo." | Nenhuma | C=C3 | Renildo decide | Não aplicável | Sim |
| Condição especial | T-C3-CONDICAO-01 | Independente | C3 | Negociação/validação* | "Entendo a situação. O pedido será encaminhado para avaliação de Renildo." | Nenhuma | C=C3 | Renildo decide | Não aplicável | Sim |
| Exceção | T-C3-EXCECAO-01 | Independente | C3 | Mantém atual | "Entendo o pedido de exceção. O pedido será encaminhado para avaliação de Renildo." | Nenhuma | C=C3 | Renildo decide | Não aplicável | Sim |
| Reclamação (grave) | T-C4-CONTENCAO-01 | Independente | C4 | Mantém último conhecido | "Entendo a situação. O pedido será encaminhado para avaliação de Renildo." | Nenhuma | Contenção C4 | Escalar imediato | Não aplicável | Sim |
| Ameaça | T-C4-AMEACA-01 | Independente | C4 | Mantém último conhecido | "Entendo que vocês estejam frustrados... Quero entender o que aconteceu para encaminhar da forma correta." | Nenhuma | Contenção C4 | Escalar imediato | Não aplicável | Sim |
| NQ | T-NQ-PERFIL-01 | NQ | C1 | Novo/Em qualificação | "A Villa Arágua não trabalha com festas ou eventos..." (ou variação do tema) | Nenhuma | Status final="Fora do perfil" | Nenhuma | Não aplicável | Não |
| Redirecionamento | T-NQ-REDIRECIONAR-01 | NQ→QL2 | C1 | Em qualificação/Nutrição | "Pelo que você descreveu, a [outro produto] pode combinar melhor... Posso contar um pouco mais sobre ela?" | Nenhuma | Observações curtas | Aguardar aceite | Não formalizado | Não |
| Encerramento | T-NQ-ENCERRAR-01 | NQ | C1 | Fecha ciclo | "Ficamos à disposição se algo mudar. Um abraço!" | Nenhuma | Motivo de perda | Nenhuma | Nenhum | Não |

*Templates com `*` têm regra de ramificação de C — ver ficha completa (seção 4).*

*†Regra oficial de primeira mensagem de campanha (06/08/2026): antes de escolher a mensagem, verificar se a campanha já define Período além do Produto — nunca perguntar Produto, Período ou qualquer outro dado que a origem/campanha já informa. Ver ficha completa (seção 4) para os dois casos.*

---

## 4. Os 35 Templates Operacionais QL/C

*Estrutura de 30 campos por template, conforme aprovado. Campos padrão salvo indicação contrária: Responsável = Rene/Nubia (C3/C4 = Renildo decide); Fontes oficiais = Funil (QL/lógica) + Arquitetura (C) + CRM (campos) + Matriz (follow-up) + Guia (ativo) + Biblioteca (texto-base); Status = Versão 1.0 — Piloto manual assistido; Data de revisão = 05/08/2026.*

### QL1 — Entrada e descoberta

#### T-QL1-ACOLHER-01

| Campo | Valor |
|---|---|
| 1. Código | T-QL1-ACOLHER-01 |
| 2. Situação | Abertura sem contexto ("Oi") |
| 3. Produto | Indefinido |
| 4. Origem | Qualquer |
| 5. QL | QL1 |
| 6. C | C2 — pedido de datas é qualificação (Arquitetura, seção 5, exemplo "pedido normal de datas e pessoas") |
| 7. Estágio | Novo |
| 8. Objetivo | Iniciar coleta do primeiro dado essencial |
| 9. Emoção desejada | Acolhimento |
| 10. Resultado esperado | Obter Datas |
| 11. Mensagem principal | "Que bom receber seu contato 😊 Quais datas vocês estão pensando?" |
| 12. Variação curta | Nenhuma |
| 13. Ativo recomendado | Nenhum |
| 14. Ativo proibido | Qualquer |
| 15. CTA | Datas |
| 16. Momento de envio | Imediato |
| 17. Quando usar | Abertura sem nenhum dado |
| 18. Quando não usar | Lead já deu algum dado (pular para o template do dado seguinte) |
| 19. Se responder | T-QL2-PESSOAS-01 |
| 20. Se não responder | T-QL1-SILENCIO-01 |
| 21. Próximo template | T-QL2-PESSOAS-01 |
| 22. Próxima ação | Aguardar Datas |
| 23. Follow-up | QL1, opcional, sem prazo fixo (Matriz seção 7) |
| 24. Registro mínimo no CRM | QL, Estágio=Novo, Canal de origem |
| 25. Responsável | Rene/Nubia |
| 26. Precisa de Renildo? | Não |
| 27. Riscos | Nenhum |
| 28. Fontes oficiais | Funil (seção 5) + Arquitetura (seção 5) |
| 29. Status | Versão 1.0 — Piloto manual assistido |
| 30. Data de revisão | 05/08/2026 |

#### T-QL1-ORIGEM-POUSADA-01

| Campo | Valor |
|---|---|
| 1. Código | T-QL1-ORIGEM-POUSADA-01 |
| 2. Situação | Lead via Meta Ads Pousada — cobre dois casos: (a) campanha define só o Produto; (b) campanha também define Período/datas (ex.: campanha de feriado) |
| 3. Produto | Pousada Arágua (pela campanha) |
| 4. Origem | Meta Ads — registrar campanha exata e, quando houver, o período do anúncio |
| 5. QL | Caso (a) — só Produto: QL1. Caso (b) — Produto+Período (2 de 3 dados essenciais): **QL3**, conforme `FUNIL_QUALIFICACAO_LEADS_WHATSAPP_QL_VILLA_ARAGUA.md` seção 4 (fonte oficial de QL) |
| 6. C | C2 |
| 7. Estágio | Novo |
| 8. Objetivo | Reconhecer o que a campanha já informa (Produto e, se houver, Período) sem repetir; iniciar coleta apenas do próximo dado realmente faltante |
| 9. Emoção desejada | Continuidade do desejo do anúncio |
| 10. Resultado esperado | Caso (a) — obter Datas. Caso (b) — obter Número de pessoas (e Criança, se pertinente) |
| 11. Mensagem principal | Caso (a), campanha só com Produto: "Que bom receber seu contato 😊 Vi que você chegou até a Pousada Arágua. Quais datas vocês estão pensando?" |
| 12. Variação curta | **Caso (b), campanha também com Período (regra oficial, 06/08/2026 — nunca perguntar dado que a campanha já informa):** "Olá! 😊 Claro! Vi que você veio pela nossa campanha do feriado de 7 de Setembro, de 04 a 08/09. Me conta só quantas pessoas estarão na viagem e se haverá alguma criança?" — adaptar nome do feriado/período ao anúncio real; nunca perguntar Produto nem Período já conhecidos pela campanha. |
| 13. Ativo recomendado | Nenhum (1º contato normalmente sem foto) |
| 14. Ativo proibido | Ativo da Casa |
| 15. CTA | Caso (a): Datas. Caso (b): Número de pessoas + criança |
| 16. Momento de envio | Imediato |
| 17. Quando usar | Origem = campanha Pousada. Verificar sempre, antes de escolher a mensagem: a campanha também define Período? Se sim, usar a Variação curta (campo 12) |
| 18. Quando não usar | Origem orgânica (usar T-QL1-ORIGEM-INDEFINIDO-01); lead já informou dado adicional na própria mensagem de abertura (nesse caso, pular direto para o template do próximo dado faltante, sem repetir nem Produto nem Período nem o que o lead já escreveu) |
| 19. Se responder | Caso (a): T-QL2-PESSOAS-01. Caso (b): T-QL2-CRIANCA-01, ou direto a T-QL3-DADO-01/T-QL4-DADOS-01 se Pessoas e Criança já vierem juntos na resposta |
| 20. Se não responder | Caso (a): T-QL1-SILENCIO-01. Caso (b): não usar T-QL1-SILENCIO-01 — seguir follow-up QL3 (Matriz seção 5, 24-48h/3 dias) |
| 21. Próximo template | Caso (a): T-QL2-PESSOAS-01. Caso (b): T-QL2-CRIANCA-01 |
| 22. Próxima ação | Caso (a): Aguardar Datas. Caso (b): Aguardar Número de pessoas/Criança |
| 23. Follow-up | Caso (a): QL1 (Matriz seção 7). Caso (b): QL3 (Matriz seção 5) |
| 24. Registro mínimo no CRM | QL, Produto=Pousada Arágua, Datas (se a campanha já define Período), Campanha/anúncio, Canal de origem="Meta Ads" |
| 25. Responsável | Rene/Nubia |
| 26. Precisa de Renildo? | Não |
| 27. Riscos | Confirmar que a campanha realmente corresponde a Pousada antes de assumir o produto; confirmar o período exato do anúncio antes de assumi-lo como Datas — nunca presumir período de campanha diferente da que gerou o lead |
| 28. Fontes oficiais | Funil (seção 5) + Arquitetura (seção 5) |
| 29. Status | Versão 1.0 — Piloto manual assistido |
| 30. Data de revisão | 06/08/2026 — campo 12 (Variação curta) adicionado: regra de primeira mensagem de campanha reconhecendo Produto + Período já conhecidos, consolidando o aprendizado do piloto de 06/08/2026. **08/08/2026 — correção crítica pós-auditoria (decisão de Renildo):** campos 5, 20 e 23 corrigidos para diferenciar caso (a)=QL1 de caso (b)=QL3 — o Funil (fonte oficial de QL) já classifica campanha com Produto+Período conhecidos e só Pessoas faltando como QL3 (2 de 3 dados essenciais); este template estava desalinhado. Coluna QL/Follow-up da tabela-resumo (seção 4) também corrigida na mesma rodada |

#### T-QL1-ORIGEM-CASA-01

| Campo | Valor |
|---|---|
| 1. Código | T-QL1-ORIGEM-CASA-01 |
| 2. Situação | Lead via Meta Ads Casa — cobre dois casos: (a) campanha define só o Produto; (b) campanha também define Período/datas (ex.: campanha de feriado) |
| 3. Produto | Casa Arágua Mariscal (pela campanha) |
| 4. Origem | Meta Ads — registrar campanha exata e, quando houver, o período do anúncio |
| 5. QL | Caso (a) — só Produto: QL1. Caso (b) — Produto+Período (2 de 3 dados essenciais): **QL3**, conforme `FUNIL_QUALIFICACAO_LEADS_WHATSAPP_QL_VILLA_ARAGUA.md` seção 4 (fonte oficial de QL) |
| 6. C | C2 |
| 7. Estágio | Novo |
| 8. Objetivo | Reconhecer o que a campanha já informa (Produto e, se houver, Período) sem repetir; iniciar coleta apenas do próximo dado realmente faltante |
| 9. Emoção desejada | Continuidade do desejo do anúncio |
| 10. Resultado esperado | Caso (a) — obter Datas. Caso (b) — obter Número de pessoas (e Criança, se pertinente) |
| 11. Mensagem principal | Caso (a), campanha só com Produto: "Que bom receber seu contato 😊 Vi que você chegou até a Casa Arágua Mariscal. Quais datas vocês estão pensando?" |
| 12. Variação curta | **Caso (b), campanha também com Período (regra oficial, 06/08/2026 — nunca perguntar dado que a campanha já informa):** "Olá! 😊 Claro! Vi que você veio pela nossa campanha do feriado de 7 de Setembro, de 04 a 08/09. Me conta só quantas pessoas estarão na viagem e se haverá alguma criança?" — adaptar nome do feriado/período ao anúncio real; nunca perguntar Produto nem Período já conhecidos pela campanha. |
| 13. Ativo recomendado | Nenhum |
| 14. Ativo proibido | Ativo da Pousada |
| 15. CTA | Caso (a): Datas. Caso (b): Número de pessoas + criança |
| 16. Momento de envio | Imediato |
| 17. Quando usar | Origem = campanha Casa. Verificar sempre, antes de escolher a mensagem: a campanha também define Período? Se sim, usar a Variação curta (campo 12) |
| 18. Quando não usar | Origem orgânica; lead já informou dado adicional na própria mensagem de abertura (nesse caso, pular direto para o template do próximo dado faltante, sem repetir nem Produto nem Período nem o que o lead já escreveu) |
| 19. Se responder | Caso (a): T-QL2-PESSOAS-01. Caso (b): T-QL2-CRIANCA-01, ou direto a T-QL3-DADO-01/T-QL4-DADOS-01 se Pessoas e Criança já vierem juntos na resposta |
| 20. Se não responder | Caso (a): T-QL1-SILENCIO-01. Caso (b): não usar T-QL1-SILENCIO-01 — seguir follow-up QL3 (Matriz seção 5, 24-48h/3 dias) |
| 21. Próximo template | Caso (a): T-QL2-PESSOAS-01. Caso (b): T-QL2-CRIANCA-01 |
| 22. Próxima ação | Caso (a): Aguardar Datas. Caso (b): Aguardar Número de pessoas/Criança |
| 23. Follow-up | Caso (a): QL1 (Matriz seção 7). Caso (b): QL3 (Matriz seção 5) |
| 24. Registro mínimo no CRM | QL, Produto=Casa Arágua, Datas (se a campanha já define Período), Campanha/anúncio, Canal de origem="Meta Ads" |
| 25. Responsável | Rene/Nubia |
| 26. Precisa de Renildo? | Não |
| 27. Riscos | Mesma checagem de campanha do template anterior; confirmar o período exato do anúncio antes de assumi-lo como Datas — nunca presumir período de campanha diferente da que gerou o lead |
| 28. Fontes oficiais | Funil (seção 5) + Arquitetura (seção 5) |
| 29. Status | Versão 1.0 — Piloto manual assistido |
| 30. Data de revisão | 06/08/2026 — campo 12 (Variação curta) adicionado: regra de primeira mensagem de campanha reconhecendo Produto + Período já conhecidos, consolidando o aprendizado do piloto de 06/08/2026. **08/08/2026 — correção crítica pós-auditoria (decisão de Renildo):** campos 5, 20 e 23 corrigidos para diferenciar caso (a)=QL1 de caso (b)=QL3 — o Funil (fonte oficial de QL) já classifica campanha com Produto+Período conhecidos e só Pessoas faltando como QL3 (2 de 3 dados essenciais); este template estava desalinhado. Coluna QL/Follow-up da tabela-resumo (seção 4) também corrigida na mesma rodada |

#### T-QL1-ORIGEM-INDEFINIDO-01

| Campo | Valor |
|---|---|
| 1. Código | T-QL1-ORIGEM-INDEFINIDO-01 |
| 2. Situação | Origem orgânica/indicação, sem produto sinalizado |
| 3. Produto | Indefinido |
| 4. Origem | Orgânico/Indicação/Instagram |
| 5. QL | QL1 |
| 6. C | C2 |
| 7. Estágio | Novo |
| 8. Objetivo | Iniciar coleta sem presumir produto |
| 9. Emoção desejada | Acolhimento |
| 10. Resultado esperado | Obter Datas |
| 11. Mensagem principal | "Que bom receber seu contato 😊 Quais datas vocês estão pensando?" |
| 12. Variação curta | Nenhuma |
| 13. Ativo recomendado | Nenhum |
| 14. Ativo proibido | Qualquer (produto ainda não identificado) |
| 15. CTA | Datas |
| 16. Momento de envio | Imediato |
| 17. Quando usar | Origem sem produto sinalizado |
| 18. Quando não usar | Campanha já identifica produto |
| 19. Se responder | T-QL2-PESSOAS-01 |
| 20. Se não responder | T-QL1-SILENCIO-01 |
| 21. Próximo template | T-QL2-PESSOAS-01 |
| 22. Próxima ação | Aguardar Datas |
| 23. Follow-up | QL1 (Matriz seção 7) |
| 24. Registro mínimo no CRM | QL, Canal de origem, Estágio=Novo |
| 25. Responsável | Rene/Nubia |
| 26. Precisa de Renildo? | Não |
| 27. Riscos | Nenhum |
| 28. Fontes oficiais | Funil (seção 5) |
| 29. Status | Versão 1.0 — Piloto manual assistido |
| 30. Data de revisão | 05/08/2026 |

#### T-QL1-FOTO-01

| Campo | Valor |
|---|---|
| 1. Código | T-QL1-FOTO-01 |
| 2. Situação | Pedido de fotos sem produto definido |
| 3. Produto | Indefinido |
| 4. Origem | Qualquer |
| 5. QL | QL1 |
| 6. C | C2 |
| 7. Estágio | Novo |
| 8. Objetivo | Acolher o pedido sem enviar nada ainda, iniciar coleta |
| 9. Emoção desejada | Disponibilidade em ajudar |
| 10. Resultado esperado | Obter Datas |
| 11. Mensagem principal | "Consigo mostrar sim 😊 Quais datas vocês estão pensando?" |
| 12. Variação curta | Nenhuma |
| 13. Ativo recomendado | Nenhum neste template |
| 14. Ativo proibido | Qualquer, antes de Produto identificado |
| 15. CTA | Datas |
| 16. Momento de envio | Imediato |
| 17. Quando usar | Pedido de foto no 1º contato |
| 18. Quando não usar | Produto já identificado (usar T-QL3-ATIVO-01) |
| 19. Se responder | T-QL2-PESSOAS-01 |
| 20. Se não responder | T-QL1-SILENCIO-01 |
| 21. Próximo template | T-QL2-PESSOAS-01 |
| 22. Próxima ação | Aguardar Datas |
| 23. Follow-up | QL1 (Matriz seção 7) |
| 24. Registro mínimo no CRM | QL, Estágio=Novo, Observações curtas="pediu fotos, produto ainda não definido" |
| 25. Responsável | Rene/Nubia |
| 26. Precisa de Renildo? | Não |
| 27. Riscos | Nunca enviar foto antes de Produto identificado |
| 28. Fontes oficiais | Funil (seção 5) + Guia (seção 2) |
| 29. Status | Versão 1.0 — Piloto manual assistido |
| 30. Data de revisão | 05/08/2026 |

#### T-QL1-SILENCIO-01

| Campo | Valor |
|---|---|
| 1. Código | T-QL1-SILENCIO-01 |
| 2. Situação | Lead não respondeu à primeira mensagem |
| 3. Produto | Indefinido |
| 4. Origem | Qualquer |
| 5. QL | QL1 (mantém — silêncio não reduz QL) |
| 6. C | C1 (mensagem leve, sem pedido de dado) |
| 7. Estágio | Aguardando retorno |
| 8. Objetivo | Reengajar sem pressão |
| 9. Emoção desejada | Leveza |
| 10. Resultado esperado | Reabrir ou aceitar silêncio |
| 11. Mensagem principal | "Oi! Se um dia quiser conhecer mais sobre a Villa Arágua, estamos por aqui 🌿" |
| 12. Variação curta | Nenhuma |
| 13. Ativo recomendado | Nenhum |
| 14. Ativo proibido | Qualquer |
| 15. CTA | Nenhum |
| 16. Momento de envio | 7 dias, opcional, sem prazo fixo |
| 17. Quando usar | Zero resposta após abertura QL1 |
| 18. Quando não usar | Lead respondeu algo |
| 19. Se responder | Reclassificar QL pela resposta |
| 20. Se não responder | Não repetir novo follow-up |
| 21. Próximo template | Nenhum |
| 22. Próxima ação | Nenhuma |
| 23. Follow-up | Único, opcional (Matriz seção 7) |
| 24. Registro mínimo no CRM | Estágio=Aguardando retorno, Último contato |
| 25. Responsável | Rene/Nubia |
| 26. Precisa de Renildo? | Não |
| 27. Riscos | Nenhum |
| 28. Fontes oficiais | Funil (seção 9) + Matriz (seção 7) |
| 29. Status | Versão 1.0 — Piloto manual assistido |
| 30. Data de revisão | 05/08/2026 |

### QL2 — Pesquisa ativa e qualificação

#### T-QL2-PRECO-01

| Campo | Valor |
|---|---|
| 1. Código | T-QL2-PRECO-01 |
| 2. Situação | Pergunta direta de preço |
| 3. Produto | Pode estar indefinido |
| 4. Origem | Qualquer |
| 5. QL | QL2 |
| 6. C | C2 (Arquitetura, exemplo literal "Qual o valor?") |
| 7. Estágio | Em qualificação |
| 8. Objetivo | Responder com transparência sem valor, coletar 1 dado por vez |
| 9. Emoção desejada | Confiança, sem sensação de resposta evasiva |
| 10. Resultado esperado | Datas → Pessoas → Produto, um por vez |
| 11. Mensagem principal | "O valor depende do período, do número de pessoas e da opção de hospedagem 😊 Quais datas vocês estão pensando?" |
| 12. Variação curta | Depois: "E quantas pessoas estarão na viagem?" · Depois, se Produto ainda indefinido: "Vocês estão considerando a Pousada ou a Casa?" — nunca pedir os 3 dados na mesma mensagem |
| 13. Ativo recomendado | Nenhum |
| 14. Ativo proibido | Qualquer, antes dos 3 dados |
| 15. CTA | Um dado por vez, na ordem Datas→Pessoas→Produto |
| 16. Momento de envio | Imediato |
| 17. Quando usar | Pergunta de preço sem nenhum dado, ou com dado parcial |
| 18. Quando não usar | Dados já completos (usar T-QL4-DADOS-01) |
| 19. Se responder | Avança para o próximo dado faltante |
| 20. Se não responder | T-QL1-SILENCIO-01 (adaptado ao ponto da coleta) |
| 21. Próximo template | T-QL2-PESSOAS-01 ou T-QL2-PRODUTO-01, conforme o que falta |
| 22. Próxima ação | Aguardar próximo dado |
| 23. Follow-up | QL2 (Matriz seção 6: 3 dias/7 dias) |
| 24. Registro mínimo no CRM | QL=QL2, C=C2, Estágio=Em qualificação, Datas/Pessoas conforme recebido |
| 25. Responsável | Rene/Nubia |
| 26. Precisa de Renildo? | Não |
| 27. Riscos | Nunca citar valor, faixa ou "a partir de" (Biblioteca, regra-mãe 1) |
| 28. Fontes oficiais | Funil (seção 6, item Linguagem) + Arquitetura (seção 5) |
| 29. Status | Versão 1.0 — Piloto manual assistido |
| 30. Data de revisão | 05/08/2026 |

#### T-QL2-PESSOAS-01

| Campo | Valor |
|---|---|
| 1. Código | T-QL2-PESSOAS-01 |
| 2. Situação | Datas informadas, falta Pessoas (ou o inverso) |
| 3. Produto | Pode estar indefinido |
| 4. Origem | Qualquer |
| 5. QL | QL2 |
| 6. C | C2 |
| 7. Estágio | Em qualificação |
| 8. Objetivo | Completar o par Datas+Pessoas |
| 9. Emoção desejada | Progresso |
| 10. Resultado esperado | Obter o dado que falta |
| 11. Mensagem principal | "E quantas pessoas estarão na viagem?" |
| 12. Variação curta | (inverso — pessoas já informadas): "Quais datas vocês estão pensando?" |
| 13. Ativo recomendado | Nenhum |
| 14. Ativo proibido | Qualquer (Produto ainda não confirmado) |
| 15. CTA | Dado faltante |
| 16. Momento de envio | Imediato após o primeiro dado |
| 17. Quando usar | Um dos dois (Datas/Pessoas) já veio |
| 18. Quando não usar | Ambos já informados (usar T-QL2-PRODUTO-01) |
| 19. Se responder | T-QL2-PRODUTO-01 |
| 20. Se não responder | Follow-up QL2 |
| 21. Próximo template | T-QL2-PRODUTO-01 |
| 22. Próxima ação | Aguardar dado faltante |
| 23. Follow-up | QL2 (Matriz seção 6) |
| 24. Registro mínimo no CRM | Datas e/ou Número de pessoas, QL=QL2, Estágio=Em qualificação |
| 25. Responsável | Rene/Nubia |
| 26. Precisa de Renildo? | Não |
| 27. Riscos | Nunca repetir o dado já informado (Funil, seção 5) |
| 28. Fontes oficiais | Funil (seção 5) |
| 29. Status | Versão 1.0 — Piloto manual assistido |
| 30. Data de revisão | 05/08/2026 |

#### T-QL2-PRODUTO-01

| Campo | Valor |
|---|---|
| 1. Código | T-QL2-PRODUTO-01 |
| 2. Situação | Datas+Pessoas completos, falta Produto |
| 3. Produto | A definir |
| 4. Origem | Qualquer |
| 5. QL | QL2 (vira QL3 se restar dúvida, ou QL4 se já pedir orçamento) |
| 6. C | C2 (Arquitetura, exemplo literal "comparação Pousada x Casa") |
| 7. Estágio | Em qualificação |
| 8. Objetivo | Identificar Produto |
| 9. Emoção desejada | Clareza, sem empurrar um produto sobre o outro |
| 10. Resultado esperado | Produto identificado |
| 11. Mensagem principal | "Vocês estão considerando a Pousada Arágua ou a Casa Arágua Mariscal?" |
| 12. Variação curta | (lead indeciso): "A Pousada tem suítes e uma proposta mais acolhedora, com café da manhã servido na acomodação. A Casa é completa e privativa, com piscina para o grupo. Qual dessas opções combina mais com a viagem de vocês?" |
| 13. Ativo recomendado | Nenhum ainda |
| 14. Ativo proibido | Qualquer, antes da definição |
| 15. CTA | Escolha de produto |
| 16. Momento de envio | Após Datas+Pessoas confirmados |
| 17. Quando usar | Produto ainda não mencionado |
| 18. Quando não usar | Lead já citou Pousada ou Casa (pular para o template do produto correspondente) |
| 19. Se responder | T-QL2-POUSADA-01 ou T-QL2-CASA-01 |
| 20. Se não responder | Follow-up QL2/QL3 |
| 21. Próximo template | T-QL2-POUSADA-01/CASA-01 |
| 22. Próxima ação | Aguardar escolha |
| 23. Follow-up | QL2/QL3 conforme o caso (Matriz) |
| 24. Registro mínimo no CRM | Datas, Número de pessoas, QL, Estágio=Em qualificação |
| 25. Responsável | Rene/Nubia |
| 26. Precisa de Renildo? | Não |
| 27. Riscos | Nunca apresentar um produto como "melhor" que o outro |
| 28. Fontes oficiais | Funil (seção 5, item 3) + Biblioteca (PC-C1-01) |
| 29. Status | Versão 1.0 — Piloto manual assistido |
| 30. Data de revisão | 05/08/2026 |

#### T-QL2-POUSADA-01

| Campo | Valor |
|---|---|
| 1. Código | T-QL2-POUSADA-01 |
| 2. Situação | Produto Pousada identificado, falta 1 dado |
| 3. Produto | Pousada Arágua |
| 4. Origem | Qualquer |
| 5. QL | QL2→QL3 |
| 6. C | C2 |
| 7. Estágio | Em qualificação |
| 8. Objetivo | Aprofundar qualificação dentro do produto certo |
| 9. Emoção desejada | Desejo leve de descanso |
| 10. Resultado esperado | Avançar dado faltante |
| 11. Mensagem principal | "A Pousada Arágua tem suítes individuais, com café da manhã servido na acomodação." + [dado faltante] |
| 12. Variação curta | Adaptar ao dado que falta ("Quais datas vocês estão pensando?" ou "E quantas pessoas estarão na viagem?"), nunca repetir o já dado |
| 13. Ativo recomendado | AT-POU-FACHADA-01 ou AT-POU-PISCINA-01, se o momento pedir (não obrigatório) |
| 14. Ativo proibido | Qualquer AT-CAS-*; AT-POU-SUITE-01 (bloqueado) |
| 15. CTA | Dado faltante |
| 16. Momento de envio | Assim que Pousada é confirmada |
| 17. Quando usar | Produto=Pousada, falta 1 dado |
| 18. Quando não usar | Produto=Casa (usar T-QL2-CASA-01) |
| 19. Se responder | T-QL3-DADO-01 ou T-QL2-CRIANCA-01/PET-01 |
| 20. Se não responder | Follow-up QL2/QL3 |
| 21. Próximo template | T-QL3-DADO-01 |
| 22. Próxima ação | Aguardar dado faltante |
| 23. Follow-up | Matriz 10.1, QL2/QL3 |
| 24. Registro mínimo no CRM | Produto=Pousada Arágua, QL, C, Estágio=Em qualificação |
| 25. Responsável | Rene/Nubia |
| 26. Precisa de Renildo? | Não |
| 27. Riscos | Nunca misturar amenities da Casa |
| 28. Fontes oficiais | Funil (seção 5) + Guia (seção 8) |
| 29. Status | Versão 1.0 — Piloto manual assistido |
| 30. Data de revisão | 05/08/2026 |

#### T-QL2-CASA-01

| Campo | Valor |
|---|---|
| 1. Código | T-QL2-CASA-01 |
| 2. Situação | Produto Casa identificado, falta 1 dado |
| 3. Produto | Casa Arágua Mariscal |
| 4. Origem | Qualquer |
| 5. QL | QL2→QL3 |
| 6. C | C2 |
| 7. Estágio | Em qualificação |
| 8. Objetivo | Aprofundar qualificação dentro do produto certo |
| 9. Emoção desejada | Desejo de privacidade/família reunida |
| 10. Resultado esperado | Avançar dado faltante |
| 11. Mensagem principal | "A Casa Arágua Mariscal é completa e privativa, com piscina para o grupo." + [dado faltante] |
| 12. Variação curta | Se grupo >4 já conhecido, considerar nota de configuração (Biblioteca, Regra 20) só quando o número já é sabido |
| 13. Ativo recomendado | AT-CAS-FACHADA-01 ou AT-CAS-PISCINA-01, se o momento pedir |
| 14. Ativo proibido | Qualquer AT-POU-*; AT-CAS-CHURRASQUEIRA-01 (bloqueado) |
| 15. CTA | Dado faltante |
| 16. Momento de envio | Assim que Casa é confirmada |
| 17. Quando usar | Produto=Casa, falta 1 dado |
| 18. Quando não usar | Produto=Pousada |
| 19. Se responder | T-QL3-DADO-01 ou T-QL2-CRIANCA-01 |
| 20. Se não responder | Follow-up QL2/QL3 |
| 21. Próximo template | T-QL3-DADO-01 |
| 22. Próxima ação | Aguardar dado faltante |
| 23. Follow-up | Matriz 10.2, QL2/QL3 |
| 24. Registro mínimo no CRM | Produto=Casa Arágua, QL, C, Estágio=Em qualificação |
| 25. Responsável | Rene/Nubia |
| 26. Precisa de Renildo? | Não |
| 27. Riscos | Nunca dizer "acomoda até 6" sem explicar a configuração |
| 28. Fontes oficiais | Funil (seção 5) + Guia (seção 8) + Biblioteca (Regra 20) |
| 29. Status | Versão 1.0 — Piloto manual assistido |
| 30. Data de revisão | 05/08/2026 |

#### T-QL2-CRIANCA-01

| Campo | Valor |
|---|---|
| 1. Código | T-QL2-CRIANCA-01 |
| 2. Situação | Criança relevante ao grupo |
| 3. Produto | Já identificado |
| 4. Origem | Qualquer |
| 5. QL | QL2/QL3 |
| 6. C | C2 (Arquitetura, exemplo "perfil da viagem") |
| 7. Estágio | Em qualificação |
| 8. Objetivo | Diagnosticar idade para indicar acomodação com segurança |
| 9. Emoção desejada | Cuidado |
| 10. Resultado esperado | Idade da criança |
| 11. Mensagem principal | "Vai ter criança na viagem? Se sim, qual a idade — isso ajuda a indicar a opção mais adequada." |
| 12. Variação curta | Bebê: acrescentar "temos possibilidade de berço portátil, com aviso antecipado e confirmação da equipe" |
| 13. Ativo recomendado | AT-POU-FAMILIA-01, só após idade confirmada |
| 14. Ativo proibido | Suíte com mezanino sem ressalva, se criança pequena |
| 15. CTA | Idade da criança |
| 16. Momento de envio | Só quando relevante — nunca pergunta fixa (Funil, seção 5, item 4) |
| 17. Quando usar | Grupo sugere família ou lead menciona criança |
| 18. Quando não usar | Casal sem menção de criança |
| 19. Se responder | T-QL3-FAMILIA-01 |
| 20. Se não responder | Follow-up QL2/QL3 |
| 21. Próximo template | T-QL3-FAMILIA-01 |
| 22. Próxima ação | Aguardar idade |
| 23. Follow-up | Matriz QL2/QL3 |
| 24. Registro mínimo no CRM | Número de pessoas (detalhado), Observações curtas="criança confirmada, idade pendente" |
| 25. Responsável | Rene/Nubia |
| 26. Precisa de Renildo? | Não |
| 27. Riscos | Nunca prometer berço como garantido |
| 28. Fontes oficiais | Funil (seção 5, item 4) + Biblioteca (PC-EXT-31) |
| 29. Status | Versão 1.0 — Piloto manual assistido |
| 30. Data de revisão | 05/08/2026 |

#### T-QL2-PET-01

| Campo | Valor |
|---|---|
| 1. Código | T-QL2-PET-01 |
| 2. Situação | Pet mencionado |
| 3. Produto | Já identificado |
| 4. Origem | Qualquer |
| 5. QL | QL2/QL3 |
| 6. C | C2 (mesma classificação de PC-C2-04 na Biblioteca) |
| 7. Estágio | Em qualificação |
| 8. Objetivo | Diagnosticar porte/quantidade, nunca autorizar |
| 9. Emoção desejada | Acolhimento sem promessa |
| 10. Resultado esperado | Porte + quantidade |
| 11. Mensagem principal | "Vocês vêm com pet? Se sim, qual o porte e quantos pets — a equipe confirma se a acomodação atende." |
| 12. Variação curta | Fora do padrão (porte grande/mais de 1 pet): "Esse caso foge do padrão comum — a equipe confirma diretamente antes de indicar a acomodação." |
| 13. Ativo recomendado | Nenhum |
| 14. Ativo proibido | Qualquer, até confirmação |
| 15. CTA | Porte e quantidade |
| 16. Momento de envio | Quando pet é mencionado |
| 17. Quando usar | Toda menção a pet |
| 18. Quando não usar | Grupo sem pet |
| 19. Se responder | Padrão: segue qualificação · Fora do padrão: escala checagem da equipe |
| 20. Se não responder | Follow-up QL2 |
| 21. Próximo template | T-QL2-PRECO-01 ou T-QL3-DADO-01 |
| 22. Próxima ação | Aguardar detalhe do pet |
| 23. Follow-up | Matriz QL2 |
| 24. Registro mínimo no CRM | Observações curtas="pet: porte/quantidade" |
| 25. Responsável | Rene/Nubia |
| 26. Precisa de Renildo? | Só se fora do padrão |
| 27. Riscos | Nunca autorizar, prometer "tranquilo" ou citar taxa |
| 28. Fontes oficiais | Biblioteca (PC-C2-04, PC-C2-04-B) |
| 29. Status | Versão 1.0 — Piloto manual assistido |
| 30. Data de revisão | 05/08/2026 |

#### T-QL2-ESTRUTURA-01

| Campo | Valor |
|---|---|
| 1. Código | T-QL2-ESTRUTURA-01 |
| 2. Situação | Pergunta objetiva sobre estrutura (o que está incluso) |
| 3. Produto | Já identificado |
| 4. Origem | Qualquer |
| 5. QL | QL2/QL3 |
| 6. C | C1 (resposta puramente informativa, sem pedido de dado) |
| 7. Estágio | Em qualificação |
| 8. Objetivo | Responder com dado oficial, sem citar valor |
| 9. Emoção desejada | Confiança na informação |
| 10. Resultado esperado | Dúvida resolvida |
| 11. Mensagem principal | "Na Pousada Arágua, o café da manhã é servido na própria suíte, e vocês têm acesso à piscina e churrasqueira compartilhadas. Na Casa Arágua, a piscina e a churrasqueira são privativas, e o café da manhã não é incluso por padrão." |
| 12. Variação curta | Usar só o trecho do produto já identificado |
| 13. Ativo recomendado | Nenhum obrigatório |
| 14. Ativo proibido | Nenhuma restrição especial além da regra de produto |
| 15. CTA | "Posso ajudar com mais alguma coisa sobre a estrutura?" |
| 16. Momento de envio | Sob demanda |
| 17. Quando usar | Dúvida objetiva de estrutura, sem pedido de dado embutido |
| 18. Quando não usar | Se a resposta incluir pedido de avanço de dado → reclassificar C2 (seção "Relação com C") |
| 19. Se responder | Segue qualificação |
| 20. Se não responder | Não gera follow-up dedicado |
| 21. Próximo template | T-QL2-PRECO-01 |
| 22. Próxima ação | Nenhuma obrigatória |
| 23. Follow-up | Não aplicável |
| 24. Registro mínimo no CRM | Nenhum campo obrigatório adicional |
| 25. Responsável | Rene/Nubia |
| 26. Precisa de Renildo? | Não |
| 27. Riscos | Café da manhã da Casa não existe em nenhuma condição — nunca dizer "opcional"/"sob consulta" (Biblioteca, regra-mãe 17, atualizada 2026-08-07) |
| 28. Fontes oficiais | Biblioteca (PC-C1-02) |
| 29. Status | Versão 1.0 — Piloto manual assistido |
| 30. Data de revisão | 05/08/2026 |

### QL3 — Intenção forte e dado faltante

#### T-QL3-DADO-01

| Campo | Valor |
|---|---|
| 1. Código | T-QL3-DADO-01 |
| 2. Situação | Falta 1 dos 3 dados essenciais (tipicamente Produto) |
| 3. Produto | Conforme o caso |
| 4. Origem | Qualquer |
| 5. QL | QL3 |
| 6. C | C2 |
| 7. Estágio | Em qualificação |
| 8. Objetivo | Fechar o último dado — ação obrigatória se o dado for Produto (Funil, seção 3) |
| 9. Emoção desejada | Sensação de estar quase lá |
| 10. Resultado esperado | Dado completo → vira QL4 |
| 11. Mensagem principal | Roteador — usar a mensagem de T-QL2-PRODUTO-01, T-QL2-PESSOAS-01 ou a variação de Datas, conforme o dado exato que falta |
| 12. Variação curta | Nenhuma — a mensagem certa depende do dado faltante identificado |
| 13. Ativo recomendado | Depende do dado |
| 14. Ativo proibido | Ativo do produto errado |
| 15. CTA | Dado exato faltante |
| 16. Momento de envio | Assim que identificado que falta 1 dado |
| 17. Quando usar | 2 dos 3 dados essenciais já confirmados |
| 18. Quando não usar | Faltam 2+ (voltar para QL2) |
| 19. Se responder | T-QL4-DADOS-01 |
| 20. Se não responder | Follow-up 24-48h/3 dias (Matriz seção 5) |
| 21. Próximo template | T-QL4-DADOS-01 |
| 22. Próxima ação | Aguardar último dado |
| 23. Follow-up | QL3 (Matriz seção 5) |
| 24. Registro mínimo no CRM | QL=QL3, Estágio=Em qualificação, Próxima ação="aguardar [dado]" |
| 25. Responsável | Rene/Nubia |
| 26. Precisa de Renildo? | Não |
| 27. Riscos | Se o dado faltante for Produto, é sempre ação obrigatória — nunca pular para orçamento sem produto definido |
| 28. Fontes oficiais | Funil (seção 3 e 4) |
| 29. Status | Versão 1.0 — Piloto manual assistido |
| 30. Data de revisão | 05/08/2026 |

#### T-QL3-DUVIDA-01

| Campo | Valor |
|---|---|
| 1. Código | T-QL3-DUVIDA-01 |
| 2. Situação | Dúvida específica sobre o produto já identificado |
| 3. Produto | Pousada ou Casa (variação) |
| 4. Origem | Qualquer |
| 5. QL | QL3 |
| 6. C | Regra de ramificação: C1 se a dúvida for puramente informativa (estrutura, capacidade, localização); C2 se a resposta incluir pedido de avanço de dado comercial |
| 7. Estágio | Em qualificação |
| 8. Objetivo | Resolver dúvida pontual sem perder o fio da qualificação |
| 9. Emoção desejada | Confiança técnica |
| 10. Resultado esperado | Dúvida resolvida, retomar dado faltante |
| 11. Mensagem principal | Roteador — usar o template C1 correspondente ao tema perguntado (Biblioteca, Bloco C1) |
| 12. Variação curta | Pousada usa Matriz 10.1; Casa usa 10.2 |
| 13. Ativo recomendado | Depende da dúvida (Guia, "Próximo ativo recomendado") |
| 14. Ativo proibido | Ativo do produto errado |
| 15. CTA | Fechar a dúvida, retomar dado faltante |
| 16. Momento de envio | Sob demanda |
| 17. Quando usar | Dúvida pontual dentro da qualificação avançada |
| 18. Quando não usar | Dúvida sobre valor (é C2, usar T-QL2-PRECO-01 ou T-QL4-DUVIDA-01) |
| 19. Se responder | Retoma T-QL3-DADO-01 |
| 20. Se não responder | Não gera follow-up dedicado |
| 21. Próximo template | T-QL3-DADO-01 |
| 22. Próxima ação | Retomar coleta de dado |
| 23. Follow-up | Segue cadência QL3 geral |
| 24. Registro mínimo no CRM | Observações curtas com o tema |
| 25. Responsável | Rene/Nubia |
| 26. Precisa de Renildo? | Não |
| 27. Riscos | Roteador — checar sempre o template C1 específico, nunca inventar dado |
| 28. Fontes oficiais | Biblioteca (Bloco C1) + Matriz (seção 10) |
| 29. Status | Versão 1.0 — Piloto manual assistido |
| 30. Data de revisão | 05/08/2026 |

#### T-QL3-ATIVO-01

| Campo | Valor |
|---|---|
| 1. Código | T-QL3-ATIVO-01 |
| 2. Situação | Envio do primeiro ativo visual |
| 3. Produto | Pousada ou Casa (variação) |
| 4. Origem | Qualquer |
| 5. QL | QL3 |
| 6. C | C2 (mensagem inclui pedido de dado) |
| 7. Estágio | Em qualificação |
| 8. Objetivo | Gerar desejo/apresentar produto com apoio visual |
| 9. Emoção desejada | Desejo concreto |
| 10. Resultado esperado | Avançar para transição/orçamento |
| 11. Mensagem principal | (Pousada) "Essa é a piscina da Pousada Arágua 😊 O ambiente é pequeno, acolhedor e tranquilo, ótimo pra relaxar depois da praia. Vocês já têm as datas e quantas pessoas seriam?" |
| 12. Variação curta | (Casa) "A Casa Arágua é completa e privativa, com piscina só pro grupo de vocês 😊 Quantas pessoas estarão na viagem?" |
| 13. Ativo recomendado | AT-POU-PISCINA-01 ou AT-CAS-PISCINA-01 (máx. 1 foto) |
| 14. Ativo proibido | Ativo do outro produto; AT-POU-SUITE-01 (bloqueado); AT-CAS-CHURRASQUEIRA-01 (bloqueado) |
| 15. CTA | Conforme ficha do ativo (Guia, seção 8) |
| 16. Momento de envio | Depois de produto confirmado, antes de negociação |
| 17. Quando usar | 1º envio visual do ciclo |
| 18. Quando não usar | Antes de produto confirmado; C3/C4 |
| 19. Se responder | T-QL3-ESTRUTURA-01 ou T-QL3-TRANSICAO-01 |
| 20. Se não responder | Follow-up QL3 |
| 21. Próximo template | Conforme "Próximo ativo recomendado" do Guia |
| 22. Próxima ação | Observar reação |
| 23. Follow-up | Matriz QL3 |
| 24. Registro mínimo no CRM | Observações curtas="ativo enviado: [código]" |
| 25. Responsável | Rene/Nubia |
| 26. Precisa de Renildo? | Não |
| 27. Riscos | Nunca mais de 1 foto no primeiro ciclo; AT-POU-PISCINA-01 não resolve dúvida objetiva de tamanho |
| 28. Fontes oficiais | Guia (AT-POU-PISCINA-01, AT-CAS-PISCINA-01) |
| 29. Status | Versão 1.0 — Piloto manual assistido |
| 30. Data de revisão | 05/08/2026 |

#### T-QL3-ESTRUTURA-01

| Campo | Valor |
|---|---|
| 1. Código | T-QL3-ESTRUTURA-01 |
| 2. Situação | Dúvida sobre café da manhã ou piscina |
| 3. Produto | Já identificado |
| 4. Origem | Qualquer |
| 5. QL | QL3 |
| 6. C | C1 (resposta informativa) |
| 7. Estágio | Em qualificação |
| 8. Objetivo | Resolver dúvida específica com apoio visual |
| 9. Emoção desejada | Segurança sobre a experiência |
| 10. Resultado esperado | Dúvida resolvida |
| 11. Mensagem principal | (café) "Sim, na Pousada Arágua o café da manhã é servido na suíte, que é um dos diferenciais da pousada." |
| 12. Variação curta | (piscina) usar mensagens ideais de AT-POU-PISCINA-01/AT-CAS-PISCINA-01 |
| 13. Ativo recomendado | AT-POU-CAFE-01 (café) ou AT-POU-PISCINA-01/AT-CAS-PISCINA-01 (piscina) |
| 14. Ativo proibido | Ativo do outro produto |
| 15. CTA | Conforme ficha do ativo |
| 16. Momento de envio | Sob demanda |
| 17. Quando usar | Pergunta específica sobre café ou piscina |
| 18. Quando não usar | Se a resposta incluir pedido de avanço de dado → reclassificar C2 |
| 19. Se responder | Retoma qualificação |
| 20. Se não responder | Não gera follow-up dedicado |
| 21. Próximo template | T-QL3-TRANSICAO-01 |
| 22. Próxima ação | Retomar dado faltante |
| 23. Follow-up | Segue cadência QL3 |
| 24. Registro mínimo no CRM | Observações curtas com o tema |
| 25. Responsável | Rene/Nubia |
| 26. Precisa de Renildo? | Não |
| 27. Riscos | Café da Casa: nunca citar valor |
| 28. Fontes oficiais | Biblioteca (PC-EXT-07) + Guia (AT-POU-PISCINA-01, AT-CAS-PISCINA-01) |
| 29. Status | Versão 1.0 — Piloto manual assistido |
| 30. Data de revisão | 05/08/2026 |

#### T-QL3-FAMILIA-01

| Campo | Valor |
|---|---|
| 1. Código | T-QL3-FAMILIA-01 |
| 2. Situação | Dúvida sobre estrutura para família/criança |
| 3. Produto | Já identificado (tipicamente Pousada) |
| 4. Origem | Qualquer |
| 5. QL | QL3 |
| 6. C | C2 (pergunta "quantas crianças" é perfil da viagem) |
| 7. Estágio | Em qualificação |
| 8. Objetivo | Confirmar adequação para o grupo |
| 9. Emoção desejada | Segurança para levar a família |
| 10. Resultado esperado | Confirmar estrutura, avançar |
| 11. Mensagem principal | "Temos uma área verde bem tranquila, com rede e espaço pras crianças brincarem 😊 Quantas crianças estarão na viagem?" |
| 12. Variação curta | Se mezanino envolvido (Fuego/Metallo), incluir ressalva de degraus |
| 13. Ativo recomendado | AT-POU-FAMILIA-01 |
| 14. Ativo proibido | Suíte com mezanino sem ressalva |
| 15. CTA | Quantidade/idade das crianças |
| 16. Momento de envio | Só depois de confirmar criança no grupo |
| 17. Quando usar | Criança já confirmada, dúvida de estrutura |
| 18. Quando não usar | Antes de confirmar criança; casal sozinho |
| 19. Se responder | T-QL3-TRANSICAO-01 |
| 20. Se não responder | Follow-up QL3 |
| 21. Próximo template | T-QL3-TRANSICAO-01 |
| 22. Próxima ação | Confirmar composição final |
| 23. Follow-up | Matriz QL3 |
| 24. Registro mínimo no CRM | Número de pessoas detalhado |
| 25. Responsável | Rene/Nubia |
| 26. Precisa de Renildo? | Não |
| 27. Riscos | Nunca indicar suíte com mezanino para criança pequena sem checagem |
| 28. Fontes oficiais | Guia (AT-POU-FAMILIA-01) + Biblioteca (PC-EXT-31) |
| 29. Status | Versão 1.0 — Piloto manual assistido |
| 30. Data de revisão | 05/08/2026 |

#### T-QL3-TRANSICAO-01

| Campo | Valor |
|---|---|
| 1. Código | T-QL3-TRANSICAO-01 |
| 2. Situação | Pedido de foto específica + transição para orçamento |
| 3. Produto | Já identificado |
| 4. Origem | Qualquer |
| 5. QL | QL3→QL4 |
| 6. C | C2 (orientação comercial ativa) |
| 7. Estágio | Em qualificação |
| 8. Objetivo | Fechar dúvidas e abrir caminho para orçamento |
| 9. Emoção desejada | Sensação de estar pronto para o próximo passo |
| 10. Resultado esperado | Virar QL4 |
| 11. Mensagem principal | "Posso mostrar isso sim 😊" + [ativo específico do catálogo, se aplicável] + "Com essas informações, a equipe consegue verificar disponibilidade e montar o orçamento conforme as regras." |
| 12. Variação curta | Se ainda faltar 1 dado, priorizar T-QL3-DADO-01 antes |
| 13. Ativo recomendado | O ativo específico pedido, se catalogado no Guia |
| 14. Ativo proibido | Ativo fora do catálogo oficial; AT-POU-SUITE-01/AT-CAS-CHURRASQUEIRA-01 (bloqueados) |
| 15. CTA | Confirmar avanço para orçamento |
| 16. Momento de envio | Quando dados + dúvidas já estão fechados |
| 17. Quando usar | Fechamento da etapa de qualificação |
| 18. Quando não usar | Dados ainda incompletos |
| 19. Se responder | T-QL4-DADOS-01 |
| 20. Se não responder | Follow-up QL3, depois QL4 |
| 21. Próximo template | T-QL4-DADOS-01 |
| 22. Próxima ação | Aguardar confirmação de avanço |
| 23. Follow-up | Matriz QL3 (3 dias) |
| 24. Registro mínimo no CRM | QL atualizado se virar QL4, Estágio=Em qualificação→Orçamento |
| 25. Responsável | Rene/Nubia |
| 26. Precisa de Renildo? | Não |
| 27. Riscos | Nunca mandar catálogo aberto de fotos |
| 28. Fontes oficiais | Funil (seção 5, item 6) + Biblioteca (PC-EXT-13/14) |
| 29. Status | Versão 1.0 — Piloto manual assistido |
| 30. Data de revisão | 05/08/2026 |

### QL4 — Orçamento e decisão

#### T-QL4-DADOS-01

| Campo | Valor |
|---|---|
| 1. Código | T-QL4-DADOS-01 |
| 2. Situação | Dados completos → encaminhamento humano |
| 3. Produto | Confirmado |
| 4. Origem | Qualquer |
| 5. QL | QL4 |
| 6. C | C2 |
| 7. Estágio | Orçamento |
| 8. Objetivo | Confirmar coleta e encaminhar |
| 9. Emoção desejada | Confiança de que será bem cuidado |
| 10. Resultado esperado | Caso encaminhado à equipe |
| 11. Mensagem principal | "Vou deixar as informações organizadas para a equipe avaliar." |
| 12. Variação curta | Nenhuma |
| 13. Ativo recomendado | Nenhum (normalmente sem novo ativo em QL4) |
| 14. Ativo proibido | Qualquer foto nova não solicitada |
| 15. CTA | Nenhum (mensagem de transição) |
| 16. Momento de envio | Assim que os 3 dados essenciais estão completos e há pedido de orçamento ou intenção clara |
| 17. Quando usar | Produto+Datas+Pessoas confirmados |
| 18. Quando não usar | Falta qualquer dos 3 (usar QL3) |
| 19. Se responder | Segue para T-QL4-ORCAMENTO-01 |
| 20. Se não responder | Não aplicável — SLA interno, não mensagem ao lead |
| 21. Próximo template | T-QL4-ORCAMENTO-01 |
| 22. Próxima ação | SLA interno da equipe preparar orçamento (não é follow-up ao lead) |
| 23. Follow-up | Nenhum ainda — só após orçamento efetivamente enviado (Matriz seção 4) |
| 24. Registro mínimo no CRM | QL=QL4, C=C2, Estágio=Orçamento, Orçamento enviado?=Não |
| 25. Responsável | Rene/Nubia |
| 26. Precisa de Renildo? | Não |
| 27. Riscos | SLA interno não pode virar mensagem ao lead disfarçada de follow-up |
| 28. Fontes oficiais | Funil (seção 4) + Arquitetura (seção 5, seção 12) |
| 29. Status | Versão 1.0 — Piloto manual assistido |
| 30. Data de revisão | 05/08/2026 |

#### T-QL4-ORCAMENTO-01

| Campo | Valor |
|---|---|
| 1. Código | T-QL4-ORCAMENTO-01 |
| 2. Situação | Orçamento efetivamente enviado + confirmação de recebimento |
| 3. Produto | Confirmado |
| 4. Origem | Qualquer |
| 5. QL | QL4 |
| 6. C | C2 |
| 7. Estágio | Orçamento |
| 8. Objetivo | Marcar o envio, reconhecer o retorno do lead |
| 9. Emoção desejada | Cuidado |
| 10. Resultado esperado | Orçamento enviado?=Sim; lead engajado |
| 11. Mensagem principal | (acompanha o envio, sempre humano) texto de valor elaborado pela equipe |
| 12. Variação curta | (confirmação de recebimento) "Que bom que chegou! Fico à disposição para qualquer dúvida 😊" |
| 13. Ativo recomendado | Nenhum |
| 14. Ativo proibido | Qualquer foto nova |
| 15. CTA | Nenhum obrigatório na confirmação |
| 16. Momento de envio | No envio real / na resposta do lead |
| 17. Quando usar | Orçamento pronto e efetivamente enviado |
| 18. Quando não usar | Orçamento ainda não pronto (usar T-QL4-DADOS-01) |
| 19. Se responder | T-QL4-DUVIDA-01 ou T-QL4-RESERVA-01 |
| 20. Se não responder | T-QL4-FOLLOWUP-01 (24h) |
| 21. Próximo template | T-QL4-FOLLOWUP-01 |
| 22. Próxima ação | Aguardar reação |
| 23. Follow-up | Matriz seção 4: 24h após orçamento enviado |
| 24. Registro mínimo no CRM | Orçamento enviado?=Sim (só após envio real), Último contato |
| 25. Responsável | Rene/Nubia |
| 26. Precisa de Renildo? | Não |
| 27. Riscos | "Orçamento enviado?=Sim" só depois do envio real — nunca antecipar |
| 28. Fontes oficiais | CRM (regras principais) + Matriz (seção 4) |
| 29. Status | Versão 1.0 — Piloto manual assistido |
| 30. Data de revisão | 05/08/2026 |

#### T-QL4-FOLLOWUP-01

| Campo | Valor |
|---|---|
| 1. Código | T-QL4-FOLLOWUP-01 |
| 2. Situação | Follow-up 24h/48h pós-orçamento |
| 3. Produto | Confirmado |
| 4. Origem | Qualquer |
| 5. QL | QL4 |
| 6. C | C2 |
| 7. Estágio | Aguardando retorno |
| 8. Objetivo | Retomar sem pressionar |
| 9. Emoção desejada | Cuidado contínuo |
| 10. Resultado esperado | Resposta do lead |
| 11. Mensagem principal | (24h) "Oi! Passando só pra saber se o orçamento chegou certinho pra você 😊" |
| 12. Variação curta | (48h) "Oi! Ficou alguma dúvida sobre os valores ou sobre a estadia? Fico à disposição pra ajudar." |
| 13. Ativo recomendado | Nenhum |
| 14. Ativo proibido | Qualquer |
| 15. CTA | Retomar decisão/dúvida |
| 16. Momento de envio | 24h e 48h após orçamento enviado (nunca por atraso interno) |
| 17. Quando usar | Orçamento enviado, sem resposta |
| 18. Quando não usar | Antes do orçamento efetivamente enviado |
| 19. Se responder | T-QL4-DUVIDA-01 ou T-QL4-RESERVA-01 |
| 20. Se não responder | T-QL4-ENCERRAR-01 |
| 21. Próximo template | T-QL4-ENCERRAR-01 |
| 22. Próxima ação | Aguardar resposta |
| 23. Follow-up | Matriz seção 4 |
| 24. Registro mínimo no CRM | Próximo follow-up, Último contato, Estágio=Aguardando retorno |
| 25. Responsável | Rene/Nubia |
| 26. Precisa de Renildo? | Não |
| 27. Riscos | Nunca confundir SLA interno com follow-up ao lead |
| 28. Fontes oficiais | Matriz (seção 4, texto oficial — não reescrito) |
| 29. Status | Versão 1.0 — Piloto manual assistido |
| 30. Data de revisão | 05/08/2026 |

#### T-QL4-DUVIDA-01

| Campo | Valor |
|---|---|
| 1. Código | T-QL4-DUVIDA-01 |
| 2. Situação | Dúvida pós-orçamento |
| 3. Produto | Confirmado |
| 4. Origem | Qualquer |
| 5. QL | QL4 |
| 6. C | Regra de ramificação: C1 se a dúvida for puramente estrutural, sem tocar em valor/condição; C2 (principal) se envolver valor, parcelamento ou revisão de orçamento |
| 7. Estágio | Orçamento |
| 8. Objetivo | Resolver dúvida sem alterar valor sozinha |
| 9. Emoção desejada | Segurança para decidir |
| 10. Resultado esperado | Dúvida resolvida, avançar para reserva |
| 11. Mensagem principal | Roteador — estrutura: template C1 correspondente; parcelamento: Biblioteca PC-EXT-20; alteração de composição: "Para encaminhar a revisão do orçamento à equipe, confirme: produto, datas, orçamento original recebido e a nova composição." |
| 12. Variação curta | Nenhuma |
| 13. Ativo recomendado | Depende da dúvida |
| 14. Ativo proibido | Ativo do produto errado |
| 15. CTA | Fechar dúvida, retomar decisão |
| 16. Momento de envio | Sob demanda |
| 17. Quando usar | Dúvida específica após orçamento |
| 18. Quando não usar | Pedido de desconto (é C3, usar T-C3-DESCONTO-01) |
| 19. Se responder | T-QL4-RESERVA-01 |
| 20. Se não responder | T-QL4-FOLLOWUP-01 |
| 21. Próximo template | T-QL4-RESERVA-01 |
| 22. Próxima ação | Aguardar decisão |
| 23. Follow-up | Matriz seção 4 |
| 24. Registro mínimo no CRM | Observações curtas com o tema |
| 25. Responsável | Rene/Nubia |
| 26. Precisa de Renildo? | Não, salvo se a dúvida escalar para valor/exceção |
| 27. Riscos | Nunca recalcular valor sozinha |
| 28. Fontes oficiais | Biblioteca (PC-EXT-20, PC-EXT-28) |
| 29. Status | Versão 1.0 — Piloto manual assistido |
| 30. Data de revisão | 05/08/2026 |

#### T-QL4-RESERVA-01

| Campo | Valor |
|---|---|
| 1. Código | T-QL4-RESERVA-01 |
| 2. Situação | Pedido de reserva / próximo passo de pagamento |
| 3. Produto | Confirmado |
| 4. Origem | Qualquer |
| 5. QL | QL4 |
| 6. C | C2 |
| 7. Estágio | Negociação/validação |
| 8. Objetivo | Orientar próximo passo sem prometer reserva sem validação |
| 9. Emoção desejada | Confiança no processo |
| 10. Resultado esperado | Pagamento/sinal encaminhado para validação humana |
| 11. Mensagem principal | "A conversa segue por aqui, mas a reserva só fica confirmada depois do pagamento ou sinal validado pela equipe. A data permanece sujeita à disponibilidade até lá." |
| 12. Variação curta | (pagamento já enviado) "Que bom! Pode enviar o comprovante — a equipe confirma o recebimento e valida com vocês." |
| 13. Ativo recomendado | Nenhum |
| 14. Ativo proibido | Qualquer |
| 15. CTA | Próximo passo de pagamento |
| 16. Momento de envio | Quando o lead pede para reservar/segurar data |
| 17. Quando usar | Pedido de reserva sem pagamento validado |
| 18. Quando não usar | Reserva já confirmada por humano |
| 19. Se responder | Aguarda comprovante/validação |
| 20. Se não responder | T-QL4-FOLLOWUP-01 |
| 21. Próximo template | Encerramento do ciclo (Registro Comercial, fora do escopo deste documento) |
| 22. Próxima ação | Aguardar comprovante/validação humana |
| 23. Follow-up | Matriz seção 4 |
| 24. Registro mínimo no CRM | Estágio=Negociação/validação, Precisa de Renildo?=conforme valor |
| 25. Responsável | Rene/Nubia |
| 26. Precisa de Renildo? | Sim, se validação financeira fora do padrão |
| 27. Riscos | Nunca dizer "reserva confirmada" sem validação real |
| 28. Fontes oficiais | Biblioteca (PC-EXT-21, PC-EXT-29) |
| 29. Status | Versão 1.0 — Piloto manual assistido |
| 30. Data de revisão | 05/08/2026 |

#### T-QL4-ENCERRAR-01

| Campo | Valor |
|---|---|
| 1. Código | T-QL4-ENCERRAR-01 |
| 2. Situação | Silêncio persistente pós-orçamento + encerramento de cadência |
| 3. Produto | Confirmado |
| 4. Origem | Qualquer |
| 5. QL | QL4 (mantém — silêncio não reduz QL) |
| 6. C | C1 (mensagem leve de fechamento, sem pedido comercial) |
| 7. Estágio | Aguardando retorno |
| 8. Objetivo | Encerrar com leveza, sem fechar a porta |
| 9. Emoção desejada | Acolhimento sem cobrança |
| 10. Resultado esperado | Ciclo pausado, relacionamento mantido |
| 11. Mensagem principal | "Oi! Ficamos à disposição se quiser retomar — é só chamar por aqui quando fizer sentido pra você 😊" |
| 12. Variação curta | Nenhuma |
| 13. Ativo recomendado | Nenhum |
| 14. Ativo proibido | Qualquer |
| 15. CTA | Nenhum |
| 16. Momento de envio | Após tentativa comercial completa sem resposta (Matriz seção 9) |
| 17. Quando usar | Fim da cadência QL4 |
| 18. Quando não usar | Lead ainda respondendo |
| 19. Se responder | Reabrir conforme conteúdo |
| 20. Se não responder | Critério de parada atingido |
| 21. Próximo template | Nenhum |
| 22. Próxima ação | Humano decide Estágio final (Perdido/Nutrição) — nunca a IA |
| 23. Follow-up | Encerra cadência oficial (Matriz seção 12) |
| 24. Registro mínimo no CRM | Próxima ação="equipe decide Estágio final", Status final=vazio até decisão |
| 25. Responsável | Rene/Nubia |
| 26. Precisa de Renildo? | Não, salvo decisão controversa |
| 27. Riscos | Nunca marcar Perdido/Convertido por dedução |
| 28. Fontes oficiais | Matriz (seção 4, seção 9, seção 12) + Funil (seção 6) |
| 29. Status | Versão 1.0 — Piloto manual assistido |
| 30. Data de revisão | 05/08/2026 |

### NQ — Fora do perfil

#### T-NQ-PERFIL-01

| Campo | Valor |
|---|---|
| 1. Código | T-NQ-PERFIL-01 |
| 2. Situação | Incompatibilidade real confirmada (não presumida) |
| 3. Produto | Não aplicável |
| 4. Origem | Qualquer |
| 5. QL | NQ |
| 6. C | C1 |
| 7. Estágio | Novo/Em qualificação, conforme o momento da identificação |
| 8. Objetivo | Encerrar sem atrito, sem falsa esperança |
| 9. Emoção desejada | Respeito |
| 10. Resultado esperado | Status final="Fora do perfil" |
| 11. Mensagem principal | "A Villa Arágua não trabalha com festas ou eventos. Nossa proposta é hospedagem para descanso, família e privacidade em Mariscal." |
| 12. Variação curta | (grupo acima do perfil / pedido fora do escopo): textos correspondentes da Matriz seção 8 |
| 13. Ativo recomendado | Nenhum |
| 14. Ativo proibido | Qualquer |
| 15. CTA | Nenhum |
| 16. Momento de envio | Assim que confirmado o desencaixe real, nunca por presunção |
| 17. Quando usar | Incompatibilidade confirmada |
| 18. Quando não usar | Dúvida ainda não esclarecida, ou apenas silêncio (silêncio não é critério de NQ) |
| 19. Se responder | T-NQ-ENCERRAR-01 |
| 20. Se não responder | Não gera follow-up (NQ é imediato) |
| 21. Próximo template | T-NQ-ENCERRAR-01 |
| 22. Próxima ação | Nenhuma |
| 23. Follow-up | Nenhum — NQ é imediato |
| 24. Registro mínimo no CRM | QL=NQ, Status final="Fora do perfil", Motivo de perda |
| 25. Responsável | Rene/Nubia |
| 26. Precisa de Renildo? | Não |
| 27. Riscos | Nunca classificar NQ cedo demais só por falta de resposta |
| 28. Fontes oficiais | Matriz (seção 8) + Funil (seção 3) |
| 29. Status | Versão 1.0 — Piloto manual assistido |
| 30. Data de revisão | 05/08/2026 |

#### T-NQ-REDIRECIONAR-01

| Campo | Valor |
|---|---|
| 1. Código | T-NQ-REDIRECIONAR-01 |
| 2. Situação | Um produto não atende, mas o outro pode; ou nutrição futura quando aplicável |
| 3. Produto | O outro produto (a definir) |
| 4. Origem | Qualquer |
| 5. QL | NQ→QL2, se aceito |
| 6. C | C1 |
| 7. Estágio | Em qualificação, se redirecionado; Nutrição, se não |
| 8. Objetivo | Não perder o lead por engano de produto |
| 9. Emoção desejada | Sensação de ser bem cuidado |
| 10. Resultado esperado | Redirecionamento aceito ou lead segue para nutrição |
| 11. Mensagem principal | "Pelo que você descreveu, a [outro produto] pode combinar melhor com o que vocês procuram. Posso contar um pouco mais sobre ela?" |
| 12. Variação curta | (nutrição futura) reaproveitar T-NQ-ENCERRAR-01 com nota de reabertura futura, sem prometer nada agora |
| 13. Ativo recomendado | Nenhum nesta mensagem |
| 14. Ativo proibido | Qualquer, antes da aceitação |
| 15. CTA | Aceitar conhecer o outro produto |
| 16. Momento de envio | Quando o desencaixe é só de produto, não de perfil geral |
| 17. Quando usar | Desencaixe só de produto |
| 18. Quando não usar | Perfil incompatível com os dois produtos (usar T-NQ-PERFIL-01) |
| 19. Se responder | T-QL2-PRODUTO-01 (com o novo produto) |
| 20. Se não responder | T-NQ-ENCERRAR-01 |
| 21. Próximo template | T-QL2-POUSADA-01/CASA-01 |
| 22. Próxima ação | Aguardar aceite |
| 23. Follow-up | Não formalizado na Matriz — usar com cautela, sem cadência automática |
| 24. Registro mínimo no CRM | Observações curtas="redirecionado de [produto A] para [produto B]" |
| 25. Responsável | Rene/Nubia |
| 26. Precisa de Renildo? | Não |
| 27. Riscos | **Texto ainda não validado formalmente por Renildo — pendência aberta (ver seção 9, Governança)** |
| 28. Fontes oficiais | Nenhuma fonte oficial preexistente — texto novo desta proposta |
| 29. Status | Versão 1.0 — Piloto manual assistido (pendente de validação específica) |
| 30. Data de revisão | 05/08/2026 |

#### T-NQ-ENCERRAR-01

| Campo | Valor |
|---|---|
| 1. Código | T-NQ-ENCERRAR-01 |
| 2. Situação | Encerramento cordial padrão |
| 3. Produto | Não aplicável |
| 4. Origem | Qualquer |
| 5. QL | NQ |
| 6. C | C1 |
| 7. Estágio | Não avança — fecha o ciclo |
| 8. Objetivo | Fechar com cordialidade |
| 9. Emoção desejada | Respeito |
| 10. Resultado esperado | Ciclo formalmente encerrado |
| 11. Mensagem principal | "Ficamos à disposição se algo mudar. Um abraço!" |
| 12. Variação curta | Se pedirem ajuda para achar outra opção: "Posso indicar onde buscar mais opções na região de Bombinhas." — genérico, nunca citando concorrente |
| 13. Ativo recomendado | Nenhum |
| 14. Ativo proibido | Qualquer |
| 15. CTA | Nenhum |
| 16. Momento de envio | Fecha a sequência NQ |
| 17. Quando usar | Sempre após T-NQ-PERFIL-01 |
| 18. Quando não usar | Isoladamente, sem contexto NQ prévio |
| 19. Se responder | Não reabrir a conversa |
| 20. Se não responder | Não aplicável |
| 21. Próximo template | Nenhum |
| 22. Próxima ação | Nenhuma |
| 23. Follow-up | Nenhum |
| 24. Registro mínimo no CRM | Status final="Fora do perfil", Motivo de perda |
| 25. Responsável | Rene/Nubia |
| 26. Precisa de Renildo? | Não |
| 27. Riscos | Nunca citar concorrente pelo nome |
| 28. Fontes oficiais | Matriz (seção 8) + Funil (seção 10) |
| 29. Status | Versão 1.0 — Piloto manual assistido |
| 30. Data de revisão | 05/08/2026 |

### C3 — Negociação ou exceção sensível

#### T-C3-DESCONTO-01

| Campo | Valor |
|---|---|
| 1. Código | T-C3-DESCONTO-01 |
| 2. Situação | Pedido de desconto ou abatimento |
| 3. Produto | Qualquer |
| 4. Origem | Qualquer |
| 5. QL | Independente (qualquer QL pode gerar C3) |
| 6. C | C3 |
| 7. Estágio | Negociação/validação, quando há negociação real em curso; caso contrário, mantém o estágio atual da Oportunidade |
| 8. Objetivo | Registrar sem prometer, encaminhar para Renildo |
| 9. Emoção desejada | Acolhimento sem abrir expectativa |
| 10. Resultado esperado | Pedido registrado, Renildo decide |
| 11. Mensagem principal | "Entendo o pedido. O pedido será encaminhado para avaliação de Renildo." |
| 12. Variação curta | Nenhuma |
| 13. Ativo recomendado | Nenhum (nunca foto em C3) |
| 14. Ativo proibido | Qualquer |
| 15. CTA | Nenhum |
| 16. Momento de envio | Imediato |
| 17. Quando usar | Pedido de desconto/abatimento |
| 18. Quando não usar | Pergunta normal de preço (é C2, usar T-QL2-PRECO-01) |
| 19. Se responder | Aguarda decisão de Renildo |
| 20. Se não responder | Não aplicável |
| 21. Próximo template | Depende da decisão de Renildo |
| 22. Próxima ação | Renildo decide |
| 23. Follow-up | Não aplicável — fluxo de decisão interna |
| 24. Registro mínimo no CRM | C=C3, Precisa de Renildo?=Sim, Observações curtas com o pedido |
| 25. Responsável | Renildo decide; Rene/Nubia coletam e registram |
| 26. Precisa de Renildo? | Sim, sempre |
| 27. Riscos | Nunca ceder valor "pra segurar o lead" |
| 28. Fontes oficiais | Biblioteca (PC-C3-01) + Arquitetura (seção 5, seção 7) |
| 29. Status | Versão 1.0 — Piloto manual assistido |
| 30. Data de revisão | 05/08/2026 |

#### T-C3-CONDICAO-01

| Campo | Valor |
|---|---|
| 1. Código | T-C3-CONDICAO-01 |
| 2. Situação | Condição especial, crédito ou compensação |
| 3. Produto | Qualquer |
| 4. Origem | Qualquer |
| 5. QL | Independente |
| 6. C | C3 |
| 7. Estágio | Mesma regra de T-C3-DESCONTO-01 |
| 8. Objetivo | Registrar sem prometer |
| 9. Emoção desejada | Acolhimento |
| 10. Resultado esperado | Pedido registrado, Renildo decide |
| 11. Mensagem principal | "Entendo a situação. O pedido será encaminhado para avaliação de Renildo." |
| 12. Variação curta | Brinde/cortesia fora do padrão: mesmo texto, adaptando o motivo |
| 13. Ativo recomendado | Nenhum |
| 14. Ativo proibido | Qualquer |
| 15. CTA | Nenhum |
| 16. Momento de envio | Imediato |
| 17. Quando usar | Parcelamento fora do padrão, crédito, compensação, brinde não previsto |
| 18. Quando não usar | Parcelamento padrão já documentado (Biblioteca PC-EXT-20, factual, fora deste inventário) |
| 19. Se responder | Aguarda decisão |
| 20. Se não responder | Não aplicável |
| 21. Próximo template | Depende da decisão de Renildo |
| 22. Próxima ação | Renildo decide |
| 23. Follow-up | Não aplicável |
| 24. Registro mínimo no CRM | C=C3, Precisa de Renildo?=Sim |
| 25. Responsável | Renildo decide |
| 26. Precisa de Renildo? | Sim, sempre |
| 27. Riscos | Nunca prometer devolução/crédito/desconto |
| 28. Fontes oficiais | Biblioteca (PC-C3-02, PC-C3-03, PC-EXT-33) |
| 29. Status | Versão 1.0 — Piloto manual assistido |
| 30. Data de revisão | 05/08/2026 |

#### T-C3-NEGOCIACAO-01

| Campo | Valor |
|---|---|
| 1. Código | T-C3-NEGOCIACAO-01 |
| 2. Situação | Negociação sensível / ameaça de desistência por preço / comparação com concorrente |
| 3. Produto | Qualquer |
| 4. Origem | Qualquer |
| 5. QL | Tipicamente QL4 |
| 6. C | C3 |
| 7. Estágio | Negociação/validação, quando há negociação real em curso (aplicável quase sempre neste template) |
| 8. Objetivo | Encaminhar com agilidade sem ceder valor |
| 9. Emoção desejada | Urgência acolhida, sem ceder |
| 10. Resultado esperado | Caso levado a Renildo com prioridade |
| 11. Mensagem principal | "Entendo a posição de vocês. O pedido será encaminhado para avaliação de Renildo com prioridade." |
| 12. Variação curta | Comparação com OTA/outra pousada: usar Biblioteca PC-EXT-19 (pedir print, comparar condições; nunca igualar preço de concorrente) |
| 13. Ativo recomendado | Nenhum |
| 14. Ativo proibido | Qualquer |
| 15. CTA | Nenhum |
| 16. Momento de envio | Imediato |
| 17. Quando usar | Negociação de preço com pressão/ameaça de desistência |
| 18. Quando não usar | Se evoluir para pressão reputacional/conflito → reclassificar C4, usar T-C4-AMEACA-01 |
| 19. Se responder | Aguarda decisão de Renildo |
| 20. Se não responder | Não aplicável |
| 21. Próximo template | Depende da decisão de Renildo |
| 22. Próxima ação | Renildo decide com prioridade |
| 23. Follow-up | Não aplicável |
| 24. Registro mínimo no CRM | C=C3, Precisa de Renildo?=Sim, Observações curtas="negociação sensível — [motivo]" |
| 25. Responsável | Renildo decide |
| 26. Precisa de Renildo? | Sim, sempre |
| 27. Riscos | Se escalar para ameaça reputacional, reclassificar imediatamente para C4 |
| 28. Fontes oficiais | Biblioteca (PC-C3-04, PC-EXT-19) |
| 29. Status | Versão 1.0 — Piloto manual assistido |
| 30. Data de revisão | 05/08/2026 |

#### T-C3-EXCECAO-01

| Campo | Valor |
|---|---|
| 1. Código | T-C3-EXCECAO-01 |
| 2. Situação | Exceção de política (cancelamento, pet, horário) |
| 3. Produto | Qualquer |
| 4. Origem | Qualquer |
| 5. QL | Independente |
| 6. C | C3 |
| 7. Estágio | Mesma regra de T-C3-DESCONTO-01 |
| 8. Objetivo | Registrar sem confirmar exceção |
| 9. Emoção desejada | Acolhimento sem promessa |
| 10. Resultado esperado | Pedido registrado, Renildo decide |
| 11. Mensagem principal | "Entendo o pedido de exceção. O pedido será encaminhado para avaliação de Renildo." |
| 12. Variação curta | Cancelamento/remarcação por motivo pessoal: pedir produto, nome da reserva, datas, antecedência |
| 13. Ativo recomendado | Nenhum |
| 14. Ativo proibido | Qualquer |
| 15. CTA | Dados mínimos para avaliação |
| 16. Momento de envio | Imediato |
| 17. Quando usar | Pedido de exceção de política |
| 18. Quando não usar | Pedido dentro da política já documentada |
| 19. Se responder | Aguarda decisão de Renildo |
| 20. Se não responder | Não aplicável |
| 21. Próximo template | Depende da decisão de Renildo |
| 22. Próxima ação | Renildo decide |
| 23. Follow-up | Não aplicável |
| 24. Registro mínimo no CRM | C=C3, Precisa de Renildo?=Sim |
| 25. Responsável | Renildo decide |
| 26. Precisa de Renildo? | Sim, sempre |
| 27. Riscos | Nunca confirmar exceção antes da decisão |
| 28. Fontes oficiais | Biblioteca (PC-C3-05, PC-EXT-23) |
| 29. Status | Versão 1.0 — Piloto manual assistido |
| 30. Data de revisão | 05/08/2026 |

### C4 — Conflito ou risco grave

#### T-C4-AMEACA-01

| Campo | Valor |
|---|---|
| 1. Código | T-C4-AMEACA-01 |
| 2. Situação | Ameaça de avaliação negativa / pressão reputacional / cobrança ou dano contestado |
| 3. Produto | Qualquer |
| 4. Origem | Qualquer |
| 5. QL | Independente |
| 6. C | C4 |
| 7. Estágio | C4 não cria Estágio — manter o último Estágio conhecido; se não houver ciclo comercial ativo, usar registro operacional apropriado |
| 8. Objetivo | Conter sem ceder, sem discutir |
| 9. Emoção desejada | Acolhimento maduro, sem defensiva |
| 10. Resultado esperado | Caso escalado com prioridade máxima |
| 11. Mensagem principal | "Entendo que vocês estejam frustrados, e isso importa muito pra gente 🙏 Quero entender o que aconteceu para encaminhar da forma correta. Pode me contar com calma? O pedido será encaminhado para avaliação de Renildo com prioridade máxima." |
| 12. Variação curta | Avaliação já publicada: nunca pedir remoção/edição — só acolher e escalar |
| 13. Ativo recomendado | Nenhum (nunca foto em C4) |
| 14. Ativo proibido | Qualquer |
| 15. CTA | Nenhum — só pedir entendimento do ocorrido |
| 16. Momento de envio | Imediato, prioridade máxima |
| 17. Quando usar | Ameaça de avaliação negativa, condicionamento a compensação |
| 18. Quando não usar | Reclamação sem ameaça/pressão (é C3, usar T-C3-CONDICAO-01) |
| 19. Se responder | Renildo assume |
| 20. Se não responder | Escalar mesmo assim |
| 21. Próximo template | Nenhum — decisão de Renildo, fora deste documento |
| 22. Próxima ação | Escalar imediatamente |
| 23. Follow-up | Não aplicável — regra de prioridade máxima (Protocolo, seção 7) |
| 24. Registro mínimo no CRM | C=C4, Precisa de Renildo?=Sim, Observações curtas="Fluxo comercial interrompido por contenção C4" |
| 25. Responsável | Renildo decide |
| 26. Precisa de Renildo? | Sim, sempre, sem exceção |
| 27. Riscos | Nunca ceder valor por pressão; nunca mencionar a ameaça na resposta |
| 28. Fontes oficiais | Biblioteca (PC-EXT-27) + Protocolo (seção 7) |
| 29. Status | Versão 1.0 — Piloto manual assistido |
| 30. Data de revisão | 05/08/2026 |

#### T-C4-CONTENCAO-01

| Campo | Valor |
|---|---|
| 1. Código | T-C4-CONTENCAO-01 |
| 2. Situação | Reclamação grave / conflito / contenção geral, sem template específico |
| 3. Produto | Qualquer |
| 4. Origem | Qualquer |
| 5. QL | Independente |
| 6. C | C4 |
| 7. Estágio | Mesma regra de T-C4-AMEACA-01 |
| 8. Objetivo | Conter com o mínimo necessário, sem discutir mérito |
| 9. Emoção desejada | Seriedade e cuidado, sem promessa |
| 10. Resultado esperado | Caso registrado e escalado |
| 11. Mensagem principal | "Entendo a situação. O pedido será encaminhado para avaliação de Renildo." |
| 12. Variação curta | Se houver problema técnico associado: acionar solução operacional em paralelo, sem misturar com a decisão financeira |
| 13. Ativo recomendado | Nenhum |
| 14. Ativo proibido | Qualquer |
| 15. CTA | Uma pergunta objetiva permitida só se faltar dado indispensável, sem discutir mérito |
| 16. Momento de envio | Imediato |
| 17. Quando usar | Qualquer C4 sem cenário específico já coberto |
| 18. Quando não usar | Situação sem risco grave real (reavaliar como C2/C3) |
| 19. Se responder | Renildo assume |
| 20. Se não responder | Escalar mesmo assim |
| 21. Próximo template | Nenhum — fora do escopo deste documento |
| 22. Próxima ação | Escalar imediatamente |
| 23. Follow-up | Não aplicável |
| 24. Registro mínimo no CRM | C=C4, Precisa de Renildo?=Sim, Observações curtas="Fluxo comercial interrompido por contenção C4" |
| 25. Responsável | Renildo decide |
| 26. Precisa de Renildo? | Sim, sempre, sem exceção |
| 27. Riscos | Nunca discutir mérito, prometer prioridade, compensação ou responsabilidade; template ainda não testado em uso real |
| 28. Fontes oficiais | Biblioteca (PC-C4-06, PC-EXT-26) |
| 29. Status | Versão 1.0 — Piloto manual assistido |
| 30. Data de revisão | 05/08/2026 |

---

## 5. Anexo A — Primeiros 15 minutos

**Objetivo:** mostrar o que Rene/Nubia fazem desde a chegada do lead até o encaminhamento para orçamento. Não significa que toda conversa dura 15 minutos — é o primeiro ciclo de recepção e qualificação.

### Momento 0 — Lead entrou

**Observar:** Nome/identificação · Canal de origem · Campanha/anúncio · Produto conhecido ou indefinido · Dados já fornecidos · risco evidente.

**Registrar:** ID · Data de entrada · Nome/identificação · Canal de origem · Campanha/anúncio · Estágio = Novo.

**Imagem:** Nenhuma.

### Momento 1 — Primeira resposta

**Objetivo:** acolher; mostrar que a mensagem foi lida; pedir apenas o primeiro dado faltante. Normalmente: Datas.

**Imagem:** Nenhuma.

### Momento 2 — Segunda informação

Se Datas vieram: perguntar Pessoas. Se Pessoas vieram: perguntar Datas. **Nunca repetir dado informado.**

**Imagem:** Nenhuma.

### Momento 3 — Produto

Quando Datas e Pessoas estiverem conhecidas: confirmar Pousada ou Casa. Quando a campanha já identifica Produto, não perguntar de novo.

**Mensagem:** "Vocês estão considerando a Pousada Arágua ou a Casa Arágua Mariscal?"

**Para indecisão:** "A Pousada tem suítes e uma proposta mais acolhedora, com café da manhã servido na acomodação. A Casa é completa e privativa, com piscina para o grupo. Qual dessas opções combina mais com a viagem de vocês?"

**Imagem:** Nenhuma antes da identificação do Produto.

### Momento 4 — Primeira imagem

Só depois de Produto identificado e quando a imagem realmente ajudar.

**Pousada:** apresentação/desejo — AT-POU-PISCINA-01 · café — AT-POU-CAFE-01 · família — AT-POU-FAMILIA-01, somente depois de criança confirmada · identidade — AT-POU-FACHADA-01, nunca para instrução de chegada.

**Casa:** apresentação — AT-CAS-FACHADA-01 · privacidade/piscina — AT-CAS-PISCINA-01 · ambiente interno — AT-CAS-SALA-01.

**Bloqueados:** AT-POU-SUITE-01 · AT-CAS-CHURRASQUEIRA-01.

**Regras:** máximo 1 imagem por resposta · nunca álbum · nunca imagem em C3/C4 · nunca imagem apenas para pressionar.

### Momento 5 — Dados completos

QL4 exige: Produto + Datas + Número de pessoas + pedido de orçamento ou intenção clara de avançar.

**Mensagem:** "Vou deixar as informações organizadas para a equipe avaliar."

**Imagem:** Nenhuma.

**CRM:** QL = QL4 · C = C2 · Estágio = Orçamento · Orçamento enviado? = Não · Próxima ação = equipe verificar e preparar orçamento.

### Momento 6 — Esperar

Não insistir imediatamente · não transformar SLA interno em mensagem ao lead · follow-up somente depois do orçamento realmente enviado · atualizar Último contato e Próxima ação.

### Tabela resumida — Anexo A

| Momento | Situação | Template | Mensagem | Imagem | CTA | CRM | Próxima ação |
|---|---|---|---|---|---|---|---|
| 0 | Lead entrou | — (registro apenas) | — | Nenhuma | — | ID, Data de entrada, Nome/identificação, Canal de origem, Campanha/anúncio, Estágio=Novo | Observar próxima mensagem |
| 1 | Primeira resposta | T-QL1-ACOLHER-01 (ou variação de origem) | "Que bom receber seu contato 😊 Quais datas vocês estão pensando?" | Nenhuma | Datas | QL, Estágio=Novo | Aguardar Datas |
| 2 | Segunda informação | T-QL2-PESSOAS-01 | "E quantas pessoas estarão na viagem?" (ou inverso) | Nenhuma | Pessoas ou Datas | Datas e/ou Pessoas | Aguardar dado faltante |
| 3 | Produto | T-QL2-PRODUTO-01 | "Vocês estão considerando a Pousada Arágua ou a Casa Arágua Mariscal?" | Nenhuma | Escolha de produto | Datas, Pessoas | Aguardar escolha |
| 4 | Primeira imagem | T-QL3-ATIVO-01 (ou T-QL2-POUSADA-01/CASA-01) | Mensagem ideal do ativo escolhido (Guia) | Código oficial do Guia | Conforme ficha do ativo | Produto, Observações curtas | Observar reação |
| 5 | Dados completos | T-QL4-DADOS-01 | "Vou deixar as informações organizadas para a equipe avaliar." | Nenhuma | Nenhum | QL=QL4, C=C2, Estágio=Orçamento, Orçamento enviado?=Não | SLA interno da equipe |
| 6 | Esperar | T-QL4-FOLLOWUP-01 (só após orçamento real enviado) | Textos oficiais da Matriz | Nenhuma | Retomar decisão | Último contato, Próxima ação | Seguir Matriz |

---

## 6. Anexo B — Follow-up

**Fonte exclusiva:** `MATRIZ_FOLLOWUP_QL_WHATSAPP_VILLA_ARAGUA.md`. Nenhum prazo novo foi criado.

### QL1

**Condição:** contato inicial sem resposta.
**Mensagem oficial:** "Oi! Se um dia quiser conhecer mais sobre a Villa Arágua, estamos por aqui 🌿"
**Imagem:** Nenhuma.
**Estágio:** Aguardando retorno.
**Parar:** não repetir nova tentativa após o encerramento previsto na Matriz.

### QL2

**Condição:** pesquisa ativa; ainda faltam dois ou mais dados essenciais.
**Prazos oficiais da Matriz:** 3 dias · 7 dias, quando aplicável.
**Imagem:** normalmente nenhuma. Só pode entrar quando: Produto já está identificado; acrescenta informação útil; não repete ativo já enviado; a Matriz e o Guia permitirem. Nunca usar foto apenas para cobrar resposta.

### QL3

**Condição:** falta apenas um dado; existe dúvida objetiva.
**Prazos oficiais da Matriz:** 24h/48h · 3 dias, conforme a situação oficial.
**Mensagem:** deve pedir somente o dado faltante ou retomar a dúvida.
**Imagem:** somente quando responde a uma dúvida concreta. Exemplos: café → AT-POU-CAFE-01 · piscina Pousada → AT-POU-PISCINA-01 · piscina Casa → AT-CAS-PISCINA-01 · família → AT-POU-FAMILIA-01, com criança confirmada.

### QL4

**Condição:** Orçamento efetivamente enviado por humano.

**24h:** "Oi! Passando só pra saber se o orçamento chegou certinho pra você 😊" — **Imagem:** Nenhuma.
**48h:** "Oi! Ficou alguma dúvida sobre os valores ou sobre a estadia? Fico à disposição pra ajudar." — **Imagem:** Nenhuma.
**Encerramento:** "Oi! Ficamos à disposição se quiser retomar — é só chamar por aqui quando fizer sentido pra você 😊" — **Imagem:** Nenhuma.

**Regras:** Orçamento enviado? = Sim somente após envio real · silêncio mantém QL4 · Estágio = Aguardando retorno · seguir a Matriz para parar · nunca insistir depois do critério de encerramento.

### NQ

Não seguir cadência comercial · encerrar cordialmente · nenhum ativo · sem insistência.

### C3

Não seguir follow-up comercial comum · aguardar decisão de Renildo · nenhum ativo · não prometer condição.

### C4

Não entrar na cadência · contenção · escalar imediatamente · nenhum ativo · Renildo obrigatório.

### Tabela resumida — Anexo B

| QL/C | Condição | Prazo oficial | Mensagem | Imagem | CTA | Estágio | CRM | Quando parar |
|---|---|---|---|---|---|---|---|---|
| QL1 | Contato inicial sem resposta | Opcional, sem prazo fixo (7 dias) | "Oi! Se um dia quiser conhecer mais sobre a Villa Arágua, estamos por aqui 🌿" | Nenhuma | Nenhum | Aguardando retorno | Último contato | Após a tentativa opcional, não repetir |
| QL2 | Pesquisa ativa, faltam 2+ dados | 3 dias / 7 dias | "Oi! Ainda pensando em Mariscal? Fico à disposição se quiser saber mais 😊" (Matriz seção 6) | Depende da dúvida | Retomar dado | Aguardando retorno | Próximo follow-up | Sem encerramento formal — deixa em aberto |
| QL3 | Falta 1 dado ou dúvida objetiva | 24h/48h / 3 dias | "Oi! Ficou alguma dúvida sobre datas ou número de pessoas? Assim que tiver esses detalhes, sigo com o orçamento 😊" (Matriz seção 5, adaptado) | Depende da dúvida | Dado faltante | Aguardando retorno | Próximo follow-up | Se não completar dados após 2-3 tentativas |
| QL4 (24h) | Orçamento enviado, sem resposta | 24h | "Oi! Passando só pra saber se o orçamento chegou certinho pra você 😊" | Nenhuma | Retomar decisão | Aguardando retorno | Próximo follow-up | — |
| QL4 (48h) | Sem resposta após 24h | 48h | "Oi! Ficou alguma dúvida sobre os valores ou sobre a estadia? Fico à disposição pra ajudar." | Nenhuma | Retomar decisão | Aguardando retorno | Próximo follow-up | — |
| QL4 (encerramento) | Sem resposta após 48h | Após tentativa comercial sem resposta | "Oi! Ficamos à disposição se quiser retomar — é só chamar por aqui quando fizer sentido pra você 😊" | Nenhuma | Nenhum | Aguardando retorno | Status final=vazio até decisão humana | Critério de parada da Matriz (seção 12) |
| NQ | Fora do perfil | Imediato | Textos da Matriz seção 8 | Nenhuma | Nenhum | Não avança | Status final="Fora do perfil" | Imediato, na primeira resposta |
| C3 | Desconto/exceção/negociação | Não aplicável | "O pedido será encaminhado para avaliação de Renildo." | Nenhuma | Nenhum | Negociação/validação* ou mantém atual | Precisa de Renildo?=Sim | Aguardar decisão de Renildo |
| C4 | Conflito/risco grave | Não aplicável | "Entendo a situação. O pedido será encaminhado para avaliação de Renildo." | Nenhuma | Nenhum | Mantém último conhecido | Contenção C4, Renildo=Sim | Escalar imediatamente, sem cadência |

---

## 7. Matriz rápida

*15 casos mais comuns, com coluna Imagem explícita (vocabulário: código oficial do Guia / Nenhuma / Depende da dúvida).*

| Situação | Código | QL | C | Estágio | Mensagem | Imagem | Próxima ação | Follow-up | Renildo? | Registro mínimo |
|---|---|---|---|---|---|---|---|---|---|---|
| Abertura "Oi" | T-QL1-ACOLHER-01 | QL1 | C2 | Novo | "Quais datas vocês estão pensando?" | Nenhuma | Aguardar Datas | QL1 opcional | Não | QL, Estágio |
| Meta Ads Pousada/Casa | T-QL1-ORIGEM-POUSADA-01 / T-QL1-ORIGEM-CASA-01 | QL1 | C2 | Novo | Confirma origem + pede Datas | Nenhuma | Aguardar Datas | QL1 opcional | Não | Produto, Campanha |
| Pergunta de preço | T-QL2-PRECO-01 | QL2 | C2 | Em qualificação | "O valor depende do período..." | Nenhuma | Aguardar próximo dado | 3 dias/7 dias | Não | QL, C |
| Datas↔pessoas | T-QL2-PESSOAS-01 | QL2 | C2 | Em qualificação | Pede o dado faltante | Nenhuma | Aguardar dado | 3 dias/7 dias | Não | Datas/Pessoas |
| Identificar produto | T-QL2-PRODUTO-01 | QL2 | C2 | Em qualificação | "Pousada ou Casa?" | Nenhuma | Aguardar escolha | 24-48h/3 dias | Não | Datas, Pessoas |
| Pousada/Casa identificada | T-QL2-POUSADA-01 / T-QL2-CASA-01 | QL2 | C2 | Em qualificação | Apresenta + pede dado | Depende da dúvida | Aguardar dado | Matriz 10.1/10.2 | Não | Produto |
| Falta 1 dado (QL3) | T-QL3-DADO-01 | QL3 | C2 | Em qualificação | Pede o dado exato | Depende da dúvida | Aguardar dado | 24-48h/3 dias | Não | Próxima ação |
| 1º ativo enviado | T-QL3-ATIVO-01 | QL3 | C2 | Em qualificação | Mensagem ideal do Guia | AT-POU-PISCINA-01 / AT-CAS-PISCINA-01 | Observar reação | Matriz QL3 | Não | Observações |
| Dados completos | T-QL4-DADOS-01 | QL4 | C2 | Orçamento | "Vou deixar as informações organizadas..." | Nenhuma | SLA interno equipe | — | Não | Orçamento enviado?=Não |
| Orçamento enviado | T-QL4-ORCAMENTO-01 | QL4 | C2 | Orçamento | Confirmação de recebimento | Nenhuma | Aguardar reação | 24h | Não | Orçamento enviado?=Sim |
| Follow-up 24h/48h | T-QL4-FOLLOWUP-01 | QL4 | C2 | Aguardando retorno | Texto oficial da Matriz | Nenhuma | Aguardar resposta | Matriz seção 4 | Não | Próximo follow-up |
| Pedido de reserva | T-QL4-RESERVA-01 | QL4 | C2 | Negociação/validação | Orienta próximo passo | Nenhuma | Aguardar validação | Matriz seção 4 | Depende | Estágio |
| Desconto | T-C3-DESCONTO-01 | Independente | C3 | Negociação/validação* | "O pedido será encaminhado para avaliação de Renildo." | Nenhuma | Renildo decide | Não aplicável | Sim | C=C3 |
| Ameaça | T-C4-AMEACA-01 | Independente | C4 | Mantém último conhecido | Acolhe + escala com prioridade máxima | Nenhuma | Escalar imediato | Não aplicável | Sim | Contenção C4 |
| Contenção geral (C4) | T-C4-CONTENCAO-01 | Independente | C4 | Mantém último conhecido | "Entendo a situação..." | Nenhuma | Escalar imediato | Não aplicável | Sim | Contenção C4 |

*Demais 20 templates seguem o mesmo padrão — ver fichas completas (seção 4) e Uso Rápido (seção 3).*

---

## 8. Testes simulados

*24 testes já consolidados, mais 11 testes adicionais desta rodada (Meta Ads completo, follow-up por QL, imagem correta/cedo demais, ativo bloqueado, C3/C4 sem imagem) — total 35, dentro do limite pedido.*

| # | Mensagem/situação | Dados conhecidos | Dado faltante | QL | C | Estágio | Template | Imagem | CRM | Próxima ação | Decisão final |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | "Oi" | Nenhum | Datas | QL1 | C2 | Novo | T-QL1-ACOLHER-01 | Nenhuma | QL, Estágio | Aguardar Datas | Rene envia direto |
| 2 | Clica anúncio Pousada | Produto (via campanha) | Datas | QL1 | C2 | Novo | T-QL1-ORIGEM-POUSADA-01 | Nenhuma | Produto, Campanha | Aguardar Datas | Rene envia direto |
| 3 | Clica anúncio Casa | Produto (via campanha) | Datas | QL1 | C2 | Novo | T-QL1-ORIGEM-CASA-01 | Nenhuma | Produto, Campanha | Aguardar Datas | Rene envia direto |
| 4 | "Quanto é a diária?" | Nenhum | Datas | QL2 | C2 | Em qualificação | T-QL2-PRECO-01 | Nenhuma | QL, C | Aguardar Datas | Rene envia direto |
| 5 | "15 a 20/12" | Datas | Pessoas | QL2 | C2 | Em qualificação | T-QL2-PESSOAS-01 | Nenhuma | Datas | Aguardar Pessoas | Rene envia direto |
| 6 | "Somos 4" | Pessoas | Datas | QL2 | C2 | Em qualificação | T-QL2-PESSOAS-01 (variação) | Nenhuma | Pessoas | Aguardar Datas | Rene envia direto |
| 7 | Datas+Pessoas dados, Produto não | Datas, Pessoas | Produto | QL3 | C2 | Em qualificação | T-QL2-PRODUTO-01 / T-QL3-DADO-01 | Nenhuma | Datas, Pessoas | Aguardar Produto (obrigatória) | Rene envia direto |
| 8 | "Queremos a Pousada" | Produto=Pousada | Datas/Pessoas | QL2 | C2 | Em qualificação | T-QL2-POUSADA-01 | AT-POU-PISCINA-01 (opcional) | Produto | Aguardar dado | Rene envia direto |
| 9 | "Queremos a Casa" | Produto=Casa | Datas/Pessoas | QL2 | C2 | Em qualificação | T-QL2-CASA-01 | AT-CAS-FACHADA-01 (opcional) | Produto | Aguardar dado | Rene envia direto |
| 10 | "Manda foto?" (sem produto) | Nenhum | Datas | QL1 | C2 | Novo | T-QL1-FOTO-01 | Nenhuma | Observações | Aguardar Datas | Rene envia direto — nunca ativo antes de Produto |
| 11 | "Vamos com nossa filha de 6 anos" | Criança | — | QL2 | C2 | Em qualificação | T-QL2-CRIANCA-01 | AT-POU-FAMILIA-01 (após confirmação) | Observações | Aguardar composição | Rene envia direto |
| 12 | "Vamos com um cachorro pequeno" | Pet | Confirmação porte único | QL2 | C2 | Em qualificação | T-QL2-PET-01 | Nenhuma | Observações | Aguardar detalhe | Rene envia direto |
| 13 | Produto+Datas+Pessoas + "quero orçamento" | Os 3 dados | Nenhum | QL4 | C2 | Orçamento | T-QL4-DADOS-01 | Nenhuma | Orçamento enviado?=Não | SLA interno equipe | Rene envia direto |
| 14 | "Qual seria o valor certinho?" (dados completos) | Os 3 dados | Nenhum | QL4 | C2 | Orçamento | T-QL4-DADOS-01 | Nenhuma | Orçamento enviado?=Não | Equipe prepara | Rene envia direto |
| 15 | Orçamento enviado pela equipe | Os 3 dados + valor | Nenhum | QL4 | C2 | Orçamento | T-QL4-ORCAMENTO-01 | Nenhuma | Orçamento enviado?=Sim | Aguardar reação | Rene registra no CRM |
| 16 | Silêncio 48h pós-orçamento | Os 3 dados + valor | Resposta do lead | QL4 (mantém) | C2 | Aguardando retorno | T-QL4-FOLLOWUP-01 / T-QL4-ENCERRAR-01 | Nenhuma | Próximo follow-up | Seguir Matriz | Rene envia follow-up oficial |
| 17 | "Fazem desconto à vista?" | Variável | Variável | Independente | C3 | Negociação/validação* | T-C3-DESCONTO-01 | Nenhuma | C=C3, Renildo=Sim | Renildo decide | Escala para Renildo |
| 18 | "Preciso cancelar, tem exceção?" | Variável | Variável | Independente | C3 | Mantém atual | T-C3-EXCECAO-01 | Nenhuma | C=C3, Renildo=Sim | Renildo decide | Escala para Renildo |
| 19 | "O quarto veio sujo, quero satisfação" | Variável | Variável | Independente | C4 | Mantém último conhecido | T-C4-CONTENCAO-01 | Nenhuma | Contenção C4, Renildo=Sim | Escalar imediato | Escala para Renildo, prioridade máxima |
| 20 | "Se não resolverem, vou avaliar mal no Google" | Variável | Variável | Independente | C4 | Mantém último conhecido | T-C4-AMEACA-01 | Nenhuma | Contenção C4, Renildo=Sim | Escalar imediato | Escala para Renildo, prioridade máxima |
| 21 | Lead pede foto da Casa, mas produto confirmado é Pousada | Produto=Pousada | — | QL3 | C2 | Em qualificação | T-QL3-ATIVO-01 (variação Pousada) | AT-POU-PISCINA-01 | Observações | Esclarecer | Rene corrige e usa ativo da Pousada, nunca da Casa |
| 22 | "Manda foto" logo na 1ª mensagem, sem produto | Nenhum | Datas | QL1 | C2 | Novo | T-QL1-FOTO-01 | Nenhuma | Observações | Aguardar Datas | Rene não envia foto — cedo demais |
| 23 | Lead pede foto da Suíte Metallo especificamente | Produto=Pousada | — | QL3 | C2 | Em qualificação | T-QL3-ATIVO-01 | Nenhuma — AT-POU-SUITE-01 bloqueado | Observações | Explicar indisponibilidade do ativo | Rene não envia; sugere outro ativo Pousada |
| 24 | "Vocês fazem festa de 15 anos?" | Não aplicável | — | NQ | C1 | Novo | T-NQ-PERFIL-01 → T-NQ-ENCERRAR-01 | Nenhuma | Status final | Nenhum | Rene envia e encerra |
| 25 | Primeiro ciclo completo Meta Ads Pousada (Oi → Datas → Pessoas → Produto já sabido → 1ª imagem → dados completos) | Progressivo | Progressivo | QL1→QL4 | C2 | Novo→Orçamento | T-QL1-ORIGEM-POUSADA-01 → T-QL2-PESSOAS-01 → T-QL3-ATIVO-01 → T-QL4-DADOS-01 | AT-POU-PISCINA-01 (só no momento 4) | Progressivo, conforme Anexo A | Progressivo | Rene conduz o ciclo completo em 4 mensagens, sem repetir dado |
| 26 | Primeiro ciclo completo Meta Ads Casa (mesmo fluxo, produto Casa) | Progressivo | Progressivo | QL1→QL4 | C2 | Novo→Orçamento | T-QL1-ORIGEM-CASA-01 → T-QL2-PESSOAS-01 → T-QL3-ATIVO-01 → T-QL4-DADOS-01 | AT-CAS-PISCINA-01 (só no momento 4) | Progressivo | Progressivo | Rene conduz o ciclo completo, sem repetir dado |
| 27 | Follow-up QL1 (7 dias, sem resposta) | Nenhum | — | QL1 | C1 | Aguardando retorno | T-QL1-SILENCIO-01 | Nenhuma | Último contato | Não repetir novo follow-up | Rene envia único follow-up opcional |
| 28 | Follow-up QL2 (3 dias, sem resposta) | Parcial | — | QL2 | C2 | Aguardando retorno | Texto Matriz seção 6 | Depende da dúvida | Próximo follow-up | Seguir para 7 dias | Rene envia follow-up oficial |
| 29 | Follow-up QL3 (24-48h, sem resposta) | 2 de 3 dados | Dado faltante | QL3 | C2 | Aguardando retorno | Texto Matriz seção 5 | Depende da dúvida | Próximo follow-up | Seguir para 3 dias | Rene envia follow-up oficial |
| 30 | Follow-up QL4 24h (orçamento sem resposta) | Os 3 dados + valor | — | QL4 | C2 | Aguardando retorno | T-QL4-FOLLOWUP-01 | Nenhuma | Próximo follow-up | Seguir para 48h | Rene envia texto oficial da Matriz |
| 31 | Follow-up QL4 48h (ainda sem resposta) | Os 3 dados + valor | — | QL4 | C2 | Aguardando retorno | T-QL4-FOLLOWUP-01 (variação) | Nenhuma | Próximo follow-up | Seguir para encerramento | Rene envia texto oficial da Matriz |
| 32 | Imagem correta (piscina Pousada, produto e dúvida confirmados) | Produto, dúvida sobre piscina | — | QL3 | C1/C2 | Em qualificação | T-QL3-ESTRUTURA-01 | AT-POU-PISCINA-01 | Observações | Retomar dado | Rene envia — uso correto, 1 imagem, dúvida real |
| 33 | Imagem cedo demais (pede foto antes de qualquer dado) | Nenhum | Datas | QL1 | C2 | Novo | T-QL1-FOTO-01 | Nenhuma (recusa educada de enviar cedo) | Observações | Aguardar Datas | Rene não envia imagem — regra "1º contato normalmente sem foto" |
| 34 | Ativo bloqueado (lead pede especificamente a Suíte Metallo em foto) | Produto=Pousada | — | QL3/QL4 | C2 | Em qualificação/Orçamento | T-QL3-ATIVO-01 ou T-QL4-DUVIDA-01 | Nenhuma — AT-POU-SUITE-01 bloqueado | Observações | Sugerir alternativa | Rene explica indisponibilidade do ativo, sugere outro |
| 35 | C3 sem imagem (pedido de desconto acompanhado de pedido de foto) | Variável | — | Independente | C3 | Negociação/validação* | T-C3-DESCONTO-01 | Nenhuma — nunca foto em C3 | C=C3, Renildo=Sim | Renildo decide | Rene não envia imagem, só registra e escala |

---

## 9. Governança

- A Arquitetura define C.
- O Funil define QL.
- O CRM define Estágio e campos.
- O Guia define ativos.
- A Matriz define cadência.
- A Biblioteca fornece conteúdo-base.
- Este documento organiza a execução — não redefine nenhum dos itens acima.
- Nenhum agente ou skill cria template oficial sozinho.
- A Recepcionista IA consulta este documento.
- A Recepcionista IA nunca envia.
- Aprendizagem só persiste após evidência, revisão e aprovação de Renildo.
- Alterações exigem changelog.

**Pendência de governança aberta:** `T-NQ-REDIRECIONAR-01` usa texto sem precedente em nenhuma fonte oficial — permanece em uso no piloto, mas sinalizado como pendente de validação específica de Renildo.

---

## 10. Checklist final

- [x] Manifesto rápido presente.
- [x] Fluxo resumido presente.
- [x] Uso Rápido presente.
- [x] 35 Templates presentes.
- [x] Anexo A — Primeiros 15 minutos presente.
- [x] Anexo B — Follow-up presente.
- [x] Matriz rápida presente.
- [x] Testes presentes.
- [x] Governança presente.
- [x] Checklist presente.
- [x] CRM usa 20 campos oficiais.
- [x] QL usa o Funil atual.
- [x] C usa a Arquitetura.
- [x] Estágios são apenas os 8 oficiais.
- [x] Cadência vem exclusivamente da Matriz.
- [x] AT-POU-SUITE-01 bloqueado.
- [x] AT-CAS-CHURRASQUEIRA-01 bloqueado.
- [x] Primeiro contato normalmente sem foto.
- [x] Nunca foto em C3/C4.
- [x] Nenhuma mensagem automática.
- [x] Nenhum outro arquivo alterado.

---

## 11. Changelog

- **05/08/2026 — Claude (a pedido de Renildo):** criação oficial deste documento, primeira versão (Versão 1.0 — Piloto manual assistido). Reúne, em arquivo único, o Manifesto rápido de uso, o Fluxo resumido, o Uso Rápido (30 casos), os 35 Templates Operacionais QL/C completos (30 campos cada), o Anexo A (Primeiros 15 minutos), o Anexo B (Follow-up, por QL/C), a Matriz Rápida (15 casos mais comuns, com coluna Imagem), 35 testes simulados e a seção de Governança. Conteúdo baseado integralmente na proposta consolidada já aprovada nesta mesma rodada de trabalho, sem reabrir nenhum conceito da Arquitetura, do Funil, do CRM, do Guia, da Matriz ou da Biblioteca. Nenhum outro arquivo do projeto foi alterado nesta rodada.
- **06/08/2026 — Claude (a pedido de Renildo):** consolidação da regra de primeira mensagem de campanha (Auditoria do Piloto Comercial Real de 06/08/2026, frente B). Resumo: (1) fichas `T-QL1-ORIGEM-POUSADA-01` e `T-QL1-ORIGEM-CASA-01` (seção 4) passaram a cobrir dois casos — campanha só com Produto (mensagem original, mantida) e campanha também com Período/datas (novo, campo 12 "Variação curta"), com o texto oficial aprovado por Renildo: "Olá! 😊 Claro! Vi que você veio pela nossa campanha do feriado de 7 de Setembro, de 04 a 08/09. Me conta só quantas pessoas estarão na viagem e se haverá alguma criança?"; campos 2, 8, 9 (parcial), 10, 15, 17, 18, 19, 21, 22, 24, 27 e 30 ajustados para refletir os dois casos, sem alterar QL, C ou Estágio; (2) seção 3 (Uso Rápido) — as duas linhas "Meta Ads Pousada/Casa" desdobradas em quatro (com/sem período conhecido), marcadas com "†" e nova nota de rodapé explicando a regra; (3) nenhum valor ou pacote do 7 de Setembro foi transformado em template estrutural — o texto de exemplo usa a campanha do 7 de Setembro apenas como ilustração da regra geral de não repetir dado já conhecido pela origem, aplicável a qualquer campanha futura com período definido. Nenhuma outra seção deste documento foi alterada — QL, C, Estágio, ativos e cadência continuam vindo exclusivamente do Funil, da Arquitetura, do Guia e da Matriz, sem redefinição aqui. Backup criado em `BACKUP_ANTES_PROPAGACAO_C1C4_PRIMEIRA_MENSAGEM_2026-08-06/` antes da edição.
