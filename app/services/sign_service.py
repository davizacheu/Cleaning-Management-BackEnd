from app.dao.auth_token_dao import AuthTokenDao
from app.dao.user_dao import UserDAO
from app.net.requests import LoginRequest

class SignService:
    def __init__(self):
        self.user_dao = UserDAO()
        self.auth_token_dao = AuthTokenDao()

    def login(self, request : LoginRequest):
        username = request.username
        password = request.password

        user = self.user_dao.validate_credentials(username, password)
        if user:
            token_str = self.auth_token_dao.create_token(user)
            return {
                "message": f"User {username} logged in successfully!",
                "auth_token": token_str
            }
        return None