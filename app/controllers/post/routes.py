from . import post
from ..auth.authenticate import jwt_required


@post.route("/post",methods=["POST"])
@jwt_required
def post(current_user):
    return "post route"

@post.route("/post/new_post", methods=["POST"])
@jwt_required
def new_post(current_user):
    return "new_post route"


@post.route("/post/edit_post", methods=["POST"])
@jwt_required
def edit_post(current_user):
    return "edit_post route"


@post.route("/post/delete_post", methods=["POST"])
@jwt_required
def delete_post(current_user):
    return "delete_post route"