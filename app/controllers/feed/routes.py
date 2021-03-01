from . import feed
from ..auth.authenticate import jwt_required

@feed.route("/feed", methods=["POST"])
@jwt_required
def feed(current_user):
    return "feed route"