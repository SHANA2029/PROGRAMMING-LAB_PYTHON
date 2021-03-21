l1=[6,5,9,3]
l2=[2,4,6,8,10]
if(len(l1)==len(l2)):
  print("both list are of same length")
else:
  print("both list are of different length")

if(sum(l1)==sum(l2)):
    print("both lists have same sum")
else:
    print("both lists have different sum")

    l3=[x for x in l1 if x in l2]
    print("common in both list are:",l3)

