from flask import Flask

app = Flask(__name__)
app.secret_key = 'l0lh@x'

DATABASE = 'dojos_and_ninjas_schema'