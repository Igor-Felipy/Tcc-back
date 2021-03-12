from . import post_detail
from ..auth.authenticate import jwt_required
from flask import request, jsonify
from app.models.tables import Detail, Post
from app.controllers.details.leia import SentimentIntensityAnalyzer 
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
                "image_feels":detail.image_feels,
                "caption_feels":detail.caption_feels,
                "post_id":detail.post_id
            })
        except:
            return jsonify({"error":"something went wrong!"})
    else:
        try:
            print(SentimentIntensityAnalyzer.polarity_scores('teste'))
            post = Post.query.filter_by(id=post_id).first()
            score = SentimentIntensityAnalyzer.polarity_scores(post.caption)
            print(score)
            new_detail = Detail(None,score.compound,post_id)
            db.session.add(new_detail)
            db.session.commit()
            new_response = Detail.query.filter_by(post_id=post_id).first()
            return jsonify({
                "id":new_response.id,
                "image_feels":new_response.image_feels,
                "caption_feels":new_response.caption_feels,
                "post_id":new_response.post_id
            })
        except:
            return jsonify({"error":"try again later!"})
