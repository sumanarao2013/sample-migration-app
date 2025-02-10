from flask import Flask, jsonify, request
import sqlite3
import os

app = Flask(__name__)
DATABASE = 'users.db'

def init_db():
    conn = sqlite3.connect(DATABASE)
    conn.execute('''CREATE TABLE IF NOT EXISTS users
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 name TEXT NOT NULL,
                 email TEXT UNIQUE NOT NULL)''')
    conn.close()

@app.route('/users', methods=['GET'])
def get_users():
    conn = sqlite3.connect(DATABASE)
    users = conn.execute('SELECT * FROM users').fetchall()
    conn.close()
    return jsonify(users)

@app.route('/users', methods=['POST'])
def add_user():
    user_data = request.get_json()
    conn = sqlite3.connect(DATABASE)
    conn.execute('INSERT INTO users (name, email) VALUES (?, ?)',
                (user_data['name'], user_data['email']))
    conn.commit()
    conn.close()
    return jsonify({"message": "User added successfully"})

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)
