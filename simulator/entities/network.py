from typing import List

from .garage import Garage
from .line import Line

class Network(object):
    def __init__(self, lines: List[Line], garages: List[Garage]):
        self.lines = lines
        self.garages = garages
