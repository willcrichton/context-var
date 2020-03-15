import context_var as cv


def test_basic():
    var = cv.ContextVar('hello')
    assert var.get() == 'hello'

    with var.set('world'):
        assert var.get() == 'world'

    assert var.get() == 'hello'
