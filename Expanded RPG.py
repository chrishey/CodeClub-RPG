#!/bin/python3

# Replace RPG starter project with this code when new instructions are live

# game ends if you enter a room with a monster

# possible enhancements
# 1. If you have some sort of item you can fight the monster, different monsters, different items to defeat them
# 2. Unlocking the chest with the key wins you the game, not just arriving in a room, add new keywords for 'use', 'with'
# 3. If you find the porg it will warn you of rooms with monsters
# 4. Only allowed to carry 2 items? So introduce that restriction and the ability to drop an item and update the rooms dictionary so it remains in there
# 5. Add an upstairs
# 6. Add some tasks to be able to reveal/find the key and chest

def showInstructions():
  #print a main menu and the commands
  print('''
RPG Game
========

Find the key and the chest then get to the garden, watch out for the monsters!!!

Commands:
  go [direction]
  get [item]
  use [item]
  with [item]
''')

def buildRooms():
  return {
            'Hall' : {
                  'north' : 'Landing',
                  'south' : 'Kitchen',
                  'west' : 'Living Room',
                  'item' : 'key'
                },

            'Kitchen' : {
                  'north' : 'Hall',
                  'east' : 'Dining Room',
                  'item' : 'pan'
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
            },
            "Landing" : {
              'south' : 'Hall',
              'west' : 'Master Bedroom',
              'east' : 'Bathroom'
            },
            "Master Bedroom" : {
              'east' : 'Landing',
              'monster' : True,
              'alerted' : False
            },
            "Bathroom" : {
              'west' : 'Landing',
              'item' : 'medicine'
            }

         }

def showExits(d):
  for k, v in d.items():
    if isinstance(v, dict):
      showExits(v)
    else:
      if(k == 'item' or k == 'monster' or k == 'companion' or k == 'alerted'):
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

  if "companion" in rooms[currentRoom] and rooms[currentRoom]['companion'] not in companions:
    print('You encounter a ' + rooms[currentRoom]["companion"] + ' who wants to help you escape.')
  print("---------------------------")

def monsterDetected():
  return "porg" in companions and 'monster' in rooms[nextRoom] and rooms[nextRoom]['monster'] == True and 'alerted' in rooms[nextRoom] and rooms[nextRoom]['alerted'] == False

def porgAlert():
 print('Your Porg friend is trying to tell you something....THERE IS A MONSTER IN THAT THE ROOM!!')
 print('You shut the door and hope it didnt see you')
 rooms[nextRoom]['alerted']=True
 porg['health'] -= 10
 print('Oh no! Your porg friend has been weakened by the monster.')

 if(porg['health'] <= porg['min-health']):
   print('Your porg friend is poorly, you need to give it some medicine.')

def monsterAttack():
  if 'monster' in rooms[currentRoom] and rooms[currentRoom]['monster'] == True:
    if 'pan' in inventory:
      print('There is a monster in the room!! Luckily you have a frying pan (who knew right?) and you knock the monster out')
      return True
    else:
      print('A monster has caught you!!!! GAME OVER!!!! :-(')
      return False
  
  return True

def gameComplete():
  if(currentRoom == 'Garden' and usedObject == 'key' and move[1] == 'chest'):
    print('YOU HAVE WON!!!!! You escaped the house and unlocked the chest')
    return True
    
  return False

def addItemToInventory(inventory):
  #add the item to their inventory
  inventory += [move[1]]
  #display a helpful message
  print(move[1] + ' got!')
  #delete the item from the room
  del rooms[currentRoom]['item']

  if(len(inventory) > maxInventoryItems):
    # drop the first item in the inventory
    print('You can only carry ' + str(maxInventoryItems) + ' items in your inventory')
    print('You drop the ' + inventory[0] + ' in this room')
    rooms[currentRoom]['item'] = inventory[0]
    del inventory[0]

#an inventory, which is initially empty
inventory = []

companions = []

usedObject = ''

maxInventoryItems = 2

#a dictionary linking a room to other rooms
rooms = buildRooms()

porg = {
  'health' : 50,
  'min-health' : 20
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
      if monsterDetected():
        porgAlert()
      else:
       #set the current room to the new room
       currentRoom = rooms[currentRoom][move[1]]
       #if you enter a room with a monster in it then the game ends
       if monsterAttack() == False:
         break
      if currentRoom == 'Garden':
        if 'chest' in inventory and 'key' in inventory:
          print('You stand in the garden having escaped the house...what do you do now?')
        else:
          missingItem = 'key' if 'key' in inventory else 'chest'
          print('You have escaped the house, but the game is not complete, you need to return and find the ' + missingItem)
      
    #there is no door (link) to the new room
    else:
        print('You can\'t go that way!')

  #if they type 'get' first
  if move[0] == 'get' :
    #if the room contains an item, and the item is the one they want to get
    if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
      addItemToInventory(inventory)
    #otherwise, if the item isn't there to get
    else:
      #tell them they can't get it
      print('Can\'t get ' + move[1] + '!')

  if move[0] == 'use':
    print('What do you want to use the ' + move[1] + ' with?')
    usedObject = move[1]

  if move[0] == "with":
    if usedObject != '':
      print('You use ' + usedObject + ' with ' + move[1])
      if gameComplete():
        break
      usedObject = ''
    else:
      print('What object are you going to use with this? Try the using keyword first.')
