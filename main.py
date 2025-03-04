import sys
from stats import num_words, num_characters, sorted_characters


def get_book_text(filepath):
    """Read and return the entire text from the file at the given filepath."""
    with open(filepath, 'r') as f:
        return f.read()

def print_report(filepath):
    book_text = get_book_text(filepath)
    word_count = num_words(book_text)
    # Get the raw character counts (do not print this raw output)
    char_counts = num_characters(book_text)
    # Build a sorted list (only alphabetical characters)
    sorted_chars = sorted_characters(char_counts)
    
    # Print the formatted report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    
    for d in sorted_chars:
        # Each dictionary d has a single key-value pair.
        for char, count in d.items():
            print(f"{char}: {count}")
    
    print("============= END ===============")

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    print("sys.argv:", sys.argv)
    print_report(filepath)
if __name__ == '__main__':
    main()

