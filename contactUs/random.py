import random
import string


def RandomStringGenerator(strLen):
    letters = string.ascii_letters
    numbers = string.digits
    list = letters+numbers
    myRandomString = ''
    for i in range(strLen):
        a = random.choice(list)
        myRandomString = myRandomString+a
    print(myRandomString)