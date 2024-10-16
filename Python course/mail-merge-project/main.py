PLACEHOLDER = "[name]" #what we want to reeplace

with open("./input/Names/invited_names.txt") as names_file: # Read all the names in the file
    names = names_file.readlines()


with open("./input/letters/starting_letters.txt") as letter_file: #read the words in the letter
    letter_words = letter_file.read()
    for name in names:
        stripped_name = name.strip() #strip all white space in the letter
        new_letter = letter_words.replace(PLACEHOLDER, stripped_name) #Replace the placeholder with the actual name from the names array
        with open(f"./output/Readytosend/letter_for_{stripped_name}.docx", mode = "w") as completed_letter: #Create letter for each person
            completed_letter.write(new_letter) # Write out the new letter





