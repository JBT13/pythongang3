def dbCreateBook(conn, book):
  sql = '''INSERT INTO books(title, pageNumber, DDC)
            VALUES(?,?,?)'''
  cur = conn.cursor()
  cur.execute(sql, book)
  conn.commit()
  return True


def createBook(conn):
    """
    Create a new user into the books table
    """
    # create a new user
    title = input('Enter your book title: ')
    pageNumber = input('Enter how many page numbers: ')
    DDC = input('Enter the DDC: ')


    book = (title, pageNumber, DDC)
    dbCreateBook(conn, book)
    return True