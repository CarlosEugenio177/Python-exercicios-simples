n1 = float(input('digite sua nota:'))
n2 = float(input('digite sua nota:'))

n3 = float(input('digite sua nota:'))
n4 = float(input('digite sua nota:'))

n5 = float(input('digite sua nota:'))
n6 = float(input('digite sua nota:'))

n7 = float(input('digite sua nota:'))
n8 = float(input('digite sua nota:'))


media = (n1 + n2 + n3 + n4 )/4 + (+ n5 + n6 + n7 + n8)/4 

print('sua media é {:.1f}'.format(media))

if media >= 7:
    print('aprovado')

elif media == 4:
    print('reprovado')

else:
    print('recuperação')
