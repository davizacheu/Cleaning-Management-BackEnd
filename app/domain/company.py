from app.extensions import db


class Company(db.Model):
    __tablename__ = 'companies'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    address = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), unique=False, nullable=False)
    logo_url = db.Column(db.String(255), nullable=True)

    roles = db.relationship(
        'Role',
        back_populates='company',
        lazy='selectin',
        passive_deletes=True,
        single_parent=True,
        cascade='all, delete-orphan',
        order_by='Role.role_title'
    )

    orders = db.relationship(
        'Order',
        back_populates='company',
        foreign_keys='[Order.company_name]',
        primaryjoin='Company.name == Order.company_name',
        lazy='selectin',
        cascade='save-update, merge',
        single_parent=True,
        passive_deletes=True
    )
