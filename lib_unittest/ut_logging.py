# Standard library
import sys
import os
import logging
from logging import handlers
# 3rd party library
import structlog
# Local library
from lib_unittest import globals as utg


# Custom structlog processor
def _custom_processor(_, __, eventdict: dict) -> str:
    # Builds the message if there is no other key-value pairs in the message
    msg = f'[{eventdict.get("timestamp")}][{eventdict.get("logger"):^15}]{eventdict.get("level").upper():>8}: {eventdict.get("event")}'
    # This next logic is used to justify keys if we have longy boi names
    total_space = max([len(x) for x in eventdict.keys()])
    # We iterate over the eventdict
    for key, val in eventdict.items():
        # If other values than the ones we expect appear
        if key not in ['event', 'logger', 'level', 'timestamp']:
            # We add them to the next line (the whole logic here is just to justify stuff)
            msg += (
                f'\n'
                f'{(len(eventdict.get("timestamp")) + 2) * " "}'  # timestamp length + '[' + ']'
                f'{(2 + 15) * " "}'                               # logname length (justified to 15, so flat 15) + '[' + ']'
                f'{" " * 8}'                                      # log level length (justified to 8, so flat 8)
                f'| < {key:>{total_space}} : {val} >'
            )  # Keep in mind this is still one line string, just broken up into multiple lines in code for clarity
    return msg


# Function here in case we want to do some fancy stuff later down the line
def get_logger(log_name='') -> structlog.types.WrappedLogger:
    return structlog.get_logger(log_name)


log_path = os.path.join(utg.root_dir, 'UnitTest.log')  # ./UnitTest.log

logging.basicConfig(
    format='%(message)s',
    level=logging.DEBUG,
)

# Adds handlers for logging to console and to file.
logging.root.handlers = [
    logging.StreamHandler(sys.stdout),
    handlers.RotatingFileHandler(log_path, maxBytes=(1000000 * 5))  # 5Mb rollover
]

structlog.configure_once(
    processors=[
        structlog.stdlib.add_logger_name,  # Takes basic config's log name
        structlog.stdlib.add_log_level,    # From basic config
        structlog.processors.TimeStamper(fmt='%Y-%m-%d %H:%M:%S', utc=False),  # Adds timestamp, very cool (local time)
        structlog.processors.StackInfoRenderer(),
        structlog.processors.format_exc_info,
        structlog.processors.UnicodeDecoder(),
        _custom_processor  # Replace with structlog.dev.ConsoleRenderer() if you don't like the custom one
    ],
    context_class=dict,
    logger_factory=structlog.stdlib.LoggerFactory(),
    wrapper_class=structlog.stdlib.BoundLogger,  # type: ignore
    cache_logger_on_first_use=True,
)

utg.main_log = get_logger()
