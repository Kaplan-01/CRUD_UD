''' 
NOMBRE: Maria del Carmen Hernandez Diaz
ACCOUNT: 1718110389
GROUP: TIC 51
DATE: 09-08-2020
DESCRIPTION: Update and delete objetive
'''
import web # IMPORTACCION DE WEB.

render = web.template.render("mvc/views/alumnos/")

class Profile():
    
    def GET(self):
        try:
            return render.profile() # RETORNAMOS EL REDERIZADO.
        except Exception as e:
            return "Error " + str(e.args) # EN CASO DE ERRORES, LOS DEVOLVERA.
