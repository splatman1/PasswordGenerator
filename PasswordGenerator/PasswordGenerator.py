import random
while True:
    NumOfChar = int(input("how long do you want password"))
    if (NumOfChar > 1) & (NumOfChar < 30):
        break
    else:
        print("enter a blah blah")


password = ''
while True:
    user_input = input("Would you like to create a random password? (y/n): ")
    if user_input.lower() == ("y"):
        for i in range (NumOfChar):
            random_integer = random.randint(0,126)
            password += chr(random_integer)
        print(password)
    else:
        break
