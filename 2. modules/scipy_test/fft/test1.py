import matplotlib.pyplot as plt

def proc_test_data():

    from VO.DDD import DDD_File

    ddd1 = DDD_File(path="./data/20191204original.ddd")
    ddd1.Load()

    fig = plt.figure()
    ax1 = fig.add_subplot(2, 1, 1)
    ax2 = fig.add_subplot(2, 1, 2)

    signal1 = ddd1.GetData()[0:ddd1.GetHeader().GetDepth()]
    signal2 = envelope(signal1, bias=50)

    ax1.plot(signal1)
    ax2.plot(signal2)

    plt.show()