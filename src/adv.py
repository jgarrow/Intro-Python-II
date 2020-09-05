from room import Room
from player import Player
from item import Item
import sys

# Declare items

item = {
    'sword': Item('sword', 'A classic soldier\'s weapon that can be wielded with one hand.'),

    'shield': Item('shield', 'A basic metal shield that can be held in one arm.'),

    'spear': Item('spear', 'A steel tipped spear with a wooden shaft. Requires two hands.'),

    'knife': Item('knife', 'A sharp, but short blade. Best suited for close combat.'),

    'torch': Item('torch', 'When lit, this torch can provide light for ~2 hours.'),

    'bow': Item('bow', 'A sniper\'s weapon of choice, the bow is best for long distance combat.'),

    'axe': Item('axe', 'A top heavy weapon that usually requires two hands to wield.')
}

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance", "North of you, the cave mount beckons."),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south."""),
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

# Populate rooms with items

room['outside'].items = [item['sword'], item['shield'], item['spear']]
room['foyer'].items = [item['knife']]
room['narrow'].items = [item['torch']]
room['overlook'].items = [item['bow']]
room['treasure'].items = [item['axe']]

# function to allow user to take an item, drop an item, or keep going
def item_action(room):
    print(f'\nYou see the following items in the {room.name}: ')

    # print('room.items: ', room.items)
    for i in room.items:
        print('\t', i.name)
    
    print('\nYou currently have the following items in your inventory: ')

    for j in player_one.inventory:
        print('\t', j.name)
    
    verb = ''
    desired_item = ''

    # keep prompting for an action until the input is "keep going"
    while verb != 'keep' and desired_item != 'going':
        action = input('\nWhat would you like to do? ').split()

        verb = action[0]

        if len(action) > 1:
            desired_item = action[1]

        if verb == 'take':
            exists = [item for item in player_one.current_room.items if item.name == desired_item]

            # if item exists, remove it from current_room and add to player inventory
            if exists:
                # this method also removes the item from the current_room
                player_one.take_item(exists[0])

        elif verb == 'drop':
            exists = [item for item in player_one.inventory if item.name == desired_item]

            # if item exists, remove it from player inventory and add to current_room
            if exists:
                # this method also adds the item to the current_room
                player_one.drop_item(exists[0])
        elif verb == 'q':
            print('\nGame over!\n')
            sys.exit()
        elif verb == 'keep' and desired_item == 'going':
            break
        else:
            print('\nPlease "take" or "drop" an item or "keep going"')
    
    print(f'\n{player_one.name}\'s current inventory: ')
    for item in player_one.inventory:
        print('\t', item.name)
        
    print(f'\nItems currently in {player_one.current_room.name}: ')
    for item in player_one.current_room.items:
        print('\t', item.name)
     
#
# Main
#

player_name = input('What is your player name? ')

# Make a new player object that is currently in the 'outside' room.
player_one = Player(player_name, room['outside'])

print(f'\nWelcome to {player_one.current_room.name}, {player_one.name}. {player_one.current_room.description}')

# prompt user to take any items before entering cave
item_action(player_one.current_room)

print(f'\nYou are in the {player_one.current_room.name}. {player_one.current_room.description}')

# let's go in the cave!
while player_one.current_room.name != 'Treasure Chamber':

    direction = input('\nWhich direction would you like to go? ')
    print(direction)

    if direction == 'n':
        try:
            if player_one.current_room.n_to != None:
                player_one.move_room(player_one.current_room.n_to)

                print(f'\nYou are now in the {player_one.current_room.name}. {player_one.current_room.description}')

                item_action(player_one.current_room)
            else:
                raise TypeError
        except TypeError:
            print('\nThere is no room to the north\n')
    elif direction == 's':
        try:
            if player_one.current_room.s_to != None:
                player_one.move_room(player_one.current_room.s_to)

                print(f'\nYou are now in the {player_one.current_room.name}. {player_one.current_room.description}')

                item_action(player_one.current_room)
            else:
                raise TypeError
        except TypeError:
            print('\nThere is no room to the south\n')
    elif direction == 'e':
        try:
            if player_one.current_room.e_to != None:
                player_one.move_room(player_one.current_room.e_to)

                print(f'\nYou are now in the {player_one.current_room.name}. {player_one.current_room.description}')

                item_action(player_one.current_room)
            else:
                raise TypeError
        except TypeError:
            print('\nThere is no room to the east\n')
    elif direction == 'w':
        try:    
            if player_one.current_room.w_to != None:
                player_one.move_room(player_one.current_room.w_to)

                print(f'\nYou are now in the {player_one.current_room.name}. {player_one.current_room.description}')

                item_action(player_one.current_room)
            else:
                raise TypeError
        except TypeError:
            print('\nThere is no room to the west\n')
    elif direction == 'q':
        print('\nGame over!\n')
        sys.exit()
    else:
        input('\nPlease choose n, s, e, or w: ')

    # print(player_one)
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
