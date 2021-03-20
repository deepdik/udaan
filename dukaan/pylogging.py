"""
To use logging:
    from . import pylogging

    pylogging.logger.info("Test info")
    pylogging.logger.warnign("Test warnign")
    pylogging.logger.error("Test error")

    pylogging.logger_info_with_request(request, data)
    pylogging.logger_info(data)
"""
import os
import logging
from django.conf import settings

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

log_path = os.path.join(settings.BASE_DIR, 'tmp/logs/project.log')

## create a file handler
handler = logging.FileHandler(log_path)
# handler.setLevel(logging.INFO)

## create a logging format
# formatter = logging.Formatter('[%(asctime)s] - name=%(name)s - level=%(levelname)s - Msg=%(message)s')
formatter = logging.Formatter('[%(asctime)s] - Msg=%(message)s')
handler.setFormatter(formatter)

logger.addHandler(handler)


def logger_info_with_request(request, data):
    if getattr(settings, 'PY_LOGGING', settings.DEBUG):
        user_agent = request.META.get('HTTP_USER_AGENT')
        content_type = request.META.get('CONTENT_TYPE', '')

        log_msg = "{api} - {content_type} - {user_agent}\n {data}".format(
            api=request.path,
            content_type=content_type,
            user_agent=user_agent,
            data=data)
        logger.info(log_msg)
    else:
        pass


def logger_info(data):
    """
    """
    if getattr(settings, 'PY_LOGGING', settings.DEBUG):
        log_msg = "{data}".format(
            data=data)
        logger.info(log_msg)
        print(log_msg)
    else:
        pass
