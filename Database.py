
import psycopg2

def connection():
    con = psycopg2.connect(
        host = "localhost",
        database = "ecommerce",
        user = "postgres",
        password = "1234",
        port = 5432
    )

    if con:
        print(">>>> CONNECTION ESTABLISHED")
    else:
        print(">>>> CONNECTION FAILED")
    con.autocommit = True

    return con

conn = connection()