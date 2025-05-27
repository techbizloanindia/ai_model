def print_pyramid(rows):
    # Center aligned pyramid
    for i in range(1, rows + 1):
        print(' ' * (rows - i) + '* ' * i)

def print_pyramid_reversed(rows):
    # Center aligned reversed 
    for i in range(rows, 0, -1):
        print(' ' * (rows - i) + '* ' * i)

def print_pyramid_left(rows):
    # Left side 
    for i in range(1, rows + 1):
        print('* ' * i)

def print_pyramid_right(rows):
    # Right side
    for i in range(1, rows + 1):
        print(' ' * (rows - i) + '*' * i)

def correct_word(word):
    corrections = {
        'revarce': 'reverse',
        'lef': 'left',
        'rigt': 'right',

    }
    return corrections.get(word, word)

command = input("Enter command (print/reverse/left/right): ").lower()
command = correct_word(command)

rows = 6

if command == 'reverse':
    print_pyramid_reversed(rows)
elif command == 'left':
    print_pyramid_left(rows)
elif command == 'right':
    print_pyramid_right(rows)
else:
    print_pyramid(rows)
    print("Pyramid printed successfully.")