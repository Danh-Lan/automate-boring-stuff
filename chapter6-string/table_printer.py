tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


def print_table(table):
    x = len(tableData)
    y = len(tableData[0])

    max_width = [0] * y
    for i in range(x):
        for j in range(y):
            max_width[i] = max(max_width[i], len(table[i][j]))

        print(max_width[i])

    for j in range(y):
        for i in range(x):
            print(table[i][j].rjust(max_width[i]), end=' ')

        print('\n')


print_table(tableData)
