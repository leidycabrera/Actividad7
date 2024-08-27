from app import mysql

class Paquete:
    @staticmethod
    def get_by_idpersona(id):
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM paquete WHERE idpersona = %s", (id,))
        paquete = cur.fetchall()
        cur.close()
        return paquete
    
    @staticmethod
    def get_all_byId(id):
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM paquete as p INNER JOIN fases_paquete f ON p.idfases_paquete = f.idfases_paquete "+
                    "INNER JOIN persona pe ON pe.idpersona = p.idpersona WHERE p.idpaquete = %s", (id,))
        paquete = cur.fetchall()
        cur.close()
        return paquete
    
    @staticmethod
    def get_all_packages():
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM paquete as p INNER JOIN fases_paquete f ON p.idfases_paquete = f.idfases_paquete "+
                    "INNER JOIN persona pe ON pe.idpersona = p.idpersona")
        paquetes = cur.fetchall()
        cur.close()
        return paquetes
    
    @staticmethod
    def get_package_byId(id):
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM paquete WHERE idpaquete = %s", (id,))
        paquete = cur.fetchone()
        cur.close()
        return paquete
    
    @staticmethod
    def edit(idpaquete, fecha_entrega, hora_entrega):
        print(idpaquete, fecha_entrega, hora_entrega)
        if idpaquete:
            try:
                cur = mysql.connection.cursor()
                query = """UPDATE paquete SET
                        fecha_entrega = %s,
                        hora_entrega = %s
                    WHERE idpaquete = %s"""
                valores = (fecha_entrega, hora_entrega, idpaquete)
                cur.execute(query, valores)
                mysql.connection.commit()
                cur.close()
                return True
            except Exception as e:
                print(f"Error al editar el paquete: {e}")
                mysql.connection.rollback()
                return False
        else :
            print(f"Error al editar el paquete")
            return False