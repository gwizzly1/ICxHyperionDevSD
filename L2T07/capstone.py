'''
--------------------------------------
Task: Create a bookstore program where the user can input the following questions:
1) Enter Book
2) Update Book
3) Delete Book
4) Search Books
0) Exit

This should be in a ebookstore database and stored in a table called book
--------------------------------------
'''

import sqlite3
db = sqlite3.connect('ebookstore')
cursor = db.cursor()
book_stack = [(3001, 'A Tale of Two Cities', 'Charles Dickens', 30),(3002, 'Harry Potter and the Philosopher\'s stone', 'J.K. Rowling', 40), (3003, 'The Lion, The Witch and the Wardrobe', 'C.S. Lewis', 25), (3004, 'The Lord of the Rings', 'J.R.R. Tolkien', 37), (3005, 'Alice in Wonderland', 'Lewis Carroll', 12)]

attempts = 5
'''
---------- This is to create a table and insert the values into it ------------
'''

# create class for the books - manipulate to get the correct values to add into the 
def create_ebookstore(book_stack):
    try:
        sqlite_create_table = '''CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, author TEXT, qty INTEGER)'''
        sqlite_insert_table = ''' INSERT INTO book(id, title, author, qty) VALUES(?,?,?,?) '''
        cursor.execute('''drop table if exists book''')
        cursor.execute(sqlite_create_table)
        cursor.executemany(sqlite_insert_table, book_stack)
        db.commit() # This causes it to bug out when the table already exists - still causes it to bug out 
    except sqlite3.Error as error:
        print("Failed to insert Python variable into sqlite table", error)

def enter_book(title, author, qty):
    new_book_title = input('Please enter the title of the new book: ')
    new_book_author = input('Please enter the author of the new book: ')
    new_book_qty = input('Please enter the quantity of new book: ')
    id_last = cursor.execute('''SELECT LAST_INSERT_ROWID();''')
    id_new = id_last.replace("'","").split() # NEED TO FIND PUT HOW TO ADD 1   
    new_book = [(id_new, new_book_title, new_book_author, new_book_qty)]

    cursor.executemany(''' INSERT INTO book(id, title, author, qty) VALUES(?,?,?,?)''', new_book)
    db.commit()

def update_book(title, author):
    for attempt in attempts: 
        try: 
            title = input('Please enter the title of the book you\d like to change')
            author = input('Please enter the author of the book you\d like to update')
            update_choice = input('Please enter the name of what you\'d like to update (as written):'
                                        '\n' 'id'
                                        '\n' 'title'
                                        '\n' 'author'
                                        '\n' 'qty')
            update_name = input('Please enter what you\d like the field to be updated to')

            cursor.execute('''UPDATE books SET ? = ? WHERE title = ? AND author = ''', (update_choice, update_name, title, author))
            db.commit() 
        except sqlite3.Error as error:
            print("Failed to update sqlite table", error)

def delete_book(id):
    cursor.execute('''DELETE FROM student WHERE id = ? ''',(id))
    cursor.execute('''DROP TABLE student''')
    db.commit()

def search_book(title, author):
    pass

def field_choice():
    field_choice = input('Please input what field you would like this to be based on:'
                            '\n' 'id'
                            '\n' 'title'
                            '\n' 'author'
                            '\n' 'qty')  
    return field_choice
    # Check that this matches                                     

def menu_choice(): # What should the input be?
     return input(
            'Select one of the following options:'
            '\n' '1 - enter a book'
            '\n' '2 - update a book'
            '\n' '3 - delete a book'
            '\n' '4 - search for a book'
            '\n' '0 - exit:'
            '\n>>>'
        ).lower() # Add error handling for inputs! Only expect numbers, if not number error

def numberError(Exception):
    pass

'''

def show_menu(config_filepath):
    while True:
        menu = menu_choice()

        if menu == '1':   
            enter_book(name, title, author, qty)
        elif menu == '2':
            update_book_title = input('Please enter the title of the book you would like to update')
            update_book_author = input('Please enter the author of the book you\'d like to update')
            update_book(title, author)
        elif menu == '3':
            id = input('Please input the id of the book you would like to delete. If you don\'t know this please use the search function.')
            delete_book(id)
        elif menu == '4':
            search_book(name, title, author, qty)
        elif menu == '0':
            print('Goodbye!!!')
            exit()
        else:
            print("You have made entered an invalid input. Please try again")

    

if __name__ == '__main__': # This runs show_menu function which is the basis for everthing else
    show_menu('user.txt')
'''
create_ebookstore(book_stack)
enter_book('Y','Z',5)

