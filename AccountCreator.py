import sqlite3
import time
import datetime
from random import randint
solution = 0
contact_question = input("Before starting the auto repair, do you have a an existing account/contact number?").lower()
if "no" in contact_question:
    contact_reg_permission = input("Would you like to create an account?").lower()
    if "yes" in contact_reg_permission:
        print("We'll start right away")
        contact_number = randint(1000,6000)
        print(contact_number)
        print("This is your new account number. You could use this number every time you contact our troubleshooting service")
    

        
        
        
    if "no" in contact_reg_permission:
        print("You must create an account before initiating the auto-diagnosing phase.")
        input("Would like you like to carry on and create an account with us?")
        if "yes" in contact_reg_permission:
            print("we shall start with creating your account right away!")
            contact_number = randint(1000,6000)
            file = open(str(contact_number)+".txt","w+")
            contact_first_name = input("First name: ")
            file.write(str(contact_first_name))
            file.write(", ")
            time.sleep(1)
            contact_surname = input("Surname: ")
            file.write(str(contact_surname))
            file.write(", ")
            time.sleep(1)
            file.close()
            file = open("contact_saved.txt","w+")
            file.write(str(contact_number))
            print("This is your contact number for future events" + str(contact_number))
            time.sleep(3)
            print("Please restart the program and enter the code")
            time.sleep(1)
            file.close()
            exit()



if "yes" in contact_question:
    contact_number_input = input("Please enter your given contact number: ")
    if contact_number_input in open('contact_saved.txt'):
        print("Ok, lets start the process")
    else: print("Sorry, that contact number was not recognized")

    exit()
name = input("What is your name? \n")
issue = input('What is the issue that you are currently experiencing?: \n')

conn = sqlite3.connect('Troubleshooting_System_V1.5.db')
c = conn.cursor()

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS table01(usercode INT, usersfullname TEXT, lastlogin TEXT, caseid INT)") 

def data_entry():
     c.execute("INSERT INTO table01 VALUES(1263, '02-02-2016', 'Halil Es', 5927)")
     conn.commit()
     c.close()
     conn.close()
     

def dynamic_data_entry():
    date = str(datetime.datetime.fromtimestap(unix).strftime('%D-%m-%y'))



#create_table()
data_entry()
