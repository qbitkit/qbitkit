# Unit test for qbitkit.qasm module
import unittest as __ut__
from os import linesep as __sep__
from qbitkit.qasm import generate as __g__


# TestCase for QASM Generation (qbitkit.qasm.generate)
class TestGeneration(__ut__.TestCase):
    def headers(self):
        # Set expectation of result when running test
        expected_headers = f"""OPENQASM 2.0;{__sep__}include "qelib1.inc";"""
        # Initialize variables
        correct_headers = False
        headers = __g__.headers()
        # Check if headers are what they should be
        if headers == expected_headers:
            correct_headers = True
        else:
            print(f"--> Headers generated are invalid. {__sep__}",
                  f"--> Here's what they should be: {__sep__}'{expected_headers}'",
                  f"--> Here's what we got: {__sep__}'{headers}'")
            correct_headers = False
        self.assertEqual(correct_headers, True)