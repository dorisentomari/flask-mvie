# -*- coding: utf-8 -*-
from datetime import datetime
from app import db

# 用户
class User(db.Model):
    __tablename__ = 'user'
    __table_args__ = {"useexisting": True}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    pwd = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    phone = db.Column(db.String(11), unique=True)
    info = db.Column(db.Text)
    face = db.Column(db.String(255), unique=True)
    # addtime = db.Column(db.DateTime, index=True, default=datetime.now)
    uuid = db.Column(db.String(255), unique=True)
    userlogs = db.relationship('Userlog', backref='user')
    comments = db.relationship('Comment', backref='user')
    moviecols = db.relationship('Moviecol', backref='user')

    def __repr__(self):
        return '<User %r>' % self.name


# 用户登录日志
class Userlog(db.Model):
    __tablename__ = 'userlog'
    __table_args__ = {"useexisting": True}
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    ip = db.Column(db.String(100))
    # addtime = db.Column(db.DateTime, index=True, default=datetime.now)

    def __repr__(self):
        return '<User %r>' % self.id


# 电影标签
class Tag(db.Model):
    __tablename__ = 'tag'
    __table_args__ = {"useexisting": True}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    # addtime = db.Column(db.DateTime, index=True, default=datetime.now)
    movies = db.relationship('Movie', backref='tag')

    def __repr__(self):
        return '<Tag %r>' % self.name


# 电影
class Movie(db.Model):
    __tablename__ = 'movie'
    __table_args__ = {"useexisting": True}
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), unique=True)
    url = db.Column(db.String(255), unique=True)
    info = db.Column(db.Text)
    logo = db.Column(db.String(255), unique=True)
    star = db.Column(db.SmallInteger)
    playnum = db.Column(db.BigInteger)
    commentnum = db.Column(db.BigInteger)
    tag_id = db.Column(db.Integer, db.ForeignKey('tag.id'))
    area = db.Column(db.String(255))
    release_time = db.Column(db.Date)
    length = db.Column(db.String(100))
    # addtime = db.Column(db.DateTime, index=True, default=datetime.now)
    comments = db.relationship('Comment', backref='movie')
    moviecols = db.relationship('Moviecol', backref='movie')

    def __repr__(self):
        return '<Movie %r>' % self.title


# 上映预告
class Preview(db.Model):
    __tablename__ = 'preview'
    __table_args__ = {"useexisting": True}
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), unique=True)
    logo = db.Column(db.String(255), unique=True)
    # addtime = db.Column(db.DateTime, index=True, default=datetime.now)

    def __repr__(self):
        return '<Preview %r>' % self.title


# 评论电影
class Comment(db.Model):
    __tablename__ = 'comment'
    __table_args__ = {"useexisting": True}
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    # addtime = db.Column(db.DateTime, index=True, default=datetime.now)

    def __repr__(self):
        return '<Comment %r>' % self.id


# 收藏电影
class Moviecol(db.Model):
    __tablename__ = 'moviecol'
    __table_args__ = {"useexisting": True}
    id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    # addtime = db.Column(db.DateTime, index=True, default=datetime.now)

    def __repr__(self):
        return '<Moviecol %r>' % self.id


# 权限
class Auth(db.Model):
    __tablename__ = 'auth'
    __table_args__ = {"useexisting": True}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    url = db.Column(db.String(255), unique=True)
    # addtime = db.Column(db.DateTime, index=True, default=datetime.now)

    def __repr__(self):
        return '<Auth %r>' % self.name


# 角色
class Role(db.Model):
    __tablename__ = 'role'
    __table_args__ = {"useexisting": True}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    auths = db.Column(db.String(600))
    # addtime = db.Column(db.DateTime, index=True, default=datetime.now)
    admins = db.relationship("Admin", backref='role')

    def __repr__(self):
        return '<Role %r>' % self.name


# 管理员
class Admin(db.Model):
    __tablename__ = 'admin'
    __table_args__ = {"useexisting": True}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    pwd = db.Column(db.String(100))
    is_super = db.Column(db.SmallInteger)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))
    # addtime = db.Column(db.DateTime, index=True, default=datetime.now)
    adminlogs = db.relationship('Adminlog', backref='admin')
    oplogs = db.relationship('Oplog', backref='admin')

    def __repr__(self):
        return '<Admin %r>' % self.name


# 登录日志
class Adminlog(db.Model):
    __tablename__ = 'adminlog'
    __table_args__ = {"useexisting": True}
    id = db.Column(db.Integer, primary_key=True)
    admin_id = db.Column(db.Integer, db.ForeignKey('admin.id'))
    ip = db.Column(db.String(100))
    # addtime = db.Column(db.DateTime, index=True, default=datetime.now)

    def __repr__(self):
        return '<Adminlog %r>' % self.id


# 操作日志
class Oplog(db.Model):
    __tablename__ = 'oplog'
    __table_args__ = {"useexisting": True}
    id = db.Column(db.Integer, primary_key=True)
    admin_id = db.Column(db.Integer, db.ForeignKey('admin.id'))
    ip = db.Column(db.String(100))
    reason = db.Column(db.String(1024))
    # addtime = db.Column(db.DateTime, index=True, default=datetime.now)

    def __repr__(self):
        return '<Oplog %r>' % self.id


if __name__ == '__main__':
    db.create_all()
    # db.metadata.clear()
