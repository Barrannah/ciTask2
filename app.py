def is_palindrome(value: str) -> bool:
    cleaned = "".join(ch.lower() for ch in value if ch.isalnum())
    return cleaned == cleaned[::-1]


def count_vowels(value: str) -> int:
    return sum(1 for ch in value.lower() if ch in "aeiou")
