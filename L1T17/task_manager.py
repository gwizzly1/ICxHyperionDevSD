#=====importing libraries===========
'''This is the section where you will import libraries'''
from datetime import datetime, date
# ===========TO DO=============
'''
1. Upate password list at the end (ie for new users)
2. Format the print statements 
4. ERROR HANDLING 
    - dates - only allow future dates for tasks
    - dates - make sure in the correct format and has YYYY not YY and not backwards
    - dateutil.parser.parse
'''

#====Login Section====
'''Here you will write code that will allow a user to login.
    - Your code must read usernames and password from the user.txt file
    - You can use a list or dictionary to store a list of usernames and passwords from the file
    - Use a while loop to validate your user name and password
'''
def read_logins(filename):
    """
    Reads userfile
    """
    with open(filename, '+r') as f:
        contents = f.read()
        line_list = contents.splitlines()
    password_list = {}
    for lines in line_list:
        username, password = lines.split(',') # Assumption that the file structure is correct
        username_clean = username.strip() # This is to remove the trailing or leading spaces
        password_clean = password.strip()
        password_list[username_clean] = password_clean
    return password_list

class PasswordError(Exception):
    pass

def check_password(username, password, p_list):
    """
    Checks password against list and raises error if not correct
    """
    if p_list[username] == password:
        print('You have successfully logged in!')
        print((40 * '-').format(50))
        return
    else:
        print('Your password is incorrect, please try again.')
        print((40 * '-').format(50))
        raise PasswordError # This is not catching a 'keyError' when I put a password of 'Georgie' in (with Georgie username) - why?

class UsernameError(Exception):
    pass

def check_username(entry_username, p_list):
    if entry_username not in p_list:
        print('The username does not exist, please re-submit your username and password.')
        print((40 * '-').format(50))
        raise UsernameError

class UserNameExistsError(Exception):
    pass

def user_check(entry_username, p_list):
    if entry_username in p_list: # This is to check if the username already exists
        print('This username already exists, please enter another one.')
        print((40 * '-').format(50))
        raise UserNameExistsError


def print_line_task(line, menu, entry_username = None):
    # Error Handling - shouldn't need 5 splits but in case something goes wrong this will
    # print any extra additions rather than give a ValueError
    (
        user_split_orig,
        task_title_split_orig,
        description_split_orig,
        due_split_orig,
        assigned_date_split_orig,
        completed_split_orig
     ) = line.split(', ', 5)
    
    # These are making sure there aren't any spaces before/after
    user_split = user_split_orig.strip()
    task_title_split = task_title_split_orig.strip()
    description_split = description_split_orig.strip()
    due_split = due_split_orig.strip() 
    assigned_date_split = assigned_date_split_orig.strip()
    completed_split = completed_split_orig.strip()
    
    # If menu is vm then only print if user_split == entry_username
    # This is equal to if menu is vm and user_split != entry_username
    if menu == "vm":
        if entry_username is None:
            raise ValueError("username must be supplied if menu is vm")
        if user_split != entry_username:
            return

    # If menu is va then print in all cases
    elif menu == 'va':
        print((40 * '-').format(50))
        print("Task: " + task_title_split.ljust(50))
        print("Assigned to: " + user_split.ljust(50))
        print("Date assigned: " + assigned_date_split.ljust(50))
        print("Task complete? " + completed_split.ljust(50))
        print("Task description: " + description_split.ljust(50))
        print("Due date: " + due_split.ljust(50))
        print((40 * '-').format(50), end='\n\n')
    
    else:
        raise ValueError(f"Unexpected menu type: {menu}")


def menu_choice(user_entry):
    """
    Note: Present the menu to the user and 
    make sure that the user input is converted to lower case.
    """
    if user_entry == 'admin':
        return input(
            'Select one of the following options:'
            '\n' 'r - register a user'
            '\n' 'a - add task'
            '\n' 'va - view all tasks'
            '\n' 'vm - view my tasks'
            '\n' 's - statistics'
            '\n' 'e - exit:'
        ).lower()
    else:
        return input(
            'Select one of the following options:'
            '\n' 'r - register a user'
            '\n' 'a - add task'
            '\n' 'va - view all tasks'
            '\n' 'vm - view my tasks'
            '\n' 'e - exit:'
        ).lower()


def menu_statistics(password_list):
    user_num = len(password_list.keys())
    with open('tasks.txt','r') as file:
        line_num = file.readlines() # As each task is on a new line we can just count the number of lines in the tasks file
        total_task_num = len(line_num)
        
    print((40 * '-').format(50))
    print(f'Total number of users: {user_num}')
    print(f'Total number of tasks: {total_task_num}')
    print((40 * '-').format(50))


def menu_view_my_tasks(entry_username):
    # I need to do the below again because the script above onl;y runs if I look at all tasks
    with open('tasks.txt', '+r') as t:
        contents_tasks = t.read()
        line_list_tasks = contents_tasks.splitlines()
    for line in line_list_tasks:
        print_line_task(line, menu="vm", entry_username=entry_username)

    '''This code block will read the task from task.txt file and
        print to the console in the format of Output 2 presented in the PDF
        You can do it in this way:
        - Read a line from the file
        - Split the line where there is comma and space.
        - Check if the username of the person logged in is the same as the 
            username you have read from the file.
        - If they are the same you print the task in the format of Output 2
            shown in the PDF '''


