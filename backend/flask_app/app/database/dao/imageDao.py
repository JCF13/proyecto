from flask_app.app.database.models import ChatImage, PostImage, ProfileImage
from flask_app.app.database import db


def generate_image(image):
    db.session.add(image)
    db.session.commit()


def find_last_profile_image():
    last = ProfileImage.query.order_by(ProfileImage.image_id.desc()).first()
    if last != 0:
        return last.image_id
    else:
        return 0