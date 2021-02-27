from app import db

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True)
    nickname = db.Column(db.String)
    nome = db.Column(db.String)
    birth = db.Column(db.Date)
    password = db.Column(db.String)

    def __init__(self, email, nickname, nome, birth, password):
        self.email = email
        self.nickname = nickname
        self.nome = nome
        self.birth = birth
        self.password = password

    def __repr__(self):
        return "<User %r>" % self.username


class Post(db.Model):
    __tablename__ = "posts"

    id = db.column(db.Integer, primary_key=True)
    caption = db.Column(db.String)
    image = db.Column(db.String)
    date = db.Column(db.Datetime)
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
    image_feels = db.Column(db.String)
    caption_feels = db.Column(db.String)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))

    post = db.relationship("Post", foreigen_keys=post_id)

    def __init__(self, image_feels, caption_feels, post_id):
        self.image_feels = image_feels
        self.caption_feels = caption_feels
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
    post_id = db.Column(db.Integer, db.ForeingKey('posts.id'))
    user_id = db.Column(db.Integer, db.ForeingKey('users.id'))

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
    user_id = db.Column(db.Integer, db.ForeingKey('users.id'))
    follower_id = db.Column(db.Integer, db.ForeingKey('users.id'))
    
    user = db.relationship("User", foreign_keys=user_id)
    follower = db.relationship("User", foreign_keys=user_id)

    def __init__(self, user_id, follower_id):
        self.user_id = user_id
        self.follower_id = follower_id

    def __repr__(self):
        return "<Follow %r>" % self.id

