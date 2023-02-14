_inv = [
    [0,0,0,0,0,0],
    [0,20,0,0,0,0],
    [0,10,0,5,0,0],
    [0,0,14,2,0,0],
    [0,0,0,0,0,0],
    [0,0,0,5,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [4,0,5,5,0,0],
    [0,0,0,0,2,0],
    [0,4,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,3,0],
    [15,10,5,0,0,0],
    [2,2,2,2,0,0],
    [0,0,3,0,0,0],
    [0,0,0,0,0,0],
    [5,0,0,0,2,0]
]


def inv(i, j):
    if(i< 1 or i > 6):
        raise Exception("value of i must be within 1 to 6")
    if(j< 1 or i > 18):
        raise Exception("value of j must be within 1 to 18")
    return _inv[j-1][i-1]