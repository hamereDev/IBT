# -------------------------------
# 1. Unique Cities
# -------------------------------

cities = [
    "Addis Ababa",
    "Adama",
    "Gonder",
    "Addis Ababa",
    "Bahir Dar",
    "Adama"
]

unique_cities = set(cities)

print("Unique Cities:")
for city in unique_cities:
    print(city)

print("Number of unique cities:", len(unique_cities))


# -------------------------------
# 2. Price Report
# -------------------------------

groceries = {
    "Pasta":200,
    "Potato":60,
    "Sugar":220,
    "Injera":50,
    "Eggs": 30
}

print("\nPrice Report:")
for item, price in groceries.items():
    print(f"{item}: {price} ETB")


# -------------------------------
# 3. Tax Comprehension
# -------------------------------

prices = [100, 250, 400, 80]

prices_with_tax = [price * 1.15 for price in prices]

print("\nPrices with 15% Tax:")
print(prices_with_tax)


# -------------------------------
# 4. Cheap Items
# -------------------------------

cheap_items = [price for price in prices if price < 200]

print("\nPrices Under 200 ETB:")
print(cheap_items)


# -------------------------------
# 5. Write & Read File
# -------------------------------

with open("names.txt", "w") as file:
    file.write("Hamere\n")
    file.write("Meti\n")
    file.write("Selam\n")

print("\nCustomer Names:")

with open("names.txt", "r") as file:
    for name in file:
        print(name.strip())


# -------------------------------
# 6. Safe Division
# -------------------------------

try:
    number = float(input("\nEnter a number: "))
    result = 1000 / number
    print("Result:", result)

except ValueError:
    print("Error: Please enter a valid number.")

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
