from flask import Blueprint
from flask import request

from controllers.course_controller import CourseController


course_blueprints = Blueprint("course_blueprints", __name__)
course_controller = CourseController()


@course_blueprints.route("/course/all", methods=["GET"])
def get_all_course():
    response = course_controller.index()
    return response, 200
@course_blueprints.route("/course/<string:id_>", methods=["GET"])
def get_course_by_id(id_):
    response = course_controller.show(id_)
    return response, 200
@course_blueprints.route("/course/insert", methods=["POST"])
def insert_course():
    course=request.get_json()
    response = course_controller.create(course)
    return response, 201
@course_blueprints.route("/course/update/<string:id_>", methods=["PATCH"])
def update_course(id_)
    course = request.get_json()
    response = course_controller.update(id_, course)
    return response, 201
@course_blueprints.route("/course/delete/<string:id_>", methods=["DELETE"])
def delete_course(id_):
    response = course_controller.delete(id_)
    return response, 204
