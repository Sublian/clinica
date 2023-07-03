from flask import Flask, request, url_for, render_template, redirect
import helper

app=Flask(__name__)

#aca empezamos
@app.route("/")
@app.route("/index")
def index():    
    return render_template("index.html")   

#ruta para acerca
@app.route("/acerca")
def acerca():    
    return render_template("acerca.html")   

#ruta para login
@app.route("/login")
def login():    
    return render_template("login.html")   

#ruta para contacto
@app.route("/contacto")
def contacto():    
    return render_template("contacto.html")  

 

if __name__=='__main__':
    app.run(debug=True)