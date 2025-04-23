from app.domain import Company
from app.extensions import db
from app.domain.order import Order
from app.domain.role import Role
from app.domain.user import User


class UserDAO:
    def __init__(self):
        self.session = db.session

    def validate_credentials(self, username, password) -> User | None:
        return User.query.filter_by(username=username, password=password).first()

    def get_user_roles(self, user: User) -> list[tuple[Role, Company]]:
        return [(role, role.company) for role in user.roles]

    def get_user_orders(self, user : User) -> list[tuple[Order, Company | None]]:
        return [(order, order.company) for order in user.orders]