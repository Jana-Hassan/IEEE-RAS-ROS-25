n = int(input())
fact = 1
seq = ""
Num=n
if Num == 0:
    print(1)
    seq=""
else:
    while Num >= 1:
        fact *= Num
        seq += str(Num) +(" * " if Num > 1 else "")
        
        Num -= 1
print(f"The factorial of {n} is {fact} ({seq}).")