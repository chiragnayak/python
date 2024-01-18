import random


class MatrixGenerator:

    def __init__(self):
        self.matrix = []

    def getMatrix(self, row, col):
        self.matrix = []
        for _ in range(0, row):
            self.matrix.append([])

        for r in self.matrix:
            for c in range(col):
                r.append(random.randint(-10, 10))

        # print(self.matrix)

        return self.matrix

    def print_me(self):
        print("======")
        for r in range(0, len(self.matrix)):
            for c in range(0, len(self.matrix)):
                print(f"{self.matrix[r][c]} ", end=" ")
            print("")
        print("======")


class MatrixMultiplication:

    debug = False

    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2
        self.product = []

    def print_me(self, m):
        print("======")
        for r in range(0, len(m)):
            for c in range(0, len(m[0])):
                print(f"{m[r][c]} ", end=" ")
            print("")
        print("======")

    def matrix_multiply(self):
        m1_row = len(self.m1)
        m1_col = len(self.m1[0])

        m2_row = len(self.m2)
        m2_col = len(self.m2[0])

        if m1_col != m2_row:
            print("Matrix multiplication not possible. Required : m,n p,q --> n==p  result --> m,q")

        for _ in range(0, m1_row):
            self.product.append([])

        for row in self.product:
            for col in range(0, m2_col):
                row.append(0)

        if self.debug:
            print(f"{m1_row}x{m1_col} * {m2_row}x{m2_col}")

        if self.debug:
            # multiplication
            for row_1 in range(0, m1_row):
                for col_1 in range(0, m1_col):
                    print(f"({row_1},{col_1})", end=" ")
                print("")
            print("-------------")
            for col_2 in range(0, m2_col):
                for row_2 in range(0, m2_row):
                    print(f"({row_2},{col_2})")
                print("")

        for row_1 in range(0, m1_row):
            for col_1 in range(0, m1_col):
                if self.debug: print(f"({row_1, col_1})", end=" = ")
                for pointer in range(0, m1_col):
                    self.product[row_1][col_1] += self.m1[row_1][pointer] * self.m2[pointer][col_1]
                    if self.debug: print(f"({row_1, pointer} * {pointer, col_1})", end=" + ")
                if self.debug: print("-----")


if __name__ == "__main__":

    mg = MatrixGenerator()
    m1 = mg.getMatrix(3000, 3000)
    m2 = mg.getMatrix(3000, 3000)

    mm = MatrixMultiplication(m1, m2)
    mm.print_me(m1)
    mm.print_me(m2)
    mm.matrix_multiply()
    mm.print_me(mm.product)
