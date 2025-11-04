import pytest


@pytest.fixture()
def before_after():
    print("before test")
    yield
    print("\nafter test")


def test_demo1(before_after):
    assert 2 == 2


def test_demo2():
    assert 1 == 1


def test_demo3(before_after):
    assert 2 == 2
