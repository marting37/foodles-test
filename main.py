from collections import Counter


def most_common_words(sentence, n):
    # Split the sentence into a list of words
    assert isinstance(sentence, str), "InputError: 'sentence' must be a string."
    assert isinstance(n, int), "InputError: 'n' must be an integer."
    words = sentence.split()
    # Create dictionary for the word frequencies
    word_freq = {}
    # Use the Counter class to count the frequency of each word
    word_counts = Counter(words)
    # Sort the words by frequency and alphabetical order
    sorted_words = sorted(word_counts.items(), key=lambda x: (-x[1], x[0]))
    # Return the top n words
    return sorted_words[:n]


print(most_common_words("baz bar foo foo zblah zblah zblah baz toto bar", 3))
