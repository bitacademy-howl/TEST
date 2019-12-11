import numpy as np

class proc:

    mask_upper = 0x07
    mask_lower = 0x7C

    @classmethod
    def procBitMerge(cls, data=None):
        # if input list : process and return []
        # else          : return []
        # returnVal = []
        # ret = bytearray()
        arr = array('L')
        # arr = np.ndarray([1], dtype=np.uint8)

        if isinstance(data, list):
            arr = np.array(data, dtype=np.uint8)

            res = bytearray(data)
            res = res[1:] if (res[0] < 128) else res
            for i in range(len(data) - 2):
                if i % 2 == 0:
                    upper = proc.mask_upper & res[i]
                    upper <<= 5
                if i % 2 != 0:
                    lower = proc.mask_lower & res[i]
                    lower >>= 2
                    x_out = lower | upper
                    np.append(arr=arr, values=x_out)
            return arr
        else:
            return []