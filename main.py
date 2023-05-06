#Imports
import eel
import mysql.connector
from random import randint

from datetime import datetime
from datetime import date

import mysql.connector
import time
from mysql.connector import errorcode

##Functions
eel.init('templates')

@eel.expose

def random_python():
    print("Random function running")
    x = randint(1,100)
    print(x)
    return x

@eel.expose
def leftToBathroom(studentId):
  print("Scan ID for dismissal...")
  x = str(studentId) + " " #input()
  f = open("output/report.txt", "a")

  f.write(x + ' ' + datetime.now().strftime("%H:%M:%S") + ' ' + date.today().strftime("%d/%m/%y") + ' Left for the Bathroom \n')
  return x

@eel.expose
def attendance(studentId):
  
  print("Signing In...")
  x = str(studentId) + " " #input()
  f = open("output/report.txt", "a")

  studentID = x
  timeStamp = date.today().strftime("%d-%m-%y") + ' ' + datetime.now().strftime("%H:%M:%S")
  reason = "Here"
  #id is auto generated

# Insert some data into table
  id=1001
  r="present"
  dt = date.today().strftime("%d-%m-%y") + ' ' + datetime.now().strftime("%H:%M:%S")

  
  cursor.execute("INSERT INTO attendance (studentid, reason, ttimestamp) VALUES (%s, %s, %s);", (x, r, dt))
  print("Inserted",cursor.rowcount,"row(s) of data.")

  cursor.execute("SELECT * FROM attendance;")
  rows = cursor.fetchall()
  print("Read",cursor.rowcount,"row(s) of data.")

  print (x)

  printDb()

#   print(studentID + timeStamp)

#   cursor.execute("INSERT INTO attendance (studentid, reason, ttimestamp) VALUES (%s, %s, %s);", (studentID, reason, timeStamp))
#   print("Inserted",cursor.rowcount,"row(s) of data.")

#   cursor.execute("SELECT * FROM attendance;")
#   rows = cursor.fetchall()
#   print("Read",cursor.rowcount,"row(s) of data.")


#   print(x)
#   print()

  f.write(str(id) + ' ' + datetime.now().strftime("%H:%M:%S") + ' ' + date.today().strftime("%d/%m/%y") + ' Got checked In \n')

  #Add a record into the DB

#   x = studentId
#   r = "present"
#   dt = date.today().strftime("%d-%m-%y") + ' ' + datetime.now().strftime("%H:%M:%S")
  
#   cursor.execute("INSERT INTO attendance (studentid, reason, ttimestamp) VALUES (%s, %s, %s);", (x, r, dt))


  return x

@eel.expose
def otherdest(input, place):
  print("Scan ID for non bathroom destination...")
  x = str(input)
  print("Going to room?")
#   search
#   search1 = search(x)
#   print(searc)
  teach = place

  f = open("output/report.txt", "a")

  f.write(x + ' ' + datetime.now().strftime("%H:%M:%S") + ' ' +
          date.today().strftime("%d/%m/%y") + ' ' + teach + '\n')
  
  return x
  
@eel.expose
def dismiss(studentId):
  print("Scan ID for dismissal...")
  x = studentId
  f = open("output/report.txt", "a")

  f.write(x + ' ' + datetime.now().strftime("%H:%M:%S") + ' ' +
          date.today().strftime("%d/%m/%y") + ' Left School \n')

def returnBathroom():
  print("Scan ID for dismissal...")
  x = input()
  f = open("output/report.txt", "a")

  f.write(x + ' ' + datetime.now().strftime("%H:%M:%S") + ' ' + date.today().strftime("%d/%m/%y") + ' Left for the Bathroom \n')
  
def otherdestReturn():
  print("Scan ID for non bathroom destination...")
  x = input()
  print("come back from room?")
  teach = input()

  f.write(x + ' ' + datetime.now().strftime("%H:%M:%S") + ' ' +
          date.today().strftime("%d/%m/%y") + ' ' + teach + '\n')

def search(a):
  attcode = "present"
  with open('testscan.me', 'r') as r:
    while True:
      
      cursor.execute("INSERT INTO inventory (name, quantity) VALUES (%s, %s);", ("banana", 150))
  
      cursor.execute("SELECT * FROM attendance WHERE studentid = %s ORDER BY desc LIMIT 1;", (x))

      rows = cursor.fetchall()
      xprev = str(row[0])
      if xprev == "present":
        attcode = "bathout"
      else:
        attcode = "returned"
      

      b = r.readline()  #should be reading backward
      #print(b) #what is this thing reading? should be reading the entire record... not needed. was debugging.
      if not b:
        break
      #search for LATEST record with same input value in records already there...
      if b.find(
          x) > -1:  #found AND same period and last one was 1( entered)...
        #f.write("found")
        attcode = "bath-out"
        break
      elif b.find(x) > -2:  #garbage reason here...
        #found and same period and last reason was out
        attcode = "bath-in"
        break
  return attcode

def printDb():
  print("Filing Report Now into: \"report.txt\"")
  
   # Print all rows
  for row in rows:
  	print("Data row = (%s, %s, %s, %s)" %(str(row[0]), str(row[1]), str(row[2]), str(row[3])))

random_python()



#Main


# mydb = mysql.connector.connect(
#   host="localhost",0610011433

#   user="yourusername",
#   password="yourpassword"
# )

# mycursor = mydb.cursor()
f = open("output/report.txt", "a")
# dismiss()
# leftToBathroom(6)

# Obtain connection string information from the portal

config = {
  'host':'sparrow.mysql.database.azure.com',
  'user':'lemonadecode',
  'password':'zRVMbRBnuKzJt@2',
  'database':'attendance',
  'client_flags': [mysql.connector.ClientFlag.SSL],
  'ssl_ca': '/Users/oliviabisset/Downloads/DigiCertGlobalRootG2.crt.pem'
}

try:
   conn = mysql.connector.connect(**config)
   print("Connection established")
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with the user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:
  cursor = conn.cursor()

  # Read data
  cursor.execute("SELECT * FROM attendance;")
  rows = cursor.fetchall()
  print("Read",cursor.rowcount,"row(s) of data.")

  printDb()

#   # Print all rows
#   for row in rows:
#   	print("Data row = (%s, %s, %s, %s)" %(str(row[0]), str(row[1]), str(row[2]), str(row[3])))


# 1000 is width of window and 600 is the height
eel.start('index.html', size=(1000, 600))



#######main code

