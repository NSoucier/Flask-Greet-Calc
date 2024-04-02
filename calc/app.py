# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div
app = Flask(__name__)

@app.route('/add')
def addAB():
    """Add a and b."""
    a = int(request.args['a'])
    b = int(request.args['b'])
    return str(add(a,b))

@app.route('/sub')
def subAB():
    """Substract b from a."""
    a = int(request.args['a'])
    b = int(request.args['b']) 
    return str(sub(a,b))

@app.route('/mult')
def multAB():
    """Multiply a and b."""
    a = int(request.args['a'])
    b = int(request.args['b']) 
    return str(mult(a,b))

@app.route('/div')
def divAB():
    """Divide a by b."""
    a = int(request.args['a'])
    b = int(request.args['b'])
    return str(div(a,b))

# mathDict = {'add': add, 'sub': sub, 'mult': mult, 'div': div}

# @app.route('/math/<operation>')
# def math(operation):
#     """Performs math operations on a and b."""
#     a = int(request.args['a'])
#     b = int(request.args['b'])
#     return str(mathDict[operation](a,b))

math = {'add': add, 'sub': sub, 'mult': mult, 'div': div,}

@app.route('/math/<operation>')
def mathOperations(operation):
    """Do math on a and b."""
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = math[operation](a, b)

    return str(result)