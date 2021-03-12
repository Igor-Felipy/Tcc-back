from . import feed
from ..auth.authenticate import jwt_required
from app.models.tables import Follow, Post
from flask import jsonify
from app import db


@feed.route("/feed", methods=["POST"])
@jwt_required
def feed(current_user):
    posts = db.session.query(
        Post, Follow
        ).filter(
            Follow.user_id == current_user
        ).filter(
            Post.user_id == Follow.follower_id
        )
    post_converted = dict()
    for post in posts:
        post_converted.update({
            "id":post.id,
            "caption":post.caption,
            "image":post.image,
            "date":post.date,
            "user_id":post.user_id
        })
    return jsonify({post_converted})