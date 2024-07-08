
import numpy as np
np.random.seed(42)
# rng = np.random.default_rng(seed=42)
# B1: Tao tu dien va ma hoa tu
vocal = {
    "Tôi": 0,
    "thích": 1,
    "học": 2,
    "AI": 3
}
# So luong tu vung
vocal_size = len(vocal)
# kich thuoc vector embedding
embedding_dim = 4

# Khoi tao ma tran embedding ngau nhien    x = generator.standard_normal()

embedding_matrix = np.random.rand(vocal_size, embedding_dim)
print('embedding matrix:\n', embedding_matrix)
# Chuoi dau vao duoc ma hoa thanh cac vector embedding
input_seq = np.array([embedding_matrix[vocal[word]]
                     for word in ["Tôi", "thích", "học", "AI"]])
print('Chuỗi đầu vào (đã mã hoá):\n', input_seq)
# B2: Khoi tao cac ma tran trong so cho Q, K, V


W_q = np.random.rand(embedding_dim, embedding_dim)
W_k = np.random.rand(embedding_dim, embedding_dim)
W_v = np.random.rand(embedding_dim, embedding_dim)

# Tinh toan Q, K, V
Q = np.dot(input_seq, W_q)
K = np.dot(input_seq, W_k)
V = np.dot(input_seq, W_v)

print("Ma trận Query Q:\n", Q)
print("Ma trận Key K:\n", K)
print("Ma trận Value V:\n", V)

# B3: tinh toan Attention score
scores = np.dot(Q, K.T)

d_k = K.shape[1]
print('d_k=', d_k)
scores = scores/np.sqrt(d_k)
print("Điểm số scores: \n", scores)
# B4: ap dung ham sofmax


def softmax(x):
    x_exp = np.exp(x)
    soft_max_value = x_exp/x_exp.sum(axis=0)
    return soft_max_value


attention_weights = softmax(scores)
print("Trọng số Attention:\n", attention_weights)
# B5: tinh toan tong co trong so cua cac value
output = np.dot(attention_weights, V)
print("output:\n", output)
