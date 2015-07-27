#! /usr/bin/env python
# -*- coding: iso-8859-1 -*-

import urllib
import cgi


cep_busca = raw_input('digite o deu CEP:')
if len(cep_busca) <= 6:
    print "CEP não encontrado ou invalido"


url = "http://cep.republicavirtual.com.br/web_cep.php?cep=" + \
    cep_busca + "&formato=query_string"
pagina = urllib.urlopen(url)
conteudo = pagina.read()
resultado = cgi.parse_qs(conteudo)

if resultado['resultado'][0] == '1':
    print "endereço desejado: "
    print resultado['tipo_logradouro'][0]
    print resultado['logradouro'][0]
    print resultado['bairro'][0]
    print resultado['cidade'][0]
    print resultado['uf'][0]
elif resultado['resultado'][0] == '2':
    print "Endereço desejado: "
    print resultado['cidade'][0]
    print resultado['uf'][0]
else:
    print "CEP não encontrado ou invalido"
