from flask import Flask, jsonify, request
import os
import gunicorn


app = Flask(__name__)

# port = int(os.environ.get('PORT', 5000))

phrases = ["You are great", "You are fantastic", "You are so good looking","I think you are special","You are number 1",
           "You sure are dandy","There's no one as good as you","You are just so lovely","You are just too perfect",
           "Aren't you just lucky to be you","Everything about you is just really great"]

pics = ["https://gdurl.com/nr3i","https://gdurl.com/j6uz","https://gdurl.com/Hj5U","https://gdurl.com/h0NR",
        "https://gdurl.com/3seU","https://gdurl.com/6bhf","https://gdurl.com/itaB","https://gdurl.com/Wpv7",
        "https://gdurl.com/s0KH","https://gdurl.com/jedc","https://gdurl.com/YSL3"]

# tests = ["test1","test2","test3"]


@app.route('/', methods=['GET','POST'])
def index():
    if (request.method == 'POST'):
        some_json = request.get_json()
        return jsonify({'you sent': some_json}), 201
    else:
        return jsonify({"about":"Hello World!"})


@app.route('/return_data', methods=['GET'])
def return_data():


    return jsonify({'compliments': phrases},{'Pictures': pics})


# @app.route('/dog_picture',methods=['GET'])


if __name__ == '__main__':
    app.run(debug=True, port=33507)
