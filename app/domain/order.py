from app.extensions import db

class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    user_id = db.Column(
        db.Integer,
        db.ForeignKey('users.id', ondelete='CASCADE'),
        nullable=False,
        index=True
    )
    icon_picture_url = db.Column(db.String(255), nullable=True)
    company_name = db.Column(
        db.String(50),
        db.ForeignKey('companies.name', ondelete='SET NULL'),
        nullable=True,
        index=True
    )

    user = db.relationship(
        'User',
        back_populates='orders',
        lazy='joined'
    )

    company = db.relationship(
        'Company',
        back_populates='orders',
        # also explicitly point to the same FK column
        foreign_keys=[company_name],
        # joined‑load parent for quick access
        lazy='joined'
    )