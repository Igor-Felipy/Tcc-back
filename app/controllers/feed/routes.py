from . import feed
from ..auth.authenticate import jwt_required
from app.models.tables import Follow, Post
from flask import jsonify
from app import db


@feed.route("/feed", methods=["POST"])
@jwt_required
def feed(current_user):
    posts = db.session.connection().execute(f"""
        SELECT * FROM posts   
        INNER JOIN follow
        ON posts.user_id = follow.user_id
        INNER JOIN users
        ON follow.follower_id = {current_user.id};
    """)
    post_converted = list()
    count = 1
    print('teste')
    for post in posts:
        post_converted.append({
                "id":post.id,
                "caption":post.caption,
                "image":post.image,
                "date":post.date,
                "user_id":post.user_id
            }
        )
        count+=1
    return jsonify(post_converted)