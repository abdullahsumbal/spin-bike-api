#Imported libraries
from flask import Flask
from flask_restful import Resource, Api
from flask_cors import CORS

#Imported local files
from bike_usage import BikeUsageAll
from login import LoginQuery
from account_creation_insert import AccountCreationInsertQuery
from usage_by_id import UsageByIDSelect
from managers import Managers
from schedule import ScheduleAll, Schedule

app = Flask(__name__)
api = Api(app)
CORS(app)

#Add route to api with functionality in specified class
api.add_resource(BikeUsageAll, '/')
api.add_resource(LoginQuery, '/auth', endpoint='auth')
api.add_resource(AccountCreationInsertQuery, '/create')
api.add_resource(UsageByIDSelect, '/usage/<bike_id>')
api.add_resource(Managers, '/managers')
api.add_resource(ScheduleAll, '/schedule_all')
api.add_resource(Schedule, '/schedule/<bm_id>')

if __name__ == '__main__':
    app.run(debug=True)