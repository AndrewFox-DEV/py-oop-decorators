from functools import wraps
import warnings

def final(method: function) -> function:
  method.__isfinal__ = True
  return method

def deprecated(method: function) -> function:
  @wraps(method)
  def wrapper(*args, **kwargs):
    warnings.warn(f"Function {method.__name__} is deprecated", DeprecationWarning)
    return method(*args, **kwargs)
  return wrapper

def readonly(method: function):
  @property
  def property(self):
    return method(self)
  return property