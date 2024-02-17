def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def tub_emas(n):
    for num in range(n):
        if not is_prime(num):
            yield num

N =int(input("N="))

tub_emaslar = tub_emas(N)


for non_prime in tub_emaslar:
    print(non_prime)