# cosine similarity
# Bai tap 1: Tinh tong tung cot trong ma tran
import numpy as np


def sum_coloumn_of_matrix(A):
    column_sum = np.einsum('ij->j', A)
    return column_sum

# Bai tap 2: tinh tich vo huong cua 2 ma tran


def dot_2_matrix(A, B):
    dot_product = np.einsum('ij,ij->', A, B)
    return dot_product
# BT3:Tinh tong cac phan tu tren duong cheo chinh cua ma tran


def sum_diagonal_matrix(A):
    sum_diagonal = np.einsum('ii->', A)
    return sum_diagonal
# BT4 nhan 2 ma tran


def multiply_2matrix(A, B):
    multiply = np.einsum('ij,jk->ik', A, B)
    return multiply

# BT 5 outer product


def outer_product(A, B):
    outer = np.einsum('i,j->ij', A, B)
    return outer

# BT6: tinh ma tran Gram của 1 Tensor 3D


def gram_matrix(tensor):
    # tensor có shape ( channels , height , width )
    channels, height, width = tensor.shape
    features = tensor.reshape(channels, height * width)
    gram = np.einsum('ik,jk->ij', features, features)
    return gram


# main
if __name__ == '__main__':
    # bt1
    A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(f'Sum of each colum is: {sum_coloumn_of_matrix(A)}')
    # bt2
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])
    print(f'dot_2_matrix is: {dot_2_matrix(A, B)}')
    # bt3
    print(f'Sum of diagonal_matrix is: \n{sum_diagonal_matrix(A)}')
    # bt4
    print(f'Multiply of 2_matrix is:\n {multiply_2matrix(A, B)}')
    # bt5
    A = np.array([1, 2, 3])
    B = np.array([4, 5, 6])
    print(f'Outer product of 2_matrix is:\n {outer_product(A, B)}')
    # bt6
    rng = np.random.default_rng(42)
    tensor = rng.random((3, 4, 4))  # ví dụ tensor ngẫu nhiên
    gram = gram_matrix(tensor)
    print(gram)
