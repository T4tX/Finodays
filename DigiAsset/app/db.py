import psycopg2


conn = psycopg2.connect(dbname='postgres', user='postgres', password='postgres', host='db')

cursor = conn.cursor()


def db_init():

    cursor.execute(
        "CREATE TABLE IF NOT EXISTS users (id serial NOT NULL PRIMARY KEY,login TEXT, password TEXT, reg_date TEXT)")

    cursor.execute(
        "CREATE TABLE IF NOT EXISTS products (id serial NOT NULL PRIMARY KEY,user_id INTEGER, token TEXT NOT NULL, name TEXT NOT NULL, create_date TEXT)")

    cursor.execute(
        "CREATE TABLE IF NOT EXISTS orders (id serial NOT NULL PRIMARY KEY,from_user_id INTEGER,to_user_id INTEGER, price INTEGER NOT NULL, product_id INTEGER NOT NULL, create_date TEXT)")

    cursor.execute(
        "insert into users values (default,'test1','test1','01.10.2022'),(default,'test2','test2','01.10.2022')")
    cursor.execute(
        "insert into products values (default,0,'token1','name1','01.10.2022'),(default,0,'token2','name2','01.10.2022')")
    cursor.execute(
        "insert into orders values (default,0,1,100,0,'01.10.2022'),(default,1,0,100,1,'01.10.2022')")
    cursor.execute('select * from users')

    records = cursor.fetchall()

    print(records)


db_init()


def query(query):
    cursor.execute(query)
    records = cursor.fetchall()
    return records
