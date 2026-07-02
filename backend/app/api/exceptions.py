class ApiException(Exception):
    def __init__(self, status_code: int, message: str):
        self.status_code = status_code
        self.message = message

class NotFound(ApiException):
    def __init__(self, message: str = "Resource not found"):
        super().__init__(404, message)

class BadRequest(ApiException):
    def __init__(self, message: str = "Bad request"):
        super().__init__(400, message)

class Unauthorized(ApiException):
    def __init__(self, message: str = "Unauthorized"):
        super().__init__(401, message)

class Forbidden(ApiException):
    def __init__(self, message: str = "Forbidden"):
        super().__init__(403, message)
