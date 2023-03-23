
# 9. fiter function in python
def even(ele):
    if ele%2==0:
        return True
    else:
        return False
lst=[1,2,4,5,8]
filtered=filter(even,lst)
print("Even numbers are:")
for ele in filtered:
    print(ele)