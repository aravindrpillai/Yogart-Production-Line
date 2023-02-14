_time = [
    [0,0.83,0,0,1.00,0],
    [0,1.67,0,0,0,1.00],
    [4.17,5.00,0,2.08,0,1.08],
    [0.83,1.67,5.33,0,0,1.67],
    [0,1.00,0,0,1.67,0],
    [0.42,1.67,3.33,1.25,0,1.67],
    [5.00,0,0,0,4.17,0],
    [0,0,0,1.25,0,0],
    [0.50,0,5.42,0,0,2.50],
    [1.00,0,0,1.67,2.08,0],
    [0,1.33,0,4.50,2.50,0],
    [0,0,1.67,0,0,0],
    [0,4.17,0,1.67,1.33,0],
    [1.67,0,0,0,0.83,1.00],
    [1.83,0,0,0,0,0],
    [0,0,6.31,3.69,1.00,0],
    [0,3.00,0,0,0,3.00],
    [0.70,0,0,5.40,2.50,0]
]

def time(i):
    if(i < 1):
        raise Exception("i cannot be less than 1")
    if(i > 6):
        raise Exception("i cannot be greater than 6")
    sum = 0
    for indx in range(0, 18):
        sum += _time[indx][i-1]
    return sum