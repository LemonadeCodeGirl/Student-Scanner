#Imports
import eel
import mysql.connector
from random import randint

from datetime import datetime
from datetime import date


eel.init('templates')

@eel.expose

def random_python():
    print("Random function running")
    x = randint(1,100)
    print(x)
    return x

def dismiss():
  print("Scan ID for dismissal...")
  x = input()
  f = open("output/report1.txt", "a")

  f.write(x + ' ' + datetime.now().strftime("%H:%M:%S") + ' ' +
          date.today().strftime("%d/%m/%y") + ' Left School \n')

def otherdest():
  print("Scan ID for non bathroom destination...")
  x = input()
  print("Going to room?")
  teach = input()

  f.write(x + ' ' + datetime.now().strftime("%H:%M:%S") + ' ' +
          date.today().strftime("%d/%m/%y") + ' ' + teach + '\n')

def search(a):
  attcode = "present"
  with open('testscan.me', 'r') as r:
    while True:
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


random_python()
# dismiss()


# mydb = mysql.connector.connect(
#   host="localhost",0610011433

#   user="yourusername",
#   password="yourpassword"
# )

# mycursor = mydb.cursor()

# 1000 is width of window and 600 is the height
eel.start('index.html', size=(1000, 600))

#######main code

