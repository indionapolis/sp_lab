from flask import Flask, request, Response
from uuid import uuid1

app = Flask(__name__)

USERS = {'valeriy':hash('val1212')}


def authenticate(username, password):
    def wrap(f):
        def wrapper(*args, **kwargs):
            auth = request.authorization
            if auth:
                if auth.username != username or auth.password != password:
                    return Response(status=401)
            else:
                return Response(status=400)
            return f(*args, **kwargs)

        return wrapper

    return wrap


@app.route('/', methods=['GET'])
def hello_world(arg='doom'):
    if arg == 'doom':
        return 'Hello, bloody world!'
    return 'Hello, World!'


@app.route('/login', methods=['GET'])
def login():
    auth = request.authorization
    if auth:
        un = auth.username
        pw = auth.password
        if un in USERS.keys() and USERS[un] == hash(pw):
            return Response(headers={'uuid': str(uuid1())}, status=200)
        else:
            return Response(status=401)
    else:
        return Response(status=400)


@app.route('/secret_stuff')
@authenticate('indionapolis', 'moscow1147')
def secret_stuff():
    # do stuff
    return Response(status=200)


if __name__ == '__main__':
    app.run()
