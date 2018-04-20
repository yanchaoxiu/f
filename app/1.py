import json
from flask import Flask
app=Flask(__name__)

data={
        'code':0,
        'msg':'OK',
        'data':{
            'name':'tony',
            'age':22
            }
        }

@app.route('/test/api',methods=['POST'])
def test_api_handler():
    return json.dumps(data)


@app.route('/test')
def test_handler():
    return "hello world"


if __name__=='__main__':
    app.run(port=6666)


# import run
# import unittest
#
# class TestDemo(unittest.TestCase):
#     def setUpClass(self):
#         self.app=run.app.test_client()
#
#     def test_test(self):
#         ret=self.app.get('/test')
#         ret=ret.data.decode('utf-8')
#         assert "hello world"==ret
#         assert 'hello' in ret
#     def test_api_demo(self):
#         ret=self.app.post('/test/api')
#         ret=ret.data.decode('utf-8')
#         assert 'name' in ret
#
# if __name__=='__main__':
#     unittest.main()
