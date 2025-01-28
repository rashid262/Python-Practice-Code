# words = list(input("Enter a word: ").split(" "))
# new_words = []
# for word in words:
#     if word.isupper():
#         word.lower()
#     else:
#         word.upper()
#     new_words.append(word)
#
# words = "".join(words)
# print(words)

def swapCase(s):
    sample = ""
    for i in s:
        if i.islower():
            sample += i.upper()
        else:
            sample += i.lower()
    return sample


print(swapCase("pYTHON2"))

