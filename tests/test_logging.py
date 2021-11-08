"""
test_logging
------------

Tests for the `logging` module.
"""
import logging
from unittest import mock
import unittest
from unittest import mock
import warnings

import hydrofunctions as hf

hf._start_logging()


class TestLogging(unittest.TestCase):
    """Test the hydrofunctions logging system.

    test the following:
        Is logging off by default?
        There should be no files generated if logging is off
        The file "hydrofunctions.log" should be generated when logging is started
        ✔HydroExceptions should generate a log message
        ✔loggers should be able to post a message to the log
        ✔hf._start_logging() calls logging.basicConfig() properly
        ✔warning messages should be logged.

    """

    def test_logging_message(self):
        logger = logging.getLogger(__name__)
        expected_message = "test_logging"

        with self.assertLogs() as captured:
            logger.info(expected_message)
            expected_level = logging.INFO

        actual_n_of_messages = len(captured.records)
        actual_message = captured.records[0].getMessage()
        actual_level = captured.records[0].levelno
        # The actual_log_line is hard to test against until you set the output format.
        # actual_log_line = captured.output
        # print(f"***********/n/n/ncaptured log line: /n{actual_log_line}/n/n/n***********/n")
        self.assertEqual(actual_n_of_messages, 1, "There should only be one message")
        self.assertEqual(actual_message, expected_message, "Wrong message was logged")
        self.assertEqual(actual_level, expected_level, "Message logged at wrong level")

    def test_logging_HydroExceptions_log_message(self):
        expected_message = "test_logging_HydroExceptions_log_msg"
        with self.assertLogs() as captured:
            try:
                raise hf.HydroNoDataError(expected_message)
            except hf.HydroNoDataError:
                pass

        expected_level = logging.ERROR
        actual_level = captured.records[0].levelno
        self.assertEqual(actual_level, expected_level, "Message logged at wrong level")
        actual_message = captured.records[0].getMessage()
        self.assertEqual(actual_message, expected_message, "Wrong message was logged")

    @mock.patch("logging.basicConfig")
    def test_logging_start_logging_logs_warnings(self, mock_config):
        # logger = logging.getLogger(__name__)
        expected_message = "Test that warnings are logged."
        # hf._start_logging()
        # mock_config.assert_called()

        with self.assertLogs() as captured:
            warnings.warn(expected_message, hf.HydroUserWarning)
        actual_message = captured.records[0].getMessage()
        # warning logs have their own formatting that contains the actual_message.
        self.assertIn(
            expected_message,
            actual_message,
            f"Wrong message was logged. Actual: {actual_message}",
        )

    @mock.patch("logging.basicConfig")
    def test_logging_start_logging_calls_basicConfig(self, mock_config):
        expected_level = logging.ERROR
        hf._start_logging("error")
        expected_filename = "hydrofunctions.log"

        # This is a bit brittle: the format is not set in stone.
        # expected format = "%(asctime)s — %(name)s — %(levelname)s — %(funcName)s — %(message)s"
        expected_format = mock.ANY
        # .assert_called_once_with() passes in pytest, but fails in unittest- called 3 times.
        # pytest prevents dependencies from calling logging.basicConfig(); unittest doesn't
        mock_config.assert_any_call(
            filename=expected_filename, level=expected_level, format=expected_format
        )
