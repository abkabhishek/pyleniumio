import json
import os

import pytest
from pylenium import Pylenium
from pylenium.config import PyleniumConfig


@pytest.fixture(scope='session')
def workspace_root():
    """ Your project's root directory (aka Workspace Root) """
    return os.path.dirname(os.path.abspath(__file__))


@pytest.fixture
def py_config(workspace_root):
    """ Initialize a PyleniumConfig for each test using pylenium.json """
    with open(f'{workspace_root}/pylenium.json') as file:
        _json = json.load(file)
    return PyleniumConfig(**_json)


@pytest.fixture
def py(py_config):
    """ Initialize a Pylenium driver for each test.

    Pass in this `py` fixture into the test function.

    Examples:
        def test_go_to_google(py):
            py.visit('https://google.com')
            assert 'Google' in py.title
    """
    py = Pylenium(py_config)
    yield py
    py.quit()


@pytest.fixture(scope='session')
def py_factory():
    """ Pylenium Fixture as a Factory. """
    def _pylenium(config: PyleniumConfig):
        py = Pylenium(config)
        return py
    return _pylenium


@pytest.fixture(scope='module')
def driver(py_factory):
    """ This Project's integration testing fixture. """
    # setup config
    with open('../pylenium/pylenium.json') as file:
        _json = json.load(file)
    config =  PyleniumConfig(**_json)

    # init driver
    py = py_factory(config)
    py.visit('https://deckshop.pro')
    yield py
    py.quit()
