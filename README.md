ExceptionWithContext
====================

A Python 2.7 exception with the `__context__` and `__taceback__` attributes like in Python 3.

It was created as a response to [this stackoverflow question](http://stackoverflow.com/questions/19234134/finding-out-an-exception-context).

This code produces the following error message:

```python
try:
    raise Exception('normal exception')
except:
    raise ExceptionWithContext('exception during errorhandling')
```

```error
Traceback (most recent call last):
  File "...\test_ExceptionWithContext.py", line 146, in module_main
    raise ExceptionWithContext('exception during errorhandling')
ExceptionWithContext: exception during errorhandling

This exception occured during the handling of the exception below:

Traceback (most recent call last):
  File "...\test_ExceptionWithContext.py", line 144, in module_main
    raise Exception('normal exception')
Exception: normal exception
```
