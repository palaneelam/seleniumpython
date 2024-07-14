#Write a function to find the longest palindromic substring in a given string
def longest_palindromic_substring(s):
    """
    Find the longest palindromic substring in a given string.

    Parameters:
    s (str): The input string

    Returns:
    str: The longest palindromic substring
    """


    startstring, endstring = 0, 0 # Initialize the start and end pointers of the longest palindromic substring

    for i in range(len(s)):

        len1 = expand_around_center(s, i, i) # Check for odd-length palindromes centered at i
        len2 = expand_around_center(s, i, i + 1) # Check for even-length palindromes centered between i and i+1
        max_len = max(len1, len2) # Determine the maximum length from both cases

        if max_len > endstring - startstring:
            startstring = i - (max_len - 1) // 2
            endstring = i + max_len // 2

    return s[startstring:endstring + 1]

def expand_around_center(s, left, right):
    """
    Expand around the center to find the length of the palindrome.

    Parameters:
    s (str): The input string
    left (int): The left pointer
    right (int): The right pointer

    Returns:
    int: The length of the palindrome
    """
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1

    return right - left - 1

input_string = str(input ("Enter the substring:")) # Takes the input
resultedsubstring = longest_palindromic_substring(input_string)
print(f"The longest palindromic substring in '{input_string}' is: '{resultedsubstring}'")
