from time import sleep

from src.resources import Stack
from src.entities import Train

def main() -> None:
    stack = Stack()

    for _ in range(0, 3):
        code = input('Digite o código do trem: ')
        type = input('Digite o tipo do trem: ')

        train = Train(code=code, type=type)

        stack.push(train)

        print(f'\n{code} inserido na pilha com sucesso!\n')

    train = stack.pop()

    print(f'Trem {train.code} utilizado com sucesso. Tempo médio de serviço de 2 horas.')

    train = stack.pop()

    print(f'Trem {train.code} utilizado com sucesso. Tempo médio de serviço de 2 horas.')

main()