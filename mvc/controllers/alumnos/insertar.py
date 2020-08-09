import web # IMPORTACCION DE WEB.

import mvc.models.model as model

model_alumnos = model.Alumnos()

render = web.template.render("mvc/views/alumnos/")

''' 
NOMBRE: Maria del Carmen Hernandez Diaz
ACCOUNT: 1718110389
GROUP: TIC 51
DATE: 09-08-2020
DESCRIPTION: Update and delete objetive
'''

class Insertar():
    
    def GET(self):
        try:
            return render.insertar() # RETORNAMOS EL REDERIZADO.
        except Exception as e:
            return "Error " + str(e.args) # EN CASO DE ERRORES, LOS DEVOLVERA.

    def POST(self):
        try:
            form = web.input()
            print(form.nombre)
            matricula = form.matricula
            nombre = form.nombre
            primer_apellido = form.primer_apellido
            segundo_apellido = form.segundo_apellido
            edad = form.edad
            fecha_nacimiento = form.fecha_nacimiento
            sexo = form.sexo
            estado = form.estado
            model_alumnos.insertar(matricula, nombre, primer_apellido, segundo_apellido, edad, fecha_nacimiento, sexo, estado)
            print(form)

        except Exception as e:
            return render.insertar()
