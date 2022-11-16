#Data Types

total_cost = input("What is the total price of your bill in dollars? $")

number_of_diners = input("\nHow many people are splitting the bill? ")

percentage_tip = input("\nWhat percentage would you like to tip? %")
converted_tip = float(percentage_tip) / 100

price_per_diner = (
    float(total_cost) +
    (float(total_cost) * converted_tip)) / float(number_of_diners)

print(f"\nThe price per diner is: ${price_per_diner:.2f}")
