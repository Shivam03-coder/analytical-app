from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse, Response
from starlette.requests import Request
from typing import Callable, Dict, Any
import json
import logging

logger = logging.getLogger(__name__)

class ResponseWrapperMiddleware(BaseHTTPMiddleware):
    """Middleware to wrap all successful JSON responses in a standard format."""
    
    async def dispatch(self, request: Request, call_next: Callable) -> Response:
        response = await call_next(request)
        logger.debug(f"Original response: {response.status_code}, {response.headers}")
        
        if response.status_code >= 400:
            logger.debug("Skipping wrapping for error response")
            return response
            
        content_type: str = response.headers.get("content-type", "")
        if not content_type.startswith("application/json"):
            logger.debug(f"Skipping non-JSON response (Content-Type: {content_type})")
            return response
            
        try:
            body: bytes = await response.body()
            original_data: Any = json.loads(body.decode())
            logger.debug(f"Successfully parsed JSON data: {original_data}")
        except json.JSONDecodeError as e:
            logger.warning(f"Failed to decode JSON: {str(e)}")
            return response
        except Exception as e:
            logger.error(f"Unexpected error parsing response: {str(e)}", exc_info=True)
            return response
            
        wrapped_response: Dict[str, Any] = {
            "success": True,
            "data": original_data,
            "meta": {  
                "status": response.status_code,
                "endpoint": str(request.url.path)
            }
        }
        
        return JSONResponse(
            content=wrapped_response,
            status_code=response.status_code,
            headers=dict(response.headers)  
        )