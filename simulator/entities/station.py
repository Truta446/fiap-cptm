class Station(object):
    def __init__(self, name: str, garage_link: str = None):
        self.name = name
        self.garage_link = garage_link
        self.platforms = {"a": None, "b": None}
