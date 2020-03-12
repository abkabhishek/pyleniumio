# Welcome to Pylenium

The mission here is simple:

> Make the onboarding experience of Selenium more like Cypress.

I teach courses and do trainings for both Selenium and Cypress, but Selenium _feels_ more clunky.

Cypress has done an amazing job of making the testing experience more enjoyable - especially for beginners.

Pylenium looks to bring more Cypress-like bindings for Selenium and Python, so behaviors and names will be the same or similar.

## Get Started

1. Install Pylenium into your Project

    ```bash
    $ pip install pylenium
    ```

2. Create a `test_google.py` file

3. Define a single **pytest fixture** which is your `BeforeEach` and `AfterEach`

```python
import pytest
from pylenium import Pylenium

@pytest.fixture
def py():
    py = Pylenium()
    yield py
    py.quit()
```

4. Write the test below your fixture

```python
def test_google_search(py):
    py.visit('https://google.com')
    py.get('[name="q"]').type('puppies')
    py.get('[name="btnK"]').submit()
    assert 'puppies' in py.title
```

### Install Chromedriver

Everyone handles the install of their drivers differently.

> As of right now, Pylenium expects your chromedriver to be on your PATH.

The easiest way to do this is with `WebDriver Manager`.

1. Install the manager

    ```bash
    $ npm install -g webdriver-manager
    ```

2. Then download the `chromedriver` executable

    ```bash
    $ webdriver-manager update
    ```

### Run the Test

This depends on your IDE, environment and configurations, but you can easily do it from the CLI using:

```bash
$ python -m pytest 
```

YOU'RE ALL SET
