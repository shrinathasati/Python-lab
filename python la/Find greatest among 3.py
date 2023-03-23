a=int(input("enter number 1: "))
b=int(input("enter number 2: "))
c=int(input("enter number 3: "))
num1=0
num2=0
if a>=b:
    num1=a
else:
    num1=b
if b>=c:
    num2=b
else:
    num2=c
if num1>=num2:
    print(f"{num1} is greatest number.")
else:
    print(f"{num2} is greatest number.")