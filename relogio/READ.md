PRIMEIRO como sempre utilize #!/usr/bin/env python
                             # -*- coding: utf-8 -*-



SEGUNDO importe a função datetime usando from datetime import datetime

logo apos:

print "hoje e dia %s " % datetime.now().day
print "do mes %s " % datetime.now().month
print "do ano de %s " % datetime.now().year



se ficou em duvida com o % ou o %s vou explicar.O operador % depois de uma string é usado para combinar uma string com variáveis. O operador % substituirá um %s na string pela variável string que vem depois dele.
