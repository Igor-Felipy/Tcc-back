from . import feed
from ..auth.authenticate import jwt_required
from app.models.tables import Post
from flask import jsonify


@feed.route("/feed", methods=["POST"])
@jwt_required
def feed(current_user):
    post = Post.query.filter_by().all()
    return jsonify(post)