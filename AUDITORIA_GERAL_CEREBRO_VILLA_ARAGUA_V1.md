# Auditoria Geral — Cérebro Villa Arágua (v1)

Auditoria do conjunto de documentos que hoje formam o "cérebro" da Recepcionista IA, do Check-in Autônomo, do Guia Digital e da curadoria local da Villa Arágua. Baseada na leitura direta do estado atual dos 12 arquivos listados — nenhum arquivo foi alterado, movido, apagado ou renomeado nesta auditoria.

---

## 1. Lista de todos os campos `[PREENCHER]`

### `DADOS_OFICIAIS_ATENDIMENTO_VILLA_ARAGUA.md` (2 ocorrências)
- Grafia oficial da cerveja "Borck" (cortesia do Tatuíra Petisqueira) — 2 menções (item 25 e linha de Diferenciais Comerciais).

### `ROTEIRO_RECEPCIONISTA_IA.md` (1 ocorrência)
- Grafia oficial da cerveja "Borck".

### `PROMPT_RECEPCIONISTA_IA_WHATSAPP.md` (1 ocorrência)
- Grafia oficial da cerveja "Borck".

### `GUIA_DIGITAL_HOSPEDE_VILLA_ARAGUA.md` (seção 33 + 1 no corpo do texto)
- Link de localização da Pousada Arágua.
- Link de localização da Casa Arágua.
- Link/página dos "Roteiros Sugeridos para Aproveitar Bombinhas".
- Horário oficial de atendimento da recepção.
- Mapa de vagas por acomodação (8 unidades).
- Canal oficial de WhatsApp para dúvidas/emergências durante a estadia.
- Senha de Wi-Fi.
- Nomes confirmados de restaurantes/pizzarias/sorveterias/padaria/mercearia/farmácia (**parcialmente desatualizado — ver Seção 3**).
- Recomendações específicas de praias por perfil (**parcialmente desatualizado — ver Seção 3**).
- Recomendações específicas de passeios (**parcialmente desatualizado — ver Seção 3**).
- Recomendações específicas para dias de chuva/nublados (**parcialmente desatualizado — ver Seção 3**).
- Contatos de emergência complementares.
- Canal oficial da Villa Arágua para emergências.
- Grafia oficial da cerveja "Borck" (cortesia do Tatuíra).

### `GUIA_CHECKIN_AUTONOMO.md` (seção 25)
- Link oficial do Guia Digital do Hóspede.
- Senha de Wi-Fi.
- Contato de suporte técnico do porteiro eletrônico.
- Política de segurança de geração/envio/rotação da senha do lock box.
- Contatos de emergência (hospital, farmácia, eletricista, piscineiro, manutenção).
- Política formal de early check-in/late check-out.
- Mapa completo de vagas por acomodação (8 unidades).
- Horário oficial de atendimento da recepção.
- Horário limite para envio das instruções de acesso.
- Número/canal oficial para o hóspede ligar em caso de problema de acesso.
- Passo a passo padrão do porteiro eletrônico e do lock box.
- (Sem tag `[PREENCHER]` explícita, mas também pendente): definição de canal seguro para códigos de acesso e de como a automação avisará Renildo em caso de problema urgente.

### `ROTEIROS_SUGERIDOS_BOMBINHAS.md` (seção 10 + cortesia no corpo)
- Nomes dos fornecedores de cada tipo de passeio (barco, mergulho, SUP, caiaque, surf, 4x4, Carro Safari Bombinhas).
- Links, telefones, valores e horários dos fornecedores de passeio.
- Condições de funcionamento/reserva de cada passeio.
- Nomes específicos de cafés/sorveterias/pizzarias para dias de chuva.
- Links, telefones e horários de Porto Belo e Balneário Camboriú.
- Distância/tempo de deslocamento até Porto Belo e Balneário Camboriú.
- Regra específica de qual praia indicar por tipo de vento.
- Telefones e links dos 8 restaurantes já cadastrados por nome.
- Links, horários e condição de acesso do Morro do Macaco, Mirante 360º e Trapiche do Canto Grande.
- Nome oficial, link, telefone, horário e deslocamento dos outlets de Tijucas e Porto Belo.
- Grafia oficial da cerveja "Borck" (4 menções — **não está na lista consolidada da seção 10, ver Seção 3**).

