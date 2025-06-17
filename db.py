# db.py
import mysql.connector

def conectar():
    return mysql.connector.connect(
        user="root",
        password="",  # tu contraseña si tienes
        host="localhost",
        database="videojuego"
    )