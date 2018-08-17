class Room():
 def __init__(self, north, south, west, east, item, monster, alerted):
     super().__init__()
     self.north = north
     self.south = south
     self.west = west
     self.east = east
     self.item = item
     self.monster = monster
     self.alerted = alerted