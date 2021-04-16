from src.entities import Train

class Stack:
    def __init__(self):
        self.train = []

    def isEmpty(self) -> None:
        return self.train == []

    def push(self, item: Train) -> None:
        self.train.insert(0, item)

    def pop(self) -> Train:
        return self.train.pop(0)

    def size(self) -> int:
        return len(self.train)