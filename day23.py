import numpy as np


def create_position_matrix(seq_length, embed_size):
    position_matrix = np.zeros((seq_length, embed_size))
    position_matrix[:, 0::2] = [[np.sin(pos/np.power(10000, i/embed_size))
                                 for i in range(0, embed_size, 2)] for pos in range(seq_length)]
    position_matrix[:, 1::2] = [[np.cos(pos/np.power(10000, i/embed_size))
                                 for i in range(1, embed_size, 2)] for pos in range(seq_length)]
    return position_matrix


# Test
seq_length = 10
embed_size = 16
position_matrix = create_position_matrix(seq_length, embed_size)
print(position_matrix)
