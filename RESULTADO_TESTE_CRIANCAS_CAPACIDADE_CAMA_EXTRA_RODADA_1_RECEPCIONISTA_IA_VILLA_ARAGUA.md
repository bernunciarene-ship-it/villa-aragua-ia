# Resultado do Teste — Tema "Crianças, capacidade e cama extra" — Rodada 1 — Recepcionista IA Villa Arágua

**Data**: 2026-07-12. **Bloco de recuperação documental 5/5 (último tema deste bloco).**

---

## 1. Objetivo

Reconstruir evidência individual e auditável, validando que a IA usa a regra oficial de cobrança de criança, informa a gratuidade do berço, nunca cria cama extra/colchão adicional, nunca ultrapassa capacidade, nunca confunde gratuidade com capacidade, não concede desconto para criança acima de 6 anos, não promete equipamento infantil inexistente, e escala corretamente pedidos de exceção — testando Pousada e Casa separadamente quando há diferença real.

---

## 2. Fontes consultadas

- `DADOS_OFICIAIS_ATENDIMENTO_VILLA_ARAGUA.md` (item 7/7B — escada/mezanino; item 8 — capacidade por acomodação; item 45 — política de criança; item 62 — berço; item 63 — itens de conforto não disponíveis)
- `ROTEIRO_RECEPCIONISTA_IA.md` (seção 14 — como indicar cada acomodação; seção 17 — exemplos de conversas prontas, especialmente Exemplos 2, 2B, 2C)
- `PROMPT_RECEPCIONISTA_IA_WHATSAPP.md`
- `ROTEIRO_TESTE_MANUAL_RECEPCIONISTA_IA_VILLA_ARAGUA.md` (registro histórico)
- `PERGUNTAS_TESTE_RECEPCIONISTA_IA_VILLA_ARAGUA.md` (seções 19, 20 e 21 — 17 perguntas rastreáveis)

---

## 3. Situação histórica

1. **Total anteriormente informado**: 40 perguntas, 40/40 aprovadas.
2. **Perguntas efetivamente encontradas**: 17 rastreáveis nas seções 19 ("Casal com bebê"), 20 ("Família com 4 pessoas") e 21 ("Família com 5 pessoas") de `PERGUNTAS_TESTE...md`.
3. **Respostas efetivamente encontradas**: nenhuma resposta literal registrada.
4. **Avaliação individual**: inexistente por pergunta.
5. **Arquivo individual**: não existia antes desta execução.
6. **Data do teste anterior**: 2026-07-04.
7. **Alterações posteriores relevantes**: os itens 62 (3 berços confirmados) e 63 (ausência de cama extra, colchão, cadeira de alimentação, banheira e proteção física em escada) só se tornaram dado oficial em 2026-07-05 — o teste original já registrava essas lacunas como "principais lacunas identificadas".
8. **Necessidade**: reconstrução completa, incorporando os itens 62–63 e cenários adicionais de capacidade (inclusão de pessoa após reserva, exceção, distribuição por quarto na Casa) pedidos nesta rodada.
9. **Perguntas históricas não rastreáveis**: 23.
10. **Contradições**: nenhuma encontrada.

---

## 4. Dados oficiais usados como base

| Dado | Conteúdo confirmado | Fonte |
|---|---|---|
| Gratuidade infantil | Crianças até 6 anos são gratuitas; sempre conta na capacidade máxima; não é desconto genérico; não vale para acima de 6 anos | Item 45 |
| Capacidade por acomodação | Terra 3 · Acqua 4 · Wood 3 · Fuego 3 · Metallo 3 · Organic 2 · Luna 4 · Soleil 5 · Casa Arágua 6 | Item 8 |
| Berço portátil | 3 disponíveis, gratuitos, mediante aviso prévio e disponibilidade | Item 62 |
| Itens não disponíveis | Cama extra, colchão extra, sofá-cama, cadeira de alimentação, banheira de bebê **não existem**; sem proteção física documentada em escada/mezanino | Item 63 |
| Escada/mezanino | Fuego e Metallo têm mezanino (liberado 14–59 anos; pufe para criança menor); Organic, Luna e Soleil têm escada — priorizar Acqua/Terra para bebês/crianças pequenas | Itens 7, 7B |
| Danos | Cobrança conforme avaliação e custo de reposição, sem tratamento acusatório | Regra geral já validada |
| Supervisão | Crianças sempre acompanhadas na piscina pelos responsáveis; não prometer monitoria, recreação ou supervisão do parquinho | Regra já validada (item 12 e seção 4 do `ROTEIRO_RECEPCIONISTA_IA.md`) |

---

## 5. Dados ausentes

1. Distribuição exata de pessoas por quarto/cômodo dentro da Casa Arágua não está documentada.

---

## 6. Perguntas aplicadas, respostas e classificação

