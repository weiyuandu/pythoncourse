# Input: List containing ages of all classmates
ages = []

# Get the number of classmates
num_classmates = int(input("Enter the number of classmates: "))

# Check if there are any classmates
if num_classmates > 0:
    # Loop to get the age of each classmate
    for i in range(num_classmates):
        age = int(input(f"Enter the age of classmate {i + 1}: "))
        ages.append(age)

    # Calculate the average age
    average_age = sum(ages) / len(ages)

    # Output the average age
    print(f"The average age of the class is: {average_age}")

else:
    print("No ages provided. Unable to calculate the average age.")
