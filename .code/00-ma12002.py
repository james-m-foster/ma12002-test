"""Jupyter setup for MA12002"""

# Add code directory to path to pick up model solutions
import sys
import os

sys.path.insert(0, os.path.expanduser("~") + "/ma12002/.code/")

# Make ipytest available
import ipytest

ipytest.autoconfig(raise_on_error=True)

def run_tests():
    """"Run ipytest on all tests in the current notebook"""
    return ipytest.run(
        "-v", module=__import__("__main__")
    )