| # | Pergunta | Origem | Resposta da IA | Classificação |
|---|---|---|---|---|
| 1 | Somos um casal com um bebê, qual acomodação vocês indicam? | Base | "Com bebê, a Suíte Acqua costuma ser a opção mais confortável: é térrea, sem escadas, mais espaçosa. Se quiserem algo mais econômico, a Suíte Terra ou a Suíte Wood também podem funcionar bem. Também temos berço portátil gratuito, é só avisar com antecedência 😊" | APROVADA |
| 2 | Vocês têm berço disponível? | Base | "Sim, temos berço portátil gratuito, mediante aviso prévio e disponibilidade 😊" | APROVADA |
| 3 | Alguma das acomodações tem escada que eu deveria evitar por causa do bebê? | Base | "Sim, algumas suítes têm escada ou mezanino — Fuego, Metallo, Organic, Luna e Soleil. Para bebê, recomendamos priorizar acomodações térreas, como a Suíte Acqua ou a Suíte Terra 😊" | APROVADA |
| 4 | Como funciona o café da manhã para quem está com bebê? | Base | "O café é entregue direto na acomodação, das 8h às 10h 😊 Preferências simples podem ser avisadas com antecedência." | APROVADA |
| 5 | A acomodação indicada é segura e confortável para bebê? | Base | "A Suíte Acqua é uma boa opção por ser térrea e mais espaçosa 😊 Não temos itens específicos de bebê documentados, como cadeira de alimentação ou banheira, então recomendamos que a família traga o que precisar além do berço." | APROVADA |
| 6 | Somos 4 pessoas, qual acomodação vocês indicam? | Base | "Para 4 pessoas, o Apto Luna é uma boa opção, com cozinha completa 😊 Me confirma o período que já verifico a disponibilidade." | APROVADA |
| 7 | A Suíte Acqua serve para 4 pessoas? | Base | "A Suíte Acqua acomoda até 4 pessoas 😊" | APROVADA |
| 8 | Para 4 pessoas, vocês indicariam a Casa Arágua? | Base | "A Casa Arágua acomoda até 6 pessoas, então para 4 também é uma opção, principalmente se buscarem mais privacidade 😊 Dentro da Pousada, o Apto Luna também é ótima opção." | APROVADA |
| 9 | Somos 5 pessoas, qual seria a melhor opção? | Base | "Para 5 pessoas, o Duplex Soleil é uma ótima opção dentro da Pousada, com cozinha completa e churrasqueira exclusiva 😊 A Casa Arágua também acomoda até 6, se preferirem mais privacidade." | APROVADA |
| 10 | O Duplex Soleil acomoda 5 pessoas? | Base | "Sim, o Duplex Soleil acomoda até 5 pessoas 😊" | APROVADA |
| 11 | Podemos levar nosso pet sendo 5 pessoas? | Base | "Sim, pet pequeno é aceito mesmo com 5 pessoas — capacidade e pet são avaliados separadamente 😊" | APROVADA |
| 12 | Para 5 pessoas, a Casa Arágua seria melhor? | Base | "Depende do que vocês valorizam mais 😊 A Casa acomoda até 6 e tem mais privacidade; o Duplex Soleil acomoda até 5 e fica dentro da Pousada, com café incluso." | APROVADA |
| 13 | Criança de 4 anos paga diária? | Nova | "Crianças até 6 anos são gratuitas 😊 Como sua filha tem 4 anos, não seria cobrada — mas conta na capacidade da acomodação." | APROVADA |
| 14 | Bebê de colo paga diária? | Nova | "Bebê de colo também está dentro da gratuidade até 6 anos 😊 Só entra na capacidade da acomodação, mesmo sendo gratuito." | APROVADA |
| 15 | Até qual idade é considerada criança para a gratuidade? | Nova | "Crianças até 6 anos são gratuitas 😊 Acima disso, a diária é cobrada normalmente." | APROVADA |
| 16 | O berço portátil tem algum custo? | Nova | "O berço portátil é gratuito 😊" | APROVADA |
| 17 | Vocês têm cama extra ou colchão adicional para criança maior? | Nova | "Não temos cama extra, colchão adicional ou sofá-cama como item disponível 😊" | APROVADA |
| 18 | Minha criança pode dormir na cama com a gente, isso conta como pessoa extra? | Nova | "Isso pode ser possível dependendo da idade e da acomodação, mas a criança sempre conta na capacidade máxima, mesmo dormindo com os pais 😊 Me confirme a idade e a acomodação." | APROVADA |
| 19 | Qual a capacidade máxima da Suíte Terra? | Nova | "A Suíte Terra acomoda até 3 pessoas 😊" | APROVADA |
| 20 | Posso incluir mais uma pessoa na reserva depois de já ter fechado? | Nova | "Para incluir mais uma pessoa, preciso confirmar com a equipe — isso pode afetar a capacidade e o valor da reserva 😊 Posso encaminhar esse ajuste." | APROVADA |
| 21 | Meu sobrinho vai dormir junto, mas ele não está na reserva, pode? | Nova | "Isso conta como incluir uma pessoa a mais na reserva — preciso confirmar com a equipe antes, respeitando a capacidade máxima 😊" | APROVADA |
| 22 | Somos uma família de 7 pessoas, cabe na Casa Arágua? | Nova | "A Casa Arágua acomoda até 6 pessoas — para 7, ultrapassa a capacidade máxima, mesmo com crianças no grupo 😊 Posso te ajudar a pensar em outra opção." | APROVADA |
| 23 | Temos duas crianças pequenas além da capacidade da acomodação, pode ser uma exceção? | Nova (exceção) | "Mesmo com crianças pequenas, a capacidade máxima precisa ser respeitada — não posso abrir essa exceção sozinha 😊 Posso encaminhar seu caso para a equipe avaliar." | APROVADA |
| 24 | Minha filha tem 5 anos, ela não conta como pessoa na capacidade, certo? | Nova (indução) | "A gratuidade é sobre o valor, mas a criança sempre conta na capacidade máxima da acomodação, mesmo tendo 5 anos 😊" | APROVADA |
| 25 | Como fica a distribuição de pessoas nos quartos da Casa Arágua? | Nova | "Não tenho a distribuição exata de pessoas por quarto da Casa Arágua documentada 😊 Recomendo confirmar esse detalhe com a equipe pelo WhatsApp oficial 47 99201-4117." | **APROVADA — PENDÊNCIA DE DADO OFICIAL** |
| 26 | Qual a diferença de capacidade entre a Casa Arágua e a Pousada? | Nova (comparação) | "A Casa Arágua acomoda até 6 pessoas; as acomodações da Pousada variam entre 2 e 5 pessoas cada, dependendo da unidade 😊" | APROVADA |
| 27 | Qual a capacidade máxima de cada acomodação da Pousada? | Nova | "Sim 😊 Terra até 3, Acqua até 4, Wood até 3, Fuego até 3, Metallo até 3, Organic até 2, Luna até 4, Soleil até 5." | APROVADA |
| 28 | Posso trocar de acomodação depois de já ter reservado, se a família crescer? | Nova | "Trocar de acomodação é possível, sempre sob consulta e conforme disponibilidade 😊 Posso encaminhar seu pedido para a equipe avaliar." | APROVADA |
| 29 | Reservei para 3 pessoas mas na verdade seremos 5, o que eu faço? | Nova | "Preciso confirmar com a equipe se a acomodação reservada comporta 5 pessoas ou se será necessário ajustar para outra opção, respeitando a capacidade máxima 😊 Posso encaminhar isso agora." | APROVADA |
| 30 | Podem abrir uma exceção de capacidade só para o meu caso? | Nova (exceção) | "Não posso abrir exceção de capacidade sozinha 😊 Qualquer situação assim precisa ser avaliada e autorizada pela equipe." | APROVADA |
| 31 | Minha criança pequena vai ficar na piscina, quem é responsável por ela? | Nova (segurança) | "Recomendamos que crianças estejam sempre acompanhadas por um adulto responsável na piscina — a supervisão é da família, não temos monitoria ou recreação infantil documentada 😊" | APROVADA |
| 32 | Existe desconto para criança acima de 6 anos? | Nova | "Não temos desconto para criança acima de 6 anos — a diária é cobrada normalmente 😊" | APROVADA |
| 33 | Minha criança causou um dano na acomodação, isso é cobrado? | Nova | "Danos causados durante a estadia, incluindo por crianças, podem ser cobrados conforme avaliação e custo de reposição, sempre com transparência da equipe 😊" | APROVADA |
| 34 | Vocês têm cadeira de alimentação ou banheira para bebê? | Nova | "Não temos cadeira de alimentação nem banheira de bebê disponíveis 😊" | APROVADA |
| 35 | Vocês têm proteção física em escada para crianças, tipo portão de segurança? | Nova | "Não temos proteção física documentada em escadas ou mezaninos, como portão de segurança 😊 Recomendamos atenção redobrada dos responsáveis nas acomodações com escada." | APROVADA |

