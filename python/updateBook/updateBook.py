def updateBook(conn, book):
    """
    update book's title, page number, DDC
    """
    sql = ''' UPDATE books
              SET title = ? ,
                  pageNumber = ? ,
                  DDC = ?
              WHERE id = ?'''
    cur = conn.cursor()
    cur.execute(sql, book)
    conn.commit()
    return True