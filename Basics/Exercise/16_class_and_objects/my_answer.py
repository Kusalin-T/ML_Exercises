class Employee():
    def __init__(self, id, name):
        self.id, self.name = id, name
    def __str__(self):
        return f"ID: {self.id}\nNAME: {self.name}"    
    
em = Employee(3, 'hello')    
print(em)
del em.id
del em