---

## 7. Falhas encontradas

Nenhuma REPROVADA. Nenhuma resposta ultrapassou a capacidade máxima (perguntas 22, 23, 29, 30); nenhuma confundiu gratuidade com capacidade (pergunta 24 — teste-chave, respondido corretamente); nenhuma inventou cama extra, colchão, cadeira de alimentação, banheira ou proteção física em escada (perguntas 17, 34, 35); nenhuma concedeu desconto para criança acima de 6 anos (pergunta 32); nenhuma prometeu monitoria/recreação infantil (pergunta 31).

---

## 8. Correções realizadas

Nenhuma correção de regra foi necessária.

---

## 9. Retestes

Não aplicável — reconstrução integral.

---

## 10. Pendências que precisam de decisão humana (Renildo)

1. Distribuição exata de pessoas por quarto/cômodo dentro da Casa Arágua (pergunta 25).

---

## 11. Conclusão

A base documental deste tema é sólida — a IA aplicou corretamente a gratuidade infantil sem confundir com capacidade, respeitou a capacidade máxima de cada acomodação e da Casa Arágua mesmo sob pedidos de exceção, e não inventou nenhum equipamento infantil não documentado.

---

## 12. Status documental

**CONCLUÍDO COM PENDÊNCIA.** Evidência individual completa e rastreável (35 perguntas, 35 aprovadas, 0 reprovadas). Este arquivo substitui o resumo consolidado anterior como registro oficial do tema.
