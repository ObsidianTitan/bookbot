def num_words(book_text):
    """Return the total number of words in the given text."""
    return len(book_text.split())


def num_characters(book_text):
    """
    Return a dictionary where each key is a character (lowercased)
    and its value is the count of that character in the text.
    """
    counts = {}
    for char in book_text:
        char = char.lower()
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return counts


def sorted_characters(counts):
    """
    From a dictionary of character counts, filter only alphabetical characters
    and return a list of single-pair dictionaries sorted in descending order by count.
    Example output: [{'e': 44538}, {'t': 29493}, {'a': 25894}, ...]
    """
    a_list = []
    for char, count in counts.items():
        if char.isalpha():
            a_list.append({char: count})
    a_list.sort(reverse=True, key=lambda d: list(d.values())[0])
    return a_list

