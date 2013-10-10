from ExceptionWithContext import *
import dis

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

def test_this_is_the_frame():
    frame = calling_frame()
    assert frame.f_globals is globals()

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

# create more tests!


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
