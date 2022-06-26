tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


    # create a new list of 3 "0" values: one for each list in tableData. It will become this [0,0,0]. Why do you need to create this? 
    # Can you use 1, 2, 3 or other integer? I tried. Output is still the same. So 0 is arbitrary? No. Try and enter 12 or 20, some
    # random bigger numbers. See what happens.  mn
    # Why do you need to set colWidths = [0] * len(table)? For what purposes? To create same number of 0 values as the number of inner lists
    # in tableData?
    # colWidths[0] can store the width of the largest string in tableData[0] and so on. 
    # What is the largest string in tableData[0]?
    colWidths = [0] * len(table)

    # search for the longest string in each list of tableData
    # and put the numbers of characters in the new list
    for y in range(len(table)):
        for x in table[y]:
            if colWidths[y] < len(x):
                colWidths[y] = len(x)

            print()