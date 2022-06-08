#Question 1 binary equivalent of a number:

num=int(input("Enter any number:"))
l=[]
while (num>0):
    fun=num%2
    l.append(fun)
    num=num//2
l.reverse()
print("Binary equivalent of the number is:",)
for i in l:
    print(i,end="")

