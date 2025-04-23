class AuthenticationError(Exception):
    """Exception raised when authentication fails due to invalid credentials or tokens."""

    def __init__(self, message="Authentication failed.", status_code=401):
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)