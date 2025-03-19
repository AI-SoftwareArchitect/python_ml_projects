import numpy as np
from numba import cuda

# Dizi oluşturma
arr = np.arange(100)

# CUDA cihazına veri gönderme
d_arr = cuda.to_device(arr)

# CUDA kerneli tanımlama
@cuda.jit
def kernel(arr):
    idx = cuda.grid(1)
    if idx < arr.shape[0]:
        arr[idx] *= 2

# CUDA kernelini çalıştırma
threads_per_block = 64
blocks_per_grid = (arr.shape[0] + (threads_per_block - 1)) // threads_per_block
kernel[blocks_per_grid, threads_per_block](d_arr)

# Sonuçları CPU'ya geri gönderme
result = d_arr.copy_to_host()

print(result)
