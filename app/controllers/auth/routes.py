from . import auth
from flask import request, jsonify
from app import db, app
from app.models.tables import User, user_share_schema, users_share_schema
import datetime
import jwt
from app.controllers.auth.authenticate import jwt_required



@auth.route('/auth/register', methods=["POST"])
def register():
    email = request.json['email']
    nickname = request.json['nickname']
    name = request.json['name']
    birth = request.json['birth']
    password = request.json['password']

    date_converted = datetime.datetime.strptime(birth, '%d/%m/%Y').date()

    user = User(
        email,
        nickname,
        name,
        date_converted,
        password
    )

    db.session.add(user)
    db.session.commit()

    result = user_share_schema.dump(
        User.query.filter_by(email=email).first()
    )

    return jsonify(result)



@auth.route('/auth/login', methods=["POST"])
def login():
    email = request.json['email']
    password = request.json['password']

    user = User.query.filter_by(email=email).first_or_404()

    if not user.verify_password(password):
        return jsonify({
            "error":"wrong credentials"
        }), 403

    payload = {
        "id":user.id,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=25)
    }

    token = jwt.encode(payload, app.config['SECRET_KEY'], algorithm="HS256")

    return jsonify({"token": token})


@auth.route('/auth/protected')
@jwt_required
def protected(current_user):    
    result =  users_share_schema.dump(
        User.query.all()
    )

    return jsonify({"current_user":current_user.name})