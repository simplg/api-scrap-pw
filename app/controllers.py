from flask import Blueprint, request, Response
from flask.json import jsonify
from .scrap import scrap_last_week, scrap_last_day

main_controller = Blueprint("app", __name__, url_prefix="/")

@main_controller.route("/")
async def index_controller():
    tf = request.args.get("tf")
    if tf is None:
        return Response(status=400)
    if tf not in ["1", "7"]:
        return Response(status=418)
    r = await scrap_last_day() if tf == "1" else await scrap_last_week()

    return jsonify(**r)
    