### `MIDIAS_E_LINKS_OFICIAIS_VILLA_ARAGUA.md` (seção 10 + campos extras)
- Google Maps da Pousada Arágua e da Casa Arágua.
- Link futuro do Guia Digital do Hóspede.
- Vídeo oficial específico da Casa Arágua.
- Fotos principais em link público (Casa Arágua + 8 acomodações da Pousada).
- Fotos/vídeos dos diferenciais da Pousada (piscina, área comum, churrasqueira, parquinho, redes, quiosques, café da manhã, árvores nativas, estacionamento, cadeiras de praia).
- Restaurantes/pizzarias/sorveterias/padaria/mercearia/farmácia (demais, além dos 2 parceiros de cortesia já nomeados).
- Praias por perfil, passeios, atendimento na areia, dias de chuva, dicas de vento.
- Link, Instagram, telefone e horário do Tatuíra Petisqueira e do Alquimista/Oliva.
- Grafia oficial da cerveja "Borck" (**também não está na lista consolidada da seção 10, ver Seção 3**).

---

## 2. Categorização dos campos `[PREENCHER]`

### Críticos para atendimento real (bloqueiam uso 100% autônomo)
- Mapa de vagas por acomodação (aparece em 3 arquivos: `DADOS_OFICIAIS` indiretamente, `GUIA_CHECKIN_AUTONOMO`, `GUIA_DIGITAL`).
- Política de segurança de geração/envio/rotação da senha do lock box.
- Passo a passo padrão do porteiro eletrônico e do lock box.
- Número/canal oficial para o hóspede ligar em caso de problema de acesso.
- Canal seguro oficial para envio de códigos de acesso.
- Como a automação avisará Renildo/apoio humano em caso de problema urgente.
- Horário oficial de atendimento da recepção.
- Senha de Wi-Fi.
- Contatos de emergência (hospital, farmácia de plantão, eletricista, piscineiro, manutenção) e canal oficial de emergência da Villa.

### Importantes, mas não bloqueantes (afetam qualidade comercial, não segurança)
- Google Maps da Pousada e da Casa Arágua.
- Fotos públicas por acomodação e da Casa Arágua (mídia bruta já existe localmente).
- Vídeo oficial da Casa Arágua.
- Grafia oficial da cerveja "Borck" (afeta apenas a precisão de um detalhe da cortesia, não a segurança da resposta — já tem fallback seguro: "conforme regra vigente do parceiro").
- Link, Instagram, telefone e horário dos 2 restaurantes parceiros de cortesia.
- Fotos/vídeos dos diferenciais da Pousada (piscina, área comum, etc.).
- Link do Guia Digital do Hóspede (referenciado em 3 arquivos diferentes, ainda não existe).
- Política formal de early check-in/late check-out.

