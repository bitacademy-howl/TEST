from datetime import datetime as dt

from VO.VO_win_python_3 import DDD_File, DDD_Header
from un0rick_test.process import Process

bytearray()

def testMain3(self):
    start = dt.now()

    pc = Process()

    print(self.UN0RICK.Nacq)

    result_original = []
    result_enveloped = []


    for y in range(0, self.Y, 1):
        for x in range(0, self.X, 1):
            data_original = pc.procBitAdvenced(self.single())
            data_enveloped = self.UN0RICK.managingValue(data_original)

            result_original.extend(data_original)
            result_enveloped.extend(data_enveloped)

            if (x % 100 == 0):
                print("X:{0}, Y:{1}".format(x, y))

    # 헤더 정보 산출 ####################################################################################################
    level = Process.processed_byte * 256
    depth = len(result_original) / (self.X * self.Y)
    v = 1.3

    ddd = DDD_File(path= str(start) + "-original",
                   header = DDD_Header(WIDTH=self.X, HEGHIT=self.Y, DEPTH=depth, LEVEL=level, SAMPLING_RATE=self.UN0RICK.sampling_rate, US_VALOCITY=v),
                   data = result_original)
    ddd.Save()

    ddd_enveloped = DDD_File(path= str(start) + "-enveloped",
                             header = DDD_Header(WIDTH=self.X, HEGHIT=self.Y, DEPTH=depth, LEVEL=level, SAMPLING_RATE=self.UN0RICK.sampling_rate, US_VALOCITY=v),
                             data = result_original)
    ddd_enveloped.Save()

    print(ddd.GetHeader(), ddd_enveloped.GetHeader())
    ####################################################################################################################

    end = dt.now()
    delta = end - start

    print("Total Processor takes time {0} ".format(str(delta)))
