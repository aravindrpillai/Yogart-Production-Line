_csetup = [
        [None,132.230,119.69,117.3,101.08,126.43,127.15,101.37,93.266,95.149,94.792,93.235,135.37,128.23,137.58,128.64,94.697,105.31],
        [None,None,97.835,132.4,126.25,137.75,122.54,106.39,108.76,97.916,121.85,117.24,123.51,108.86,103.01,104.86,122.5,108.53],
        [None,None,None,130.1,93.412,122.82,136.99,134.97,108.68,110.68,112.15,131.82,138.09,135.02,115.73,98.893,137.61,125.34],
        [None,None,None,None,138.21,127.12,131.64,105.69,114.2,118.02,93.319,97.266,98.149,99.172,121.82,124.54,112.89,98.418],
        [None,None,None,None,None,107.25,113.5,102.58,138.47,103.43,108.71,98.576,127.43,108.42,110.05,103.2,116.84,130.69],
        [None,None,None,None,None,None,121.49,111.65,107.1,129.21,102.46,93.402,108.7,135.87,114.33,112.89,93.324,113.31],
        [None,None,None,None,None,None,None,132.12,102.63,109.39,136.24,131.2,112.71,115.8,127.52,132.18,114.69,126.11],
        [None,None,None,None,None,None,None,None,119.24,91.549,121.47,96.699,91.928,94.515,96.31,134.07,110.88,139.74],
        [None,None,None,None,None,None,None,None,None,119.28,133.92,134.24,118.12,126.77,92.153,125,104.61,108.13],
        [None,None,None,None,None,None,None,None,None,None,122.08,115.74,108.62,90.236,108.55,127.78,104.48,126.54],
        [None,None,None,None,None,None,None,None,None,None,None,138.18,129.64,120.16,124.67,138.73,127.69,122.48],
        [None,None,None,None,None,None,None,None,None,None,None,None,129.76,137.84,136.79,110.11,94.84,124.07],
        [None,None,None,None,None,None,None,None,None,None,None,None,None,109.87,113.88,96.564,93.846,90.381],
        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,96.455,126.24,126.05,122.71],
        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,134.98,128.25,137.26],
        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,122.9,120.66],
        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,129.15],
        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None]
]

def csetup(j, l):
    if(j<1 or j > 18):
        raise Exception("value of j must be within the range 1 to 18 ")
    if(l<1 or l > 18):
        raise Exception("value of l must be within the range 1 to 18 ")
    val = _csetup[j-1][l-1]
    return 0 if val == None else val