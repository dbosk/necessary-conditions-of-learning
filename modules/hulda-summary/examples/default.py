class Test:
    def __init__(self):
        print("konstruktor för Test")

def test_funk2(default=1):
    default += 1
    print(default)

def test_funk(default=Test()):
    print("test_funk anropad")

def append_element(lst=[], element=1):
    lst.append(element)
    return lst
