import os
import requests  # 未使用的导入，会触发flake8 F401错误

def add(a, b):
    return a + b

def multiply(a,b): # 逗号后缺少空格，会触发E231错误
    return a * b

def divide(a, b):
    if b == 0
        raise ValueError("Cannot divide by zero") # 缺少冒号，会触发SyntaxError
    return a / b
