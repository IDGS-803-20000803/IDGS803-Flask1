from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/operasBa", methods=["GET","POST"])
def operasBa():

    if request.method == "POST":
        
        num1 = request.form.get("num1")
        num2 = request.form.get("num2")

        eleccion = request.form.get("op")
        if eleccion == "1":
            return "La suma es: {}".format(str(int(num1)+int(num2)))
        elif eleccion == "2":
            return "La resta es: {}".format(str(int(num1)-int(num2)))
        elif eleccion == "3":
            return "La multiplicacion es: {}".format(str(int(num1)*int(num2)))
        elif eleccion == "4":
            return "La division es: {}".format(str(int(num1)/int(num2)))
    else:
        return '''
        <form action = "/operasBa" method= "POST"
        <label>N1:</label>
        <input type = "text" name = "num1"/><br><br>
        <label>N2:</label>
        <input type = "text" name = "num2"/><br><br>
        
        <label>Suma:</label>
        <input type = "radio" value = "1" name = "op"/> 
         <label>Resta:</label>
        <input type = "radio" value = "2" name = "op"/> 
         <label>Multiplicar:</label>
        <input type = "radio" value = "3" name = "op"/> 
         <label>Dividir:</label>
        <input type = "radio" value = "4" name = "op"/><br><br> 

        <input type = "submit" value = "calcular"/>
        </form>
    '''
if __name__=="__main__":
    app.run(debug=True)