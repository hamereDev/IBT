# inventory.py

stock = {}

# Read stock from file
try:
    with open("stock.txt", "r") as file:
        for line in file:
            item, qty = line.strip().split(",")
            stock[item] = int(qty)

except FileNotFoundError:
    print("No stock file yet — starting empty.")


# Function to adjust stock
def adjust(item, amount):
    stock[item] = stock.get(item, 0) + amount


# -------------------------
# Example stock updates
# -------------------------

adjust("Paracetamol", 5)     # Increase by 5
adjust("Amoxicillin", -2)    # Decrease by 2
adjust("Vitamin C", 10)      # Add new item if it doesn't exist


# -------------------------
# Low stock report
# -------------------------

low_stock = [item for item, qty in stock.items() if qty < 10]

print("\nCurrent Stock:")
for item, qty in stock.items():
    print(f"{item}: {qty}")

print("\nLow Stock Items:")
if low_stock:
    for item in low_stock:
        print(item)
else:
    print("No low stock items.")


# -------------------------
# Save updated stock
# -------------------------

with open("stock.txt", "w") as file:
    for item, qty in stock.items():
        file.write(f"{item},{qty}\n")

print("\nStock has been saved successfully.")