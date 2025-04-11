def even_sum(Num):
    Nums = range(2, Num+1, 2)
    return sum(Nums), ' + '.join(str(n) for n in Nums)

Num=int(input())
sum, seq = even_sum(Num)

print(f"The sum of even numbers from 1 to {Num} is {sum} ({seq}).")
