from dataclasses import dataclass

def struct(cls):
  """
  Simulates a C++-like struct using a dataclass.
  All attributes are public by convention.
  """
  return dataclass(cls)