# MODO_RASCUNHO_ASSISTIDO_VILLA_ARAGUA

**Projeto:** VILLA ARAGUA IA
**Rodada:** 4 — Automação WhatsApp segura
**Tema:** 4.22 — Desenho do modo Rascunho Assistido
**Data de persistência:** 2026-07-16
**Status:** aprovado para uso prático imediato; não é automação; WhatsApp real não conectado.

> Este documento depende de `BIBLIOTECA_OFICIAL_RECEPCIONISTA_IA_VILLA_ARAGUA.md` (25 templates, testada em regressão via `teste_regressao_biblioteca.py`). Leia os dois documentos juntos.

---

## 1. Diagnóstico

A biblioteca operacional está persistida, testada e íntegra. O que faltava não era mais conteúdo — era **o procedimento humano** que transforma a biblioteca em uso real no dia a dia, sem depender de nenhuma automação. Este documento descreve esse procedimento: o "Modo Rascunho Assistido".

---

## 2. Objetivo

Permitir que Rene, Nubia ou Renildo usem a Recepcionista IA para **acelerar** respostas de hóspede sem nunca abrir mão do controle final sobre o que é enviado.

---

## 3. Fluxo operacional

```
1. HÓSPEDE ESCREVE
   Mensagem chega no WhatsApp real da Villa Arágua (número oficial 47 99201-4117),
   como já acontece hoje — nada muda aqui.

2. HUMANO COPIA
   Rene, Nubia ou Renildo copia o texto exato da mensagem do hóspede
   (sem editar, sem resumir) e cola numa conversa com a IA (Claude),
   junto com o contexto que já sabe: Pousada ou Casa, se a reserva
   está confirmada, se há algo incomum.

3. IA CLASSIFICA
   A IA identifica o nível (1, 2, 3 ou 4) usando a Biblioteca Oficial
   (BIBLIOTECA_OFICIAL_RECEPCIONISTA_IA_VILLA_ARAGUA.md) como referência.

4. IA SUGERE
   - Nível 1/2 → a IA devolve um rascunho de resposta pronto,
     usando o template correspondente (PC-N1-xx / PC-N2-xx).
   - Nível 3 → a IA devolve um texto de contenção (nunca autoriza)
     + indica para quem escalar (Rene/Nubia comercial ou operacional;
     Renildo se for preço/desconto/exceção/reputação).
   - Nível 4 → a IA devolve um texto curto de contenção + alerta
     de prioridade máxima, indicando Rene → Nubia → Renildo
     (regra dos 3 minutos).

5. HUMANO REVISA
   A pessoa lê o rascunho e decide: aprovar sem edição, aprovar com
   edição, ou bloquear/reescrever do zero. Nunca copia e cola sem ler.

6. HUMANO ENVIA
   Só a pessoa envia a mensagem final pelo WhatsApp real — a IA
   nunca tem acesso ao WhatsApp da Villa Arágua neste modo.

7. CASOS N3/N4
   Não seguem os passos 4–6 da forma normal: o texto de contenção
   pode ser enviado rapidamente pelo humano (não é uma "resposta
   final" no sentido comercial, é uma ponte), mas a decisão real
   (autorizar, negociar, resolver) sempre fica com o humano indicado.
```

---

## 4. Papéis e responsabilidades

| Quem | O que faz |
|---|---|
| **Rene** | Copia mensagens, pede rascunho à IA, aprova/edita casos operacionais (N1–N3), primeira linha em N4 |
| **Nubia** | Mesma função de Rene, como substituta |
| **Renildo** | Só entra quando o caso é escalado (preço, desconto, exceção, reputação, ou retaguarda de N4) |
| **A IA** | Só sugere. Nunca envia. Nunca decide. Nunca tem acesso ao WhatsApp real |

---

## 5. Como usar a Biblioteca Oficial neste modo

- A IA sempre parte de `BIBLIOTECA_OFICIAL_RECEPCIONISTA_IA_VILLA_ARAGUA.md` como fonte — não inventa template novo na hora, a menos que declare explicitamente "sem template dedicado".
- Se a pergunta for comercial ou de turismo (fora dos 25 templates operacionais), a IA deve dizer isso claramente, não tentar encaixar à força.
- Se faltar dado (tipo de hospedagem, nome da reserva, horário), a IA pede — nunca assume.

---

## 6. Modelo prático de uso (o que colar na IA)

```
Mensagem do hóspede: "[colar exatamente o que o hóspede escreveu]"
Contexto: Pousada ou Casa (se souber) | reserva confirmada? | algo incomum?
```

A IA responde com: nível identificado, template usado (ou lacuna declarada), rascunho pronto (se N1/N2) ou texto de contenção + destino de escalonamento (se N3/N4).

---

## 7. Regras de bloqueio dentro do rascunho assistido

- Nível 3 e 4 **nunca** viram "rascunho pronto para copiar e enviar como resposta final" — são sempre texto de contenção + encaminhamento.
- Nenhum rascunho de N3/N4 deve ser enviado sem o humano responsável (conforme seção 4) ter, de fato, decidido o mérito do pedido.
- A IA nunca deve ser tratada como "quem decidiu" — mesmo que o texto saia perfeito, quem aprovou o envio foi a pessoa.

---

## 8. O que este modo NÃO é

- Não é WhatsApp conectado.
- Não é envio automático.
- Não é IA respondendo hóspede diretamente.
- Não é decisão de preço, desconto ou exceção pela IA.
- É, estritamente, um copiloto de digitação para quem já ia responder de qualquer forma.

---

## 9. Riscos do modo Rascunho Assistido

- **Fadiga de revisão:** depois de muitos rascunhos "aprovados sem edição" seguidos, a tentação é parar de ler com atenção.
- **Copiar e colar sem contexto:** se o humano não informar corretamente Pousada/Casa/reserva confirmada, a IA vai pedir esclarecimento (PC-N1-07) em vez de arriscar — isso é seguro, mas pode gerar impressão de "trabalho duplicado" se o humano não perceber que só precisa informar o contexto de uma vez.
- **Uso fora do escopo:** tentar usar o modo para perguntas comerciais/turísticas ainda não cobertas pela biblioteca operacional, esperando uma resposta pronta que não existe.

---

## 10. Critérios de sucesso antes de avançar

- Rene, Nubia e Renildo usam o modo por um período real (sugestão: 1–2 semanas) sem confusão sobre quando aprovar/editar/bloquear.
- Nenhum caso de N3/N4 é enviado sem passar pelo humano responsável.
- Feedback qualitativo: o modo realmente economiza tempo de digitação sem criar risco novo.

---

## 11. Decisão do Tema 4.22

**Modo Rascunho Assistido desenhado e pronto para uso prático** — não exige nenhuma ferramenta nova, nenhuma conexão, nenhum arquivo adicional além do que já existe (`BIBLIOTECA_OFICIAL_RECEPCIONISTA_IA_VILLA_ARAGUA.md`). Pode começar a ser usado por Rene/Nubia/Renildo imediatamente, copiando mensagens manualmente para uma conversa com a IA, sem qualquer automação.

---

## 12. Bloqueios que continuam de pé

Nenhuma automação real foi criada por este documento. Continuam bloqueados, como em toda a Rodada 4: WhatsApp real, Zapier, Make, API, backend, e qualquer envio automático de mensagem a hóspede. Este modo é 100% manual — a IA participa apenas como copiloto de texto, nunca como executora.
