#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import date
import time

try:
    while True:
        nome = raw_input("Qual é o seu nome?\n")
        if nome == 'sair':
            break

        hora_atual = time.strftime("%H")

        if hora_atual < 12:
            saudacao = "Bom dia"
        elif hora_atual > 12 and hora_atual < 18:
            saudacao = "Boa tarde"
        else:
            saudacao = "Boa noite"

        print "{} {}, bem vindo ao nosso sistema.".format(saudacao, nome)
        ano = raw_input("Em que ano você nasceu?\n")
        idade = date.today().year - int(ano)
        print "{}, então você tem ou fará {} anos".format(nome, idade)

        if idade <= 10:
            classificacao = "criança"
        elif idade > 10 and idade <= 13:
            classificacao = "pré-adolescente"
        elif idade > 13 and idade <= 18:
            classificacao = "adolescente"
        elif idade > 18 and idade <= 48:
            classificacao = "adulto"
        else:
            classificacao = "idoso"

        print "Você está classificado como", classificacao
        print "\nPara sair do sistema digite 'sair'"
except Exception, e:
    print "ERRO: Não consigo indentificar a informação digitada."
except KeyboardInterrupt, e:
    print "Obrigado por usar nossos serviços. Volte sempre."
