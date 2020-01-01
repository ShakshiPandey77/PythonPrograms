string=input("enter the string:")
c=0
for i in string:
    if i.isupper():
        c=c+1
print("no of uppercase",c)
        

'''
import re


def avg_word_length(filepath):
    file = open(filepath)
    words = re.findall('\w+', file.read())
    return sum([len(word) for word in words]) / len(words)


if __name__ == "__main__":
    print avg_word_length('io_files/ex38.txt')
'''


'''
# Python3 program to 
# Check if the string is pangram 
import string 
  
def ispangram(str): 
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet: 
        if char not in str.lower(): 
            return False
  
    return True
      
# Driver code 
string = 'the quick brown fox jumps over the lazy dog'
if(ispangram(string) == True): 
    print("Yes") 
else: 
    print("No") 
'''



'''
def sum_digits_sqr(n):
    a = n
    rem = 0
    sum = 0
    while a != 0:
        rem = a % 10
        sum += rem**2
        a /= 10
    return sum
 
n = int(raw_input("Enter number: "))
a = n
 
while sum_digits_sqr(n) != 1:
    n = sum_digits_sqr(n)
    if sum_digits_sqr(n) == 1:
        print "Happy number"
        break
'''




'''
num = 407
# To take input from the user
#num = int(input("Enter a number: "))
# prime numbers are greater than 1
if num > 1:
   # check for factors
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           print(i,"times",num//i,"is",num)
           break
   else:
       print(num,"is a prime number")
       
# if input number is less than
# or equal to 1, it is not prime
else:
   print(num,"is not a prime number")
'''


'''
# Python3 program to find minimum 
# difference in an unsorted array. 

# Returns minimum difference between 
# any two pair in arr[0..n-1] 
def printMinDiffPairs(arr , n): 
	if n <= 1: return

	# Sort array elements 
	arr.sort() 
	
	# Compare differences of adjacent 
	# pairs to find the minimum difference. 
	minDiff = arr[1] - arr[0] 
	for i in range(2 , n): 
		minDiff = min(minDiff, arr[i] - arr[i-1]) 

	# Traverse array again and print all 
	# pairs with difference as minDiff. 
	for i in range(1 , n): 
		if (arr[i] - arr[i-1]) == minDiff: 
			print( "(" + str(arr[i-1]) + ", "
				+ str(arr[i]) + "), ", end = '') 

# Driver code 
arr = [5, 3, 2, 4, 1] 
n = len(arr) 
printMinDiffPairs(arr , n) 

# This code is contributed by Ansu Kumari
'''




'''
# Python program to convert time 
# from 12 hour to 24 hour format 

# Function to convert the date format 
def convert24(str1): 
	
	# Checking if last two elements of time 
	# is AM and first two elements are 12 
	if str1[-2:] == "AM" and str1[:2] == "12": 
		return "00" + str1[2:-2] 
		
	# remove the AM	 
	elif str1[-2:] == "AM": 
		return str1[:-2] 
	
	# Checking if last two elements of time 
	# is PM and first two elements are 12 
	elif str1[-2:] == "PM" and str1[:2] == "12": 
		return str1[:-2] 
		
	else: 
		
		# add 12 to hours and remove PM 
		return str(int(str1[:2]) + 12) + str1[2:8] 

# Driver Code		 
print(convert24("08:05:45 PM")) 
'''


'''
def firstNonRepeatingChar(str1):
   char_order = []
   counts = {}
   for c in str1:
      if c in counts:
         counts[c] += 1
      else:
         counts[c] = 1
         char_order.append(c)
   for c in char_order:
      if counts[c] == 1:
      return c
   return None

print(firstNonRepeatingChar('PythonforallPythonMustforall'))
print(firstNonRepeatingChar('tutorialspointfordeveloper'))
print(firstNonRepeatingChar('AABBCC'))


Result:1st non repeating char
M
u
None
'''



'''
# Python3 code to find the sum of 
# all duration in the form of MM : SS. 

# Print sum of all duration. 
def printSum (m, s, n ): 
	total = 0
	
	# finding total seconds 
	for i in range(n): 
		total += s[i] 
		total += (m[i] * 60) 
	
	# print the hours. 
	print(int(total / 3600) , end= " : ") 
	total %= 3600
	
	# print the minutes. 
	print(int(total / 60) , end=": ") 
	total %= 60
	
	# print the hours. 
	print(int(total)) 

# Driven Code 
m = [ 0, 2, 3, 2, 1 ] 
s = [ 45, 31, 11, 27, 28 ] 
n = len(m) 
printSum(m, s, n) 

# This code is contributed by "Sharad_Bhardwaj". 
'''




'''
min and max frequency list:

def frequency(l):
    ls=sorted(l)
    from itertools import groupby
    l2=[len(list(group)) for key, group in groupby(ls)]
    mina=min(l2)
    maxa=max(l2)
    #print mina,maxa
    r=[]
    s=[]
    a=[]
    b=[]
    for i in range(0,len(l2)):
        if l2[i]==mina:
            a.append(i)
        if l2[i]==maxa:
            b.append(i)
    for i in range(0,len(a)):
        z=a[i]
        sumo=0
        for k in range(0,z+1):
            sumo=sumo+l2[k]
        sumo=sumo-1
        r.append(ls[sumo])
    for i in range(0,len(b)):
        z=b[i]
        sumo=0
        for k in range(0,z+1):
            sumo=sumo+l2[k]
        sumo=sumo-1
        s.append(ls[sumo])
    return r,s
'''




'''
import random
 
hidden = random.randrange(1, 201)
# print hidden
 
guess = int(raw_input("Please enter your guess: "))
 
if guess == hidden:
    print "Hit!"
elif guess < hidden:
    print "Your guess is too low"
else:
    print "Your guess is too high"
'''




'''   to print repeated char as symbol except 1st letter
def change_char(str1):
  char = str1[0]
  str1 = str1.replace(char, '$')
  str1 = char + str1[1:]

  return str1

print(change_char('restart'))
'''


'''
ow_num = int(input("Input number of rows: "))
col_num = int(input("Input number of columns: "))
multi_list = [[0 for col in range(col_num)] for row in range(row_num)]

for row in range(row_num):
    for col in range(col_num):
        multi_list[row][col]= row*col

print(multi_list)
'''
