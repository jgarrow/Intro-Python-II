# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    # initialize inventory as empty list
    def __init__(self, name, current_room, inventory=[]):
        self.name = name
        self.current_room = current_room # will be instance of Room
        self.inventory = inventory
    
    def __str__(self):
        return '{self.name}, {self.current_room}, Inventory: {self.inventory}'.format(self=self)
    
    def move_room(self, new_room):
        self.current_room = new_room

    def take_item(self, item):
        # add to player inventory
        self.inventory.append(item)
        item.on_take()

        # remove item from current_Room
        self.current_room.remove_item(item)
    
    def drop_item(self, drop_item):
        # add the item to the current_room
        self.current_room.add_item(drop_item)
        drop_item.on_drop()

        # remove the item from the player's inventory
        for i, item in enumerate(self.inventory):
            if item.name == drop_item.name:
                self.inventory.pop(i)
                break # so we only remove 1 matching item