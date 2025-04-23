from app.dao.auth_token_dao import AuthTokenDao
from app.dao.user_dao import UserDAO
from app.net.requests import GetUserRolesRequest, GetUsersRequestsRequest, LogoutRequest
from app.services.authenticated_service import AuthenticatedService

class UserService(AuthenticatedService):
    def __init__(self):
        super().__init__()
        self.user_dao = UserDAO()
        self.auth_token_dao = AuthTokenDao()

    def get_user_roles(self, request : GetUserRolesRequest):
        user = self.authenticate(request.token)
        roles = self.user_dao.get_user_roles(user)
        return roles

    def get_user_orders(self, request : GetUsersRequestsRequest):
        user = self.authenticate(request.token)
        orders = self.user_dao.get_user_orders(user)
        return orders

    def logout(self, request : LogoutRequest):
        user = self.authenticate(request.token)
        self.auth_token_dao.logout(user)
        return {
            "message": f"User {user.username} logged out successfully!"
        }




