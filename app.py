# Importamos flask, render_template, request y url_for
from flask import Flask, redirect, render_template, request, url_for

# Inicializamos la aplicación y la carpeta template
app = Flask(__name__, template_folder="templates")
app.config['SECRET_KEY'] = '7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe'

# Definimos el decorador principal


@app.route("/")
def index():  # Creamos la función
    # Los parámetros page y list los podríamos utilizar para paginar el listado
    page = request.args.get('page', 1)  # estamos pidiendo la primera página
    list = request.args.get('list', 10)  # Los primeros diez post
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

# ****************************************************************************************************************************+


@app.route("/temas")
def temas():

  # Redirección a la pagina tematica.html
    return render_template('tematica.html', temasRedes=temasRedes)


# creamos un array para los datos ingresados en la pag temática
temasRedes = []

# Definimos el decorador para la pag de tematica para redes sociales


@app.route("/temasR", methods=['POST'])
def temasR():  # Creamos la función temas
    data = request.form
    with open('resultado.txt', 'w') as archivo:
        archivo.write(str(data))
    print(data)
    # utilizamos el método post
    if request.method == 'POST':
        # Extraemos los datos ingresados en el input de la descripcion de contactar proveedores
        redS = request.form['redS']
        sectAgro = request.form['sectAgro']
        mensaje = request.form['mensaje']
        # Creamos la condición para que no guarde el registro cuando los campos estén vacíos
        if redS == '' or sectAgro == '' or mensaje == '':
            return redirect(url_for('temas'))
        else:
            # Agrega a la lista los campos llenos
            temasRedes.append(
                {'redS': redS, 'sectAgro': sectAgro, 'mensaje': mensaje})
            # redireccion a la funcion  temas
            return redirect(url_for('temas'))

# Creamos el decorador para borrar contenido de la tabla de temática de redes sociales


@app.route('/borrar1', methods=['POST'])
def borrar1():  # cramos la función borrar
    if request.method == 'POST':  # usamos el metodo Post
        if temasRedes == []:  # array temasRedes
            # redireccion a la funcion  temas
            return redirect(url_for('temas'))
        else:
            temasRedes.clear()  # limpiar lista de usuario
            # redireccion a la funcion  temas
            return redirect(url_for('temas'))


# ***************************************************************************


# Definimos el decorador para la pag de anuncios publicitarios
@app.route("/anuncios")
def anuncios():  # Creamos la función anuncios
    # Redirección a la pagina anuncios.html
    return render_template('anuncios.html')

#############################################################################
# Definimos el decorador para la pag contactar proveedores


@app.route("/contProv")
def contProveedor():  # Creamos la función def contProveedor():

    # Redirección a la pagina contac-prove.html y el array listaUsuario
    return render_template('contac-prove.html', listaUsuario=listaUsuario)


# Creamos un array lista Usuario
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


@app.route("/registro/", methods=["GET", "POST"])
def registro():  # creamos la función registro
    data = request.form
    with open('resultado.txt', 'w') as archivo:
        archivo.write(str(data))
    print(data)
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        clave = request.form['clave']
        if name == '' or email == '' or clave == '':
            return redirect(url_for('registro'))
        else:
            return redirect(url_for('index'))

    # Renderiza a la pag registrar.html
    return render_template('registrar.html')


# ***************************************************************************************************************************************
# Definimos el decorador para iniciar sesión


@app.route("/login/", methods=["GET", "POST"])
def login():  # creamos la función login
    data = request.form
    with open('resultado.txt', 'w') as archivo:
        archivo.write(str(data))
    print(data)
    if request.method == 'POST':
        email = request.form['email']
        clave = request.form['clave']
        if email == '' or clave == '':
            return redirect(url_for('login'))
        else:
            return redirect(url_for('temas'))

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
