''' 
NOMBRE: Maria del Carmen Hernandez Diaz
ACCOUNT: 1718110389
GROUP: TIC 51
DATE: 19-07-2020
DESCRIPTION: Uso de la arquitectura MVC. Formulario HTML5, haciendo uso de Bulma y Web.py, muestra los archivos insertados en list.html
'''
import web # IMPORTACCION DE WEB.

import mvc.models.model as model

model_alumnos = model.Alumnos()

render = web.template.render("mvc/views/alumnos/")

class Modificar():
    
    def GET(self, id_alumno):
        try:
            result = model_alumnos.view(id_alumno)[0]
        #    print(result)
            return render.modificar(result) # RETORNAMOS EL REDERIZADO.
        except Exception as e:
            return "Error " + str(e.args) # EN CASO DE ERRORES, LOS DEVOLVERA.

    def POST(self, id_alumno):
        try:
            form = web.input()
            id_alumno = form.id_alumno  
            print(id_alumno)
            matricula = form.matricula
            nombre = form.nombre
            primer_apellido = form.primer_apellido
            segundo_apellido = form.segundo_apellido
            edad = form.edad
            fecha_nacimiento = form.fecha_nacimiento
            sexo = form.sexo
            estado = form.estado
            result = model_alumnos.modificar(id_alumno, matricula, nombre, primer_apellido, segundo_apellido, edad, fecha_nacimiento, sexo, estado)
            print(result)
            web.seeother('/list')

        except Exception as e:
            print(e)
            return "Error"