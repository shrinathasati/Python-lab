size1=int(input("enter the size of list1: "))
size2=int(input("enter the size of list2: "))

lst=[]
lst1=[]
for i in range(0,size1):
    lst.append(int(input("enter the number of first list: ")))
    
for i in range(0,size2):
    lst1.append(int(input("enter the number of second list: ")))
print("first list is",lst)
print("second list is",lst1)
if(size1!=size2):
    print("the size are not equal, list are not equal.")
    
elif(lst==lst1):
    print("your both list are equal")
else:
    print("your both list are not equal")