import json
import time
from time import sleep

import logger
import threading

from flask import Flask, render_template, request

import things
from things import *




app = Flask(__name__)

gripper=things.Gripper()
vacuum=things.Vacuum()
light=things.Light()
terminal=things.Terminal()
camera=things.Camera()
logger=logger.Log()

def log_all():
    while True:
        if logger.is_logging:
            logger.log_data(gripper.get_data(), 'gripper_data')
            logger.log_data(vacuum.get_data(), 'vacuum_data')
            logger.log_data(camera.get_data(), 'camera_data')
            print("залогировано")
            logger.get_chart()
        time.sleep(5)

thread = threading.Thread(target=log_all)
thread.daemon=True
thread.start()

@app.route('/')
def hello_world():  # put application's codeй here
    return render_template('emulator.html')

@app.route('/o')
def o():  # put application's codeй here
    return render_template('operator.html')

@app.route('/e')
def e():  # put application's codeй here
    return render_template('engeneer.html')


@app.route('/change_is_logger')
def c_i_l():
    if(request.args.get('F','')=='true'):
        logger.is_logging=True
    else:
        logger.is_logging=False
    return json.dumps({'response': 0})
@app.route('/get_chart')
def g_c():

    return logger.get_chart()


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




if __name__ == '__main__':
    app.run()
