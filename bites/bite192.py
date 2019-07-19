import logging
from typing import Callable

logger = logging.getLogger("pybites_logger")

DEBUG = logger.debug
INFO = logger.info
WARNING = logger.warning
ERROR = logger.error
CRITICAL = logger.critical


def log_it(level: Callable, msg: str) -> None:
    level(msg)


if __name__ == "__main__":
    log_it(DEBUG, "This is a debug message.")
    log_it(INFO, "This is an info message.")
    log_it(WARNING, "This is a warning message.")
    log_it(ERROR, "This is an error message.")
    log_it(CRITICAL, "This is a critical message.")


# tests
# import logging

import pytest

# from log_it import CRITICAL, DEBUG, ERROR, INFO, WARNING, log_it

LOG_LEVEL = {
    "debug": DEBUG,
    "info": INFO,
    "warning": WARNING,
    "error": ERROR,
    "critical": CRITICAL,
}


@pytest.mark.parametrize(
    "msg, level",
    [
        ("This is a debug message", "debug"),
        ("This is an info message", "info"),
        ("This is a warning message", "warning"),
        ("This is an error message", "error"),
        ("This is a critical message", "critical"),
    ],
)
def test_log_it(msg, level, caplog):
    caplog.set_level(logging.DEBUG)
    log_it(LOG_LEVEL[level], msg)
    assert len(caplog.records) == 1
    for record in caplog.records:
        assert record.levelname == level.upper()
        assert record.message == msg
        assert record.name == "pybites_logger"


def test_wrong_log_level(caplog):
    msg = "This is a warning message"
    caplog.set_level(logging.ERROR)
    log_it(WARNING, msg)
    assert len(caplog.records) == 0

    caplog.set_level(logging.ERROR)
    msg = "This is an error message"
    log_it(ERROR, msg)
    assert len(caplog.records) == 1
    for record in caplog.records:
        assert record.levelname == "ERROR"
        assert record.message == msg
        assert record.name == "pybites_logger"