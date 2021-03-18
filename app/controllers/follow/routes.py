from . import follows
from app.controllers.auth.authenticate import jwt_required
from flask import request, jsonify
from app.models.tables import Follow
from app import db


@follows.route("/follow/new_follow",methods=["post"])
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
    


@follows.route("/follow/user_follows",methods=["post"])
@jwt_required
def user_follows(current_user):
    user = request.json['user_id']
    try:
        many_follows = Follow.query.filter_by(user_id = user).all()
        all_follows = dict()
        count = 1
        for follow in many_follows:
            all_follows.update({
                str(count):{
                    "user_id":follow.user_id,
                    "follower_id":follow.follower_id
                }
            })
            count+=1
        return jsonify(all_follows)
    except:
        return jsonify({"error":"something went wrong!"})
    

@follows.route("/follow/unfollow",methods=["post"])
@jwt_required
def unfollow(current_user):
    user_id = request.json['user_id']
    try:
        db.session.query(Follow).filter_by(follower_id=user_id,user_id=current_user.id).delete()
        return jsonify({"ok":f"follow {user_id} deleted"})
    except:
        return jsonify({"error":"something went wrong!"})