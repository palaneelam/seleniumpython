# Write a program that counts the number of vowels in a given string.

count_v = 0
word = input("Please enter text to find vowel: ")
vowel = ["a", "e", "i" , "o", "u"]

for word_let in word:
    # print(word_let)
    for vol_let in vowel:
        # print(vol_let)
        if word_let == vol_let:
            # print("Found Vovels")
            count_v += 1
print(count_v)
