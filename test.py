import re

def test():
    pattern = re.compile(r'^http')
    m = pattern.match('http://www.baidu.com')
    n = pattern.match('hta')
    print(m)
    print(n)
    return