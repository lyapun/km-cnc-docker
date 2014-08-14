import os

from flask import Flask, render_template, jsonify
from flask.ext.pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_HOST'] = os.environ['MONGO_MONGO1_HOST']
app.config['MONGO_PORT'] = os.environ['MONGO_MONGO1_CLIENT_PORT']

mongo = None


def get_mongo():
    global mongo
    if not mongo:
        mongo = PyMongo(app)
    return mongo


@app.route('/env')
def env():
    return jsonify({'dic': os.environ.__dict__})


@app.route('/')
def home_page():
    mongo = get_mongo()
    users = mongo.db.users.find()
    return render_template('index.html', users=users)


if __name__ == "__main__":
    app.run('0.0.0.0', debug=True)
