from app.domain import Role
from app.schemas.base import BaseSchema


class RoleSchema(BaseSchema):
    class Meta:
        model = Role