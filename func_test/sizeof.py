import sys

from un0rick_test.process import Process

a = [200, 40, 230, 50]

s_a = sys.getsizeof(a[0])

print(s_a)

pc = Process()
ac = pc.procBitAdvenced(a)

size_ac = sys.getsizeof(ac[0])
print(ac, size_ac)