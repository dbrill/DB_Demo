import MySQLdb

# passwordless root access to db running locally.
host = '127.0.0.1'
user = 'root'
password = ''
port = 3306
db = 'shopping_list'

conn = MySQLdb.Connection(
        host = host,
        user = user,
        passwd = password,
        port = port,
        db = db
)

conn.query("""SELECT * FROM list""")
result = conn.store_result()

for i in range(result.num_rows()):
    print(result.fetch_row())

