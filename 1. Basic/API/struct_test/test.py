# /usr/bin/env python

import struct


def main(argv=None):
    # write a file
    binfile = open('bin.dat', 'wb')
    for num in range(50):
        data = struct.pack('i', num)  # pack 'num' with a integer size
        binfile.write(data)

    # read the file
    binfile = open('bin.dat', 'rb')
    intsize = struct.calcsize('i')
    while 1:
        data = binfile.read(intsize)
        if data == '':
            break
        num = struct.unpack('i', data)
        print(num)


if __name__ == '__main__':
    main()