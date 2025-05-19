from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Good Day!</h1>'

if __name__ == '__main__':
    app.run(debug=True)
