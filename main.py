#import modules
import string
import random
#Stores all the possible characters
s1 = list(string.ascii_lowercase)
s2 = list(string.ascii_uppercase)
s3 = list(string.digits)
s4 = list(string.punctuation)
#Takes the number of characters
characters_number = input("Enter the number of characters you want to use: ")
#Makes sure the number of characters is an integer && 6 or more
while True:
    try:
        characters_number = int(characters_number)
        if characters_number < 6 :
            print("you need at least 6 characters")
            characters_number = print("please enter a number again")
        else:
            break
    except:
        print("please enter  numbers only")
        characters_number = input("Enter the number of characters you want to use: ")

#Shuffles all lists
random.shuffle(s1)
random.shuffle(s2)
random.shuffle(s3)
random.shuffle(s4)

#claculate 30% and 20% of the characters
part1 = round(characters_number * (30/100) )
part2 = round(characters_number * (20/100) )

#Create password 60% letters and 40% digits and punctuation
password = []
for i in range(part1):
    password.append(s1[i])
    password.append(s2[i])

for i in range(part2):
    password.append(s3[i])
    password.append(s4[i])

password="".join(password[0:])
print(password)