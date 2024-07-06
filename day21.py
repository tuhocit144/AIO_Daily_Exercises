import numpy as np
import math
# Bước 1: Tạo tập tài liệu mẫu
documents = ["Tôi thích học AI", "AI là trí tuệ nhân tạo",
             "AGI là siêu trí tuệ nhân tạo"]

# Bước 2: Tiền xử lý- tách từ và tính tần số


def compute_tf(doc=documents):
    var_tmp = [x.strip().split() for x in doc]
    result = []
    for d in var_tmp:
        d_hist = []
        length = len(d)
        for x in d:
            d_hist.append(d.count(x)/length)
        result.append(d_hist)
    # print(result)
    return result

 ## Your code here ##
# Bước 3: Tính toán IDF


def compute_idf(docs=documents):
    # tong so tai lieu D
    n_doc = len(docs)
    var_tmp = [x.strip().split() for x in docs]
    result = []
    for d in var_tmp:
        d_hist = []
        for x in d:
            x_counter = 0
            for t in var_tmp:
                if (t.count(x) > 0):
                    x_counter += 1
            d_hist.append(np.log(n_doc/(1+x_counter)))
        result.append(d_hist)
    return (result)
# Your code here ##
# Bước 4: Tính toán TF-IDF


def compute_tf_idf(tf, idf):
    tf_idf = []
    length = len(tf)
    for k in range(length):
        var_tmp = np.array(tf[k])*np.array(idf[k])
        tf_idf.append(var_tmp)
    return tf_idf


def print_result(docs, mt_tf_idf):
    var_tmp = [x.strip().split() for x in docs]
    n_docs = len(var_tmp)
    for k in range(n_docs):
        print('-'*50)
        print('Doc 1:', var_tmp[k])
        lenght = len(var_tmp[k])
        for i in range(lenght):
            print(f'{var_tmp[k][i]}: {mt_tf_idf[k][i]:.4f}')


if __name__ == "__main__":
    tf = compute_tf()
    idf = compute_idf()
    tf_idf = compute_tf_idf(tf, idf)
    print_result(documents, tf_idf)
