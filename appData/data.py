import mysql.connector
from mysql.connector import errorcode

    
# ====== DATABASE HANDLER ====== #
class Connect:
    """ Context manager for MySQL connection object """
    def __init__(self, config: dict, database: str) -> object:
        self.DB_CONFIG = config
        self.DB = database

    def __enter__(self):
        try:
            self.cnx = mysql.connector.connect(
                user=self.DB_CONFIG['user'],
                passwd=self.DB_CONFIG['passwd'],
                host=self.DB_CONFIG['host'],
                port=self.DB_CONFIG['port'],
                auth_plugin=self.DB_CONFIG['auth_plugin'],
                database=self.DB
            )
            return self.cnx # 
            # --
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                return None, "User and/or password is incorrect"
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                return None, "Database does not exist"
            else:
                return None, err

    def __exit__(self, type, value, traceback):
        self.cnx.close()
# -- QUERIES -- #
class SQL:
    @staticmethod
    def version(cursor: object) -> str:
        """ Shows MySQL version number

        Args:
            cursor (object): connection object cursor

        Returns:
            str: formatted repr
        """     
        query = "SHOW VARIABLES like 'version';"
        cursor.execute(query)
        result = cursor.fetchall()
        version = result[0]
        return F"MySQL {version[0]} {version[1]}"

    @staticmethod
    def inject(cursor: object, query: str, *args) -> list[tuple]:
        """ Inject a query string with optional args

        Args:
            cursor (object): connection object cursor
            query (str): SQL query with optional arguments to replace % tags

        Returns:
            list[str]: returns a list of strings
        """
        cursor.execute(query, args)
        raw_data = cursor.fetchall()
        # result = [item[0] for item in raw_data]
        return raw_data # result
