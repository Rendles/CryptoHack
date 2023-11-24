import numpy as np

state = np.asarray([
    [206, 243, 61, 34],
    [171, 11, 93, 31],
    [16, 200, 91, 108],
    [150, 3, 194, 51],
])

round_key = np.asarray([
    [173, 129, 68, 82],
    [223, 100, 38, 109],
    [32, 189, 53, 8],
    [253, 48, 187, 78],
])


def matrix2bytes(matrix):
    arr = np.asarray(matrix, dtype=np.int8)
    arr_flatten = arr.flatten()
    arr_bytes = arr_flatten.tobytes()
    return arr_bytes


def add_round_key(s, k):
    assert s.shape == k.shape, "EEEEEEEEEEEEEEEEEEEEEEBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB"
    text = np.bitwise_xor(s, k)
    return text


matrix_xor = add_round_key(state, round_key)
matrix_to_bytes = bytes.decode(matrix2bytes(matrix_xor))


# print(matrix_to_bytes)

