from app import db, ma
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String, unique=True, nullable=False)
    nickname = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)
    birth = db.Column(db.Date, nullable=False)
    password = db.Column(db.String, nullable=False)

    def __init__(self, email, nickname, name, birth, password):
        self.email = email
        self.nickname = nickname
        self.name = name
        self.birth = birth
        self.password = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return "<User %r>" % self.name


class UserSchema(ma.Schema):
    class Meta:
        fields = ('id','email','nickname','name','birth')

user_share_schema = UserSchema()
users_share_schema = UserSchema(many=True)


class Post(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    caption = db.Column(db.String)
    image = db.Column(db.String)
    date = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    user = db.relationship("User",foreign_keys=user_id)

    def __init__(self, caption, image, date, user_id):
        self.caption = caption
        self.image = image
        self.date = date
        self.user_id = user_id

    def __repr__(self):
        return "<Post %r>" % self.id


class Detail(db.Model):
    __tablename__ = "details"

    id = db.Column(db.Integer, primary_key=True)
    neg = db.Column(db.Float)
    neu = db.Column(db.Float)
    pos = db.Column(db.Float)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))

    post = db.relationship("Post", foreign_keys=post_id)

    def __init__(self, neg, neu, pos, post_id):
        self.neg = neg
        self.neu = neu
        self.pos = pos
        self.comp = comp
        self.post_id = post_id

    def __repr__(self):
        return "<Detail %r>" % self.id


class Like(db.Model):
    __tabelname__ = "likes"

    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    post = db.relationship("Post", foreign_keys=post_id)
    user = db.relationship("User", foreign_keys=user_id)

    def __init__(self, post_id, user_id):
        self.post_id = post_id
        self.user_id = user_id

    def __repr__(self):
        return "<Like %r>" % self.id


class Comment(db.Model):
    __tablename__ = "comments"

    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    post = db.relationship("Post", foreign_keys=post_id)
    user = db.relationship("User", foreign_keys=user_id) 

    def __init__(self, comment, post_id, user_id):
        self.comment = comment
        self.post_id = post_id
        self.user_id = user_id

    def __repr__(self):
        return "<Comment %r>" % self.comment


class Follow(db.Model):
    __tablename__ = "follow"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    follower_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    
    user = db.relationship("User", foreign_keys=user_id)
    follower = db.relationship("User", foreign_keys=user_id)

    def __init__(self, user_id, follower_id):
        self.user_id = user_id
        self.follower_id = follower_id

    def __repr__(self):
        return "<Follow %r>" % self.id

