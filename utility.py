

import mysql.connector
from mysql.connector import Error

class ConnectionUtil:

    def get_connection(self):
        try:
            self.connection = mysql.connector.connect(
                host='localhost',
                database='sakila',
                user='root',
                password='Visioture'
            )
            if self.connection.is_connected():
                print('Connection established')
        except Error as e:
            print(e)
        return self.connection

    def get_cursor(self, connection):
        self.cursor = connection.cursor()
        print('Cursor created')
        return self.cursor

    def close_connection(self, connection):
        connection.close()
        print('Connection closed')

    def getAllActors(self):

        self.cursor.execute(
            """
            SELECT a.first_name, a.last_name
            FROM actor ORDER BY LAST_NAME
            """
            )
        records = self.cursor.fetchall()
        for row in records:
            print(row)

    
    def getAllFilm(self):

        self.cursor.execute(
            """
            SELECT * FROM film
           
            """
            )
        records = self.cursor.fetchall()
        for row in records:
            print(row)        


    def getFilmByTitle(self):

        self.cursor.execute(
            """
            SELECT title
            FROM `sakila`.`film`;
           
            """
            )
        records = self.cursor.fetchall()
        for row in records:
            print(row)       


    def getFilmByDirectors(self):

        self.cursor.execute(
            """
            SELECT title
            FROM `sakila`.`film`;
           
            """
            )
        records = self.cursor.fetchall()
        for row in records:
            print(row)       
