n1 = float(input('numero:'))
n2 = float(input('numero:'))

ad = n1 + n2
sub = n1 - n2
multi = n1 * n2
div = n1 / n2

operacao = int(input('digite sua operação: adição = 1\n subtração = 2 \n multiplicação = 3\n divisão = 4\n:'))

if operacao == 1:
    print('{}'.format(ad)) 
    
if operacao == 2:
    print('{}'.format(sub)) 
    
if operacao == 3:
    print('{}'.format(multi)) 
    
if operacao == 4:
    print('{}'.format(div)) 
