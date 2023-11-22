# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./Input/Letters/starting_letter.txt") as text:
    letter_content = text.read()
    with open("Input/Names/invited_names.txt") as names:
        for name in names:
            name = name.strip()
            with open(f"A:/100DAYSPYTHON/dayTwentyFour/Output/ReadyToSend/letter_for_{name.strip()}.txt",
                      "w") as to_send:
                new_text = ''
                new_text += letter_content.replace("[name]", name)
                to_send.write(f"{new_text}")
