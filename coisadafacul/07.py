ano_atual = int(input('digite o ano atual:'))
ano_nascimento = int(input('digite seu de nascimento:'))

votacao = (ano_atual - ano_nascimento)

if votacao < 18 :
    print('você não está habito para votar')
    print('sua idade é {:.1f}'.format(votacao))
if votacao >= 18:
    print('você está habito para votar')
    print('sua idade é {:.1f}'.format(votacao))

