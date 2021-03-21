st1="Hello World""\n""welcome to python programming""\n"
fw=open("file.txt","w")
fw.write(st1)
fw.close()
fr=open("file.txt","r")
st2=fr.readlines()
for i in st2:
 print(i)
