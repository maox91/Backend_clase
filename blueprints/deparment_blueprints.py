from flask import Blueprint
from flask import request

from controllers.department_controller import DepartmentController


department_blueprint = Blueprint("department_blueprints", __name__)
department_controller = DepartmentController()

@department_controller.route("/department/all", methods=["GET"])
def get_all_departments():
    response = department_controller.index()
    return response, 200

@department_controller.route("/department/<string:id_", methods=["GET"])
def gte_department_by_id(id_):
    response = department_controller.show(id_)
    return response, 200

@department_controller.route("/department/insert", methods=["POST"])
def insert_department():
    department = request.get_json()
    response = department_controller.create(department)
    return response, 201
@department_controller.route("/department/update/<string:id_>", methods=["PATCH"])
def update_department(id_):
    department = request.get_json()
    response = department_controller.update(id_, department)
    return response, 201


@department_controller.route("/department/delete/<string:id_>", methods=["DELETE"])
def delete_department(id_):
    response = department_controller.delete(id_)
    return response, 204