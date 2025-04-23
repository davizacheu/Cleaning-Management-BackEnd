from app.extensions import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    profile_picture_url = db.Column(db.String(255), nullable=True)

    auth_token = db.relationship(
        'AuthToken',
        back_populates='user',
        uselist=False,
        cascade='all, delete-orphan',
        passive_deletes=True,
        lazy='joined'
    )

    roles = db.relationship(
        'Role',
        back_populates='user',
        lazy='selectin',
        single_parent=True,
        passive_deletes='all'
    )

    role_invitations = db.relationship(
        'RoleInvitation',
        back_populates='user',
        cascade='all, delete-orphan',
        lazy='selectin'
    )

    orders = db.relationship(
        'Order',
        back_populates='user',
        lazy='selectin',
        single_parent=True,
        cascade='all, delete-orphan',
        passive_deletes=True,
    )

    def __repr__(self):
        return f'<User {self.username}>'
