#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("Input/Names/invited_names.txt", "r") as data:
    name_list = data.readlines()
    with open("Input/letters/starting_letter.txt", "r") as letter:
        letter_contant = letter.read()
        for names in name_list:        
            stripped_names = names.strip()
            new_letter = letter_contant.replace("[name]",stripped_names)
            with open(f"Output/ReadyToSend/Letter_For_{stripped_names}.txt", "w") as file:
                file.write(new_letter)
