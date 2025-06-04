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