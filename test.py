import pytest

from main import most_common_words


def test_most_common_words():
    # Test with the example given in the exercise
    sentence = "baz bar foo foo zblah zblah zblah baz toto bar"
    n = 3
    expected_output = [('zblah', 3), ('baz', 2), ('bar', 2)]
    assert most_common_words(sentence, n) == expected_output
    # Test with a simple sentence
    sentence = "The quick brown fox jumps over the lazy dog."
    n = 3
    expected_output = [("The", 1), ("brown", 1), ("dog.", 1)]
    assert most_common_words(sentence, n) == expected_output

    # Test with a longer sentence
    sentence = "The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog."
    n = 5
    expected_output = [("The", 2), ("brown", 2), ("dog.", 2), ("fox", 2), ("jumps", 2)]
    assert most_common_words(sentence, n) == expected_output

    # Test with a sentence that has multiple words with the same frequency
    sentence = "The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy cat."
    n = 5
    expected_output = [("The", 2), ("brown", 2), ("fox", 2), ("jumps", 2), ("lazy", 2)]
    assert most_common_words(sentence, n) == expected_output


def test_input_type_most_common_words():
    # Test with an integer input
    sentence = 123
    n = 3
    expected_output = "InputError: 'sentence' must be a string."
    try:
        most_common_words(sentence, n)
    except Exception as e:
        assert str(e) == expected_output
    # Test with a float input
    sentence = 123.456
    n = 3
    expected_output = "InputError: 'sentence' must be a string."
    try:
        most_common_words(sentence, n)
    except Exception as e:
        assert str(e) == expected_output
    # Test with a string for the size of the list
    sentence = "The quick brown fox jumps over the lazy dog."
    n = "3"
    expected_output = "InputError: 'n' must be an integer."
    try:
        most_common_words(sentence, n)
    except Exception as e:
        assert str(e) == expected_output