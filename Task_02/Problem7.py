Num = int(input())
print("Prime Factors: ", end=' ')

i = 2
while Num > 1:
    if Num % i ==0:
        print(i, end=' ')
        while Num % i == 0:
            Num //=i
    i +=1

