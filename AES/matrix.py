import numpy as np

def bytes2matrix(text):
    """ Converts a 16-byte array into a 4x4 matrix.  """
    return [list(text[i:i+4]) for i in range(0, len(text), 4)]


def matrix2bytes(matrix):
    arr = np.asarray(matrix, dtype=np.int8)
    arr_flatten = arr.flatten()
    arr_bytes = arr_flatten.tobytes()
    return arr_bytes


matrix = [
    [99, 114, 121, 112],
    [116, 111, 123, 105],
    [110, 109, 97, 116],
    [114, 105, 120, 125],
]

bytes_str = matrix2bytes(matrix)
bytes_to_smt = bytes.decode(bytes_str)


# print(bytes_to_smt)
