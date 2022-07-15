from flask_app import app
from flask_app.models.dojo_model import Dojo
from flask_app.models.ninja_model import Ninja
from flask import render_template, redirect, request

@app.route('/ninjas')
def newNinja():
    return render_template('ninjas.html', dojos=Dojo.showAll())

@app.route('/ninjas/add', methods=['POST'])
def addNewNinja():
    rslt = Ninja.addNewNinja(request.form)
    return redirect(f"/dojos/{request.form['dojo_id']}")