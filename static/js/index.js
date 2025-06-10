var interv = 3
var interval_id = setInterval(connecting, interv * 1000);

function new_interval() {
    if (Number(document.getElementById("chastot").value) >= 3) {
        clearInterval(interval_id)
        interv = Number(document.getElementById("chastot").value)
        interval_id = setInterval(connecting, interv * 1000);
    }
    else {
        alert("значение не меньше 3")
    }
}



function connecting() {
    if (document.getElementById("get_data").checked) {
        connect_robot_1()
        connect_robot_2()
        connect_camera()
        draw_chart()
    }
    traffic_lights_set_data()
    remote_terminal_set_data()

}

function connect_robot_1() {
    $.ajax({
        type: 'GET',
        url: "robot_gripper_get_data",
        dataType: 'json',
        contentType: 'application/json',
        data: {

        },

        success: function (response) {

            document.getElementById("t1_1").value = response['t1'],
                document.getElementById("t2_1").value = response['t2'],
                document.getElementById("t3_1").value = response['t3'],
                document.getElementById("t4_1").value = response['t4'],
                document.getElementById("t5_1").value = response['t5'],
                document.getElementById("t6_1").value = response['t6'],
                document.getElementById("l1_1").value = response['l1'],
                document.getElementById("l2_1").value = response['l2'],
                document.getElementById("l3_1").value = response['l3'],
                document.getElementById("l4_1").value = response['l4'],
                document.getElementById("l5_1").value = response['l5'],
                document.getElementById("l6_1").value = response['l6'],
                document.getElementById("m1_1").value = response['m1'],
                document.getElementById("m2_1").value = response['m2'],
                document.getElementById("m3_1").value = response['m3'],
                document.getElementById("m4_1").value = response['m4'],
                document.getElementById("m5_1").value = response['m5'],
                document.getElementById("m6_1").value = response['m6'],
                document.getElementById("s_1").value = response['s'],
                document.getElementById("c_1").value = response['c'],
                document.getElementById("n_1").value = response['n'],

                document.getElementById("m1_1_prev").value = response['m1'] * 360 / 1024,
                document.getElementById("m2_1_prev").value = response['m2'] * 360 / 1024,
                document.getElementById("m3_1_prev").value = response['m3'] * 360 / 1024,
                document.getElementById("m4_1_prev").value = response['m4'] * 360 / 1024,
                document.getElementById("m5_1_prev").value = response['m5'] * 360 / 1024,
                document.getElementById("m6_1_prev").value = response['m6'] * 360 / 1024,
                vse_usloviya("_1")
        }

    });
}

function connect_robot_2() {
    $.ajax({
        type: 'GET',
        url: "robot_vacuum_get_data",
        dataType: 'json',
        contentType: 'application/json',
        data: {

        },

        success: function (response) {

            document.getElementById("t1_2").value = response['t1'],
                document.getElementById("t2_2").value = response['t2'],
                document.getElementById("t3_2").value = response['t3'],
                document.getElementById("t4_2").value = response['t4'],
                document.getElementById("t5_2").value = response['t5'],
                document.getElementById("t6_2").value = response['t6'],
                document.getElementById("l1_2").value = response['l1'],
                document.getElementById("l2_2").value = response['l2'],
                document.getElementById("l3_2").value = response['l3'],
                document.getElementById("l4_2").value = response['l4'],
                document.getElementById("l5_2").value = response['l5'],
                document.getElementById("l6_2").value = response['l6'],
                document.getElementById("m1_2").value = response['m1'],
                document.getElementById("m2_2").value = response['m2'],
                document.getElementById("m3_2").value = response['m3'],
                document.getElementById("m4_2").value = response['m4'],
                document.getElementById("m5_2").value = response['m5'],
                document.getElementById("m6_2").value = response['m6'],
                document.getElementById("s_2").value = response['s'],
                document.getElementById("c_2").value = response['c'],
                document.getElementById("n_2").value = response['n'],

                document.getElementById("m1_2_prev").value = response['m1'] * 360 / 1024,
                document.getElementById("m2_2_prev").value = response['m2'] * 360 / 1024,
                document.getElementById("m3_2_prev").value = response['m3'] * 360 / 1024,
                document.getElementById("m4_2_prev").value = response['m4'] * 360 / 1024,
                document.getElementById("m5_2_prev").value = response['m5'] * 360 / 1024,
                document.getElementById("m6_2_prev").value = response['m6'] * 360 / 1024,
                vse_usloviya("_2")
        }

    });
}

