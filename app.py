import json
import threading
import time

from flask import Flask, render_template, request

import logger
import things

app = Flask(__name__)
gripper=things.Gripper()
vacuum=things.Vacuum()
light=things.Light()
camera=things.Camera()
terminal=things.Terminal()
loger=logger.Log()


def log_data():
    while True:
        if loger.is_logging:
            loger.log_data(gripper.get_data(), 'gripper_data')
            loger.log_data(vacuum.get_data(), 'vacuum_data')
            loger.log_data(camera.get_data(), 'camera_data')
        time.sleep(5)


thread = threading.Thread(target=log_data)
thread.daemon=True
thread.start()

@app.route('/change_is_logger')
def c_i_l():
    if(request.args.get('F','')=='true'):
        loger.is_logging=True
    else:
        loger.is_logging=False
    return json.dumps({'response': 0})
@app.route('/get_chart')
def g_c():

    return loger.get_chart()


@app.route('/robot_gripper_connect')
def r_g_c():
    return (gripper.connect(request))

@app.route('/robot_vacuum_connect')
def r_v_c():
    return vacuum.connect(request)

@app.route('/traffic_lights_connect')
def t_l_c():
    return light.connect()

@app.route('/remote_terminal_connect')
def r_t_c():
    return terminal.connect(request)


@app.route('/smart_camera_connect')
def s_c_c():
    return camera.connect(request)

@app.route('/robot_gripper_set_data')
def r_g_s_d():
    return gripper.set_data(request)

@app.route('/robot_vacuum_set_data')
def r_v_s_d():
    return vacuum.set_data(request)

@app.route('/traffic_lights_set_data')
def l_s_d():
    return light.set_data(request)

@app.route('/remote_terminal_set_data')
def t_s_d():
    return terminal.set_data(request)

@app.route('/robot_gripper_get_data')
def r_g_g_d():
    return json.dumps(gripper.get_data())

@app.route('/robot_vacuum_get_data')
def r_v_g_d():
    return json.dumps(vacuum.get_data())

@app.route('/smart_camera_get_data')
def s_c_g_d():
    return json.dumps(camera.get_data())











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
