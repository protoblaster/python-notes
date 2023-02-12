file = open('topic_3/data_file/001-sample.txt', 'r')
print(file.seek(0))
print(file.read(5))
print(file.seek(0))
print(file.readline())
print(file.readline())
print(file.readline())

file.seek(0)

print(file.readlines())         # returns a list of all the lines in the file
file.close()

print(file.closed)              # check if the file is closed

# to prevent accidental access to a file in python we can use
# a 'with' statement
# the 'with' statement automatically closes a file after we have finished with
# the 'with' block of code
with open('topic_3/data_file/001-sample.txt', 'r') as f:
    data = f.readlines()

print(data)

print(f.closed)

with open('topic_3/data_file/001-sample.txt', 'r') as f:
    line = f.readline()

    while line:
        print(line)
        line = f.readline()

# the 'while' loop above iterates through the lines within f
