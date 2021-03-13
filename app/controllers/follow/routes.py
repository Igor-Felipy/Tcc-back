from . import follows
from app.controllers.auth import jwt_required
from flask import request, jsonify
from app.models.tables import Follow
from app import db


@follows.route("/follow/new_follow")
@jwt_required
def new_follows(current_user):
    user = request.json['user_id']
    try:
        new_follow = Follow(current_user.id,user)
        db.session.add(new_follow)
        db.session.commit()
        return jsonify({"ok":"Follow added"})
    except:
        return jsonify({"error":"something went wrong!"})
    


@follows.route("/follow/user_follows")
@jwt_required
def user_follows(current_user):
    user = request.json['user_id']
    try:
        follows = Follow.query.filter_by(user_id = user).all()
        all_follows = dict()
        Follow()
        for follow in follows:
            all_follows.update({
                "user_id":follow.user_id,
                "follower_id":follow.follower_id
            })
        return jsonify({"all_follows":all_follows})
    except:
        return jsonify({"error":"something went wrong!"})
    

@follows.route("/follow/unfollow")
@jwt_required
def unfollow(current_user):
    user_id = request.json['user_id']
    try:
        db.session.query(Follow).filter_by(follower_id=user_id,user_id=current_user.id).delete()
        return jsonify({"ok":"follow deleted"})
    except:
        return jsonify({"error":"something went wrong!"})