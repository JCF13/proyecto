import datetime
from flask_login import current_user
from sqlalchemy import Column, DateTime, ForeignKey, Integer
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import relationship

class CreatedMixin(object):
    """
        AuditMixin
        Mixin for models, adds 4 columns to stamp,
        time and user on creation and modification
        will create the following columns:

        :created on:
        :changed on:
        :created by:
        :changed by:
    """

    created_on = Column(DateTime, default=datetime.datetime.now, nullable=False)

    @declared_attr
    def created_by_fk(self):
        return Column(
            Integer, ForeignKey("user.user_id"), default=self.get_user_id, nullable=False
        )
    @declared_attr
    def created_by(self):
        return relationship(
            "User",
            primaryjoin="%s.created_by_fk == user.user_id" % self.__name__,
            enable_typechecks=False,
        )




    @classmethod
    def get_user_id(self):
        try:
            return current_user.id
        except Exception:
            return None
