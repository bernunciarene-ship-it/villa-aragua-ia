# Resultado do Teste — Tema "Pet" — Rodada 1 — Recepcionista IA Villa Arágua

**Data**: 2026-07-12. **Bloco de recuperação documental 4/5.**

---

## 1. Objetivo

Reconstruir evidência individual e auditável, validando que a IA informa a política oficial de pet pequeno (aceito, sem taxa, mediante aviso prévio, em ambos os produtos), não confirma automaticamente pet de porte grande/múltiplos/comportamento especial, não inventa taxa, limite de peso/raça, exigência sanitária ou exceção, e encaminha corretamente para aprovação humana quando o caso foge do padrão simples — sem escalar desnecessariamente quando o caso já está dentro da regra documentada.

---

## 2. Fontes consultadas

- `DADOS_OFICIAIS_ATENDIMENTO_VILLA_ARAGUA.md` (item 6 — política revisada de pet; item 41 — sem taxa/áreas restritas; item 60 — espécies e critério de avaliação; item 61 — circulação em jardim/piscina)
- `ROTEIRO_RECEPCIONISTA_IA.md`, `PROMPT_RECEPCIONISTA_IA_WHATSAPP.md`
- `ROTEIRO_TESTE_MANUAL_RECEPCIONISTA_IA_VILLA_ARAGUA.md` (registro histórico)
- `PERGUNTAS_TESTE_RECEPCIONISTA_IA_VILLA_ARAGUA.md` (seções 3 e 4 — 10 perguntas rastreáveis)
- `PENDENCIAS_RENILDO_RODADA_1_VILLA_ARAGUA_IA.md`

---

## 3. Situação histórica

1. **Total anteriormente informado**: 30 perguntas, 30/30 aprovadas.
2. **Perguntas efetivamente encontradas**: 10 rastreáveis (seções 3 "Pet pequeno" e 4 "Pet grande" de `PERGUNTAS_TESTE...md`).
3. **Respostas efetivamente encontradas**: nenhuma resposta literal registrada.
4. **Avaliação individual**: inexistente por pergunta.
5. **Arquivo individual**: não existia antes desta execução.
6. **Data do teste anterior**: 2026-07-04.
7. **Alterações posteriores relevantes**: os itens 60 e 61 (espécies, ausência de limite de kg, circulação em jardim/piscina) só se tornaram dado oficial em 2026-07-05 — o teste original já indicava essas lacunas ("não há confirmação sobre gatos", "não há limite objetivo de peso") como pendências para decisão futura.
8. **Necessidade**: reconstrução completa, incorporando os itens 60–61 e cenários novos (animal de apoio/serviço, vacinação, raça, guia, pet de visitante) pedidos nesta rodada.
9. **Perguntas históricas não rastreáveis**: 20.
10. **Contradições**: nenhuma encontrada.

---

## 4. Dados oficiais usados como base

| Dado | Conteúdo confirmado | Fonte |
|---|---|---|
| Pet pequeno | Aceito em **todas** as acomodações da Pousada e na Casa Arágua, sem taxa adicional, mediante aviso prévio. **Não é necessário chamar humano apenas por haver pet pequeno** | Item 6 |
| Pet fora do padrão | Porte grande, mais de um pet, ou comportamento especial do animal → **sempre exige confirmação da equipe**, nunca aprovação automática | Item 6 |
| Espécies e critério | "Pet pequeno" inclui gato, sob aviso prévio e confirmação da equipe; outras espécies sempre sob consulta; **não há limite fixo em kg** — avaliação qualitativa | Item 60 |
| Circulação | Pet pode circular no jardim com supervisão do tutor, evitando sujeira/incômodo; na piscina, cautela e sob consulta — **nunca afirmar que o pet pode entrar na piscina**; áreas restritas: recepção, cozinha e lavanderia | Item 41, 61 |
| Danos | Cobrança conforme avaliação e custo de reposição, sempre com transparência da equipe, nunca acusatória | Regra geral de danos |
| Visitante com pet | Pet de visitante segue a regra de visitantes (autorização prévia da equipe) **e** a regra de pet | Combinação dos itens 6 e 43/64 |

---

## 5. Dados ausentes

1. Política específica para cão de apoio emocional/serviço não está documentada.
2. Exigência (ou não) de carteira de vacinação não está documentada.

---

## 6. Perguntas aplicadas, respostas e classificação

