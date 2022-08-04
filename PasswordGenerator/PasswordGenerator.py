import random
NumOfChar = 10
password = ''
while True:
    user_input = input("Would you like to create a random password? (y/n): ")
    if user_input.lower() == ("y"):
        for i in range (NumOfChar):
            random_integer = random.randint(0,126)
            password += chr(random_integer)
        print(password)
    else:
        pass