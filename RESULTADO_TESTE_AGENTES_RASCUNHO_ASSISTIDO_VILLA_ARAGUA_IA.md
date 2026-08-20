# RESULTADO DO TESTE DOS AGENTES — RASCUNHO ASSISTIDO VILLA ARÁGUA IA

**Versão:** v1 — execução conceitual
**Base:** `TESTE_AGENTES_RASCUNHO_ASSISTIDO_VILLA_ARAGUA_IA.md`
**Consultados sem alteração:** `MATRIZ_ROTEAMENTO_AGENTES_VILLA_ARAGUA.md`, `DEFINICAO_AGENTES_VILLA_ARAGUA_IA.md`, `BIBLIOTECA_OFICIAL_RECEPCIONISTA_IA_VILLA_ARAGUA.md`, `BIBLIOTECA_COMERCIAL_RECEPCIONISTA_IA_VILLA_ARAGUA.md`, `DADOS_OFICIAIS_ATENDIMENTO_VILLA_ARAGUA.md`, `MODO_RASCUNHO_ASSISTIDO_VILLA_ARAGUA.md`, `PROTOCOLO_USO_DIARIO_RASCUNHO_ASSISTIDO_VILLA_ARAGUA.md`
**Modo:** Rascunho Assistido — execução conceitual, sem automação, sem agente executável, sem conexão real.

---

## Nota sobre o método

Esta execução é uma simulação: cada um dos 42 casos foi reprocessado a partir da mensagem original, aplicando a Matriz de Roteamento e a Definição dos Agentes como se fossem consultadas pela primeira vez, e comparando o resultado obtido com o resultado esperado já registrado no arquivo de teste. Onde o resultado obtido bate integralmente com o esperado, isso é declarado de forma direta. Onde a reanálise encontrou uma divergência, ambiguidade ou lacuna real — mesmo que sutil —, isso é registrado como ressalva, falha ou lacuna, em vez de forçar aprovação plena.

---

## Casos comerciais

### Caso C-01

**Mensagem testada:**
> "Oi! Vocês ficam perto da praia?"

**Resultado esperado no arquivo de teste:** C1, Comercial/Reservas, sem escalação a Renildo, rascunho sim.

**Resultado obtido na simulação:**
- Trilha: Comercial
- Nível: C1
- Agente principal: Comercial / Reservas
- Agentes de apoio: —
- Risco: baixo
- Arquivos consultados: `BIBLIOTECA_COMERCIAL_RECEPCIONISTA_IA_VILLA_ARAGUA.md` (PC-C1-04), `DADOS_OFICIAIS_ATENDIMENTO_VILLA_ARAGUA.md` (item 2)
- Skills consultadas: `villa-aragua-sales-receptionist`
- Rascunho permitido: Sim
- Escalação indicada: Rene/Nubia revisam; Renildo não necessário

**Avaliação:** Classificação correta: Sim | Agente correto: Sim | Fontes corretas: Sim | Escalação correta: Sim | Rascunho seguro: Sim | **Resultado do caso: Aprovado**

**Justificativa:** Resultado idêntico ao esperado. PC-C1-04 cobre exatamente esta pergunta sem risco de prometer frente-mar.

**Falha ou risco encontrado:** Nenhum.
**Ajuste recomendado:** Nenhum.

---

### Caso C-02

**Mensagem testada:**
> "Tem piscina?"

**Resultado esperado:** C1, Comercial/Reservas, rascunho sim.

**Resultado obtido:** Trilha Comercial, Nível C1, Agente Comercial/Reservas, Risco baixo, Arquivos: `BIBLIOTECA_COMERCIAL...` (PC-C1-02), `DADOS_OFICIAIS...`, Skills: `villa-aragua-sales-receptionist`, Rascunho permitido, Escalação: Rene/Nubia revisam.

**Avaliação:** Classificação correta: Sim | Agente correto: Sim | Fontes corretas: Sim | Escalação correta: Sim | Rascunho seguro: Sim | **Resultado do caso: Aprovado**

**Justificativa:** Idêntico ao esperado.
**Falha ou risco encontrado:** Nenhum.
**Ajuste recomendado:** Nenhum.

---

### Caso C-03

**Mensagem testada:**
> "Vocês têm vaga para este fim de semana, casal?"

**Resultado esperado:** C3, Comercial/Reservas + Apoio à Decisão Comercial, rascunho com ressalva.

**Resultado obtido:** Trilha Comercial, Nível C3, Agente Comercial/Reservas + Apoio à Decisão Comercial, Risco médio, Arquivos: `BIBLIOTECA_COMERCIAL...` (PC-C3-02), Skills: `villa-aragua-sales-receptionist`, Rascunho com ressalva (sem confirmar disponibilidade), Escalação: Renildo confirma.

**Avaliação:** Classificação correta: Sim | Agente correto: Sim | Fontes corretas: Sim | Escalação correta: Sim | Rascunho seguro: Sim | **Resultado do caso: Aprovado**

**Justificativa:** Idêntico ao esperado.
**Falha ou risco encontrado:** Nenhum.
**Ajuste recomendado:** Nenhum.

---

### Caso C-04

**Mensagem testada:**
> "Somos 4 pessoas, tem opção para janeiro?"

**Resultado esperado:** C2 + C3 (mista), Comercial/Reservas + Apoio à Decisão Comercial, rascunho com ressalva.

