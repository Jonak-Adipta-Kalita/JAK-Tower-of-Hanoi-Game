import os
import mysql
import mysql.connector

from dotenv import load_dotenv # type: ignore

load_dotenv()

class Database:
    def __init__(self):
        self.db = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database="tower_of_hanoi",
        )
        self.cursor = self.db.cursor()

        self.curr_user = ""
        self.stored_score_in_session = False

    def close_db(self):
        self.db.close()

    def call_file_query(self, filename: str, *args):
        with open(os.path.join("src", "database", filename), "r") as f:
            query = f.read()
            self.cursor.execute(query, args)
            fetched = self.cursor.fetchone()
            self.db.commit()

            return fetched

    def login_or_register(self):
        username = input("Enter your Username: ")
        password = input("Enter your Password: ")

        self.cursor.execute("SELECT password FROM players WHERE username=%s;", (username,))
        res = self.cursor.fetchall()

        if len(res) == 0:
            self.cursor.execute(
                "INSERT INTO players (username, password) VALUES (%s, %s)",
                (username, password)
            )
            self.db.commit()
        elif password != res[0][0]: # type: ignore
            raise Exception("Authentication Error | Password is Wrong!")

        self.curr_user = username


    def store_highscore(self, score: int, moves: int):
        self.stored_score_in_session = True