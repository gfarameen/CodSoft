#  Password Generator:

import string
import random

def Password_Generator(length):
    # Taking type of password from user
    print('''Choose Type of Password:
         1. All Digits
         2. All Letters
         3. Special characters
         4. Mix of all''')
    
    choice=int(input("Pick a number"))
    
    # Defining passsowrd types:
    Digits= string.digits
    Letters=string.ascii_letters
    Special_characters=string.punctuation
    Mixed=string.ascii_letters+string.punctuation+string.digits

    # Randomly choosing from string
    if choice==1:
        password = ''.join(random.choice(Digits) for lengthof in range(length))
    
        return password
    
    elif choice==2:
        password = ''.join(random.choice(Letters) for lengthof in range(length))
    
        return password
    
    elif choice==3:
        password = ''.join(random.choice(Special_characters) for lengthof in range(length))
    
        return password
    elif choice==4:
        password = ''.join(random.choice(Mixed) for lengthof in range(length))
    
        return password
    else:
        print("Choose a valid Choice")

# Taking length of passsowrd
length= int(input("Enter length for your passowrd"))
# Function calling
Generatedpassword=Password_Generator(length)
# Displaying  Generated Password
print("Generated Password:", Generatedpassword)