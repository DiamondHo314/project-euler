print(8*'*' + 'Largest Palindrome Finder' + 8*'*')
start = int(input('enter starting number: '))
end = int(input('enter end number: '))
max = -9999999999999
n1, n2 = 0, 0 
for i in range(start, end+1):
    for j in range(i):
        prod = (j)*(i)
        string_prod = str(prod)
        rev_prod = string_prod[::-1]
        if prod>max and string_prod==rev_prod:
            max = prod
            n1 = j
            n2 = i
       # if j>=100 and i>=100 and string_prod == rev_prod and prod!=0 :
       #     print('palindrome:',prod, '\nnum1:',(j) ,'\nnum2:',(i))
print('palindrome:', max, '\nnum1:', n1, '\nnum2:', n2)