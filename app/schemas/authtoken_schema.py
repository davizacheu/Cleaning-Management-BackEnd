from app.domain import AuthToken
from app.schemas.base import BaseSchema


class AuthTokenSchema(BaseSchema):
    class Meta:
        model = AuthToken