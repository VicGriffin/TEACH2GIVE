#Write a program that accepts a string as input, capitalizes the first letter of each word in the string, and then returns the result string.
def capitalize_first_letter(sentence):
    words = sentence.split()
    capitalized_words = [word.capitalize() for word in words]
    return ' '.join(capitalized_words)

def main():
    user_input = input("Enter a string: ")
    result = capitalize_first_letter(user_input)
    print("Capitalized string:", result)

if __name__ == "__main__":
    main()
