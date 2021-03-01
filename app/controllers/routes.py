from . import controller
from flask import jsonify

@controller.route('/')
def definition():
    return jsonify({"API Routes":{
        "auth":{
            "/auth/login":"The route used to log in the application, you need to send a POST (using a JSON) request with the parameters: email and password, you'll receive a token.",
            "/auth/register":"The route used to create a new user, you need to send a POST (using a JSON) request with the parameters: email, nickname, name, birth, password, you'll receive the public data of the user created.",
            "/auth/protected":"Route created only for test pourpose, you send a GET request with a header authorization using the follower pattern: Bearer YOUR_TOKEN, and you'll receive the name of the logged user."
        },
        "user":{
            "/user/edit_user":"Route used to edit users information (JWT required)"
        },
        "post":{
            "/post":"This route get an especific post",
            "/post/new_post":"This route create a new post",
            "/post/edit_post":"This route edit a post",
            "/post/delet_post":"This route delete a post"
        },
        "details":{
            "/detail":"This route get the detail of some post"
        },
        "feed":{
            "/feed":"This route return the posts used in feed page, you need to send the header authorization(explained in /auth/protected)"
        },
        "others":{
            "/":"The route to describe the routes (used to explain how to implement the front)."
        }
    }})