def menu_view_all_tasks():
    with open('tasks.txt', '+r') as t:
        contents_tasks = t.read()
        line_list_tasks = contents_tasks.splitlines()

    for line in line_list_tasks:
        print_line_task(line, menu="va")
        # TO DO: NEED TO FORMAT PROPERLY! 


    '''This code block will read the task from task.txt file and
        print to the console in the format of Output 2 presented in the PDF
        You can do it in this way:
        - Read a line from the file.
        - Split that line where there is comma and space.
        - Then print the results in the format shown in the Output 2 in the PDF
        - It is much easier to read a file using a for loop.'''

def date_format(due_date_components):
        day, month, year = [int(component) for component in due_date_components]
        return date(year,month,day).strftime("%d %b %Y") # This is to format the dates the same as what's already in the file
    
class DateFormatError(Exception):
    pass

def menu_assign_task(password_list, entry_username):

    for attempts in range(1, 8):
        user_task = input('Please enter the username you would like to assign the task to: ')
    
        if user_task in password_list:
            break
        else:
            print('This username does not match a given username, please re-enter:')

    while True:
        task_title = input('Please add a brief title for the task: ')
        task_desc = input('Please add a description of the task: ')
        if task_title == '':
            print('You have not entered a title for the task, please include one.')
        elif task_desc == '':
            print('You have not entered a brief description, please include one')
        else:
            break

    for attempts in range(1, 8):
        try: 
            due_date_question = input('Please add a due date for the task in the format dd/mm/yyyy: ').split('/') 
            due_date = date_format(due_date_question)
            date_split = datetime.strptime(due_date, "%d %b %Y")
            if date_split.year< 100:
                print('This year has 2 digits, please enter a a 4 digit year (i.e. 2023)')
                raise ValueError
            else:
                break
        except ValueError:
            print('The date is in the incorrect format, please try again')
            #raise DateFormatError # This isn't stopping the errors.... why?!
    
    
    current_date = date.today().strftime("%d %b %Y")
    task_completed = 'No'

    total_add_str = user_task + ', '+ task_title + ', ' + task_desc + ', ' + due_date + ', ' + current_date + ', ' + task_completed
    
    with open('tasks.txt', 'a') as f:
        f.write(f'\n{total_add_str}')
    
    print((40 * '-').format(50))


    '''This code block will allow a user to add a new task to task.txt file
    - You can use these steps:
        - Prompt a user for the following: 
            - the username of the person whom the task is assigned to,
            - the title of the task,
            - the description of the task, and 
            - the due date of the task.
        - Then, get the current date.
        - Add the data to the file task.txt
        - Remember to include 'No' to indicate that the task is not complete.'''


def menu_register_user(password_list, entry_username):
    while entry_username != 'admin':
        print('This option isn\'t available, only admin can register a user. Please contact your administrator.')
        print((40 * '-').format(50))
        break
    else:
        for t in range(1,8):
            username_new = input('Please enter the new username you\'d like to register: ')
            try:
                user_check(username_new, password_list) 
                break
            except UserNameExistsError:
                pass
        else:
            print("You've made too many attempts.")
            exit() 

        for attempts in range(1, 8):   
            pw_new = input('Please enter the new password: ')
            # Password validation
            pw_match = input('Please re-enter your password: ')
            if pw_new == pw_match:
                print('You have successfully created a new user.')
                print((40 * '-').format(50))
                password_list[username_new] = pw_new # also make sure a new user doens't put the same username in
                # I've decided to only update password_list dictionary now and then at the end update the whole file - time efficient? 
                break
            else:
                print('Those passwords do not match, please re-start entering the password.')
                print((40 * '-').format(50))
        else:
            print("You've made too many attempts.")
            exit()

    #password_list_str = '\n'.join(str(user) for user in password_list) # GETTING there with it! but only prints user  

    # with open('user.txt', 'w') as f:
    #    f.write(password_list)
    # ******ISSUE******** I can't upload the user.txt file with a dict so need to convert the dict or change the txt file to a json

    '''This code block will add a new user to the user.txt file
    - You can use the following steps:
        - Request input of a new username
        - Request input of a new password
        - Request input of password confirmation.
        - Check if the new password and confirmed password are the same
        - If they are the same, add them to the user.txt file,
            otherwise present a relevant message'''

def show_menu(config_filepath):

    password_list = read_logins(config_filepath)

    for attempts in range(1, 8): # I've started the range at 1 so if the print statment says how many attempts have been made we want it to start at 1
        entry_un = input('Please enter your username: ')
        entry_pw = input('Please enter your password: ')
        try:
            check_password(entry_un, entry_pw, password_list)
            break
        except (UsernameError, PasswordError):
            print('You have had {attempts} attempts. Max of 7 attempts allowed.')
    else:
        print("You've made too many attempts.")
        exit() # Does this have to be a while loop?


    while True:
        menu = menu_choice(entry_un)

        if menu == 'r':   
            menu_register_user(password_list, entry_un)
        elif menu == 'a':
            menu_assign_task(password_list, entry_un)
        elif menu == 'va':
            menu_view_all_tasks(entry_un)
        elif menu == 'vm':
            menu_view_my_tasks(entry_un)
        elif menu == 's':
            menu_statistics(password_list)
        elif menu == 'e':
            print('Goodbye!!!')
            exit()
        else:
            print("You have made entered an invalid input. Please try again")

        # remember to update the whole list of password_list to the user.txt file

if __name__ == '__main__':
    show_menu('user.txt')
