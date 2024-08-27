from app import mysql

class Persona:
    @staticmethod
    def get_all_users():
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM persona")
        users = cur.fetchall()
        cur.close()
        return users
    
    @staticmethod
    def find_by_username(username):
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM persona WHERE username = %s", (username,))
        user = cur.fetchone()
        cur.close()
        return user
    
    @staticmethod
    def find_by_id(id):
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM persona as p INNER JOIN tipo_persona as tp ON p.idtipo_persona = tp.idtipo_persona WHERE p.idpersona = %s", (id,))
        user = cur.fetchone()
        cur.close()
        return user
    
    @staticmethod
    def get_by_tipoPersona(tipo):
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM persona as p INNER JOIN tipo_persona as tp ON p.idtipo_persona = tp.idtipo_persona WHERE tp.nombre_tipo = %s", (tipo,))
        user = cur.fetchall()
        cur.close()
        return user
    
    @staticmethod
    def get_by_tipoPersona2(tipo1, tipo2):
        cur = mysql.connection.cursor()
        query = """
        SELECT * 
        FROM persona as p 
        INNER JOIN tipo_persona as tp 
        ON p.idtipo_persona = tp.idtipo_persona 
        WHERE tp.nombre_tipo IN (%s, %s)
        """
        cur.execute(query, (tipo1, tipo2))
        user = cur.fetchall()
        cur.close()
        return user

    @staticmethod
    def save(idpersona, nombre, apellido, docidentidad, telefono, direccion, correo, username, password, idtipo_persona):
        try:
            cur = mysql.connection.cursor()
            if idpersona:  # Si idpersona está presente, es una actualización
                query = """
                UPDATE persona SET
                    nombre_persona = %s,
                    apellido = %s,
                    docidentidad = %s,
                    telefono = %s,
                    direccion = %s,
                    correo = %s,
                    username = %s
                WHERE idpersona = %s
                """
                valores = (nombre, apellido, docidentidad, telefono, direccion, correo, username, idpersona)
            else:  # Si no hay idpersona, es una inserción
                query = """
                INSERT INTO persona (
                    nombre_persona, apellido, docidentidad, telefono, direccion, correo, username, password, idtipo_persona
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                """
                valores = (nombre, apellido, docidentidad, telefono, direccion, correo, username, password, idtipo_persona)
            
            cur.execute(query, valores)
            mysql.connection.commit()
            cur.close()
            return True
        except Exception as e:
            print(f"Error al guardar la persona: {e}")
            mysql.connection.rollback()
            return False

    @staticmethod
    def delete(idpersona):
        try:
            cur = mysql.connection.cursor()
            query = "DELETE FROM persona WHERE idpersona = %s"
            cur.execute(query, (idpersona,))
            mysql.connection.commit()
            cur.close()
            return True
        except Exception as e:
            print(f"Error al eliminar la persona: {e}")
            mysql.connection.rollback()
            return False
