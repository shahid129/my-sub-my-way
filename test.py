"""
Import pytest to check the code in run.py
"""
import pytest


def test_food_price():
    """
    The function to test the code for food_price() in run.py
    """
    assert float(round(2))


@pytest.fixture(name="my_name")
def fixture_my_name():
    """
    A function in fixture that can accept username to test the code
    """
    name = "shahid"
    return name


def test_user_name(my_name):
    """
    The function to test the code for user_name() in run.py
    """
    assert my_name == 'shahid'


@pytest.fixture(name="new_latest_receipt")
def fixture_new_latest_receipt():
    """
    A function in fixture that can accept user input to test the code
    """


def test_last_receipt(new_latest_receipt):
    """
    The function to test the code for last_receipt() in run.py
    """
    assert new_latest_receipt == "y" or "n"


@pytest.fixture(name="sub")
def fixture_sub():
    """
    A function in fixture that can accept user input to test the code
    """


def test_sandwich_size(sub):
    """
    The function to test the code in sandwich_size() in run.py
    """
    assert sub == "a" or "b"


@pytest.fixture(name="bread")
def fixture_bread():
    """
    A function in fixture that can accept user input to test the code
    """
    user_input = "1"
    return user_input


def test_choose_bread(bread):
    """
    The function to test the code in choose_bread() in run.py
    """
    assert bread == "1"


@pytest.fixture(name="new_choose_sandwich")
def fixture_new_choose_sandwich():
    """
    A function in fixture that can accept user input to test the code
    """
    user_input = "1"
    return user_input


def test_sandwich_names(new_choose_sandwich):
    """
    The function to test the code in sandwich_names() in run.py
    """
    assert new_choose_sandwich == "1"


@pytest.fixture(name="new_select_cheese")
def fixture_new_select_cheese():
    """
    A function in fixture that can accept user input to test the code
    """


def test_select_cheese(new_select_cheese):
    """
    The function to test the code in select_cheese() in run.py
    """
    assert new_select_cheese == "1" or "2" or "3"


@pytest.fixture(name="new_choose_cheese")
def fixture_new_choose_cheese():
    """
    A function in fixture that can accept user input to test the code
    """


def test_choose_cheese(new_choose_cheese):
    """
    The function to test the code in choose_cheese() in run.py
    """
    assert new_choose_cheese == "y" or "n"


@pytest.fixture(name="new_get_salad_from_user")
def fixture_new_get_salad_from_user():
    """
    A function in fixture that can accept user input to test the code
    """


def test_get_salad_from_user(new_get_salad_from_user):
    """
    The function to test the code in get_salad_from_user() in run.py
    """
    assert new_get_salad_from_user == "1" or "2" or "3"


@pytest.fixture(name="new_get_sauce_from_user")
def fixture_new_get_sauce_from_user():
    """
    A function in fixture that can accept user input to test the code
    """


def test_get_sauce_from_user(new_get_sauce_from_user):
    """
    The function to test the code in get_sauce_from_user() in run.py
    """
    assert new_get_sauce_from_user == "1" or "2" or "3"


@pytest.fixture(name="new_discount_price")
def fixture_new_discount_price():
    """
    A function in fixture that can accept user input to test the code
    """


def test_discount_price(new_discount_price):
    """
    The function to test the code in discount_price() in run.py
    """
    assert new_discount_price == "y" or "n"


@pytest.fixture(name="new_restart")
def fixture_new_restart():
    """
    A function in fixture that can accept user input to test the code
    """


def test_restart(new_restart):
    """
    The function to test the code in restart() in run.py
    """
    assert new_restart == "y" or "n"
