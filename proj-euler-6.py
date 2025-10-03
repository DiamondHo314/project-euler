sum = 0
square = 0
for i in range(1, 101):
    sum += i**2
    square += i
square = square**2
diff = square - sum
print(diff)