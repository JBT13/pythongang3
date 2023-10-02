def dbReadBook(conn, id):
  """
  Find book by id
  """
  cur = conn.cursor()
  cur.execute("SELECT * FROM books WHERE id = ?", (id,))

  row = cur.fetchone()
  if row is None:
    raise ValueError("Book not found")
  
  return row

def dbDeleteBook(conn, id):
  sql = 'DELETE FROM books WHERE id=?'
  cur = conn.cursor()
  try:
    cur.execute(sql, (id,))
    conn.commit()
  except:
    print("Deletion failed")
    return False
  
def deleteBook(conn):
    """
    Delete book
    """
    id = input('Enter user id to be deleted: ')
    try:
        id = int(id)
    except ValueError:
        print("Invalid id")
        return False
    
    book = dbReadBook(conn, id)
    print(f"Are you sure you want to delete book {book[1]} {book[2]} (id: {book[0]})?")
    confirmation = input("Type 'yes' to confirm: ")
    if confirmation.lower() != "yes":
        print("Deletion cancelled")
        return False
    dbDeleteBook(conn, id)
    print("Book deleted successfully")
    return True