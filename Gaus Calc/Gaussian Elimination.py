#####V.3.4#####

"""Matrix Creation"""

matrix = [] #create empty, 1D array for matrix
row = []    #create empty array for row values


print("Enter the augmented matrix, one value at\n"
      "a time and row-by-row, for the system of\n"
      "equations you are trying to solve.\n"
      "Enter 'n' to move to the next row and 'f'\n"
      "when you are finished forming your matrix.\n")

rowNum = 1 #create row number counter
colNum = 1 #create column number counter
keepGoing = True
while keepGoing:
    matVal = input("Enter value for row {}, column {}.  ".format(rowNum, colNum))

    if matVal == "n":   #checks if user is done with row
        matrix.append(row)  #add row to matrix
        rowNum += 1             #move to next row creation
        colNum = 1          #reset column number
        row = []                #clear row       

    elif matVal == "f": #checks if user is done with matrix
        matrix.append(row) #add final 'row' to 'matrix'
        keepGoing = False #exit matrix formation

    else:
        try:
            row.append(float(matVal)) #attempts to convert input to float type
            colNum += 1     #move to next column

        except:
            print("Not a valid character. Try again.")  #if not a valid input, tell them

for row in range(len(matrix)):  #step through rows
    for col in range(len(matrix[row])): #step through columns within rows
        if matrix[row][col] == int(matrix[row][col]):   #check if value is integer
           matrix[row][col] = int(matrix[row][col]) #remove insignificant zeroes

print("\nYour matrix is:\n")    #
for row in range(len(matrix)):  #prints matrix in easy to read form
    print(matrix[row])          #

##################################################################

"""Gaussian Elimination"""

for row in range(len(matrix)):  #steps through rows
    for count in range(1, len(matrix)): #steps through each other row
        try:  #attempts to compare current row to next 'other' row below it
            multiple = matrix[row][row]             #assigns multiples as the target
            otherMult = matrix[row + count][row]    #column for each row

            if multiple != 0 and otherMult != 0: #checks that neither multiple is zero
                for col in range(len(matrix[row])): #steps through columns within rows
                    matrix[row + count][col] = (matrix[row][col] * otherMult -          #THE
                                                matrix[row + count][col] * multiple)    #MATHS
        except:
            "hi"    #allows the previous try function to run without error

    for count in range(1, len(matrix)):
        try:                                                                            #Does the
            multiple = matrix[row][row]                                                 #same thing
            otherMult = matrix[row - count][row]                                        #as previous
                                                                                        #block, but
            if multiple != 0 and otherMult != 0:                                        #compares
                for col in range(len(matrix[row])):                                     #current row
                    matrix[row - count][col] = (matrix[row][col] * otherMult -          #to each
                                                matrix[row - count][col] * multiple)    #'other' row
                                                                                        #above it
        except:                                                                         #
            "hi"

for row in range(len(matrix)):
    divisor = matrix[row][row]  #assigns divisor to reduce target value to 1
    for col in range(len(matrix[row])):
        try:    #keeps program from freaking out, in case target value is zero
            matrix[row][col] /= divisor     #MORE MATHS!

        except:
            "hi"

        if matrix[row][col] == int(matrix[row][col]):   #checks if value is integer
           matrix[row][col] = int(matrix[row][col]) #removes insignificant zeroes
        
print("\nYour matrix, in reduced row echelon form, is:\n")  #prints the reduced row echelon form
for row in range(len(matrix)):                              #of the matrix in easily read form
    print(matrix[row])
