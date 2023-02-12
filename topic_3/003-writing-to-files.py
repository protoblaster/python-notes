# writing to files in python 

file = open('data_file/003-example.txt', 'w')
file.write("Lets check the write operation!")

file.seek(5)        # move cursor to 6th byte (letter)

file.write(" examine ")

file.close()

file = open('data_file/003-example.txt')    # not specifying the mode opens file in read only mode

for lines in file:
    print(lines)

file.close()

# we will now open 003-example.txt using a with block
with open('data_file/003-sample.txt', 'w') as f:
    f.write("First Line\n")
    f.write("Second Line\n")
    f.write("Third Line\n")

print(f.closed)

# if we want to add information to a file without overwriting
# it we use append mode 

with open('data_file/003-sample.txt', 'a') as f:
    print(f.tell())

    f.writelines(["Another Line was appened\n",
                  "What will the file look like now?\n",
                  "Lets check it out!\n"])

    print(f.fileno())   # this is used by the OS to identify where the file is in memory

    print(f.isatty())          # this is used to see if the file is attatched to a terminal process

    print(f.readable())        # this checks if the file is readable

    print(f.writable())        # checks if the file is writable

print(file.closed)