#Write a program that takes a text input from the user and counts the number of words, characters, and lines in the input.

def get_word_Line_char_count(text):
    """
    Calculate the number of words, characters, and lines in the input text.

    Parameters:
    text (str): The input text

    Returns:
    dict: A dictionary with the counts of words, characters, and lines
    """
    # Calculate number of lines
    lines = text.split('\n')
    num_lines = len(lines)

    # Calculate number of words
    words = text.split()
    num_words = len(words)

    # Calculate number of characters
    num_characters = len(text)

    return {
        'lines': num_lines,
        'words': num_words,
        'characters': num_characters
    }


def count():
    print("Enter your input text (press R to finish):")
    lines = []
    while True:
        line = input()
        if line == "R":
            break
        lines.append(line)

    text = "\n".join(lines)
    display_count = get_word_Line_char_count(text)

    print(f"Number of lines: {display_count['lines']}")
    print(f"Number of words: {display_count['words']}")
    print(f"Number of characters: {display_count['characters']}")

count()