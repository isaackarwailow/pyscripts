import requests
import random
import string

def generate_random_word():
    prefixes = ['re', 'pre', 'post', 'un', 'dis']
    suffixes = ['able', 'er', 'ish', 'ment', 'ness']
    word = ''.join(random.choice(string.ascii_lowercase) for i in range(random.randint(3, 8)))

    if random.choice([True, False]):
        word = random.choice(prefixes) + word
    else:
        word = word + random.choice(suffixes)
    
    word = word.capitalize()
    return word
# password to be in the form XXXTTTTT004
def generate_password():
    word1 = generate_random_word()
    word2 = generate_random_word()

    number = str(random.randint(0, 999)).zfill(3)
    password = word1 + word2 + number
    return password

password = generate_password()
print(password)

rw = generate_random_word()
print(rw)


word_site = "https://www.mit.edu/~ecprice/wordlist.10000"

response = urllib2.urlopen(word_site)
txt = response.read()
WORDS = txt.splitlines()