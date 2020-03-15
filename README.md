# context-var

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
