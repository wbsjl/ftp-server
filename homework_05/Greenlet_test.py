from greenlet import greenlet

def test1():
    print('run test1')
    gr2.switch()
    print('test1 finished ')
    gr2.switch()


def test2():
    print('run test2')
    gr1.switch()
    print('test2 finished ')



gr1 = greenlet(test1)
gr2 = greenlet(test2)
gr1.switch()
