from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    nombre = "Filemona"
    c = ['Espanol','Ingles','Quimica']
   
    return render_template("index.html", nombre = nombre, c = c)

@app.route("/usuarios")
def user():
    return render_template("archivo2.html")

if __name__ == "__main__":
    app.run(debug = True)

