import struct



num = 1.3
print(type(num))
a = struct.pack("d", num)
with open("a.d", "wb") as f:
    f.write(a)


with open("a.d", "rb") as f:
    b = f.read(struct.calcsize("d"))
    res = struct.unpack("d", b)
    print(res[0])
    print(struct.calcsize('d'))
