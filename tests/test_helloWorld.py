import pytest
import src.helloWorld as hw

def test_msg():
    sayHelloObj = hw.sayHello()
    assert sayHelloObj == 'Hello World!'