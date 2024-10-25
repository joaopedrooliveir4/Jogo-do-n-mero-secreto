# Jogo do Número Secreto

Este é um jogo simples de adivinhação do número secreto, desenvolvido em Python. O jogador tem que adivinhar um número secreto, escolhido aleatoriamente entre 1 e 10, com um limite de tentativas para acertar.

## Como Jogar

1. Ao iniciar o jogo, um número secreto é sorteado aleatoriamente entre 1 e 10.
2. O jogador tem **3 chances** para tentar acertar o número.
3. A cada tentativa, o jogo fornece uma dica se o número secreto é **maior** ou **menor** que o número informado pelo jogador.
4. Se o jogador não conseguir adivinhar o número dentro das 3 tentativas, o jogo termina com um **GAME OVER**.

## Funcionalidades

- O jogo permite que o jogador continue jogando após o **GAME OVER**, se desejar.
- Caso o jogador acerte o número, o jogo informa em quantas tentativas isso ocorreu. O texto da mensagem se ajusta automaticamente entre singular e plural:
  - Exemplo: "Você acertou em 1 tentativa" ou "Você acertou em 3 tentativas".
