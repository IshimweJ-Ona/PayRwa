import mysql.connector
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import get_db_connection

class User(UserMixin):
    def __init__(self, id, username, email, password_hash, currency):
        self.id = id
        self.username = username
        self.email = email
        self.password_hash = password_hash
        self.currency = currency

    @staticmethod
    def get_by_id(user_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, username, email, password, currency FROM users WHERE id = %s", (user_id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return User(*row)
        return None
    
    @staticmethod
    def get_by_username(username):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, username, email, password, currency FROM users WHERE username = %s", (username,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return User(*row)
        return None
    
    @staticmethod
    def create(username, email, password, currency):
        password_hash = generate_password_hash(password)
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                "Insert INTO users (username, email, password, currency) VALUES (%s, %s, %s, %s)",
                (username, email, password_hash, currency)
            )
            conn.commit()
            user_id = cursor.lastrowid
            return User(user_id, username, email, password_hash, currency)
        except mysql.connector.IntegrityError:
            return None
        finally:
            conn.close()

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
def add_transaction(user_id, amount, paid_to, date):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO transactions (user_id, amount, paid_to, date) VAlUES (%s, %s, %s, %s)",
        (user_id, amount, paid_to, date)
    )
    conn.commit()
    conn.close()

def get_transactions(user_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT amount, paid_to, date FROM transactions WHERE user_id = %s ORDER BY date DESC",
        (user_id,)
    )
    rows = cursor.fetchall()
    conn.close()
    return [{'amount': row[0], 'paid_to': row[1], 'date': row[2]} for row in rows]
        