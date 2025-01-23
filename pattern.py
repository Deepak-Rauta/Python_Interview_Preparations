def pattern(n):
    # outer loop to handel number of rows:
    for i in range(0, n):

        #inner loop to handle the number of column:
        for j in range(0, i+1):
            print("*", end=" ") # end =" " that means print() function allows you to specify what character or String should be print at the end of each line.
            print("\r")
n = 5
pattern(n)            

