class CallDetail:
     def __init__(self):
          self.number=None
          self.callednumber=None
          self.duration=None
          self.calltype=None
     def set(self,number,callednumber,duration,calltype):
          self.number=number
          self.callednumber=callednumber
          self.duration=duration
          self.calltype=calltype
     def display(self):
          print("Details")
          print("call num:",self.number)
          print("called number:",self.callednumber)
          print("duration:",self.duration)
          print("Type:",self.calltype)
          
               
class Util:
     def __init__(self):
          self.list_of_call_objects=None
     def parse_customer(self,list_of_call_string):
          self.list_of_call_objects=list_of_call_string
          for x in self.list_of_call_objects:
               a=x.split(',')
               obj=CallDetail()
               obj.set(a[0],a[1],a[2],a[3])
               obj.display()
    
call='9990009867,897899076,23,STD'
call2='9900879657,93007965849,54,Local'
call3='9908785645,789504789,6,ISD'
list_of_call_string=[call,call2,call3]
Util().parse_customer(list_of_call_string)

     
