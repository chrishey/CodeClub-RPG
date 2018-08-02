# CodeClub-RPG
A text adventure game for use at Code Club

## Usage

`Base RPG.py` - scafold game structure that allows you to move between rooms and display inventory.

`Expanded RPG.py` - based of the scafold game, added extra rooms, items, monsters. The game can be won and lost, items can be picked up and added to the inventory.

The scripts can be run in [Trinket](https://trinket.io/) via a browser

## How does it work

The rooms, their exits and items are held in a Dicitionary of key/value pairs, the values here are objects that are key/value pairs themselves.

### Expanded game
Entering a room with a monster in will end the game, the objective is to collect the chest and key and escape the house to the garden.
