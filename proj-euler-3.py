import math
#project euler 3
n = 600851475143
sqrt_n = math.sqrt(n)
primes = []
for i in range(2,int(sqrt_n)):
    if n%i==0:
        j = 0
        for k in range(1,i+1):
            if i%k == 0:
                j += 1
        if j == 2:
            primes.append(i)

largest_factor = max(primes)
print(largest_factor)