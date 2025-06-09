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
    return light.connect()

@app.route('/smart_camera_connect')
def s_c_c():
    return camera.connect(request)






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
