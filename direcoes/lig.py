#!/usr/bin/env python
# -*- coding: utf-8 -*-


def feira():

    print 'Voce '  'acabou '  'de '' entrar ' 'no '' mercado!'
    print "Voce vai entrar pelo corredor da (esquerda) da (direita)?"
    pergunta = raw_input(
        "Digite  (esquerda) ou  (direita) e pressione 'Enter'.").lower()
    if pergunta == "esquerda" or pergunta == "l":
        print 'Esta ' 'e '  'o ' 'corredor ' 'das ' 'frutas ', 'agora '  'aqui ' 'ha ' 'uma'  'variedade ' 'delas '
    elif pergunta == "direita" or pergunta == "r":
        print 'este ' ' e ' 'o ' 'corredor da direita' ',aproveite ' 'para ' 'comprar ' ' bolachas.'
    else:
        print "Voce nao escolheu esquerda ou direita. Tente de novo."
        feira()

feira()
