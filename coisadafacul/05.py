salario = float(input("Digite seu salario: "))
emprestimo = float(input("Digite o valor do emprestimo: "))
mes = int(input('Quantidade de meses a se pagar o emprestimo:'))

valor_prestação = emprestimo/ mes
   

if valor_prestação > salario * 0.2:
    print('Negado')
else:
    print('Aprovado!sua prestação fica {:.2f}reais.'.format(valor_prestação))
    print('a Cada {} meses'.format(mes))

  

