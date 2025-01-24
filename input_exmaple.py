name=input("what is your name? ")
print("hello", name)
age=input("How old are you" + name + "?")
print(name+ "based on my advanced calculation, you were born in " +str(2024-int(age)))

age2= input(f"How old are you" + "{name}?")
age2=int(age2)
print(f"{age2}, you were born in {2024-age2}")
