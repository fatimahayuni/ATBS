# Step 1: Write pseudocode. Similar to Love Grid Code.

tableData = [['apples', 'oranges', 'cherries', 'banana'],
['Alice', 'Bob', 'Carol', 'David'],
['dogs', 'cats', 'moose', 'goose']]

def printTable(table):
    for i in range (len(tableData[0])):
        for j in range (len(tableData)):
             print(table[j][i].rjust(colWidths[y]), end = ' ')
        print()

printTable(tableData)




