from sqlalchemy.dialects.postgresql import JSONB
from app.extensions import db

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    company_id = db.Column(
        db.Integer,
        db.ForeignKey('companies.id', ondelete='CASCADE'),
        nullable=False,
        index=True
    )
    role_title = db.Column(db.String(50), nullable=False, default='Owner')
    user_id = db.Column(
        db.Integer,
        db.ForeignKey('users.id', ondelete='SET NULL'),
        nullable=True,
        index=True
    )
    personnel_name = db.Column(db.String(50), unique=True, nullable=True)
    contact_data = db.Column(JSONB, nullable=True, default=dict)
    profile_picture_url = db.Column(db.String(255), nullable=True)

    company = db.relationship(
        'Company',
        back_populates='roles',
        lazy='joined'
    )

    user = db.relationship(
        'User',
        back_populates='roles',
        lazy='joined'
    )

    invitations = db.relationship(
        'RoleInvitation',
        back_populates='role',
        cascade='all, delete-orphan',
        lazy='dynamic'
    )

    def __repr__(self):
        return f'<Role {self.role_title} at {self.company_id}>'
