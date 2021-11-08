tree_width = int(input('Enter the width of the Christmas tree (odd number): '))

with open('tree.txt', 'w') as tree:
    fout = open('tree.txt', 'w')
    new_line = ''
    for i in range(tree_width):
        for j in range(tree_width - i):
            new_line = new_line + '0 '
        for k in range(2 * i + 1):
            new_line = new_line + '* '
        for j in range(tree_width - i):
            new_line = new_line + '0 '
        new_line = new_line + "\n"
    for i in range(2):
        for j in range(tree_width-1):
            new_line = new_line + '  '
        new_line = new_line + '* * *'
        new_line = new_line + "\n"
    fout.write(new_line)

