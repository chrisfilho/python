Saudacão e classificação de idade
==============

Desenvolver um programa educado para fazer uma saudação de acordo com o horário atual e, com base no ano de nascimento, exibir sua classificação de faixa etária.
Bom dia, boa tarde, boa noite.
Pergunte o nome do usuário e informe sua idade com sua respectiva classificação por faixa etária: 

**Instruções**
==================
- O sistema deverá solicitar o nome do usuário, para poder fazer o cumprimento adequado;
- A Saudação deverá utilizar os textos: Bom dia, boa tarde ou boa noite;
- As faixas estárias deverão contemplar as seguintes denominações: criança, pré-adolescente, adolescente, adulto ou idoso.

**Exemplo:**
1. ***[Sistema]*** Qual é o seu nome? 
2. ***[Usuário]*** Chris
3. ***[Sistema]*** Bom dia Chris, bem vindo ao nosso sistema
4. ***[Sistema]*** Que ano você nasceu?
5. ***[Usuário]*** 2003
6. ***[Sistema]*** Então você tem ou fará neste ano 12 anos. Você está classificado como pré-adolescente.


**Especificações**
==================
- Nome do script: hello.py
- Permitir que o script seja executável utilizando ./hello.py
- Codificação UTF8
- O script deve ser "teimoso", ou seja, executar a mesma rotina disposta no exemplo acima até que o usuário saia do sistema
- Prover uma forma do usuário sair do sistema caso não queira interromper via teclado (CRTL+C)
- Fazer tratamento de erros (Exception|KeyboardInterrupt)