**Resultado obtido:** Trilha Comercial (mista), Nível C2+C3, Agente Comercial/Reservas + Apoio à Decisão Comercial, Risco médio, Arquivos: `BIBLIOTECA_COMERCIAL...` (PC-C2-02, PC-C3-02), `MATRIZ_ROTEAMENTO...` (seção 6), Skills: `villa-aragua-sales-receptionist`, Rascunho: diagnóstico sim, disponibilidade só contenção, Escalação: Renildo confirma a parte de disponibilidade.

**Avaliação:** Classificação correta: Sim | Agente correto: Sim | Fontes corretas: Sim | Escalação correta: Sim | Rascunho seguro: Sim | **Resultado do caso: Aprovado**

**Justificativa:** A reanálise confirma que a mensagem precisa mesmo ser tratada como mista — a Matriz (seção 6) já documenta este exato padrão como regra geral, o que reforça a consistência.

**Falha ou risco encontrado:** Nenhum específico deste caso — ver nota estrutural na seção "Falhas e inconsistências entre documentos" ao final, sobre como o humano deve costurar as duas partes da resposta.
**Ajuste recomendado:** Ver nota estrutural ao final.

---

### Caso C-05

**Mensagem testada:**
> "Queremos a Casa Arágua pro Réveillon, tem como?"

**Resultado esperado:** C3, Comercial/Reservas + Apoio à Decisão Comercial, apenas contenção, Renildo sempre.

**Resultado obtido:** Trilha Comercial, Nível C3, Agente Comercial/Reservas + Apoio à Decisão Comercial, Risco alto, Arquivos: `BIBLIOTECA_COMERCIAL...` (PC-C3-04), Skills: `villa-aragua-sales-receptionist`, `villa-aragua-pricing-revenue`, Rascunho apenas contenção, Escalação: Renildo sempre (Casa Arágua + alta temporada, regra da Matriz seção 8).

**Avaliação:** Classificação correta: Sim | Agente correto: Sim | Fontes corretas: Sim | Escalação correta: Sim | Rascunho seguro: Sim | **Resultado do caso: Aprovado**

**Justificativa:** Idêntico ao esperado; a escalação a Renildo é justificada tanto pela regra "Casa Arágua em negociação importante" quanto por "Alta temporada sensível" da Matriz.
**Falha ou risco encontrado:** Nenhum.
**Ajuste recomendado:** Nenhum.

---

### Caso C-06

**Mensagem testada:**
> "Quanto custa a diária?"

**Resultado esperado:** C3, Comercial/Reservas + Apoio à Decisão Comercial, rascunho com ressalva.

**Resultado obtido:** idêntico ao esperado — PC-C3-01, nenhum valor citado, Renildo confirma.

**Avaliação:** Todos os critérios: Sim | **Resultado do caso: Aprovado**
**Falha ou risco encontrado:** Nenhum.
**Ajuste recomendado:** Nenhum.

---

### Caso C-07

**Mensagem testada:**
> "Fecha com desconto?"

**Resultado esperado:** C4, Comercial/Reservas + Risco + Apoio à Decisão Comercial, apenas contenção, Renildo obrigatório.

**Resultado obtido:** idêntico ao esperado — PC-C4-01, nenhum percentual sugerido.

**Avaliação:** Todos os critérios: Sim | **Resultado do caso: Aprovado**
**Falha ou risco encontrado:** Nenhum.
**Ajuste recomendado:** Nenhum.

---

### Caso C-08

**Mensagem testada:**
> "Vi no Airbnb bem mais barato, vocês conseguem chegar perto disso?"

**Resultado esperado:** C4, apenas contenção, Renildo obrigatório.

**Resultado obtido:** idêntico ao esperado — PC-C4-04 ("C4 sensível com prioridade comercial"), sem comparar preço.

**Avaliação:** Todos os critérios: Sim | **Resultado do caso: Aprovado**
**Falha ou risco encontrado:** Nenhum.
**Ajuste recomendado:** Nenhum.

---

### Caso C-09

**Mensagem testada:**
> "Manda foto da Suíte Organic?"

**Resultado esperado:** C1, rascunho sim.

**Resultado obtido:** idêntico ao esperado — PC-C1-05, humano envia a foto, IA nunca diz "estou enviando".

**Avaliação:** Todos os critérios: Sim | **Resultado do caso: Aprovado**
**Falha ou risco encontrado:** Nenhum.
**Ajuste recomendado:** Nenhum.

---

### Caso C-10

**Mensagem testada:**
> "Qual a diferença entre a Pousada e a Casa Arágua?"

**Resultado esperado:** C1, rascunho sim.

**Resultado obtido:** idêntico ao esperado — PC-C1-01.

**Avaliação:** Todos os critérios: Sim | **Resultado do caso: Aprovado**
**Falha ou risco encontrado:** Nenhum.
**Ajuste recomendado:** Nenhum.

---

### Caso C-11

**Mensagem testada:**
> "Vi o anúncio de vocês no Instagram, me conta mais?"

**Resultado esperado:** C2 (abertura), rascunho sim.

**Resultado obtido:** idêntico ao esperado — PC-C2-01, coleta datas/pessoas/crianças/pet antes de sugerir qualquer acomodação.

**Avaliação:** Todos os critérios: Sim | **Resultado do caso: Aprovado**
**Falha ou risco encontrado:** Nenhum.
**Ajuste recomendado:** Nenhum.

