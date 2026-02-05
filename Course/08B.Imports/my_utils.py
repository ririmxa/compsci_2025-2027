def shout(text: str) -> str:
    return text.upper() + "!"


def is_even(n: int) -> bool:
    return n % 2 == 0


def clamp(value: int, minimum: int, maximum: int) -> int:
    if value < minimum:
        return minimum
    if value > maximum:
        return maximum
    return value
