"""""
Constante= "variaveis" que nunca vai mudar
Muitas condições no mesmo if (ruim)
    <-contagem de complexidade (ruim)
"""""

#Ex: O contratante do serviço quer saber se o carro passou da velocidade permitida pelo radar.

velocidade = 61 # velocidade atual do carro.
local_carro = 100 # km em que o carro está na estrada.

#variaveis com letras maisculas quer dizer que não pode ser mudada. Não atribuir outros valores.

RADAR_1 = 60 #velocidade máxima do radar 1
LOCAL_1 = 100 # local onde o radar 1 está
RADAR_RANGE = 1 #A distância onde o radar pega.

velocidade_carro_passou_radar_1 = velocidade > RADAR_1
carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE)
carro_multado_radar1 = carro_passou_radar_1 and velocidade_carro_passou_radar_1

if velocidade_carro_passou_radar_1:
    print("Veículo ultrapassou a velocidade no radar 1.")

if carro_passou_radar_1:
    print('Carro passou no radar 1.')

if carro_multado_radar1:
    print('Carro multado em radar 1.')

