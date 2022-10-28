from utility import ConnectionUtil

connection = ConnectionUtil()
connession = connection.get_connection()
cursor = connection.get_cursor(connession)

cursor.execute(
        """
        SELECT a.first_name, a.last_name
        FROM actor a, film f, film_actor fa
        WHERE a.actor_id = fa.actor_id
        AND f.film_id = fa.film_id
        GROUP BY a.actor_id
        HAVING COUNT(f.film_id) >= 10
        ORDER BY LAST_NAME
        """
        )
records = cursor.fetchall()
for row in records:
        print(row)

cursor.close()
connection.close_connection(connession)