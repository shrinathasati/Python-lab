f=open("shri.txt","w")
f.write("hi this is shrinath")
f.close()

f=open("shri.txt")

text=f.read()
print(text)