#!/usr/bin/python3.6

import string
import random
import os
import json

from flask import Flask
from flask import request
from flask_restplus import Api, Resource, fields
from werkzeug.contrib.fixers import ProxyFix

from texts import *

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)

api = Api(app, version='1.0', title='flask restplus workshop', description=descriptiveTextCourse3)

awesomeDictionaryToReturn = {}
awesomeDictionaryToReturn["Most awesome programming language."] = "Python"
awesomeDictionaryToReturn["Reason"]                             = "You dont need a reason."
awesomeDictionaryToReturn["Why"]                                = "Just try to do these labs in another language."
awesomeDictionaryToReturn["Original request"]                   = ""

@api.route('/hints')

class hints(Resource):
    @api.doc(responses={200: 'Ok'})
    def get(self):
        return course3_hints


@api.route('/question1')
class question1(Resource):
    def get(self):
        return question3_1


@api.route('/question2')
class question2(Resource):
    def get(self):
        return question3_2


@api.route('/question3')
class question3(Resource):
    def get(self):
        return question3_3


@api.route('/returnJson')
class returnJson(Resource):
    def get(self):
        res = json.dumps(awesomeDictionaryToReturn)
        return res

requestjson = api.model('Resource', {
    'Origial Request': fields.String,
})

@api.route('/concatJson')
class concatJson(Resource):
    @api.expect(requestjson)
    def post(self):
        data = request.json
        awesomeDictionaryToReturn["Original request"] = data['Request']
        res = json.dumps(awesomeDictionaryToReturn)
        return res

@api.route('/modeledJson')
class modeledJson(Resource):
    @api.expect(requestjson)
    def post(self):
        data = request.json
        awesomeDictionaryToReturn["Original request"] = data['Request']
        res = json.dumps(awesomeDictionaryToReturn)
        return res


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='127.0.0.1', port=port)