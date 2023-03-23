weeks = ["sunday", "monday", "tuesday",
         "wednesday", "thursday", "friday", "saturday"]
a = int(input("enter number for corresponding weeks: "))
if a>0 and a<=7:
    print(f"the value of weeks {a} is {weeks[a-1]}")
else:
    print("Invaild input")