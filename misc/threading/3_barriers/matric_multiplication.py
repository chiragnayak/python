m1 = [[2, 3, 4],
      [5, 6, -3]
      ]

m2 = [[1, 2, 3],
      [4, 5, 5],
      [5, 2, 1]
      ]

m3 = []


def print_me(m):
    print("======")
    for r in range(0, len(m)):
        for c in range(0, len(m[0])):
            print(f"{m[r][c]} ", end=" ")
        print("")
    print("======")


def matrix_multiply(first, second):
    m1_row = len(first)
    m1_col = len(first[0])

    m2_row = len(second)
    m2_col = len(second[0])

    for _ in range(0, m1_row):
        m3.append([])

    print(f"{m1_row}x{m1_col} * {m2_row}x{m2_col}")

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



matrix_multiply(m1, m2)
print_me(m1)
print_me(m2)
