import logging
from typing import Any

LOG_SEPARATOR = '::'


class ContextLogger:
    def __init__(self, name: str) -> None:
        self.logger = logging.getLogger(name)
        self.context: dict[str, Any] = {}

        self.add_context('module', name)

    @staticmethod
    def setup_logging() -> None:
        logging.basicConfig(
            format=f'%(levelname)s{LOG_SEPARATOR}%(message)s',
            level=logging.DEBUG,
        )

    def add_context(self, key, value) -> None:
        if key in self.context:
            self.warning(
                f'Setting existing key in context, key={key} with value={self.context[key]} -> {value}'
            )

        self.context[key] = value

    def _add_context_to_msg(self, msg: str) -> str:
        return f'{self.context}{LOG_SEPARATOR}{msg}'

    def debug(self, msg: str, **kwargs) -> None:
        context_msg = self._add_context_to_msg(msg)
        self.logger.debug(context_msg, **kwargs)

    def info(self, msg: str, **kwargs) -> None:
        context_msg = self._add_context_to_msg(msg)
        self.logger.info(context_msg, **kwargs)

    def warning(self, msg: str, **kwargs) -> None:
        context_msg = self._add_context_to_msg(msg)
        self.logger.warning(context_msg, **kwargs)

    def error(self, msg: str, **kwargs) -> None:
        context_msg = self._add_context_to_msg(msg)
        self.logger.error(context_msg, **kwargs)
