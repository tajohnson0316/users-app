from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE


class User:
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def get_all(cls):
        query = """ 
        SELECT *
        FROM users;
        """

        result = connectToMySQL(DATABASE).query_db(query)

        list_of_users = []
        for row in result:
            list_of_users.append(cls(row))

        return list_of_users

    @classmethod
    def get_one(cls, data):
        query = """ 
        SELECT *
        FROM users
        WHERE id = %(id)s
        """

        result = connectToMySQL(DATABASE).query_db(query, data)
        return cls(result[0])

    @classmethod
    def create_one(cls, data):
        query = """ 
        INSERT INTO users (first_name, last_name, email)
        VALUES (%(first_name)s, %(last_name)s, %(email)s);
        """

        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def update_one(cls, data):
        query = """ 
        UPDATE users
        SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s
        WHERE id = %(id)s;
        """

        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def delete_one(cls, data):
        query = """ 
        DELETE FROM users
        WHERE id = %(id)s;
        """
        # returns None
        return connectToMySQL(DATABASE).query_db(query, data)
