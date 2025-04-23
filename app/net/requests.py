from app.net.net_errors import RequestValidationError

class LoginRequest:
    def __init__(self, request):
        """
        Initializes the LoginRequest with username and password from request data.
        Validates that the required fields are present and properly formatted.

        :param request: Flask request object
        :raises RequestValidationError: If validation fails
        """
        # Check if content type is JSON
        if not request.is_json:
            raise RequestValidationError("Request must be JSON", 415)

        # Get JSON data
        data = request.get_json()

        # Check if data is present
        if not data:
            raise RequestValidationError("Missing request body")

        # Validate required fields
        self.username = data.get('username')
        self.password = data.get('password')

        if not self.username:
            raise RequestValidationError("Username is required")

        if not self.password:
            raise RequestValidationError("Password is required")

        # Optional: Add more validation rules
        if len(self.username) < 4:
            raise RequestValidationError("Username must be at least 4 characters")

        if len(self.password) < 8:
            raise RequestValidationError("Password must be at least 8 characters")


class AuthenticatedRequest:
    def __init__(self, request):
        """
        Initializes and validates the authentication request with a Bearer token.

        :param request: Flask request object
        :raises RequestValidationError: If validation fails
        """
        # Extract authorization header
        auth_header = request.headers.get('Authorization')

        # Validate header exists
        if not auth_header:
            raise RequestValidationError("Authorization header is required", 401)

        # Validate it's a Bearer token
        if not auth_header.startswith('Bearer '):
            raise RequestValidationError("Invalid authorization format - must be Bearer token", 401)

        # Extract token
        self.token = auth_header.split("Bearer ")[1].strip()

        # Validate token is not empty
        if not self.token:
            raise RequestValidationError("Empty token provided", 401)

        # Optional: validate token format (e.g., length, character set)
        if len(self.token) < 10:  # Adjust based on your token requirements
            raise RequestValidationError("Invalid token format", 401)


class GetUserRolesRequest(AuthenticatedRequest):
    def __init__(self, request):
        super().__init__(request)

class GetUsersRequestsRequest(AuthenticatedRequest):
    def __init__(self, request):
        super().__init__(request)

class LogoutRequest(AuthenticatedRequest):
    def __init__(self, request):
        super().__init__(request)