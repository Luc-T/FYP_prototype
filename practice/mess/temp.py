import random
""" fruits = ["Apple", "Banana", "Pear"]
veg = ["Pepper", "Courgette", "Carrot"]

j = 0
for i in range(2):
    print("i: ", fruits[i], "| j: ", veg[j])
    j+=1
 """


for i in range(10):
    b = bool(random.getrandbits(1))
    if b:
        print("true")
    else:
        print("False")