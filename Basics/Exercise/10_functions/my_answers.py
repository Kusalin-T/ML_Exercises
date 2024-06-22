def calculate_area(base, height, shape):
    if shape=='rectangle':
        return base*height
    return .5*base*height

def print_pattern(n):
    print(''.join(''.join(['*' for _ in range(i+1)]) + '\n' for i in range(n)))

print_pattern(5)