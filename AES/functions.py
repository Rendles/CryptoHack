import numpy as np

def matrix2bytes(matrix):
    arr = np.asarray(matrix, dtype=np.int8)
    arr_flatten = arr.flatten()
    arr_bytes = arr_flatten.tobytes()
    return arr_bytes

def add_round_key(s, k):
    assert s.shape == k.shape, "EEEEEEEEEEEEEEEEEEEEEEBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB"
    text = np.bitwise_xor(s, k)
    return text