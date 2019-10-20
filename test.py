from euiupdate.helpers import get_logger, NullHandler
from logging import Logger


class TestLoggingHelper:
    def __init__(self):
        self.logger = get_logger(__name__)

    def returns_logger(self):
        assert isinstance(self.logger, Logger)

    def has_null_handler(self):
        assert any((h for h in self.logger.handlers if isinstance(h, NullHandler)))