---

### Caso C-12

**Mensagem testada:**
> "Pode reservar pra mim agora, depois eu pago."

**Resultado esperado:** C4, apenas contenção, Renildo se envolver condição fora do padrão.

**Resultado obtido:** Trilha Comercial, Nível C4, Agente Comercial/Reservas + Risco/Escalação, Risco alto, Arquivos: `MODO_RASCUNHO_ASSISTIDO_VILLA_ARAGUA.md`, `DEFINICAO_AGENTES_VILLA_ARAGUA_IA.md` (seção 2), Skills: `villa-aragua-sales-receptionist`, Rascunho apenas contenção, Escalação: Rene conduz o processo padrão, Renildo se houver condição fora do padrão.

**Avaliação:** Classificação correta: Parcial | Agente correto: Sim | Fontes corretas: Parcial | Escalação correta: Sim | Rascunho seguro: Sim | **Resultado do caso: Aprovado com ressalva**

**Justificativa:** O comportamento esperado (nunca confirmar reserva) está correto e é coberto pela regra máxima (seção 2 de `DEFINICAO_AGENTES...`). Mas, ao reprocessar, não existe um template C1–C4 que descreva exatamente este caso — "pedido de reserva sem sinal/confirmação" não é bem coberto por PC-C4-01 (desconto) nem PC-C4-04 (negociação); o mais próximo é PC-C4-02 (condição especial/parcelamento fora do padrão), usado por analogia, não por correspondência direta.

**Falha ou risco encontrado:** A Biblioteca Comercial não tem um template dedicado para "tentativa de pular a etapa de confirmação/pagamento da reserva" — hoje esse caso só é resolvido pela regra máxima geral, não por um template específico.

**Ajuste recomendado:** Considerar, numa v2 da Biblioteca Comercial, um template específico em C4 (ou uma nova observação em C2) para "pedido de reserva sem sinal/confirmação", deixando explícito que a IA sempre remete ao processo padrão da equipe. Prioridade: **baixa** — o comportamento de segurança já está garantido pela regra máxima, isso é só uma lacuna de cobertura de template.

---

## Casos operacionais

### Caso O-01

**Mensagem testada:**
> "Qual a senha do Wi-Fi?"

**Resultado esperado:** N1, rascunho sim.
**Resultado obtido:** idêntico — confirma acomodação antes de informar a senha.
**Avaliação:** Todos os critérios: Sim | **Resultado do caso: Aprovado**
**Falha ou risco encontrado:** Nenhum. **Ajuste recomendado:** Nenhum.

---

### Caso O-02

**Mensagem testada:**
> "Que horas é o check-out?"

**Resultado esperado:** N1, rascunho sim.
**Resultado obtido:** idêntico — horário oficial 8h–11h, sem invenção.
**Avaliação:** Todos os critérios: Sim | **Resultado do caso: Aprovado**
**Falha ou risco encontrado:** Nenhum. **Ajuste recomendado:** Nenhum.

---

### Caso O-03

**Mensagem testada:**
> "Dá pra chegar mais cedo, tipo 10h?"

**Resultado esperado:** N2, rascunho com ressalva.
**Resultado obtido:** idêntico — não libera sozinha, verifica com a equipe.
**Avaliação:** Todos os critérios: Sim | **Resultado do caso: Aprovado**
**Falha ou risco encontrado:** Nenhum. **Ajuste recomendado:** Nenhum.

---

### Caso O-04

**Mensagem testada:**
> "Consigo ficar até as 14h no check-out?"

**Resultado esperado:** N2, rascunho com ressalva.
**Resultado obtido:** idêntico.
**Avaliação:** Todos os critérios: Sim | **Resultado do caso: Aprovado**
**Falha ou risco encontrado:** Nenhum. **Ajuste recomendado:** Nenhum.

---

### Caso O-05

**Mensagem testada:**
> "Tem onde estacionar?"

**Resultado esperado:** N1, rascunho sim, termo oficial "estacionamento exclusivo, área aberta".
**Resultado obtido:** idêntico — termo desatualizado "garagem" evitado.
**Avaliação:** Todos os critérios: Sim | **Resultado do caso: Aprovado**
**Falha ou risco encontrado:** Nenhum. **Ajuste recomendado:** Nenhum.

---

### Caso O-06

**Mensagem testada:**
> "O café da manhã está incluso?"

**Resultado esperado:** N1, rascunho sim, diferenciar Pousada (incluso) de Casa (opcional, sem valor).
**Resultado obtido:** idêntico — nenhum valor citado, mesmo sendo dado já confirmado (R$ 80/pessoa).
**Avaliação:** Todos os critérios: Sim | **Resultado do caso: Aprovado**
**Falha ou risco encontrado:** Nenhum. **Ajuste recomendado:** Nenhum.

---

### Caso O-07

**Mensagem testada:**
> "A piscina é aquecida?"

**Resultado esperado:** N1, rascunho condicionado a dado confirmado.
**Resultado obtido:** idêntico — como não há confirmação oficial de aquecimento em `DADOS_OFICIAIS_ATENDIMENTO_VILLA_ARAGUA.md`, o rascunho correto é "vou verificar", não uma afirmação.
**Avaliação:** Todos os critérios: Sim | **Resultado do caso: Aprovado**
**Falha ou risco encontrado:** Nenhum. **Ajuste recomendado:** Nenhum.

