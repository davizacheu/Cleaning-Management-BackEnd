from datetime import datetime
from app.extensions import db

class RoleInvitation(db.Model):
    __tablename__ = 'role_invitations'

    role_id = db.Column(
        db.Integer,
        db.ForeignKey('roles.id', ondelete='CASCADE'),
        primary_key=True
    )
    user_id = db.Column(
        db.Integer,
        db.ForeignKey('users.id', ondelete='CASCADE'),
        primary_key=True
    )
    accepted = db.Column(db.Boolean, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    responded_at = db.Column(db.DateTime, nullable=True)

    # relationships back to Role and User
    role = db.relationship('Role', back_populates='invitations')
    user = db.relationship('User', back_populates='role_invitations')

    def __repr__(self):
        return (
            f"<RoleInvitation "
            f"role={self.role_id} user={self.user_id} "
            f"accepted={self.accepted}>"
        )