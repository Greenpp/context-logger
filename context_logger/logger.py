import logging
from typing import Any, Optional

LOG_SEPARATOR = '::'
MODULE_KEY = 'module'


class ContextLogger:
    def __init__(self, name: str) -> None:
        self.logger = logging.getLogger(name)

        if context is None:
            self.context: dict[str, Any] = {}
        else:
            self.context = context.copy()
        self.add_context(MODULE_KEY, name, warn_on_existing=False)

    @staticmethod
    def setup_logging(level=logging.INFO) -> None:
        logging.basicConfig(
            format=f'%(levelname)s{LOG_SEPARATOR}%(message)s',
            level=level,
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
