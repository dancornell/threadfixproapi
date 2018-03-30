import sys
import pytest


def f(name):
    print("Hello {}".format(name))


def test_f(capfd):
    f("ThreadFixProApi")

    out, err = capfd.readouterr()
    assert out == "Hello ThreadFixProApi\n"
