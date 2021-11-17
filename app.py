from flask import Flask
from database.ConnectionFactory import ConnectionFactory

app = Flask(__name__)
database = ConnectionFactory(app)

from controllers import sellers

if __name__ == '__main__':
    app.run(debug=True)