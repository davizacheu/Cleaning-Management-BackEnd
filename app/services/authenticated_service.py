from app.dao.auth_token_dao import AuthTokenDao
from app.domain import User
from app.net.requests import AuthenticatedRequest
from app.services.service_errors import AuthenticationError


class AuthenticatedService:
    def __init__(self):
        self.auth_token_dao = AuthTokenDao()

    def authenticate(self, request : AuthenticatedRequest) -> User:
        user = self.auth_token_dao.validate_token(request)
        if user:
            return user
        raise AuthenticationError("Invalid or expired token")
