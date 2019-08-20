def rev1(str1):
    lis=str1.split(" ")
    lis.reverse()
    print(lis)
    a=" "
    s2=a.join(lis)
    print(s2)
    
def revstring(str):
    lis=str.split(" ")
    lis2=""
    for i in lis:
        lis2+=i[: : -1]
        lis2+=" "
    print(lis2)
str1=input("enter the string")
rev1(str1)
revstring(str1)
