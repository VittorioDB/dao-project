from utility import ConnectionUtil

connection = ConnectionUtil()
connession = connection.get_connection()
cursor = connection.get_cursor(connession)

cursor.execute(
        """
        SELECT * FROM film
       
        """
        )
records = cursor.fetchall()
for row in records:
        print(row)

cursor.close()
connection.close_connection(connession)