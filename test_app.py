from app import count_vowels, is_palindrome


def test_count_vowels_simple():
    assert count_vowels("hello") == 2


def test_count_vowels_empty():
    assert count_vowels("") == 0


def test_is_palindrome_true():
    assert is_palindrome("Madam, I'm Adam")


def test_is_palindrome_false():
    assert not is_palindrome("codex")
