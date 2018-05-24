import datetime


class LogBot(object):
    def __init__(self, db, keys):
        self._db = db
        self._keys = keys

    # accessor methods
    def get_db(self):
        return self._db

    def get_keys(self):
        return self._keys

    # update database
    def update(self, collection, dix):
        dix['datetime'] = datetime.datetime.today()
        db = self.get_db()
        db[collection].insert(dix)

    # message handler
    def analyze_msg(self, bot, update):
        msg = update.message.text

