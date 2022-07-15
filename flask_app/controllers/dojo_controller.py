from flask_app import app
from flask_app.models.dojo_model import Dojo
from flask import render_template, redirect, request

@app.route('/dojos')
def allDojos():
    return render_template('dojos.html', dojos=Dojo.showAll())

@app.route('/dojos/<int:id>')
def viewDojo(id):
    dojos_and_ninjas = Dojo.showDojo(id, add_ninjas=True)
    if dojos_and_ninjas is None:
        dojos_and_ninjas = Dojo.showDojo(id, add_ninjas=False)
    return render_template('dojoPage.html', dojo=dojos_and_ninjas[0], ninjas=dojos_and_ninjas[1])

@app.route('/dojos/add', methods= ['POST'])
def addDojo():
    rslt = Dojo.addNewDojo(request.form)
    return redirect('/dojos')