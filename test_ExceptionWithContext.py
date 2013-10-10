from ExceptionWithContext import *
import dis
import sys

## tests for Exception in general

def exc_info(exception):
    try:
        raise exception
    except:
        import sys
        return sys.exc_info()

def test_raised_has_message():
    assert exc_info(ExceptionWithContext('hallo'))[1].args == ('hallo',)

def test_raised_has_type():
    assert exc_info(ExceptionWithContext())[0] == ExceptionWithContext

## tests for calling_frame

def test_this_is_the_frame():
    frame = calling_frame()
    assert frame.f_globals is globals()

## tests for is_in_error_handling()
    
def test_is_before_error_handling():
    assert not is_in_error_handling()
    try: pass
    except (): pass
    finally: pass
    
def test_is_after_error_handling():
    try: pass
    except: pass
    finally: pass
    assert not is_in_error_handling()

def test_is_after_error():
    try: raise Exception()
    except: pass
    finally: pass
    assert not is_in_error_handling()

def test_try_is_not_error_handling():
    try: assert not is_in_error_handling()
    except (): pass
    finally: pass

def test_is_in_except_block():
    try: raise Exception()
    except: assert is_in_error_handling()
    finally: pass
    
def test_is_in_finally_block():
    try: raise Exception()
    except: pass
    finally: assert is_in_error_handling()

def test_is_in_try_but_after_error_handling():
    try:
        try: raise Exception()
        except: pass
        finally: pass
        assert not is_in_error_handling()
    except:pass

def test_is_in_finally_of_other_error_handling():
    try:
        try: raise Exception()
        except: pass
        finally: pass
    except:pass
    finally: assert not is_in_error_handling()


def test_is_in_finally_block():
    try: raise Exception()
    except: pass
    finally: assert is_in_error_handling()
    

def test_is_in_finally_block_with_try_before_exception():
    try:
        try:pass
        except:pass
        raise Exception()
    except: pass
    finally: assert is_in_error_handling()

# TODO: create more tests for is_in_error_handling() with more try and except stuff

## tests for the exception:

def test_has_context_of_raised_exception():
    try:
        try:
            e = Exception('trallala')
            raise e
        except:
            ty1, err1, tb1 = sys.exc_info()
            raise ExceptionWithContext('mimimi')
    except ExceptionWithContext:
        ty, err, tb = sys.exc_info()
        assert err.args == ('mimimi',)
        assert err.__context__ == e
        assert e == err1
        assert tb1 == err.__traceback__



def xxxxx():
    try:
        try:pass
        except:pass
        finally:pass
    except:
        try: pass
        except: pass
        finally: pass
    print is_in_error_handling()
