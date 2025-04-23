from app.domain import RoleInvitation
from app.schemas.base import BaseSchema

class RoleInvitationSchema(BaseSchema):
    class Meta:
        model = RoleInvitation