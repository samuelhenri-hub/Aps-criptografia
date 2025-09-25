# 🔐 Programa de Criptografia - Cifra de César  

Este projeto implementa um programa em Python que realiza **criptografia e descriptografia** de mensagens utilizando a **Cifra de César**.  

O sistema permite que o usuário insira uma mensagem e uma chave de deslocamento para codificá-la ou decodificá-la.  

---

## 📌 Funcionalidades  

- Menu interativo com opções de:
  - Criptografar mensagem  
  - Descriptografar mensagem  
  - Encerrar o programa  

- Validações de entrada:
  - Apenas números inteiros aceitos para chave e opção  
  - Chave não pode ser `0`  
  - Mensagem não pode estar vazia  

- Suporte a letras maiúsculas e minúsculas (padroniza para minúsculo na saída).  
- Caracteres que não são letras (números, espaços, pontuação) **não são alterados**.  

---

## 📖 Como funciona  

O programa utiliza a **Cifra de César**, uma técnica clássica de criptografia de substituição, onde cada letra da mensagem é deslocada um número fixo de posições no alfabeto.  

- **Criptografar (opção 1):**  
  Cada letra é deslocada para frente no alfabeto de acordo com a chave.  

- **Descriptografar (opção 2):**  
  Cada letra é deslocada para trás no alfabeto de acordo com a chave.  

Exemplo:  
```text
Mensagem: "abc"
Chave: 2
Criptografada: "cde"
Descriptografada (com a mesma chave): "abc"
