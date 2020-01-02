
x = [1,2,3,4,5]

def proc(x):
    x[0:2] = [0,1]
    return [3, 4]

print(x, proc(x))
x[0:2] = proc(x)
print(x)


