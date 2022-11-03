import random
import string


main = string.ascii_letters + string.digits + string.punctuation
password = random.sample(main, 6)
password += random.sample(string.ascii_uppercase, 2)
password += random.choice(string.digits)
password += random.choice(string.punctuation)
passwordList = list(password)
random.SystemRandom().shuffle(passwordList)
for i in passwordList:
    print(i,end="")