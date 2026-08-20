# Relatório de Status — Check-in Autônomo Villa Arágua (v1.1)

## 1. O que foi criado

- `GUIA_CHECKIN_AUTONOMO.md`: guia operacional completo para check-in autônomo da Villa Arágua, cobrindo objetivo, princípios de atendimento, fluxos por prazo (7 dias, 3 dias, 1 dia antes e dia do check-in), estacionamento, porteiro eletrônico, lock box, regras da casa, café da manhã, piscina/áreas comuns, pet, famílias com crianças pequenas, concierge local, tratamento de problemas na chegada, mensagens prontas, checklist interno, o que nunca prometer e pendências para implantação real.
- **Objetivo do guia**: permitir que o hóspede chegue e acesse a acomodação com segurança e tranquilidade mesmo com a recepção física mais fechada, sem perder o tom acolhedor da Villa Arágua ("Férias Pra Sempre").
- **Relação com a operação semi-autônoma**: o guia é a peça operacional que viabiliza a transição da Villa Arágua para uma operação mais organizada e menos dependente da presença direta de Renildo — mantendo sempre um canal humano disponível para dúvidas e emergências, conforme já previsto no DNA/Playbook da marca.

## 2. Principais decisões operacionais registradas

- Check-in **a partir das 15h**.
- Chegada **após 22h é permitida** quando o fluxo autônomo estiver ativo, a reserva estiver confirmada e as instruções de acesso tiverem sido enviadas corretamente antes.
- **22h não é tratado como limite absoluto** de chegada — apenas como referência do fluxo padrão de recepção presencial.
- Uso futuro de **porteiro eletrônico** (liberação remota, orientação por WhatsApp em caso de falha).
- Uso futuro de **lock box** (vídeo explicativo, senha individual enviada perto do horário do check-in).
- Códigos de acesso enviados **somente no momento correto e por canal seguro definido**.
- **Nenhuma senha real é registrada** no documento até existir uma política de segurança formal de geração/envio/rotação.

## 3. Estacionamento

- **Pousada Arágua**: 1 vaga gratuita, identificada e organizada por acomodação.
- Estrutura física: 3 vagas na frente/recepção e 5 vagas nos fundos/rua de trás (a pousada atravessa a quadra; ambas as ruas são sem saída); todas as vagas têm placa com o nome da acomodação, tamanho semelhante (boas, mas justas).
- **Mapa de vagas por acomodação — resolvido (2026-07-03)**: frente/recepção — Vaga 1 Luna, Vaga 2 Acqua, Vaga 3 Organic; fundos/rua de trás (outro portão) — Vaga 4 Wood, Vaga 5 Terra, Vaga 6 Metallo, Vaga 7 Fuego, Vaga 8 Soleil. Organic e Soleil exigem mais atenção na manobra (entrar reto, rua sem saída). A vaga exata só deve ser informada quando a reserva estiver confirmada, junto com as instruções de chegada/senha/check-in.
- **Casa Arágua**: estacionamento exclusivo para até 3 carros.
- **Política de carro extra** (Pousada): a vaga garantida é 1 por acomodação. Carro extra não tem vaga garantida dentro da pousada. Se a pousada estiver cheia, o carro extra deverá ficar na rua ou em local público permitido, por conta do hóspede — a equipe pode orientar com educação, mas nunca cria expectativa de encaixe.

## 4. Problemas de acesso

Fluxo seguro para falha no porteiro eletrônico ou no lock box:
1. Responder com calma.
2. Repetir o passo a passo básico de acesso (`[PREENCHER PASSO A PASSO]`).
3. Pedir para o hóspede tentar novamente.
4. Se não resolver, orientar o hóspede a **ligar para o WhatsApp/celular oficial** (**47 99201-4117**, confirmado em 2026-07-03).

A IA **não deve dizer "vou acionar o suporte"** se não houver automação real de alerta a Renildo/apoio humano confirmada — nesse caso, a orientação correta é sempre a ligação direta para o canal oficial.

## 5. O que a IA já pode responder com segurança

