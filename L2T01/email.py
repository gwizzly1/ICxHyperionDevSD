### --- OOP Email Simulator --- ###

# --- Email Class --- #
# Create the class, constructor and methods to create a new Email object. DONE
# Declare the class variable, with default value, for emails. DONE
# Initialise the instance variables for emails. DONE
# Create the method to change 'has_been_read' emails from False to True. 


class EmailChoiceError(Exception):
    pass


class InvalidInputError(Exception):
    pass


class TooManyAttempts(Exception):
    pass


class Email:
    '''
    This creates the framework for an email and has a method which converts the has been read flag to true 
    '''

    has_been_read = False

    def __init__(self, email_address: str, subject_line: str, email_content: str):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
        
    def mark_as_read(self):
        self.has_been_read = True
        print("This email flag has now been changed to read")


class Inbox:
    '''
    This class allows the structure of the inbox to be filled, the methods included in this class are:
    >>>> Populate inbox - this fills the inbox with 3 emails with the 3 sectione: email address, subject line and content
    >>>> List emails - this iterates through the number of emails and prints the index number and the subject line
    >>>> read_email - this reads the chosen email but iterating through the content and marks as read
    '''
    def __init__(self):
        self.email_list = []

    def populate_inbox(self):
        email_1 = Email('a@b.com', 'email 1', 'Hello this is email 1')
        email_2 = Email('b@c.com', 'email 2', 'Hello this is email 2')
        email_3 = Email('c@d.com', 'email 3', 'Hello this is email 3')

        self.email_list.append(email_1)
        self.email_list.append(email_2)
        self.email_list.append(email_3)

    def list_emails(self):
        for i, email in enumerate(self.email_list, start=1):
            print(i, email.subject_line)

    def read_email(self, i):
        if i - 1 < 0: # This prevents the email choice from going backwards as we are -1 in line 62 to allow the index to not start at 0,, so it matches the email number
            raise EmailChoiceError(f'Invalid index: {i} - note that we start at 1')
        try:
            email = self.email_list[i - 1] # As above this enables the index to match the email number, instead of email 1 having an index of 0 
            print(i, email.email_content)
            email.mark_as_read()
        except IndexError:
            raise EmailChoiceError(f'Invalid index: {i}')


# Defines the number of attemps that are allowed before failing
n_attempts = 5

# Create an inbox and poulate with emails
inbox = Inbox() # This instantiates the inbox 
inbox.populate_inbox()

while True:
    user_choice = input('''\nWould you like to:
1. Read an email
2. View unread emails
3. Quit application

Enter selection:
>>> ''')

    try:
        int_user_choice = int(user_choice)
    except ValueError:
        print(f'Invalid choice - must be an integer: {user_choice}')
        continue
       
    if user_choice == 1:
        print("Select email you wish to read:")
        inbox.list_emails()

        for attempts in range(n_attempts):
            try:
                try:
                    email_idx = int(input(">>> ").strip()) # This strips out all spaces
                except ValueError:
                    raise InvalidInputError("This is not an integer")
                inbox.read_email(email_idx)
                break
            except (InvalidInputError, EmailChoiceError):
                pass
        else:
            raise TooManyAttempts(f"Failed to choose an email in {n_attempts} attemps")
        
    elif user_choice == 2:
        print()
        for index, e in enumerate(inbox.email_list, start=1):
            if not e.has_been_read:
                inbox.read_email(index)
    
    elif user_choice == 3:
        exit()
    
    else:
        print("Oops - incorrect input.")
        