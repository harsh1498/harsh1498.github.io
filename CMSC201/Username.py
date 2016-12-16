# File: username.py
# Author: Harsh Patel
# Date: 11/29/16
# Section: 23
# E-mail: harsh3@umbc.edu
# Description:
# Creates a file for users and allows secure editing of text files
# in a line by line editing interface. It password secures the file.
# Collaboration:
# I did not collaborate on this project

# def read(): Reads the dictonary from a file and creates local dict
# Input:      names.txt
# Output:     A dictonary of usernames and passwords
def read():

    # Create empty dict and open file
    dict1 = {}
    file1 = open("names.txt" , "r")

    # Reads each line in file, seperates into username and passsword
    # and creates new key value pair
    for eachline in file1:
        eachline = eachline.strip()
        username,password = eachline.split(" ; ")
        dict1[username] = password

    return dict1

# def newUser(dict1): Adds new user into dictonary, and creates their file
# Input:              Dict1
# Output:             Updated dictonary, and user's new file
def newUser(dict1):

    username = input("Please enter a username: ")

    # Checks if username exists and prints error until username not found
    while username in dict1:
        username = input("I am sorry, that username is already taken, try another one: ")

    # Asks for password
    password = input("Please enter a pasword: ")
    while len(password) < 3 or len(password) > 12:
		if len(password) < 3:
            password = input("Please enter a longer pasword: ")
        else:
             password = input("Please enter a shorter pasword: ")

    password_check = input("Please re-enter your password here: ")

    # Checks if password is correct both times
    while password != password_check:
        print("The check didn't work, please try again ")
        password = input("Please enter a pasword: ")
        password_check = input("Please re-enter your password here: ")

    # Creates user's file and writes first line to it & updates dict1
    file2 = open(username+".txt" , "w")
    file2.write(username)
    file2.write("   -------   Welcome to your secure journal : ")
    file2.write("\n" + " : ")
    file2.close()
    file1 = open("names.txt" , 'a')
    file1.write(username)
    file1.write(" ; ")
	file1.write(password)
    file1.write("\n")
    dict1[username] = password

# def check(dict1,user,passworda): Checks if password is correct
# Input:                           Username, Password attempt, and Dict1
# Output:                          Boolean and login in status print
def check(dict1,user,passworda):

    # Amount of tries allowed
    tries = 3

    # While the password does not match and tries are allowed, allows
    # user to re try password attempt
    while dict1[user] != passworda and tries <= 3 and tries > 0:
        print("invalid password! " , tries , " Tries left!!!")
        passworda = input("Please enter your password here: ")
        tries -= 1

    # If password matches, login occurs
    if passworda == dict1[user]:
        print("Login successful!!!!! ")
		return "True"

# def program(user): Shows user file contents and allows for appending
# Input:             Username, User's Choice to append, and user's content to app end
# Output:            Updtated user file
def program(user):

    # Opens user's file
    file1 = open(user+".txt" , "r")

    # Prints file onto screen
    for eachline in file1:
        print (eachline)
    file1.close()

    # Asks user if they would like to edit file, opens file for appending
    userinput = input("Would you like to write new info to your account? y/n: ")
    if userinput == "y":
        file1 = open(user+".txt" , "a")
    lineNum = 0

    # While user chooses to edit file, writes userinput to file
    while userinput == "y":
        userinfo = input("Type line "+ str(lineNum) + " here: ")
        file1.write(userinfo)
        file1.write("\n")
        userinput = input("Would you like to continue on the next line? y/n: ")
        lineNum += 1

    # Close file and reprint edits
    file1.close()
	file1 = open(user+".txt" , "r")
    if lineNum >= 1:
        for eachline in file1:
            print (eachline)
    file1.close()

def main():
    dict1 = read()
    login = input("Would you like to create a new account? y/n: ")

    # If one is a newuser, runs newUser function
    if login == "y":
        newUser(dict1)

    # Gets username and checks if it exists
    user = input("Please enter your username to login: ")
    bool1 = not(user in dict1)
    while bool1:
        user = input("Please enter a valid username to login: ")
        bool1 = not(user in dict1)

    # If username found, proceed to gaining password info
    passworda = input("Please enter your password here: ")
    bool2 = check(dict1,user,passworda)

    # If admin password mathces, runs admin version of program
    if user == "admin":
        choice = input("Would you like to access a user's file? y/n: ")
        while choice == "y":
            user = input("Please enter the username of a user here : ")
            program(user)
            choice = input("Would you like to access a another user's file? y/n: ")

    # If password matches the of user, proceeds to run user version of program
    elif bool2 == "True":
        program(user)

    # Exits program if password is wrong
	else:
        print("Account locked, please contact Admin")

    print("Thank you for using this secure terminal, have a good one : )")

main()


