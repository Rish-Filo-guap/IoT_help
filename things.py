import abc
import json


class Robot(abc.ABC):
    def __init__(self):
        self.t1=0
        self.t2=0
        self.t3=0
        self.t4=0
        self.t5=0
        self.t6=0
        self.l1=0
        self.l2=0
        self.l3=0
        self.l4=0
        self.l5=0
        self.l6=0
        self.m1=0
        self.m2=0
        self.m3=0
        self.m4=0
        self.m5=0
        self.m6=0

        self.s=0
        self.c=0
        self.n=0

        self.N=0
        self.X=0
        self.Y=0
class Vacuum(Robot):
    def __init__(self):
        super().__init__()
        self.V=0
    def connect(self, request):
        self.t1 = request.args.get('t1','')
        self.t2 = request.args.get('t2','')
        self.t3 = request.args.get('t3','')
        self.t4 = request.args.get('t4','')
        self.t5 = request.args.get('t5','')
        self.t6 = request.args.get('t6','')
        self.l1 = request.args.get('l1','')
        self.l2 = request.args.get('l2','')
        self.l3 = request.args.get('l3','')
        self.l4 = request.args.get('l4','')
        self.l5 = request.args.get('l5','')
        self.l6 = request.args.get('l6','')
        self.m1 = request.args.get('m1','')
        self.m2 = request.args.get('m2','')
        self.m3 = request.args.get('m3','')
        self.m4 = request.args.get('m4','')
        self.m5 = request.args.get('m5','')
        self.m6 = request.args.get('m6','')
        self.s = request.args.get('s', '')
        self.c = request.args.get('c', '')
        self.n = request.args.get('n', '')

        return json.dumps({
            'N':self.N,
            'X':self.X,
            'Y':self.Y,
            'V':self.V
        })
    def set_data(self, request):
        self.N=request.args.get('N', '')
        self.X=request.args.get('X', '')
        self.Y=request.args.get('Y', '')
        self.V=request.args.get('V', '')
        return json.dumps({'response': 0})
    def get_data(self):
        return {
            'N': self.N,
            'X': self.X,
            'Y': self.Y,
            'V': self.V,
            't1': self.t1,
            't2': self.t2,
            't3': self.t3,
            't4': self.t4,
            't5': self.t5,
            't6': self.t6,
            'l1': self.l1,
            'l2': self.l2,
            'l3': self.l3,
            'l4': self.l4,
            'l5': self.l5,
            'l6': self.l6,
            'm1': self.m1,
            'm2': self.m2,
            'm3': self.m3,
            'm4': self.m4,
            'm5': self.m5,
            'm6': self.m6,
            'n': self.n,
            's': self.s,
            'c': self.c
        }

class Gripper(Robot):
    def __init__(self):
        super().__init__()
        self.G=0
        self.T=0

    def connect(self, request):
        self.t1 = request.args.get('t1','')
        self.t2 = request.args.get('t2','')
        self.t3 = request.args.get('t3','')
        self.t4 = request.args.get('t4','')
        self.t5 = request.args.get('t5','')
        self.t6 = request.args.get('t6','')
        self.l1 = request.args.get('l1','')
        self.l2 = request.args.get('l2','')
        self.l3 = request.args.get('l3','')
        self.l4 = request.args.get('l4','')
        self.l5 = request.args.get('l5','')
        self.l6 = request.args.get('l6','')
        self.m1 = request.args.get('m1','')
        self.m2 = request.args.get('m2','')
        self.m3 = request.args.get('m3','')
        self.m4 = request.args.get('m4','')
        self.m5 = request.args.get('m5','')
        self.m6 = request.args.get('m6','')
        self.s = request.args.get('s', '')
        self.c = request.args.get('c', '')
        self.n = request.args.get('n', '')
        return json.dumps({
            'N':self.N,
            'X':self.X,
            'Y':self.Y,
            'T':self.T,
            'G':self.G
        })


    def set_data(self, request):
        self.N=request.args.get('N', '')
        self.X=request.args.get('X', '')
        self.Y=request.args.get('Y', '')
        self.T=request.args.get('T', '')
        self.G=request.args.get('G', '')
        return json.dumps({'response': 0})
    def get_data(self):
        return {
            'N': self.N,
            'X': self.X,
            'Y': self.Y,
            'T': self.T,
            'G': self.G,
            't1': self.t1,
            't2': self.t2,
            't3': self.t3,
            't4': self.t4,
            't5': self.t5,
            't6': self.t6,
            'l1': self.l1,
            'l2': self.l2,
            'l3': self.l3,
            'l4': self.l4,
            'l5': self.l5,
            'l6': self.l6,
            'm1': self.m1,
            'm2': self.m2,
            'm3': self.m3,
            'm4': self.m4,
            'm5': self.m5,
            'm6': self.m6,
            'n': self.n,
            's': self.s,
            'c': self.c

        }

class Light():
    def __init__(self):
        self.L1=0
        self.L2=0
        self.L3=0
        self.L4=0
    def connect(self):
        return json.dumps({
            'L1': self.L1,
            'L2': self.L2,
            'L3': self.L3,
            'L4': self.L4
        })
    def set_data(self, request):
        self.L1 = request.args.get('L1', '')
        self.L2 = request.args.get('L2', '')
        self.L3 = request.args.get('L3', '')
        self.L4 = request.args.get('L4', '')
        return json.dumps({'response': 0})

class Terminal():
    def __init__(self):
        self.L1=0
        self.L2=0
        self.L3=0
        self.L4=0
        self.b1=0
        self.b2=0
        self.b3=0
        self.p=0
    def connect(self, request):
        self.b1 = request.args.get('b1', '')
        self.b2 = request.args.get('b2', '')
        self.b3 = request.args.get('b3', '')
        self.p = request.args.get('p', '')
        return json.dumps({
            'L1': self.L1,
            'L2': self.L2,
            'L3': self.L3,
            'L4': self.L4
        })

    def set_data(self, request):
        self.L1 = request.args.get('L1', '')
        self.L2 = request.args.get('L2', '')
        self.L3 = request.args.get('L3', '')
        self.L4 = request.args.get('L4', '')
        return json.dumps({'response': 0})

class Camera:
    def __init__(self):
        self.code=0
    def connect(self,request):
        self.code=request.args.get('code','')
        return json.dumps({'response': 0})
    def get_data(self):
        return {
            'code': self.code
        }