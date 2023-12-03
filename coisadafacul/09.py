time_1 = str(input('Qual é seu primeiro time?'))
time_2 = str(input('Qual é seu segundo time?'))

Gol_time_01 = int(input('Quantos gols o {} fez nesta partida?'.format(time_1)))
Gol_time_02 = int(input('Quantos gols o {} fez nesta partida?'.format(time_2)))

if Gol_time_01 > Gol_time_02:
    print('O {} venceu!'.format(time_1))
if Gol_time_01 < Gol_time_02:
    print('O {} venceu!'.format(time_2)) 
if Gol_time_01 == Gol_time_02:
    print('Empate')       