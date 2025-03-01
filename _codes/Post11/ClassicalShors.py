import numpy as np
import matplotlib.pyplot as plt

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mod_exp(a, b, n):
    result = 1
    a = a % n
    while b > 0:
        if b % 2 == 1:
            result = (result * a) % n
        b //= 2
        a = (a * a) % n
    return result

def shors_algorithm(N, plot=False):
    # Step 1: Choose a random number 'a' such that 1 < a < N
    a = np.random.randint(2, N)
    
    # Step 2: Compute the greatest common divisor of 'a' and 'N'
    if gcd(a, N) != 1:
        return gcd(a, N)
    
    # Step 3: Compute the period r of the function f(x) = a^x mod N
    r = 1
    while True:
        if (a**r) % N == 1:
            break
        r += 1
    
    if r % 2 != 0:
        return None
    
    # Step 4: Determine whether r is even and (a^(r/2)) + 1 or (a^(r/2)) - 1 has a nontrivial factor of N
    candidate1 = gcd(mod_exp(a, r//2, N) + 1, N)
    candidate2 = gcd(mod_exp(a, r//2, N) - 1, N)
    
    if plot:
        x = np.arange(1, r+1)
        y = [mod_exp(a, i, N) for i in x]
        plt.plot(x, y, marker='o')
        plt.title(f"Function $a^x$ mod N for a = {a}, N = {N}")
        plt.xlabel("x")
        plt.ylabel("$a^x$ mod N")
        plt.grid(True)
        plt.show()
    
    if candidate1 != 1 and candidate2 != 1:
        return candidate1, candidate2
    elif candidate1 != 1:
        return candidate1
    elif candidate2 != 1:
        return candidate2
    else:
        return None

# Test the algorithm with a small number
N = 15
result = shors_algorithm(N, plot=True)
print("Factors of", N, ":", result)
