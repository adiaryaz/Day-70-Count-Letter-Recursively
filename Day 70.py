def count_letter_recursively(s, letter):
    if not s:
        return 0
    return (1 if s[0] == letter else 0) + count_letter_recursively(s[1:], letter)

input_string = input("Enter a string: ")
input_letter = input("Enter the letter to count: ")

if len(input_letter) != 1:
    print("Please enter only one letter.")
else:
    count = count_letter_recursively(input_string, input_letter)
print(f"The letter '{input_letter}' occurs {count} times in the string.")