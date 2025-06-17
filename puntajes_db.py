# puntajes_db.py
import db

def guardar_puntaje(usuario_id, puntaje):
    conn = db.conectar()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO puntajes (usuario_id, puntaje) VALUES (%s, %s)",
        (usuario_id, puntaje)
    )
    conn.commit()
    conn.close()

    
def obtener_ranking():
    conn = db.conectar()
    cur = conn.cursor()
    cur.execute("""
        SELECT u.username, MAX(p.puntaje) as max_puntaje
        FROM usuarios u
        JOIN puntajes p ON u.id = p.usuario_id
        GROUP BY u.username
        ORDER BY max_puntaje DESC
        LIMIT 10
    """)
    ranking = cur.fetchall()
    conn.close()
    return ranking