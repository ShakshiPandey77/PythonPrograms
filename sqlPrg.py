import sqlite3

dbase = sqlite3.connect('Our_data.db') # Open a database File
print('Database opened')

dbase.execute(''' CREATE TABLE IF NOT EXISTS employee_records(
    ID INT PRIMARY KEY NOT NULL,
    NAME TEXT NOT NULL,
    DIVISION TEXT NOT NULL,
    STARS INT NOT NULL) ''')

print('Table created')
dbase.execute('''Insert Into employee_records(ID,NAME,DIVISION,STARS) VALUES(1,'lenny','software',3)
''')
def insert_record(ID,NAME,DIVISION,STARS):
    dbase.execute(''' INSERT INTO employee_records(ID,NAME,DIVISION,STARS)
            VALUES(?,?,?,?)''',(ID,NAME,DIVISION,STARS))

    dbase.commit()
    print ('Record inserted')
    
insert_record(7,'mock','Hardware',6)
insert_record(9,'pop','EC',7)
insert_record(10,'cvh','nnC',0)


def read_Data():
    # from math import *
    data = dbase.execute(''' SELECT * FROM employee_records ORDER BY NAME''')
    for record in data:
        print ('ID :' +str(record[0]))
        print ('NAME : '+str(record[1]))
        print ('DIVISION : '+str(record[2]))
        print ('STARS : '+str(record[3])+'\n')


read_Data()

def update_record():
    dbase.execute(''' UPDATE employee_records set STARS=5 WHERE ID=9 ''')
    dbase.commit()
    print ('Updated')

#update_record()
#print ('----------------------')
#read_Data()

def delete_record():
    dbase.execute(''' DELETE from employee_records WHERE ID = 6 ''')
    dbase.commit()
    print ('Deleted')

delete_record()
print ('----------------------')
read_Data()

dbase.close()
print('Database Closed')
 






''' import sqlite3

conn = sqlite3.connect('mysqlite.db')
c = conn.cursor()

#records or rows in a list
records = [(1, 'Glen', 8),
			(2, 'Elliot', 9),
			(3, 'Bob', 7)]

#insert multiple records in a single query
c.executemany('INSERT INTO students VALUES(?,?,?);',records);

print('We have inserted', c.rowcount, 'records to the table.')

#commit the changes to db			
conn.commit()
#close the connection
conn.close()
'''
