from flaskext.mysql import MySQL, pymysql

class ConnectionFactory:
    app = None

    def __init__(self, app) -> None:
        self.app = app

        self.app.config['MYSQL_DATABASE_USER'] = 'root'
        self.app.config['MYSQL_DATABASE_PASSWORD'] = 'bancodedados'
        self.app.config['MYSQL_DATABASE_DB'] = 'flask_sellers'
        self.app.config['MYSQL_DATABASE_HOST'] = 'localhost'

        self.mysql = MySQL(cursorclass=pymysql.cursors.DictCursor)
        self.mysql.init_app(self.app)

    def get_connection(self):
        self.mysql_connection = self.mysql.connect()

        return self.mysql_connection