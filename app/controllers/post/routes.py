from . import posts
from ..auth.authenticate import jwt_required


@posts.route("/post",methods=["POST"])
@jwt_required
def post(current_user):
    return "post route"

@posts.route("/post/new_post", methods=["POST"])
@jwt_required
def new_post(current_user):
    return "new_post route"


@posts.route("/post/edit_post", methods=["POST"])
@jwt_required
def edit_post(current_user):
    return "edit_post route"


@posts.route("/post/delete_post", methods=["POST"])
@jwt_required
def delete_post(current_user):
    return "delete_post route"