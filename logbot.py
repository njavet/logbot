import datetime
import pymongo
import helpers


class LogBot(object):
    def __init__(self, db, keys, attrs, collections):
        self._db = db
        self._keys = keys
        self._attrs = attrs
        self._collections = collections

    # accessor methods
    def get_db(self):
        return self._db

    def get_keys(self):
        return self._keys

    def get_attrs(self):
        return self._attrs

    def get_collections(self):
        return self._collections

    # basic
    def get_field(self, key):
        return self.get_keys()[key]

    def get_attr_lst(self, key):
        field = self.get_field(key)
        return self.get_attrs()[field]

    def get_collection(self, key):
        cols = self.get_collections()
        return cols[key[0]]

    def get_dict(self, key, payload):
        key_lst = self.get_attr_lst(key)
        dix = dict(zip(key_lst, payload))
        return dix

    def analyze_key(self, key):
        keys = self.get_keys()
        col, field = None, None
        if key in keys:
            col = self.get_collection(key)
            field = self.get_field(key)
        return col, field

    # update database
    def update(self, collection, dix):
        dix['datetime'] = datetime.datetime.today()
        db = self.get_db()
        db[collection].insert(dix)

    # access database
    def read(self, collection):
        db = self.get_db()
        cursor = db[collection].find().sort('_id', pymongo.ASCENDING)
        return cursor

    # message handler
    def analyze_msg(self, bot, update):
        msg = update.message.text
        chat_id = update.message.chat_id
        words = msg.split(' ')
        key = words[0]
        payload = words[1:] + ['']

        col, field = self.analyze_key(key)
        correct = helpers.correct_payload(payload)
        if all([col, field, correct]):
            dix = self.get_dict(key, payload)
            self.update(col, {field: dix})
            ans = ' '.join([field, 'unit has been confirmed...'])
        else:
            ans = 'wrong msg format...'

        bot.send_message(chat_id=chat_id, text=ans)


    # commands
    def stronglift(self, bot, update):
        # ugly with the 'stronglift' variable
        cursor = self.read('stronglift')
        helpers.stronglift_summary(cursor)