function vse_usloviya(num) {
    document.getElementById("dopysk").style.display = 'none'
    document.getElementById("critikal").style.display = 'none'

    let tn = ['t1', 't2', 't3', 't4', 't5', 't6']
    let ln = ['l1', 'l2', 'l3', 'l4', 'l5', 'l6']
    let mn = ['m1', 'm2', 'm3', 'm4', 'm5', 'm6']

    for (let i = 0; i < 6; i++) {
        if (Number(document.getElementById(tn[i] + num).value) < Number(document.getElementById('td_1').value) || Number(document.getElementById(tn[i] + num).value) > Number(document.getElementById('td_2').value)) {
            document.getElementById("dopysk").style.display = 'block'
        }
        if (Number(document.getElementById(ln[i] + num).value) < Number(document.getElementById('ld_1').value) || Number(document.getElementById(ln[i] + num).value) > Number(document.getElementById('ld_2').value)) {
            document.getElementById("dopysk").style.display = 'block'
        }
        if (Number(document.getElementById(mn[i] + num).value) < Number(document.getElementById('md_1').value) || Number(document.getElementById(mn[i] + num).value) > Number(document.getElementById('md_2').value)) {
            document.getElementById("dopysk").style.display = 'block'
        }
        if (Number(document.getElementById(tn[i] + num).value) < Number(document.getElementById('tk_1').value) || Number(document.getElementById(tn[i] + num).value) > Number(document.getElementById('tk_2').value)) {
            document.getElementById("critikal").style.display = 'block'
        }
        if (Number(document.getElementById(ln[i] + num).value) < Number(document.getElementById('lk_1').value) || Number(document.getElementById(ln[i] + num).value) > Number(document.getElementById('lk_2').value)) {
            document.getElementById("critikal").style.display = 'block'
        }
        if (Number(document.getElementById(mn[i] + num).value) < Number(document.getElementById('mk_1').value) || Number(document.getElementById(mn[i] + num).value) > Number(document.getElementById('mk_2').value)) {
            document.getElementById("critikal").style.display = 'block'
        }

    }
}

function connect_camera() {
    $.ajax({
        type: 'GET',
        url: "smart_camera_get_data",
        dataType: 'json',
        contentType: 'application/json',
        data: {

        },

        success: function (response) {

            document.getElementById("SmartCamera").value = response['code']

        }

    });
}

function traffic_lights_set_data() {
    $.ajax({
        type: 'GET',
        url: "traffic_lights_set_data",
        dataType: 'json',
        contentType: 'application/json',
        data: {
            "L1": Number(document.getElementById("k1_1").checked),
            "L2": Number(document.getElementById("k2_1").checked),
            "L3": Number(document.getElementById("k3_1").checked),
            "L4": Number(document.getElementById("k4_1").checked)

        },

        success: function (response) { }

    });
}

function remote_terminal_set_data() {
    $.ajax({
        type: 'GET',
        url: "remote_terminal_set_data",
        dataType: 'json',
        contentType: 'application/json',
        data: {
            "L1": Number(document.getElementById("k1_2").checked),
            "L2": Number(document.getElementById("k2_2").checked),
            "L3": Number(document.getElementById("k3_2").checked),
            "L4": Number(document.getElementById("k4_2").checked)

        },

        success: function (response) { }

    });
}

function robot_gripper_set_data() {
    $.ajax({
        type: 'GET',
        url: "robot_gripper_set_data",
        dataType: 'json',
        contentType: 'application/json',
        data: {
            "N": document.getElementById("N_control_1").value,
            "X": document.getElementById("X_1").value,
            "Y": document.getElementById("Y_1").value,
            "T": document.getElementById("T_1").value,
            "G": document.getElementById("G_1").value

        },

        success: function (response) { console.log(response) }

    });
}

function robot_vacuum_set_data() {
    $.ajax({
        type: 'GET',
        url: "robot_vacuum_set_data",
        dataType: 'json',
        contentType: 'application/json',
        data: {
            "N": document.getElementById("N_control_2").value,
            "X": document.getElementById("X_2").value,
            "Y": document.getElementById("Y_2").value,
            "V": document.getElementById("V_2").value


        },

        success: function (response) { console.log(response) }

    });
}

function save_data_change() {
    $.ajax({
        type: 'GET',
        url: "change_is_logger",
        dataType: 'json',
        contentType: 'application/json',
        data: {
            "F": Boolean(document.getElementById("save_data").checked)



        },

        success: function (response) { console.log(response) }

    });
}
let f=false;
let ch;


function draw_chart() {
    let time = []
    let temp = []
    $.ajax({
        type: 'GET',
        url: "get_chart",
        dataType: 'json',
        contentType: 'application/json',
        data: {

        },

        success: function (response) {

            if(f){
                ch.data.labels=response['time'];
                ch.data.datasets[0].data=response['temp'];
                ch.update();
            }else{
             f=true
             ch = new Chart(
                document.querySelector('.chart'), {
                type: 'line',
                data: {
                    labels: response['time'],
                    datasets: [{
                        borderColor: 'red',
                        label: 'Temperature',
                        data: response['temp'],
                        cubicInterpolationMode: 'monotone'
                    }]
                },
                options: {}
            }
            );

            }

        }

    });
    //alert(resp)




}