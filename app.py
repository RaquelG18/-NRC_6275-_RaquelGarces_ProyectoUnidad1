# Importamos flask, render_template, request y url_for
from flask import Flask, redirect, render_template, request, url_for

# Inicializamos la aplicación y la carpeta template
app = Flask(__name__, template_folder="templates")

# Definimos el decorador principal

@app.route("/")
def index():  # Creamos la función
    # Redirección a la pagina index.html
    return render_template('index.html')

# Definimos el decorador para la subpagina acerca de nosotros

@app.route("/acerca")
def acerca():  # Creamos la función acerca
    # Redirección a la pagina acerca.html
    return render_template('acerca.html')

# Definimos el decorador para la pag servicios


@app.route("/servicios")
def servicios():  # Creamos la función servicios
    # Redirección a la pagina servicios.html
    return render_template('servicios.html')

# Definimos el decorador para la pag de tematica para redes sociales


@app.route("/temas")
def temas():  # Creamos la función temas
    # Redirección a la pagina tematica.html
    return render_template('tematica.html')

# Definimos el decorador para la pag de anuncios publicitarios


@app.route("/anuncios")
def anuncios():  # Creamos la función anuncios
    # Redirección a la pagina anuncios.html
    return render_template('anuncios.html')

###########################################################################################################################################################
# Definimos el decorador para la pag contactar proveedores


@app.route("/contProv")
def contProveedor():  # Creamos la función def contProveedor(): #Creamos la función anuncios

    # Redirección a la pagina contac-prove.html y el array listaUsuario
    return render_template('contac-prove.html', listaUsuario=listaUsuario)


# Creamos un array lista Usuario para la peticion del cliente en la pag contactar proveedor
listaUsuario = []

# Controlador del decorador de envio de datos


@app.route('/enviar', methods=['POST'])
# creamos la función enviar
def enviar():
    # utilizamos el método post
    if request.method == 'POST':
        # Extraemos los datos ingresados en el input de la descripcion de contactar proveedores
        nombre_empresa = request.form['nombre_empresa']
        correoElect = request.form['correoElect']
        mensaje = request.form['mensaje']
        # Creamos la condición para que no guarde el registro cuando los campos estén vacíos
        if nombre_empresa == '' or correoElect == '' or mensaje == '':
            return redirect(url_for('contProveedor'))
        else:
            # Agrega a la lista los campos llenos
            listaUsuario.append(
                {'nombre_empresa': nombre_empresa, 'correoElect': correoElect, 'mensaje': mensaje})
            # redireccion a la funcion  contProveedor
            return redirect(url_for('contProveedor'))

# Controlador del decorador para borrar los datos de la tabla


@app.route('/borrar', methods=['POST'])
def borrar():  # cramos la función borrar
    if request.method == 'POST':  # usamos el metodo Post
        if listaUsuario == []:  # array listaUsuario
            # redireccion a la funcion  contProveedor
            return redirect(url_for('contProveedor'))
        else:
            listaUsuario.clear()  # limpiar lista de usuario
            # redireccion a la funcion  contProveedor
            return redirect(url_for('contProveedor'))

#################################################################################################################################################################

# Definimos el decorador para registrarse


@app.route("/registro")
def registro():  # creamos la función registro
    # Renderiza a la pag registrar.html
    return render_template('registrar.html')

# Definimos el decorador para iniciar sesión


@app.route("/login")
def login():  # creamos la función login
    return render_template('login.html')  # Renderiza a la pag login.html

 # Definimos el decorador para la subpagina quienes somos


@app.route("/quienes")
def quienesSomos():  # creamos la función quienesSomos
    # Renderiza a la pag quienes-somos.html
    return render_template('quienes-somos.html')

# Definimos el decorador para la subpagina de contactanos


@app.route("/contactanos")
def contactanos():  # creamos la función contactanos
    # Renderiza a la pag contactanos.html
    return render_template('contactanos.html')

# Definimos el decorador para la subpagina de contactos


@app.route("/contacto")
def contacto():  # creamos la función contacto
    return render_template('contacto.html')  # Renderiza a la pag contacto.html

# Definimos el decorador para la sibpagina de politica de privacidad


@app.route("/politica")
def politica():  # creamos la función politica
    return render_template('politica.html')  # Renderiza a la pag politica.html


# Creamos el main para que la app se pueda ejecutar
if __name__ == '__main__':
    app.run(debug=True)
