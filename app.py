
from flask import Flask, render_template



app = Flask(__name__)



@app.route("/")
def inicio():
   
    return render_template("index.html")



@app.route("/HOLA")
def hola():
    
    return render_template("HOLA.html")

@app.route("/ADIOS")
def adios():
    
    return render_template("ADIOS.html")






@app.route("/LOVE")
def love():
    
    return render_template("LOVE.html")




if __name__ == "__main__":
    
    app.run(debug=True)
