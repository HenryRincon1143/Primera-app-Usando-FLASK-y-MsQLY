# con flask enviamos msj #pip install Flask
from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_mysqldb import MySQL, MySQLdb  # pip install Flask-MySQLdb
from os import path  # pip install notify-py
from notifypy import Notify
import MySQLdb.cursors

app = Flask(__name__)

# connexion a la base de datos
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'hjas_data'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
# este comando es importante para extablecer conexion con la base de datos
mysql = MySQL(app)

# esta es una session para los msj que se envia por servidor flask "importante."
app.secret_key = 'mysecretkey'


# name se utiliza si queremos expecifiar un nombre que acompañe la url que samos para desplegara el server
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/desboard")
def desboard():
    return render_template('desboard.html')

@app.route("/crud_trabajadores")
def crud_trabajadores():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM trabajadores')
    data = cur.fetchall()
    return render_template('crud_trabajadores.html', trabajadores = data)

@app.route("/crud_productos")
def crud_productos():
    return render_template('crud_productos.html')

# llamamos el formulario login y validamos los roles de cada usuario que intente ingresar.

@app.route("/login", methods=['GET', 'POST'])
def login():

    # con este codigo activamos los msj de notificaciones "importante"
    notificacion = Notify()

    if request.method == 'POST':
        usuario = request.form['usuario']
        clave = request.form['clave']

        cur = mysql.connection.cursor()
        # importante no borrar la coma que acompaña a usuario.
        cur.execute('SELECT * FROM trabajadores WHERE usuario = %s', (usuario,))
        user = cur.fetchone()
        cur.close()

        if len(user) > 0:
            if clave == user['clave']:
                session['usuario'] = user['usuario']
                session['clave'] = user['clave']
                session['tipo'] = user['id_cargos']

                if session['tipo'] == 1:  # validamos los usuarios y se determina que rol tienen
                    notificacion.title = "Bienvenido Super Administrador"
                    notificacion.message = "puede trabajar a su gusto."
                    notificacion.send()
                    return render_template('desboard.html')

                elif session['tipo'] == 2:  # validamos los usuarios y se determina que rol tienen
                    notificacion.title = "Bienvenido Administrador."
                    notificacion.message = "puede trabajar a su gusto."
                    notificacion.send()
                    # estoy redirigiendo al mismo formulario que el super admin, se debe cambiar
                    return render_template('f_registro_trabajadores.html')

                elif session['tipo'] == 3:  # validamos los usuarios y se determina que rol tienen
                    notificacion.title = "Bienvenido apreciado cliente."
                    notificacion.message = "puede seguir disfrutando de nuestro contenido."
                    notificacion.send()
                    return render_template('index.html')
                else:
                    notificacion.tittle = "Error de Acceso"
                    notificacion.message = "Correo o contraseña no valida"
                    notificacion.send()
                    return redirect(url_for('login'))
            else:
                notificacion.title = "Error de Acceso"
                notificacion.message = "No existe el usuario"
                notificacion.send()
                return redirect(url_for('login'))
        else:
            notificacion.title = "Error de Acceso"
            notificacion.message = "No existe el usuario"
            notificacion.send()
            return redirect(url_for('login'))
    else:
        #flash('Imposible Ingresar, Contacta a soporte Tecnico.')
        return render_template('login.html')

@app.route("/recuperar_clave")
def recuperar_clave():
    return render_template('recuperar_clave.html')

# con esta funcion tomamos los datos que estan en el formulario y los trabajamos con la intencion de registrarlos en la bd trabajadores

@app.route("/f_clientes")
def f_clientes():
    return render_template('f_registro_trabajadores.html')

@app.route("/add_registro_usuario", methods=['GET', 'POST'])
def add_registro_usuario():

    notificacion = Notify()

    if request.method == 'GET':
        return render_template('f_registro_trabajadores.html')

    else:
        nombres = request.form['nombres']
        apellidos = request.form['apellidos']
        op = request.form['op']
        documento = request.form['documento']
        celular = request.form['celular']
        correo = request.form['correo']
        usuario = request.form['usuario']
        clave = request.form['clave']
        tip = request.form['tipo']

        # insertamos datos en la base de datos clientes.
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO trabajadores (nombres, apellidos, op, documento, celular, correo, usuario, clave, id_cargos) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)',
                    (nombres, apellidos, op, documento, celular, correo, usuario, clave, tip))
        mysql.connection.commit()
        notificacion.title = "Registro Exitoso"
        notificacion.message = "Datos guardados de forma correcta"
        notificacion.send()
        # flash('Datos agregados correctamente.') con flash podemos enviar msj entre las pestañas.
        return redirect(url_for('login'))
        # hasta aqui va el codigo del registro de datos

@app.route("/add_registro_cliente", methods=['GET', 'POST'])
def add_registro_cliente():

    notificacion = Notify()

    if request.method == 'GET':
        return render_template('f_registro_clientes.html')

    else:
        nombres = request.form['nombres']
        apellidos = request.form['apellidos']
        op = request.form['op']
        documento = request.form['documento']
        celular = request.form['celular']
        correo = request.form['correo']
        usuario = request.form['usuario']
        clave = request.form['clave']
        tip = request.form['tipo']

        # insertamos datos en la base de datos clientes.
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO trabajadores (nombres, apellidos, op, documento, celular, correo, usuario, clave, id_cargos) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)',
                    (nombres, apellidos, op, documento, celular, correo, usuario, clave, tip))
        mysql.connection.commit()
        notificacion.title = "Registro Exitoso"
        notificacion.message = "Datos guardados de forma correcta"
        notificacion.send()
        # flash('Datos agregados correctamente.') con flash podemos enviar msj entre las pestañas.
        return redirect(url_for('index'))
        # hasta aqui va el codigo del registro de datos

@app.route("/carrito_compra")
def carrito_compra():
    return render_template('carrito_compra.html')

# asi hacemos con todos lo demas si queremos llamarlos .


if __name__ == '__main__':  # Este codigo es para que nuesta aplicacion corra de forma automatica y detecte los cambios
    app.run(debug=True)
