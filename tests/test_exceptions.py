"""
test_exceptions
----------------------------------

Tests for the `exceptions` module.
"""
import unittest
import warnings

from hydrofunctions import exceptions


def raiseHydroNoDataError():
    raise exceptions.HydroNoDataError("test_exceptions.py raiseHydroNoDataError() ")


class TestExceptions(unittest.TestCase):
    def test_exceptions_HydroNoDataError_can_be_raised(self):
        self.assertRaises(exceptions.HydroNoDataError, raiseHydroNoDataError)

    def test_exceptions_HydroNoDataError_can_be_caught(self):
        actual = False
        try:
            raiseHydroNoDataError()
        except exceptions.HydroNoDataError as err:
            actual = True
        self.assertTrue(
            actual, "The HydroNoDataError should have been caught, but wasn't."
        )


class TestWarnings(unittest.TestCase):
    @unittest.skip(
        "assertWarns errors on Linux. See https://bugs.python.org/issue29620"
    )
    def test_exceptions_HydroUserWarning_can_be_called(self):
        with self.assertWarns(exceptions.HydroUserWarning):
            warnings.warn("test warning message", exceptions.HydroUserWarning)


if __name__ == "__main__":
    unittest.main(verbosity=2)
