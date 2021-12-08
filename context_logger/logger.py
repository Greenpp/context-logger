import logging
from typing import Any, Optional

LOG_SEPARATOR = '::'
NAME_KEY = 'name'
DEFAULT_NAME = 'default'


class ContextLogger:
    def __init__(
        self,
        name: str = DEFAULT_NAME,
        context: Optional[dict] = None,
    ) -> None:
        """Creates a new instance of ContextLogger.

        If another logger is passed, its context is used as the base. Name is replaced on creation.

        Args:
            name (str): Name of the logger
            from_logger (Optional[dict]): Optional context which should be used. Defaults to None.
        """
        self.logger = logging.getLogger(name)

        if context is None:
            self.context: dict[str, Any] = {}
        else:
            self.context = context.copy()
        self.add_context(NAME_KEY, name, warn_on_existing=False)

    @staticmethod
    def setup_logging(level=logging.INFO) -> None:
        """Configures global options for logging format and level.

        Args:
            level ([type], optional): Default level of logging. Defaults to INFO.
        """
        logging.basicConfig(
            format=f'%(levelname)s{LOG_SEPARATOR}%(message)s',
            level=level,
        )

    def add_context(
        self,
        key: str,
        value: Any,
        warn_on_existing: bool = True,
    ) -> None:
        """Adds new value to the context.

        Args:
            key (str): Value name in the context. Must be unique.
            value (Any): Value added to the context.
            warn_on_existing (bool, optional): If warning should be logged if the key already exists in the context. Defaults to True.
        """
        if warn_on_existing and key in self.context:
            self.warning(
                f'Setting existing key in context, key={key} with value={self.context[key]} -> {value}'
            )

        self.context[key] = value

    def _add_context_to_msg(self, msg: str) -> str:
        return f'{self.context}{LOG_SEPARATOR}{msg}'

    def debug(self, msg: str, **kwargs) -> None:
        """Logs debug output.

        Args:
            msg (str): Log message.
        """
        context_msg = self._add_context_to_msg(msg)
        self.logger.debug(context_msg, **kwargs)

    def info(self, msg: str, **kwargs) -> None:
        """Logs info output.

        Args:
            msg (str): Log message.
        """
        context_msg = self._add_context_to_msg(msg)
        self.logger.info(context_msg, **kwargs)

    def warning(self, msg: str, **kwargs) -> None:
        """Logs warning output.

        Args:
            msg (str): Log message.
        """
        context_msg = self._add_context_to_msg(msg)
        self.logger.warning(context_msg, **kwargs)

    def error(self, msg: str, **kwargs) -> None:
        """Logs error output.

        Args:
            msg (str): Log message.
        """
        context_msg = self._add_context_to_msg(msg)
        self.logger.error(context_msg, **kwargs)

    def critical(self, msg: str, **kwargs):
        """ogs critical output.

        Args:
            msg (str): Log message.
        """
        context_msg = self._add_context_to_msg(msg)
        self.logger.critical(context_msg, **kwargs)
