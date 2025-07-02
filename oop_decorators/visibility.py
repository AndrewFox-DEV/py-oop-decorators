from functools import wraps
from typing import Any, Callable, cast
import inspect

def private(method: function) -> function:
  @wraps(method)
  def wrapper(self: Any, *args: Any, **kwargs: Any) -> Any:
    if not getattr(self, '_allow_private_access', False):
      raise AttributeError(f"Method '{method.__name__}' is private.")
    return method(self, *args, **kwargs)

  wrapper.__visibility__ = 'private'
  return cast(function, wrapper)

def protected(method: Callable) -> Callable:
    @wraps(method)
    def wrapper(self: Any, *args: Any, **kwargs: Any) -> Any:
        stack = inspect.stack()
        for frame_info in stack[1:]:
            caller_locals = frame_info.frame.f_locals
            caller_self = caller_locals.get('self', None)
            if isinstance(caller_self, self.__class__) or isinstance(self, caller_self.__class__):
                break
        else:
            raise AttributeError(f'Method {method.__name__} is protected and cannot be accessed externally.')
        return method(self, *args, **kwargs)

    wrapper.__visibility__ = 'protected'
    return cast(Callable, wrapper)

def public(method: function) -> function:
  method.__visibility__ = 'public'
  return method
