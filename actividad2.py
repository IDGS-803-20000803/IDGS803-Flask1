
from flask import Flask, render_template
from flask import request

app = Flask(__name__)

@app.route("/")
def cinepolis():
    return render_template("formulario-cine.html")

@app.route("/resultado", methods = ['POST'])
def resultado():
    nombre = request.form.get("txtNombre")
    cCompradores = int(request.form.get("txtCompradores"))
    tarjeta = request.form.get("respuesta")
    cBoletos = int(request.form.get("txtCantidadB"))
    vp = 12*int(cBoletos)
    span = ""
    totalBoletos = cCompradores * 7

    if totalBoletos < cBoletos:
        span = "solo puedes comprar 7 boletos por persona"
        res = ""
        nombre = ""
    else:

        if int(cBoletos) > 5:
            if tarjeta == "si":
                num1 = vp - (vp*0.15)
                res = num1 - (num1*0.10)
            else:
                res = vp - (vp*0.15)
        elif int(cBoletos) == 3 or int(cBoletos) == 4 or int(cBoletos) == 5:
            if tarjeta == "si":
                    num1= vp-(vp*0.10)
                    res = num1 -(num1*0.10)
            else:
                    res = vp-(vp*0.10)
        else:
            if tarjeta == "si":
                    res = vp - (vp*0.10)
            else:
                    res= vp
            
    return render_template("formulario-cine.html", nombre = nombre,  res = res, span = span)


if __name__ == "__main__":
    app.run(debug = True)