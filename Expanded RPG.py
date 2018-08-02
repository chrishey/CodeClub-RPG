#!/bin/python3

# Replace RPG starter project with this code when new instructions are live

# game ends if you enter a room with a monster

# possible enhancements
# 1. If you have some sort of item you can fight the monster, different monsters, different itemss to defeat them
# 2. Unlocking the chest with the key wins you the game, not just arriving in a room
# 3. If you find the porg it will warn you of rooms with monsters


def showInstructions():
  #print a main menu and the commands
  print('''
RPG Game
========
Commands:
  go [direction]
  get [item]
''')

def showExits(d):
  for k, v in d.items():
    if isinstance(v, dict):
      showExits(v)
    else:
      if(k == 'item'):
        continue
      print('\t' * 2, "{0} -> {1}".format(k, v))


def showStatus():
  #print the player's current status
  print('---------------------------')
  print('You are in the ' + currentRoom)
  print('Your exits are : ')
  
  showExits(rooms[currentRoom])
  
  #print the current inventory
  print('Inventory : ' + str(inventory))
  #print an item if there is one
  if "item" in rooms[currentRoom]:
    print('You see a ' + rooms[currentRoom]['item'])
  print("---------------------------")

#an inventory, which is initially empty
inventory = []

#a dictionary linking a room to other rooms
rooms = {

            'Hall' : { 
                  'south' : 'Kitchen',
                  'west' : 'Living Room',
                  'item' : 'key'
                },

            'Kitchen' : {
                  'north' : 'Hall',
                  'east' : 'Dining Room',
                  'item' : 'spoon'
                },
            'Living Room' : {
              'east' : "Hall",
              'north' : "Library",
              'item' : 'monster'
            },
            "Library" : {
              'south' : 'Living Room',
              'north' : 'Garden',
              'item' : 'chest'
            },
            "Dining Room" : {
              'west' : 'Kitchen',
              'north' : 'Study'
            },
            "Study" : {
              'west' : 'Library',
              'south' : 'Dining Room'
            },
            "Garden" : {
              'south' : 'Library'
            }

         }

#start the player in the Hall
currentRoom = 'Hall'

showInstructions()

#loop forever
while True:

  showStatus()

  #get the player's next 'move'
  #.split() breaks it up into an list array
  #eg typing 'go east' would give the list:
  #['go','east']
  move = ''
  while move == '':  
    move = input('>')
    
  move = move.lower().split()

  #if they type 'go' first
  if move[0] == 'go':
    #check that they are allowed wherever they want to go
    if move[1] in rooms[currentRoom]:
      #set the current room to the new room
      currentRoom = rooms[currentRoom][move[1]]
      #if you enter a room with a monster in it then the game ends
      if 'item' in rooms[currentRoom] and rooms[currentRoom]['item'] == 'monster':
        print('A monster has caught you!!!! GAME OVER!!!! :-(')
        break
      if currentRoom == 'Garden' and 'chest' in inventory and 'key' in inventory:
        print('YOU HAVE WON!!!!! You escaped the house and unlocked the chest')
        break
      
    #there is no door (link) to the new room
    else:
        print('You can\'t go that way!')

  #if they type 'get' first
  if move[0] == 'get' :
    #if the room contains an item, and the item is the one they want to get
    if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
      #add the item to their inventory
      inventory += [move[1]]
      #display a helpful message
      print(move[1] + ' got!')
      #delete the item from the room
      del rooms[currentRoom]['item']
    #otherwise, if the item isn't there to get
    else:
      #tell them they can't get it
      print('Can\'t get ' + move[1] + '!')

