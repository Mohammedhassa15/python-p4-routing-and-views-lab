#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return f'<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_text(parameter):
    print(parameter)
    return parameter


@app.route('/count/<int:parameter>')
def count(parameter):
    output = ''
    for i in range(parameter):
        output += f'{i}\n'
    return output

@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math_operation(num1, operation, num2):
    if operation == '+':
        return str(num1 + num2)
    elif operation == '*':
        return str(num1 * num2)
    elif operation == 'div':
        return str(num1 / num2)
    elif operation == '-':
        return str(num1 - num2)
    elif operation == '%':
        return str(num1 % num2)
    else:
        return 'Invalid operation'



if __name__ == '__main__':
    app.run(port=5555, debug=True)
