def reverse_sequence(data):
    """Reverse the input string or lists."""
    return data[::-1]

user_input = input("Enter a string or number to reverse: ")
print(f"Reversed: {reverse_sequence(user_input)}")