#Importamos flask
from flask import Flask, render_template

#Inicializamos la aplicación 
app = Flask(__name__, template_folder="templates")

#Definimos la ruta principal 
@app.route("/")
def index(): #Definimos la función 
    return render_template('index.html')#Obtenemos la ruta de la pagina index.html

#Definimos la ruta para la subpagina acerca de nosotros 
@app.route("/acerca")
def acerca():
    return render_template('acerca.html')

#Definimos la ruta para la pag servicios 
@app.route("/servicios")
def servicios():
    return render_template('servicios.html')

#Definimos la ruta para la subpagina de tematica para redes sociales 
@app.route("/temas")
def temas():
    return render_template('tematica.html')

#Definimos la ruta para la subpagina de anuncios publicitarios 
@app.route("/anuncios")
def anuncios():
    return render_template('anuncios.html')

#Definimos la ruta para la subpagina de anuncios publicitarios 
@app.route("/contProv")
def contProveedor():
    return render_template('contac-prove.html')



#Definimos la ruta para registrarse 
@app.route("/registro")
def  registro():
    return render_template('registrar.html')

#Definimos la ruta para iniciar sesión 
@app.route("/iniciar")
def  iniciar():
    return render_template('registrar.html')

 #Definimos la ruta para la subpagina quienes somos        
@app.route("/quienes")
def quienesSomos():
    return render_template('quienes-somos.html')

#Definimos la ruta para la subpagina de contactanos
@app.route("/contactanos")
def contactanos():
    return render_template('contactanos.html')

#Definimos la ruta para la subpagina de contactos 
@app.route("/contacto")
def contacto():
    return render_template('contacto.html')

#Definimos la ruta para la sibpagina de politica de privacidad 
@app.route("/politica")
def politica():
    return render_template('politica.html')

#Creamos en main para que la app se pueda ejecutar 
if __name__ == '__main__':
    app.run(debug=True)
