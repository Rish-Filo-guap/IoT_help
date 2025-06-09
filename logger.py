import datetime

import pymongo

class Log:
    def __init__(self):
        self.is_logging=True
        self.client=pymongo.MongoClient('mongodb://localhost:27017/')
        self.db=self.client['IoT_ex_db']
    def log_data(self, data, collection):
        self.db[collection].insert_one({
            'timeStemp': datetime.datetime.now(),
            **data
        })
