from sqlalchemy import text

from connect import session

if __name__ == "__main__":
    q = session.execute(text("SELECT * FROM students"))
    for row in q:
        print(row)

    session.close()