# Python Context Logger

Simple wrapper for python logger allowing for inclusion of a context in logs.

## Example

```python
# main.py
from context_logger import ContextLogger

ContextLogger.setup_logging()
```

```python
# module.py
from context_logger import ContextLogger

logger = ContextLogger(__name__)

logger.add_context('important property', 42)
logger.info('Info log')

# INFO::{'name': '__module__', 'important property': 42}::Info log
```
