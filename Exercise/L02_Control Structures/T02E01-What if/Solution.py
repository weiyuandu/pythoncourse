# Prompt the user to enter the age
passenger_age = int(input("Enter passenger's age: "))

# Determine the ticket price based on age
if passenger_age <= 5:
    ticket_price = "Free"
elif 6 <= passenger_age <= 18:
    ticket_price = "50% discount"
elif 19 <= passenger_age <= 60:
    ticket_price = "Regular price"
else:
    ticket_price = "25% discount"

# Output the ticket price
print(f"Ticket price for an {['child', 'student', 'adult', 'senior'][ticket_price.find('Free') + ticket_price.find('discount')]}: {ticket_price}")
