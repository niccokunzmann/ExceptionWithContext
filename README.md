ExceptionWithContext
====================

A Python 2.7 exception with the `__context__` and `__traceback__` attributes like in Python 3.

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

In Python 3, the order would be:

 1. `ExceptionWithContext` 
 2. `This exception occured during the handling of the exception below:`
 3. `Exception`
 
But here it is the other way around:

 1. `Exception` 
 2. `During handling of the above exception, another exception occurred:`
 3. `ExceptionWithContext`