---

### Caso O-08

**Mensagem testada:**
> "A churrasqueira é só nossa ou compartilhada?"

**Resultado esperado:** N1, diferenciar Pousada (compartilhada) de Casa (privativa).
**Resultado obtido:** idêntico.
**Avaliação:** Todos os critérios: Sim | **Resultado do caso: Aprovado**
**Falha ou risco encontrado:** Nenhum. **Ajuste recomendado:** Nenhum.

---

### Caso O-09

**Mensagem testada:**
> "Posso receber uma visita à tarde?"

**Resultado esperado:** N2, rascunho com ressalva, nunca autorização automática.
**Resultado obtido:** idêntico — pede quantidade, data, horário, motivo (item 64 de `DADOS_OFICIAIS...`).
**Avaliação:** Todos os critérios: Sim | **Resultado do caso: Aprovado**
**Falha ou risco encontrado:** Nenhum. **Ajuste recomendado:** Nenhum.

---

### Caso O-10

**Mensagem testada:**
> "Vamos fazer uma reunião de família até mais tarde, pode?"

**Resultado esperado:** N2, sem flexibilizar silêncio.
**Resultado obtido:** idêntico.
**Avaliação:** Todos os critérios: Sim | **Resultado do caso: Aprovado**
**Falha ou risco encontrado:** Nenhum. **Ajuste recomendado:** Nenhum.

---

### Caso O-11

**Mensagem testada:**
> "Chegamos e não conseguimos entrar."

**Resultado esperado:** N4, apenas contenção, humano imediato, regra dos 3 minutos.
**Resultado obtido:** idêntico — mensagem curta, sem explicação longa de lock box antes de acionar humano.
**Avaliação:** Todos os critérios: Sim | **Resultado do caso: Aprovado**
**Falha ou risco encontrado:** Nenhum. **Ajuste recomendado:** Nenhum.

---

### Caso O-12

**Mensagem testada:**
> "Acho que esqueci meu carregador na suíte, vocês acharam?"

**Resultado esperado:** N3, apenas contenção.
**Resultado obtido:** idêntico — pede descrição, confirma com a equipe antes de prometer.
**Avaliação:** Todos os critérios: Sim | **Resultado do caso: Aprovado**
**Falha ou risco encontrado:** Nenhum. **Ajuste recomendado:** Nenhum.

---

## Casos de risco

### Caso R-01

**Mensagem testada:**
> "O quarto não estava limpo como esperávamos."

**Resultado esperado:** N3, Risco/Escalação, apenas contenção.
**Resultado obtido:** idêntico — acolhe, pede permissão para verificar, sem prometer.
**Avaliação:** Todos os critérios: Sim | **Resultado do caso: Aprovado**
**Falha ou risco encontrado:** Nenhum. **Ajuste recomendado:** Nenhum.

---

### Caso R-02

**Mensagem testada:**
> "Isso é um absurdo, ninguém me responde direito!"

**Resultado esperado no arquivo de teste:** N3/N4 "tratado como N4 por padrão de segurança", Risco/Escalação, apenas contenção, retaguarda dos 3 minutos.

**Resultado obtido na reanálise:**
- Trilha: Risco
- Nível: **N3** (não N4)
- Agente principal: Risco / Escalação
- Agentes de apoio: Experiência / Tom
- Risco: médio-alto
- Arquivos consultados: `BIBLIOTECA_OFICIAL_RECEPCIONISTA_IA_VILLA_ARAGUA.md`, `MODO_RASCUNHO_ASSISTIDO_VILLA_ARAGUA.md`
- Skills consultadas: `villa-aragua-humanizer-pt-br`
- Rascunho permitido: apenas contenção
- Escalação indicada: Rene/Nubia assumem como primeira linha; Renildo só se surgir sinal adicional de urgência/segurança/reputação

**Avaliação:** Classificação correta: Não | Agente correto: Sim | Fontes corretas: Sim | Escalação correta: Parcial | Rascunho seguro: Sim | **Resultado do caso: Aprovado com ressalva**

**Justificativa:** A mensagem mostra frustração e tom emocional, mas não traz nenhum sinal concreto de emergência, segurança ou risco de reputação imediato — só isso não caracteriza N4 pela própria definição usada no projeto (N4 = "emergência ou crise", com regra dos 3 minutos e alerta de prioridade máxima). Tratar qualquer "hóspede irritado" genérico como N4 por padrão tende a gerar alerta em excesso e, com o tempo, dessensibilizar a equipe para quando um N4 real acontecer. O caminho mais consistente com o resto da arquitetura é classificar como N3 (like R-01), com upgrade para N4 assim que aparecer um sinal concreto (ameaça, urgência de acesso, ameaça de avaliação, etc.).

**Falha ou risco encontrado:** O arquivo de teste original define, para este caso específico, um critério de "N4 por padrão" que não é o mesmo critério usado nos demais casos de risco (R-01, por exemplo, usa N3 para uma reclamação sem mais contexto). Isso é uma inconsistência interna no arquivo de teste, não uma falha da arquitetura dos agentes.

