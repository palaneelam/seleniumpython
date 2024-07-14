#Write a function that takes a string as input and returns a dictionary with the frequency count of each word in the string. Ignore case and punctuation.
import string

def word_frequency(text):
    """
    Calculate the frequency of each word in a given string.

    Parameters:
    text (str): The input string

    Returns:
    dict: A dictionary with words as keys and their frequency count as values
    """

    text = text.lower() # Convert the text to lower case
    text = text.translate(str.maketrans("", "", string.punctuation)) # Remove punctuation from text
    words = text.split() # Split the text into words
    frequency_dict = {} # Initialize an empty dictionary to store the word frequencies

    for word in words: # Count the frequency of each word
        if word in frequency_dict:
            frequency_dict[word] += 1
        else:
            frequency_dict[word] = 1

    return frequency_dict

input_text = input("Enter Input Text String:")
dictionary = word_frequency(input_text)
print(f"Word frequency count:{dictionary}")