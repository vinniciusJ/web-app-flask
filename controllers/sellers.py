from __main__ import app, database
from flask import render_template

@app.route('/')
@app.route('/sellers')

def get_sellers():
    connection = database.get_connection()
    connection_cursor = connection.cursor()

    connection_cursor.execute('SELECT * FROM seller')
    data = connection_cursor.fetchall()

    return render_template('sellers.html', sellers=data)

@app.route('/sellers/<id>')

def find_seller(id):
    connection = database.get_connection()
    connection_cursor = connection.cursor()

    connection_cursor.execute(f'SELECT * FROM seller WHERE Id = {id}')
    datum = connection_cursor.fetchall()[0]


    return render_template('seller.html', seller=datum)

@app.route('/sellers/register')

def register_seller():
    return 'mostrar formulario'

