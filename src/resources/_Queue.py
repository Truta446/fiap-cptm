from src.entities import Train

class Queue:
    def __init__(self):
        self.train = []

    def isEmpty(self) -> None:
        return self.train == []

    def enqueue(self, item: Train) -> None:
        self.train.append(item)

    def dequeue(self) -> Train:
        return self.train.pop(0)

    def size(self) -> int:
        return len(self.train)
