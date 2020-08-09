''' 
NOMBRE: Maria del Carmen Hernandez Diaz
ACCOUNT: 1718110389
GROUP: TIC 51
DATE: 05-07-2020
DESCRIPTION: Uso de la arquitectura MVC. Formulario HTML5, haciendo uso de Bulma y Web.py. 
'''

import web

urls = [
    '/','mvc.controllers.alumnos.index.Index', 
    '/index/?','mvc.controllers.alumnos.index.Index',
    '/insertar/?','mvc.controllers.alumnos.insertar.Insertar',
    '/borrar/(.*)','mvc.controllers.alumnos.borrar.Borrar',
    '/view/(.*)','mvc.controllers.alumnos.view.View',
    '/modificar/(.*)','mvc.controllers.alumnos.modificar.Modificar',
    '/list/?','mvc.controllers.alumnos.list.List',
    '/profile/?','mvc.controllers.alumnos.profile.Profile',

] # COLOCAMOS LA RUTA

app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()