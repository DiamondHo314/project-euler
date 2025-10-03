fib1 = 0
fib2 = 1
sum = 0
n = 4000000

while fib1<n and fib2<n:
    fib1 += fib2
    fib2 += fib1
    if fib1%2==0 and fib1<n:
        sum += fib1
    if fib2%2==0 and fib2<n:
        sum += fib2
print(sum)
