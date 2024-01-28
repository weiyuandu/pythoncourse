def remove_duplicates(input_string):
    # Use a set to keep track of unique characters
    unique_chars = set()

    # Initialize an empty string to store the modified result
    result_string = ""

    for char in input_string:
        # Check if the character (case-sensitive) is not in the set (i.e., it's the first occurrence)
        if char not in unique_chars:
            # Add the character to the set and result string
            unique_chars.add(char)
            result_string += char

    return result_string

# Example usage:
input_string = "Hello World"
result = remove_duplicates(input_string)
print(result)
