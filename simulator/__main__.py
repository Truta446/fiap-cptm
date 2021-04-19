from collections import deque
from random import randrange
from time import sleep

from typing import List

from .entities.garage import Garage
from .entities.line import Line
from .entities.network import Network
from .entities.station import Station
from .entities.train import Train
from .timer import Timer


class Simulator:
    def __init__(self):
        self.network = None
        self.timer = None

    def start(self):
        self.timer = Timer('23:00')

        print('Simulação iniciada - %s' % self.timer.get_time())

        trains = deque([])

        for _ in range(0, 4):

            train = Train(name=randrange(
                100, 999), passengers=0, garage_key='Lapa', line='esmeralda', platform='a')

            trains.append(train)

        emerald_stations = [Station('Lapa', garage_link='Lapa'), Station('Osasco'), Station('Carapicuiba'), Station(
            'Barueri')]

        emerald_line = Line(name='esmeralda', stations=emerald_stations)

        lapa_garage = Garage(name='Estação Lapa',
                             cars=trains, key='Lapa', volume=10)

        self.network = Network(lines=[emerald_line], garages=[lapa_garage])

        print('Iniciando movimentação de carros - %s' % self.timer.get_time())

        self.__move_cars()

        print('Simulação finalizada - %s' % self.timer.get_time())

    def __move_cars(self):
        sleep(2)
        self.__move_cars_at_the_station()
        self.__remove_car_from_the_garage()

        self.__move_cars()

    def __remove_car_from_the_garage(self):
        sleep(1)
        print('Removendo carro do pátio - %s' % self.timer.get_time())
        garages = self.network.garages
        lines = self.network.lines

        for garage_index, garage in enumerate(garages):
            for car_index, car in enumerate(garage.cars):
                if(not car):
                    break
                [line_index, line] = self.__find_line_by_name(car.line)

                line_stations = lines[line_index].stations

                [station_index, station] = self.__find_station_by_garage_link(
                    stations=line_stations, garage_key=car.garage_key)

                # Move car to station in destination plataform
                self.network.lines[line_index].stations[station_index].platforms[car.platform] = car
                # Remove car from garage
                del self.network.garages[garage_index].cars[car_index]

                sleep(3)

                print('Carro %s saiu da pátio e entrou no estação %s linha %s na plataforma %s - %s' % (
                    car.name, station.name, line.name.capitalize(), car.platform.upper(), self.timer.get_time()))

                # Break the loop to move one car at a time
                break

    def __find_line_by_name(self, name: str):
        for index, line in enumerate(self.network.lines):
            if line.name == name:
                return index, line

    def __find_station_by_garage_link(self, stations: List[Station],  garage_key: str):
        for index, garage in enumerate(stations):
            if garage.garage_link == garage_key:
                return index, garage

    def __move_cars_at_the_station(self):

        lines = self.network.lines
        for line_index, line in enumerate(lines):
            for station_index in range(len(line.stations) - 1, 0, -1):

                # Checks if the next station is empty, if the car is not moving
                if (line.stations[station_index - 1].platforms['a']):

                    car = line.stations[station_index - 1].platforms['a']

                    line.stations[station_index].platforms['a'] = car

                    print('O carro %s chegou a estação %s - %s' %
                          (car.name, line.stations[station_index].name, self.timer.get_time()))

                    self.network.lines[line_index].stations[station_index -
                                                            1].platforms['a'] = None

                    sleep(5)
