credito = float(input('digite seu credito:'))
debito = float(input('digite seu debito:'))
saldo_total = credito - debito

if saldo_total >= 0:
    print('Parabens!Saldo positivo')
    print('Valor {:.2f} reais'.format(saldo_total))
else:
    print('Saldo negativado! valor {:.2f}'.format(saldo_total))