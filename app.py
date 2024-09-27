from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

# Configuration de la connexion à la base de données
DB_NAME = "mydb"
DB_USER = "postgres"
DB_PASS = "password"
DB_HOST = "db"  # Nom du conteneur pour la base de données

def get_db_connection():
    connection = psycopg2.connect(
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS,
        host=DB_HOST,
        port="5432"
    )
    return connection

@app.route('/')
def index():
    # Connexion à la base de données et récupération des noms de tables
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';")
    tables = cur.fetchall()
    cur.close()
    conn.close()
    # Retourne la liste des tables dans une réponse JSON
    return jsonify({"Tables in public schema": [table[0] for table in tables]})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
