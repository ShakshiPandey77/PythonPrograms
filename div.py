def divisor(num):
    b=[]
    for i in range(1,num+1):
        if num%i==0:
            b.append(i)
    print(b)

divisor(10)
