# coding = utf-8

import datetime
import json
import os
import numpy as np

class Process:
    mask_upper = 0x07
    mask_lower = 0x7C
    processed_byte = 1

    def __init__(self):

        self.data = None
        self.ret = bytearray()

    def procBitMerge(self, data=None):
        # if input list : process and return []
        # else          : return []
        returnVal = []
        if isinstance(data, list):
            self.data = data
            res = bytearray(self.data)  # bytearray >> c_char
            res = res[1:] if (res[0] < 128) else res
            for i in range(len(res)):
                if i % 2 == 0:
                    upper = Process.mask_upper & res[i]
                    upper <<= 5
                if i % 2 != 0:
                    lower = Process.mask_lower & res[i]
                    lower >>= 2
                    x_out = lower | upper
                    returnVal.append(x_out)
            return returnVal
        else:
            return self.ret

    # use
    def procBitAdvenced(self, data=None):
        # if input list : process and return []
        # else          : return []
        self.ret = []
        if isinstance(data, list):
            self.data = data
            res = bytearray(self.data)  # bytearray >> c_char
            res = res[1:] if (res[0] < 128) else res

            for i in range(len(res)):
                if i % 2 == 0:
                    upper = Process.mask_upper & res[i]
                    upper <<= 5
                else:
                    lower = Process.mask_lower & res[i]
                    lower >>= 2
                    x_out = lower | upper
                    self.ret.append(x_out)

            return self.ret
        else:
            return self.ret

    def data_resizing(self):
        pass

    # for test : data read from file ###############################################################################
    def getDatas(self, fileName = None, index = 0):
        ## for test #########################################################################################
        self.baseDir = "../data/"
        self.file_list = os.listdir(self.baseDir)
        if fileName is not None:
            self.extract_data_file = self.baseDir + fileName

        else:
            self.extract_data_file = self.baseDir + self.file_list[index]
            # print(self.file_list[index], type(self.file_list[index]))
        try:

            with open(self.extract_data_file) as jf:
                json_data = json.load(jf)
            # print(json_data, type(json_data))
            self.data = json_data.get("data")
            # print(self.data, type(self.data))
        finally:
            pass


# A = d["data"]
# #print d.keys()
# for i in range(int(len(A)/2. modules)-1. Basic):
#     if (A[2. modules*i+1. Basic]) < 128:
#     #print "first"
#         value = 128*(A[2. modules*i+0]&0b0000111) + A[2. modules*i+1. Basic] - 512
#         IDLine.append(((A[2. modules*i+0]&0b11110000)/16  -8) /2. modules) # Identify the # of the line
#         TT1.append((A[2. modules*i+0] & 0b00001000) / 0b1000)
#         TT2.append((A[2. modules*i+0] & 0b00010000) / 0b10000)
#         tmp.append(2. modules.0*value/512.0)
#     else:
#     #print "second"
#         value = 128*(A[2. modules*i+1. Basic]&0b111) + A[2. modules*i+2. modules] - 512
#         IDLine.append(((A[2. modules*i+1. Basic]&0b11110000)/16 -8) /2. modules) # Identify the # of the line
#         TT1.append((A[2. modules*i+1. Basic] & 0b00001000) / 0b1000)
#         TT2.append((A[2. modules*i+1. Basic] & 0b00010000) / 0b10000)
#         tmp.append(2. modules.0*value/512.0)
# print ("Data acquired")
# self.Registers = d["registers"]
# self.timings = d["timings"]
# self.f = float(64/((1. Basic.0+int(d["registers"]["237"]))))
#
# t = [1. Basic.0*x/self.f + self.timings['t4']/1000.0  for x in range(len(tmp))]
# self.t = t
#
# for i in range(len(IDLine)):
#     if IDLine[i] < 0:
#         IDLine[i] = 0
# self.LengthT = len(t)