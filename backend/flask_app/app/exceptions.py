from sqlalchemy.exc import IntegrityError


class InvalidUsername(AttributeError):
    pass


class InvalidPassword(AttributeError):
    pass


class EmailUsed(IntegrityError):
    pass


class UsernameUsed(IntegrityError):
    pass


class RequiredEmail(IntegrityError):
    pass


class RequiredUsername(IntegrityError):
    pass


class RequiredName(IntegrityError):
    pass


class RequiredPassword(IntegrityError):
    pass
