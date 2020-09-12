# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    # initialize all room directions to None so you don't have to pass any of those values in to create an instance of a Room
    # initialize items in room as empty list
    def __init__(self, name, description, n_to=None, s_to=None, e_to=None, w_to=None, items=[]):
        self.name = name
        self.description = description
        self.n_to = n_to
        self.s_to = s_to
        self.e_to = e_to
        self.w_to = w_to
        self.items = items
    
    def __str__(self):
        return '{self.name} -- \nDescription: {self.description}\nItems: {self.items}'.format(self=self)

    def add_item(self, new_item):
        self.items.append(new_item)
    
    def remove_item(self, item):
        # remove the item from the room's items
        for i, itm in enumerate(self.items):
            if itm.name == item.name:
                self.items.pop(i)
                break # so we only remove 1 matching item