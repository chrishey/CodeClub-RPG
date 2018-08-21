class Room():
 def __init__(self, name, north, south, west, east, item, companion, monster, alerted):
     super().__init__()
     self.name = name
     self.north = north
     self.south = south
     self.west = west
     self.east = east
     self.item = item
     self.monster = monster
     self.alerted = alerted
     self.companion = companion
    
def get_exits(self):
 if(self.north != ''):
  print('North -> ' + self.north)
 if(self.south != ''):
  print('South -> ' + self.south)
 if(self.west != ''):
  print('West -> ' + self.west)
 if(self.east != ''):
  print('East -> ' + self.east)