from registration import app
from flask import request, jsonify
from registration.manager import Manager


@app.route('/register', methods=['POST'])
def register():
    data = request.get_json(force=True)
    name = data['name']
    fullname = data['fullname']
    nickname = data['nickname']

    mananger = Manager()
    value = mananger.register_user(name, fullname, nickname)
    message = 'Exception occured while creating user.'

    if value:
        message = value
    
    response = {
        'message': message
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0')