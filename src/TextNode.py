from enum import Enum

# Base class for game objects
class textnode(Enum):
    def __init__(self, text, text_type, url):
        self.text = text
        self.text_type = text_type
        self.url = url

    def fart(self):
        print (self.text)
        print (self.text_type)
        print (self.text_type)

# class Bender(Enum):
#     AIR_BENDER = "air"
#     WATER_BENDER = "water"
#     EARTH_BENDER = "earth"
#     FIRE_BENDER = "fire"