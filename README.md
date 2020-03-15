# context-var

[![Build Status](https://travis-ci.com/willcrichton/context-var.svg?branch=master)](https://travis-ci.com/willcrichton/context-var)
[![PyPI version](https://badge.fury.io/py/context-var.svg)](https://badge.fury.io/py/context-var)


React-style context management, i.e. dynamically scoped variables. Example:

```python
import context_var as cv

var = cv.ContextVar('hello')
assert var.get() == 'hello'

with var.set('world'):
    assert var.get() == 'world'

assert var.get() == 'hello'
```

## Installation

```python
pip install context-var
```
