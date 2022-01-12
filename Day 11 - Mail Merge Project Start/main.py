# Reads the Template of invitaion and stores it
with open("./Input/Letters/starting_letter.txt") as f:
    start_text = f.read()

# Stores all the names to which invitation is to send
with open("./Input/Names/invited_names.txt") as f:
    # To remove blank line("|\n") from the lines.
    names = [line.rstrip() for line in f.readlines()]

# Make automated Invitaion Cards
for name in names:
    template = start_text.replace("[name]", name)
    with open(f"D:/python/Day 10/Mail Merge Project Start/Output/ReadyToSend/letter_for_{name}.txt", "w") as f:
        f.write(template)