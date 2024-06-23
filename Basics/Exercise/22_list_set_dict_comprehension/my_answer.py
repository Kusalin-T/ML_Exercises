integer = [0, 1, 2, 3, 4]
binary = ["0", "1", "10", "11", "100"]

print({k:v for k,v in zip(integer, binary)})

integer = [1, -1, 2, 3, 5, 0, -7]
print([-i for i in integer])

integer = [1, -1, 2, -2, 3, -3]
print({i**2 for i in integer})