import json

from flask import Flask
from flask import jsonify
from flask_cors import CORS
from waitress import serve

from blueprints.course_blueprints import course_blueprints
from blueprints.department_blueprints import department_blueprints
from blueprints.enrollment_blueprints import enrollment_blueprints
from blueprints.student_blueprints import student_blueprints

app = Flask(__name__)
cors = CORS(app)
app.register_blueprint(course_blueprints)
app.register_blueprint(department_blueprints)
app.register_blueprint(enrollment_blueprints)
app.register_blueprint(student_blueprints)


@app.route("/", methods=["GET"])
def home():
    response = {"message" : "Welcome to app"}
    return jsonify(response)

#======Config and setuo app========
def load_file_config():
    with open("config.json", "r") as config_file:
        data = json.load(config_file)
    return data



if __name__ == '__main__':
    data_config = load_file_config()
    print("Server running: http://" + data_config.get("url-backend") + ":" + str(data_config.get("port")))
    serve(app, host=data_config.get("url-backend"), port=data_config.get("port"))
