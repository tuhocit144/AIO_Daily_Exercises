import numpy as np


def correlation(vector1, vector2):
    # Tính toán hệ số tương quan
    ## Your code Here ##
    x_mean = np.mean(vector1)
    y_mean = np.mean(vector2)
    x_sub = X-x_mean
    y_sub = Y-y_mean
    tmp_tuso = np.sum(x_sub*y_sub)
    tmp_mauso = np.sqrt(np.sum(x_sub**2)*np.sum(y_sub**2))
    return tmp_tuso/tmp_mauso


if __name__ == '__main__':

    # Tạo hai mảng dữ liệu
    X = np.array([1, 2, 3, 4, 5])
    Y = np.array([2, 4, 6, 8, 10])
    print("Hệ số tương quan giữa X và Y là:", correlation(X, Y))
    # Tạo hai mảng dữ liệu mới
    X_new = np.array([10, 20, 30, 40, 50])
    Y_new = np.array([3, 15, 25, 35, 45])
    print("Hệ số tương quan giữa X_new và Y_new là:", correlation(X_new, Y_new))