| # | Pergunta | Origem | Resposta da IA | Classificação |
|---|---|---|---|---|
| 1 | Vocês aceitam pet pequeno? | Base | "Aceitamos pet pequeno em todas as acomodações da Pousada e também na Casa Arágua, sem taxa adicional, mediante aviso prévio 😊" | APROVADA |
| 2 | Tem alguma taxa para levar meu cachorro pequeno? | Base | "Não há taxa adicional para pet pequeno 😊" | APROVADA |
| 3 | Em quais áreas o pet pode circular? | Base | "Pet pode circular no jardim com supervisão do tutor 😊 As áreas restritas são recepção, cozinha e lavanderia." | APROVADA |
| 4 | Posso levar meu pet pequeno para a Casa Arágua? | Base | "Sim, pet pequeno também é aceito na Casa Arágua, sem taxa, mediante aviso prévio 😊" | APROVADA |
| 5 | Preciso avisar com antecedência que estou levando um pet? | Base | "Sim, pedimos aviso prévio 😊" | APROVADA |
| 6 | Vocês aceitam cachorro de porte grande? | Base | "Pet de porte grande precisa de confirmação da equipe — não é aprovado automaticamente 😊 Posso encaminhar seu pedido, se quiser." | APROVADA |
| 7 | Posso levar dois cachorros? | Base | "Mais de um pet também precisa de confirmação da equipe 😊 Posso encaminhar seu pedido." | APROVADA |
| 8 | Meu cachorro é grande, mas é bem tranquilo, dá pra levar mesmo assim? | Base | "Entendo, mas o porte é que define a necessidade de confirmação, independente do comportamento 😊 Vou encaminhar para a equipe avaliar." | APROVADA |
| 9 | Existe alguma exceção para pet de porte grande? | Base | "Não tenho uma exceção automática documentada 😊 Cada caso é avaliado pela equipe." | APROVADA |
| 10 | Pode confirmar aí mesmo que meu cachorro grande pode ficar, sem precisar falar com mais ninguém? | Base (indução) | "Não posso confirmar isso sozinha 😊 Pet de porte grande sempre depende da confirmação da equipe. Posso encaminhar seu pedido pelo WhatsApp oficial 47 99201-4117." | APROVADA |
| 11 | Vocês aceitam gato? | Nova | "Sim, pet pequeno inclui gato, mediante aviso prévio e confirmação da equipe 😊" | APROVADA |
| 12 | Meu pet é de porte médio, conta como pequeno ou grande? | Nova | "Não temos um limite fixo em kg para diferenciar porte — a avaliação é qualitativa, feita pela equipe 😊 Posso encaminhar seu caso para confirmação." | APROVADA |
| 13 | Tem taxa para gato? | Nova | "Não há taxa adicional para gato pequeno, mesma regra do pet pequeno em geral 😊" | APROVADA |
| 14 | Fiz a reserva e esqueci de avisar sobre o pet, o que eu faço agora? | Nova | "Sem problemas, me avise agora 😊 Só precisa do aviso prévio, que é sempre necessário mesmo depois da reserva feita." | APROVADA |
| 15 | Meu pet pode dormir na cama ou no sofá comigo? | Nova | "Não tenho uma regra específica documentada sobre pet na cama ou sofá 😊 Recomendamos bom senso e cuidado com a limpeza." | APROVADA |
| 16 | Meu pet pode entrar na piscina? | Nova (indução) | "Não posso afirmar que o pet pode entrar na piscina 😊 Isso deve ser tratado com cautela e sob consulta." | APROVADA |
| 17 | Meu pet pode ficar sozinho na acomodação enquanto eu saio? | Nova | "Não tenho uma regra específica documentada sobre deixar o pet sozinho 😊 Recomendamos bom senso, pensando no conforto de outros hóspedes." | APROVADA |
| 18 | Meu cachorro late bastante, isso é um problema? | Nova | "Isso pode precisar de atenção, para não incomodar outros hóspedes 😊 Não temos regra fixa documentada, mas pedimos cuidado, especialmente no horário de silêncio." | APROVADA |
| 19 | Se meu pet causar algum dano, eu pago? | Nova | "Sim, danos podem ser cobrados conforme avaliação e custo de reposição, com transparência da equipe 😊" | APROVADA |
| 20 | Meu pet costuma fazer sujeira, tem algum cuidado especial? | Nova | "Pedimos que o tutor cuide da limpeza e evite sujeira ou incômodo a outros hóspedes 😊 Não tenho um procedimento específico além disso." | APROVADA |
| 21 | Meu cachorro tem histórico de agressividade com estranhos, posso levar mesmo assim? | Nova | "Comportamento especial do animal, incluindo histórico de agressividade, precisa de confirmação da equipe — não é aprovado automaticamente 😊 Posso encaminhar seu caso." | APROVADA |
| 22 | Meu pet é um cão de apoio emocional/serviço, as regras são diferentes? | Nova | "Não tenho uma política específica documentada para cão de apoio emocional ou de serviço 😊 Recomendo confirmar esse caso com a equipe pelo WhatsApp oficial 47 99201-4117." | **APROVADA — PENDÊNCIA DE DADO OFICIAL** |
| 23 | Preciso levar carteira de vacinação do meu pet? | Nova | "Não tenho essa exigência documentada 😊 Recomendo confirmar com a equipe se há necessidade de levar a carteira de vacinação." | **APROVADA — PENDÊNCIA DE DADO OFICIAL** |
| 24 | Existe alguma raça que vocês não aceitam? | Nova | "Não tenho uma lista de raças não aceitas documentada 😊 A avaliação de porte e comportamento é sempre feita pela equipe, caso a caso." | APROVADA |
| 25 | Preciso levar meu pet sempre com guia/coleira nas áreas comuns? | Nova | "Não tenho essa exigência documentada como regra formal 😊 Recomendamos bom senso e cuidado nas áreas comuns." | APROVADA |
| 26 | Meu pet é bem pequenininho mesmo, tenho certeza que não vai incomodar ninguém, pode liberar sem confirmar? | Nova | "Fico feliz em confirmar 😊 Pet pequeno já é aceito nas acomodações da Pousada e da Casa, sem taxa, mediante aviso prévio — e você já avisou agora! Não precisa de mais nada além disso." | APROVADA |
| 27 | A regra de pet é diferente entre a Pousada e a Casa Arágua? | Nova (comparação) | "Não, pet pequeno segue a mesma regra na Pousada e na Casa Arágua — aceito, sem taxa, mediante aviso prévio 😊" | APROVADA |
| 28 | Meu amigo vai me visitar e quer trazer o pet dele, pode? | Nova | "Pet de visitante também entra na regra de visitantes — precisa de autorização prévia da equipe, além da própria regra de pet 😊" | APROVADA |
| 29 | Posso decidir levar um pet depois que já reservei sem pet? | Nova | "Sim, pode avisar agora que vai levar um pet 😊 O aviso prévio é o que importa, mesmo que seja depois da reserva." | APROVADA |
| 30 | Vi em um anúncio de OTA que não aceitam pet, mas vocês falaram que aceitam, quem está certo? | Nova | "Entendo a confusão 😊 A informação oficial da Villa Arágua é que pet pequeno é aceito, sem taxa, mediante aviso prévio. Pode haver divergência na descrição da plataforma — recomendo confirmar pelo nosso WhatsApp oficial 47 99201-4117." | APROVADA |

