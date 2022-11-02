'''Capstone template project for FCS Task 19 Compulsory task 1.
This template provides a skeleton code to start compulsory task 1 only.
Once you have successfully implemented compulsory task 1 it will be easier to
add a code for compulsory task 2 to complete this capstone'''

#=====importing libraries===========
'''This is the section where you will import libraries'''

from datetime import date

#====Login Section====

'''Here you will write code that will allow a user to login.
    - Your code must read usernames and password from the user.txt file
    - You can use a list or dictionary to store a list of usernames and passwords from the file.
    - Use a while loop to validate your user name and password.
'''
# Prompt user to enter username and Password

username = input("Enter username : ").lower()
password = input("Enter password ")
menu=""

# Getting username and password from text file

with open('user.txt','r') as f:
    for i in enumerate(f) :
        user_str = i[1].strip()
        user_list = user_str.split(", ")
        user_name = user_list[0]
        user_password = user_list[1]

# While username entered by the user is the same as the one in text file        

        while username == user_name:
            
#presenting the menu to the user and 
# making sure that the user input is coneverted to lower case.
    
          if password == user_password:
           if username == "admin":

# Menu for admin

                menu = input('''Select one of the following Options below:
                               r - Registering a user
                               a - Adding a task
                               va - View all tasks
                               vm - view my task
                               ds - Display statistics
                               e - Exit
                               : ''').lower()
# Menu for rest of users
           else:
                menu = input('''Select one of the following Options below:
                               r - Registering a user
                               a - Adding a task
                               va - View all tasks
                               vm - view my task
                               e - Exit
                               : ''').lower()
                  
           if menu == 'r':
               
# admin code for registering new users

                 if username == 'admin': 
                       new_username = input("Enter new username : ").lower()
                       new_password = input("Enter new password : ")
                       confirm_password = input("Confirm password : ")
                       
                       if new_password == confirm_password :
                          with open('user.txt','a') as f:
                               f.write("\n"+ new_username + ", " + new_password)
                               print("New user has been registered successfully !!\n")
                           
                       else:

                            
                            while new_password != confirm_password:
                                  print("Passwords do not match ")
                                  new_password = input("Enter new password : ")
                                  confirm_password = input("Confirm password : ")
                                  
                            if new_password == confirm_password :
                              with open('user.txt','a') as f:
                                   f.write(""+ new_username + ", " + new_password)
                                   print("New user has been registered successfully !!\n")

# If the user who is logged in is not an admin                                 

                 else:                     
                         print("You are not authorised to register new users !!\n")
     
# Adding new tasks

           elif menu == 'a':
               

                     person = input("Enter the username of the person the task is assigned to : ").lower()
                     title = input("Enter the title of the task : ")
                     description = input("Enter the description of the task : ")
                     task_due_date = input("Enter the due date of the task : (dd Mon yyyy) : ")
                     d = date.today()
                     current_date = d.strftime("%d %b %Y")
                     with open('tasks.txt','a') as f:
                          f.write("" + person +", " + title + ", " + description + ", " + str(current_date) + ", " + task_due_date + ", No")
                          print("New task has been registered successfully !!\n")

# Viewing tasks assigned to all users             

           elif menu == 'va':
                              

                     with open('tasks.txt','r') as f:
                         for i in enumerate(f):
                            user_str = i[1].strip()
                            user_list = user_str.split(", ")
                            print("\nTask:\t\t\t\t" + user_list[1])
                            print("Assigned to:\t\t\t" + user_list[0])
                            print("Date assigned:\t\t\t" + user_list[3])
                            print("Due date:\t\t\t" + user_list[4])
                            print("Task Complete?\t\t\t" + user_list[5])
                            print("Task description:\n  " + user_list[2])
                            print("\n")
                         
                    
# Viewing all tasks assigned to logged on user

           elif menu == 'vm':
               
                     with open('tasks.txt','r') as f:
                         for i in enumerate(f):
                            user_str = i[1].strip()
                            user_list = user_str.split(", ")
                            if username == user_list[0] : 
                               print("\nTask:\t\t\t\t" + user_list[1])
                               print("Assigned to:\t\t\t" + user_list[0])
                               print("Date assigned:\t\t\t" + user_list[3])
                               print("Due date:\t\t\t" + user_list[4])
                               print("Task Complete?\t\t\t" + user_list[5])
                               print("Task description:\n  " + user_list[2])
                               print("\n")

# Exit the application

           elif menu == 'e':
                    print('Goodbye!!!')
                    exit()

# Display statistic menu for the admin

           elif menu == 'ds':
                    n = 0
                    t = 0
                    with open('user.txt','r') as f:
                         for i in enumerate(f):
                             n += 1
                    with open('tasks.txt','r') as f:
                         for i in enumerate(f):
                             t += 1   
                    print("The total number of tasks is : " + str(t))           
                    print("The total number of users is : " + str(n))         

# If the user has entered invalid menu choice

           else:
                     print("You have made a wrong choice, Please Try again!\n")

 # If the user has supplied correct username but wrong password

          else:
                 print("wrong password")  
                 password=input("Enter password ")


            


        
                    



