# Villa Arágua — Claude Code Agents

Este pacote contém uma primeira versão segura dos subagentes da Villa Arágua para uso no Claude Code dentro do VSCode.

## Como instalar no projeto

1. Abra a pasta do projeto no VSCode.
2. Copie a pasta `.claude` para a raiz do projeto.
3. Se ainda não existir, use o conteúdo de `CLAUDE.example.md` como base para criar ou atualizar o seu `CLAUDE.md`.
4. Abra o terminal do VSCode na raiz do projeto.
5. Inicie o Claude Code.
6. Peça algo como:

```text
Use o agente villa-recepcionista-rascunho para classificar esta conversa e criar uma resposta segura para revisão humana.
```

## Agentes incluídos

- villa-orquestrador-triagem
- villa-recepcionista-rascunho
- villa-comercial-reservas
- villa-operacional-estadia
- villa-risco-escalacao
- villa-experiencia-tom
- villa-precificacao-calendario
- villa-marketing-meta-ads
- villa-aprendizado-manual

## Decisão de arquitetura desta versão

Todos os agentes foram configurados como agentes de leitura e rascunho, usando apenas:

```yaml
tools: Read, Grep, Glob
```

Isso evita que os agentes editem arquivos ou executem ações sem revisão. A fase seguinte pode liberar `Write` ou `Edit` para agentes específicos, mas somente depois de criar regras de governança e pastas de saída seguras.

## Regra de ouro

A IA não envia, não decide preço, não concede desconto, não confirma disponibilidade, não autoriza exceção e não executa automação externa.
