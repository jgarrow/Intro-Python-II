class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    
    def __str__(self):
        return '{self.name}, {self.description}'.format(self=self)

    def on_take(self):
        print(f'Picked up {self.name}')
    
    def on_drop(self):
        print(f'Dropped {self.name}')

class LightSource(Item):
    def __init__(self, name, description):
        super().__init__(name, description)
    
    def __str__(self):
        return 'LightSource: {self.name}, {self.description}'.format(self=self)
    
    def on_drop(self):
        print(f'It\'s not wise to drop your source of light!\nDropped {self.name}')