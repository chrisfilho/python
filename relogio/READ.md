e um codico muito simples .Primeiro voce importa o datetime assim:from datetime import datetime depois de ter feito isso

imprima o conteudo na tela assim:print "aqui está o horario:"' %s:%s' % (now.hour,now.minute)

hh:mm:ss

Para começar, mude a string format para a esquerda do operador %.

Garanta que ela tem 3%s espaçadores temporários.ficando deste modo  %s:%s: %

depois coloque as variaveis now.hour, now.minute não se esqueca de colocar os () antes e depois das tres variaveis e assim sera exibido na tela:
aqui está o horario:(hora atual).

e se esqueceu para que serve o % e %s
aqui esta uma explicaçao;o operador % preencherá os espaços temporátios %s na string à esquerda com as strings nos parênteses à direita.

agora se quiser a data e hora atuais imprima isso;print '%s/%s/%s %s:%s' % (now.month,now.day,now.year,now.hour,now.minute)


 
