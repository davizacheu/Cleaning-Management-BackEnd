from datetime import datetime, timedelta
from app.extensions import db
from app.domain.authtoken import AuthToken
from app.domain.user import User


class AuthTokenDao:
    def __init__(self):
        self.session = db.session
        # how long tokens stay valid
        self._ttl = timedelta(hours=1)

    def validate_token(self, token_str) -> User | None:
        authtoken = AuthToken.query.filter_by(token_str=token_str).first()

        if not authtoken:
            return None

        if authtoken.created_at + self._ttl < datetime.utcnow():
            # token expired: clean up and reject
            self.session.delete(authtoken)
            self.session.commit()
            return None

        return authtoken.user

    def create_token(self, user: User) -> str:
        authtoken = AuthToken(user)
        self.session.add(authtoken)
        self.session.commit()
        return authtoken.token_str

    def logout(self, user : User):
        self.session.delete(user.auth_token)
        self.session.commit()
