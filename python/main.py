from createConnection.createConnection import createConnection
from createBook.createBook import createBook
from updateBook.updateBook import updateBook
from deleteBook.deleteBook import deleteBook
from readBook.readBooks import readBooks

def printMenu():
    print('////////////////////////////////////////////////')
    print('1. Read all books')
    print('2. Create a new book')
    print('3. Update a book')
    print('4. Delete a book')
    print('5. Exit')
    

def main():
    while True:
        printMenu()
        action = input('Enter your action: ')
        conn = createConnection('./db/books.db')

        if action == '1':
            # read all users
            readBooks(conn)
        elif action == '2':
            # create a new user
            createBook(conn)
        elif action == '3':
            # update a user
            updateBook(conn)
        elif action == '4':
            # delete a user
            deleteBook(conn)
        elif action == '5':
            # exit the program
            print('Exiting program...')
            exit()
        else:
            # invalid action choice
            print('Invalid action choice. Please try again.')
            continue
        
main()