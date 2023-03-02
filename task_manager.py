import datetime
#====Login Section====
#asking the user to enter username and user password
username = input("Enter your username: ")
user_password = input("Enter your password: ")

with open("user.txt", "r") as f:
    for line in f.readlines():
        data = line.strip().split(",")
        if username == data[0] and user_password == data[1]:
            logged_in = True
            print("Succesful Login")

while True:
    #presenting the menu to the user and 
    # making sure that the user input is coneverted to lower case.
    if username == "admin":
        
        
        menu = input('''Select one of the following Options below:
    r - Registering a user
    a - Adding a task
    va - View all tasks
    vm - view my task
    e - Exit''')
    else:
        #code to allow only the admin user to be able to register another user
        menu = input('''Select one of the following Options below:       
    a - Adding a task
    va - View all tasks
    vm - view my task
    e - Exit''')
#using the if, elif and else loops to choose from the menu bar
#if loop to register a new user if the choice was r
    if menu == 'r':
        new_user = input("Enter a new username: ")
        new_user_password = input("Enter a new password: ")
        password_confirmation = input("Enter new password again: ")
        if new_user_password == password_confirmation:
            with open("user.txt", "a") as userfile:
                userfile.write('\n' + new_user + ", " + new_user_password)
            
            
#if the user instead chose a use the elif menu to add a task
#open the file and append 
    elif menu == 'a':
        assigned_user = input("Enter the user the task is assigned to: ")
        task_title = input("Enter the title of the task: ")
        description = input("Describe the task: ")
        due_date = input("Enter the task due date: ")
        current_date = datetime.datetime.now()
        with open("tasks.txt", 'a') as taskfile:
            taskfile.write('\n' + f"{username}  ,  {task_title} ,  {description} , {due_date} ,  {current_date}" )
            
#if from the menu the choice we verify all tasks
    elif menu == 'va':
        with open("tasks.txt", 'r') as taskfile:
            for line in taskfile:
                split = line.split(", " )
                print(split)
        

    elif menu == 'vm':
        with open("tasks.txt", "r") as taskfile:
            for line in taskfile:
                split = line.split(", ")
                if username == data[0]:
                    
                    print("")
        

    elif menu == 'e':
        print('Goodbye!!!')
        exit()
#if the choice is not on the we ask the user to try again
    else:
        print("You have made a wrong choice, Please Try again")

        
        
