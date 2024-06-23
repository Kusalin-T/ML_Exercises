import threading
import time

def timeit(func):
    def wrapper(*args, **kwargs):
        start=time.time()
        result=func(*args, **kwargs)
        end=time.time()
        print(f"{func.__name__} took {(end-start):.2f}s")
        return result
    return wrapper

@timeit
def facc(n):
    acc=1
    for i in range(n):
        time.sleep(0.1)
        acc*=i
    return acc    

@timeit
def cubes(n):
    acc=1
    for i in range(n):
        time.sleep(0.1)
        acc+=i**3
    return acc   

for i in range(10):
    th = threading.Thread(target=facc, args=(i,))
    th.start()
    print(f"Current Threads: {threading.active_count()}")