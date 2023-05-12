from typing import Any, Optional, Dict

from fastapi import HTTPException


class BaseError(HTTPException):
    def __init__(
        self,
        status_code: int = 500,
        detail: Any = None,
        headers: Optional[Dict[str, Any]] = None,
    ) -> None:
        super().__init__(status_code=status_code, detail=detail, headers=headers)


class ServerError(BaseError):
    status_code = 500
    detail = "Server Error"


class AuthenticationError(BaseError):
    status_code = 401
    detail = "Authentication Error"
