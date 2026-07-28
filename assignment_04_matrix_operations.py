# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================
def read_matrix(rows, cols, name):
    print(f"Enter matrix {name}:")
    matrix = []
    for i in range(rows):
        row = list(map(int, input(f"Enter row {i + 1}: ").split()))
        matrix.append(row)
    return matrix


def print_matrix(matrix):
    for row in matrix:
        print(" ".join(str(val) for val in row))


def transpose(matrix, rows, cols):
    result = []
    for j in range(cols):
        new_row = []
        for i in range(rows):
            new_row.append(matrix[i][j])
        result.append(new_row)
    return result


def add_matrices(a, b, rows, cols):
    result = []
    for i in range(rows):
        new_row = []
        for j in range(cols):
            new_row.append(a[i][j] + b[i][j])
        result.append(new_row)
    return result


def multiply_matrices(a, b, m, n, p):
    result = []
    for i in range(m):
        new_row = []
        for j in range(p):
            total = 0
            for k in range(n):
                total += a[i][k] * b[k][j]
            new_row.append(total)
        result.append(new_row)
    return result


# --- Part A: Transpose ---
print("PART A: Transpose")
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
matrix = read_matrix(rows, cols, "")

print("\nOriginal Matrix:")
print_matrix(matrix)

transposed = transpose(matrix, rows, cols)
print("\nTransposed Matrix:")
print_matrix(transposed)

# --- Part B: Addition ---
print("\nPART B: Matrix Addition")
r = int(input("Enter number of rows for both matrices: "))
c = int(input("Enter number of columns for both matrices: "))
matrix_a = read_matrix(r, c, "A")
matrix_b = read_matrix(r, c, "B")

sum_result = add_matrices(matrix_a, matrix_b, r, c)
print("\nSum of Matrices:")
print_matrix(sum_result)

# --- Part C: Multiplication ---
print("\nPART C: Matrix Multiplication")
m = int(input("Enter rows of Matrix A: "))
n = int(input("Enter columns of Matrix A (= rows of Matrix B): "))
p = int(input("Enter columns of Matrix B: "))
matrix_a2 = read_matrix(m, n, "A")
matrix_b2 = read_matrix(n, p, "B")

product = multiply_matrices(matrix_a2, matrix_b2, m, n, p)
print("\nProduct of Matrices:")
print_matrix(product)