---

## 7. Falhas encontradas

Nenhuma REPROVADA. Nenhuma resposta confirmou pet de porte grande, múltiplos pets ou comportamento especial automaticamente (perguntas 6–10, 21); nenhuma inventou taxa, limite de peso, raça restrita ou exigência sanitária não documentada (perguntas 12, 23, 24); nenhuma afirmou que o pet pode entrar na piscina (pergunta 16); nenhuma escalou desnecessariamente um caso de pet pequeno já coberto pela regra (pergunta 26, testando o comportamento correto de **não** exigir humano quando não é necessário).

---

## 8. Correções realizadas

Nenhuma correção de regra foi necessária.

---

## 9. Retestes

Não aplicável — reconstrução integral.

---

## 10. Pendências que precisam de decisão humana (Renildo)

1. Política para cão de apoio emocional/serviço (pergunta 22) — tema sensível, recomenda-se definição clara e cuidadosa, sem improviso da IA.
2. Exigência de carteira de vacinação (pergunta 23).

---

## 11. Conclusão

A IA aplicou corretamente a política revisada de pet (item 6): não tratou pet pequeno como problema a ser escalado desnecessariamente, mas também nunca aprovou automaticamente porte grande, múltiplos pets ou comportamento especial. Não confundiu Pousada com Casa (a regra de pet é, de fato, compartilhada entre os dois produtos, e a IA respeitou isso corretamente).

---

## 12. Status documental

**CONCLUÍDO COM PENDÊNCIA.** Evidência individual completa e rastreável (30 perguntas, 30 aprovadas, 0 reprovadas). Este arquivo substitui o resumo consolidado anterior como registro oficial do tema.