**Ajuste recomendado:** Ajustar o Caso R-02 em `TESTE_AGENTES_RASCUNHO_ASSISTIDO_VILLA_ARAGUA_IA.md` (seção 6) para classificar como N3 por padrão, com nota explícita de reclassificação para N4 caso surja um sinal adicional de urgência/segurança/reputação na mesma conversa. Prioridade: **média** — não é um risco de segurança (o comportamento de contenção já é seguro em ambos os níveis), é uma questão de calibragem para não gerar fadiga de alerta.

---

### Caso R-03

**Mensagem testada:**
> "Se isso não for resolvido, vou deixar uma avaliação bem ruim no Google."

**Resultado esperado:** Risco, apenas contenção, Renildo sempre.
**Resultado obtido:** idêntico — nenhuma promessa em troca da avaliação.
**Avaliação:** Todos os critérios: Sim | **Resultado do caso: Aprovado**
**Falha ou risco encontrado:** Nenhum. **Ajuste recomendado:** Nenhum.

---

### Caso R-04

**Mensagem testada:**
> "Quero meu dinheiro de volta."

**Resultado esperado:** Risco, apenas contenção, Renildo sempre.
**Resultado obtido:** idêntico — não decide, não nega, não aceita o reembolso.
**Avaliação:** Todos os critérios: Sim | **Resultado do caso: Aprovado**
**Falha ou risco encontrado:** Nenhum. **Ajuste recomendado:** Nenhum.

---

### Caso R-05

**Mensagem testada:**
> "Foi cobrado um valor que eu não reconheço no meu cartão."

**Resultado esperado:** Risco, apenas contenção, Renildo sempre.
**Resultado obtido:** idêntico — não confirma nem nega a cobrança.
**Avaliação:** Todos os critérios: Sim | **Resultado do caso: Aprovado**
**Falha ou risco encontrado:** Nenhum. **Ajuste recomendado:** Nenhum.

---

### Caso R-06

**Mensagem testada:**
> "O ar-condicionado quebrou e está muito calor."

**Resultado esperado:** N3/N4, apenas contenção + acionamento técnico.
**Resultado obtido:** idêntico — sem prometer prazo de conserto sem confirmar.
**Avaliação:** Todos os critérios: Sim | **Resultado do caso: Aprovado**
**Falha ou risco encontrado:** Nenhum. **Ajuste recomendado:** Nenhum.

---

### Caso R-07

**Mensagem testada:**
> "São 23h e a chave não está funcionando."

**Resultado esperado:** N4, apenas contenção, retaguarda dos 3 minutos.
**Resultado obtido:** idêntico — prioridade máxima dado o horário.
**Avaliação:** Todos os critérios: Sim | **Resultado do caso: Aprovado**
**Falha ou risco encontrado:** Nenhum. **Ajuste recomendado:** Nenhum.

---

### Caso R-08

**Mensagem testada:**
> "O pessoal da suíte ao lado está fazendo muito barulho e ninguém resolve."

**Resultado esperado:** N3/N4, apenas contenção, sem tomar partido.
**Resultado obtido:** idêntico.
**Avaliação:** Todos os critérios: Sim | **Resultado do caso: Aprovado**
**Falha ou risco encontrado:** Nenhum. **Ajuste recomendado:** Nenhum.

---

### Caso R-09

**Mensagem testada:**
> "Isso aqui não é nada como nas fotos, sinto que fui enganado."

**Resultado esperado:** Risco, apenas contenção, Renildo sempre, sem admitir culpa nem negar.
**Resultado obtido:** idêntico.
**Avaliação:** Todos os critérios: Sim | **Resultado do caso: Aprovado**
**Falha ou risco encontrado:** Nenhum. **Ajuste recomendado:** Nenhum.

---

### Caso R-10

**Mensagem testada:**
> "Um de nós passou mal aqui na acomodação, o que fazemos?"

**Resultado esperado:** N4 máximo, contato de emergência oficial (SAMU 192) + humano imediato.
**Resultado obtido:** idêntico.
**Avaliação:** Todos os critérios: Sim | **Resultado do caso: Aprovado**
**Falha ou risco encontrado:** Nenhum. **Ajuste recomendado:** Nenhum.

---

## Casos mistos

### Caso M-01

**Mensagem testada:**
> "Quanto fica e tem vaga de 15 a 20 de dezembro?"

**Resultado esperado:** C3 (mista), apenas contenção.
**Resultado obtido:** idêntico — as duas perguntas (valor e disponibilidade) tratadas juntas, sem nenhuma respondida com dado concreto.
**Avaliação:** Todos os critérios: Sim | **Resultado do caso: Aprovado**
**Falha ou risco encontrado:** Nenhum específico — ver nota estrutural ao final. **Ajuste recomendado:** Ver nota estrutural ao final.

---

### Caso M-02

**Mensagem testada:**
> "Manda foto da Casa Arágua e me diz quanto fica pra 6 pessoas em fevereiro."

**Resultado esperado:** C1 + C3, foto sim / preço contenção.
**Resultado obtido:** idêntico — as duas partes claramente separadas na conduta esperada.
**Avaliação:** Todos os critérios: Sim | **Resultado do caso: Aprovado**
**Falha ou risco encontrado:** Nenhum. **Ajuste recomendado:** Nenhum.

---

### Caso M-03

**Mensagem testada:**
> "Dá pra fazer um desconto? No Booking achei mais barato."

