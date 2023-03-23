# 1. using iterative method
num=int(input("enter number: "))
fact=1

for i in range(1,num+1):
    fact=fact*i
if num==0:
    print(f"factorial of number {num} is {fact}")
else:
    print(f"factorial of number {num} is {fact}")

# 2. using recursive method
def fact(num):
    if num==0:
        return 1
    else:
        return num*fact(num-1)
num=int(input("enter the number: "))
print(f"The factorial of {num} is {fact(num)}")