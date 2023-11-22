class Matrix:
    def __init__(self, matrix_list_1, matrix_list_2):
        self.result_matrix = [[0, 0, 0] for _ in range(3)]
        self.matrix_list_1 = matrix_list_1
        self.matrix_list_2 = matrix_list_2

    def add_matrices(self):
        self.result_matrix = [
            [a + b for a, b in zip(row1, row2)]
            for row1, row2 in zip(self.matrix_list_1, self.matrix_list_2)
        ]

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, row)) for row in self.result_matrix])
matrix_instance = Matrix([[5, 18, 11], [6, 17, 23], [41, 30, 9]], [[5, 18, 11], [6, 17, 23], [41, 50, 9]])
matrix_instance.add_matrices()
print(matrix_instance)