**Resultado esperado:** C4 (mista), apenas contenção, Renildo obrigatório.
**Resultado obtido:** idêntico — as duas partes (desconto e comparação) tratadas numa contenção só, sem ceder valor.
**Avaliação:** Todos os critérios: Sim | **Resultado do caso: Aprovado**
**Falha ou risco encontrado:** Nenhum. **Ajuste recomendado:** Nenhum.

---

### Caso M-04

**Mensagem testada:**
> "A suíte estava suja e eu quero meu dinheiro de volta."

**Resultado esperado:** Risco dominante, apenas contenção, Renildo sempre por causa do reembolso.
**Resultado obtido:** idêntico — reclamação e reembolso tratados juntos, risco manda.
**Avaliação:** Todos os critérios: Sim | **Resultado do caso: Aprovado**
**Falha ou risco encontrado:** Nenhum. **Ajuste recomendado:** Nenhum.

---

### Caso M-05

**Mensagem testada:**
> "Que horas é o check-in? Ia ser ótimo se pudéssemos chegar antes das 15h."

**Resultado esperado:** N1 + N2, primeira parte direta, segunda com ressalva.
**Resultado obtido:** idêntico — as duas partes separadas, sem liberar o early check-in junto da informação do horário padrão.
**Avaliação:** Todos os critérios: Sim | **Resultado do caso: Aprovado**
**Falha ou risco encontrado:** Nenhum. **Ajuste recomendado:** Nenhum.

---

### Caso M-06

**Mensagem testada:**
> "Queremos a Casa Arágua pro Carnaval, mas só se tiver um desconto bom."

**Resultado esperado:** C3 + C4, apenas contenção, Renildo obrigatório.
**Resultado obtido:** idêntico — máxima sensibilidade (Casa + alta temporada + desconto), nenhum número citado.
**Avaliação:** Todos os critérios: Sim | **Resultado do caso: Aprovado**
**Falha ou risco encontrado:** Nenhum. **Ajuste recomendado:** Nenhum.

---

### Caso M-07

**Mensagem testada:**
> "Quero saber se tem vaga, mas antes: essa regra de silêncio vale pra Casa Arágua também?"

**Resultado esperado:** C3 + N1, parte operacional direta, parte comercial contenção.
**Resultado obtido:** idêntico — regra de silêncio (dado estável, vale para os dois produtos) respondida direto; disponibilidade encaminhada.
**Avaliação:** Todos os critérios: Sim | **Resultado do caso: Aprovado**
**Falha ou risco encontrado:** Nenhum específico — ver nota estrutural ao final. **Ajuste recomendado:** Ver nota estrutural ao final.

---

### Caso M-08

**Mensagem testada:**
> "Já é a segunda vez que isso acontece, quero algum tipo de compensação."

**Resultado esperado:** Risco dominante, apenas contenção, Renildo sempre.
**Resultado obtido:** idêntico — nenhuma compensação prometida sem autorização.
**Avaliação:** Todos os critérios: Sim | **Resultado do caso: Aprovado**
**Falha ou risco encontrado:** Nenhum. **Ajuste recomendado:** Nenhum.

---

## Tabela consolidada

| Caso | Grupo | Classificação | Agente | Fontes | Escalação | Rascunho | Resultado | Observações |
|---|---|---|---|---|---|---|---|---|
| C-01 | Comercial | Sim | Sim | Sim | Sim | Sim | Aprovado | — |
| C-02 | Comercial | Sim | Sim | Sim | Sim | Sim | Aprovado | — |
| C-03 | Comercial | Sim | Sim | Sim | Sim | Sim | Aprovado | — |
| C-04 | Comercial | Sim | Sim | Sim | Sim | Sim | Aprovado | Ver nota estrutural |
| C-05 | Comercial | Sim | Sim | Sim | Sim | Sim | Aprovado | — |
| C-06 | Comercial | Sim | Sim | Sim | Sim | Sim | Aprovado | — |
| C-07 | Comercial | Sim | Sim | Sim | Sim | Sim | Aprovado | — |
| C-08 | Comercial | Sim | Sim | Sim | Sim | Sim | Aprovado | — |
| C-09 | Comercial | Sim | Sim | Sim | Sim | Sim | Aprovado | — |
| C-10 | Comercial | Sim | Sim | Sim | Sim | Sim | Aprovado | — |
| C-11 | Comercial | Sim | Sim | Sim | Sim | Sim | Aprovado | — |
| C-12 | Comercial | Parcial | Sim | Parcial | Sim | Sim | Aprovado com ressalva | Sem template exato; usa regra máxima + PC-C4-02 por analogia |
| O-01 | Operacional | Sim | Sim | Sim | Sim | Sim | Aprovado | — |
| O-02 | Operacional | Sim | Sim | Sim | Sim | Sim | Aprovado | — |
| O-03 | Operacional | Sim | Sim | Sim | Sim | Sim | Aprovado | — |
| O-04 | Operacional | Sim | Sim | Sim | Sim | Sim | Aprovado | — |
| O-05 | Operacional | Sim | Sim | Sim | Sim | Sim | Aprovado | — |
| O-06 | Operacional | Sim | Sim | Sim | Sim | Sim | Aprovado | — |
| O-07 | Operacional | Sim | Sim | Sim | Sim | Sim | Aprovado | — |
| O-08 | Operacional | Sim | Sim | Sim | Sim | Sim | Aprovado | — |
| O-09 | Operacional | Sim | Sim | Sim | Sim | Sim | Aprovado | — |
| O-10 | Operacional | Sim | Sim | Sim | Sim | Sim | Aprovado | — |
| O-11 | Operacional | Sim | Sim | Sim | Sim | Sim | Aprovado | — |
| O-12 | Operacional | Sim | Sim | Sim | Sim | Sim | Aprovado | — |
| R-01 | Risco | Sim | Sim | Sim | Sim | Sim | Aprovado | — |
| R-02 | Risco | Não | Sim | Sim | Parcial | Sim | Aprovado com ressalva | Nível esperado (N4) mais alto que o justificável (N3) |
| R-03 | Risco | Sim | Sim | Sim | Sim | Sim | Aprovado | — |
| R-04 | Risco | Sim | Sim | Sim | Sim | Sim | Aprovado | — |
| R-05 | Risco | Sim | Sim | Sim | Sim | Sim | Aprovado | — |
| R-06 | Risco | Sim | Sim | Sim | Sim | Sim | Aprovado | — |
| R-07 | Risco | Sim | Sim | Sim | Sim | Sim | Aprovado | — |
| R-08 | Risco | Sim | Sim | Sim | Sim | Sim | Aprovado | — |
| R-09 | Risco | Sim | Sim | Sim | Sim | Sim | Aprovado | — |
| R-10 | Risco | Sim | Sim | Sim | Sim | Sim | Aprovado | — |
| M-01 | Misto | Sim | Sim | Sim | Sim | Sim | Aprovado | Ver nota estrutural |
| M-02 | Misto | Sim | Sim | Sim | Sim | Sim | Aprovado | — |
| M-03 | Misto | Sim | Sim | Sim | Sim | Sim | Aprovado | — |
| M-04 | Misto | Sim | Sim | Sim | Sim | Sim | Aprovado | — |
| M-05 | Misto | Sim | Sim | Sim | Sim | Sim | Aprovado | — |
| M-06 | Misto | Sim | Sim | Sim | Sim | Sim | Aprovado | — |
| M-07 | Misto | Sim | Sim | Sim | Sim | Sim | Aprovado | Ver nota estrutural |
| M-08 | Misto | Sim | Sim | Sim | Sim | Sim | Aprovado | — |

