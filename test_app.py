from app import add, multiply, divide

def test_add():
    assert add(2, 3) == 5

def test_multiply():
    assert multiply(3, 4) == 12

def test_divide():
    assert divide(10, 2) == 5
    # 下面这个测试会失败，因为没有捕获异常
    assert divide(10, 0) == 0
