from backend.flask_app.app.database import db


def generate_image(image):
    """
    Takes a ChatImage, PostImage or ProfileImage object
    depends on the type of the param

    :param image: the actual object which will be
                    saved at the data base
    """
    db.session.add(image)
    db.session.commit()


#def find_last_profile_image():
#    """
#    Find the last image_id from ProfileImage object

#    Return int
#    """
#    last = ProfileImage.query.order_by(ProfileImage.image_id.desc()).first()
#    if last != 0:
#        return last.image_id
#    else:
#        return 0