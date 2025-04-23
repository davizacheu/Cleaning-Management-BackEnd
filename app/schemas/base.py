# app/schemas/base.py
from app.extensions import ma


class BaseSchema(ma.SQLAlchemyAutoSchema):
    """Shared Meta options for all model schemas."""
    class Meta:
        include_fk = True  # include foreign‐key fields by default
