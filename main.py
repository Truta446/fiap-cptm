from time import sleep

from src.resources import Stack, Queue
from src.entities import Train, Parking


def main():
    # qty_trains = int(input('Digite a quantidades de trens a serem atendidos: '))
    qty_trains = 102

    # Filas de saida dos patios
    queue_lapa = Queue()
    queue_altino = Queue()
    queue_calmon_viana = Queue()
   
    #Pilha de carros no patio
    #, "Carro 6", "Carro 7","Carro 8","Carro 9","Carro 10","Carro 11","Carro 12","Carro 13","Carro 14","Carro 15","Carro 16","Carro 17",
    trem = Train("Carro 1", "Tipo 1")
    parking_lapa = Parking([trem, trem, trem, trem, trem])
    parking_altino = Parking([trem, trem, trem, trem, trem, trem, trem, trem, trem])
    parking_calmon_viana = Parking([trem, trem, trem, trem, trem, trem, trem, trem, trem])
    stack = Stack([parking_lapa, parking_altino, parking_calmon_viana ])

    saida_por_patio = dividir_por_patios(qty_trains)

    # Criar um for para tirar os trens das filas e enviar para a manutencao
    for x in range(1, qty_trains, 3):
        print(stack[0])
        print(queue_lapa)
        len_lapa = len(stack[0] - 1)
        queue_lapa.push(stack[0][len_lapa])
        stack[0][len_lapa].pop()
        print(stack[0])
        print(queue_lapa)


    #    ----

       #Remover um trem do altino e colocar na fila
        # ----
    
        #Remover um trem da calmon e colocar na fila
       


    for _ in range(0, 3):
        code = input('Digite o coigo do trem: ')
        type = input('Digite o tipo do trem: ')

        train = Train(code=code, type=type)

        stack.push(train)

        # print(f'\n{code} inserido na pilha com sucesso!\n')

    # train = stack.pop()

    # print(f'Trem {train.code} utilizado com sucesso. Tempo medio de servico de 2 horas.')

    # train = stack.pop()

    # print(f'Trem {train.code} utilizado com sucesso. Tempo medio de servico de 2 horas.')

main()