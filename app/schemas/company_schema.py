from app.domain import Company
from app.schemas.base import BaseSchema


class CompanySchema(BaseSchema):
    class Meta:
        model = Company