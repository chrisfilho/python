#!/usr/bin/env python
# -*- coding: utf-8 -*-

pergunta = 256

erros = 0
perg = 1
while perg != pergunta:
    perg = input("quanto e 16*16:")
    erros += 1

    if perg == pergunta:
        print "Parabéns você Acertou com %s erros." % erros
        break
    else:
        if perg != pergunta:
            print "sinto muito mas sua resposta esta errada."

per = 216

erros = 1

while per != pergunta:
    per = input("agora 18*12:")
    erros += 1

    if perg == pergunta:
        print "Parabéns você Acertou com %s erros." % erros
        break
    else:
        if per != pergunta:
            print "sinto muito mas sua resposta esta errada"


per = 528

erros = 1

while per != pergunta:
    per = input("por ultimo vamos ver se voce e bom mesmo 22*24:")
    erros += 1

    if perg == pergunta:
        print "Parabéns você Acertou com %s erros." % erros
        break
    else:
        if per != pergunta:
            print "sinto muito mas sua resposta esta errada"


print "muito obrigado por jogar esse quiz"
