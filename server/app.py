#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_route(parameter):
    print(parameter)
    return f'{parameter}'

@app.route('/count/<int:parameter>')
def count_route(parameter):
    count  = ''
    for x in range(int(parameter)):
        count += f'{str(x)}\n'
    return count
@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    num1, num2 = int(num1), int(num2)
    if operation == '+':
        x = num1 + num2
    elif operation == '-':
        x = num1 - num2
    elif operation == '*':
        x = num1 * num2
    elif operation == 'div':
        x = num1 / num2
    elif operation == '%':
        x = num1 % num2
    return str(x)
    
if __name__ == '__main__':
    app.run(port=5555, debug=True)
