name = "Елена"
print(name)

five_names = name * 4 + name
print(five_names)

user_name = input("Enter your name: ")
if " " in user_name:
    print("Only name is required!")
    exit()
user_age = input("Enter your age: ")
print("Hello, " + user_name + "!")
try:
    user_age = int(user_age)
except ValueError:
    print("Age entered incorrectly: it should be number")
    exit()
if (user_age <= 0) or (user_age > 150):
    print("Age entered incorrectly: it should be strictly between 0 and 150")
    exit()
if (user_age >= 18) and (user_age < 30):
    print("Age doesn't mean anything if you are not some cheese or wine")
elif user_age < 18:
    print("Hey, kiddo! Isn't it time for bed now?")
else:
    print("Everyone gets to be young once, and your turn is over :(")
print(user_name[1:-1])
print(user_name[::-1])
print(user_name[:5])
print(len(user_name))
digit1 = user_age // 100
digit2 = user_age // 10 % 10
digit3 = user_age % 10
if (digit1 == 0) and (digit2 == 0):
    product_of_numbers = digit3
    result = "Number of digits is 1"
elif (digit1 == 0) and (digit2 != 0):
    product_of_numbers = digit2 * digit3
    result = "Number of digits is 2"
else:
    product_of_numbers = digit1 * digit2 * digit3
    result = "Number of digits is 3"
summ_of_numbers = digit1 + digit2 + digit3
result += "\nSumm of digits is " + str(summ_of_numbers)
result += "\nProduct of numbers is " + str(product_of_numbers)
print(result)
print(user_name.lower())
print(user_name.upper())
print(user_name.capitalize())
print(user_name.capitalize().swapcase())
n = input("What is 2+2*2? ")
n = int(n)
if n == 6:
    print("It is correct")
else:
    print("It's incorrect")
print("тест")
print("Еще тест!")