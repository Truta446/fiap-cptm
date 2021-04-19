from typing import List

from .station import Station


class Line(object):
    def __init__(self, name: str, stations: List[Station]):
        self.name = name
        self.stations = stations
