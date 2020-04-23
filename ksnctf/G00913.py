import math

pi = math.pi

def is_prime(num):
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return i
    return 0

for i in range(50):
    pi = (pi * 10) % (10 ** 10)
    print(int(pi), ": ",is_prime(int(pi)))
