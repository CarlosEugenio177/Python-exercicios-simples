velocidade = float(input('Digite sua distancia em km/h:'))

if velocidade <= 70.0:
    print('você está no limite de velocidade,cuidado!')
else :
    Km = velocidade - 70.0
    multa = Km * 5
    print('sua multa é de {:.2f}R$'.format(multa))