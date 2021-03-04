from . import user
from ..auth.authenticate import jwt_required
from flask import jsonify, request
from app.models.tables import User
from app import db


@user.route("/user/edit_user", methods=["POST"])
@jwt_required
def edit_user(current_user):
    id = request.json['id']
    nickname = request.json['nickname']
    name = request.json['name']
    birth = request.json['birth']
    if id == current_user.id:
        try:
            user = User.query.filter_by(id=id)
            user.nickname = nickname
            user.name = name
            user.birth = birth
            db.session.add(user)
            db.session.commit()
        except:
            return jsonify({"error":"data error"})
    else:
        return jsonify({"error":"user not allowed"})
    return jsonify({"Ok":"All right"})


@user.route("/user/get_user", methods=["POST"])
@jwt_required
def get_user(current_user):
    id = request.json['id']
    try:
        user = User.query.filter_by(id=id)
        return jsonify({"data":user})
    except:
        return jsonify({"error":"something is wrong"})