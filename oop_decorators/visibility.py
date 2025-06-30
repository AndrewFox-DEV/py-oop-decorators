from functools import wraps
from typing import Any, cast

def private(method: function) -> function:
  @wraps(method)
  def wrapper(self: Any, *args: Any, **kwargs: Any) -> Any:
    if not getattr(self, '_allow_private_access', False):
      raise AttributeError(f"Method '{method.__name__}' is private.")
    return method(self, *args, **kwargs)

  wrapper.__visibility__ = 'private'
  return cast(function, wrapper)

def public(method: function) -> function:
  method.__visibility__ = 'public'
  return method