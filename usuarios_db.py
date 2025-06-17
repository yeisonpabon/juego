# usuarios_db.py

import hashlib
import db

def registrar_usuario(username, password):
    conn = db.conectar()
    cur = conn.cursor()
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    try:
        # Verificar si el usuario ya existe
        cur.execute("SELECT id FROM usuarios WHERE username = %s", (username,))
        if cur.fetchone():
            print("El usuario ya existe.")
            return False
        cur.execute(
            "INSERT INTO usuarios (username, password) VALUES (%s, %s)",
            (username, password_hash)
        )
        conn.commit()
        print("Usuario registrado.")
        return True
    except Exception as e:
        print("Error al registrar:", repr(e))
        return False
    finally:
        conn.close()


def login_usuario(username, password):
    conn = db.conectar()
    cur = conn.cursor()
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    cur.execute("SELECT id FROM usuarios WHERE username=%s AND password=%s", (username, password_hash))
    user = cur.fetchone()
    conn.close()
    if user:
        return user[0]  # id del usuario
    else:
        return None
    
import db

def obtener_ranking():
    conn = db.conectar()
    cur = conn.cursor()
    cur.execute("""
        SELECT u.username, SUM(p.puntaje) AS total_puntaje
        FROM usuarios u
        JOIN puntajes p ON u.id = p.usuario_id
        GROUP BY u.id
        ORDER BY total_puntaje DESC
        LIMIT 10
    """)
    ranking = cur.fetchall()
    conn.close()
    return ranking