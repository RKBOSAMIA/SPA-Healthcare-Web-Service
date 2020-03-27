import flask
from flask_restful import Api, Resource, reqparse

app = flask.Flask(__name__)
api = Api(app)


patientDB = [{
                'name':"Rushikesh",
                'age' :24,
                'note':"Fit"
            },
            {
                'name':"Kunal",
                'age' :25,
                'note':"Obese"
            }
        ]

class Patients(Resource):
    def get(self):
        #return flask.jsonify(patientDB),200
        resp = ""
        for patient in patientDB:
                resp += "<body><b>Name:</b> " + patient['name'] + "<b> Age: </b>" + str(patient['age'])
                resp += " <b>Notes:</b> " + patient['note'] +"</body> <br>"

        return flask.make_response(resp)
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("name")
        parser.add_argument("age")
        parser.add_argument("note")
        args = parser.parse_args()

        patient = { 'name': args["name"],
                    'age' : args["age"],
                    'note': args["note"]
                    }
        patientDB.append(patient)
        resp = ""
        for patient in patientDB:
                resp += "<body><b>Name:</b> " + patient['name'] + "<b> Age: </b>" + str(patient['age'])
                resp += " <b>Notes:</b> " + patient['note'] +"</body> <br>"


        return flask.make_response(resp)

api.add_resource(Patients,"/patient")
app.run(debug=True)