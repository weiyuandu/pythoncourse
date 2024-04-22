def letter_positions(input_string):
    positions = []
    for char in input_string:
        if char.isalpha():
            # Convert the letter to lowercase and get its position in the alphabet
            position = ord(char.lower()) - ord('a') + 1
            positions.append(position)
    return positions

# Example usage:
input_string = "heLLo!"
result = letter_positions(input_string)
print(result)
