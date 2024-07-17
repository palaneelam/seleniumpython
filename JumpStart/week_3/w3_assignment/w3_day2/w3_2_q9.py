
# Write a function that takes a string as input and
# returns a dictionary with the frequency count of each word in the string.
# Ignore case and punctuation.

# def user_dictionary(user_text):
#     print("user_text: ", user_text)
#     user_text_len = user_text.__len__()
#     # user_text.count(1)
#     print("user_text_len: ", user_text_len)
#
#     for i in user_text():
#         print(i)
#
#
# user_text_1 = "This is Manoranjan dubey and meenakshi dubey"
# user_dictionary(user_text_1)

# --------------------------------------------------------------
# text = input("Please enter Text: ")
# text = text.upper()
# text_list = text.split(" ")
# text_list_len = text_list.__len__()
#
# print(text_list)
#
# for i in text_list:
#     print(i)

# ***************************************************************************
def user_dictionary(text):
    text = text.upper()
    text_list = text.split(" ")
    text_list_len = text_list.__len__()

    print(text_list)

    for i in text_list:
        print(i)
        count = 1
        if text_list[i-1] == text_list[i]:
            count = count+1
            print(i, count)


user_text_input = input("Please enter text input: ")
user_dictionary(user_text_input)