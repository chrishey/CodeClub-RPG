#!/bin/python3

# Replace RPG starter project with this code when new instructions are live

# game ends if you enter a room with a monster

# possible enhancements
# 1. If you have some sort of item you can fight the monster, different monsters, different items to defeat them
# 2. Unlocking the chest with the key wins you the game, not just arriving in a room
# 3. If you find the porg it will warn you of rooms with monsters
# 4. Only allowed to carry 2 items? So introduce that restriction and the ability to drop an item and update the rooms dictionary so it remains in there

def showInstructions():
  #print a main menu and the commands
  print('''
RPG Game
========

Find the key and the chest then get to the garden, watch out for the monsters!!!

Commands:
  go [direction]
  get [item]
''')

def showExits(d):
  for k, v in d.items():
    if isinstance(v, dict):
      showExits(v)
    else:
      if(k == 'item' or k == 'monster' or k == 'companion'):
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
  print('Companions : ' + str(companions))

  #print an item if there is one
  if "item" in rooms[currentRoom]:
    print('You see a ' + rooms[currentRoom]['item'])

  if "companion" in rooms[currentRoom]:
    print('You encounter a ' + rooms[currentRoom]["companion"] + ' who wants to help you escape.')
  print("---------------------------")

#an inventory, which is initially empty
inventory = []

companions = []

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
                  'item' : 'frying-pan'
                },
            'Living Room' : {
              'east' : "Hall",
              'north' : "Library",
              'monster' : True,
              'alerted' : False
            },
            "Library" : {
              'south' : 'Living Room',
              'north' : 'Garden',
              'item' : 'chest'
            },
            "Dining Room" : {
              'west' : 'Kitchen',
              'north' : 'Study',
              'companion' : 'porg'
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

  if "companion" in rooms[currentRoom]:
    companions += [rooms[currentRoom]["companion"]]

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
      nextRoom = rooms[currentRoom][move[1]]
      # if they have the porg and there is a monster then alert them!
      if "porg" in companions and 'monster' in rooms[nextRoom] and rooms[nextRoom]['monster'] == True and 'alerted' in rooms[nextRoom] and rooms[nextRoom]['alerted'] == False:
        print('Your Porg friend is trying to tell you something....THERE IS A MONSTER IN THE ROOM!!')
        rooms[nextRoom]['alerted']=True
        break

      #set the current room to the new room
      currentRoom = rooms[currentRoom][move[1]]
      #if you enter a room with a monster in it then the game ends
      if 'monster' in rooms[currentRoom] and rooms[currentRoom]['monster'] == True:
        if 'frying pan' in inventory:
         print('There is a monster in the room!! Luckily you have a frying pan (who knew right?) and you knock the monster out')
        else:
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