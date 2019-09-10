#!/usr/bin/python3.6

import string
import random
import os
import csv
import json

from flask import Flask
from flask import request
from flask_restplus import Api, Resource, fields
from werkzeug.contrib.fixers import ProxyFix

from texts import *

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)

api = Api(app, version='1.0', title='flask restplus workshop', description=descriptiveTextCourse4)
csvfile = "example.csv"

@api.route('/thecall')
class question1(Resource):
    def get(self):
        csv_read = csv.reader(csvfile, delimiter=',')
        rows = []
        for row in csv_read:
            rows.append(row)

        cols = rows[0]
        res = []
        for row in csv_read[1:]:
            temp = {}
            for index, col in enumerate(cols):
                temp[col] = row[index]
            res.append(temp)
        return json.dumps(res)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='127.0.0.1', port=port)