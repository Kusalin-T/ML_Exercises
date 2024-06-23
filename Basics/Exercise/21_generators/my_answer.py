def square_gen():
    n=1
    while True:
        yield n**2
        n+=1

sg = square_gen()
for _ in range(10):
    print(next(sg))       