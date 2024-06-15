# Define a placeholder string to be replaced in the template letter
PLACEHOLDER = "[name]"

# Open the file containing the list of names to be used in the mail merge
with open("/media/zoro-d-code/Personal/Roger/Training/100_Days_with_Python/Day_24/Mail+Merge+Project+Start/Mail Merge Project Start/Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()  # Read all lines from the file into a list

# Open the template letter file
with open("/media/zoro-d-code/Personal/Roger/Training/100_Days_with_Python/Day_24/Mail+Merge+Project+Start/Mail Merge Project Start/Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()  # Read the contents of the letter file

    # Iterate through each name in the list
    for name in names:
        stripped_name = name.strip()  # Remove leading/trailing whitespace characters
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)  # Replace the placeholder with the name

        # Create a new file for each personalized letter
        with open(f"/media/zoro-d-code/Personal/Roger/Training/100_Days_with_Python/Day_24/Mail+Merge+Project+Start/Mail Merge Project Start/Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)  # Write the personalized letter to the file