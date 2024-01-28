# Prompt the user to enter the age
passenger_age = int(input("Enter passenger's age: "))

# Prompt the user to enter the current time (in 24-hour format)
current_time = int(input("Enter the current time (in 24-hour format): "))

# Determine peak or off-peak time
is_peak_time = (8 <= current_time <= 10) or (17 <= current_time <= 19)

# Determine the ticket price based on age and peak/off-peak time
if passenger_age <= 5:
    ticket_price = "Free"
elif 6 <= passenger_age <= 18:
    ticket_price = "50% discount"
elif 19 <= passenger_age <= 60:
    ticket_price = "Regular price"
else:
    ticket_price = "25% discount"

# Apply the 20% surcharge for peak time
if is_peak_time and ticket_price != "Free":
    ticket_price += " with 20% surcharge"

# Output the ticket price
print(f"Ticket price for a {['child', 'student', 'adult', 'senior'][ticket_price.find('Free') + ticket_price.find('discount')]} during {'peak' if is_peak_time else 'off-peak'} time: {ticket_price}")
