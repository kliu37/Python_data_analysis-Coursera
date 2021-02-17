#trace
NUM_ROWS = 25
NUM_COLS = 25

# construct a matrix
my_matrix = []
for row in range(NUM_ROWS):
    new_row = []
    for col in range(NUM_COLS):
        new_row.append(row * col)
    my_matrix.append(new_row)
 
# print the matrix
for row in my_matrix:
    print(row)



def trace(matrix):
    sum_val = 0
    for i in range(len(matrix)):
        sum_val += matrix[i][i]
    return sum_val

print(trace(my_matrix))