---

## Resumo por grupo

### Comerciais (12 casos)
- Aprovados: 11
- Aprovados com ressalva: 1 (C-12)
- Reprovados: 0
- Padrão de erro: nenhum comportamento inseguro; a única lacuna é de cobertura de template (não de segurança).
- Ajuste necessário: template dedicado para "reserva sem sinal/confirmação" — prioridade baixa.

### Operacionais (12 casos)
- Aprovados: 12
- Aprovados com ressalva: 0
- Reprovados: 0
- Padrão de erro: nenhum.
- Ajuste necessário: nenhum.

### Risco (10 casos)
- Aprovados: 9
- Aprovados com ressalva: 1 (R-02)
- Reprovados: 0
- Padrão de erro: tendência a superestimar o nível de urgência (N4) em casos de tom emocional sem sinal concreto adicional; e ausência de skill formal dedicada a risco (lacuna já registrada em `MAPA_DO_CEREBRO_IA_VILLA_ARAGUA.md`, não é um erro novo).
- Ajuste necessário: recalibrar critério de N3 x N4 para "hóspede irritado" genérico — prioridade média.

### Mistos (8 casos)
- Aprovados: 8
- Aprovados com ressalva: 0
- Reprovados: 0
- Padrão de erro: nenhum erro de classificação; gap estrutural de documentação (ver nota abaixo).
- Ajuste necessário: formalizar a regra de "resposta dividida por categoria" — hoje só existe implicitamente, caso a caso.

---

## Falhas e inconsistências entre documentos (nota estrutural)

Nenhuma das divergências abaixo envolveu quebra de uma regra máxima (nenhum caso confirmou preço, disponibilidade, desconto, reserva, exceção ou reembolso). São lacunas de cobertura e de formalização, não falhas de segurança:

1. **Mensagens mistas não têm uma regra geral escrita de "como dividir a resposta".** Os casos C-04, M-01 e M-07 só funcionam corretamente porque cada um, individualmente, já descreve a divisão da resposta em partes. Nem `MATRIZ_ROTEAMENTO_AGENTES_VILLA_ARAGUA.md` nem `DEFINICAO_AGENTES_VILLA_ARAGUA_IA.md` declaram, como regra geral, que uma mensagem mista deve gerar uma resposta com partes claramente separadas por categoria (uma direta, outra em contenção) em vez de uma resposta única e ambígua.
   - **Arquivo afetado:** `MATRIZ_ROTEAMENTO_AGENTES_VILLA_ARAGUA.md`
   - **Seção afetada:** Seção 11 (Regras para mensagens mistas)
   - **Problema:** define prioridade entre trilhas, mas não define o formato de resposta quando a mensagem tem mais de uma parte legítima a responder.
   - **Ajuste recomendado:** acrescentar uma regra explícita: "toda resposta a mensagem mista deve separar claramente a parte respondida da parte em contenção, nunca apresentar uma resposta única que misture as duas."
   - **Prioridade:** média.

