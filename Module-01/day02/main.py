# TeleBirr Tip Calculator

# Store the bill total and number of people
bill_total = 3000
number_of_people = 4

# List of friends
friends = ["Hamere", "Abiy", "Kal", "Marta"]

# Function to calculate each person's share
def split_bill(total, people, tip_rate=0.10):
    total_with_tip = total + (total * tip_rate)
    return total_with_tip / people

# Calculate each person's share
share = split_bill(bill_total, number_of_people)

# Print the results
print(f"Total Bill: {bill_total} ETB")
print("Tip: 10%")
print(f"Each person pays: {share} ETB")

# Print each friend's share
for friend in friends:
    print(f"{friend} pays {share} ETB")