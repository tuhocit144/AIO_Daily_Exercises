# Bai 1
import numpy as np
rng = np.random.default_rng(42)


def create_matrix(row=3, col=3):
    a = rng.integers(0, 21, size=(row, col))
    return a


matrix = create_matrix(3, 3)
print("Ma trận 3x3 với các giá trị nguyên ngẫu nhiên từ 0 đến 10:")
print(matrix)
# Bai 2 Phep cong hai ma tran
matrix1 = create_matrix()
matrix2 = create_matrix()
print('Tong hai ma tran:')
print(matrix1)
print(matrix2)
sum_matrix = np.add(matrix1, matrix2)
print(sum_matrix)
# Bai 3 Phep nhan 2 ma tran
matrix1 = create_matrix()
matrix2 = create_matrix()
print('Tich hai ma tran:')
print(matrix1)
print(matrix2)
multi_matrix = np.multiply(matrix1, matrix2)
print(multi_matrix)
# Bai 4. Ma tran chuyen vi
matrix_c4 = create_matrix()
matrix_c4_transform = np.transpose(matrix_c4)
print('Ma tran chuyen vi cua ma tran: \n', matrix_c4,
      ' \nla ma trận: \n', matrix_c4_transform)

# Bai 5. Ma tran nghich dao
matrix = create_matrix()
try:
    matrix_inverse = np.linalg.inv(matrix)
    print('\nMa tran nghich dao cua ma tran: \n',
          matrix, '\nla ma tran: \n', matrix_inverse)
except np.linalg.LinAlgError:
    print('Ma tran khong kha nghich')

# Bai 6. Tinh dinh thuc ma tran
matrix = create_matrix()
det_matrix = np.linalg.det(matrix)
print('Dinh thuc cua ma tran la:\n', det_matrix)
