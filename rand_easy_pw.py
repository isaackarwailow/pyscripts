import requests
import random
import string

def generate_random_word():

    word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
    response = requests.get(word_site)
    WORDS = response.content.splitlines()

    number = random.randint(0, 9999)
    # print out b'zus'
    q_word = str(WORDS[number])
    word = q_word.split("'")[1]
    # there are 10000 words in this url dictionary
    # generate a random number between 0 and 9999

    word = word.capitalize()

    return word # Output: example string

# password to be in the form XXXTTTTT004
def generate_password():
    word1 = generate_random_word()
    word2 = generate_random_word()

    number = '00' + str(random.randint(0, 9))
    password = word1 + word2 + number
    return password

print(generate_password())