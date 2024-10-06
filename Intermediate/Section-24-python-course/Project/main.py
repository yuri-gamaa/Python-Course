# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

REPLACE_TXT = '[name]'

with open("./Mail Merge Project Start/Input/Names/invited_names.txt") as file:
    names = file.readlines()

with open('./Mail Merge Project Start/Input/Letters/starting_letter.txt', 'r') as file:
    base_letter = file.read()

for name in names:
    just_name = name.strip()
    with open(f'./{just_name}_letter.txt', 'w') as file:
        new_letter = base_letter.replace(REPLACE_TXT, just_name)
        file.write(new_letter)
