# pystrict - Documentation

## Overview

The `pystrict` package provides a set of decorators inspired by Java and C++ to enforce strict OOP design rules in Python.
These decorators help you define interfaces, structures, visibility modifiers (`private`, `public`), final methods, deprecations, and read-only properties.

---

## Decorators

### 1. `@interface`

Transforms a Python class into a **Java-like interface**.

* All methods must be abstract.
* No concrete attributes allowed.
* Enforced via `abc.ABCMeta` and `abstractmethod`.

#### Usage:

```python
from pystrict import interface

@interface
class MyInterface:
    def method1(self):
        pass

    def method2(self, arg):
        pass
```

#### Explanation:

* The decorated class will raise an error if any method is not overridden.
* Attempting to add concrete attributes raises `TypeError`.
* This helps in defining clear contracts for your classes.

---

### 2. `@struct`

Simulates a **C++-like struct** using Python's `dataclasses`.

* Automatically generates `__init__`, `__repr__`, `__eq__`, etc.
* All attributes are public by convention.

#### Usage:

```python
from pystrict import struct

@struct
class Point:
    x: float
    y: float

p = Point(1.0, 2.0)
print(p)  # Output: Point(x=1.0, y=2.0)
```

---

### 3. `@private`

Marks a **method as private**.

* Raises `AttributeError` if accessed without explicit permission.
* Simulates private methods not directly supported in Python.

#### Usage:

```python
from pystrict import private

class MyClass:
    def __init__(self):
        self._allow_private_access = True

    @private
    def _secret_method(self):
        print("This is private")

obj = MyClass()
obj._secret_method()  # Works because _allow_private_access is True

obj._allow_private_access = False
obj._secret_method()  # Raises AttributeError
```

---

### 4. `@public`

Marks a method as public (mainly for clarity and symmetry with `@private`).

* Does not change Python’s default behavior.
* Adds metadata `__visibility__ = "public"` to the method.

#### Usage:

```python
from pystrict import public

class MyClass:
    @public
    def do_something(self):
        print("Public method")
```

---

### 5. `@final`

Marks a method as **final**, meaning it should not be overridden in subclasses.

* This is metadata only; enforcement must be manual or via additional tools.

#### Usage:

```python
from pystrict import final

class Base:
    @final
    def cannot_override(self):
        print("This method should not be overridden")
```

---

### 6. `@deprecated`

Marks a function or method as **deprecated**.

* Emits a `DeprecationWarning` when called.

#### Usage:

```python
from pystrict import deprecated

@deprecated
def old_function():
    print("This function is deprecated")

old_function()
# Warning: Function old_function is deprecated
```

---

### 7. `@readonly`

Turns a method into a **read-only property**.

* The decorated method behaves like a property without a setter.

#### Usage:

```python
from pystrict import readonly

class MyClass:
    def __init__(self, value):
        self._value = value

    @readonly
    def value(self):
        return self._value

obj = MyClass(42)
print(obj.value)  # 42
obj.value = 10    # AttributeError: can't set attribute
```

---

## Summary Table

| Decorator     | Purpose                                | Example Usage         |
| ------------- | -------------------------------------- | --------------------- |
| `@interface`  | Define Java-like interface             | `@interface class I`  |
| `@struct`     | Define C++-like struct (dataclass)     | `@struct class S`     |
| `@private`    | Mark method as private                 | `@private def _m()`   |
| `@public`     | Mark method as public                  | `@public def m()`     |
| `@final`      | Mark method as final (non-overridable) | `@final def m()`      |
| `@deprecated` | Mark method/function deprecated        | `@deprecated def f()` |
| `@readonly`   | Create read-only property              | `@readonly def p()`   |

## License

This project is licensed under a custom license by AndrewFox_DEV.  
See the [LICENSE](LICENSE) file for details.

