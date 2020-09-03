from room import Room
from player import Player
import sys

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player_one = Player('Player One', room['outside'])

print(player_one)

while player_one.current_room.name != 'Treasure Chamber':

    direction = input('Which direction would you like to go? ')
    print(direction)

    if direction == 'n':
        try:
            if player_one.current_room.n_to != None:
                player_one.move_room(player_one.current_room.n_to)
            else:
                raise TypeError
        except TypeError:
            print('There is no room to the north\n')
    elif direction == 's':
        try:
            if player_one.current_room.s_to != None:
                player_one.move_room(player_one.current_room.s_to)
            else:
                raise TypeError
        except TypeError:
            print('There is no room to the south\n')
    elif direction == 'e':
        try:
            if player_one.current_room.e_to != None:
                player_one.move_room(player_one.current_room.e_to)
            else:
                raise TypeError
        except TypeError:
            print('There is no room to the east\n')
    elif direction == 'w':
        try:    
            if player_one.current_room.w_to != None:
                player_one.move_room(player_one.current_room.w_to)
            else:
                raise TypeError
        except TypeError:
            print('There is no room to the west\n')
    elif direction == 'q':
        print('\nGame over!\n')
        sys.exit()
    else:
        input('Please choose n, s, e, or w: ')

    print(player_one)
    print('\n')

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
