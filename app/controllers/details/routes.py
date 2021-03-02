from . import post_detail
from ..auth.authenticate import jwt_required


@post_detail.route("/detail", methods=["POST"])
@jwt_required
def post_detail(current_user):
    return "details route"