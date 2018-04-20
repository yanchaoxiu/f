
import run
import unittest

class TestDemo(unittest.TestCase):
    def setUpClass(self):
        self.app=run.app.test_client()

    def test_test(self):
        ret=self.app.get('/test')
        ret=ret.data.decode('utf-8')
        assert "hello world"==ret
        assert 'hello' in ret
    def test_api_demo(self):
        ret=self.app.post('/test/api')
        ret=ret.data.decode('utf-8')
        assert 'name' in ret

if __name__=='__main__':
    unittest.main()
