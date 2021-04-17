from typing import List

from ._Train import Train

class Parking(object):
    def __init__(self, trains: List(Train)):
        self.trains = trains