### Complementares (curadoria/experiência, sem urgência)
- Fornecedores, links, valores e horários de passeios (barco, mergulho, SUP, caiaque, surf, 4x4, Safari).
- Detalhes de acesso ao Morro do Macaco, Mirante 360º e Trapiche do Canto Grande.
- Nomes/links dos demais restaurantes (Berro D'Água, Pisco, Cezar etc.), pizzarias, sorveterias, padaria, mercearia, farmácia.
- Detalhes de Porto Belo, Balneário Camboriú e outlets.
- Regra específica de praia por tipo de vento.

---

## 3. Contradições e inconsistências encontradas

1. **`DADOS_OFICIAIS` — nota de rastreamento desatualizada (item 2, distância da Casa Arágua)**: o valor oficial já está correto (250m) e os arquivos-fonte `.docx` já foram corrigidos nas rodadas anteriores (confirmado ao reler o arquivo original agora), mas a própria coluna de rastreamento do item 2 ainda afirma que 4 arquivos-fonte "ainda dizem ~180 metros" — essa nota interna ficou desatualizada e não reflete mais a realidade. Não afeta o atendimento (a IA usa o valor oficial, 250m), mas é uma imprecisão no próprio painel de controle.

2. **`GUIA_DIGITAL_HOSPEDE_VILLA_ARAGUA.md` — seção 33 desatualizada frente ao `ROTEIROS_SUGERIDOS_BOMBINHAS.md`**: a seção 33 ainda lista como `[PREENCHER]` as "recomendações específicas de praias por perfil", "recomendações de passeios" e "recomendações para dias de chuva" — mas esse conteúdo **já existe e está validado** em `ROTEIROS_SUGERIDOS_BOMBINHAS.md` (5 praias, 10 passeios, dias de chuva com outlets). A seção 28 do Guia Digital já faz a referência cruzada corretamente, mas a lista de pendências da seção 33 não foi atualizada para refletir isso. Resultado prático: parece haver mais trabalho pendente do que realmente há.

3. **`ROTEIROS_SUGERIDOS_BOMBINHAS.md` e `MIDIAS_E_LINKS_OFICIAIS_VILLA_ARAGUA.md` — listas de pendências (seção 10) não incluem a grafia da cerveja "Borck"**: o placeholder `[PREENCHER/CONFIRMAR GRAFIA]` existe corretamente no corpo dos dois arquivos (4 menções em `ROTEIROS_SUGERIDOS` e 1 em `MIDIAS_E_LINKS`), mas não foi replicado nas respectivas listas consolidadas de pendências (seção 10 de ambos). Risco baixo (o dado real já está marcado corretamente onde importa), mas gera divergência entre "o que está pendente no texto" e "o que está pendente na lista-resumo".

4. **3 relatórios de status desatualizados frente às últimas 7 rodadas de melhoria**: `RELATORIO_ROTEIROS_SUGERIDOS_BOMBINHAS_V1.md`, `RELATORIO_MIDIAS_E_LINKS_OFICIAIS_VILLA_ARAGUA_V1.md` e `RELATORIO_GUIA_DIGITAL_HOSPEDE_V1.md` não mencionam: as cortesias gastronômicas (Tatuíra/Alquimista-Oliva), a hierarquia comercial argentino/hispânica com Casa Arágua em primeiro lugar, nem a regra de idioma português/espanhol — todas adicionadas depois desses relatórios terem sido escritos. Não é uma contradição de conteúdo (os arquivos principais estão corretos), mas os relatórios de status não refletem mais o estado real desses arquivos.

5. **Nenhuma contradição de regra operacional foi encontrada** nos arquivos principais (`DADOS_OFICIAIS`, `ROTEIRO`, `PROMPT`): pet, escada/mezanino, estacionamento, café da manhã, cortesias, hierarquia argentina e regra de idioma estão consistentes entre os 3 arquivos nas verificações realizadas.

---

## 4. Regras que ainda precisam de teste controlado

- **Fuego/Metallo com cama de solteiro no mezanino para "casal com adolescente/filho maior"** — regra adicionada, mas **nunca simulada** em nenhuma rodada de teste controlado até agora. É a única regra comercial recente sem validação por simulação.
- **Hierarquia comercial argentina/hispânica em casos-limite**: os testes feitos cobriram família pequena (4 pessoas) e pedido de cozinha completa, mas não testaram o **limite exato da "família grande"** (ex.: 5 pessoas — está no meio do caminho entre "Apto Luna até 4" e "Casa Arágua para grande"?) nem o caso de família que quer ficar **dentro da pousada mas é grande demais para o Soleil** (6+ pessoas sem aceitar a Casa).
- **Interação entre regra de idioma + hierarquia argentina + cortesias na mesma conversa**: os testes fizeram essas 3 regras separadamente; falta um teste que misture as três no mesmo atendimento (ex.: família argentina grande, em espanhol, que também pergunta sobre restaurante parceiro).
- **Cenário de reserva confirmada com pedido de cortesia gastronômica antecipado** (ex.: hóspede pergunta sobre a cortesia do Tatuíra antes mesmo de perguntar sobre a acomodação) — ainda não simulado.
- **Chegada fora do padrão combinada com estacionamento cheio** (2+ carros extras, Pousada sem vaga, hóspede insistindo) — testado apenas o caso de 2 carros para 1 acomodação; não testado o caso de negociação mais insistente do hóspede.

---

## 5. Status de cada arquivo: pronto vs. dependente de preenchimento

| Arquivo | Status |
|---|---|
| `DADOS_OFICIAIS_ATENDIMENTO_VILLA_ARAGUA.md` | **Pronto** para uso como fonte — só falta a grafia da cerveja Borck (não bloqueante) |
| `ROTEIRO_RECEPCIONISTA_IA.md` | **Pronto** — mesma pendência da cerveja |
| `PROMPT_RECEPCIONISTA_IA_WHATSAPP.md` | **Pronto para simulação/teste**, mesma pendência da cerveja; ainda não testado nos cenários da Seção 4 acima |
| `ROTEIROS_SUGERIDOS_BOMBINHAS.md` | **Parcialmente dependente** — estrutura e curadoria principal prontas (praias, restaurantes, passeios), mas boa parte dos dados operacionais (links, telefones, horários, fornecedores) ainda é `[PREENCHER]` |
| `MIDIAS_E_LINKS_OFICIAIS_VILLA_ARAGUA.md` | **Parcialmente dependente** — os links realmente oferecidos (páginas, vídeos, redes sociais, WhatsApp, e-mail) estão prontos; mapas, fotos públicas e restaurantes ainda pendentes |
| `GUIA_DIGITAL_HOSPEDE_VILLA_ARAGUA.md` | **Dependente de preenchimento** — não deve ser publicado antes de resolver ao menos os itens críticos (Wi-Fi, mapa de vagas, horário da recepção, canal de emergência) |
| `GUIA_CHECKIN_AUTONOMO.md` | **Dependente de preenchimento crítico** — não deve operar 100% automático (ver Seção 8) |
| Relatórios (`RELATORIO_*`) | **Desatualizados** frente às últimas melhorias (ver Seção 3, item 4) — não bloqueiam operação, mas não devem ser lidos como retrato fiel do estado atual sem esta auditoria como complemento |

---

## 6. O que falta para a Recepcionista IA WhatsApp v1.7 ficar pronta para teste controlado real

1. Confirmar a grafia oficial da cerveja "Borck" (ou substituir/remover a cortesia se o nome estiver errado).
2. Rodar o teste controlado específico da regra "casal com adolescente/Fuego-Metallo com cama de solteiro" (nunca testado).
3. Rodar um teste combinado (idioma + hierarquia argentina + cortesia) numa única conversa, para verificar se as regras não colidem quando usadas juntas.
4. Testar o caso-limite de "família grande mas quer ficar na pousada, não cabe no Soleil".
5. Atualizar (ou aceitar como está) a versão do `RELATORIO_RECEPCIONISTA_IA_WHATSAPP_V1_3.md`, hoje travado em "v1.5", sem refletir pet-commercial-rule, Acqua, credibilidade combinada, hierarquia argentina, idioma e cortesias — recomendo gerar um `RELATORIO...V1_7.md` novo consolidando tudo antes de declarar a versão pronta.
6. Nenhuma pendência de segurança foi encontrada nos arquivos `DADOS_OFICIAIS`, `ROTEIRO` e `PROMPT` — o texto das regras já está internamente consistente.

## 7. O que falta para o Guia Digital ficar pronto para publicação

1. Resolver os campos críticos: horário oficial da recepção, senha de Wi-Fi, canal oficial de WhatsApp/emergência, contatos de emergência complementares.
2. Resolver os links de localização (Google Maps) da Pousada e da Casa Arágua.
3. Atualizar a seção 33 para não listar mais como pendente o que `ROTEIROS_SUGERIDOS_BOMBINHAS.md` já resolveu (praias, passeios, dias de chuva) — hoje a seção passa a impressão de mais trabalho pendente do que existe de fato.
4. Confirmar/preencher o link do Guia Digital em si (autorreferência pendente — o link "de si mesmo" ainda não existe, o que é esperado antes da publicação, mas precisa existir no momento do lançamento).
5. Confirmar a grafia da cerveja Borck.
6. Só então: revisão de conteúdo final e teste com hóspedes reais (já indicado como próxima melhoria).

## 8. O que falta para o Check-in Autônomo sair do nível documental e virar operação real

Praticamente inalterado desde o `RELATORIO_CHECKIN_AUTONOMO_V1_1.md` — as pendências continuam sendo as mesmas 12 identificadas naquele relatório, todas ainda presentes na seção 25 do `GUIA_CHECKIN_AUTONOMO.md`:
1. Mapa completo de vagas por acomodação.
2. Horário oficial de atendimento da recepção.
3. Horário limite para envio de instruções de acesso.
4. Canal seguro oficial para envio de códigos de acesso.
5. Número/canal oficial para o hóspede ligar em caso de problema.
6. Passo a passo do porteiro eletrônico e do lock box.
7. Política de geração/envio/rotação da senha do lock box.
8. Definição de como a automação avisará Renildo/apoio humano.
9. Contatos de emergência (hospital, farmácia, eletricista, piscineiro, manutenção).
10. Senha de Wi-Fi.
11. Link do Guia Digital do Hóspede.
12. Política formal de early check-in/late check-out.

Nenhuma dessas pendências foi resolvida desde o relatório v1.1 — este é o arquivo com a maior distância entre "documentado" e "operável de verdade".

---

## 9. Lista de prioridades

### Fazer agora
1. Confirmar a grafia oficial da cerveja "Borck" (afeta 6 arquivos, correção rápida e pontual).
2. Definir o horário oficial de atendimento da recepção (afeta Check-in Autônomo, Guia Digital e diversas respostas da Recepcionista IA).
3. Definir a política de segurança da senha do lock box + passo a passo do porteiro eletrônico/lock box (maior bloqueio real do Check-in Autônomo).
4. Definir o número/canal oficial para o hóspede ligar em caso de problema de acesso.
5. Confirmar a senha de Wi-Fi.

### Fazer depois
6. Mapa completo de vagas por acomodação (Pousada).
7. Corrigir a seção 33 do Guia Digital para não repetir pendências já resolvidas por `ROTEIROS_SUGERIDOS_BOMBINHAS.md`.
8. Rodar o teste controlado da regra Fuego/Metallo + casal com adolescente (nunca testada).
9. Rodar o teste combinado idioma + hierarquia argentina + cortesia.
10. Gerar um `RELATORIO_RECEPCIONISTA_IA_WHATSAPP_V1_7.md` novo, consolidando todas as melhorias desde o v1.5.
11. Links de Google Maps da Pousada e da Casa Arágua.
12. Contatos de emergência complementares e canal oficial de emergência.

### Pode esperar
13. Fotos públicas por acomodação e vídeo específico da Casa Arágua.
14. Link/Instagram/telefone/horário dos 2 parceiros de cortesia.
15. Fornecedores, links e valores de passeios (barco, mergulho, SUP, caiaque, surf, 4x4, Safari).
16. Detalhes de acesso ao Morro do Macaco, Mirante 360º e Trapiche.
17. Nomes/links dos demais restaurantes, pizzarias, sorveterias, padaria, mercearia, farmácia.
18. Detalhes de Porto Belo, Balneário Camboriú e outlets.
19. Regra específica de praia por tipo de vento.
20. Política formal de early check-in/late check-out.
