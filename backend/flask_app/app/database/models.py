from sqlalchemy.sql.schema import ForeignKey
from flask_app.app.database import db
from flask_app.app.database.mixins import CreatedMixin

class Usuario(db.Model):
    __tablename__ = 'usuario'

    usuario_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(200), nullable=False)
    name = db.Column(db.String(25), nullable=True)
    surename = db.Column(db.String(756), nullable=True)
    password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    profile_pic_path = db.Column(db.String(246))
    profile_pic_fname = db.Column(db.String(20))
    privado = db.Column()
    publicaciones = db.relationship(
        'publicacion',
        back_populates='emisor')

class Followers(db.Model,CreatedMixin):
    followed_id = db.Column(db.Integer,db.ForeignKey('usuario.usuario_id'))
    follower_id = db.Column(db.Integer,db.ForeignKey('usuario.usuario_id'))
    id_follow = db.Column(db.Integer,primary_key = True)
    agree = db.Column(db.Boolean, default=False)

class PostLikes(db.Model,CreatedMixin):
    publicacion_id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer,db.ForeignKey('usuario.usuario_id'))
    liked = db.Column(db.Boolean(), nullable=True)

class Publicacion(db.Model, CreatedMixin):
    __tablename__ = 'publicacion'

    publicacion_id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer,db.ForeignKey('usuario.usuario_id'))
    emisor = db.relationship('usuario',back_populates='publicaciones')
    caption = db.Column(db.String(200), nullable=True)
    comentarios = db.relationship('comentario', backref=db.backref('publicacion'))



class Comentario(db.Model, CreatedMixin):
    __tablename__ = 'comentario'

    publicacion_id = db.Column(db.Integer,db.ForeignKey('publicacion.publicacion_id'))
    usuario_id = db.Column(db.Integer,db.ForeignKey('usuario.usuario_id'))
    comentario_id = db.Column(db.Integer,primary_key=True)
    content = db.Column(db.String(200), nullable=True)
