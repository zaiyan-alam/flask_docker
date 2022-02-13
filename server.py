from flask import Flask, render_template, request, jsonify, make_response
from flask_restful import Resource, Api, reqparse
import pandas as pd
import os

app = Flask(__name__)
api = Api(app)

@app.route('/')
def index():
    return render_template('index.html', title='Carvana Asessment')

# class to handle our work of processing the CSVs through api endpoint
class Locations(Resource):
    def __init__(self):
        self.data_locations = pd.read_csv('static/locations.csv')  # read local CSVs in the constructor
        self.data_trips = pd.read_csv('static/trips.csv')

    def get(self):
        parser = reqparse.RequestParser()  # initialize the argument parser
        parser.add_argument('codes', required=True, help = 'Enter Location Code')
        arguments = parser.parse_args()    # input location codes
        entered_codes = arguments["codes"].split()

        results = {}                       # to save the information regarding multiple location codes
        for each in entered_codes:         # each ---> regarding each location code
            if each not in set(self.data_locations['LocationCode']):
                return 'The location code - '+each+' does not exist!', 404   # if a location code doesn't exists in the dataframe with NOT FOUND status code
            retrieved_location = self.data_locations.loc[self.data_locations['LocationCode'] == each]
            result = retrieved_location.to_dict(orient = 'records')
            retrieved_trips = self.data_trips.loc[(self.data_trips['Origin'] == each) | (self.data_trips['Destination'] == each)]
            result[0]['trips'] = retrieved_trips.to_dict(orient = 'records')
            results[each] = result[0]
        return results, 200               # returing the retrieved data with 200 OK status code

api.add_resource(Locations, '/locations')   # add api endpoint

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host="0.0.0.0", port=port, debug=True)  # run our Flask app
