divisor = 3
for num in range(0, 12, 3):
    print(num / divisor)

for letter in 'Ahola':
    print(letter)

num = 0
while num <= 5:
    print(num)
    num += 2
print("Out")
print(num)

num = 0
count = 0
while num <= 19:
    if num % 3 == 0:
        count += 1
    num += 1
print("Numbers divisible by 3", count)

for i in range(1, 11):
    for j in range(i, 11):
        print(f"{i} * {j} = {i * j}")


a = 2
b = 3

result = 1
for _ in range(b):
    temp = 0
    for _ in range(a):
        temp += result
    result = temp

print(f"{a} ** {b} = {result}")

num = input("Enter a number: ")
print(f"{num} is a palindrome." if num == num[::-1] else f"{num} is not a palindrome.")

