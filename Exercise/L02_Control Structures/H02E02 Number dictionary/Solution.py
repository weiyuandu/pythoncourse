# Input: Dictionary mapping numerical values to words
cipher_dict = {1523: 'hello', 272: 'world', 3635: 'python'}

# Input: Sequence of numbers representing encrypted text
ciphered_text = [1523, 272, 3635, 272, 1523, 1523]

# Decrypt the ciphered text
deciphered_text = [cipher_dict[num] for num in ciphered_text]

# Output the deciphered text
print("The deciphered text is:", ' '.join(deciphered_text))
