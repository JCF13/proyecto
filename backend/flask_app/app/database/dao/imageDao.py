from flask_app.app.database.models import ChatImage, PostImage, ProfileImage
from flask_app.app.database import db


def create_image(image: ChatImage or PostImage or ProfileImage):
    db.session.add(image)
    db.session.commit()