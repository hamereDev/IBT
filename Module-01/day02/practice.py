# Exercise 1
temperature = float(input("Enter temperature in °C: "))

if temperature < 15:
    print("cold")
elif temperature <= 28:
    print("warm")
else:
    print("hot")

print()

# Exercise 2
for i in range(1, 11):
    print(f"Receipt #{i}")

print()

# Exercise 3
for number in range(1, 21):
    if number % 2 == 0:
        print(number)

print()

# Exercise 4
def apply_discount(price, percent=10):
    discount = price * percent / 100
    return price - discount

print(apply_discount(1000))
print(apply_discount(1000, 20))

print()

# Exercise 5
count = 5

while count > 0:
    print(count)
    count -= 1

print("Liftoff!")