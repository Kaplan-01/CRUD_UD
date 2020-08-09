''' 
NOMBRE: Maria del Carmen Hernandez Diaz
ACCOUNT: 1718110389
GROUP: TIC 51
DATE: 09-08-2020
DESCRIPTION: Update and delete objetive
'''
import mysql.connector

class Alumnos():
# Conexion
        def connect(self):
            try:
                self.cnx = mysql.connector.connect(
                    # Usamos el nombre de nuestro usuario con la contrasena.
                    user='melanie', 
                    password='Agenda.2020',
                    host='127.0.0.1',
                    port=3309,
                    database='escuela'
                    )
                self.cursor = self.cnx.cursor()

            except Exception as e:
                print(e)


        # Realizamos una consulta de todos los datos existentes de todas las columnas y filas
        def select(self):
            try:
                self.connect()
                # Consulta
                query = ("SELECT * from alumnos;")
                self.cursor.execute(query)
                # Arreglo
                result = []
                for row in self.cursor:
                    # Diccionario para almacenamiento
                    r = {
                        'id_alumno':row[0],
                        'matricula':row[1],
                        'nombre':row[2],
                        'primer_apellido':row[3],
                        'segundo_apellido':row[4],
                        'edad':row[5],
                        'fecha_nacimiento':row[6],
                        'sexo':row[7],
                        'estado':row[8],
                    }
                    result.append(r)
                self.cursor.close()
                self.cnx.close()
                return result

            except Exception as e:
                print(e)
                # En caso de que haya problemas con el diccionario
                result = []
                return result
    # Insertar

        def insertar(self, matricula, nombre, primer_apellido, segundo_apellido, edad, fecha_nacimiento, sexo, estado):
            try:
                self.connect()
                query = ("INSERT INTO alumnos (matricula, nombre, primer_apellido, segundo_apellido, edad, fecha_nacimiento, sexo, estado) values(%s, %s, %s, %s, %s, %s, %s, %s);")
                values = (matricula, nombre, primer_apellido, segundo_apellido, edad, fecha_nacimiento, sexo, estado)
                self.cursor.execute(query, values)
                self.cnx.commit()
                self.cursor.close()
                self.cnx.close()
                return True
            except Exception as e:
                print(e)
                return False

    # Eliminar

        def borrar(self, id_alumno, ):
            try:
                self.connect()
                query = ("DELETE FROM alumnos WHERE id_alumno = %s;")
                values = (id_alumno,)
                self.cursor.execute(query, values)
                self.cnx.commit()
                self.cursor.close()
                self.cnx.close()
                return True
            except Exception as e:
                print(e)
                return False

    # Vista

        def view(self, id_alumno):
            try:
                self.connect()
                query = ("SELECT * from alumnos where id_alumno = %s;")
                values = (id_alumno,)
                self.cursor.execute(query, values)
                result = []
                for row in self.cursor:
                     r = {
                        'id_alumno':row[0],
                        'matricula':row[1],
                        'nombre':row[2],
                        'primer_apellido':row[3],
                        'segundo_apellido':row[4],
                        'edad':row[5],
                        'fecha_nacimiento':row[6],
                        'sexo':row[7],
                        'estado':row[8],
                    }
                result.append(r)
                self.cursor.close()
                self.cnx.close()
                return result
            except Exception as e:
                print(e)
                result = []
                return result

    # Actualizar

        def modificar(self, id_alumno, matricula, nombre, primer_apellido, segundo_apellido, edad, fecha_nacimiento, sexo, estado):
            try:
                self.connect()
                query = ("UPDATE alumnos SET matricula=%s, nombre=%s, primer_apellido=%s, segundo_apellido=%s, edad=%s, fecha_nacimiento=%s, sexo=%s, estado=%s WHERE id_alumno=%s;")
                values = (matricula, nombre, primer_apellido, segundo_apellido, edad, fecha_nacimiento, sexo, estado, id_alumno)
                self.cursor.execute(query, values)
                self.cnx.commit()
                self.cursor.close()
                self.cnx.close()
                return True
            except Exception as e:
                print(e)
                return False


objeto = Alumnos()
objeto.connect()
objeto.modificar(7, 123423567,'Melanie', 'Kaplan', 'Armstrong', 19, '2000-10-10', 'Femenino', 'Soltero'),

#for row in objeto.select():
#    print(row)

for row in objeto.view(1):
    print(row)
    
    # En caso de requerir solo uno es como:
    # print(row['nombre'])

