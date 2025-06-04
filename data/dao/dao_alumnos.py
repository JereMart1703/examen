from data.modelo.alumnos import alumnos

class DaoAlumnos:
    def get_all(self, db) -> list[alumnos]:
        cursor = db.cursor()

        cursor.execute("SELECT * FROM alumnos")

        alumnos_en_db = cursor.fetchall()
        lista_alumnos: list[alumnos] = []
        for alumno in alumnos_en_db:
            obj = alumnos(alumno[0], alumno[1], alumno[2], alumno[3], alumno[4])
            lista_alumnos.append(obj)  # Aquí usas la lista, no la clase
        cursor.close()
        return lista_alumnos

####################### AÑADIR ################################

    def insert(self, db, nombre: str, nota1: float, nota2: float, nota3: float):
        cursor = db.cursor()
        sql = "INSERT INTO alumnos (nombre, nota1, nota2, nota3) VALUES (%s, %s, %s, %s)"
        data = (nombre, nota1, nota2, nota3)
        cursor.execute(sql, data)
        db.commit()
        cursor.close()


################### BORRAR ###################################

    def delete(self, db, nombre: str): ############# EL SELF DA ERROR SI SE PONEN MAL LOS ESPACIOS ######################
        cursor = db.cursor()
        sql = "DELETE FROM alumnos WHERE id = %s"
        data = (nombre,)
        cursor.execute(sql, data)
        db.commit()
        cursor.close()


################# ACTUALIZAR #################################

    def update(self, db, nota1: int, nota2: int, nota3: int):
        cursor = db.cursor()
        sql = "UPDATE alumnos SET nota1 = %s, nota2 = %s, nota3 = %s WHERE id = %s"
        data = (nota1, nota2,nota3, id)
        cursor.execute(sql, data)
        db.commit()
        cursor.close()