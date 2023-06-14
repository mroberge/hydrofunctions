"""
hydrofunctions.logging
~~~~~~~~~~~~~~~~~~~~~~

This module contains the tools used for internal diagnostic logging.

Logging is disabled by default. Users can start logging by using the
`hf._start_logging()`  function. This will create a file "hydrofunctions_testing.log" in
the main directory. This function also allows users to set the level of severity that
will be logged. The default is to capture all messages, including the lowest level
'DEBUG' messages.

To create log messages within a module, follow these steps:

1. Create a custom logger for the module.
    - Place the statement `logger = logging.getLogger(__name__)` at the top of the module.
    - This will create a custom logger that is named after the module.
    - call the logger like this: logger.info("Hello!")

2. Log a message within your code.
    - Create a message: `msg = "This is the text of the message."`
    - Include the value of important variables
    - There is no need to include the time or name of the module or function. These are included in the standard message format.
    - Decide on a 'level' for the message:
        - DEBUG: this is the lowest level; for tracking ordinary internal values
        - INFO: internal or user events that are working as expected
        - WARNING: situations where back-up procedures are needed, unexpected\
            situations and possibly ordinary exceptions that have been caught
        - ERROR: internal problems that prevent the software from completing an action
        - CRITICAL: serious errors that cause the shutdown of the software
    - Add the message to the log file: `logger.info(msg)`
    - Each level of severity has its own method: .debug(), .info(), .critical(), etc.
    - HydroExceptions such as HydroNoDataError generate their own error logs.
    - It might be useful to log other errors when they are raised.

3. Start the logging system.
    - Logging is off by default.
    - To start logging, call hydrofunctions._start_logging()
    - You can specify the level that will be captured in the log with the `loglevel` parameter.
    - Set level like this: `hf._start_logging('info')`  (Case does not matter)
    - The default is to capture from the lowest level (DEBUG) up
    - Starting the logging system will create a new file "hydrofunctions_testing.log"\
        if it doesn't already exist; if it does, it will add new messages at the\
        bottom under a start up message to the 'root' module.

4. Read the log.
    - The file, "hydrofunctions_testing.log" will appear in the root directory
    - All messages from hydrofunctions will have the following:
        - timestamp
        - name of logger: 'root' for the start message, all others should be named for\
            the module that creates the message
        - levelname: the level of the message ('DEBUG', 'INFO', etc)
        - funcName: the name of the function that sent the message to the log
        - message: the message generated by the logger function: `logger.info("Hello!")`
    - The first message created by the `hf._start_logging()` will be from 'root'
    - Messages from dependencies will be captured too.

-----
"""
import logging


def _start_logging(loglevel="DEBUG"):
    """Create a log file if it doesn't exist and start logging messages.

    Args:
        loglevel (str):
            The level of message that should be captured in the log. Valid values
            are (from lowest to highest):
            - 'DEBUG': (default) Detailed information, typically of interest only when diagnosing problems.
            - 'INFO': Confirmation that things are working as expected.
            - 'WARNING': An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.
            - 'ERROR': Due to a more serious problem, the software has not been able to perform some function.
            - 'CRITICAL': A serious error, indicating that the program itself may be unable to continue running.

    Raises:
        ValueError: if loglevel does not correspond to one of the five valid levels
    """
    # This code is from Vinay Sajip in the Python.org logging tutorial.
    # https://docs.python.org/3/howto/logging.html
    numeric_level = getattr(logging, loglevel.upper(), None)
    if not isinstance(numeric_level, int):
        raise ValueError("Invalid log level: %s" % loglevel)
    format = "%(asctime)s — %(name)s — %(levelname)s — %(funcName)s — %(message)s"
    logging.basicConfig(
        filename="hydrofunctions.log",
        level=numeric_level,
        format=format,
    )
    logging.captureWarnings(True)
    logging.info(
        f"Logging started. Messages at the {loglevel} level and above will be captured.\nLine format is: {format}"
    )
