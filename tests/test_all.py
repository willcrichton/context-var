import context_var as cv


def test_basic():
    var = cv.ContextVar('hello')
    assert var.get() == 'hello'

    with var.set('world'):
        assert var.get() == 'world'

    assert var.get() == 'hello'


def test_nested():
    var = cv.ContextVar()
    assert var.get() == None

    with var.set(1):
        assert var.get() == 1

        with var.set(2):
            assert var.get() == 2

        assert var.get() == 1

    assert var.get() == None


def test_multiple():
    v1 = cv.ContextVar()
    v2 = cv.ContextVar()

    with v1.set(1):
        with v2.set(2):
            assert v1.get() == 1
            assert v2.get() == 2

    assert v1.get() == None
    assert v2.get() == None
