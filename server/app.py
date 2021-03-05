from flask import Flask, jsonify, request
from flask_cors import CORS
import MySQLdb


# configuration
DEBUG = True
# passwordless root access to db running locally.
host = '127.0.0.1'
user = 'root'
password = ''
port = 3306
db = 'shopping_list'

DB_CONN = MySQLdb.Connection(
        host = host,
        user = user,
        passwd = password,
        port = port,
        db = db
)

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


@app.route('/list', methods=['GET'])
def handle_list():
    if request.method == 'GET':
        DB_CONN.query("""SELECT * FROM list;""")
        res = DB_CONN.store_result()
        json_data = []

        for i in range(res.num_rows()):
            json_data.append(res.fetch_row(maxrows=1, how=1)[0])

        return jsonify(json_data)

@app.route('/item', methods=['POST'])
def handle_post():
    json_data = request.json
    item = json_data['item']
    quantity = json_data['quantity']
    price = json_data['price']

    DB_CONN.query(f"""INSERT INTO list (item, quantity, price) VALUES ("{item}", {quantity}, {price});""")
    DB_CONN.commit()
    print(f'**POSTED ITEM**\nitem: {item}\nquantity: {quantity}\nprice: {price}')
    return jsonify('oohh we\'re postin!')

@app.route('/<id>', methods=['DELETE'])
def handle_delete(id=-1):
    if id == -1:
        return jsonify('You can\'t delete that!')
    
    DB_CONN.query(f"""DELETE FROM list WHERE id = {id};""")
    DB_CONN.commit()
    print('deleted!')
    return jsonify(f'deleted! {id}')

if __name__ == '__main__':
    app.run()
