#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

sorteado = random.randint(1, 100)

tentativas = 0
num = 0 ;
while num != sorteado :
    num = input("escolha um Numero de 1 a 100: ")
    tentativas += 1 
  
    if num == sorteado:
        print "Parabéns você Acertou em %s tentativas." % tentativas 
        break;
    else:
    	if num < sorteado:
        	print "O seu número é menor que o sorteado."
        else:
        	print "O seu número é maior que o sorteado."
