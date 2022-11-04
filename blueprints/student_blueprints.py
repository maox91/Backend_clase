from flask import Blueprint
from flask import request

from controllers.student_controller import StudentController

student_blueprints = Blueprint("student_blueprints", __name__)
student_controller = StudentController()

@student_blueprints.route("/course/all", methods=["GET"])
def get_all_students():
    response = student_controller.index()
    return response, 200
@student_blueprints.route("/course/<string:id_>", methods=["GET"])
def get_student_by_id(id_):
    response = student_controller.show(id_)
    return response, 200

@student_blueprints.route("/course/insert", methods=["POST"])
def insert_student():
    student = request.get_json()
    response = student_controller.insert(student)
    return response, 201
@student_blueprints.route("/course/update/<string:id_>", methods=["PATCH"])
def update_student(id_):
    student = request.get_json()
    response = student_controller.update(student)
    return response, 201

@student_blueprints.route("/course/delete/<string:id_>", methods=["DELETE"])
def delete_student(id_):
    response = student_controller.delete(id_)
    return response, 204

