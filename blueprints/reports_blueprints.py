from flask import Blueprints
from controllers.reports_controller import ReportsController

reports_blueprints = Blueprints("reports_blueprints", __name__)
reports_controller = ReportsController()


@reports_blueprints.route("/reports/highest_grade", methods= ["GET"])
def report_highets_grade():
    response = reports_controller.get_highest_grade()
    return response, 200