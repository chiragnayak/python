

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
        N = self.order-1
        rotated = list(list())
        for c in range(0, len(self.matrix)):
            for r in range(0, len(self.matrix[c])):
                new_r, new_c = c, N-r
                rotated[new_r][new_r] = self.matrix[r][c]
                self.print(rotated)

    def print(self, matrix : [[]]):
        print("=" * 10)
        for r in range(0, len(matrix)):
            for c in range(0, len(matrix[r])):
                print(matrix[r][c], end=" ")
            print("")
        print("=" * 10)

if __name__=="__main__":

    m = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]

    o = Matrix(m)
    o.print(m)
    o.rotate()
    o.print()