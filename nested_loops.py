# nested loop = A loop within another loop (outer, inner)
#               outer loop:
#                   inner loop:

for x in range(3): # whatever is in this loop will be executed 3 times.
    for y in range(1, 10): # the second number is exclusive.
        print(y, end=" ") # ends each print statement with a new line character.
    print()
    
    
# if you want it to be on the same string put (x, end=" "). a \n separates the numbers into different lines.
# putting print() makes each iteration be on different lines.



# example: make a rectangle of a symbol that the user inputs

rows = int(input("Enter the # of rows: "))
columns = int(input("Enter the # of columns: "))
symbol = input("Enter a symbol to use: ")

for ex in range(rows):
    for ey in range(columns):
        print(symbol, end=" ")
    print()