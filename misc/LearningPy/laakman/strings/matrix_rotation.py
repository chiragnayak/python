
class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix
        self.order = len(self.matrix)
        self.rows = len(self.matrix)
        self.columns = len(self.matrix[0])

        if self.rows != self.columns:
            raise Exception("Not a NxN matrix")
        else:
            print(f"It is {self.rows} x {self.columns} matrix !!")

    def rotate(self):
        N = self.order -1
        rotated = [[0 for _ in range(self.columns)] for _ in range(self.rows)]
        for c in range(0, len(self.matrix)):
            for r in range(0, len(self.matrix[c])):
                new_r, new_c = c, N- r # this is important
                rotated[new_r][new_c] = self.matrix[r][c]

        self.matrix = rotated
        return rotated

    def rotate_in_place(self):
        """
        TODO
        :return:
        """
        n = len(self.matrix)
        for layer in range(int(n/2)):
            first = layer
            last = n - 1 - layer
            for col in range(first, last):
                print("processing", (first, col))

                # save top
                temp = self.matrix[first][col]

                # move left
                #self.swap(self.matrix, first, col)

                # move bottom

                # move right

                # shift top

                continue

    def swap(self, matrix, oldRow, oldCol):
        self.print_matrix(matrix)
        newRow = oldCol
        newCol = len(matrix) - 1 - oldRow
        temp = matrix[oldRow][oldCol]
        matrix[oldRow][oldCol] = matrix[newCol][newRow]
        matrix[newRow][newCol] = temp
        print((oldRow, oldCol), (newRow, newCol))
        self.print_matrix(matrix)

    def print_matrix(self, matrix: [[]]):
        print("=" * 10)
        for r in range(0, len(matrix)):
            for c in range(0, len(matrix[r])):
                print(matrix[r][c], end=" ")
            print("")
        print("=" * 10)


if __name__ == "__main__":
    m = [
        [1, 2, 3, 0],
        [4, 5, 6, 0],
        [7, 8, 9, 0],
        [10, 11, 12, 0]
    ]

    o = Matrix(m)
    o.print_matrix(m)

    # approach # 1
    # o.rotate()
    # o.print(o.matrix)
    # o.rotate()
    # o.print(o.matrix)
    # o.rotate()
    # o.print(o.matrix)
    # o.rotate()
    # o.print(o.matrix)

    # approach # 2
    o.rotate_in_place()