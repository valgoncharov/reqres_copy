import time
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from .exceptions import RateLimitExceeded
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class RequestLoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()

        # Log request
        logger.info(f"Request: {request.method} {request.url}")

        response = await call_next(request)

        # Calculate processing time
        process_time = time.time() - start_time

        # Log response
        logger.info(
            f"Response: {request.method} {request.url} - Status: {response.status_code} - Time: {process_time:.3f}s"
        )

        return response


class RateLimitMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, requests_per_minute: int = 60):
        super().__init__(app)
        self.requests_per_minute = requests_per_minute
        self.requests = {}

    async def dispatch(self, request: Request, call_next):
        client_ip = request.client.host
        current_time = time.time()

        # Clean up old requests
        self.requests = {
            ip: times for ip, times in self.requests.items()
            if any(t > current_time - 60 for t in times)
        }

        # Get request times for this IP
        request_times = self.requests.get(client_ip, [])
        request_times = [t for t in request_times if t > current_time - 60]

        if len(request_times) >= self.requests_per_minute:
            raise RateLimitExceeded()

        # Add current request
        request_times.append(current_time)
        self.requests[client_ip] = request_times

        return await call_next(request)
