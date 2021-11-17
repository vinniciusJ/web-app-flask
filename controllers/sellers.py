from __main__ import app, database


@app.route('/')
@app.route('/sellers')

def get_sellers():
    connection = database.get_connection()
    connection_cursor = connection.cursor()

    connection_cursor.execute('SELECT * FROM seller')
    data = connection_cursor.fetchall()

    for datum in data: 
        print(datum)


    return 'vendedores'

@app.route('/sellers/<id>')

def find_seller(id):
    return f'obter {id}'

@app.route('/sellers/register')

def register_seller():
    return 'mostrar formulario'

