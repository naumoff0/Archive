import os
import string
import sys
import unittest
from contextlib import contextmanager
from io import StringIO
from unittest.mock import patch

import termcolor

base_dir = os.getcwd().replace("\\tests", "")
sys.path.append(base_dir)
sys.path.append(base_dir + "\\game")
import ui


def capture_output(function, *args):
    """ captures the printed output from a function """
    @contextmanager
    def captured_output():
        new_out, new_err = StringIO(), StringIO()
        old_out, old_err = sys.stdout, sys.stderr

        try:
            sys.stdout, sys.stderr = new_out, new_err
            yield sys.stdout, sys.stderr
        finally:
            sys.stdout, sys.stderr = old_out, old_err

    with captured_output() as (out, err):
        function(*args)
        if err.errors:
           return False

    return out.getvalue()


class TestMenu(unittest.TestCase):
    """ ui testing """
    def setUp(self):
        self.test_menu = ui.Menu("Test Menu")

    def test_add(self):
        def function(*args):
            return

        self.test_menu.add(string.ascii_letters)
        self.test_menu.add(string.ascii_lowercase, function)
        self.test_menu.add(string.ascii_uppercase, function, 1, "2", 3.01)

        # ensure that menu option has matching description
        self.assertEqual(string.ascii_letters, self.test_menu.options["1"][0])

        self.assertEqual(string.ascii_lowercase, self.test_menu.options["2"][0])
        # ensure menu option has matching function
        self.assertEqual(function, self.test_menu.options["2"][1])

        self.assertEqual(string.ascii_uppercase, self.test_menu.options["3"][0])
        self.assertEqual(function, self.test_menu.options["3"][1])
        # ensure menu option has matching arguments
        self.assertEqual((1, "2", 3.01), self.test_menu.options["3"][2])

    def test_display(self):
        def function(arg=None):
            return arg

        self.test_menu.add(string.ascii_letters)
        self.test_menu.add(string.ascii_lowercase, function)
        self.test_menu.add(string.ascii_uppercase, function, string.ascii_letters)


def ui_suite():
    suite = unittest.TestSuite()
    suite.addTest(TestMenu("test_add"))
    suite.addTest(TestMenu("test_display"))

    return suite

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(ui_suite())
