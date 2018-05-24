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

    def get_field(self, key):
        return self.get_keys()[key]

    def get_category(self, key):
        if
    def get_dict(self, key):
        pass

    def analyze_key(self, key):
        if len(key) != 2:
            return None
        elif key[0] == 'S':



    # update database
    def update(self, collection, dix):
        dix['datetime'] = datetime.datetime.today()
        db = self.get_db()
        db[collection].insert(dix)

    # message handler
    def analyze_msg(self, bot, update):
        msg = update.message.text
        words = msg.split(' ')
        key = words[0]
        payload = words[1:]

