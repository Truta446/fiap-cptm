from typing import List

from src.entities import Parking, Train

# Pilha de patios
class Stack:
    def __init__(self, parkings: List(Train)):
        self.parking = []

    def isEmpty(self) -> None:
        return self.parking == []

    def push(self, item: Parking) -> None:
        self.parking.insert(0, item)

    def pop(self) -> Parking:
        return self.parking.pop(0)

    def size(self) -> int:
        return len(self.parking)