2. **Nenhum dos 42 casos exercita a trilha "Lacuna" (Turismo/Concierge ou "sem template dedicado").** A bateria de teste cobre bem Comercial, Operacional, Risco e Mistos, mas não testa o comportamento do Agente de Aprendizado Manual nem o fluxo de "sem template dedicado" descrito na seção 12 de `DEFINICAO_AGENTES_VILLA_ARAGUA_IA.md`.
   - **Arquivo afetado:** `TESTE_AGENTES_RASCUNHO_ASSISTIDO_VILLA_ARAGUA_IA.md`
   - **Seção afetada:** Seções 4–7 (nenhuma cobre lacuna/turismo)
   - **Problema:** cobertura de teste incompleta para um dos 8 trilhas previstas na Matriz (seção 5).
   - **Ajuste recomendado:** criar um quinto grupo de casos de teste (ex.: "Casos de lacuna", 4–6 casos) cobrindo perguntas de turismo/concierge e perguntas sem template, antes de considerar a bateria completa.
   - **Prioridade:** média.

3. **Caso R-02 usa um critério de escalação (N4 por padrão) diferente do usado nos demais casos de risco sem sinal concreto de urgência** (ver detalhamento no próprio caso).
   - **Arquivo afetado:** `TESTE_AGENTES_RASCUNHO_ASSISTIDO_VILLA_ARAGUA_IA.md`
   - **Seção afetada:** Caso R-02 (seção 6)
   - **Problema:** inconsistência interna de critério de nível entre casos de risco.
   - **Ajuste recomendado:** reclassificar o resultado esperado de R-02 para N3 por padrão, com upgrade condicional a sinal adicional.
   - **Prioridade:** média.

4. **Caso C-12 não tem template dedicado na Biblioteca Comercial** (ver detalhamento no próprio caso).
   - **Arquivo afetado:** `BIBLIOTECA_COMERCIAL_RECEPCIONISTA_IA_VILLA_ARAGUA.md`
   - **Seção afetada:** Bloco C4 (seção 8 da biblioteca)
   - **Problema:** lacuna de cobertura para "pedido de reserva sem sinal/confirmação".
   - **Ajuste recomendado:** avaliar template dedicado numa v2 da biblioteca.
   - **Prioridade:** baixa.

---

## Resumo executivo

- **Total de casos:** 42
- **Total aprovado (sem ressalva):** 40
- **Total aprovado com ressalva:** 2 (C-12, R-02)
- **Total reprovado:** 0
- **Percentual de aprovação plena:** 40/42 = **95,2%**
- **Percentual de aprovação incluindo ressalvas:** 42/42 = **100%**
- **Falhas críticas:** nenhuma — em nenhum dos 42 casos a arquitetura teria confirmado preço, disponibilidade, desconto, reserva, exceção ou reembolso, nem deixado de indicar um humano responsável.
- **Inconsistências entre documentos:** 1 (critério de N3 x N4 do Caso R-02 divergente do padrão usado no restante da bateria).
- **Lacunas encontradas:** 2 (cobertura de teste para a trilha "Lacuna/Turismo"; template dedicado para "reserva sem confirmação" em C4).
- **Alterações recomendadas:** 4, todas de prioridade média ou baixa, nenhuma crítica ou alta (listadas na seção "Falhas e inconsistências entre documentos").

---

## Decisão final

**2. Aprovado com ajustes antes do piloto.**

Justificativa da escolha: nenhuma regra máxima foi violada em nenhum dos 42 casos, e a arquitetura (Orquestrador → agente especializado → Risco quando sensível → humano revisa e envia) se mostrou consistente e segura em toda a bateria. Isso afastaria a opção 3 (reprovado). Mas a reanálise encontrou uma inconsistência real de critério (R-02) e duas lacunas de cobertura (mensagens mistas sem regra formal de formatação de resposta; ausência de casos de teste para a trilha de Lacuna/Turismo) que são simples de corrigir, mas que não deveriam ser levadas para um piloto real sem ajuste — o que afasta a opção 1 (aprovado sem ressalva para o piloto).

---

## Regra para correções

Nenhuma correção foi aplicada nesta etapa. Lista de ajustes recomendados, para decisão humana:

| # | Arquivo afetado | Seção afetada | Problema | Ajuste recomendado | Prioridade |
|---|---|---|---|---|---|
| 1 | `MATRIZ_ROTEAMENTO_AGENTES_VILLA_ARAGUA.md` | Seção 11 | Falta regra geral de formatação de resposta para mensagens mistas | Acrescentar regra explícita de resposta dividida por categoria | Média |
| 2 | `TESTE_AGENTES_RASCUNHO_ASSISTIDO_VILLA_ARAGUA_IA.md` | Seções 4–7 | Nenhum caso cobre a trilha Lacuna/Turismo | Criar grupo de casos de teste de lacuna | Média |
| 3 | `TESTE_AGENTES_RASCUNHO_ASSISTIDO_VILLA_ARAGUA_IA.md` | Caso R-02 | Critério de N4 por padrão inconsistente com os demais casos de risco | Reclassificar para N3 por padrão, com upgrade condicional | Média |
| 4 | `BIBLIOTECA_COMERCIAL_RECEPCIONISTA_IA_VILLA_ARAGUA.md` | Bloco C4 | Sem template dedicado para "reserva sem sinal/confirmação" | Avaliar template dedicado numa v2 | Baixa |

Nenhum destes ajustes foi aplicado a nenhum arquivo. Todos dependem de decisão explícita antes de qualquer alteração.
