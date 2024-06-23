class Animal():
    def __init__(self, habitat) -> None:
        self.habitat = habitat
    def add_habi(self, habitat):
        self.habitat = habitat
    def __str__(self):
        return f'I am Animal in {self.habitat}'

class Dog(Animal):
    def __init__(self, habitat) -> None:
        super().__init__(habitat)        
    def __str__(self):
        return f'I am Dog in {self.habitat}'    
    
ann = Animal('Lake')
dgo = Dog('Dessert')
print(ann)
print(dgo)
ann.add_habi('Forest')
print(ann)
dgo.add_habi('Mountain')
print(dgo)
