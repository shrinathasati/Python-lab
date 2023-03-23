import itertools
def add_ele(a,b):
    return a+b
lst=[1,2,3]
result=itertools.accumulate(lst,add_ele)
for ele in result:
    print("the sum of",ele)