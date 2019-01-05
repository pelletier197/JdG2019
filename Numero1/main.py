from flask import Flask, redirect, url_for, request, abort
import json
import uuid

app = Flask(__name__)

aliens = []


@app.route('/api/alien', methods=['POST'])
def create_alien():
    req = json.loads(to_not_shit(request.data.decode("utf-8")))
    if not all_exist(req['friends']):
        abort(400)
    id = str(uuid.uuid4())
    req['id'] = id
    aliens.append(req)

    return to_shit(json.dumps(req, sort_keys=True, indent=4))


@app.route('/api/alien/name/<id>', methods=['GET'])
def get_alien(id):
    for a in aliens:
        if a['id'] == id:
            return to_shit(json.dumps(a, sort_keys=True, indent=4))
    abort(400)


@app.route('/api/alien', methods=['GET'])
def get_all_alien():
    return to_shit(json.dumps({'aliens': aliens}, sort_keys=True, indent=4))


@app.route('/api/alien/name/<id>', methods=['DELETE'])
def delete_alien(id):
    for a in aliens:
        if a['id'] == id:
            aliens.remove(a)
            return ("", 200)

    abort(400)


@app.route('/api/alien/name/<id>', methods=['PUT'])
def edit_alien(id):
    for a in aliens:
        if a['id'] == id:
            aliens.remove(a)
            na = json.loads(to_not_shit(request.data.decode("utf-8")))
            na['id'] = id
            aliens.append(na)
            return ("", 200)

    abort(400)


def to_not_shit(json_fucke: str):
    return json_fucke.replace("^", "{").replace("&", "}").replace("/*", "[").replace("*/", "]").replace("'", "\"")


def to_shit(json: str):
    return json.replace("{", "^").replace("}", "&").replace("[", "/*").replace("]", "*/").replace("\"", "'")


def all_exist(friends):
    for f in friends:
        if not exist(f):
            return False

    return True


def exist(name):
    for a in aliens:
        if a['name'] == name:
            return True

    return False


if __name__ == '__main__':
    app.run()
