# ELLA MARIE A. MALLARI
# BSCPE 1-4

# MULTIPLE LINE 

# to open and write mylife.txt as text file
with open("mylife.txt", "w") as text_file:
    # to do While loop yes or no: 
    while True:
        # input line text
        input_line = input("Input any text line that you want to write: ")
        # to write it at the text file
        text_file.write(input_line + "\n")
        # to ask for lines 
        ask_more_lines = input("Do you want to input another text line? (yes/no) ")
        # break
        if ask_more_lines != 'yes':
            break
