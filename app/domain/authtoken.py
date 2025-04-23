from datetime import datetime
from app.extensions import db
from app.domain.user import User
from app.utils.token_generator import generate_token_str


class AuthToken(db.Model):
    __tablename__ = 'auth_tokens'
    id = db.Column(db.Integer, primary_key=True)
    token_str = db.Column(db.String(255), unique=True, nullable=False, index=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(
        db.Integer,
        db.ForeignKey('users.id', ondelete='CASCADE'),
        nullable=False,
        unique=True,
        index=True
    )

    user = db.relationship(
        'User',
        back_populates='auth_token',
        lazy='joined'
    )

    def __init__(self, user : User):
        self.token_str = generate_token_str()
        self.user = user

    def __repr__(self):
        return f"<AuthToken token={self.token_str!r} user_id={self.user_id}>"
