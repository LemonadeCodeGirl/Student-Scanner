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

random_python()

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="yourusername",
#   password="yourpassword"
# )

# mycursor = mydb.cursor()

# 1000 is width of window and 600 is the height
eel.start('index.html', size=(1000, 600))

#######main code

