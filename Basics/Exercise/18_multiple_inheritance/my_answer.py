class Teacher():
    def __init__(self):
        #Its weird how super needs to be called here so the Student class can use Youtuber's init
        super().__init__()
        print('Am Teacher')

class Youtuber():
    def __init__(self):
        print('Am Youtuber')

class Student(Teacher, Youtuber):
    def __init__(self):
        #Some say calling the class directly is better:
        #Teacher.__init__(self)
        #Youtuber.__init__(self)
        super().__init__()
        print('Am Student')
    #super() only calls Teacher class method
    
st = Student()
print(Student.__mro__)
