import sqlite3
conn=sqlite3.connect("test.db")
cur=conn.cursor()
cur.execute('''CREATE TABLE if not exists Student
(student_usn varchar(10) NOT NULL, name TEXT NOT NULL, sem int NOT NULL, college varchar(20));''')
if cur:
    print ("Table created successfully");
student_usn=''
name=''
sem=''
college=''
ch=input("You want enter the details:(enter y for yes)\n")
if ch=='y':
    n=int(input("Enter the number of students \n"))
    for i in range(0,n):
        print("")
        student_usn=input("Enter usn\n")
        print("")
        name=input("Enter name of student\n")
        print("")
        sem=int(input("Enter sem\n"))
        print("")
        college=input("Enter college\n")
        cur.execute("INSERT INTO Student (student_usn,name,sem,college)VALUES (:0,:1,:2,:3)",(student_usn,name,sem,college));
        cur.execute(''' SELECT * FROM Student''');
else:
    cur.execute(''' update Student set sem=8 where usn=8 ''')
    cur.execute(''' delete Student where name=sakshi ''')
    cur.execute("SELECT * from Student")
    cursor=cur.fetchall()
    for row in cursor:
        print("USN = ", row[0],)
        print( "NAME = ", row[1], )
        print( "SEMESTER = ", row[2],)
        print( "COLLEGE = ", row[3],)
    
conn.commit()
conn.close()
