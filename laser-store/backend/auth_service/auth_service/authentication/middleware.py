import logging
from threading import local
from django.utils.deprecation import MiddlewareMixin
from django.conf import settings


_thread_locals = local()
logger = logging.getLogger('auth')


class LoggingMiddleware(MiddlewareMixin):
    def process_request(self, request):
        _thread_locals.request=request
        logger.info('Request started', extra={
            'user': getattr(request.user, 'id', None),
            'path': request.path,
            'method': request.method,
            'service_name': 'auth_service'
        })
        
    def process_response(self, request, response):
        logger.info("Request completed", extra={
            'status_code': response.status_code,
            'content_length': len(response.content),
            'service_name': 'auth_service'
        })
        return response
        
class RequestContextFilter(logging.Filter):
    def filter(self, record):
        request = getattr(_thread_locals, 'request', None)
        if request:
            record.username = getattr(request.user, 'email', 'anonymous')
            record.service_name = settings.SERVICE_NAME
        else:
            record.username = 'system'
            record.service_name = settings.SERVICE_NAME
        return True