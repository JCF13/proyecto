from sqlalchemy.exc import IntegrityError


class InvalidUsername(AttributeError):
    pass


class EmailUsed(IntegrityError):
    pass

class UsernameUsed(IntegrityError):
    pass
