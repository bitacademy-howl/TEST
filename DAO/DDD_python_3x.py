import os
import struct
from datetime import datetime
import numpy as np

class DDD_Header:

    def __init__(self, WIDTH:int = None, HEGHIT:int = None, DEPTH:int = None, LEVEL:int=None, SAMPLING_RATE:int=None, US_VALOCITY:float=None):
        self.SetAll(WIDTH=WIDTH, HEGHIT=HEGHIT, DEPTH=DEPTH, LEVEL=LEVEL, SAMPLING_RATE=SAMPLING_RATE, US_VALOCITY=US_VALOCITY)

    def SetAll(self, WIDTH:int = None, HEGHIT:int = None, DEPTH:int = None, LEVEL:int=None, SAMPLING_RATE:int=None, US_VALOCITY:float=None):
        self.SetWidth(WIDTH)
        self.SetHeight(HEGHIT)
        self.SetDepth(DEPTH)
        self.SetLevel(LEVEL)
        self.SetSamplingRate(SAMPLING_RATE) # MHz [ UNIT : sample / s ]
        self.SetVelocityDouble(US_VALOCITY) # [ UNIT : us / 2T ( T = mm ) ]

        self._SetCaluclationFactor()

    def _SetCaluclationFactor(self):
        # Calculated Factors ###########################################################################################
        self._SetTRange()
        self._SetTLabel()
        ################################################################################################################
    def GetCaluclationFactor(self):
        return [self.GetTRange(), self.GetTLabel()]

    def SetWidth(self, WIDTH : int):
        self.__WIDTH = WIDTH
    def GetWidth(self) -> int:
        return self.__WIDTH

    def SetHeight(self, HEIGHT : int):
        self.__HEIGHT = HEIGHT
    def GetHeight(self) -> int:
        return self.__HEIGHT

    def SetDepth(self, DEPTH : int):
        self.__DEPTH = DEPTH
    def GetDepth(self) -> int:
        return self.__DEPTH

    def SetLevel(self, LEVEL : int):
        self.__LEVEL = LEVEL
    def GetLevel(self) -> int:
        return self.__LEVEL

    def SetSamplingRate(self, SAMPLING_RATE : int = 80):
        self.__SAMPLING_RATE = SAMPLING_RATE
    def GetSamplingRate(self):
        return self.__SAMPLING_RATE

    def SetVelocityDouble(self, VELOCITY_DOUBLE = 1.3):
        self.__US_VELOCITY_DOUBLE = VELOCITY_DOUBLE
    def GetVelocityDouble(self):
        return self.__US_VELOCITY_DOUBLE

    def _SetTRange(self):
        self.__T_RANGE = np.arange(0, self.__DEPTH + 1, self.__DEPTH / 10)
    def GetTRange(self):
        return self.__T_RANGE

    def _SetTLabel(self):
        self.__T_Label = np.round(self.__T_RANGE / (self.__SAMPLING_RATE * self.__US_VELOCITY_DOUBLE), 1)
    def GetTLabel(self):
        return self.__T_Label

    def __str__(self):
        return "WIDTH = {0}\nHEGHIT = {1}\nDEPTH = {2}\nLEVEL = {3}\nSAMPLING_RATE = {4}\nUS_VALOCITY = {5}"\
            .format(self.GetWidth(),
                    self.GetHeight(),
                    self.GetDepth(),
                    self.GetLevel(),
                    self.GetSamplingRate(),
                    self.GetVelocityDouble())

    def __repr__(self):
        return "DDD_Header(WIDTH = {}, HEGHIT = {}, DEPTH = {}, LEVEL = {}, SAMPLING_RATE = {}, US_VALOCITY = {})".format(
            self.GetWidth(),
            self.GetHeight(),
            self.GetDepth(),
            self.GetLevel(),
            self.GetSamplingRate(),
            self.GetVelocityDouble()
        )

class DDD_File:
    def __init__(self, path = None, header=None, data = None):
        # initialize ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        if path is not None and isinstance(path, str):
            self.__path = path
        else:
            self.__path = self.__getctime() + ".ddd"

        self.SetHeader(header)
        self.SetData(data)

    def SetHeader(self, header : DDD_Header = None):
        if isinstance(header, DDD_Header):
            self.__header = header
        elif header == None:
            pass
        else:
            raise TypeError("Type Must Be Class of DDD_HEADER")
    def GetHeader(self) -> DDD_Header :
        return self.__header
    def IsHeader(self):
        return True if self.GetHeader() != None else False

    def SetData(self, data : list):
        self.__data = data
    def GetData(self) -> list:
        return self.__data

    def Save(self, path = None):
        if path == None:
            path = self.__path

        _, extention = os.path.splitext(path)
        if extention != ".ddd":
            raise Exception

        if self.GetHeader() == None:
            raise NoneHeaderException

        pixel_size = round(self.__header.GetLevel() / 256)
        if len(self.__data) == (self.__header.GetWidth() * self.__header.GetHeight() * self.__header.GetDepth() * pixel_size):
            with open(self.__path, "wb") as f:
                f.write(struct.pack('5i', self.__header.GetWidth(), self.__header.GetHeight(), self.__header.GetDepth(), self.__header.GetLevel(), self.__header.GetSamplingRate()))
                f.write(struct.pack('d', self.__header.GetVelocityDouble()))
                f.write(bytearray(self.__data))

    def Load(self, path = None):
        if path == None:
            path = self.__path
        if path is not None and isinstance(path, str):
            self.__path = path
            _, extention = os.path.splitext(self.__path)

        if extention == ".ddd":

            with open(self.__path, "rb") as f:
                headlist = [f.read(struct.calcsize('i')), f.read(struct.calcsize('i')), f.read(struct.calcsize('i')), f.read(struct.calcsize('i')), f.read(struct.calcsize('i')), f.read(struct.calcsize('d'))]
                w = struct.unpack("i", headlist[0])[0]
                h = struct.unpack("i", headlist[1])[0]
                d = struct.unpack("i", headlist[2])[0]
                l = struct.unpack("i", headlist[3])[0]
                sr = struct.unpack("i", headlist[4])[0]
                v = struct.unpack("d", headlist[5])[0]

                self.SetHeader(DDD_Header(WIDTH=w, HEGHIT=h, DEPTH=d, LEVEL=l, SAMPLING_RATE=sr, US_VALOCITY=v))
                self.SetData(bytearray(f.read()))

    def __getctime(self):
        date = datetime.now()
        ret = date.strftime("%Y%m%d-%H%M%S")   # return : str
        return ret

    # def __str__(self):
    #     return "WIDTH = {0}\nHEGHIT = {1}\nDEPTH = {2}\nLEVEL = {3}\nSAMPLING_RATE = {4}\nUS_VALOCITY = {5}"\
    #         .format(self.GetWidth(),
    #                 self.GetHeight(),
    #                 self.GetDepth(),
    #                 self.GetLevel(),
    #                 self.GetSamplingRate(),
    #                 self.GetVelocityDouble())
    #
    # def __repr__(self):
    #     return "DDD_Header(WIDTH = {}, HEGHIT = {}, DEPTH = {}, LEVEL = {}, SAMPLING_RATE = {}, US_VALOCITY = {})".format(
    #         self.GetWidth(),
    #         self.GetHeight(),
    #         self.GetDepth(),
    #         self.GetLevel(),
    #         self.GetSamplingRate(),
    #         self.GetVelocityDouble()
    #     )

class NoneHeaderException(Exception):
    def __str__(self):
        return "file with NoneType Header is not Allowed"