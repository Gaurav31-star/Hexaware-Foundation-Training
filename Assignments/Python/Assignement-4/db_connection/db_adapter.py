import mysql.connector


def get_db_connection():
    # Replace the following values with your MySQL server credentials
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'localhost',
        'database': 'couriermanagementsystem',
        'port':'3306',
        'auth_plugin':'mysql_native_password'
    }

    try:
        connection = mysql.connector.connect(**config)
        # print("Connected to the database")
        # print('hello World')
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None


def get_ids(table_name, id_column_name):
    mydb = get_db_connection()
    my_cursor = mydb.cursor()
    sql = 'SELECT ' + id_column_name + ' FROM ' + table_name + ' ORDER BY ' + id_column_name + ' DESC LIMIT 1'
    # print(sql)
    my_cursor.execute(sql)
    x = list(my_cursor.fetchone())[0]
    return int(x) + 1


def get_cnts(table_name, id_column_name, column_id):
    mydb = get_db_connection()
    my_cursor = mydb.cursor()
    sql = 'SELECT count(*) as count FROM ' + table_name + ' WHERE ' + id_column_name + '=' + column_id
    # print(sql)
    my_cursor.execute(sql)
    x = list(my_cursor.fetchone())[0]
    return int(x)

def get_counts(table_name, id_column_name1, id_column_name2, column_id1, column_id2):
    mydb = get_db_connection()
    my_cursor = mydb.cursor()
    sql = 'SELECT count(*) as count FROM ' + table_name + ' WHERE ' + id_column_name1 + '=' + column_id1 + ' AND ' + id_column_name2 + '=' + '"' + str(column_id2) + '"'
    # print(sql)
    my_cursor.execute(sql)
    x = list(my_cursor.fetchone())[0]
    # print(x)
    return int(x)