class Train():
    def __init__(self, name: str, platform: str, line: str, passengers: int, garage_key: str, current_garage_key: str = None):
        self.name = name
        self.passengers = passengers
        self.garage_key = garage_key
        self.current_garage_key = current_garage_key
        self.line = line
        self.platform = platform
