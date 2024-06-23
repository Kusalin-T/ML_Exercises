
def nonneg(func):
    def wrapper(*args, **kwargs):
        if args[0]<0:
            raise Exception('NEGATIVE')
        return func(*args, **kwargs)
    return wrapper    

@nonneg
def addd(n):
    return n+1

@nonneg
def fac(n):
    acc=1
    for i in range(n):
        acc *= i+1
    return acc

print(fac(5))