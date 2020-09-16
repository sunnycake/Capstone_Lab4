import re

def camel_case(sentence):
    # Capitalized first letter of each word
    upper_first_word = sentence.title()
    remove_space = upper_first_word.replace(" ", "")  # removes space
    # lowercase the first word then add with the rest
    return(remove_space[0:1].lower() + remove_space[1:])


def main():
    sentence = input("Please enter a sentence: ")
    # https://www.8bitavenue.com/how-to-remove-special-characters-from-string-except-space-in-python/
    result = re.sub("[^a-zA-Z0-9\s]","", sentence)
    camelcased = camel_case(result)
    print(camelcased)


if __name__ == '__main__':
    main()
