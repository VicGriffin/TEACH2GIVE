#Write a program that counts the number of vowels in a sentence.
def count_vowels(sentence):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    sentence = sentence.lower()
    vowel_count = 0
    for char in sentence:
        if char in vowels:
            vowel_count += 1
    return vowel_count

user_sentence = input("Enter a sentence: ")
print("Number of vowels in the sentence:", count_vowels(user_sentence))
#allows your to write sentece and calculates the number of vowels in the sentece
