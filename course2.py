#!/usr/bin/python3.6

import string
import random
import os

from flask import Flask
from flask import request
from flask_restplus import Api, Resource, fields
from flask_restplus import reqparse
from werkzeug.contrib.fixers import ProxyFix

from texts import *

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)

api = Api(app, version='1.0', title='flask restplus workshop', description=descriptiveTextCourse2)


@api.route('/hints')
class hints(Resource):
    @api.doc(responses={200: 'Ok'})
    def get(self):
        return course2_hints


@api.route('/question1')
class question1(Resource):

    def get(self):
        return question2_1

@api.route('/question2')
class question2(Resource):
    def get(self):
        return question2_2

@api.route('/question3')
class Question3(Resource):

    def get(self):
        return question2_3

    def post(self):
        return question2_3


@api.route('/question4')
class question4(Resource):

    def get(self):
        return question2_4

@api.doc(params={'parma' : 'int' , 'parb' :'int' })
@api.route('/sum')
class sum(Resource):

    def get(self):
        args = request.args
        no1 = int(args['parma'])
        no2 = int(args['parb'])
        res = no1 + no2
        return res

    def post(self):
        args = request.args
        no1 = int(args['parma'])
        no2 = int(args['parb'])
        res = no1 + no2
        return res

@api.route('/compute/<string:action>/<int:parma>/<int:parb>')
class compute(Resource):

    def post(self, action, parma, parb):

        if action == "add":
            return parma + parb
        elif action == 'subtract':
            return parma - parb
        elif action == 'multiply':
            return parma * parb
        elif action == 'devide':
            return parma / parb
        else:
            return "No valid action. Possible actions are  'add', 'subtract', 'multiply' or 'devide'."


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='127.0.0.1', port=port)

