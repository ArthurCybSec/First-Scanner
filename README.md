# Meu Primeiro Scanner de Portas em Python

Este é o meu primeiro projeto de cibersegurança, desenvolvido como uma intrução de um projeto simples. O objetivo é criar uma ferramenta extremamente simples para identificar portas TCP abertas em um host.

## 🚀 Sobre o Projeto

A ferramenta funciona conectando-se a uma lista predefinida de portas em um alvo. Se a conexão for bem-sucedida, a porta é considerada "ABERTA". Este é um passo fundamental em auditorias de segurança e testes de invasão.

## 🛠️ O que eu usei?

* Linguagem: **Python 3**
* Biblioteca Principal: **`socket`** (para a comunicação de rede)

## 👨‍💻 Como funciona?

O script tenta estabelecer uma conexão TCP em portas comuns como 21, 22, 80, 443, etc. O alvo padrão é `localhost` (a própria máquina), para que qualquer pessoa possa testar com segurança.

## O que foi mostrado neste projeto?

* **Programação em Python:** Como usar laços, variáveis e tratamento de exceções (`try...except`).
* **Redes de Computadores:** O conceito de portas, sockets e o protocolo TCP.
* **Cibersegurança:** O princípio básico da fase de "Reconhecimento" 
