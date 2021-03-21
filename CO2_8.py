a = input("enter the list:")
l=a.split(" ")
m=len(l[0])
for i in l:
    if(len(i)>m):
        m=len(i)
        t=i
print("longest word is ",t,"and its length is ",m)