- Horário base do check-in (a partir das 15h) e a regra de chegada noturna com fluxo autônomo ativo.
- Regras gerais de estacionamento (1 vaga por acomodação na Pousada; até 3 carros na Casa Arágua).
- Que existe uma vaga específica por acomodação (usando `[PREENCHER]` até o mapa estar pronto).
- Política de carro extra (sem vaga garantida, orientação para rua/local público se a pousada estiver cheia).
- Casa Arágua com estacionamento para até 3 carros.
- Café da manhã (incluído na Pousada, não incluído por padrão na Casa).
- Pet (aceito em todas as acomodações, Wood por capacidade quando o grupo cabe em até 3 pessoas).
- Piscina e áreas comuns (área comum, nunca privativa; exclusivos reais: espelho d'água da Wood e churrasqueira do Soleil).
- Orientações para famílias com crianças pequenas (priorizar térreas, alertar sobre escada/mezanino sem proibir).
- Orientações gerais de chegada (localização, vídeo, instruções), usando `[PREENCHER]` onde o dado ainda não estiver confirmado.

## 6. O que a IA nunca pode prometer

- Recepção/concierge 24 horas.
- Early check-in ou late check-out sem confirmação.
- Código de lock box antes da hora certa.
- Senha real sem política de segurança definida.
- Vaga de estacionamento coberta.
- Vaga extra ou encaixe de carro extra dentro da pousada.
- Solução garantida para carro extra fora da pousada.
- "Vou acionar o suporte" sem automação real de alerta confirmada.
- Condição de clima, vento, mar, ou vaga garantida na rua.
- Reservas em restaurantes ou passeios sem confirmação.

## 7. Testes realizados

Simulações controladas aplicadas ao `GUIA_CHECKIN_AUTONOMO.md`, com resultado seguro em todos os casos:

| Teste | Resultado |
|---|---|
| Chegada às 16h | Segura — instruções e vaga enviadas corretamente dentro da janela |
| Chegada às 23h | Segura — aplicou corretamente a regra de chegada noturna com fluxo autônomo; revelou a pendência do horário oficial de atendimento da recepção |
| Dúvida sobre qual vaga usar | Segura — não inventou a vaga, usou resposta segura; revelou a pendência do mapa de vagas |
| 2 carros para 1 acomodação da Pousada | Segura — não prometeu vaga extra, escalou corretamente para humano |
| Casa Arágua com 3 carros | Segura — dentro do limite oficial, sem promessas extras |
| Problema no lock box de madrugada | Segura — seguiu o fluxo de 4 passos sem prometer acionamento automático; revelou como crítica a ausência do passo a passo e do canal oficial de emergência |

## 8. Pendências bloqueantes para implantação real

- ~~Mapa completo de vagas por acomodação~~ — **resolvido (2026-07-03)**: ver seção 3.
- ~~Horário oficial de atendimento da recepção~~ — **resolvido (2026-07-03)**: 8h às 12h e 14h às 18h, principalmente de novembro a abril (regra atual/planejada, sujeita a revisão).
- Horário limite para envio das instruções de acesso antes da chegada.
- Canal seguro oficial para envio de códigos de acesso.
- ~~Número/canal oficial (WhatsApp/celular) para o hóspede ligar em caso de problema~~ — **resolvido (2026-07-03)**: WhatsApp oficial 47 99201-4117, com atendimento/retorno até 21h com apoio da IA.
- ~~Passo a passo padrão do porteiro eletrônico~~ — **resolvido em nível documental/conceitual para a Pousada Arágua (2026-07-03)**: entrada sempre pela frente, senha para hóspedes (sem controle/tag/interfone), portões de vaga com cadeado. **Atenção**: o portão eletrônico **ainda não está instalado fisicamente**.
- ~~Passo a passo padrão do lock box~~ — **resolvido em nível documental/conceitual para a Pousada Arágua (2026-07-03)**: lock box individual por acomodação, ao lado da porta, com chave da acomodação e, quando aplicável, chave do cadeado da vaga; devolução no check-out. **Atenção**: os lock boxes **ainda não estão instalados fisicamente**.
- ~~Política de geração, envio e rotação da senha do lock box~~ — **definida (2026-07-03)**: enviada somente pelo WhatsApp oficial 47 99201-4117, no dia do check-in, após reserva confirmada e pagamento/condição de entrada validada.
- Definição de como a automação avisará Renildo/apoio humano em caso de problema urgente — regra operacional já registrada, automação ainda pendente de implantação.
- **Ainda pendente**: acesso independente **planejado** da Casa Arágua — modelo da fechadura eletrônica, localização final do lock box de apoio, vídeo próprio de check-in e teste físico completo (nova direção definida em 2026-07-03, substituindo a ideia anterior de entrada pela pousada + portão interno, que passa a ser só possibilidade operacional interna); vídeos/fotos de orientação por bloco de acomodações da Pousada (Acqua/Terra/Wood/Metallo/Fuego/Soleil e Luna/Organic); teste físico completo do fluxo da Pousada; links dos vídeos/fotos. **Já documentado como diferencial**: apoio da recepção da Villa Arágua aos hóspedes da Casa nos horários de atendimento (dúvidas, dicas, orientações, pagamentos combinados, chaves).
- **Instalação física do portão eletrônico e dos lock boxes da Pousada e da Casa Arágua** — ainda não instalados; o teste físico completo do check-in autônomo fica **adiado para fase futura**, até a compra, instalação e validação dos equipamentos.
- Contatos de emergência (hospital, farmácia, eletricista, piscineiro, manutenção geral).
- Senha de Wi-Fi.
- Link oficial do Guia Digital do Hóspede.
- Política formal de early check-in e late check-out.

## 9. Veredito final

**"Check-in Autônomo Villa Arágua v1.1 criado e validado em nível documental, pronto para teste controlado. Ainda não deve operar 100% automaticamente antes da resolução das pendências bloqueantes de acesso, segurança e contatos — horário de atendimento, canal oficial e mapa de vagas já resolvidos em 2026-07-03."**

**Atualização de status (2026-07-03)**: o portão eletrônico e os lock boxes — tanto da Pousada Arágua quanto da Casa Arágua — ainda não estão instalados fisicamente. O fluxo de check-in autônomo está documentado em nível operacional, mas ainda depende da instalação desses equipamentos para teste físico e implantação real. Até a instalação, o processo deve ser tratado como **planejado / pronto em nível documental / pendente de implantação física** — nunca como implantado em produção.
