Nums= []
while True:
   Num = int(input())
   if Num == -1:
    break
   Nums.append(Num)
if Nums:
   print(max(Nums), min(Nums))
else:
    print("No Numbers Entered!")
