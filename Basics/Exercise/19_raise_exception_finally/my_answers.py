class AdultException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class Person():
    def __init__(self, name, age) -> None:
        self.name, self.age = name, age

    def get_minor_age(self):
        if self.age>18: raise AdultException('Over 18')
        return self.age
    
    def display_person(self):
        try:
            print(f"Age: {self.get_minor_age()}")
        except AdultException:
            print('is ADULT')
        finally:
            print(f"Name: {self.name}")
p = Person('D', 30)    
p.display_person()