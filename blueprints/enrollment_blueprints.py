from flask import Blueprint
from flask import request

from controllers.enrollment_controller import EnrolmentController

enrollment_blueprints = Blueprint("enrollment_blueprints", __name__)
enrollment_controller = EnrolmentController()


@enrollment_blueprints.route("/enrollment/all", methos=["GET"])
def get_all_enrollment():
    response = enrollment_controller.index()
    return response, 200


@enrollment_blueprints.route("/enrollment/<string:id_>", methos=["GET"])
def get_enrollment_by_id(id_):
    response = enrollment_controller.show(id_)
    return response, 200


@enrollment_blueprints.route("/enrollment/course/<string:course_id>", methods=["GET"])
def get_enrolmment_by_course(course_id):
    response = enrollment_controller.get_student_by_course(course_id)
    return response, 200

@enrollment_blueprints.route("/enrollment/insert/course/<string:course_id>/student/<string:student_id>", methos=["POST"])
def insert_enrollment(course_id, student_id):
    enrollment = request.get_json()
    response = enrollment_controller.create(enrollment, course_id, student_id)
    return response, 201


@enrollment_blueprints.route("/enrollment/update/<string:id_>", methos=["PATCH"])
def update_enrollment():
    enrollment = request.get_json()
    response = enrollment_controller.update(id_, enrollment)
    return response, 204


@enrollment_blueprints.route("/enrollment/delete/<string:id_>", methos=["DELETE"])
def delete_course(id_):
    response = enrollment_controller.delete(id_)
    return response, 204

