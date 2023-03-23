from functools import reduce
def add_ele(a,b):
    return a+b
lst=[1,2,3,4,5]
print("the sum of list element is:",reduce(add_ele,lst))