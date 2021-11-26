import pytest
from context_logger import __version__
from context_logger.logger import DEFAULT_NAME, NAME_KEY, ContextLogger


def test_version():
    assert __version__ == '0.1.0'


def test_default_name():
    cl = ContextLogger()

    assert cl.context[NAME_KEY] == DEFAULT_NAME


def test_module_name():
    custom_name = 'test'

    cl = ContextLogger(custom_name)

    assert cl.context[NAME_KEY] == custom_name


@pytest.mark.parametrize(
    ['cx_key', 'cx_value'],
    [
        ('key', 42),
        ('key', 0.5),
        ('key', 'test'),
        ('key', {'test': 42}),
    ],
)
def test_context_addition(cx_key, cx_value):
    cl = ContextLogger()

    cl.add_context(cx_key, cx_value)

    assert cl.context[cx_key] == cx_value


def test_key_override(caplog):
    cl = ContextLogger()
    cx_key = 'test'

    cl.add_context(cx_key, 42)
    assert not caplog.text

    cl.add_context(cx_key, 0)
    assert 'WARN' in caplog.text


def test_inherit_context(caplog):
    cl = ContextLogger()
    cx_key = 'test'
    cx_val = 42
    cx_new_name = 'new'
    cx_new_key = 'test2'
    cx_new_val = 0

    cl.add_context(cx_key, cx_val)
    cl2 = ContextLogger(cx_new_name, cl)

    assert not caplog.text

    assert cl.context[NAME_KEY] == DEFAULT_NAME
    assert cl2.context[NAME_KEY] == cx_new_name

    cl2.add_context(cx_new_key, cx_new_val)

    assert cl2.context[cx_new_key] == cx_new_val
    assert cx_new_key not in cl.context
