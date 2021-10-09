import psycopg2
from psycopg2.extras import DictCursor
from os import listdir
from app import config

def init_db():
    global db
    db = _db_connect()
    global cur
    cur = db.cursor()

def _db_connect():
    return psycopg2.connect(
        dbname = config.cfg['database']['dbname'],
        user = config.cfg['database']['user'],
        password = config.cfg['database']['password'],
        host = config.cfg['database']['host'],
        port = config.cfg['database']['port'],
        cursor_factory = DictCursor
    )

def check_connection():
    try:
        return db
    except:
        return None

def init_requests():
    global requests
    requests = _load_requests()

def _load_requests():
    requests = {}
    for file in listdir('scripts/requests'):
        requests[file] = open('scripts/requests/' + file).read()
    return requests

def create_student(name, group):
    request = requests['create_student.sql']
    try:
        cur.execute(request, {'name': name, 'group': group})
        db.commit()
        return True
    except Exception as e:
        print(e)
        db.rollback()
        return False

def create_group(group):
    request = requests['create_group.sql']
    try:
        cur.execute(request, {'group': group})
        db.commit()
        return True
    except Exception as e:
        print(e)
        db.rollback()
        return False

def get_group(group):
    request = requests['get_group.sql']
    cur.execute(request, {'group': group})
    return cur.fetchone()

def get_students():
    request = requests['get_students.sql']
    cur.execute(request)
    return cur.fetchall()

def recreate_db():
    db_creation_file = open('scripts/init/create_db.sql').read()
    requests = db_creation_file.strip().split(';')
    requests = requests[:-1]
    result = 'Success'
    for request in requests:
        try:
            cur.execute(request, {'user': config.cfg['database']['user'], 'db': config.cfg['database']['dbname']})
            db.commit()
        except Exception as e:
            db.rollback()
            result = e
            break
    return result
