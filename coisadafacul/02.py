from random import randint

computador = randint(0,10)
print('qual numero estou pensando?')
player = int(input('digite:'))

if player == computador:
    print('Parabéns!')
else:
    print('triste...era {},tente dnv'.format(computador))

