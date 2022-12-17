def most_common_words(sentence, n):
    # Split the sentence into a list of words
    assert isinstance(sentence, str), "InputError: 'sentence' must be a string."
    assert isinstance(n, int), "InputError: 'n' must be an integer."
    words = sentence.split()
    # Create dictionary for the word frequencies
    word_freq = {}
    # Count the frequency of each word and store it in the dictionary
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
    # Sort the words by frequency and alphabetical order
    sorted_words = sorted(word_freq.items(), key=lambda x: (-x[1], x[0]))
    # Return the top n words
    return sorted_words[:n]


print(most_common_words("baz bar foo foo zblah zblah zblah baz toto bar", 3))
