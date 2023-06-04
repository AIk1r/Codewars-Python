def transpose(matrix):
    zip_mat = zip(*matrix)
    trans_matrix = [list(i) for i in zip_mat]
    return trans_matrix
