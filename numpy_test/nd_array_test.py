import numpy as np
timespace_byte = bytearray([255, 3, 4, 0, 100])

ndarr_data1 = np.array(list(timespace_byte))

ndarr_data2 = np.array(timespace_byte)

print(ndarr_data1, ndarr_data2)
print(type(ndarr_data1), type(ndarr_data2))
print(ndarr_data1[0], ndarr_data2[0])
print(type(ndarr_data1[0]), type(ndarr_data2[0]))


