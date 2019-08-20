def search(lis,a):
    print(lis)
    if a in lis:
        return True
    else:
        return False
    
lis=[]
while True:
    a=int(input("enter the ele"))
    if a!=-1:
        lis.append(a)
    else:
        break
b=input("enter the element to be searched")
print(search(lis,int(b)))
