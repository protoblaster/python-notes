# open a file
file = open('topic_3/data_file/001-sample.txt', 'r')
print(file)
print('The file is in', file.mode, 'mode')
print('The file is closed:', file.closed)
file.close()
print('The file is closed:', file.closed)

file = open('topic_3/data_file/001-sample.txt', 'r')
print(file.read())
file.close()

file = open('topic_3/data_file/001-sample.txt', 'r')
print(file.seek(0))            # this places the cursor at the 0th byte of the file 
print(file.read(5))            # this reads the first 5 bytes of the file
print(file.tell())             # this tells us where the cursor in the file is currently
print(file.read(5))            # read 5 more bytes from the file
print(file.tell())             # this tells us where the cursor in the file is
file.close()