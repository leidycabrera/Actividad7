from app import mysql

class Fases:
    @staticmethod
    def get_all_phase():
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM fases_paquete")
        fases = cur.fetchall()
        cur.close()
        return fases
    