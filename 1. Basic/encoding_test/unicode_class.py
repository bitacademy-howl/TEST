from datetime import datetime

import numpy
import pyparsing

a = numpy.unicode(datetime.now())
b = pyparsing.unicode(datetime.now())


print(a, type(a))
print(b, type(b))