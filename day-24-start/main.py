# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

name_list = []
PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as name_file:
    name_list = name_file.readlines()

with open("./Input/Letters/starting_letter.txt") as letter_file:
    for name in name_list:
        letter_name = name.strip("\n")
        letter = letter_file.read()
        letter = letter.replace(PLACEHOLDER, letter_name)
        with open(f"./Output/ReadyToSend/letter_for_{letter_name}", mode="w") as new_file:
            new_file.write(letter)
