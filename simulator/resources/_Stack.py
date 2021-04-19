from typing import List

from ..entities import Train

class Stack:
    def __init__(self):
        self.trains = []

    def isEmpty(self) -> None:
        return self.trains == []

    def push(self, item: Train) -> None:
        self.trains.insert(0, item)

    def pop(self) -> Train:
        return self.trains.pop(0)

    def size(self) -> int:
        return len(self.trains)

    def get(self) -> List[Train]:
        return self.trains