class FibIter():
    def __init__(self, n):
        self.a, self.b, self.n = 0, 1, n

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.a+self.b > self.n:
            raise StopIteration  
        self.a, self.b = self.b, self.a+self.b
        return self.a      

ff = FibIter(100)
print(next(ff))    
print(next(ff))    
print(next(ff))    
print(next(ff))    
print(next(ff))    
print(next(ff))    
print(next(ff))    
print(next(ff))    
print(next(ff))    
