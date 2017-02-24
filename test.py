import work
import random
import os

def test_wd():
    assert work.wd() == 'tmp/'
    work.swd('dir1')
    assert work.wd() == 'dir1/'

def test_io():
    try:
        work.swd('tmp/')
        data = [2,0,1,7]
        n = 8
        x = list(range(n))
        y = [random.randint(0,5) for _ in range(n)]
        s = 'filename'
        work.save(s, n, x=x, y=y)
        assert os.path.isfile('tmp/filename.pkl')

        d = work.load(s)
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