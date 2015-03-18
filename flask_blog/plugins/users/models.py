from flask.ext.login import UserMixin, AnonymousUserMixin
from bson import ObjectId

class UserLogin(UserMixin):
    def __init__(self, **entries):
        self.__dict__.update(entries)
        self.username = entries["username"]
        self.password = entries["password"]
        self.id = str(ObjectId(entries["_id"]))

    def check_password(self, password):
        if password == self.password:
            return True
        return False

    def is_active(self):
        return True

    def is_authenticated(self):
        if isinstance(self, AnonymousUserMixin):
            return False
        else:
            return True

    def is_anonymous(self):
        if isinstance(self, AnonymousUserMixin):
            return True
        else:
            return False

    def get_id(self):
        return self.id

    def __repr__(self):
        return '<User %r>' % self.username
