from flask import Flask
from flask import request
app = Flask(__name__)

@app.route("/operasBa", methods=["GET","POST"])
def operasBa():

    if request.method == "POST":
        num1 = request.form.get("num1")
        num2 = request.form.get("num2")
        return "La suma es: {}".format(str(int(num1)+int(num2)))
    else:
        return '''
        <form action = "/operasBa" method= "POST"
        <label>N1:</label>
        <input type = "text" name = "num1"/><br><br>
        <label>N2:</label>
        <input type = "text" name = "num2"/><br><br>
        <input type = "submit" value = "calcular"/>
        </form>
    '''
if __name__=="__main__":
    app.run(debug=True)