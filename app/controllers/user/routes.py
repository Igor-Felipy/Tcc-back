from . import user
from ..auth.authenticate import jwt_required


@user.route("/user/edit_user", methods=["POST"])
@jwt_required
def edit_user(current_user):
    return "edit_user page"