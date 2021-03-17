from . import post_detail
from ..auth.authenticate import jwt_required
from flask import request, jsonify
from app.models.tables import Detail, Post
from leia import SentimentIntensityAnalyzer 
from app import db


@post_detail.route("/detail", methods=["POST"])
@jwt_required
def post_detail(current_user):
    post_id = request.json['post_id']
    detail = Detail.query.filter_by(post_id=post_id).first()
    if detail is not None:
        try:
            return jsonify({
                "id":detail.id,
                "neg":detail.neg, 
                "neu":detail.neu,
                "pos":detail.pos,
                "post_id":detail.post_id
            })
        except:
            return jsonify({"error":"something went wrong!"})
    else:
        try:
            analyser = SentimentIntensityAnalyzer()
            post = Post.query.filter_by(id=post_id).first()
            score = analyser.polarity_scores(post.caption)
            print(score)
            new_detail = Detail(None,score["neg"],score["neu"],score["pos"],post_id)
            db.session.add(new_detail)
            db.session.commit()
            new_response = Detail.query.filter_by(post_id=post_id).first()
            return jsonify({
                "id":new_response.id,
                "neg":new_response.neg, 
                "neu":new_response.neu,
                "pos":new_response.pos,
                "post_id":new_response.post_id
            })
        except:
            return jsonify({"error":"try again later!"})
