from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse
from starlette.requests import Request
from typing import Callable
import json

class ResponseWrapperMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next: Callable):
        response = await call_next(request)

        if response.status_code >= 400:
            return response

        if not response.media_type or "application/json" not in response.media_type:
            return response

        original_body = b""
        async for chunk in response.body_iterator:
            original_body += chunk

        response.body_iterator = iter([original_body])

        try:
            data = json.loads(original_body)
        except Exception:
            return response

        wrapped_response = {
            "success": True,
            "data": data,
        }
        return JSONResponse(content=wrapped_response, status_code=response.status_code)
