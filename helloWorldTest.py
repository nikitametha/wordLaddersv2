import unittest
from helloWorld import sayHello

class testHello(unittest.TestCase):
    def test_msg(self):
        sayHelloObj = sayHello()
        self.assertEqual(sayHelloObj.msg, 'Hello World!')

if __name__ == '__main__':
    unittest.main()