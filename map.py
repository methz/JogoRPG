from random import randint

class Map:
    def __init__(self):
        self.maps = ['Brasil', 'China', 'Polo Norte', 'Acre']
    
    def getRandomMap(self):
        mapId = randint(0, len(self.maps) - 1)
        return self.maps[mapId]