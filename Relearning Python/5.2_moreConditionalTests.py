# Date: 1/9/2024
# Have at least one true and one false result for each of the following:
# - tests using equality and inequality with strings
# - tests using the lower() method
# - numerical tests involving equality and inequality, greater than and less than, greater than or equal to, and less than or equal to
# - tests using the and keyword and the or keyword
# - test whether an item is in a list
# - test whether an item is not in a list

# Tests using equality and inequality with strings
stringA = "A"
stringB = "B"
print(stringA == 'B')
print(stringB == 'B')

# Tests using the lower() method
stringC = "C"
print(stringC.lower() == 'C')
print(stringC == 'C')

# Numerical tests involving equality and inequality, greater than and less than, greater than or equal to, and less than or equal to
numA = 1
numB = 2
print(numA > numB)
print(numA < numB)
print(numA < numB or numA == numB)
print(numA > numB or numA == numB)

# Test using the and keyword and the or keyword
stringD = "D"
stringE = "E"
numD = 3
numE = 4
print(stringD == 'D' and stringE == 'E' )
print(stringD == 'A' or stringE  == 'D')
print(numD == 1 and numE == 4)
print(numD == 1 or numE == 4)

# Test whether an item is in a list
listA = ['listItemA', 'listItemB', 'listItemC', 'listItemD', 'listItemE']
print('listItemA' in listA)
print('listItemF' in listA)

# Test whether an item is not in a list
listB = ['listItemF', 'listItemG', 'listItemH', 'listItemI', 'listItemJ']
listItemK = 'listItemK'
print(listItemK not in listB)
print(listItemK in listB)