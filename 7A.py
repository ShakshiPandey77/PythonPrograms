import os
f1=open("prime.txt","r")
f2=open("happy.txt","r")

ls3=[]
s1=f1.read()
s2=f2.read()
l1=s1.split(",")
l2=s2.split(",")
for i in l1:
   if i in l2 and i!="," and i!=" ":
       ls3.append(i)

print(ls3)
    
f1.close()
f2.close()
