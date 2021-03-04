from . import posts
from ..auth.authenticate import jwt_required
from app.models.tables import  Comment, Like
from app import db
from flask import jsonify, request


#posts routes
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


@posts.route("/post/comments", methods=["POST"])
@jwt_required
def commments(current_user):
    return "all the coments from a post"





#comments routes
@posts.route("/post/new_comment", methods=["POST"])
@jwt_required
def New_comment(current_user):
    return "Create a comment"

@posts.route("/post/qtd_comment", methods=["POST"])
@jwt_required
def qtd_comment(current_user):
    return "Create a comment"
    





#likes routes
@posts.route("/post/like_qtd", methods=["POST"])
@jwt_required
def like_qtd(current_user):
    post_id = request.json['post_id']
    qtt_like = Like.query.filter_by(post_id=post_id).count()
    return jsonify({"like quantity":qtt_like})


@posts.route("/post/new_like", methods=["POST"])
@jwt_required
def new_like(current_user):
    post_id = request.json['post_id']
    new_like = Like(post_id,current_user.id)
    db.session.add(new_like)
    db.session.commit()
    return "New_like route"

