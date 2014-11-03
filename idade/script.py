#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime

ano = datetime.now().year
idade = raw_input("Qual sua idade?\n")
nascimento = ano - int(idade)
print "Você nasceu em %s " % nascimento
