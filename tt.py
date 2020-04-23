from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '''<!DOCTYPE HTML><html>
    <head>
        <title>Flaskapp</title>
    </head>
    <body>
        <h1>Hello Flask!</h1>
    </body>
    </html>'''

@app.route('/about')
def about():
    return "ABOUT"

if __name__ == '__main__':
    app.run(host = '0.0.0.0')