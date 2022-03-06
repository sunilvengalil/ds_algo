import numpy as np
from scipy.signal import correlate2d


def insert_zeros(r, s):
    zero_inserted = np.zeros((s + 1) * r.shape[0])
    for i in range(r.shape[0]):
        zero_inserted[(s + 1) * i] = r[i]
    return zero_inserted


def deconv(x: np.ndarray, w: np.ndarray, stride=(1, 1)) -> np.ndarray:
    result = np.zeros(tuple([2 * s for s in x.shape]))
    for i in range(0, x.shape[0], stride[0]):
        for j in range(0, x.shape[1], stride[1]):
            result[i:i + 3, j:j + 3] += x[i, j] * w
    return result


def deconv_with_insert_zeros(x, w, stride=(1, 1)):
    result_1 = np.zeros(tuple([s * im_dim for (s, im_dim) in zip(stride, x.shape)]))
    for i in range(x.shape[0]):
        ai_zero_inserted = insert_zeros(x[i], stride[1] - 1)
        result_1[stride[0] * i, :] = ai_zero_inserted
    return correlate2d(result_1, w)


a = np.asarray([[1, 2, 3, 4, 5, 6], [4, 3, 2, 1, 5, 6], [3, 2, 1, 4, 5, 6], [2, 3, 4, 1, 5, 6], [1, 2, 3, 4, 5, 6],
                [1, 2, 3, 4, 5, 6]],
               dtype=np.float64)
k = np.asarray([[1.0, 1.0, 1.0],
                [1.0, 2.0, 1.0],
                [1.0, 1.0, 1.0]],
               dtype=np.float64)
print("Kernel")
print(k)
print("Image")
print(a)
print(deconv(a, k))
print(deconv_with_insert_zeros(a, k))
print( "Stride 2")
print(deconv(a, k, (2,2)))
print(deconv_with_insert_zeros(a, k, (2, 2)))