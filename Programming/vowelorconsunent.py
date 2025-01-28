alphabet = input("Enter an Alphabet to check for vowel or consonant: ")
set1 = {"a","e","i","o","u","A","E","I","O","U"}
if alphabet in set1:
    print(f"{alphabet} is a Vowel")
else:
    print(f"{alphabet} is a Consonant")