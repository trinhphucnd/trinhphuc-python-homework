import mongoengine

#mongodb://<dbuser>:<dbpassword>@ds249798.mlab.com:49798/muadongkhonglanh
# mongodb://<dbuser>:<dbpassword>@ds259596.mlab.com:59596/muadongcolanh
host = "ds259596.mlab.com"
port = 59596
db_name = "muadongcolanh"
user_name = "admin"
password = "524365Nd"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password,retryWrites=False)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())