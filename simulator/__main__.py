from random import randrange
from time import sleep
from typing import List

from .const import TIME_OF_TRAVEL, MAINTENANCE_TIME
from .entities import Garage, Line, Network, Station, Train
from .resources import Stack, Timer

class Simulator:
    def __init__(self):
        self.network = None
        self.timer = None

    def start(self) -> None:
        self.timer = Timer('23:00')

        qty_trains = int(input('Digite a quantidade de trens: '))

        print(f'Simulação iniciada - {self.timer.get_time()}')

        diamond_garage = Stack()
        emerald_garage = Stack()
        sapphire_garage = Stack()

        for i in range(0, qty_trains):
            if i % 3 == 0:
                train = Train(
                    name=randrange(100, 999),
                    garage_key='Lapa',
                    line='diamante',
                    platform='a'
                )

                diamond_garage.push(train)
            elif i % 3 == 1:
                train = Train(
                    name=randrange(100, 999),
                    garage_key='Altino',
                    line='esmeralda',
                    platform='a'
                )

                emerald_garage.push(train)
            else:
                train = Train(
                    name=randrange(100, 999),
                    garage_key='Calmon Viana',
                    line='safira',
                    platform='a'
                )

                sapphire_garage.push(train)

        diamond_stations = [
            Station('Lapa', garage_link='Lapa'),
            Station('Osasco'),
            Station('Carapicuiba'),
            Station('Barueri')
        ]

        emerald_stations = [
            Station('Altino', garage_link='Altino'),
            Station('Pinheiros'),
            Station('Vila Olimpia'),
            Station('Morumbi')
        ]

        sapphire_stations = [
            Station('Calmon Viana', garage_link='Calmon Viana'),
            Station('Itaquaquecetuba'),
            Station('Itaim Paulista'),
            Station('Tatuapé')
        ]

        diamond_line = Line(name='diamante', stations=diamond_stations)
        emerald_line = Line(name='esmeralda', stations=emerald_stations)
        sapphire_line = Line(name='safira', stations=sapphire_stations)

        lapa_garage = Garage(
            name='Estação Lapa',
            cars=diamond_garage.get(),
            key='Lapa',
        )

        altino_garage = Garage(
            name='Estação Lapa',
            cars=emerald_garage.get(),
            key='Lapa',
        )

        calmon_garage = Garage(
            name='Estação Calmon Viana',
            cars=sapphire_garage.get(),
            key='Calmon Viana',
        )

        self.network = Network(
            lines=[diamond_line, emerald_line, sapphire_line],
            garages=[lapa_garage, altino_garage, calmon_garage]
        )

        print(f'Iniciando movimentação de carros - {self.timer.get_time()}')

        self.__move_cars()

        print(f'Simulação finalizada - {self.timer.get_time()}')

    def __move_cars(self) -> None:
        sleep(2)
        self.__move_cars_at_the_station()
        self.__remove_car_from_the_garage()
        sleep(TIME_OF_TRAVEL)

        self.__move_cars()

    def __remove_car_from_the_garage(self) -> None:
        sleep(1)
        garages = self.network.garages
        lines = self.network.lines

        for garage_index, garage in enumerate(garages):
            for car_index, car in enumerate(garage.cars):
                if(not car):
                    break

                print(f'Removendo carro do pátio - {self.timer.get_time()}')

                [line_index, line] = self.__find_line_by_name(car.line)

                line_stations = lines[line_index].stations

                [station_index, station] = self.__find_station_by_garage_link(
                    stations=line_stations,
                    garage_key=car.garage_key
                )

                # Move car to station in destination platform
                self.network.lines[line_index].stations[station_index].platforms[car.platform] = car
                
                # Remove car from garage
                del self.network.garages[garage_index].cars[car_index]

                sleep(TIME_OF_TRAVEL)

                print(f'Carro {car.name} saiu do pátio e entrou na estação {station.name} linha {line.name.capitalize()} na plataforma {car.platform.upper()} - {self.timer.get_time()}')

                # Break the loop to move one car at a time
                break

    def __find_line_by_name(self, name: str) -> (int, Line):
        for index, line in enumerate(self.network.lines):
            if line.name == name:
                return index, line

    def __find_station_by_garage_link(self, stations: List[Station],  garage_key: str) -> (int, Garage):
        for index, garage in enumerate(stations):
            if garage.garage_link == garage_key:
                return index, garage

    def __move_cars_at_the_station(self) -> None:

        lines = self.network.lines

        def move_in_plataform_a(line_index: int, line: Line) -> None:
            for station_index in range(len(line.stations) - 1, 0, -1):

                # Checks if the next station is empty, if the car is not moving
                if (line.stations[station_index - 1].platforms['a']):

                    car = line.stations[station_index - 1].platforms['a']

                    line.stations[station_index].platforms['a'] = car

                    print(f'O carro {car.name} chegou a estação {line.stations[station_index].name} na plataforma A - {self.timer.get_time()}')

                    if line.stations[station_index].garage_link == car.garage_key:
                        clean_car(car.name, line.stations[station_index].name)

                    self.network.lines[line_index].stations[station_index - 1].platforms['a'] = None

                    return

        def move_in_plataform_b(line_index: int, line: Line) -> None:
            for station_index in range(len(line.stations) - 1):

                # Checks if the next station is empty, if the car is not moving
                if (line.stations[station_index + 1].platforms['b']):

                    car = line.stations[station_index + 1].platforms['b']

                    line.stations[station_index].platforms['b'] = car

                    print(f'O carro {car.name} chegou a estação {line.stations[station_index].name} na plataforma B - {self.timer.get_time()}')

                    if line.stations[station_index].garage_link == car.garage_key:
                        clean_car(car.name, line.stations[station_index].name)

                    self.network.lines[line_index].stations[station_index + 1].platforms['b'] = None

                    return

        def change_car_plataform(line: Line) -> None:
            if(line.stations[-1].platforms['a']):
                print(f'Mudando trêm de plataforma na estação {line.stations[-1].name}')
                line.stations[-1].platforms['b'] = line.stations[-1].platforms['a']
                line.stations[-1].platforms['a'] = None

            if(line.stations[0].platforms['b']):
                print(f'Mudando trêm de plataforma na estação {line.stations[0].name}')
                line.stations[0].platforms['a'] = line.stations[0].platforms['b']
                line.stations[0].platforms['b'] = None

        def clean_car(train_name: str, station_name: str) -> None:
            print(f'Iniciando manutenção no trem {train_name} em {station_name} - {self.timer.get_time()}')

            sleep(MAINTENANCE_TIME)

            print(f'Manutenção no trem {train_name} em {station_name} finalizada com sucesso! - {self.timer.get_time()}')

        for line_index, line in enumerate(lines):
            move_in_plataform_a(line_index, line)
            move_in_plataform_b(line_index, line)
            change_car_plataform(line)
