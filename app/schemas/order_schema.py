from app.domain import Order
from app.schemas.base import BaseSchema


class OrderSchema(BaseSchema):
    class Meta:
        model = Order