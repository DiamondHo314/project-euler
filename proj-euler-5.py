thenumber = None
j = 2520
while True:
    j += 20 #but why should it increment by 20?
    #maybe because to be divisible by 20 it should have an increase of 20
    for i in range(1, 21):
        if j%i != 0:
            break
    else:
        thenumber = j
        break
print(thenumber)