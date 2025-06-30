from abc import ABCMeta, abstractmethod

def interface(cls):
  """
  Converts a class into a Java-like interface.
  All methods must be abstract.
  No concrete attributes allowed.
  """
  namespace = {}
  for name, value in cls.__dict__.items():
    if name.startswith('__') and name.endswith('__'):
      namespace[name] = value  # keep dunder methods
    elif callable(value):
      namespace[name] = abstractmethod(value)
    else:
      raise TypeError(f"Interfaces cannot have concrete attributes: '{name}'")

  return ABCMeta(cls.__name__, cls.__bases__, namespace)