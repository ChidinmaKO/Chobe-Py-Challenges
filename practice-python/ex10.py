from random import sample
a = sample(range(1,50),10)
b = sample(range(1,55),10)
# one way
list_comp = [i for i in list(set(a) & set(b))]
# another way
list_comp2 = [i for i in a if i in b]
print(list_comp)
print(list_comp2)