from flask import Flask, render_template, request

import things

app = Flask(__name__)
gripper=things.Gripper()
vacuum=things.Vacuum()
light=things.Light()
camera=things.Camera()
terminal=things.Terminal()


@app.route('/robot_gripper_connect')
def r_g_c():
    return gripper.connect(request)

@app.route('/robot_vacuum_connect')
def r_v_c():
    return vacuum.connect(request)

@app.route('/remote_terminal_connect')
def r_t_c():
    return terminal.connect(request)

@app.route('/traffic_lights_connect')
def t_l_c():
    return light.connect(request)



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
