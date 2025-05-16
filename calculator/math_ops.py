def add(a, b):
    """Повертає суму a та b."""
    return a + b


def subtract(a, b):
    """Повертає різницю a та b."""
    return a - b


def multiply(a, b):
    """Повертає добуток a та b."""
    return a * b


def divide(a, b):
    """Повертає частку a на b."""
    if b == 0:
        raise ValueError("Ділення на нуль!")
    return a / b
