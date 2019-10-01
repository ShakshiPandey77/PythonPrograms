class validate:
     def __init__(self):
          self.mystring=None
     def check(mystring):
          mystring=str(input("enter brackets:"))
          brackets=['()','{}','[]']
          while any(x in mystring for x in brackets):
               for br in brackets:
                    mystring=mystring.replace(br,'')
               return not mystring

val=validate()
if val.check():
     print("valid")
else:
     print("not valid")
               
