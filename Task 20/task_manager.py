#**************************************# Task 20: task_manager #**************************************#
from datetime import datetime   # Used for the current date used in the add task.

#**************************************# login #**************************************#
login = False                                           #This will be used to check if the user is logged in
user_file = open("user.txt", "r+")                      #Opens the user file

while login == False:                                   #While the logged in variable if false this whole statment will run

    username = input("Please enter your username: ")
    password = input("Please enter your password: ")

    for line in user_file:                              #Checks the user_file continuously to check for all the details
        line = line.rstrip()                            #We use this to remove the white space at the end of any user account
        valid_user, valid_password = line.split(", ")   #Splits the username and password by replaceing the ", "

        if username == valid_user:                      #Checks if the username matches the username in the text file
            if password == valid_password:              #Checks if the password matches with that account
                login = True                            #Sets login to true
                print("Correct details!")

    if login == False:                                  #Sets the login to false so that the while loop repeats
        print("Your details are inncorect.")

    user_file.seek(0)                                   #Goes back to the start of the text document should we need to read through it again.

if username != 'admin' and login == True:               #If the username is not equal to admin, this message will be printed
    print("#****************************************************************************#")
    print("Welcome, Please select one of the following tasks you'd like to perform!")
    print("")
    print("a  |\t Add a task")
    print("va |\t View all the tasks")
    print("vm |\t View all your current tasks")
    print("e  |\t Exit the program")
    print("")
    print("#****************************************************************************#")

if username == 'admin' and login == True:               #Checks if the user is 'admin' and if it is this text block will be displayed
    print("#****************************************************************************#")
    print("Welcome, Please select one of the following tasks you'd like to perform!")
    print("")
    print("r  |\t Register a user")
    print("a  |\t Add a task")
    print("va |\t View all the tasks")
    print("vm |\t View all your current tasks")
    print("s  |\t Prints out the total number of users and tasks")
    print("e  |\t Exit the program")
    print("")
    print("#****************************************************************************#")

user_input = input().lower()                                        #This requests the user to input any of the following above lines

while user_input != 'e':                                            #This checks if the user didn't enter 'e', if they did it will not run the loop and the program will exit

#**************************************# Register Function (admin only) #**************************************#
    if user_input == 'r' and username == 'admin':                           #If the user entered 'r' it will enter this block
        with open("user.txt", "a") as user_details:                         #This opens the users text file
            user_name = input("Please enter your username: ")

            password_match = 0                                              #We will use this variable to test if passwords match

            while password_match == 0:                                      #While the password match is at 0 (which it is by default) it will run this while block
                password = input("Please enter a password: ")
                password_check = input("Please confirm your password: ")

                if password_check == password:                              #We check if the password_check is equal to the password
                    password_match += 1                                     #If it is equal we add one so that we break out the while loop

                else:
                    print("Your passwords did not match, please try again.")#If the passwords didn't match it will print this message and return to the original while loop

            user_details.write(f"\n{user_name}, {password}")                #Once we break out the while loop we write the user details in the text document.

            print("Your account has been created. The program will now stop, launch again to use your account.")

            user_input = input("Please enter a value: ").lower()            #This allows the user to input the next command they'd like to do, and lowering it so case sensitivity is ignored

#**************************************# register  (None Admin)  #**************************************#

    elif user_input == 'r' and username != 'admin':
        print("You are not an admin. Only admin accounts can create new accounts.")

        user_input = input("Please enter a value: ").lower()



#**************************************# Add task #**************************************#
    elif user_input == 'a':                                                     #If the user entered 'A' we enter the add a task block.
        user_of_task = input("Please enter the user who will do this task: ")   #All of the below input statments are clearly marked what
        task_title = input("Please enter the title of the task: ")              #information they'll be holding by their variable name.
        task_desc = input("Please enter the description of the task: ")
        due_date = input("Please enter a due date: ")
        completed = "No"                                                        #Due to the idea of all the tasks being 'no' by default we make the output now
        date_sub = datetime.date(datetime.now())                                #This gets the date the user submitted the task.

        new_task = f" Assigned to \t\t| \t {user_of_task} , Task \t\t\t\t| \t {task_title} , Date Subbited \t\t| \t {date_sub} , Due Date \t\t\t| \t {due_date} , Task Descirption \t| \t {task_desc}, Completed \t\t\t| \t {completed}\n"

        with open("tasks.txt", "a") as reg_task:                                #We open the tasks text document
            reg_task.write(new_task)                                            #We write the new task (the long line of code above) and add a \n at the end to make sure that the tasks don't all clunk up on one line

        print("Task has been added.")
        user_input = input("Please enter a value: ").lower()


#**************************************# View all tasks #**************************************#

    elif user_input == 'va':                            #If this value was entered we view all the tasks in the text file

        file = open("tasks.txt", "r")
        read_lines = file.readlines()                   # Reads all the lines

        for user_task in read_lines:
            user_task = user_task.replace(",", "\n")    # If it is it gets all of them and replaces the ',' with a new line for ease of reading
            print(user_task)                            # Prints out the user task

        file.close()                                    # Closes the file to save memory
        user_input = input("Please enter a value: ").lower()


#**************************************# View your tasks #**************************************#

    elif user_input == 'vm':                                  #If the user entered 'vm' it lets use view their task

        file = open("tasks.txt", "r")
        read_lines = file.readlines()                           # Reads all the lines

        for user_task in read_lines:

            if username in user_task:                           #This checks if the username is in the user tasks folder
                user_task = user_task.replace(",", "\n")        #If it is it gets all of them and replaces the ',' with a new line for ease of reading
                print(user_task)                                #Prints out the user task

        file.close()                                            #Closes the file to save memory

        user_input = input("Please enter a value: ").lower()

#**************************************# Stats  (admin only)  #**************************************#
    elif username == 'admin' and user_input == 's':                 #This checks if the username is admin and they typed 's'
        num_users = 0                                               #These are just place holder values
        num_tasks = 0

        file_user = open("user.txt", "r")                           #Opens the users text document
        for line in file_user:                                      #Checks the lines in the user file document
            if line != "\n":                                        #If the line does not have a \n add 1
                num_users += 1
        file_user.close()

        file_task = open("tasks.txt", "r")                          #Checks the tasks text document
        for line in file_task:                                      #Cehcks each line in the document
            if line != "\n":                                        #If it does not contain a \n add 1
                num_tasks += 1
        file_task.close()


        print(f"The total number of users are | \t {num_users}")    #Prints the num of users
        print(f"The total number of tasks are | \t {num_tasks}")    #Prints the num of tasks

        user_input = input("Please enter a value: ").lower()

#**************************************# Stats  (None Admin)  #**************************************#
    elif username != 'admin' and user_input == 's':                 #Checks if the username is not an admin
        print("Only admins are able to view the statistics page.")  #Tells the user only admins can view this page

        user_input = input("Please enter a value: ").lower()
