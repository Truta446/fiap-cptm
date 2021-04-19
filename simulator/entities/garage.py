from typing import List

from .train import Train

class Garage(object):
    def __init__(
        self,
        name: str,
        key: str,
        cars: List[Train]
    ):
        self.name = name
        self.key = key
        self.cars = cars
