from app.domain import User
from app.schemas.base import BaseSchema


class UserSchema(BaseSchema):
    class Meta:
        model = User