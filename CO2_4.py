A=int(input("enter range from:"))
B=int(input("enter range to:"))
a=[]
for x in range(A,B+1):
    if x%2==0 and x**2:
        a.append(x)
print(a)
