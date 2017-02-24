import datadump as dd
import random
import os

def test_wd():
    assert dd.wd() == 'tmp/'
    dd.swd('dir1')
    assert dd.wd() == 'dir1/'

def test_io():
    try:
        dd.swd('tmp/')
        data = [2,0,1,7]
        n = 8
        x = list(range(n))
        y = [random.randint(0,5) for _ in range(n)]
        s = 'filename'
        dd.save(s, n, x=x, y=y)
        assert os.path.isfile('tmp/filename.pkl')

        d = dd.load(s)
        print(d)
        assert (d[0] == (n,))
        assert (d[1]['x'] == x)
        assert (d[1]['y'] == y)
    finally:
        try: 
            os.remove('tmp/filename.pkl')
            os.rmdir('tmp')
        except OSError:
            pass 

if __name__=='__main__':
    test_wd()
    test_io()