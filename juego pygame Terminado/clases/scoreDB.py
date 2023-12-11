import sqlite3

class ScoreDB():

    def crear_DB(self):
        with sqlite3.connect("registros.db") as conexion:
            try:
                sentencia = ''' CREATE TABLE score
                                (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    usuario TEXT,
                                    correctas INTEGER,
                                    incorrectas INTEGER,
                                    vidas INTEGER
                                )
                            '''
                conexion.execute(sentencia)
                conexion.commit()
            except sqlite3.OperationalError:
                print("la tabla score ya existe")


    def insertar_registro(self, usuario, correctas, incorrectas, vidas):
        with sqlite3.connect("registros.db") as conexion:
            try:
                sentencia = " INSERT INTO score(usuario, correctas, incorrectas, vidas) VALUES (?,?,?,?)"
                conexion.execute(sentencia, (usuario, correctas, incorrectas, vidas))
                conexion.commit()
            except:
                print("error")


    def seleccionar_registros(self): #devuelve los registros en formato list[tuple]
        with sqlite3.connect("registros.db") as conexion:
            cursor = conexion.execute("SELECT usuario, correctas, incorrectas, vidas FROM score ORDER BY correctas DESC, incorrectas ASC, vidas DESC LIMIT 5")
            registros = cursor.fetchall()
            return registros
        