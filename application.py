from flask_app import app
from flask_app.controllers import dojo_controller, ninja_controller

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
 