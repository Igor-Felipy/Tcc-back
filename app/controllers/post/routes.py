from . import posts
from ..auth.authenticate import jwt_required
from app.models.tables import  Comment, Like, Post
from app import db
from flask import jsonify, request
from datetime import datetime


#posts routes
@posts.route("/post",methods=["POST"])
@jwt_required
def post(current_user):
    id = request.json['post_id']
    try:
        post = Post.query.filter_by(id=id).first()
        qtt_comments = Comment.query.filter_by(post_id=id).count()
        qtt_likes = Like.query.filter_by(post_id=id).count()
        return jsonify({
            "post_id":post.id,
            "caption":post.caption,
            "image":post.image,
            "date":post.date,
            "post_owner_id":post.user_id,
            "qtt_comments":qtt_comments,
            "qtt_likes":qtt_likes
        })
    except:
        return jsonify({"error":"Post not found"})



@posts.route("/post/new_post", methods=["POST"]) 
@jwt_required
def new_post(current_user):
    try:
        caption = request.json['caption']
        image = request.json['image']
        date = datetime.utcnow()
        post = Post(caption,image,date,user_id=current_user.id)
        db.session.add(post)
        db.session.commit()
        return jsonify({"ok":"post is created"})
    except:
        return jsonify({"error":"Something went wrong!"})


@posts.route("/post/edit_caption", methods=["POST"])
@jwt_required
def edit_post(current_user):
    post_id = request.json['post_id']
    caption = request.json['caption']
    try:
        post = Post.query.filter_by(id=post_id).first()
        if post.user_id == current_user.id:
            post.caption=caption
            db.session.add(post)
            db.session.commit()
            return jsonify({"ok":"caption edited"})
        else:
            return jsonify({"error":"user cannot edit this post"})
    except:
        return jsonify({"error":"something wrong is'nt right"})


@posts.route("/post/delete_post", methods=["POST"])
@jwt_required
def delete_post(current_user):
    post_id = request.json['post_id']
    try:
        post = db.session.query(Post).filter_by(id=post_id).delete()
        print(1)
        # db.session.delete(post)
        print(2)
        db.session.commit()
        print(3)
        return jsonify({"OK":"post deleted"})
    except:
        return jsonify({"error":"error"})







#comments routes
@posts.route("/post/new_comment", methods=["POST"])
@jwt_required
def New_comment(current_user):
    try:
        comment = request.json['comment']
        post_id = request.json['post_id']
        new_comment = Comment(comment,post_id,current_user.id)
        db.session.add(new_comment)
        db.session.commit()
        return jsonify({"ok":"your comment has been added"})
    except:
        return jsonify({"error":"Something wrong is'nt right"})


@posts.route("/post/comments", methods=["POST"])
@jwt_required
def commments(current_user):
    try:
        post_id = request.json['post_id']
        comments = Comment.query.filter_by(post_id=post_id).all()
        all_comments = dict()
        for n in comments:
            all_comments.update({str(n.id):n.comment})
        return jsonify(all_comments)
    except:
        return jsonify({"error":"Something went wrong!"})






#likes routes
@posts.route("/post/new_like", methods=["POST"])
@jwt_required
def new_like(current_user):
    try:
        post_id = request.json['post_id']
        new_like = Like(post_id,current_user.id)
        db.session.add(new_like)
        db.session.commit()
        return jsonify({"ok":"like added"})
    except:
        return jsonify({"error":"something went wrong!"})


@posts.route("/post/cancel_like", methods=["POST"])
@jwt_required
def cancel_like(current_user):
    try:
        post_id = request.json['post_id']
        db.session.query(Like).filter_by(post_id=post_id).filter_by(user_id=current_user.id).delete()
        db.session.commit()
        return jsonify({"ok":"like canceled!"})
    except:
        return jsonify({"error":"something went wrong!"})