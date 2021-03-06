import pytest


def test_element_with_no_siblings(py):
    py.visit('https://deckshop.pro')
    elements = py.get("a[href='/spy/']").siblings()
    assert elements.is_empty()


def test_element_parent_and_siblings(py):
    py.visit('https://deckshop.pro')
    parent = py.get("a.nav-link[href='/spy/']").parent()
    assert parent.tag_name == 'li'
    assert parent.siblings().length == 8


def test_element_text(py):
    py.visit('https://deckshop.pro')
    assert py.contains('More info').should().have_text('More info')


def test_find_in_element_context(py):
    py.visit('https://deckshop.pro')
    headers = py.find('h5')
    assert headers[1].get('a').should().contain_text('Royal')


def test_input_type_and_get_value(py):
    py.visit('https://deckshop.pro')
    search_field = py.get('#smartSearch')
    assert search_field.type('golem').should().have_value('golem')
    assert search_field.clear().should().have_value('')


def test_children(py):
    py.visit('https://deckshop.pro')
    first_row_of_cards_in_deck = py.get("[href*='/deck/detail/'] > span").children()
    assert first_row_of_cards_in_deck.length == 4


def test_forced_click(py):
    py.visit('https://amazon.com')
    # without forcing, this raises ElementNotInteractableException
    py.get("#nav-al-your-account > a").click(force=True)


def test_element_should_be_clickable(py):
    py.visit('https://deckshop.pro')
    assert py.get("a.nav-link[href='/spy/']").should().be_clickable()


def test_element_should_not_be_clickable(py):
    py.visit('https://deckshop.pro')
    with pytest.raises(AssertionError):
        py.get('#smartHelp').should().be_visible()


def test_element_should_be_visible(py):
    py.visit('http://book.theautomatedtester.co.uk/chapter1')
    py.get('#loadajax').click()
    assert py.get('#ajaxdiv').should().be_visible()


def test_element_should_be_hidden(py):
    py.visit('https://deckshop.pro')
    assert py.get('#smartHelp').should().be_hidden()


def test_element_should_be_focused(py):
    py.visit('https://deckshop.pro')
    py.get('#smartSearch').click()
    assert py.get('#smartSearch').should().be_focused()


def test_element_should_not_be_focused(py):
    py.visit('https://deckshop.pro')
    assert py.get('#smartSearch').should().not_be_focused()
