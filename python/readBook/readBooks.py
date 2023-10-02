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




def dbReadBooks(conn):
    """
    Query all rows in the books table
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM books ORDER BY title")

    rows = cur.fetchall()
    books = []
    for row in rows:
        book = {
            'title': row[1],
            'pageNumber': row[2],
            'DDC': row[3],
        }
        books.append(book)

    return books




def readBooks(conn):
    books = dbReadBooks(conn)
    for book in books:
        print(f"Title : {book['title']}, "
              f"Page Number: {book['pageNumber']}, "
              f"DDC: {book['DDC']}, ")
        print("")