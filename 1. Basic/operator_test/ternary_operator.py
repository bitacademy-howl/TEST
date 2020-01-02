from VO.DDD_python_3x import DDD_File, DDD_Header

a = DDD_File(header=DDD_Header(1,2,3,4,5,0.5))
print(a.GetHeader())


def IsHeader(self):
    return True if self.GetHeader() != None else False

print(a.IsHeader())