from replit import db, clear
from time import sleep

print("Hello!")
sleep(3)
clear()
print("Welcome to your Online Classroom, Middle School Edition!")

print("""Start by logging in: 
(if you want to create a new account,
start by entering 'username' in Username
and "password" in Password)""")
username = input("Username : ")
password = input("Password : ")

if username and password == db:
	print('You\'re logged in!')
elif username in db and password not in db:
	print("""Uh oh. You may have forgoten your password.
	Please restart this program and try again.""")
	exit("password lost")
elif username == "username" and password == "password":
	print("You/'re creating a new account.")
	global newaccount
	newusername = input("Enter your new username : ")
	db[username] = newusername
	global newpassword
	newpassword = input("Enter your new password : ")
	db[password] = newpassword
	clear()
	sleep(2)
	print("All set! Login to your new account after this program gets terminated...")
	sleep(2)
	exit("New account made")
elif username == 'admin' and password == 'admin':
	admin_actions = input("""Hello admin. what would you like to do?
	Delete account
	###MORE TO BE ADDED###""")
	if admin_actions == ("delete account").lower:
		print("OK! What account would you like to delete?")
		keys = db.keys
		print(keys)
		input()
elif username and password not in db:
	print("""This login does not exist. 
	Please try again or create a new account.""")

Class_choose = input("""What class would you like to start with?
Math
English
PE
Science
World History
Computer Science
""")