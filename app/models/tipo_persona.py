from app import mysql

class TipoPersona:
    @staticmethod
    def get_all_types():
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM tipo_persona")
        types = cur.fetchall()
        cur.close()
        return types
    
    @staticmethod
    def getId_by_type(type):
        cur = mysql.connection.cursor()
        cur.execute("SELECT idtipo_persona FROM tipo_persona where nombre_tipo = %s", (type,))
        type = cur.fetchall()
        cur.close()
        return type