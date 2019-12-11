import numpy as np

from VO.VO_win_python_3 import DDD_File, DDD_Header

if __name__ == "__main__":

    # Random Data Generation ###########################################################################################

    # DATA 1 -> Windows, 3.7
    # data = np.random.randint(0, 256, size = (192, 192, 521)).astype(np.uint8)
    data = np.random.randint(0, 256, size=(192, 192, 521), dtype=np.uint8)
    data = list(data.reshape(-1))

    # DATA 2 -> linux, ??? --------------> Segmentation fault
    data = list(np.random.randint(0, 256, size=19206144, dtype=np.uint8))

    ####################################################################################################################

    # Write Example ####################################################################################################

    # usage 1
    # DDD1 = DDD_File()
    # DDD1.SetHeader(DDD_Header(WIDTH=192, HEGHIT=192, DEPTH=521, LEVEL=256, SAMPLING_RATE=80, US_VALOCITY=1.3))
    # DDD1.SetData(data)
    # DDD1.Save()

    # # usage 2
    DDD1 = DDD_File(header=DDD_Header(WIDTH=192, HEGHIT=192, DEPTH=521, LEVEL=256, SAMPLING_RATE=80, US_VALOCITY=1.3))
    # print(DDD1.GetHeader())
    DDD1.SetData(data)
    # print(DDD1.GetData())
    DDD1.Save()
    ####################################################################################################################

    # Read Example #####################################################################################################
    DDD2 = DDD_File(DDD1.path)
    DDD2.Load()
    ####################################################################################################################

    # check the data & header ##########################################################################################
    print(DDD1.GetHeader())
    print(DDD1.path)

    a = np.array(DDD1.GetData()).reshape(DDD1.GetHeader().GetWidth(), DDD1.GetHeader().GetHeight(), DDD1.GetHeader().GetDepth())
    print(a.shape, a[191][191][520])

    print(DDD1.GetHeader())
    print(DDD2.path)
    b = np.array(DDD2.GetData()).reshape(DDD2.GetHeader().GetWidth(), DDD2.GetHeader().GetHeight(), DDD2.GetHeader().GetDepth())
    print(b.shape, b[191][191][520])
    ####################################################################################################################

    # # error Test
    # DDD3 = DDD_File()
    # DDD3.SetHeader(3)
    # print(DDD3.GetHeader())