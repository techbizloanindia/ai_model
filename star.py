def print_pyramid(rows):
    for i in range(1, rows + 1):
        # Print leading spaces
        print(' ' * (rows - i), end='')
        # Print asterisks with a space between them
        print('* ' * i)

# Set the number of rows in the pyramid
print_pyramid(6)