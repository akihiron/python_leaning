import inspect

def test(func):
    def _decolate(*args, **kwargs):
        func(*args, **kwargs)
        print(func.__name__+inspect.getfile(func))
    return _decolate