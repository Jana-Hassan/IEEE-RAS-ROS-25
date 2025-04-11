def intersect(set_1, set_2):
  result= set(set_1).intersection(set(set_2))
  return result

set_1= input("Set 1: ").split()
set_2 = input("Set 2: ").split()

result = intersect(set_1, set_2)

if result:
    print("Intersection b/w the two sets:", result)
else:
    print("There is No intersection b/w the two sets.")

