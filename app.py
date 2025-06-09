from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('emulator.html')

@app.route('/e')
def e():
    return render_template('engeneer.html')

@app.route('/o')
def o():
    return render_template('operator.html')


if __name__ == '__main__':
    app.run()
