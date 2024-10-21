from flask import Flask, render_template, request

app = Flask(__name__)

# Página de inicio
@app.route('/')
def index():
    return render_template('index.html')

# Página Quiénes Somos
@app.route('/quienes_somos')
def quienes_somos():
    return render_template('quienes_somos.html')

# Página de Servicios
@app.route('/servicios')
def servicios():
    return render_template('servicios.html')

# Página de Noticias
@app.route('/noticias')
def noticias():
    return render_template('noticias.html')

# Página de Contacto
@app.route('/contacto', methods=['GET', 'POST'])
def contacto():
    if request.method == 'POST':
        nombre = request.form['nombre']
        correo = request.form['correo']
        mensaje = request.form['mensaje']
        return f"Mensaje recibido de {nombre}. ¡Gracias por contactarnos!"
    return render_template('contacto.html')

if __name__ == '__main__':
    app.run(debug=True)