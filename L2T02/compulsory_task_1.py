"""
Compulsory Task 1: 
------------------

Copy the code provided below to a new file named compulsory_task_1.py: 
1. Add another method in the Course class that prints the head office location: Cape Town
2. Create a subclass of the Course class named OOPCourse
3. Create a constructor that initialises the following attributes and assigns these values:
    --- "description" with a value "OOP Fundamentals"
    --- "trainer" with a value "Mr Anon A. Mouse"
4. Create a method in the subclass named "trainer_details" that prints what the 
   course is about and the name of the trainer by using the description and trainer attributes.
5. Create a method in the subclass named "show_course_id" that prints the ID number of the course: #12345
6. Create an object of the subclass called course_1 and call the following methods
   contact_details
   trainer_details
   show_course_id
   These methods should all print out the correct information to the terminal

Note: this task covers single inheritance. Multiple inheritance is also possible in Python and 
we encourage you to do some research on multiple inheritance when you have finished this course.
"""
class Course:
    '''
    This creates global variables of name and contact_website for the course it contains the methods of:
    >>>> contact_details which prints the website
    >>>> head_office which is 'Cape town'
    '''
    name = "Fundamentals of Computer Science"
    contact_website = "www.hyperiondev.com"

    def contact_details(self):
        print(f"Please contact us by visiting: {self.contact_website}")
    
    def head_office(self):
        print("Cape Town") 

class OOPCourse(Course):
    '''
    This class inherits all traits from the Course class
    It includes the descrpition and the trainer and has methods of:
    >>>> trainer_details - prints trainer details
    >>>> show_course_id which prints the course ID 
    '''
    def __init__(self, description = "OOP Fundamentals", trainer = "Mr Anon A. Mouse"):
        self.description = description
        self.trainer = trainer

    def trainer_details(self):
        print(f"{self.description}, {self.trainer}")

    def show_course_id(self):
        print('#12345')

course_1 = OOPCourse() # This creates an instantiation

course_1.contact_details()
course_1.trainer_details()
course_1.show_course_id()