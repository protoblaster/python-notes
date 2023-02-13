import sys

print("Script name is:", sys.argv)

if len(sys.argv) > 1:
    print("There are", len(sys.argv) -1, "arguments")

    for arg in sys.argv[1:]:
        print(arg)
else:
    print("There are no arguments")

'''
This program counts the amount of arguments specified
when running the program
'''
