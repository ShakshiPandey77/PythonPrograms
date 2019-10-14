import string
from random import randint
str1=string.printable
print(str1)
print(len(str1))
for i in range(6):
    print(str1[randint(0,100)],end="")
    
    
    
    
    
    ''' random passsord generator program.
    Constraints : a. Minimum length of 10, maximum length of 15
                  b. Password must contain at least one capital letter,
                     one small letter, one number and one special character
    '''
    
    import string
from random import randint
str1 = string.printable

def generatePassword():
    passLen = randint(10,15)
    password = ''
    for i in range(passLen):
        password+=str1[randint(0,len(str1)-1)]
    return password

while True:
    password =  generatePassword()
    if (any(x.isupper() for x in password) and
       any(x.islower() for x in password) and
       any(x.isdigit() for x in password) and
       (len(password)>=10 or len(password)<=15) ):
           print(password)
           break

