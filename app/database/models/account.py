from app import db


class Account(db.Model):
    """Model for accounts."""

    __tablename__ = 'account'

    id = db.Column(db.Integer,
                   primary_key=True)
    name = db.Column(db.String(64),
                     index=False,
                     unique=True,
                     nullable=False)
    created_at = db.Column(db.DateTime,
                        index=False,
                        unique=False,
                        nullable=False)

    def __repr__(self):
        return '<Account {}>'.format(self.name)
