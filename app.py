from flask import Flask, jsonify
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import HTTPException
from werkzeug.exceptions import BadRequest

from werkzeug.exceptions import default_exceptions
import settings

app = Flask(__name__)


@app.errorhandler(Exception)
def handle_error(e):
    #import pdb;pdb.set_trace()
    code = 500
    if isinstance(e, BadRequest):
        code = e.code
    if isinstance(e, HTTPException):
        code = e.code
    return jsonify(error=str(e)), code

for ex in default_exceptions:
    app.register_error_handler(ex, handle_error)



app.config['SQLALCHEMY_DATABASE_URI'] = settings.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = settings.SQLALCHEMY_TRACK_MODIFICATIONS
app.config['BUNDLE_ERRORS'] = settings.BUNDLE_ERRORS

db = SQLAlchemy(app)
# this import must be after db (cyclic imports)
#from endpoints.cure.resource import errors as CureErrors
api = Api(app)#,errors=CureErrors)
api.prefix = '/api'

from endpoints.users.resource import UsersResource
from endpoints.todos.resource import TodosResource
from endpoints.cure.resource import CuredbResource


api.add_resource(UsersResource, '/users', '/users/<int:user_id>')
api.add_resource(TodosResource, '/todos', '/todos/<int:todo_id>')
api.add_resource(CuredbResource, '/cures', '/cures/<int:cure_id>')

if __name__ == '__main__':
    app.run()
