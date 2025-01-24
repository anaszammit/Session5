#lets create a virtual bartender that serves you if you are of legal age

from random import choice
drinks = [ "whiskey", "rum", "tequila", "gin", "sake", "wine", "beer", "vodka"]
mixers = ["fanta", "fanta limon", "redbull", "tonic", "cola", "soda"]

print(f"{choice(drinks)}{choice(mixers)}")
print( "I am the virtual bartender, welcome to my humble bar")
name = input(" How should I call you?")

try:
    age= input("How old are you?")
    age= int(age)
    legal= None
    country = input(" where are you from?")
    if age < 14:
        legal= False
    elif age < 16:
        if country == "Austria":
            legal = True
        else:
            legal = False
    elif age < 18:
        if country == "Austria" or country == "luxembourg":
            legal = True
        else:
            legal = False
    elif age < 21:
        if country == "USA" or country == "UAE":
            Legal = False
        else:
            Legal = True
    else:# for age greater than 21
        Legal = True

    if legal:
        print(f" here is a {choice(drinks)} {choice(mixers)}")
    else:
        print(f"I can only serve you{ choice(mixers)}")

except ValueError:
    print("I dont have time for your games! Get out!")
