#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import time


def data_valida(data):
    try:
        date = time.strptime(data, '%d/%m/%Y')
    except ValueError:
        return False

    return True

print 'Bem vindo a pagina'

nome = senha = nascimento = ""

cadastrado = False
while not cadastrado:
    if not nome:
        nome = raw_input("Insira o seu nome completo: ")
        if len(nome) < 6:
            print "É necessario ter pelo menos 6 letras."
            nome = ""
        continue

    if not senha:
        senha = raw_input("Agora sua senha:")
        if len(senha) < 6 or len(senha) > 12:
            print" sua senha tem que ter entre 6 e 12 dígitos."
            senha = ""
        continue

    if not nascimento:
        nascimento = raw_input("Agora sua data de nascimento:")
        if not data_valida(nascimento):
            print('Data inválida!')
            nascimento = ""

        continue

    cadastrado = True


print "Parabens agora voce e cadastrado na pagina"
print "Aproveite nossos servicos"
print "Seu nome: %s" % nome

print "Sua senha: %s" % senha

print "Sua data: %s" % nascimento
