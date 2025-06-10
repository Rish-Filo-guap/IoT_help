import datetime

import pymongo

class Log:
    def __init__(self):
        self.is_logging=False
        self.client=pymongo.MongoClient('mongodb://localhost:27017/')
        self.db=self.client['IoT_ex_db']
    def log_data(self, data, collection):
        self.db[collection].insert_one({
            'timeStemp': datetime.datetime.now(),
            **data
        })
    def get_chart(self):
        temp=[]
        time=[]
        cursor=self.db["gripper_data"].find()
        for elem in cursor:
            time.append(elem['timeStemp'])
            tmp=0
            for i in range(1,6):
                tmp+=float(elem['t'+str(i)])
            temp.append(int(tmp/6))
        #print(temp)



        return {
            'time': time[-10:],
            'temp': temp[-10:]
        }