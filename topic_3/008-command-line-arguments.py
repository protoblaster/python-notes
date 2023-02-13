program = 'argv-demo.py'
source = 'default.src'
dest = 'default.dst'

def show_config():
    print('Here is the current configuration:')
    print('Program: %s' % program)
    print('Source: %s' % source)
    print('Destination: %s' % dest)

if __name__ == '__main__':
    import sys
    print('Here is the sys.argv: %s' % sys.argv)
    if len(sys.argv) > 2:
        program, source, dest = sys.argv[:3]
    elif len(sys.argv) > 1:
        program, source = sys.argv[:2]
    else:
        program = sys.argv[0]
    show_config()