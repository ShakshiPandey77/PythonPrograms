lst=[]
n=int(input("enter the size of list:"))
for i in range(0,n):
    x=int(input())
    lst.append(x)
new=[]
for i in lst:
    if i%2==0:
        new.append(i)
print("new list")
print(new)
    
